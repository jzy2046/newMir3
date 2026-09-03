# -*- coding: utf-8 -*-
import sys
from Globals import *
import collections
import clr
clr.AddReference("Library")
clr.AddReference('System')
from Library import *
import NpcEvent
from Defines import *
import PlayerEvent
import Server
import Utils.Colors as Colors
import Server.Envir.SEnvir as SEnvir
from Utils import ServerUtils
from Npc import *
from Npc.商店列表 import *
import datetime

# 导入回收配置
from Npc.其他.回收配置 import RECYCLE_EQUIPMENT, RECYCLE_REWARDS

# 菜单ID定义
MAIN_MENU = 100      # 主菜单ID，避免与传送ID冲突

# 武器回收开关变量 - 改为个人变量
# RECYCLE_ENABLED = True  # 删除全局变量

# 定义传送点数据
TELEPORT_DATA = {
    # 城镇传送(金币)
    "town": {
        1: {"cost": 0, "map": 7, "x": 400, "y": 125},    # 道馆
        2: {"cost": 0, "map": 6, "x": 226, "y": 177},    # 银杏
        3: {"cost": 0, "map": 5, "x": 458, "y": 223},    # 边境
        4: {"cost": 0, "map": 1, "x": 450, "y": 390},    # 比奇
        5: {"cost": 0, "map": 24, "x": 307, "y": 221},   # 毒蛇
        6: {"cost": 10000, "map": 25, "x": 218, "y": 157}, # 潘夜岛
        7: {"cost": 0, "map": 57, "x": 192, "y": 577},   # 失乐园
        8: {"cost": 10000, "map": 55, "x": 288, "y": 238}, # 诺玛
        9: {"cost": 10000, "map": 33, "x": 181, "y": 135}, # 绿洲
        10: {"cost": 10000, "map": 27, "x": 433, "y": 81}, # 沙漠土城
        11: {"cost": 10000, "map": 37, "x": 200, "y": 288}, # 盟重土城
        12: {"cost": 10000, "map": 1, "x": 378, "y": 307}, # 比奇买马
        13: {"cost": 10000, "map": 6, "x": 248, "y": 239}, # 银杏加点
        14: {"cost": 10000, "map": 50, "x": 345, "y": 327} # 盟重土城
    },
    # 危险地图传送(金币)
    "danger": {
        15: {"cost": 30000, "map": 77, "x": 74, "y": 72},   # 沃玛神殿
        16: {"cost": 30000, "map": 170, "x": 203, "y": 201}, # 石阁寺庙
        17: {"cost": 30000, "map": 149, "x": 159, "y": 167}, # 万年峡谷
        18: {"cost": 30000, "map": 270, "x": 51, "y": 283},  # 赤月峡谷
        19: {"cost": 30000, "map": 299, "x": 127, "y": 172}, # 潘夜石窟
        20: {"cost": 30000, "map": 285, "x": 135, "y": 180}, # 潘夜神殿
        21: {"cost": 30000, "map": 340, "x": 173, "y": 223}, # 真天宫
        22: {"cost": 30000, "map": 356, "x": 119, "y": 109}, # 黑度宫
        23: {"cost": 30000, "map": 362, "x": 38, "y": 147},  # 
        24: {"cost": 30000, "map": 375, "x": 283, "y": 278}, # 
        25: {"cost": 30000, "map": 26, "x": 170, "y": 135}  # 祖玛神殿
    }
}

def handle_teleport(Sender, teleport_type, menu_id):
    """处理传送逻辑"""
    data = TELEPORT_DATA.get(teleport_type, {}).get(menu_id)
    if not data:
        return False
    
    cost = data.get("cost", 0)
    
    # 检查金币是否足够
    if Sender.Gold < cost:
        return """你没有足够的金币，无法传送。
            
            [关闭:0]"""
    
    # 扣除金币
    SubGold(Sender, cost)
    
    # 执行传送
    Sender.TeleportByMapIndex(data["map"], data["x"], data["y"])
    return None

def OnClick(args):
    Self = args[0]
    Sender = args[1]
    Menu = args[2]
    Dict = {}
    say = ""
    
    # 处理传送
    if Menu in TELEPORT_DATA["town"]:
        say = handle_teleport(Sender, "town", Menu)
    elif Menu in TELEPORT_DATA["danger"]:
        say = handle_teleport(Sender, "danger", Menu)
    
    elif Menu == 511:  # 一键售卖菜单
        say = """你好吗。

        [购买:512]药品
        
        [出售:513]物品
        
        [结束:0]"""
    
    elif Menu == 512:  # 购买菜单
        Dict['Goods'] = goods
        Dict['Types'] = types
        Dict['DialogType'] = NPCDialogType.BuySell
        Dict['CastleName'] = '沙巴克'
        say = """你需要什么东西？
        
        [前一步:99]"""
    
    elif Menu == 513:  # 出售菜单
        Dict['Types'] = types
        Dict['DialogType'] = NPCDialogType.RootSell
        say = """请把要出售的物品交给我。
        
        [前一步:99]"""
    
    elif Menu == 600:  # 装备回收开关
        # 获取当前玩家的个人回收开关状态
        recycle_enabled = PlayerGetV(Sender, GV_PLAYER_RECYCLE_ENABLED)
        # 切换状态
        new_recycle_enabled = not recycle_enabled
        # 更新个人变量
        PlayerSetV(Sender, GV_PLAYER_RECYCLE_ENABLED, new_recycle_enabled)
        # 重新显示主菜单，这样状态会自动刷新
        status = "开启" if new_recycle_enabled else "关闭"
        status_color = "0xff00ff00" if new_recycle_enabled else "0xffff0000"
        
        say = """           欢迎来到  <font color=\"0xff00ff00\">肝帝传奇3</font>  
        
        
<font color=\"0xff00ff00\">城镇传送：免费</font>

[道馆:1]   [比奇:4]   [银杏:2]    [边境:3]    [毒蛇:5]   [失乐园:7]  

<font color=\"0xff00ff00\">城镇传送：费用10000金币</font>

[银杏加点:13]  [比奇买马:12] [潘夜岛:8]   [诺玛:9]   [绿洲:10]   
[沙漠土城:11]  [盟重土城:14]

<font color=\"0xff00ff00\">危险地图传送：费用30000金币</font>

[沃玛神殿:15] [石阁寺庙:16] [万年峡谷:17]
[赤月峡谷:18] [潘夜石窟:19] [潘夜神殿:20]
[祖玛神殿:25] [真天宫:21] [黑度宫:22]

<font color=\"0xff00ff00\">快捷功能</font>

[一键售卖:511]

<font color=\"0xff00ff00\">装备回收</font>

[自动回收开关:600]  [手动回收:602]  [回收列表:603]  <font color=\"{}\">自动回收状态：{}</font>
        
        """.format(status_color, status)
    

    
    elif Menu == 603:  # 回收列表主菜单
        # 生成回收列表分类菜单
        say = """<font color=\"0xff00ff00\">装备回收列表</font>

<font color=\"0xffffff00\">请选择要查看的装备类型：</font>

"""
        # 按类型分组统计装备
        equipment_by_type = {}
        for equipment in RECYCLE_EQUIPMENT:
            if equipment in RECYCLE_REWARDS:
                reward = RECYCLE_REWARDS[equipment]
                equipment_type = reward.get("type", "其他")
                if equipment_type not in equipment_by_type:
                    equipment_by_type[equipment_type] = []
                equipment_by_type[equipment_type].append((equipment, reward["gold"]))
        
        # 装备类型中文映射
        type_chinese = {
            "Weapon": "武器",
            "Armour": "防具",
            "Ring": "戒指",
            "Necklace": "项链",
            "Bracelet": "手镯",
            "Helmet": "头盔",
            "Shoes": "鞋子",
            "Book": "书籍",
            "其他": "其他"
        }
        
        # 生成类型菜单
        menu_id = 610  # 从610开始分配子菜单ID
        equipment_type_list = list(equipment_by_type.keys())  # 保存装备类型列表，确保顺序一致
        for equipment_type in equipment_type_list:
            chinese_name = type_chinese.get(equipment_type, equipment_type)
            say += "[{}:{}]  ".format(chinese_name, menu_id)
            menu_id += 1
        
        say += """

<font color=\"0xffffff00\">说明：</font>
- 点击装备类型查看该类型的所有可回收装备
- 点击"手动回收"按钮可一键回收所有可回收装备
- 回收后将获得对应金币奖励
- 装备回收后不可恢复，请谨慎操作

[返回主菜单:{}]""".format(MAIN_MENU)
    
    elif Menu >= 610 and Menu < 620:  # 装备类型子菜单 (610-619)
        # 获取装备类型
        equipment_types = []
        equipment_by_type = {}
        for equipment in RECYCLE_EQUIPMENT:
            if equipment in RECYCLE_REWARDS:
                reward = RECYCLE_REWARDS[equipment]
                equipment_type = reward.get("type", "其他")
                if equipment_type not in equipment_by_type:
                    equipment_by_type[equipment_type] = []
                equipment_by_type[equipment_type].append((equipment, reward["gold"]))
        
        # 装备类型中文映射
        type_chinese = {
            "Weapon": "武器",
            "Armour": "防具",
            "Ring": "戒指",
            "Necklace": "项链",
            "Bracelet": "手镯",
            "Helmet": "头盔",
            "Shoes": "鞋子",
            "Book": "书籍",
            "其他": "其他"
        }
        
        # 按菜单ID获取装备类型
        menu_id = Menu - 610
        # 使用与主菜单相同的装备类型列表顺序
        equipment_type_list = list(equipment_by_type.keys())
        
        if menu_id < len(equipment_type_list):
            selected_type = equipment_type_list[menu_id]
            items = equipment_by_type[selected_type]
            chinese_name = type_chinese.get(selected_type, selected_type)
            
            say = """<font color=\"0xff00ff00\">{} 回收列表</font>

<font color=\"0xffffff00\">可回收装备及价格：</font>

""".format(chinese_name)
            # 计算最长装备名长度，用于对齐
            max_equipment_length = max(len(equipment) for equipment, _ in items) if items else 0
            max_equipment_length = max(max_equipment_length, 8)  # 最小8字符宽度
            
            # 分页显示，每页最多20个装备
            items_per_page = 20
            total_items = len(items)
            total_pages = (total_items + items_per_page - 1) // items_per_page  # 提前计算总页数
            
            if total_items <= items_per_page:
                # 装备数量不超过20个，直接显示
                for equipment, gold in items:
                    equipment_padded = equipment.ljust(max_equipment_length + 2)
                    gold_str = str(gold)
                    line_text = "<font color=\"0xff00ff00\">{}</font>: <font color=\"0xffffffff\">{:>6}金币</font>".format(equipment_padded, gold_str)
                    say += line_text + "\n"
            else:
                # 装备数量超过20个，显示第一页并生成分页菜单
                first_page_items = items[:items_per_page]
                
                # 显示第一页装备
                for equipment, gold in first_page_items:
                    equipment_padded = equipment.ljust(max_equipment_length + 2)
                    gold_str = str(gold)
                    line_text = "<font color=\"0xff00ff00\">{}</font>: <font color=\"0xffffffff\">{:>6}金币</font>".format(equipment_padded, gold_str)
                    say += line_text + "\n"
                
            # 添加分页导航
            for page in range(1, total_pages + 1):
                if page == 1:
                    say += "[第{}页:{}]  ".format(page, Menu)  # 当前页
                else:
                    # 生成下一页菜单ID，使用装备类型和页码组合
                    # 格式：700 + 装备类型索引 * 10 + 页码
                    equipment_type_index = equipment_type_list.index(selected_type)
                    next_page_menu_id = 700 + equipment_type_index * 10 + page
                    say += "[第{}页:{}]  ".format(page, next_page_menu_id)
                
            say += """

<font color=\"0xffffff00\">说明：</font>
- 点击"手动回收"按钮可一键回收所有可回收装备
- 回收后将获得对应金币奖励
- 装备回收后不可恢复，请谨慎操作

[返回回收列表:603]  [返回主菜单:{}]""".format(MAIN_MENU)
        else:
            say = """<font color=\"0xffff0000\">错误：未找到对应的装备类型</font>

[返回回收列表:603]  [返回主菜单:{}]""".format(MAIN_MENU)
    
    elif Menu >= 700 and Menu < 800:  # 分页菜单 (700-799)
        # 解析菜单ID获取装备类型和页码
        # 格式：700 + 装备类型索引 * 10 + 页码
        menu_offset = Menu - 700
        equipment_type_index = menu_offset // 10
        page_number = menu_offset % 10
        
        if page_number == 0:  # 页码为0表示第10页
            page_number = 10
        
        # 获取装备类型
        equipment_types = []
        equipment_by_type = {}
        for equipment in RECYCLE_EQUIPMENT:
            if equipment in RECYCLE_REWARDS:
                reward = RECYCLE_REWARDS[equipment]
                equipment_type = reward.get("type", "其他")
                if equipment_type not in equipment_by_type:
                    equipment_by_type[equipment_type] = []
                equipment_by_type[equipment_type].append((equipment, reward["gold"]))
        
        # 装备类型中文映射
        type_chinese = {
            "Weapon": "武器",
            "Armour": "防具",
            "Ring": "戒指",
            "Necklace": "项链",
            "Bracelet": "手镯",
            "Helmet": "头盔",
            "Shoes": "鞋子",
            "Book": "书籍",
            "其他": "其他"
        }
        
        # 根据索引获取装备类型
        equipment_type_list = list(equipment_by_type.keys())
        if equipment_type_index < len(equipment_type_list):
            selected_type = equipment_type_list[equipment_type_index]
            items = equipment_by_type[selected_type]
            chinese_name = type_chinese.get(selected_type, selected_type)
            
            # 分页显示
            items_per_page = 20
            total_items = len(items)
            total_pages = (total_items + items_per_page - 1) // items_per_page
            
            if page_number <= total_pages:
                # 计算当前页的装备
                start_idx = (page_number - 1) * items_per_page
                end_idx = min(start_idx + items_per_page, total_items)
                page_items = items[start_idx:end_idx]
                
                say = """<font color=\"0xff00ff00\">{} 回收列表 - 第{}页</font>

<font color=\"0xffffff00\">可回收装备及价格：</font>

""".format(chinese_name, page_number)
                
                # 计算最长装备名长度，用于对齐
                max_equipment_length = max(len(equipment) for equipment, _ in page_items) if page_items else 0
                max_equipment_length = max(max_equipment_length, 8)  # 最小8字符宽度
                
                # 显示当前页装备
                for equipment, gold in page_items:
                    equipment_padded = equipment.ljust(max_equipment_length + 2)
                    gold_str = str(gold)
                    line_text = "<font color=\"0xff00ff00\">{}</font>: <font color=\"0xffffffff\">{:>6}金币</font>".format(equipment_padded, gold_str)
                    say += line_text + "\n"
                
                # 添加分页导航
                for page in range(1, total_pages + 1):
                    if page == page_number:
                        say += "[第{}页:{}]  ".format(page, Menu)  # 当前页
                    else:
                        # 生成其他页面的菜单ID
                        other_page_menu_id = 700 + equipment_type_index * 10 + page
                        say += "[第{}页:{}]  ".format(page, other_page_menu_id)
                
                say += "\n[返回回收列表:603]  [返回主菜单:{}]".format(MAIN_MENU)
            else:
                say = """<font color=\"0xffff0000\">错误：页码超出范围</font>

[返回回收列表:603]  [返回主菜单:{}]""".format(MAIN_MENU)
        else:
            say = """<font color=\"0xffff0000\">错误：装备类型索引超出范围</font>

[返回回收列表:603]  [返回主菜单:{}]""".format(MAIN_MENU)
    
    elif Menu == 602:  # 手动装备回收
        # 执行手动回收
        print("玩家 {} 点击了手动回收按钮".format(Sender.Character.CharacterName))
        try:
            ExecuteEquipmentRecycleForSender(Sender)
            # 重新显示主菜单，不跳转页面
            recycle_enabled = PlayerGetV(Sender, GV_PLAYER_RECYCLE_ENABLED)
            status = "开启" if recycle_enabled else "关闭"
            status_color = "0xff00ff00" if recycle_enabled else "0xffff0000"
            
            say = """           欢迎来到  <font color=\"0xff00ff00\">肝帝传奇3</font>  
            
            
<font color=\"0xff00ff00\">城镇传送：免费</font>

[道馆:1]   [比奇:4]   [银杏:2]    [边境:3]    [毒蛇:5]   [失乐园:7]  

<font color=\"0xff00ff00\">城镇传送：费用10000金币</font>

[银杏加点:13]  [比奇买马:12] [潘夜岛:8]   [诺玛:9]   [绿洲:10]   
[沙漠土城:11]  [盟重土城:14]

<font color=\"0xff00ff00\">危险地图传送：费用30000金币</font>

[沃玛神殿:15] [石阁寺庙:16] [万年峡谷:17]
[赤月峡谷:18] [潘夜石窟:19] [潘夜神殿:20]
[祖玛神殿:25] [真天宫:21] [黑度宫:22]

<font color=\"0xff00ff00\">快捷功能</font>

[一键售卖:511]

<font color=\"0xff00ff00\">装备回收</font>

[自动回收开关:600]  [手动回收:602]  [回收列表:603]  <font color=\"{}\">自动回收状态：{}</font>
        
        """.format(status_color, status)
        except Exception as e:
            print("手动回收执行失败: {}".format(e))
            # 重新显示主菜单，不跳转页面
            recycle_enabled = PlayerGetV(Sender, GV_PLAYER_RECYCLE_ENABLED)
            status = "开启" if recycle_enabled else "关闭"
            status_color = "0xff00ff00" if recycle_enabled else "0xffff0000"
            
            say = """           欢迎来到  <font color=\"0xff00ff00\">肝帝传奇3</font>  
            
            
<font color=\"0xff00ff00\">城镇传送：免费</font>

[道馆:1]   [比奇:4]   [银杏:2]    [边境:3]    [毒蛇:5]   [失乐园:7]  

<font color=\"0xff00ff00\">城镇传送：费用10000金币</font>

[银杏加点:13]  [比奇买马:12] [潘夜岛:8]   [诺玛:9]   [绿洲:10]   
[沙漠土城:11]  [盟重土城:14]

<font color=\"0xff00ff00\">危险地图传送：费用30000金币</font>

[沃玛神殿:15] [石阁寺庙:16] [万年峡谷:17]
[赤月峡谷:18] [潘夜石窟:19] [潘夜神殿:20]
[祖玛神殿:25] [真天宫:21] [黑度宫:22]

<font color=\"0xff00ff00\">快捷功能</font>

[一键售卖:511]

<font color=\"0xff00ff00\">装备回收</font>

[自动回收开关:600]  [手动回收:602]  [回收列表:603]  <font color=\"{}\">自动回收状态：{}</font>
        
        """.format(status_color, status)
    
        
    # 主菜单 (Menu == 0 是初始打开，Menu == MAIN_MENU 是返回主菜单)
    elif Menu == 0 or Menu == MAIN_MENU:
        # 获取当前回收状态
        recycle_enabled = PlayerGetV(Sender, GV_PLAYER_RECYCLE_ENABLED)
        status = "开启" if recycle_enabled else "关闭"
        status_color = "0xff00ff00" if recycle_enabled else "0xffff0000"  # 绿色表示开启，红色表示关闭
        
        say = """           欢迎来到  <font color=\"0xff00ff00\">肝帝传奇3</font>  
        
        
<font color=\"0xff00ff00\">城镇传送：免费</font>

[道馆:1]   [比奇:4]   [银杏:2]    [边境:3]    [毒蛇:5]   [失乐园:7]  

<font color=\"0xff00ff00\">城镇传送：费用10000金币</font>

[银杏加点:13]  [比奇买马:12] [潘夜岛:8]   [诺玛:9]   [绿洲:10]   
[沙漠土城:11]  [盟重土城:14]

<font color=\"0xff00ff00\">危险地图传送：费用30000金币</font>

[沃玛神殿:15] [石阁寺庙:16] [万年峡谷:17]
[赤月峡谷:18] [潘夜石窟:19] [潘夜神殿:20]
[祖玛神殿:25] [真天宫:21] [黑度宫:22]

<font color=\"0xff00ff00\">快捷功能</font>

[一键售卖:511]

<font color=\"0xff00ff00\">装备回收</font>

[自动回收开关:600]  [手动回收:602]  [回收列表:603]  <font color=\"{}\">自动回收状态：{}</font>
        
        """.format(status_color, status)
    
    # 如果没有处理结果(如成功传送)，则返回None
    if say is None:
        return None
    
    Dict['Say'] = say
    return Dict

def ExecuteEquipmentRecycleForSender(Sender):
    """只针对当前Sender执行装备回收功能"""
    import datetime
    import time
    import os
    
    current_time = datetime.datetime.now()
    player_name = Sender.Character.CharacterName
    
    # 记录到专门的回收日志文件
    log_message = "[{}] 开始检查玩家 {} 的回收状态".format(current_time.strftime("%Y-%m-%d %H:%M:%S"), player_name)
    print(log_message)
    
    # 写入回收日志文件
    try:
        with open("equipment_recycler.log", "a", encoding="utf-8") as f:
            f.write(log_message + "\n")
    except Exception as e:
        print("写入回收日志失败: {}".format(e))
    
    last_recycle_timestamp = PlayerGetV(Sender, GV_PLAYER_LAST_RECYCLE_TIME)
    print("玩家 {} 的上次回收时间戳: {}".format(player_name, last_recycle_timestamp))
    
    # 手动回收没有间隔限制，每次点击都执行
    print("玩家 {} 执行手动回收".format(player_name))
    
    recycled_count = 0
    gold_given = 0
    
    print("开始检查玩家 {} 的装备:".format(player_name))
    print("回收列表中共有 {} 种装备".format(len(RECYCLE_EQUIPMENT)))
    for equipment in RECYCLE_EQUIPMENT:
        try:
            equipment_count = int(Sender.GetItemCount(equipment))
            print("  - {}: {}个".format(equipment, equipment_count))
            if equipment_count > 0:
                print("发现玩家 {} 有 {} 个 {}".format(player_name, equipment_count, equipment))
                # 检查装备是否在回收字典中
                if equipment in RECYCLE_REWARDS:
                    Sender.TakeItem(equipment, equipment_count)
                    reward = RECYCLE_REWARDS.get(equipment, {"gold": 1000})
                    gold_reward = reward["gold"] * equipment_count
                    # 给予金币
                    Sender.GiveItem("金币", gold_reward)
                    recycled_count += equipment_count
                    gold_given += gold_reward
                    # 发送每种装备的回收消息
                    try:
                        Sender.Connection.ReceiveChat("成功回收{}件装备，获得金币{}".format(equipment_count, gold_reward), MessageType.System)
                    except:
                        print("发送回收消息失败，但回收操作已完成")
                    print("已回收 {} 个 {}，给予 {} 金币".format(equipment_count, equipment, gold_reward))
                else:
                    skip_message = "[{}] 装备 {} 不在回收列表中，跳过".format(current_time.strftime("%Y-%m-%d %H:%M:%S"), equipment)
                    print(skip_message)
                    try:
                        with open("equipment_recycler.log", "a", encoding="utf-8") as f:
                            f.write(skip_message + "\n")
                    except:
                        pass
        except Exception as e:
            error_message = "[{}] 回收装备 {} 时发生错误: {}".format(current_time.strftime("%Y-%m-%d %H:%M:%S"), equipment, e)
            print(error_message)
            try:
                with open("equipment_recycler.log", "a", encoding="utf-8") as f:
                    f.write(error_message + "\n")
            except:
                pass
            continue  # 继续处理下一个武器
    
    if recycled_count > 0:
        # 更新回收时间
        current_timestamp = time.time()
        PlayerSetV(Sender, GV_PLAYER_LAST_RECYCLE_TIME, current_timestamp)
        # 发送总计消息
        Sender.Connection.ReceiveChat("成功回收{}件装备，获得金币{}".format(recycled_count, gold_given), MessageType.System)
        
            # 记录回收完成日志
    success_message = "[{}] 玩家 {} 回收完成，总计回收 {} 件装备，给予 {} 金币".format(
        current_time.strftime("%Y-%m-%d %H:%M:%S"), player_name, recycled_count, gold_given)
    print(success_message)
    try:
        with open("weapon_recycler.log", "a", encoding="utf-8") as f:
            f.write(success_message + "\n")
    except:
        pass
    
    # 检查玩家包裹中是否有不在回收列表中的装备
    print("检查玩家包裹中是否有不在回收列表中的装备...")
    try:
        # 这里可以添加检查玩家包裹中所有装备的逻辑
        # 由于没有直接的API获取所有装备，我们只能通过已知的装备名称来检查
        print("无法直接检查所有装备，请手动确认装备名称")
    except Exception as e:
        print("检查包裹装备时发生错误: {}".format(e))
    
    if recycled_count > 0:
        # 更新回收时间
        current_timestamp = time.time()
        PlayerSetV(Sender, GV_PLAYER_LAST_RECYCLE_TIME, current_timestamp)
        # 发送总计消息
        Sender.Connection.ReceiveChat("成功回收{}件装备，获得金币{}".format(recycled_count, gold_given), MessageType.System)
        
        # 记录回收完成日志
        success_message = "[{}] 玩家 {} 回收完成，总计回收 {} 件装备，给予 {} 金币".format(
            current_time.strftime("%Y-%m-%d %H:%M:%S"), player_name, recycled_count, gold_given)
        print(success_message)
        try:
            with open("equipment_recycler.log", "a", encoding="utf-8") as f:
                f.write(success_message + "\n")
        except:
            pass
    else:
        no_weapon_message = "[{}] 玩家 {} 没有可回收的武器".format(current_time.strftime("%Y-%m-%d %H:%M:%S"), player_name)
        print(no_weapon_message)
        try:
            with open("weapon_recycler.log", "a", encoding="utf-8") as f:
                f.write(no_weapon_message + "\n")
        except:
            pass

def TestRecycleForSender(Sender):
    """手动测试回收功能 - 只针对当前Sender"""
    print("TestRecycleForSender: 清空当前玩家的回收时间记录")
    try:
        PlayerSetV(Sender, GV_PLAYER_LAST_RECYCLE_TIME, 0)
        print("TestRecycleForSender: 已清空玩家 {} 的回收时间记录".format(Sender.Character.CharacterName))
    except Exception as e:
        print("TestRecycleForSender: 清空回收时间记录失败: {}".format(e))
    
    print("TestRecycleForSender: 调用ExecuteEquipmentRecycleForSender")
    ExecuteEquipmentRecycleForSender(Sender)
    print("TestRecycleForSender: 执行完成")

def ImmediateRecycleForSender(Sender):
    """立即回收测试 - 忽略时间间隔，只针对当前Sender"""
    print("ImmediateRecycleForSender: 开始立即回收测试")
    
    # 临时禁用时间间隔检查
    try:
        original_time = PlayerGetV(Sender, GV_PLAYER_LAST_RECYCLE_TIME)
        PlayerSetV(Sender, GV_PLAYER_LAST_RECYCLE_TIME, 0)
        
        ExecuteEquipmentRecycleForSender(Sender)
        print("ImmediateRecycleForSender: 立即回收测试完成")
        
        # 恢复原来的时间记录
        PlayerSetV(Sender, GV_PLAYER_LAST_RECYCLE_TIME, original_time)
    except Exception as e:
        print("ImmediateRecycleForSender: 立即回收测试失败: {}".format(e))

def TestMessageForSender(Sender):
    """测试消息发送功能 - 只针对当前Sender"""
    print("TestMessageForSender: 开始测试消息发送")
    try:
        Sender.Connection.ReceiveChat("测试消息发送功能", MessageType.System)
        print("测试消息发送成功给玩家: {}".format(Sender.Character.CharacterName))
    except Exception as e:
        print("测试消息发送失败给玩家: {} - {}".format(Sender.Character.CharacterName, e))

def GiveTestWeaponsForSender(Sender):
    """给当前Sender测试武器"""
    print("GiveTestWeaponsForSender: 开始给玩家测试武器")
    try:
        # 给玩家一些测试武器
        Sender.GiveItem("匕首", 1)
        Sender.GiveItem("井中月", 1)
        Sender.GiveItem("银蛇", 1)
        print("测试武器发放成功给玩家: {}".format(Sender.Character.CharacterName))
        Sender.Connection.ReceiveChat("已发放测试武器：匕首、井中月、银蛇各1个", MessageType.System)
        
        # 测试TakeItem功能
        print("测试TakeItem功能...")
        if Sender.GetItemCount("匕首") > 0:
            print("玩家有匕首，尝试回收1个")
            Sender.TakeItem("匕首", 1)
            print("TakeItem执行完成")
            Sender.Connection.ReceiveChat("测试：已回收1个匕首", MessageType.System)
        else:
            print("玩家没有匕首")
            Sender.Connection.ReceiveChat("测试：玩家没有匕首", MessageType.System)
            
    except Exception as e:
        print("测试武器发放失败给玩家: {} - {}".format(Sender.Character.CharacterName, e))
        Sender.Connection.ReceiveChat("测试武器发放失败: {}".format(str(e)), MessageType.System)

def TestPlayerVarsForSender(Sender):
    """测试玩家个人变量 - 只针对当前Sender"""
    print("TestPlayerVarsForSender: 开始测试玩家个人变量")
    try:
        player_name = Sender.Character.CharacterName
        # 设置不同的测试值
        test_value = hash(player_name) % 1000  # 根据玩家名生成不同的测试值
        PlayerSetV(Sender, GV_PLAYER_LAST_RECYCLE_TIME, test_value)
        print("玩家 {} 设置变量值: {}".format(player_name, test_value))
        
        # 读取变量值
        read_value = PlayerGetV(Sender, GV_PLAYER_LAST_RECYCLE_TIME)
        print("玩家 {} 读取变量值: {}".format(player_name, read_value))
        
        if read_value == test_value:
            print("玩家 {} 个人变量测试成功".format(player_name))
            Sender.Connection.ReceiveChat("个人变量测试成功", MessageType.System)
        else:
            print("玩家 {} 个人变量测试失败，设置值: {}, 读取值: {}".format(player_name, test_value, read_value))
            Sender.Connection.ReceiveChat("个人变量测试失败", MessageType.System)
            
    except Exception as e:
        print("TestPlayerVarsForSender失败: {}".format(e))

# 类型为 Enums里的普通类
types = [ItemType.Nothing]
# 商品列表 '商品名称' 商品价格比例,固定格式为float(1.5)比例倍数
goods = collections.OrderedDict(yaodiangoodslist)

NpcEvent.add_listener(211, "OnClick", OnClick)