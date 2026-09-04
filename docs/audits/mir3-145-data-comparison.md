# 传奇3 光通 1.45 数据完整对比报告

## 口径与安全说明

- 仅以官方正式名称及其显式别名做 Unicode NFKC 与 Unicode 空白归一化后的精确匹配；不做繁简转换或模糊匹配。
- 未匹配或证据版本不确定均标为“版本不确定”，不得仅因缺少资料建议删除；仅有明确后续版本排除证据的条目进入删除候选。
- 本报告为只读快照比对，未修改 System.db、快照、官方参考或来源文档。

## 快照绑定信息

| System.db逻辑路径 | SHA-256 | exportedAt |
| --- | --- | --- |
| Database/System.db | 46fe189e57842d408efc5fa974e1de66a5eb36f0aae62a5d49109064fe1e8c90 | 2026-09-04T07:01:47.474631+00:00 |

## 数量汇总

| 类型 | 本服快照数 | 官方参考数 | 确认保留 | 疑似同物异名 | 建议删除 | 版本不确定 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 物品 | 3903 | 81 | 54 | 0 | 0 | 3849 |
| 怪物 | 611 | 11 | 7 | 0 | 0 | 604 |
| 套装 | 97 | 4 | 0 | 0 | 0 | 97 |

## 来源表

- 来源文档逻辑路径：`docs/research/mir3-145-sources.md`
- 来源文档 SHA-256：`b976e2b00f9027637c7f6b886ca74f9a972b13a859da263d41ba249d3d777a3b`

| 来源ID | 标题 | 链接 | 级别 | 版本 | 分类 | 定位 | 说明 |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| official-145-release | 光通《传奇3》官方网站 V1.45 上线页（请求 2004-04-16，Wayback 当前解析至 2004-04-18 快照） | https://web.archive.org/web/20040416063846id_/http://www.mir3.com.cn/ | 1 | 1.45 | version-history | Wayback 当前解析的 2004-04-18 首页“我的《传奇3》我做主 V1.45版真情奉献”区块，含“4月15日上线的V1.45版”及更新摘要。 | 请求的 Wayback 2004-04-16 快照当前重定向至 2004-04-18 快照；该官网正文写明 4 月 15 日上线 V1.45。只用于版本边界，不为未列名的物品、怪物或套装背书。 |
| official-145-skill-activity | 光通《闯诺玛・巧拼字・夺技能》活动攻略（2004-04-29 存档） | https://web.archive.org/web/20040429013452id_/http://www.mir3.com.cn/column/v1.4/act_book2.htm | 1 | 1.45 | items, version-history | “第一步闯诺玛”“第二步巧拼字”“第三步夺技能”三段；末段明确写“V1.45版中”。 | 光通官网 V1.45 活动正文直接列出诺玛遗址出现的任务道具、兑换书名和奖励物品。 |
| official-145-items-ring | 光通 V1.45 专区戒指物品表（2004-06-03 存档） | https://web.archive.org/web/20040603222737id_/http://www.mir3.com.cn/column/v1.4/item_ring.htm | 1 | 1.45 | items | 页面“战士戒指”“法师戒指”“道士戒指”三个表格；顶部为该官方专区的 top145 标识。 | 光通官网 V1.45 专区的上线后存档；表格直接列出战士、法师、道士戒指及元素括号名称。 |
| official-145-items-bracelet | 光通 V1.45 专区手镯物品表（2004-06-05 存档） | https://web.archive.org/web/20040605012353id_/http://www.mir3.com.cn/column/v1.4/item_bracelet.htm | 1 | 1.45 | items | 页面“战士手镯”“法师手镯”“道士手镯”“共用手镯”表格；顶部为该官方专区的 top145 标识。 | 光通官网 V1.45 专区的上线后存档；表格直接列出战士、法师、道士和共用手镯。 |
| official-145-items-amulet | 光通 V1.45 专区项链物品表（2004-06-05 存档） | https://web.archive.org/web/20040605013351id_/http://www.mir3.com.cn/column/v1.4/item_amulet.htm | 1 | 1.45 | items | 页面“战士项链”“法师项链”“道士项链”“共用项链”表格；顶部为该官方专区的 top145 标识。 | 光通官网 V1.45 专区的上线后存档；表格直接列出战士、法师、道士和共用项链。 |
| official-145-monsters-nooma | 光通 V1.45 专区诺玛怪物资料（2004-06-03 存档） | https://web.archive.org/web/20040603224208id_/http://www.mir3.com.cn/column/v1.4/mon.htm | 1 | 1.45 | monsters | “一、诺玛遗址怪物”与“二、诺玛平民”两段的名称和说明表；顶部为该官方专区的 top145 标识。 | 光通官网 V1.45 专区的上线后怪物目录；正文按“诺玛遗址怪物”和“诺玛平民”分组。 |
| s17173-20040415-v145-release | 以人为本 《传奇3》V1.45版正式上线！（17173，2004-04-15） | https://news.17173.com/content/2004-4-15/n479_395577.html | 2 | 1.45 | version-history | 正文第 1 段的“4月15日…V1.45版隆重上线”及末段“4月15日至4月23日…升级维护”。 | 同期大型游戏站新闻正文带时间戳，记载光通于 2004-04-15 上线 V1.45、并在 4 月 15 日至 23 日分批升级；仅作版本时间线交叉核验。 |
| s17173-kr-20040316-update-plan | 韩服 3月16日 更新计划介绍（17173 同期译整） | https://mir3.17173.com/up/2004316up.htm | 2 | 韩国3月16日更新计划 | items, sets | “3.新套装”“金刚套装”“祈祷套装”表格，逐项列出五件组成和套装说明。 | 正文明确是“韩服”更新计划，不证明中国光通 1.45 已部署；只为 uncertain-version 套装和部件保留其逐项正文证据。 |
| s17173-20030820-moxue-set | 全面理性剖析魔血套装（17173，2003-08-20） | https://mir3.17173.com/content/2003-8-20/n751_667503.html?_platform=PC | 2 | 2003-08-20（版本未明） | items, sets | 正文第 1 节 a、b、c 三项与“3个全部佩带”说明。 | 同期正文有日期并逐项写出魔血戒指、手镯、项链；它早于 1.45 且没有证明持续适用，故只能支持 uncertain-version。 |

## 官方物品完整表

| 正式名 | 别名 | 类别/区域/组成 | 状态 | 引入版本 | 来源ID | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| 师承戒指 |  | 首饰-战士戒指 | confirmed-145 | — | official-145-items-ring | 官方专区“战士戒指”表中的基础名称。 |
| 师承戒指（火） |  | 首饰-战士戒指 | confirmed-145 | — | official-145-items-ring | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 师承戒指（冰） |  | 首饰-战士戒指 | confirmed-145 | — | official-145-items-ring | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 师承戒指（风） |  | 首饰-战士戒指 | confirmed-145 | — | official-145-items-ring | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 师承戒指（雷） |  | 首饰-战士戒指 | confirmed-145 | — | official-145-items-ring | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 师承戒指（神圣） |  | 首饰-战士戒指 | confirmed-145 | — | official-145-items-ring | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 师承戒指（暗黑） |  | 首饰-战士戒指 | confirmed-145 | — | official-145-items-ring | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 龙马戒指 |  | 首饰-法师戒指 | confirmed-145 | — | official-145-items-ring | 官方专区“法师戒指”表中的基础名称。 |
| 龙马戒指（火） |  | 首饰-法师戒指 | confirmed-145 | — | official-145-items-ring | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 龙马戒指（冰） |  | 首饰-法师戒指 | confirmed-145 | — | official-145-items-ring | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 龙马戒指（风） |  | 首饰-法师戒指 | confirmed-145 | — | official-145-items-ring | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 龙马戒指（雷） |  | 首饰-法师戒指 | confirmed-145 | — | official-145-items-ring | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 青云戒指 |  | 首饰-道士戒指 | confirmed-145 | — | official-145-items-ring | 官方专区“道士戒指”表中的基础名称。 |
| 青云戒指（神圣） |  | 首饰-道士戒指 | confirmed-145 | — | official-145-items-ring | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 青云戒指（暗黑） |  | 首饰-道士戒指 | confirmed-145 | — | official-145-items-ring | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 青云戒指（幻影） |  | 首饰-道士戒指 | confirmed-145 | — | official-145-items-ring | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 金棱手镯 |  | 首饰-战士手镯 | confirmed-145 | — | official-145-items-bracelet | 官方专区“战士手镯”表中的基础名称。 |
| 金棱手镯（火） |  | 首饰-战士手镯 | confirmed-145 | — | official-145-items-bracelet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 金棱手镯（冰） |  | 首饰-战士手镯 | confirmed-145 | — | official-145-items-bracelet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 金棱手镯（风） |  | 首饰-战士手镯 | confirmed-145 | — | official-145-items-bracelet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 金棱手镯（雷） |  | 首饰-战士手镯 | confirmed-145 | — | official-145-items-bracelet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 金棱手镯（神圣） |  | 首饰-战士手镯 | confirmed-145 | — | official-145-items-bracelet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 金棱手镯（暗黑） |  | 首饰-战士手镯 | confirmed-145 | — | official-145-items-bracelet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 思过手镯 |  | 首饰-法师手镯 | confirmed-145 | — | official-145-items-bracelet | 官方专区“法师手镯”表中的基础名称。 |
| 思过手镯（火） |  | 首饰-法师手镯 | confirmed-145 | — | official-145-items-bracelet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 思过手镯（冰） |  | 首饰-法师手镯 | confirmed-145 | — | official-145-items-bracelet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 思过手镯（风） |  | 首饰-法师手镯 | confirmed-145 | — | official-145-items-bracelet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 思过手镯（雷） |  | 首饰-法师手镯 | confirmed-145 | — | official-145-items-bracelet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 世尊手镯 |  | 首饰-道士手镯 | confirmed-145 | — | official-145-items-bracelet | 官方专区“道士手镯”表中的基础名称。 |
| 世尊手镯（神圣） |  | 首饰-道士手镯 | confirmed-145 | — | official-145-items-bracelet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 世尊手镯（暗黑） |  | 首饰-道士手镯 | confirmed-145 | — | official-145-items-bracelet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 世尊手镯（幻影） |  | 首饰-道士手镯 | confirmed-145 | — | official-145-items-bracelet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 心念手镯 |  | 首饰-共用手镯 | confirmed-145 | — | official-145-items-bracelet | 官方专区“共用手镯”表中单列的名称。 |
| 破荒项链 |  | 首饰-战士项链 | confirmed-145 | — | official-145-items-amulet | 官方专区“战士项链”表中的基础名称。 |
| 破荒项链（火） |  | 首饰-战士项链 | confirmed-145 | — | official-145-items-amulet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 破荒项链（冰） |  | 首饰-战士项链 | confirmed-145 | — | official-145-items-amulet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 破荒项链（风） |  | 首饰-战士项链 | confirmed-145 | — | official-145-items-amulet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 破荒项链（雷） |  | 首饰-战士项链 | confirmed-145 | — | official-145-items-amulet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 破荒项链（神圣） |  | 首饰-战士项链 | confirmed-145 | — | official-145-items-amulet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 破荒项链（暗黑） |  | 首饰-战士项链 | confirmed-145 | — | official-145-items-amulet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 魔云项链 |  | 首饰-法师项链 | confirmed-145 | — | official-145-items-amulet | 官方专区“法师项链”表中的基础名称。 |
| 魔云项链（火） |  | 首饰-法师项链 | confirmed-145 | — | official-145-items-amulet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 魔云项链（冰） |  | 首饰-法师项链 | confirmed-145 | — | official-145-items-amulet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 魔云项链（风） |  | 首饰-法师项链 | confirmed-145 | — | official-145-items-amulet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 魔云项链（雷） |  | 首饰-法师项链 | confirmed-145 | — | official-145-items-amulet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 定心项链 |  | 首饰-道士项链 | confirmed-145 | — | official-145-items-amulet | 官方专区“道士项链”表中的基础名称。 |
| 定心项链（神圣） |  | 首饰-道士项链 | confirmed-145 | — | official-145-items-amulet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 定心项链（暗黑） |  | 首饰-道士项链 | confirmed-145 | — | official-145-items-amulet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 定心项链（幻影） |  | 首饰-道士项链 | confirmed-145 | — | official-145-items-amulet | 官方表格的独立元素行；括号元素为名称的一部分。 |
| 圣山项链 |  | 首饰-共用项链 | confirmed-145 | — | official-145-items-amulet | 官方专区“共用项链”表中单列的名称。 |
| 旧娃娃 |  | 任务物品 | confirmed-145 | — | official-145-skill-activity | 官方活动正文称诺玛遗址出现刻有不同名字的“旧娃娃”道具；未据此扩展未展示的刻名。 |
| 秘籍书（十） |  | 任务物品 | confirmed-145 | — | official-145-skill-activity | 官方活动正文列为可凑齐的刻名旧娃娃。 |
| 秘籍书（方） |  | 任务物品 | confirmed-145 | — | official-145-skill-activity | 官方活动正文列为可凑齐的刻名旧娃娃。 |
| 秘籍书（斩） |  | 任务物品 | confirmed-145 | — | official-145-skill-activity | 官方活动正文列为可凑齐的刻名旧娃娃。 |
| 秘籍书（魄） |  | 任务物品 | confirmed-145 | — | official-145-skill-activity | 官方活动正文列为可凑齐的刻名旧娃娃。 |
| 秘籍书（冰） |  | 任务物品 | confirmed-145 | — | official-145-skill-activity | 官方活动正文列为可凑齐的刻名旧娃娃。 |
| 秘籍书（刺） |  | 任务物品 | confirmed-145 | — | official-145-skill-activity | 官方活动正文列为可凑齐的刻名旧娃娃。 |
| 十方斩（秘籍） |  | 技能书 | confirmed-145 | — | official-145-skill-activity | 官方活动正文明确写三枚对应旧娃娃可兑换此书。 |
| 魄冰刺（秘籍） |  | 技能书 | confirmed-145 | — | official-145-skill-activity | 官方活动正文明确写三枚对应旧娃娃可兑换此书。 |
| 祝福油 |  | 消耗品 | confirmed-145 | — | official-145-skill-activity | 官方活动正文列为诺玛遗址活动路上的奖励物品。 |
| 回生神水 |  | 消耗品 | confirmed-145 | — | official-145-skill-activity | 官方活动正文列为活动奖励物品。 |
| 亡灵之药水 |  | 消耗品 | confirmed-145 | — | official-145-skill-activity | 官方活动正文列为活动奖励物品。 |
| 高级技能书 |  | 技能书 | confirmed-145 | — | official-145-skill-activity | 官方活动正文以该名称称呼活动可得的新技能书；未把它扩展为未逐一列出的书名。 |
| 诺马勇气 |  | 套装部件（原文未明示栏位类型） | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的诺马勇士套装部件；未证明光通中国 1.45 已部署。 |
| 诺马智慧手镯 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的诺马勇士套装部件；未证明光通中国 1.45 已部署。 |
| 诺马正义手镯 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的诺马勇士套装部件；未证明光通中国 1.45 已部署。 |
| 诺马防御手套 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的诺马勇士套装部件；未证明光通中国 1.45 已部署。 |
| 诺马魔法手套 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的诺马勇士套装部件；未证明光通中国 1.45 已部署。 |
| 金刚铃铛 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的金刚套装部件；未证明光通中国 1.45 已部署。 |
| 金刚防御手镯 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的金刚套装部件；未证明光通中国 1.45 已部署。 |
| 金刚魔法手镯 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的金刚套装部件；未证明光通中国 1.45 已部署。 |
| 金刚魔法戒指 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的金刚套装部件；未证明光通中国 1.45 已部署。 |
| 金刚精神戒指 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的金刚套装部件；未证明光通中国 1.45 已部署。 |
| 祈祷之刃 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的祈祷套装部件；未证明光通中国 1.45 已部署。 |
| 祈祷头盔 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的祈祷套装部件；未证明光通中国 1.45 已部署。 |
| 祈祷项链 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的祈祷套装部件；未证明光通中国 1.45 已部署。 |
| 祈祷手镯 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的祈祷套装部件；未证明光通中国 1.45 已部署。 |
| 祈祷戒指 |  | 套装部件 | uncertain-version | — | s17173-kr-20040316-update-plan | 正文表格列为韩服计划中的祈祷套装部件；未证明光通中国 1.45 已部署。 |
| 魔血戒指 |  | 首饰-戒指 | uncertain-version | — | s17173-20030820-moxue-set | 2003 同期正文列为魔血套装部件；没有光通中国 1.45 持续适用证据。 |
| 魔血手镯 |  | 首饰-手镯 | uncertain-version | — | s17173-20030820-moxue-set | 2003 同期正文列为魔血套装部件；没有光通中国 1.45 持续适用证据。 |
| 魔血项链 |  | 首饰-项链 | uncertain-version | — | s17173-20030820-moxue-set | 2003 同期正文列为魔血套装部件；没有光通中国 1.45 持续适用证据。 |

## 本服物品完整对比表

| 快照索引 | 数据库原名 | 官方1.45名称 | 匹配状态 | 匹配方式 | 判断依据 | 证据来源 | 处理建议 | 本地字段（类型/职业/需求/图像） |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| <!-- local:item:1 -->1 | 金币 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/0 |
| <!-- local:item:2 -->2 | 金创药（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5 |
| <!-- local:item:3 -->3 | 魔法药（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/15 |
| <!-- local:item:4 -->4 | 鹿肉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Meat/All/1/300 |
| <!-- local:item:5 -->5 | 布衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/1/940 |
| <!-- local:item:6 -->6 | 布衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/1/950 |
| <!-- local:item:7 -->7 | 木剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1042 |
| <!-- local:item:8 -->8 | 铁剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/7/1043 |
| <!-- local:item:9 -->9 | 青铜剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/5/1043 |
| <!-- local:item:10 -->10 | 轻型盔甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/11/941 |
| <!-- local:item:11 -->11 | 轻型盔甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/11/951 |
| <!-- local:item:12 -->12 | 干肉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/93 |
| <!-- local:item:13 -->13 | 包子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/90 |
| <!-- local:item:14 -->14 | 凝霜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/25/1044 |
| <!-- local:item:15 -->15 | 火球术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/7/304 |
| <!-- local:item:16 -->16 | 治愈术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/7/304 |
| <!-- local:item:17 -->17 | 基本剑术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/7/304 |
| <!-- local:item:18 -->18 | 蜡烛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/290 |
| <!-- local:item:19 -->19 | 短剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/10/1054 |
| <!-- local:item:20 -->20 | 精神力战法 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/8/304 |
| <!-- local:item:21 -->21 | 青铜斧 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/14/1060 |
| <!-- local:item:22 -->22 | 重盔甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/22/990 |
| <!-- local:item:23 -->23 | 魔法长袍（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/22/1030 |
| <!-- local:item:24 -->24 | 灵魂战衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/22/1010 |
| <!-- local:item:25 -->25 | 重盔甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/22/980 |
| <!-- local:item:26 -->26 | 魔法长袍（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/22/1020 |
| <!-- local:item:27 -->27 | 灵魂战衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/22/1000 |
| <!-- local:item:28 -->28 | 大火球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/15/304 |
| <!-- local:item:29 -->29 | 攻杀剑术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/14/304 |
| <!-- local:item:30 -->30 | 施毒术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/12/304 |
| <!-- local:item:31 -->31 | 匕首 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/3/1045 |
| <!-- local:item:32 -->32 | 井中月 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/35/1068 |
| <!-- local:item:33 -->33 | 银蛇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/26/1102 |
| <!-- local:item:34 -->34 | 海魂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/14/1080 |
| <!-- local:item:35 -->35 | 修罗 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/20/1065 |
| <!-- local:item:36 -->36 | 炼狱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/26/1066 |
| <!-- local:item:37 -->37 | 凌风 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/17/1055 |
| <!-- local:item:38 -->38 | 破魂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/10/1052 |
| <!-- local:item:39 -->39 | 斩马刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/18/1063 |
| <!-- local:item:40 -->40 | 食人花树叶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/113 |
| <!-- local:item:41 -->41 | 毒蜘蛛牙齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/111 |
| <!-- local:item:42 -->42 | 食人花果实 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/114 |
| <!-- local:item:43 -->43 | 蝎子的尾巴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/112 |
| <!-- local:item:44 -->44 | 蛆卵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/110 |
| <!-- local:item:45 -->45 | 灰色药粉（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Poison/All/1/131 |
| <!-- local:item:46 -->46 | 黄色药粉（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Poison/All/1/130 |
| <!-- local:item:47 -->47 | 古铜戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/7/530 |
| <!-- local:item:48 -->48 | 青铜头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/9/370 |
| <!-- local:item:49 -->49 | 金项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/2/870 |
| <!-- local:item:50 -->50 | 铁手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/3/646 |
| <!-- local:item:51 -->51 | 灰色药粉（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Poison/All/1/131 |
| <!-- local:item:52 -->52 | 灰色药粉（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Poison/All/1/131 |
| <!-- local:item:53 -->53 | 黄色药粉（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Poison/All/1/130 |
| <!-- local:item:54 -->54 | 黄色药粉（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Poison/All/1/130 |
| <!-- local:item:55 -->55 | 乌木剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/7/1042 |
| <!-- local:item:56 -->56 | 魔杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/26/1082 |
| <!-- local:item:57 -->57 | 八荒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/15/1053 |
| <!-- local:item:58 -->58 | 鸡肉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Meat/All/1/301 |
| <!-- local:item:59 -->59 | 水晶魔戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/7/490 |
| <!-- local:item:60 -->60 | 牛角戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/8/470 |
| <!-- local:item:61 -->61 | 蓝色水晶戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/9/472 |
| <!-- local:item:62 -->62 | 六绝星环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/7/510 |
| <!-- local:item:63 -->63 | 黑檀项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/11/850 |
| <!-- local:item:64 -->64 | 黄色水晶项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/11/830 |
| <!-- local:item:65 -->65 | 黑色水晶项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/11/810 |
| <!-- local:item:66 -->66 | 魔法头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/15/370 |
| <!-- local:item:67 -->67 | 沃玛号角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/100 |
| <!-- local:item:68 -->68 | 半月 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/14/1100 |
| <!-- local:item:69 -->69 | 皮制手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/5/640 |
| <!-- local:item:70 -->70 | 坚固手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/17/642 |
| <!-- local:item:71 -->71 | 钢手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/8/646 |
| <!-- local:item:72 -->72 | 玄铁指环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/9/471 |
| <!-- local:item:73 -->73 | 金戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/473 |
| <!-- local:item:74 -->74 | 灯笼项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/13/872 |
| <!-- local:item:75 -->75 | 白色虎齿项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/18/871 |
| <!-- local:item:76 -->76 | 魅力戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/19/512 |
| <!-- local:item:77 -->77 | 道德戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/19/492 |
| <!-- local:item:78 -->78 | 白金项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/10/851 |
| <!-- local:item:79 -->79 | 降妖除魔戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/27/474 |
| <!-- local:item:80 -->80 | 躲避手链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/7/874 |
| <!-- local:item:81 -->81 | 地牢逃脱卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/206 |
| <!-- local:item:82 -->82 | 偃月 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/18/1081 |
| <!-- local:item:83 -->83 | 降魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/18/1101 |
| <!-- local:item:84 -->84 | 传统项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/3/873 |
| <!-- local:item:85 -->85 | 小手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/4/648 |
| <!-- local:item:86 -->86 | 银手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/5/722 |
| <!-- local:item:87 -->87 | 大手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/9/644 |
| <!-- local:item:88 -->88 | 鹤嘴锄 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/8/1040 |
| <!-- local:item:89 -->89 | 隐身戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/574 |
| <!-- local:item:90 -->90 | 抗拒火环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/12/304 |
| <!-- local:item:91 -->91 | 地狱火 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/20/304 |
| <!-- local:item:92 -->92 | 雷电术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/16/304 |
| <!-- local:item:93 -->93 | 疾光电影 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/21/304 |
| <!-- local:item:94 -->94 | 灵魂火符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/13/304 |
| <!-- local:item:95 -->95 | 幽灵盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/21/304 |
| <!-- local:item:96 -->96 | 神圣战甲术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/25/304 |
| <!-- local:item:97 -->97 | 金创药（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/6 |
| <!-- local:item:98 -->98 | 魔法药（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/16 |
| <!-- local:item:99 -->99 | 黑色水晶戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/13/531 |
| <!-- local:item:100 -->100 | 魔鬼项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/15/811 |
| <!-- local:item:101 -->101 | 珊瑚戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/533 |
| <!-- local:item:102 -->102 | 蓝翡翠项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/21/812 |
| <!-- local:item:103 -->103 | 蛇眼戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/13/511 |
| <!-- local:item:104 -->104 | 琥珀项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/15/852 |
| <!-- local:item:105 -->105 | 护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/330 |
| <!-- local:item:106 -->106 | 刺杀剑术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/19/304 |
| <!-- local:item:107 -->107 | 放大镜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/22/853 |
| <!-- local:item:108 -->108 | 红宝石戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/20/513 |
| <!-- local:item:109 -->109 | 珍珠戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/13/491 |
| <!-- local:item:110 -->110 | 竹笛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/22/832 |
| <!-- local:item:111 -->111 | 铂金戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Taoist/20/493 |
| <!-- local:item:112 -->112 | 骷髅戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/30/532 |
| <!-- local:item:113 -->113 | 龙之戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Warrior/20/534 |
| <!-- local:item:114 -->114 | 死神手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/22/661 |
| <!-- local:item:115 -->115 | 骷髅头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/30/373 |
| <!-- local:item:116 -->116 | 魔法手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/12/647 |
| <!-- local:item:117 -->117 | 金手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/25/645 |
| <!-- local:item:118 -->118 | 道士头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/20/372 |
| <!-- local:item:119 -->119 | 传送戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/573 |
| <!-- local:item:120 -->120 | 尽力手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/15/660 |
| <!-- local:item:121 -->121 | 骑士手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/AssWar/30/662 |
| <!-- local:item:122 -->122 | 绿色项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/AssWar/30/814 |
| <!-- local:item:123 -->123 | 凤凰明珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/19/831 |
| <!-- local:item:124 -->124 | 道士手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/10/680 |
| <!-- local:item:125 -->125 | 三眼手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Taoist/22/681 |
| <!-- local:item:126 -->126 | 灵魂项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/30/834 |
| <!-- local:item:127 -->127 | 黑檀手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/10/700 |
| <!-- local:item:128 -->128 | 思贝儿手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Wizard/22/701 |
| <!-- local:item:129 -->129 | 恶魔铃铛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Wizard/30/855 |
| <!-- local:item:130 -->130 | 铜矿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ore/All/0/216 |
| <!-- local:item:131 -->131 | 铁矿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ore/All/0/215 |
| <!-- local:item:132 -->132 | 银矿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ore/All/0/211 |
| <!-- local:item:133 -->133 | 金矿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ore/All/0/210 |
| <!-- local:item:134 -->134 | 战神油 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/61 |
| <!-- local:item:135 -->135 | 回城卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/207 |
| <!-- local:item:136 -->136 | 祝福油 | 祝福油 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-skill-activity | 确认保留 | Consumable/All/0/63 |
| <!-- local:item:137 -->137 | 麻痹戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/571 |
| <!-- local:item:138 -->138 | 复活戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/575 |
| <!-- local:item:139 -->139 | 火焰戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/577 |
| <!-- local:item:140 -->140 | 防御戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/570 |
| <!-- local:item:142 -->142 | 护身戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/576 |
| <!-- local:item:143 -->143 | 神力戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/572 |
| <!-- local:item:144 -->144 | 技巧项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/891 |
| <!-- local:item:145 -->145 | 狂风戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/550 |
| <!-- local:item:146 -->146 | 夏普儿手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/7/721 |
| <!-- local:item:147 -->147 | 狂风项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/877 |
| <!-- local:item:148 -->148 | 辟邪手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/7/723 |
| <!-- local:item:149 -->149 | 探测项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/890 |
| <!-- local:item:150 -->150 | 困魔咒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/27/304 |
| <!-- local:item:151 -->151 | 召唤骷髅 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/17/304 |
| <!-- local:item:152 -->152 | 隐身术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/20/304 |
| <!-- local:item:153 -->153 | 集体隐身术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/23/304 |
| <!-- local:item:154 -->154 | 诱惑之光 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/13/304 |
| <!-- local:item:155 -->155 | 瞬息移动 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/14/304 |
| <!-- local:item:156 -->156 | 火墙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/24/304 |
| <!-- local:item:157 -->157 | 爆裂火焰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/32/304 |
| <!-- local:item:158 -->158 | 地狱雷光 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/33/304 |
| <!-- local:item:159 -->159 | 半月弯刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/24/304 |
| <!-- local:item:160 -->160 | 愤怒之钟（雷） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/25/856 |
| <!-- local:item:161 -->161 | 愤怒之钟（风） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/25/856 |
| <!-- local:item:162 -->162 | 太阳水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/20 |
| <!-- local:item:163 -->163 | 祖玛头像 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/101 |
| <!-- local:item:164 -->164 | 兑换卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/180 |
| <!-- local:item:165 -->165 | 随机传送卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/205 |
| <!-- local:item:166 -->166 | 无极棍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/38/1103 |
| <!-- local:item:167 -->167 | 血饮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/33/1083 |
| <!-- local:item:168 -->168 | 裁决之杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/38/1069 |
| <!-- local:item:169 -->169 | 记忆戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/590 |
| <!-- local:item:170 -->170 | 记忆项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/910 |
| <!-- local:item:171 -->171 | 记忆手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/0/760 |
| <!-- local:item:172 -->172 | 记忆头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/0/390 |
| <!-- local:item:173 -->173 | 祈祷之刃 | 祈祷之刃 | 版本不确定 | exact | 与官方正式名称精确匹配；官方条目状态：uncertain-version | s17173-kr-20040316-update-plan | 版本不确定 | Weapon/All/0/1120 |
| <!-- local:item:174 -->174 | 祈祷手镯 | 祈祷手镯 | 版本不确定 | exact | 与官方正式名称精确匹配；官方条目状态：uncertain-version | s17173-kr-20040316-update-plan | 版本不确定 | Bracelet/All/0/761 |
| <!-- local:item:175 -->175 | 祈祷项链 | 祈祷项链 | 版本不确定 | exact | 与官方正式名称精确匹配；官方条目状态：uncertain-version | s17173-kr-20040316-update-plan | 版本不确定 | Necklace/All/0/911 |
| <!-- local:item:176 -->176 | 祈祷戒指 | 祈祷戒指 | 版本不确定 | exact | 与官方正式名称精确匹配；官方条目状态：uncertain-version | s17173-kr-20040316-update-plan | 版本不确定 | Ring/All/0/591 |
| <!-- local:item:177 -->177 | 祈祷头盔 | 祈祷头盔 | 版本不确定 | exact | 与官方正式名称精确匹配；官方条目状态：uncertain-version | s17173-kr-20040316-update-plan | 版本不确定 | Helmet/WarWizTao/0/391 |
| <!-- local:item:178 -->178 | 行会回城卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/204 |
| <!-- local:item:179 -->179 | 修复油 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/53 |
| <!-- local:item:180 -->180 | 金创药（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7 |
| <!-- local:item:181 -->181 | 魔法药（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/17 |
| <!-- local:item:182 -->182 | 生命项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Wizard/23/854 |
| <!-- local:item:183 -->183 | 力量戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/AssWar/30/535 |
| <!-- local:item:184 -->184 | 心灵手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Taoist/30/682 |
| <!-- local:item:185 -->185 | 黑铁头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Warrior/40/374 |
| <!-- local:item:186 -->186 | 烈火剑法 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/32/304 |
| <!-- local:item:187 -->187 | 野蛮冲撞 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/27/304 |
| <!-- local:item:188 -->188 | 心灵启示 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/99/304 |
| <!-- local:item:189 -->189 | 群体治愈术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/31/304 |
| <!-- local:item:190 -->190 | 召唤神兽 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/30/304 |
| <!-- local:item:191 -->191 | 魔法盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/29/304 |
| <!-- local:item:192 -->192 | 圣言术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/26/304 |
| <!-- local:item:193 -->193 | 冰咆哮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/34/304 |
| <!-- local:item:194 -->194 | 金创药（大）包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/245 |
| <!-- local:item:195 -->195 | 魔法药（大）包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/255 |
| <!-- local:item:196 -->196 | 强效太阳水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/21 |
| <!-- local:item:197 -->197 | 骰子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/140 |
| <!-- local:item:198 -->198 | 木料 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/305 |
| <!-- local:item:199 -->199 | 黑铁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ore/All/0/214 |
| <!-- local:item:200 -->200 | 彩票 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/192 |
| <!-- local:item:201 -->201 | 祝福道士头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/37/372 |
| <!-- local:item:205 -->205 | 命运之刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/33/1067 |
| <!-- local:item:206 -->206 | 屠龙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/50/1070 |
| <!-- local:item:207 -->207 | 骨玉权杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/38/1084 |
| <!-- local:item:208 -->208 | 龙纹剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/40/1104 |
| <!-- local:item:209 -->209 | 嗜魂法杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/40/1272 |
| <!-- local:item:210 -->210 | 火把 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/291 |
| <!-- local:item:212 -->212 | 鹿茸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/71 |
| <!-- local:item:213 -->213 | 命运之书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:214 -->214 | 紫碧螺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/30/514 |
| <!-- local:item:215 -->215 | 泰坦戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Taoist/30/494 |
| <!-- local:item:216 -->216 | 幽灵手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/AssWar/22/641 |
| <!-- local:item:217 -->217 | 阎罗手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/0/643 |
| <!-- local:item:218 -->218 | 龙之手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Wizard/30/702 |
| <!-- local:item:219 -->219 | 天珠项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/25/833 |
| <!-- local:item:220 -->220 | 幽灵项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/AssWar/23/813 |
| <!-- local:item:221 -->221 | 米糕 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/91 |
| <!-- local:item:222 -->222 | 金条 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/125 |
| <!-- local:item:223 -->223 | 鹿血 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/32 |
| <!-- local:item:224 -->224 | 神秘戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/18/740 |
| <!-- local:item:225 -->225 | 神秘腰带 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/18/702 |
| <!-- local:item:226 -->226 | 神秘头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/18/410 |
| <!-- local:item:227 -->227 | 神水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/64 |
| <!-- local:item:228 -->228 | 蓝包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/132 |
| <!-- local:item:229 -->229 | 红包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/133 |
| <!-- local:item:230 -->230 | 绿包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/134 |
| <!-- local:item:231 -->231 | 人参 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/70 |
| <!-- local:item:232 -->232 | 馒头 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/91 |
| <!-- local:item:233 -->233 | 莲花宝镜（暗黑） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/25/817 |
| <!-- local:item:234 -->234 | 莲花宝镜（幻影） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/25/817 |
| <!-- local:item:235 -->235 | 五色项链（火） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/913 |
| <!-- local:item:236 -->236 | 五色项链（冰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/913 |
| <!-- local:item:237 -->237 | 五色项链（雷） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/913 |
| <!-- local:item:238 -->238 | 五色项链（风） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/913 |
| <!-- local:item:239 -->239 | 介绍信 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/173 |
| <!-- local:item:240 -->240 | 红苹果 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/86 |
| <!-- local:item:241 -->241 | 筹码 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/302 |
| <!-- local:item:242 -->242 | 特殊药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/40 |
| <!-- local:item:243 -->243 | 万年雪霜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/70 |
| <!-- local:item:244 -->244 | 金创药（小）包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/243 |
| <!-- local:item:245 -->245 | 魔法药（小）包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/253 |
| <!-- local:item:246 -->246 | 金创药（中）包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/244 |
| <!-- local:item:247 -->247 | 魔法药（中）包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/254 |
| <!-- local:item:248 -->248 | 地牢逃脱卷包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/266 |
| <!-- local:item:249 -->249 | 随机传送卷包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/265 |
| <!-- local:item:250 -->250 | 回城卷包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/267 |
| <!-- local:item:251 -->251 | 行会回城卷包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/264 |
| <!-- local:item:252 -->252 | 筹码包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/270 |
| <!-- local:item:253 -->253 | 参加活动卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/180 |
| <!-- local:item:254 -->254 | 水饺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/94 |
| <!-- local:item:255 -->255 | 攻击神水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/11/84 |
| <!-- local:item:256 -->256 | 自然神水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/11/82 |
| <!-- local:item:257 -->257 | 灵魂神水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/11/81 |
| <!-- local:item:258 -->258 | 疾风神水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/11/80 |
| <!-- local:item:259 -->259 | 体力强效神水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/11/85 |
| <!-- local:item:260 -->260 | 魔力强效神水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/11/83 |
| <!-- local:item:261 -->261 | 金条包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/126 |
| <!-- local:item:262 -->262 | 金盒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/127 |
| <!-- local:item:263 -->263 | 攻击神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/22/84 |
| <!-- local:item:264 -->264 | 自然神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/22/82 |
| <!-- local:item:265 -->265 | 灵魂神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/22/81 |
| <!-- local:item:266 -->266 | 疾风神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/22/80 |
| <!-- local:item:267 -->267 | 体力强效神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/22/85 |
| <!-- local:item:268 -->268 | 魔力强效神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/22/83 |
| <!-- local:item:269 -->269 | 攻击神水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/33/84 |
| <!-- local:item:270 -->270 | 自然神水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/33/82 |
| <!-- local:item:271 -->271 | 灵魂神水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/33/81 |
| <!-- local:item:272 -->272 | 体力强效神水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/33/85 |
| <!-- local:item:273 -->273 | 魔力强效神水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/33/83 |
| <!-- local:item:274 -->274 | 攻击神水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/44/84 |
| <!-- local:item:275 -->275 | 自然神水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/44/82 |
| <!-- local:item:276 -->276 | 灵魂神水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/44/81 |
| <!-- local:item:277 -->277 | 体力强效神水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/44/85 |
| <!-- local:item:278 -->278 | 魔力强效神水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/44/83 |
| <!-- local:item:279 -->279 | 疾风神水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/44/80 |
| <!-- local:item:280 -->280 | 疾风神水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/33/80 |
| <!-- local:item:281 -->281 | 青苹果 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/86 |
| <!-- local:item:282 -->282 | 赤血宝剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/30/1121 |
| <!-- local:item:283 -->283 | 魔血戒指 | 魔血戒指 | 版本不确定 | exact | 与官方正式名称精确匹配；官方条目状态：uncertain-version | s17173-20030820-moxue-set | 版本不确定 | Ring/All/0/593 |
| <!-- local:item:284 -->284 | 魔血手镯 | 魔血手镯 | 版本不确定 | exact | 与官方正式名称精确匹配；官方条目状态：uncertain-version | s17173-20030820-moxue-set | 版本不确定 | Bracelet/All/0/763 |
| <!-- local:item:285 -->285 | 魔血项链 | 魔血项链 | 版本不确定 | exact | 与官方正式名称精确匹配；官方条目状态：uncertain-version | s17173-20030820-moxue-set | 版本不确定 | Necklace/All/0/913 |
| <!-- local:item:286 -->286 | 虹魔戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/592 |
| <!-- local:item:287 -->287 | 虹魔手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/0/762 |
| <!-- local:item:288 -->288 | 虹魔项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/912 |
| <!-- local:item:289 -->289 | 血剑碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1140 |
| <!-- local:item:290 -->290 | 鉴定石一级 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1620 |
| <!-- local:item:291 -->291 | 鉴定石二级 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/2/1622 |
| <!-- local:item:292 -->292 | 鉴定石三级 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/3/1623 |
| <!-- local:item:293 -->293 | 鉴定石四级 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/4/1624 |
| <!-- local:item:294 -->294 | 鉴定石五级 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/5/1625 |
| <!-- local:item:296 -->296 | 玉水晶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1141 |
| <!-- local:item:297 -->297 | 血魔心脏 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1142 |
| <!-- local:item:298 -->298 | 魔血油 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1143 |
| <!-- local:item:299 -->299 | 生死宝刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1050 |
| <!-- local:item:300 -->300 | 战神盔甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/33/981 |
| <!-- local:item:301 -->301 | 战神盔甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/33/991 |
| <!-- local:item:302 -->302 | 恶魔长袍（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/33/1021 |
| <!-- local:item:303 -->303 | 恶魔长袍（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/33/1031 |
| <!-- local:item:304 -->304 | 幽灵战衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/33/1001 |
| <!-- local:item:305 -->305 | 幽灵战衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/33/1011 |
| <!-- local:item:306 -->306 | 无名刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/33/1062 |
| <!-- local:item:307 -->307 | 袖里剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DartWeapon/Warrior/10/1071 |
| <!-- local:item:308 -->308 | 标枪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DartWeapon/Warrior/30/1072 |
| <!-- local:item:309 -->309 | 铁枪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DartWeapon/Warrior/20/1073 |
| <!-- local:item:310 -->310 | 白马标志 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/320 |
| <!-- local:item:311 -->311 | 马牌（黄骠马） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/320 |
| <!-- local:item:312 -->312 | 马牌（的卢） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/320 |
| <!-- local:item:313 -->313 | 古籍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:314 -->314 | 鸡血 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/31 |
| <!-- local:item:315 -->315 | 烧酒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1145 |
| <!-- local:item:316 -->316 | 毒蛇牙齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1152 |
| <!-- local:item:317 -->317 | 王铁匠的铁锤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1153 |
| <!-- local:item:318 -->318 | 角笛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1146 |
| <!-- local:item:319 -->319 | 半块不死牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1147 |
| <!-- local:item:320 -->320 | 不死牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1148 |
| <!-- local:item:321 -->321 | 雷电僵尸骨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1149 |
| <!-- local:item:322 -->322 | 僧侣僵尸骨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1149 |
| <!-- local:item:323 -->323 | 毁灭护身符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1150 |
| <!-- local:item:324 -->324 | 七点白蛇胆 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1151 |
| <!-- local:item:325 -->325 | 斗笠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/27/411 |
| <!-- local:item:326 -->326 | 翔空剑法 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/35/304 |
| <!-- local:item:327 -->327 | 莲月剑法 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/38/304 |
| <!-- local:item:328 -->328 | 空拳刀法 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/28/304 |
| <!-- local:item:329 -->329 | 月魂断玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/14/304 |
| <!-- local:item:330 -->330 | 冰月神掌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/9/304 |
| <!-- local:item:331 -->331 | 冰月震天 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/17/304 |
| <!-- local:item:332 -->332 | 霹雳掌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/8/304 |
| <!-- local:item:333 -->333 | 月魂灵波 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/24/304 |
| <!-- local:item:334 -->334 | 墨龙屠龙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/36/1201 |
| <!-- local:item:335 -->335 | 墨龙嗜魂法杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/36/1085 |
| <!-- local:item:336 -->336 | 墨龙龙纹剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/36/1222 |
| <!-- local:item:344 -->344 | 师承戒指（火） | 师承戒指（火） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/All/49/538 |
| <!-- local:item:348 -->348 | 七点白蛇血 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/31 |
| <!-- local:item:349 -->349 | 金刚铃铛 | 金刚铃铛 | 版本不确定 | exact | 与官方正式名称精确匹配；官方条目状态：uncertain-version | s17173-kr-20040316-update-plan | 版本不确定 | Necklace/All/0/914 |
| <!-- local:item:350 -->350 | 金刚魔法指环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/594 |
| <!-- local:item:351 -->351 | 金刚精神戒指 | 金刚精神戒指 | 版本不确定 | exact | 与官方正式名称精确匹配；官方条目状态：uncertain-version | s17173-kr-20040316-update-plan | 版本不确定 | Ring/All/0/594 |
| <!-- local:item:352 -->352 | 金刚防御手镯 | 金刚防御手镯 | 版本不确定 | exact | 与官方正式名称精确匹配；官方条目状态：uncertain-version | s17173-kr-20040316-update-plan | 版本不确定 | Bracelet/All/0/764 |
| <!-- local:item:353 -->353 | 金刚魔法手镯 | 金刚魔法手镯 | 版本不确定 | exact | 与官方正式名称精确匹配；官方条目状态：uncertain-version | s17173-kr-20040316-update-plan | 版本不确定 | Bracelet/All/0/764 |
| <!-- local:item:354 -->354 | 霹雷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/40/1074 |
| <!-- local:item:355 -->355 | 铁轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/50/1086 |
| <!-- local:item:356 -->356 | 逍遥扇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/50/1105 |
| <!-- local:item:357 -->357 | 劳动蚂蚁卵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/102 |
| <!-- local:item:358 -->358 | 诺玛法老珍珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1424 |
| <!-- local:item:360 -->360 | 雷神戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/35/857 |
| <!-- local:item:361 -->361 | 毁灭手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Wizard/35/683 |
| <!-- local:item:362 -->362 | 神谕项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Wizard/35/858 |
| <!-- local:item:363 -->363 | 昏暗风印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/816 |
| <!-- local:item:364 -->364 | 润神戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Taoist/35/475 |
| <!-- local:item:365 -->365 | 如来手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Taoist/35/663 |
| <!-- local:item:366 -->366 | 猫眼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/35/838 |
| <!-- local:item:367 -->367 | 怨恨项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/815 |
| <!-- local:item:368 -->368 | 尾毛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1422 |
| <!-- local:item:369 -->369 | 生存游戏场地地图1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/180 |
| <!-- local:item:370 -->370 | 信件 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/180 |
| <!-- local:item:371 -->371 | 帐簿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:372 -->372 | 半兽人角笛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1146 |
| <!-- local:item:373 -->373 | 不死骨头 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/103 |
| <!-- local:item:374 -->374 | 尹老人的酒瓶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/65 |
| <!-- local:item:375 -->375 | 姜铁匠的斧头 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1060 |
| <!-- local:item:376 -->376 | 盔甲的蚂蚁卵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/102 |
| <!-- local:item:377 -->377 | 七点白蛇胆汁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1341 |
| <!-- local:item:378 -->378 | 邪恶钳虫皮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/107 |
| <!-- local:item:379 -->379 | 腐蚀人鬼之泪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1348 |
| <!-- local:item:380 -->380 | 沃玛勇士号角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1338 |
| <!-- local:item:381 -->381 | 钳虫皮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/107 |
| <!-- local:item:383 -->383 | 千年毒蛇牙齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1152 |
| <!-- local:item:384 -->384 | 沃玛角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1338 |
| <!-- local:item:385 -->385 | 骷髅精灵骨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/103 |
| <!-- local:item:386 -->386 | 啊潘的信件 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/180 |
| <!-- local:item:387 -->387 | 华玉的信件 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/180 |
| <!-- local:item:388 -->388 | 比奇历史书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:389 -->389 | 魔灵牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/320 |
| <!-- local:item:391 -->391 | 幻影蜘蛛线 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/105 |
| <!-- local:item:394 -->394 | 血巨人心脏 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1142 |
| <!-- local:item:395 -->395 | 触龙神皮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/108 |
| <!-- local:item:396 -->396 | 法师神杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1082 |
| <!-- local:item:397 -->397 | 航海日志 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:398 -->398 | 遗骸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/103 |
| <!-- local:item:399 -->399 | 七点白蛇牙齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1152 |
| <!-- local:item:400 -->400 | 魔幻戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/450 |
| <!-- local:item:401 -->401 | 石头 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/311 |
| <!-- local:item:402 -->402 | 箭 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/310 |
| <!-- local:item:403 -->403 | 天机戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/476 |
| <!-- local:item:404 -->404 | 巨龙戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/25/534 |
| <!-- local:item:405 -->405 | 天鸣戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/25/493 |
| <!-- local:item:406 -->406 | 火玉戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/25/513 |
| <!-- local:item:407 -->407 | 五彩项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/30/854 |
| <!-- local:item:408 -->408 | 遗魂项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/30/833 |
| <!-- local:item:409 -->409 | 王大人的书信 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1330 |
| <!-- local:item:410 -->410 | 葫芦 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1465 |
| <!-- local:item:411 -->411 | 瓶中信 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1443 |
| <!-- local:item:412 -->412 | 生锈牙轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1463 |
| <!-- local:item:413 -->413 | 汤药 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1462 |
| <!-- local:item:414 -->414 | 瓷器箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1449 |
| <!-- local:item:415 -->415 | 旧扇子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1457 |
| <!-- local:item:416 -->416 | 怀旧项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/795 |
| <!-- local:item:417 -->417 | 旧娃娃 | 旧娃娃 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-skill-activity | 确认保留 | Material/All/1/1455 |
| <!-- local:item:418 -->418 | 水晶球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1335 |
| <!-- local:item:419 -->419 | 锦秀的衣角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1461 |
| <!-- local:item:420 -->420 | 万多罗的护身符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1456 |
| <!-- local:item:421 -->421 | 万相的护身符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1457 |
| <!-- local:item:422 -->422 | 三妹的护身符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1460 |
| <!-- local:item:423 -->423 | 战士的证票 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1453 |
| <!-- local:item:424 -->424 | 秘密医书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1458 |
| <!-- local:item:425 -->425 | 黑野猪牙齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1431 |
| <!-- local:item:426 -->426 | 七点白蛇的牙齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1152 |
| <!-- local:item:427 -->427 | 祖玛卫士雕像 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1430 |
| <!-- local:item:428 -->428 | 半兽利齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1431 |
| <!-- local:item:430 -->430 | 千年毒蛇血 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/31 |
| <!-- local:item:431 -->431 | 虎蛇血 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/31 |
| <!-- local:item:432 -->432 | 黑檀雕像 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1467 |
| <!-- local:item:433 -->433 | 波善的短剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1464 |
| <!-- local:item:434 -->434 | 黑蝉项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1466 |
| <!-- local:item:435 -->435 | 消魔的护身符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1451 |
| <!-- local:item:436 -->436 | 陈氏护身符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1451 |
| <!-- local:item:437 -->437 | 荣耀项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/25/837 |
| <!-- local:item:438 -->438 | 愤怒之钟 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/25/856 |
| <!-- local:item:439 -->439 | 莲花宝镜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/25/817 |
| <!-- local:item:440 -->440 | 魔神怪手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/620 |
| <!-- local:item:441 -->441 | 行者帽 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Wizard/40/413 |
| <!-- local:item:442 -->442 | 战神头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Warrior/0/414 |
| <!-- local:item:443 -->443 | 虎面头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WizTao/0/415 |
| <!-- local:item:444 -->444 | 旋风流星刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/45/1049 |
| <!-- local:item:445 -->445 | 角剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/10/1062 |
| <!-- local:item:446 -->446 | 飞魂魔刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/45/1061 |
| <!-- local:item:447 -->447 | 虚空道环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/479 |
| <!-- local:item:448 -->448 | 准确之炼狱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/33/1066 |
| <!-- local:item:449 -->449 | 红叶血环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/20/499 |
| <!-- local:item:450 -->450 | 六棱戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/498 |
| <!-- local:item:451 -->451 | 紫金环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/0/497 |
| <!-- local:item:452 -->452 | 武圣之戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/496 |
| <!-- local:item:453 -->453 | 基本剑术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/7/304 |
| <!-- local:item:454 -->454 | 攻杀剑术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/14/304 |
| <!-- local:item:455 -->455 | 刺杀剑术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/19/304 |
| <!-- local:item:456 -->456 | 半月弯刀（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/24/304 |
| <!-- local:item:457 -->457 | 野蛮冲撞（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/27/304 |
| <!-- local:item:458 -->458 | 烈火剑法（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/32/304 |
| <!-- local:item:459 -->459 | 莲月剑法（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/38/304 |
| <!-- local:item:460 -->460 | 翔空剑法（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/35/304 |
| <!-- local:item:461 -->461 | 火球术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/7/304 |
| <!-- local:item:462 -->462 | 诱惑之光（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/13/304 |
| <!-- local:item:463 -->463 | 抗拒火环（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/12/304 |
| <!-- local:item:464 -->464 | 雷电术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/16/304 |
| <!-- local:item:465 -->465 | 瞬息移动（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/14/304 |
| <!-- local:item:466 -->466 | 大火球（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/15/304 |
| <!-- local:item:467 -->467 | 地狱火（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/20/304 |
| <!-- local:item:468 -->468 | 爆裂火焰（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/32/304 |
| <!-- local:item:469 -->469 | 疾光电影（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/21/304 |
| <!-- local:item:470 -->470 | 火墙（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/24/304 |
| <!-- local:item:471 -->471 | 地狱雷光（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/33/304 |
| <!-- local:item:472 -->472 | 魔法盾（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/29/304 |
| <!-- local:item:473 -->473 | 圣言术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/26/304 |
| <!-- local:item:474 -->474 | 冰咆哮（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/34/304 |
| <!-- local:item:475 -->475 | 冰月神掌（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/9/304 |
| <!-- local:item:476 -->476 | 冰月震天（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/17/304 |
| <!-- local:item:477 -->477 | 霹雳掌（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/8/304 |
| <!-- local:item:478 -->478 | 精神力战法（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/8/304 |
| <!-- local:item:479 -->479 | 治愈术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/7/304 |
| <!-- local:item:480 -->480 | 施毒术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/12/304 |
| <!-- local:item:481 -->481 | 灵魂火符（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/13/304 |
| <!-- local:item:482 -->482 | 幽灵盾（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/21/304 |
| <!-- local:item:483 -->483 | 神圣战甲术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/25/304 |
| <!-- local:item:484 -->484 | 召唤骷髅（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/17/304 |
| <!-- local:item:485 -->485 | 困魔咒（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/27/304 |
| <!-- local:item:486 -->486 | 隐身术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/20/304 |
| <!-- local:item:487 -->487 | 集体隐身术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/23/304 |
| <!-- local:item:488 -->488 | 七彩金环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/478 |
| <!-- local:item:489 -->489 | 群体治愈术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/31/304 |
| <!-- local:item:490 -->490 | 召唤神兽（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/30/304 |
| <!-- local:item:491 -->491 | 空拳刀法（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/28/304 |
| <!-- local:item:492 -->492 | 月魂断玉（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/14/304 |
| <!-- local:item:493 -->493 | 月魂灵波（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/24/304 |
| <!-- local:item:494 -->494 | 拓本 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1330 |
| <!-- local:item:495 -->495 | 心魔戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/477 |
| <!-- local:item:496 -->496 | 破真刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1332 |
| <!-- local:item:497 -->497 | 纱王项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1333 |
| <!-- local:item:498 -->498 | 灵魂明珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1343 |
| <!-- local:item:499 -->499 | 花毒粉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1334 |
| <!-- local:item:500 -->500 | 沃毒神精 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:501 -->501 | 连环明珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1468 |
| <!-- local:item:502 -->502 | 祖玛卫士明珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1336 |
| <!-- local:item:503 -->503 | 制灵水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1341 |
| <!-- local:item:504 -->504 | 真实明镜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1339 |
| <!-- local:item:505 -->505 | 祖玛明珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1335 |
| <!-- local:item:506 -->506 | 安心石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1337 |
| <!-- local:item:507 -->507 | 诸神道书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:508 -->508 | 宝玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1424 |
| <!-- local:item:509 -->509 | 祖玛雕像号角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1338 |
| <!-- local:item:510 -->510 | 制魔油 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/60 |
| <!-- local:item:511 -->511 | 牛肉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Meat/All/1/300 |
| <!-- local:item:512 -->512 | 猪肉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Meat/All/1/300 |
| <!-- local:item:513 -->513 | 攻杀铁剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1122 |
| <!-- local:item:514 -->514 | 道力护身符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1150 |
| <!-- local:item:515 -->515 | 肉汤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/94 |
| <!-- local:item:516 -->516 | 灵珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1343 |
| <!-- local:item:517 -->517 | 无名药 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/81 |
| <!-- local:item:518 -->518 | 千年毒蛇胆汁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1151 |
| <!-- local:item:519 -->519 | 胆汁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/82 |
| <!-- local:item:520 -->520 | 生存游戏场地地图2 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/181 |
| <!-- local:item:521 -->521 | 战酒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1145 |
| <!-- local:item:522 -->522 | 耐久轻型盔甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/11/942 |
| <!-- local:item:523 -->523 | 耐久轻型盔甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/11/952 |
| <!-- local:item:524 -->524 | 狼肉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Meat/All/1/300 |
| <!-- local:item:525 -->525 | 羊肉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Meat/All/1/300 |
| <!-- local:item:526 -->526 | 不死戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/532 |
| <!-- local:item:527 -->527 | 起爆石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1339 |
| <!-- local:item:528 -->528 | 树脂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/110 |
| <!-- local:item:529 -->529 | 闪电石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1335 |
| <!-- local:item:530 -->530 | 树脂魔法长袍（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/25/1020 |
| <!-- local:item:531 -->531 | 树脂魔法长袍（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/25/1030 |
| <!-- local:item:532 -->532 | 书信 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/180 |
| <!-- local:item:533 -->533 | 诺玛石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1335 |
| <!-- local:item:534 -->534 | 诺玛重盔甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/25/980 |
| <!-- local:item:535 -->535 | 诺玛重盔甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/25/990 |
| <!-- local:item:536 -->536 | 神奇灵魂战衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/25/1000 |
| <!-- local:item:537 -->537 | 神奇灵魂战衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/25/1010 |
| <!-- local:item:538 -->538 | 蚂蚁卵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/102 |
| <!-- local:item:540 -->540 | 浪雨刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1122 |
| <!-- local:item:541 -->541 | 波纹手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/17/645 |
| <!-- local:item:542 -->542 | 白虎剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1122 |
| <!-- local:item:543 -->543 | 灵魂护卫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/65 |
| <!-- local:item:544 -->544 | 沃玛神铁锤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1153 |
| <!-- local:item:545 -->545 | 无名日志 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:546 -->546 | 沃玛金牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1344 |
| <!-- local:item:547 -->547 | 地狱神钟 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1345 |
| <!-- local:item:548 -->548 | 黑珍珠戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/15/531 |
| <!-- local:item:549 -->549 | 龙骨戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/532 |
| <!-- local:item:550 -->550 | 天龙环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/25/534 |
| <!-- local:item:551 -->551 | 魔家项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/19/850 |
| <!-- local:item:552 -->552 | 流星天玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/17/853 |
| <!-- local:item:553 -->553 | 月光石手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/26/760 |
| <!-- local:item:554 -->554 | 天仙之珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/14/831 |
| <!-- local:item:555 -->555 | 松笛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/17/832 |
| <!-- local:item:556 -->556 | 八面太极戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/590 |
| <!-- local:item:557 -->557 | 伏羲手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/15/660 |
| <!-- local:item:558 -->558 | 中秋之夜（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1407 |
| <!-- local:item:559 -->559 | 中秋之夜（秋） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1408 |
| <!-- local:item:560 -->560 | 中秋之夜（之） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1409 |
| <!-- local:item:561 -->561 | 中秋之夜（夜） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1400 |
| <!-- local:item:562 -->562 | 中秋之夜（团） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1401 |
| <!-- local:item:563 -->563 | 中秋之夜（圆） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1402 |
| <!-- local:item:564 -->564 | 中秋之夜（美） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1403 |
| <!-- local:item:565 -->565 | 中秋之夜（满） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1404 |
| <!-- local:item:566 -->566 | 中秋之夜（幸） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1405 |
| <!-- local:item:567 -->567 | 中秋之夜（福） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1406 |
| <!-- local:item:572 -->572 | 成致日志 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:580 -->580 | 毒蛇胆汁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1341 |
| <!-- local:item:581 -->581 | 千年毒蛇之牙齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1152 |
| <!-- local:item:582 -->582 | 褐色栗子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1410 |
| <!-- local:item:583 -->583 | 铜色栗子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1413 |
| <!-- local:item:584 -->584 | 银色栗子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1412 |
| <!-- local:item:585 -->585 | 金色栗子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1411 |
| <!-- local:item:586 -->586 | 回生神水 | 回生神水 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-skill-activity | 确认保留 | Consumable/All/1/64 |
| <!-- local:item:587 -->587 | 霸王教主雕像 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/45/1343 |
| <!-- local:item:588 -->588 | 老中医的医书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:589 -->589 | 未鉴定阴阳刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/1/1064 |
| <!-- local:item:590 -->590 | 未鉴定拐杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/1/1087 |
| <!-- local:item:591 -->591 | 未鉴定天狼刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/1/1078 |
| <!-- local:item:592 -->592 | 魔灵戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Taoist/40/495 |
| <!-- local:item:593 -->593 | 石榴戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/40/516 |
| <!-- local:item:594 -->594 | 青摇戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Warrior/40/536 |
| <!-- local:item:595 -->595 | 火焰沃玛之角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1338 |
| <!-- local:item:596 -->596 | 莲丸戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/40/537 |
| <!-- local:item:597 -->597 | 冰沙掌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/22/304 |
| <!-- local:item:598 -->598 | 铁系项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Warrior/40/878 |
| <!-- local:item:599 -->599 | 追魂项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Wizard/40/892 |
| <!-- local:item:600 -->600 | 追风项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Assassin/40/893 |
| <!-- local:item:601 -->601 | 魔令项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/40/894 |
| <!-- local:item:602 -->602 | 缥缈戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/3290 |
| <!-- local:item:603 -->603 | 尸王白骨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1149 |
| <!-- local:item:604 -->604 | 魔令手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/40/649 |
| <!-- local:item:605 -->605 | 宝藏岛地图3 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/182 |
| <!-- local:item:607 -->607 | 未鉴定赤龙神甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/1/3323 |
| <!-- local:item:608 -->608 | 未鉴定赤龙神甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/1/3333 |
| <!-- local:item:609 -->609 | 未鉴定赤龙头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/1/416 |
| <!-- local:item:610 -->610 | 未鉴定虎影戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Warrior/1/540 |
| <!-- local:item:611 -->611 | 风掌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/10/304 |
| <!-- local:item:612 -->612 | 未鉴定永柳戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Taoist/1/500 |
| <!-- local:item:614 -->614 | 诺玛药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/62 |
| <!-- local:item:615 -->615 | 气血项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/916 |
| <!-- local:item:616 -->616 | 龙卷风 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/35/304 |
| <!-- local:item:617 -->617 | 风震天 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/23/304 |
| <!-- local:item:618 -->618 | 击风 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/18/304 |
| <!-- local:item:619 -->619 | 流星项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/898 |
| <!-- local:item:620 -->620 | 毁灭魔链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Assassin/0/899 |
| <!-- local:item:621 -->621 | 回生术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/35/304 |
| <!-- local:item:622 -->622 | 震天项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/29/896 |
| <!-- local:item:623 -->623 | 五行神镜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/915 |
| <!-- local:item:624 -->624 | 银镜项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/29/895 |
| <!-- local:item:625 -->625 | 沙漠鱼魔牙齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1152 |
| <!-- local:item:626 -->626 | 武器强化油 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/53 |
| <!-- local:item:627 -->627 | 黑皮手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/32/669 |
| <!-- local:item:628 -->628 | 铁炼腕 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/0/667 |
| <!-- local:item:629 -->629 | 英雄手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/0/666 |
| <!-- local:item:630 -->630 | 生存游戏场地地图4 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/183 |
| <!-- local:item:632 -->632 | 诅咒之药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/64 |
| <!-- local:item:633 -->633 | 强魔震法 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/29/304 |
| <!-- local:item:634 -->634 | 月光鞋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/Wizard/0/1371 |
| <!-- local:item:635 -->635 | 亡灵之药水 | 亡灵之药水 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-skill-activity | 确认保留 | Consumable/All/1/64 |
| <!-- local:item:636 -->636 | 无影靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/Assassin/0/1373 |
| <!-- local:item:637 -->637 | 五彩鞋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/26/1374 |
| <!-- local:item:638 -->638 | 猛虎强势 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/34/304 |
| <!-- local:item:639 -->639 | 仙云靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/Taoist/0/1375 |
| <!-- local:item:640 -->640 | 武神之靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/Warrior/0/1376 |
| <!-- local:item:641 -->641 | 绝地靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/0/1377 |
| <!-- local:item:642 -->642 | 乾坤大挪移（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/42/309 |
| <!-- local:item:645 -->645 | 野山花 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/102 |
| <!-- local:item:646 -->646 | 盔甲蚂蚁卵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/102 |
| <!-- local:item:647 -->647 | 阿才的书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:648 -->648 | 移形换位 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/27/304 |
| <!-- local:item:650 -->650 | 斗转星移（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/46/309 |
| <!-- local:item:651 -->651 | 红娥宝玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1424 |
| <!-- local:item:652 -->652 | 破山剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/300/1041 |
| <!-- local:item:653 -->653 | 阴阳刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/1/1064 |
| <!-- local:item:654 -->654 | 拐杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/1/1087 |
| <!-- local:item:655 -->655 | 铁布衫（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/45/309 |
| <!-- local:item:656 -->656 | 封魔剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/45/1046 |
| <!-- local:item:657 -->657 | 破血狂杀（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/48/309 |
| <!-- local:item:658 -->658 | 花色蜘蛛毒药 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/133 |
| <!-- local:item:659 -->659 | 十方斩（秘籍） | 十方斩（秘籍） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-skill-activity | 确认保留 | Book/Warrior/40/309 |
| <!-- local:item:660 -->660 | 冰沙掌（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/22/304 |
| <!-- local:item:661 -->661 | 魄冰刺（秘籍） | 魄冰刺（秘籍） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-skill-activity | 确认保留 | Book/Wizard/38/309 |
| <!-- local:item:662 -->662 | 震天魔印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1441 |
| <!-- local:item:663 -->663 | 思念珍珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1346 |
| <!-- local:item:664 -->664 | 怒神霹雳（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/40/309 |
| <!-- local:item:665 -->665 | 天神法杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/260/1047 |
| <!-- local:item:666 -->666 | 稻草人木剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1042 |
| <!-- local:item:667 -->667 | 凝血离魂（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/46/309 |
| <!-- local:item:668 -->668 | 云寂术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/38/304 |
| <!-- local:item:669 -->669 | 复血 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/AssWar/35/818 |
| <!-- local:item:670 -->670 | 沃玛头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/21/373 |
| <!-- local:item:671 -->671 | 天藤头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/29/410 |
| <!-- local:item:672 -->672 | 移花接玉（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/40/309 |
| <!-- local:item:673 -->673 | 妙影无踪（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/43/309 |
| <!-- local:item:674 -->674 | 风掌（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/10/304 |
| <!-- local:item:675 -->675 | 阴阳法环（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/46/309 |
| <!-- local:item:676 -->676 | 双刃剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/26/1044 |
| <!-- local:item:677 -->677 | 石人心核 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1449 |
| <!-- local:item:679 -->679 | 龙卷风（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/35/304 |
| <!-- local:item:680 -->680 | 风震天（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/23/304 |
| <!-- local:item:681 -->681 | 击风（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/18/304 |
| <!-- local:item:684 -->684 | 回生术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/35/304 |
| <!-- local:item:685 -->685 | 乾坤一气 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/897 |
| <!-- local:item:690 -->690 | 乾坤大挪移 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/42/309 |
| <!-- local:item:691 -->691 | 斗转星移 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/46/309 |
| <!-- local:item:692 -->692 | 瑕疵黑檀手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/700 |
| <!-- local:item:693 -->693 | 蛇谷老人手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/646 |
| <!-- local:item:694 -->694 | 铁布衫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/45/309 |
| <!-- local:item:695 -->695 | 破血狂杀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/48/309 |
| <!-- local:item:696 -->696 | 强魔震法（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/29/304 |
| <!-- local:item:699 -->699 | 润神戒指（暗黑） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/475 |
| <!-- local:item:700 -->700 | 润神戒指（幻影） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/475 |
| <!-- local:item:701 -->701 | 猛虎强势（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/34/304 |
| <!-- local:item:711 -->711 | 移形换位（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/27/304 |
| <!-- local:item:712 -->712 | 沃毒骷髅戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/532 |
| <!-- local:item:713 -->713 | 白月银蛇戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/19/511 |
| <!-- local:item:714 -->714 | 白眼珍珠戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/19/491 |
| <!-- local:item:715 -->715 | 金刚黑檀手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/16/700 |
| <!-- local:item:716 -->716 | 沃毒小手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/27/660 |
| <!-- local:item:717 -->717 | 沃角手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/16/680 |
| <!-- local:item:718 -->718 | 十方斩 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/40/309 |
| <!-- local:item:719 -->719 | 魄冰刺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/38/309 |
| <!-- local:item:720 -->720 | 怒神霹雳 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/40/309 |
| <!-- local:item:721 -->721 | 凝血离魂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/46/309 |
| <!-- local:item:722 -->722 | 云寂术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/38/304 |
| <!-- local:item:723 -->723 | 移花接玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/40/309 |
| <!-- local:item:724 -->724 | 蓝光凝霜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/28/1212 |
| <!-- local:item:725 -->725 | 红光偃月 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/20/1081 |
| <!-- local:item:726 -->726 | 黑光降魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/20/1101 |
| <!-- local:item:727 -->727 | 诺玛族修罗 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/27/1250 |
| <!-- local:item:728 -->728 | 诅咒银蛇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/27/1231 |
| <!-- local:item:729 -->729 | 诺玛族魔杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/27/1280 |
| <!-- local:item:731 -->731 | 腐烂骷髅头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/35/373 |
| <!-- local:item:732 -->732 | 蓝竹笛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/32/832 |
| <!-- local:item:733 -->733 | 腐烂竹笛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/32/832 |
| <!-- local:item:740 -->740 | 旧放大镜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/26/853 |
| <!-- local:item:741 -->741 | 旧蓝翡翠项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/22/812 |
| <!-- local:item:742 -->742 | 幸运降妖除魔戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/34/474 |
| <!-- local:item:743 -->743 | 炸铜炼狱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/29/1240 |
| <!-- local:item:744 -->744 | 潘夜命运之刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/33/1170 |
| <!-- local:item:745 -->745 | 潘夜银蛇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/31/1233 |
| <!-- local:item:746 -->746 | 潘夜魔杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/31/1281 |
| <!-- local:item:747 -->747 | 沃玛修罗 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/23/1252 |
| <!-- local:item:748 -->748 | 沃玛降魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/23/1163 |
| <!-- local:item:749 -->749 | 沃玛偃月 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/23/1310 |
| <!-- local:item:750 -->750 | 骷髅骨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/103 |
| <!-- local:item:751 -->751 | 虎蛇牙齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1152 |
| <!-- local:item:752 -->752 | 红蛇血 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/31 |
| <!-- local:item:753 -->753 | 祖玛裁决之杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/33/1302 |
| <!-- local:item:754 -->754 | 祖玛无极棍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/33/1260 |
| <!-- local:item:755 -->755 | 祖玛骨玉权杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/33/1193 |
| <!-- local:item:756 -->756 | 童子像 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1420 |
| <!-- local:item:757 -->757 | 竹棍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1421 |
| <!-- local:item:758 -->758 | 牛毛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1422 |
| <!-- local:item:759 -->759 | 苍蝇拍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1423 |
| <!-- local:item:760 -->760 | 制魔宝玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1424 |
| <!-- local:item:761 -->761 | 亮蜡烛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/290 |
| <!-- local:item:762 -->762 | 焰火项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/17/850 |
| <!-- local:item:763 -->763 | 焰火手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/11/700 |
| <!-- local:item:764 -->764 | 闪电眼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/11/511 |
| <!-- local:item:765 -->765 | 灵魂铁手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/10/646 |
| <!-- local:item:766 -->766 | 幻影玉珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/1333 |
| <!-- local:item:767 -->767 | 黑除魔戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/474 |
| <!-- local:item:768 -->768 | 神圣铂金戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/26/493 |
| <!-- local:item:769 -->769 | 亮火把 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/291 |
| <!-- local:item:770 -->770 | 草鞋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/6/1360 |
| <!-- local:item:771 -->771 | 皮靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/16/1361 |
| <!-- local:item:772 -->772 | 赤飞靴子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/33/1363 |
| <!-- local:item:773 -->773 | 黑皮靴子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/45/1364 |
| <!-- local:item:774 -->774 | 天掌靴子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/38/1362 |
| <!-- local:item:775 -->775 | 潘夜珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1349 |
| <!-- local:item:776 -->776 | 潘夜之泪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1348 |
| <!-- local:item:777 -->777 | 夜明珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1350 |
| <!-- local:item:778 -->778 | 超强召唤骷髅 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/33/304 |
| <!-- local:item:779 -->779 | 超强召唤骷髅（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/33/304 |
| <!-- local:item:780 -->780 | 牙齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1431 |
| <!-- local:item:781 -->781 | 祝福霸龙头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/39/412 |
| <!-- local:item:782 -->782 | 古诗秘书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:783 -->783 | 蜘蛛线 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/105 |
| <!-- local:item:784 -->784 | 浓烟黑檀项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/850 |
| <!-- local:item:785 -->785 | 妙影无踪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/43/309 |
| <!-- local:item:786 -->786 | 金创药（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/8 |
| <!-- local:item:787 -->787 | 蝉翼刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1122 |
| <!-- local:item:788 -->788 | 魔法药（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/18 |
| <!-- local:item:789 -->789 | 金创药（特）包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/246 |
| <!-- local:item:790 -->790 | 魔法药（特）包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/256 |
| <!-- local:item:791 -->791 | 耐久铁手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/3/646 |
| <!-- local:item:792 -->792 | 气霖证书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/173 |
| <!-- local:item:793 -->793 | 玉指环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/490 |
| <!-- local:item:794 -->794 | 威魂深怨护身符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/303 |
| <!-- local:item:795 -->795 | 第一困魔石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/216 |
| <!-- local:item:796 -->796 | 第二困魔石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/215 |
| <!-- local:item:797 -->797 | 第三困魔石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/214 |
| <!-- local:item:798 -->798 | 第四困魔石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/213 |
| <!-- local:item:799 -->799 | 最后困魔石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/212 |
| <!-- local:item:800 -->800 | 焱火剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1121 |
| <!-- local:item:801 -->801 | 新火镜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:802 -->802 | 皮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/107 |
| <!-- local:item:803 -->803 | 断交先生的书信 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/172 |
| <!-- local:item:805 -->805 | 灵魂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1441 |
| <!-- local:item:806 -->806 | 阴阳法环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/46/309 |
| <!-- local:item:807 -->807 | 无名油 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/53 |
| <!-- local:item:808 -->808 | 指甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1340 |
| <!-- local:item:809 -->809 | 神灵雕像 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1430 |
| <!-- local:item:810 -->810 | 僵尸骨头 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1149 |
| <!-- local:item:811 -->811 | 护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/330 |
| <!-- local:item:812 -->812 | 灵魂护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/1150 |
| <!-- local:item:813 -->813 | 灵魂护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/1150 |
| <!-- local:item:814 -->814 | 藏罪据证 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1442 |
| <!-- local:item:817 -->817 | 焰天火雨（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/43/309 |
| <!-- local:item:818 -->818 | 霸龙头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Taoist/40/412 |
| <!-- local:item:821 -->821 | 紫水晶矿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ore/All/1/217 |
| <!-- local:item:822 -->822 | 石榴石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ore/All/1/218 |
| <!-- local:item:823 -->823 | 金刚石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ore/All/0/219 |
| <!-- local:item:824 -->824 | 钢玉石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ore/All/0/220 |
| <!-- local:item:825 -->825 | 风之鹤嘴锄 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/10/1048 |
| <!-- local:item:826 -->826 | 跳蚤皮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1444 |
| <!-- local:item:827 -->827 | 诅咒海魂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/11/1080 |
| <!-- local:item:828 -->828 | 潘夜血饮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/34/1083 |
| <!-- local:item:829 -->829 | 诅咒半月 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/11/1100 |
| <!-- local:item:830 -->830 | 潘夜无极棍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/34/1263 |
| <!-- local:item:831 -->831 | 幸运青铜头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/18/370 |
| <!-- local:item:832 -->832 | 幸运斗笠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/33/411 |
| <!-- local:item:833 -->833 | 幸运骷髅头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/38/373 |
| <!-- local:item:834 -->834 | 焰天火雨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/43/309 |
| <!-- local:item:835 -->835 | 师承戒指（冰） | 师承戒指（冰） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/All/45/538 |
| <!-- local:item:836 -->836 | 师承戒指（雷） | 师承戒指（雷） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/All/45/538 |
| <!-- local:item:837 -->837 | 师承戒指（风） | 师承戒指（风） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/All/45/538 |
| <!-- local:item:838 -->838 | 龙鳞战甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/38/982 |
| <!-- local:item:839 -->839 | 龙鳞战甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/38/992 |
| <!-- local:item:840 -->840 | 袁灵法衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/38/1022 |
| <!-- local:item:841 -->841 | 袁灵法衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/38/1032 |
| <!-- local:item:842 -->842 | 天极道衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/38/1002 |
| <!-- local:item:843 -->843 | 天极道衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/38/1012 |
| <!-- local:item:844 -->844 | 帝王戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/AssWar/35/515 |
| <!-- local:item:845 -->845 | 润神戒指（神圣） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/475 |
| <!-- local:item:846 -->846 | 雷神戒指（火） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/857 |
| <!-- local:item:847 -->847 | 武士手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Warrior/35/660 |
| <!-- local:item:848 -->848 | 火玉手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Assassin/35/684 |
| <!-- local:item:849 -->849 | 毁灭手镯（火） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/0/683 |
| <!-- local:item:850 -->850 | 如来手镯（神圣） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/0/663 |
| <!-- local:item:851 -->851 | 钻石项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/13/837 |
| <!-- local:item:852 -->852 | 勇士项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/30/835 |
| <!-- local:item:853 -->853 | 破坏项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/836 |
| <!-- local:item:854 -->854 | 五色项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/19/913 |
| <!-- local:item:855 -->855 | 愤怒之钟（火） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/25/856 |
| <!-- local:item:856 -->856 | 昏暗封印（火） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/816 |
| <!-- local:item:857 -->857 | 真善项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/15/830 |
| <!-- local:item:858 -->858 | 莲花宝镜（神圣） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/25/817 |
| <!-- local:item:859 -->859 | 怨恨项链（神圣） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/815 |
| <!-- local:item:860 -->860 | 指环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/5/530 |
| <!-- local:item:861 -->861 | 神圣护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/335 |
| <!-- local:item:862 -->862 | 神圣护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/335 |
| <!-- local:item:863 -->863 | 火焰护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/331 |
| <!-- local:item:864 -->864 | 寒气护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/332 |
| <!-- local:item:865 -->865 | 霹雷护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/333 |
| <!-- local:item:866 -->866 | 狂风护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/334 |
| <!-- local:item:867 -->867 | 号角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1338 |
| <!-- local:item:868 -->868 | 雪球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DartWeapon/All/1/1320 |
| <!-- local:item:869 -->869 | 诺玛王雕像 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/101 |
| <!-- local:item:888 -->888 | 箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1425 |
| <!-- local:item:889 -->889 | 破军城堡雕像 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1432 |
| <!-- local:item:890 -->890 | 泰轮拂尘 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/260/1106 |
| <!-- local:item:891 -->891 | 师承戒指 | 师承戒指 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/Warrior/45/538 |
| <!-- local:item:892 -->892 | 龙马戒指 | 龙马戒指 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/Wizard/45/518 |
| <!-- local:item:893 -->893 | 青云戒指 | 青云戒指 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/Taoist/45/553 |
| <!-- local:item:894 -->894 | 破荒项链 | 破荒项链 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/AssWar/45/819 |
| <!-- local:item:895 -->895 | 魔云项链 | 魔云项链 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/Wizard/45/859 |
| <!-- local:item:896 -->896 | 定心项链 | 定心项链 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/Taoist/45/839 |
| <!-- local:item:897 -->897 | 缥缈项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/3255 |
| <!-- local:item:898 -->898 | 金棱手镯 | 金棱手镯 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/AssWar/45/685 |
| <!-- local:item:899 -->899 | 思过手镯 | 思过手镯 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/Wizard/45/703 |
| <!-- local:item:900 -->900 | 世尊手镯 | 世尊手镯 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/Taoist/45/725 |
| <!-- local:item:901 -->901 | 缥缈手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/0/3269 |
| <!-- local:item:902 -->902 | 当啷戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/742 |
| <!-- local:item:903 -->903 | 影刺雷戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/45/554 |
| <!-- local:item:904 -->904 | 遗物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1449 |
| <!-- local:item:905 -->905 | 神女书信 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/180 |
| <!-- local:item:906 -->906 | 地图 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/180 |
| <!-- local:item:907 -->907 | 密信 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/180 |
| <!-- local:item:908 -->908 | 养颜长生果 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/86 |
| <!-- local:item:909 -->909 | 比奇城主书信 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/180 |
| <!-- local:item:910 -->910 | 诺玛族信物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1750 |
| <!-- local:item:911 -->911 | 破损古书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1459 |
| <!-- local:item:912 -->912 | 诺玛遗物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1449 |
| <!-- local:item:913 -->913 | 寂幻之刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1075 |
| <!-- local:item:914 -->914 | 血花落照 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/1490 |
| <!-- local:item:915 -->915 | 黑天暗云 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/1491 |
| <!-- local:item:916 -->916 | 九宫云雾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/1492 |
| <!-- local:item:917 -->917 | 万里碧海 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/1493 |
| <!-- local:item:918 -->918 | 影魅之刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1076 |
| <!-- local:item:919 -->919 | 藏宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1425 |
| <!-- local:item:920 -->920 | 红玫瑰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Flower/All/1/88 |
| <!-- local:item:922 -->922 | 喜袋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/133 |
| <!-- local:item:923 -->923 | 血花落照（血） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1470 |
| <!-- local:item:924 -->924 | 血花落照（花） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1471 |
| <!-- local:item:925 -->925 | 血花落照（落） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1472 |
| <!-- local:item:926 -->926 | 血花落照（照） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1473 |
| <!-- local:item:927 -->927 | 黑天暗云（黑） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1474 |
| <!-- local:item:928 -->928 | 黑天暗云（天） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1475 |
| <!-- local:item:929 -->929 | 黑天暗云（暗） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1476 |
| <!-- local:item:930 -->930 | 黑天暗云（云） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1477 |
| <!-- local:item:931 -->931 | 九宫云雾（九） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1480 |
| <!-- local:item:932 -->932 | 九宫云雾（宫） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1481 |
| <!-- local:item:933 -->933 | 九宫云雾（云） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1482 |
| <!-- local:item:934 -->934 | 九宫云雾（雾） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1483 |
| <!-- local:item:935 -->935 | 万里碧海（万） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1484 |
| <!-- local:item:936 -->936 | 万里碧海（里） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1485 |
| <!-- local:item:937 -->937 | 万里碧海（碧） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1486 |
| <!-- local:item:938 -->938 | 万里碧海（海） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1487 |
| <!-- local:item:939 -->939 | 大族长角笛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1146 |
| <!-- local:item:940 -->940 | 遗址雕像 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/101 |
| <!-- local:item:944 -->944 | 通用卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/180 |
| <!-- local:item:945 -->945 | 未鉴定咒恶戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/1/517 |
| <!-- local:item:946 -->946 | 未鉴定神魔手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/1/671 |
| <!-- local:item:947 -->947 | 未鉴定神魔项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/928 |
| <!-- local:item:948 -->948 | 未鉴定龙血鞋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/1/1394 |
| <!-- local:item:949 -->949 | 未鉴定修罗战甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/1/3382 |
| <!-- local:item:950 -->950 | 未鉴定修罗战甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/1/3392 |
| <!-- local:item:951 -->951 | 未鉴定生死轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/1/3451 |
| <!-- local:item:952 -->952 | 未鉴定修罗戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/1/3287 |
| <!-- local:item:953 -->953 | 未鉴定桃源仙甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/2/6000 |
| <!-- local:item:954 -->954 | 未鉴定桃源仙甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/2/6010 |
| <!-- local:item:955 -->955 | 未鉴定桃之蓁蓁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/2/3295 |
| <!-- local:item:956 -->956 | 师承戒指（神圣） | 师承戒指（神圣） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/All/46/538 |
| <!-- local:item:957 -->957 | 师承戒指（暗黑） | 师承戒指（暗黑） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/All/46/538 |
| <!-- local:item:958 -->958 | 龙马戒指（火） | 龙马戒指（火） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/All/46/518 |
| <!-- local:item:959 -->959 | 龙马戒指（冰） | 龙马戒指（冰） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/All/46/518 |
| <!-- local:item:960 -->960 | 龙马戒指（雷） | 龙马戒指（雷） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/All/46/518 |
| <!-- local:item:961 -->961 | 龙马戒指（风） | 龙马戒指（风） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/All/46/518 |
| <!-- local:item:962 -->962 | 青云戒指（神圣） | 青云戒指（神圣） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/All/46/553 |
| <!-- local:item:963 -->963 | 青云戒指（暗黑） | 青云戒指（暗黑） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/All/46/553 |
| <!-- local:item:964 -->964 | 青云戒指（幻影） | 青云戒指（幻影） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-ring | 确认保留 | Ring/All/46/553 |
| <!-- local:item:965 -->965 | 破荒项链（火） | 破荒项链（火） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/All/48/819 |
| <!-- local:item:966 -->966 | 破荒项链（冰） | 破荒项链（冰） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/All/48/819 |
| <!-- local:item:967 -->967 | 破荒项链（雷） | 破荒项链（雷） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/All/48/819 |
| <!-- local:item:968 -->968 | 破荒项链（风） | 破荒项链（风） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/All/48/819 |
| <!-- local:item:969 -->969 | 破荒项链（神圣） | 破荒项链（神圣） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/All/48/819 |
| <!-- local:item:970 -->970 | 破荒项链（暗黑） | 破荒项链（暗黑） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/All/48/819 |
| <!-- local:item:971 -->971 | 魔云项链（火） | 魔云项链（火） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/All/48/859 |
| <!-- local:item:972 -->972 | 魔云项链（冰） | 魔云项链（冰） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/All/48/859 |
| <!-- local:item:973 -->973 | 魔云项链（雷） | 魔云项链（雷） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/All/48/859 |
| <!-- local:item:974 -->974 | 魔云项链（风） | 魔云项链（风） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/All/48/859 |
| <!-- local:item:975 -->975 | 定心项链（神圣） | 定心项链（神圣） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/All/48/839 |
| <!-- local:item:976 -->976 | 定心项链（暗黑） | 定心项链（暗黑） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/All/48/839 |
| <!-- local:item:977 -->977 | 定心项链（幻影） | 定心项链（幻影） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-amulet | 确认保留 | Necklace/All/48/839 |
| <!-- local:item:978 -->978 | 金棱手镯（火） | 金棱手镯（火） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/All/45/685 |
| <!-- local:item:979 -->979 | 金棱手镯（冰） | 金棱手镯（冰） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/All/45/685 |
| <!-- local:item:980 -->980 | 金棱手镯（雷） | 金棱手镯（雷） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/All/45/685 |
| <!-- local:item:981 -->981 | 金棱手镯（风） | 金棱手镯（风） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/All/45/685 |
| <!-- local:item:982 -->982 | 金棱手镯（神圣） | 金棱手镯（神圣） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/All/45/685 |
| <!-- local:item:983 -->983 | 金棱手镯（暗黑） | 金棱手镯（暗黑） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/All/45/685 |
| <!-- local:item:984 -->984 | 思过手镯（火） | 思过手镯（火） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/All/45/703 |
| <!-- local:item:985 -->985 | 思过手镯（冰） | 思过手镯（冰） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/All/45/703 |
| <!-- local:item:986 -->986 | 思过手镯（雷） | 思过手镯（雷） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/All/45/703 |
| <!-- local:item:987 -->987 | 思过手镯（风） | 思过手镯（风） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/All/45/703 |
| <!-- local:item:988 -->988 | 世尊手镯（神圣） | 世尊手镯（神圣） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/All/45/725 |
| <!-- local:item:989 -->989 | 世尊手镯（暗黑） | 世尊手镯（暗黑） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/All/45/725 |
| <!-- local:item:990 -->990 | 世尊手镯（幻影） | 世尊手镯（幻影） | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-items-bracelet | 确认保留 | Bracelet/All/45/725 |
| <!-- local:item:991 -->991 | 生锈师承戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/538 |
| <!-- local:item:992 -->992 | 生锈龙马戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/518 |
| <!-- local:item:993 -->993 | 生锈青云戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/553 |
| <!-- local:item:994 -->994 | 生锈破荒项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/819 |
| <!-- local:item:995 -->995 | 生锈魔云项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/859 |
| <!-- local:item:996 -->996 | 生锈定心项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/839 |
| <!-- local:item:997 -->997 | 生锈金棱手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/685 |
| <!-- local:item:998 -->998 | 生锈思过手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/703 |
| <!-- local:item:999 -->999 | 生锈世尊手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/725 |
| <!-- local:item:1000 -->1000 | 火焰护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/331 |
| <!-- local:item:1001 -->1001 | 寒气护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/332 |
| <!-- local:item:1002 -->1002 | 霹雷护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/333 |
| <!-- local:item:1003 -->1003 | 狂风护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/334 |
| <!-- local:item:1004 -->1004 | 神圣护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/335 |
| <!-- local:item:1005 -->1005 | 护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/330 |
| <!-- local:item:1007 -->1007 | 任务索引 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1469 |
| <!-- local:item:1008 -->1008 | 公文 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/192 |
| <!-- local:item:1009 -->1009 | 肉块 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/300 |
| <!-- local:item:1010 -->1010 | 毁灭之印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1436 |
| <!-- local:item:1012 -->1012 | 尸骨项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1435 |
| <!-- local:item:1013 -->1013 | 击退护身符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1437 |
| <!-- local:item:1014 -->1014 | 未鉴定桃源盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/2/6100 |
| <!-- local:item:1015 -->1015 | 未鉴定桃源靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/2/3319 |
| <!-- local:item:1016 -->1016 | 未鉴定桃源虎翼刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/2/3426 |
| <!-- local:item:1017 -->1017 | 未鉴定桃源曜灵杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/2/3436 |
| <!-- local:item:1018 -->1018 | 未鉴定桃源三焰扇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/2/3447 |
| <!-- local:item:1019 -->1019 | 未鉴定桃之夭夭 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/WarWizTao/2/3293 |
| <!-- local:item:1020 -->1020 | 未鉴定桃之灼灼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/2/3279 |
| <!-- local:item:1021 -->1021 | 元素糖果 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2932 |
| <!-- local:item:1022 -->1022 | 攻击糖果 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2934 |
| <!-- local:item:1023 -->1023 | 未鉴定桃源之心 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/2/3253 |
| <!-- local:item:1024 -->1024 | 未鉴定桃源斩轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/2/3454 |
| <!-- local:item:1025 -->1025 | 书籍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:1026 -->1026 | 神勇之物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/917 |
| <!-- local:item:1027 -->1027 | 节制之物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/765 |
| <!-- local:item:1028 -->1028 | 决断之物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/766 |
| <!-- local:item:1029 -->1029 | 智慧之物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/595 |
| <!-- local:item:1030 -->1030 | 正义之物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/596 |
| <!-- local:item:1031 -->1031 | 投票单 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/192 |
| <!-- local:item:1032 -->1032 | 青空石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1351 |
| <!-- local:item:1033 -->1033 | 大地石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1352 |
| <!-- local:item:1034 -->1034 | 太阳石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1353 |
| <!-- local:item:1035 -->1035 | 月光石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1354 |
| <!-- local:item:1036 -->1036 | 受胎石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1355 |
| <!-- local:item:1037 -->1037 | 安息石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1356 |
| <!-- local:item:1038 -->1038 | 活石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1357 |
| <!-- local:item:1039 -->1039 | 心石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1358 |
| <!-- local:item:1040 -->1040 | 神秘之印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/448 |
| <!-- local:item:1041 -->1041 | 机关零件 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1359 |
| <!-- local:item:1042 -->1042 | 霹雳手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/3/646 |
| <!-- local:item:1043 -->1043 | 碧玉水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/42 |
| <!-- local:item:1044 -->1044 | 猫眼石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1335 |
| <!-- local:item:1045 -->1045 | 养神护身符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/330 |
| <!-- local:item:1046 -->1046 | 冰洁石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1452 |
| <!-- local:item:1047 -->1047 | 卷轴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/206 |
| <!-- local:item:1048 -->1048 | 青蛇眼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/11/511 |
| <!-- local:item:1049 -->1049 | 月影戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/11/491 |
| <!-- local:item:1050 -->1050 | 灵气剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1042 |
| <!-- local:item:1051 -->1051 | 绿水晶项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/11/830 |
| <!-- local:item:1052 -->1052 | 冰月项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/9/471 |
| <!-- local:item:1053 -->1053 | 恋风手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/16/700 |
| <!-- local:item:1054 -->1054 | 呼风手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/10/700 |
| <!-- local:item:1055 -->1055 | 种子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1410 |
| <!-- local:item:1056 -->1056 | 树苗 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/73 |
| <!-- local:item:1057 -->1057 | 肥料 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/74 |
| <!-- local:item:1058 -->1058 | 无名书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1332 |
| <!-- local:item:1059 -->1059 | 调查报告 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:1060 -->1060 | 祖玛宝典 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:1061 -->1061 | 乐透彩票 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/75 |
| <!-- local:item:1062 -->1062 | 天赐战甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/50/984 |
| <!-- local:item:1063 -->1063 | 天赐战甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/50/994 |
| <!-- local:item:1064 -->1064 | 康乃馨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Flower/All/1/76 |
| <!-- local:item:1065 -->1065 | 百里香 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/113 |
| <!-- local:item:1066 -->1066 | 财富之书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/182 |
| <!-- local:item:1067 -->1067 | 解毒药 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/60 |
| <!-- local:item:1068 -->1068 | 金令牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/321 |
| <!-- local:item:1069 -->1069 | 恶狼之血 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/31 |
| <!-- local:item:1070 -->1070 | 森林雪人指甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1431 |
| <!-- local:item:1071 -->1071 | 家谱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:1072 -->1072 | 神秘油 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1341 |
| <!-- local:item:1073 -->1073 | 圣人灵药 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/40 |
| <!-- local:item:1074 -->1074 | 遗失的手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/645 |
| <!-- local:item:1075 -->1075 | 灵药 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/94 |
| <!-- local:item:1076 -->1076 | 史书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:1077 -->1077 | 遗失的斧子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1060 |
| <!-- local:item:1078 -->1078 | 医术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:1079 -->1079 | 火焰沃玛号角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1338 |
| <!-- local:item:1080 -->1080 | 蜜袋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1151 |
| <!-- local:item:1081 -->1081 | 药箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1425 |
| <!-- local:item:1082 -->1082 | 遗失的手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/640 |
| <!-- local:item:1083 -->1083 | 震天魔镜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:1084 -->1084 | 遗失的项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/812 |
| <!-- local:item:1085 -->1085 | 祖玛护法铁锤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1153 |
| <!-- local:item:1086 -->1086 | 血巨人指甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1340 |
| <!-- local:item:1087 -->1087 | 遗失的铁锄 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1040 |
| <!-- local:item:1088 -->1088 | 遗失的头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/370 |
| <!-- local:item:1089 -->1089 | 魔艳项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1335 |
| <!-- local:item:1090 -->1090 | 遗失的护身符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/330 |
| <!-- local:item:1091 -->1091 | 巨象兽牙齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1431 |
| <!-- local:item:1092 -->1092 | 药草 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/70 |
| <!-- local:item:1093 -->1093 | 除魔大师的秘传书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:1094 -->1094 | 素玉戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/530 |
| <!-- local:item:1095 -->1095 | 名册 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:1096 -->1096 | 抛魂铃铛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1520 |
| <!-- local:item:1097 -->1097 | 断了的琵琶弦 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1522 |
| <!-- local:item:1098 -->1098 | 极乐琵琶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1521 |
| <!-- local:item:1099 -->1099 | 噬魂铃铛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1520 |
| <!-- local:item:1100 -->1100 | 麒麟宝铠（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/44/983 |
| <!-- local:item:1101 -->1101 | 麒麟宝铠（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/44/993 |
| <!-- local:item:1102 -->1102 | 仙风神袍（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/44/1023 |
| <!-- local:item:1103 -->1103 | 仙风神袍（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/44/1033 |
| <!-- local:item:1104 -->1104 | 阴阳圣衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/44/1003 |
| <!-- local:item:1105 -->1105 | 阴阳圣衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/44/1013 |
| <!-- local:item:1106 -->1106 | 飞龙剑（火） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1050 |
| <!-- local:item:1107 -->1107 | 飞龙剑（冰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1050 |
| <!-- local:item:1108 -->1108 | 飞龙剑（雷） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1050 |
| <!-- local:item:1109 -->1109 | 飞龙剑（风） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1050 |
| <!-- local:item:1110 -->1110 | 古书籍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:1111 -->1111 | 牛角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1422 |
| <!-- local:item:1112 -->1112 | 地图书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:1113 -->1113 | 碧玉项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/812 |
| <!-- local:item:1114 -->1114 | 旧锤子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1063 |
| <!-- local:item:1115 -->1115 | 诺玛将士药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/62 |
| <!-- local:item:1116 -->1116 | 咒书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:1117 -->1117 | 祖玛雕像碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1338 |
| <!-- local:item:1118 -->1118 | 飞龙剑（神圣） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1050 |
| <!-- local:item:1119 -->1119 | 飞龙剑（元素） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1050 |
| <!-- local:item:1120 -->1120 | 飞龙剑（幻影） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1050 |
| <!-- local:item:1121 -->1121 | 未鉴定黑玉战甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/2/6001 |
| <!-- local:item:1122 -->1122 | 未鉴定黑玉战甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/2/6011 |
| <!-- local:item:1123 -->1123 | 未鉴定沐水璃殇佩 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/3/3571 |
| <!-- local:item:1124 -->1124 | 未鉴定沐水手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/3/3569 |
| <!-- local:item:1125 -->1125 | 经书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1458 |
| <!-- local:item:1126 -->1126 | 金属块 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/108 |
| <!-- local:item:1127 -->1127 | 未鉴定沐水霜晓戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/WarWizTao/3/3567 |
| <!-- local:item:1128 -->1128 | 未鉴定沐水灭魂戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/3/3589 |
| <!-- local:item:1129 -->1129 | 触龙神之钟 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1345 |
| <!-- local:item:1130 -->1130 | 红野猪牙齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1431 |
| <!-- local:item:1131 -->1131 | 飞龙剑碎片（火） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1531 |
| <!-- local:item:1132 -->1132 | 飞龙剑碎片（冰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1532 |
| <!-- local:item:1133 -->1133 | 飞龙剑碎片（雷） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1533 |
| <!-- local:item:1134 -->1134 | 飞龙剑碎片（风） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1534 |
| <!-- local:item:1135 -->1135 | 飞龙剑碎片（神圣） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1535 |
| <!-- local:item:1136 -->1136 | 飞龙剑碎片（元素） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1536 |
| <!-- local:item:1137 -->1137 | 飞龙剑碎片（幻影） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1536 |
| <!-- local:item:1138 -->1138 | 绝世战甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/58/3342 |
| <!-- local:item:1139 -->1139 | 绝世战甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/58/3352 |
| <!-- local:item:1140 -->1140 | 头领证明书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/1435 |
| <!-- local:item:1141 -->1141 | 未鉴定沐水天靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/3/3568 |
| <!-- local:item:1142 -->1142 | 未鉴定沐水天冠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/3/3511 |
| <!-- local:item:1143 -->1143 | 未鉴定龙雀开山钺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/3/3421 |
| <!-- local:item:1144 -->1144 | 未鉴定奕天破邪杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/3/3431 |
| <!-- local:item:1145 -->1145 | 未鉴定秋水无痕剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/3/6220 |
| <!-- local:item:1146 -->1146 | 未鉴定碎情雾影环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/3/3455 |
| <!-- local:item:1147 -->1147 | 未鉴定幻世魔衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/3/2700 |
| <!-- local:item:1148 -->1148 | 未鉴定幻世魔衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/3/2710 |
| <!-- local:item:1149 -->1149 | 未鉴定沐水天衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/3/3325 |
| <!-- local:item:1150 -->1150 | 未鉴定沐水天衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/3/3335 |
| <!-- local:item:1151 -->1151 | 未鉴定蝶恋清寒链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/4/3579 |
| <!-- local:item:1152 -->1152 | 未鉴定玄云碎魄镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/4/3577 |
| <!-- local:item:1153 -->1153 | 未鉴定鹰扬醉舞戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/WarWizTao/4/3575 |
| <!-- local:item:1196 -->1196 | 未鉴定清寒浅浪戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/4/3590 |
| <!-- local:item:1255 -->1255 | 虎齿刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1431 |
| <!-- local:item:1274 -->1274 | 狂暴冲撞 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/99/309 |
| <!-- local:item:1275 -->1275 | 狂暴冲撞（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/99/309 |
| <!-- local:item:1276 -->1276 | 旋风墙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/49/309 |
| <!-- local:item:1277 -->1277 | 旋风墙（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/49/309 |
| <!-- local:item:1278 -->1278 | 灵魂分裂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/39/309 |
| <!-- local:item:1279 -->1279 | 灵魂分裂（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/39/309 |
| <!-- local:item:1280 -->1280 | 暗黑护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/336 |
| <!-- local:item:1281 -->1281 | 暗黑护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/336 |
| <!-- local:item:1282 -->1282 | 泣血花 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/76 |
| <!-- local:item:1283 -->1283 | 急救丸（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/25 |
| <!-- local:item:1284 -->1284 | 急救丸（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/26 |
| <!-- local:item:1285 -->1285 | 急救丸（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/27 |
| <!-- local:item:1286 -->1286 | 急救丸（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/28 |
| <!-- local:item:1287 -->1287 | 清心丸（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/35 |
| <!-- local:item:1288 -->1288 | 清心丸（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/36 |
| <!-- local:item:1289 -->1289 | 清心丸（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/37 |
| <!-- local:item:1290 -->1290 | 清心丸（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/38 |
| <!-- local:item:1291 -->1291 | 金创药（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/9 |
| <!-- local:item:1292 -->1292 | 急救丸（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/29 |
| <!-- local:item:1298 -->1298 | 清心丹（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/35 |
| <!-- local:item:1299 -->1299 | 清心丹（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/36 |
| <!-- local:item:1300 -->1300 | 清心丹（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/37 |
| <!-- local:item:1301 -->1301 | 清心丹（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/38 |
| <!-- local:item:1318 -->1318 | 制炼石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/224 |
| <!-- local:item:1319 -->1319 | 结晶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/221 |
| <!-- local:item:1320 -->1320 | 魔光片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/223 |
| <!-- local:item:1321 -->1321 | 杂货商的旧文件 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:1322 -->1322 | 木制零件 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1570 |
| <!-- local:item:1323 -->1323 | 生锈钉子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1573 |
| <!-- local:item:1324 -->1324 | 未鉴定玄云靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/4/3576 |
| <!-- local:item:1325 -->1325 | 未鉴定玄云盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/4/3470 |
| <!-- local:item:1326 -->1326 | 未鉴定熔金落日刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/4/3428 |
| <!-- local:item:1327 -->1327 | 未鉴定龙破沧溟 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/4/1092 |
| <!-- local:item:1328 -->1328 | 未鉴定天雷真火扇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/4/3448 |
| <!-- local:item:1329 -->1329 | 未鉴定天星耀阳环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/4/3457 |
| <!-- local:item:1330 -->1330 | 慧理的遗骸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1554 |
| <!-- local:item:1331 -->1331 | 药剂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1462 |
| <!-- local:item:1332 -->1332 | 老鼠指甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1453 |
| <!-- local:item:1333 -->1333 | 旧香匣 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1572 |
| <!-- local:item:1334 -->1334 | 旧羊皮纸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1459 |
| <!-- local:item:1335 -->1335 | 未鉴定凶陌圣甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/4/3381 |
| <!-- local:item:1336 -->1336 | 未鉴定凶陌圣甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/4/3391 |
| <!-- local:item:1337 -->1337 | 未鉴定玄云鸾暮铠（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/4/3324 |
| <!-- local:item:1338 -->1338 | 旧梳子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1571 |
| <!-- local:item:1339 -->1339 | 金属板 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1458 |
| <!-- local:item:1340 -->1340 | 钉子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1573 |
| <!-- local:item:1341 -->1341 | 旧箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1425 |
| <!-- local:item:1342 -->1342 | 祖玛教主印记 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1524 |
| <!-- local:item:1343 -->1343 | 生锈金属板 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1458 |
| <!-- local:item:1344 -->1344 | 旧木雕 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1467 |
| <!-- local:item:1345 -->1345 | 内伤治疗剂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1346 |
| <!-- local:item:1346 -->1346 | 记忆之珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1335 |
| <!-- local:item:1347 -->1347 | 结婚礼服 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1032 |
| <!-- local:item:1348 -->1348 | 戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/530 |
| <!-- local:item:1349 -->1349 | 疗伤丹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1145 |
| <!-- local:item:1350 -->1350 | 海西秘记 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:1356 -->1356 | 金牛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1434 |
| <!-- local:item:1357 -->1357 | 山参 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/70 |
| <!-- local:item:1358 -->1358 | 夏马风屠龙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/42/1203 |
| <!-- local:item:1359 -->1359 | 夏马风龙纹剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/42/1223 |
| <!-- local:item:1360 -->1360 | 夏马风嗜魂法杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/42/1273 |
| <!-- local:item:1361 -->1361 | 期望之霹雷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/49/1077 |
| <!-- local:item:1362 -->1362 | 期望之逍遥扇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/49/1107 |
| <!-- local:item:1363 -->1363 | 期望之铁轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/49/1088 |
| <!-- local:item:1364 -->1364 | 潘夜嗜魂法杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1281 |
| <!-- local:item:1365 -->1365 | 潘夜井中月 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/34/1182 |
| <!-- local:item:1366 -->1366 | 天狼刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/1/1078 |
| <!-- local:item:1367 -->1367 | 三台项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/AssWar/55/797 |
| <!-- local:item:1368 -->1368 | 三台手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/AssWar/55/767 |
| <!-- local:item:1369 -->1369 | 三台戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/AssWar/55/597 |
| <!-- local:item:1370 -->1370 | 天丛项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/55/798 |
| <!-- local:item:1371 -->1371 | 天丛手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Taoist/55/768 |
| <!-- local:item:1372 -->1372 | 天丛戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Taoist/55/598 |
| <!-- local:item:1373 -->1373 | 转轮项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Wizard/55/799 |
| <!-- local:item:1374 -->1374 | 转轮手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Wizard/55/769 |
| <!-- local:item:1375 -->1375 | 转轮戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/55/599 |
| <!-- local:item:1376 -->1376 | 礼物箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1506 |
| <!-- local:item:1381 -->1381 | 玄武盾碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3173 |
| <!-- local:item:1382 -->1382 | 稀有书籍残片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:1383 -->1383 | 代书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/204 |
| <!-- local:item:1384 -->1384 | 催眠香 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1558 |
| <!-- local:item:1385 -->1385 | 回信 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1332 |
| <!-- local:item:1386 -->1386 | 金绿玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/223 |
| <!-- local:item:1387 -->1387 | 破旧的地图碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1459 |
| <!-- local:item:1388 -->1388 | 真天宫藏宝图 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/183 |
| <!-- local:item:1389 -->1389 | 古月历 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1457 |
| <!-- local:item:1390 -->1390 | 许可印证 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/264 |
| <!-- local:item:1391 -->1391 | 黄昏泪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1580 |
| <!-- local:item:1392 -->1392 | 黄昏项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1581 |
| <!-- local:item:1393 -->1393 | 雪包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1320 |
| <!-- local:item:1394 -->1394 | 凝血液 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/52 |
| <!-- local:item:1395 -->1395 | 冰晶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1452 |
| <!-- local:item:1396 -->1396 | 金面玉牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1605 |
| <!-- local:item:1397 -->1397 | 赤眼红花蛇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1590 |
| <!-- local:item:1398 -->1398 | 紫云剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1591 |
| <!-- local:item:1399 -->1399 | 封印的乌木箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1592 |
| <!-- local:item:1400 -->1400 | 未鉴定玄云鸾暮铠（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/4/3334 |
| <!-- local:item:1401 -->1401 | 未鉴定幻陌靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/5/1391 |
| <!-- local:item:1402 -->1402 | 未鉴定虎啸项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/WarWizTao/5/3259 |
| <!-- local:item:1403 -->1403 | 未鉴定虎啸手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/WarWizTao/5/3014 |
| <!-- local:item:1404 -->1404 | 未鉴定虎啸戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/WarWizTao/5/3296 |
| <!-- local:item:1405 -->1405 | 未鉴定神魂湮灭剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/5/2550 |
| <!-- local:item:1406 -->1406 | 未鉴定龙吟项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Assassin/5/3247 |
| <!-- local:item:1407 -->1407 | 未鉴定龙吟手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Assassin/5/3271 |
| <!-- local:item:1408 -->1408 | 破碎的红印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1595 |
| <!-- local:item:1409 -->1409 | 红印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1596 |
| <!-- local:item:1410 -->1410 | 破碎的黑印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1597 |
| <!-- local:item:1411 -->1411 | 黑印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1598 |
| <!-- local:item:1412 -->1412 | 触角神魔皮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1599 |
| <!-- local:item:1413 -->1413 | 破碎的白印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1600 |
| <!-- local:item:1414 -->1414 | 白印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1601 |
| <!-- local:item:1415 -->1415 | 破碎的绿印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1602 |
| <!-- local:item:1416 -->1416 | 绿印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1603 |
| <!-- local:item:1417 -->1417 | 无名项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1604 |
| <!-- local:item:1418 -->1418 | 神人项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1604 |
| <!-- local:item:1425 -->1425 | 鸡蛋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1414 |
| <!-- local:item:1434 -->1434 | 煎鸡蛋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1415 |
| <!-- local:item:1435 -->1435 | 黄金蛋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1416 |
| <!-- local:item:1436 -->1436 | 珀玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1343 |
| <!-- local:item:1442 -->1442 | 太极旗 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/1615 |
| <!-- local:item:1443 -->1443 | 旭日戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/AssWar/50/557 |
| <!-- local:item:1444 -->1444 | 霸王项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/AssWar/50/919 |
| <!-- local:item:1445 -->1445 | 登天手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/AssWar/50/688 |
| <!-- local:item:1446 -->1446 | 三桓戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/50/556 |
| <!-- local:item:1447 -->1447 | 避难项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Wizard/50/918 |
| <!-- local:item:1448 -->1448 | 云龙手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Wizard/50/686 |
| <!-- local:item:1449 -->1449 | 继承戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Taoist/50/555 |
| <!-- local:item:1450 -->1450 | 昆仑项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/50/920 |
| <!-- local:item:1451 -->1451 | 至善手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Taoist/50/687 |
| <!-- local:item:1452 -->1452 | 天狼头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/40/355 |
| <!-- local:item:1453 -->1453 | 天狼靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/40/1384 |
| <!-- local:item:1455 -->1455 | 横扫千军 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/54/309 |
| <!-- local:item:1456 -->1456 | 横扫千军（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/54/309 |
| <!-- local:item:1457 -->1457 | 五星牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/78 |
| <!-- local:item:1458 -->1458 | 紫色鸡蛋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1620 |
| <!-- local:item:1459 -->1459 | 粉红色鸡蛋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1621 |
| <!-- local:item:1460 -->1460 | 红色鸡蛋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1622 |
| <!-- local:item:1461 -->1461 | 白色鸡蛋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1623 |
| <!-- local:item:1462 -->1462 | 金色鸡蛋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1624 |
| <!-- local:item:1463 -->1463 | 复活节鸡蛋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1625 |
| <!-- local:item:1469 -->1469 | 祖玛葫芦 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/65 |
| <!-- local:item:1470 -->1470 | 潘夜葫芦 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/65 |
| <!-- local:item:1471 -->1471 | 赤月葫芦 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/65 |
| <!-- local:item:1472 -->1472 | 震天葫芦 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/65 |
| <!-- local:item:1473 -->1473 | 黑度葫芦 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/65 |
| <!-- local:item:1527 -->1527 | 移花接木 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/55/309 |
| <!-- local:item:1528 -->1528 | 移花接木（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/55/3040 |
| <!-- local:item:1529 -->1529 | 陨冰杀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/58/1860 |
| <!-- local:item:1530 -->1530 | 陨冰杀（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/58/3043 |
| <!-- local:item:1531 -->1531 | 焰魔石（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/30/340 |
| <!-- local:item:1532 -->1532 | 焰魔石（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/35/340 |
| <!-- local:item:1533 -->1533 | 焰魔石（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/40/340 |
| <!-- local:item:1534 -->1534 | 焰魔石（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/45/340 |
| <!-- local:item:1535 -->1535 | 马牌（绝影） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/321 |
| <!-- local:item:1536 -->1536 | 马牌（赤兔马） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/321 |
| <!-- local:item:1537 -->1537 | 征服者日志碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:1538 -->1538 | 比奇城设计图 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/181 |
| <!-- local:item:1539 -->1539 | 封印宝剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1043 |
| <!-- local:item:1540 -->1540 | 雷神灵珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1351 |
| <!-- local:item:1541 -->1541 | 神圣灵珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1352 |
| <!-- local:item:1542 -->1542 | 幻影灵珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1353 |
| <!-- local:item:1543 -->1543 | 破坏护身符（雷） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1437 |
| <!-- local:item:1544 -->1544 | 破坏护身符（神圣） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1437 |
| <!-- local:item:1545 -->1545 | 破坏护身符（幻影） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1437 |
| <!-- local:item:1546 -->1546 | 诺玛司令封印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1339 |
| <!-- local:item:1547 -->1547 | 诺玛斧兵心脏 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1347 |
| <!-- local:item:1548 -->1548 | 封印的灭绝刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1160 |
| <!-- local:item:1549 -->1549 | 诺玛族宝物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1425 |
| <!-- local:item:1550 -->1550 | 杀魔血刀戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/AssWar/60/539 |
| <!-- local:item:1551 -->1551 | 师玉戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/60/558 |
| <!-- local:item:1552 -->1552 | 九梦戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Taoist/60/519 |
| <!-- local:item:1553 -->1553 | 杀魔血刀手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/AssWar/60/706 |
| <!-- local:item:1554 -->1554 | 师玉手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Wizard/60/705 |
| <!-- local:item:1555 -->1555 | 九梦手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Taoist/60/704 |
| <!-- local:item:1556 -->1556 | 杀魔血刀项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/AssWar/60/923 |
| <!-- local:item:1557 -->1557 | 师玉项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Wizard/60/922 |
| <!-- local:item:1558 -->1558 | 九梦项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/60/921 |
| <!-- local:item:1559 -->1559 | 雷天鞋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/40/1385 |
| <!-- local:item:1560 -->1560 | 银光鞋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/1/1386 |
| <!-- local:item:1561 -->1561 | 灵云鞋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/1/1387 |
| <!-- local:item:1562 -->1562 | 金刚之躯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/58/1860 |
| <!-- local:item:1563 -->1563 | 金刚之躯（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/58/3043 |
| <!-- local:item:1564 -->1564 | 养生术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/47/309 |
| <!-- local:item:1565 -->1565 | 养生术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/47/309 |
| <!-- local:item:1566 -->1566 | 泰山压顶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/55/309 |
| <!-- local:item:1567 -->1567 | 泰山压顶（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/55/309 |
| <!-- local:item:1568 -->1568 | 快刀斩马 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/52/309 |
| <!-- local:item:1569 -->1569 | 快刀斩马（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/52/309 |
| <!-- local:item:1570 -->1570 | 运气术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/38/309 |
| <!-- local:item:1571 -->1571 | 运气术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/38/309 |
| <!-- local:item:1572 -->1572 | 天打雷劈 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/52/309 |
| <!-- local:item:1573 -->1573 | 天打雷劈（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/52/3040 |
| <!-- local:item:1574 -->1574 | 电闪雷鸣 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/55/1860 |
| <!-- local:item:1575 -->1575 | 电闪雷鸣（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/55/3043 |
| <!-- local:item:1576 -->1576 | 新传染 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/56/1860 |
| <!-- local:item:1577 -->1577 | 新传染（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/56/3043 |
| <!-- local:item:1578 -->1578 | 吸星大法 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/60/1860 |
| <!-- local:item:1579 -->1579 | 吸星大法（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/60/3043 |
| <!-- local:item:1580 -->1580 | 迷魂大法 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/52/309 |
| <!-- local:item:1581 -->1581 | 迷魂大法（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/52/309 |
| <!-- local:item:1584 -->1584 | 光魔石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/223 |
| <!-- local:item:1585 -->1585 | 白光魔石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/225 |
| <!-- local:item:1586 -->1586 | 黑光魔石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/226 |
| <!-- local:item:1587 -->1587 | 初级碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/271 |
| <!-- local:item:1588 -->1588 | 中级碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/272 |
| <!-- local:item:1589 -->1589 | 高级碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/273 |
| <!-- local:item:1590 -->1590 | 超级碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/274 |
| <!-- local:item:1591 -->1591 | 冰魔石（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/30/341 |
| <!-- local:item:1592 -->1592 | 冰魔石（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/35/341 |
| <!-- local:item:1593 -->1593 | 冰魔石（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/40/341 |
| <!-- local:item:1594 -->1594 | 冰魔石（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/45/341 |
| <!-- local:item:1595 -->1595 | 雷魔石（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/30/342 |
| <!-- local:item:1596 -->1596 | 雷魔石（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/35/342 |
| <!-- local:item:1597 -->1597 | 雷魔石（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/40/342 |
| <!-- local:item:1598 -->1598 | 雷魔石（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/45/342 |
| <!-- local:item:1599 -->1599 | 风魔石（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/30/343 |
| <!-- local:item:1600 -->1600 | 风魔石（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/35/343 |
| <!-- local:item:1601 -->1601 | 风魔石（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/40/343 |
| <!-- local:item:1602 -->1602 | 风魔石（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/45/343 |
| <!-- local:item:1603 -->1603 | 护身碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/271 |
| <!-- local:item:1604 -->1604 | 麻痹碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/272 |
| <!-- local:item:1605 -->1605 | 复活碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/273 |
| <!-- local:item:1606 -->1606 | 防御碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/274 |
| <!-- local:item:1607 -->1607 | 8级妖丹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/3580 |
| <!-- local:item:1608 -->1608 | 照妖镜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1449 |
| <!-- local:item:1609 -->1609 | 佛像泪珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1420 |
| <!-- local:item:1610 -->1610 | 铁链锁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1442 |
| <!-- local:item:1611 -->1611 | 魔石狂热者牙齿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1431 |
| <!-- local:item:1612 -->1612 | 自尊石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1358 |
| <!-- local:item:1613 -->1613 | 赤龙剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1121 |
| <!-- local:item:1614 -->1614 | 灵泉水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/60 |
| <!-- local:item:1615 -->1615 | 南襄葫芦 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1555 |
| <!-- local:item:1616 -->1616 | 破血魔镜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/1491 |
| <!-- local:item:1617 -->1617 | 破血魔镜（破） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1474 |
| <!-- local:item:1618 -->1618 | 破血魔镜（血） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1475 |
| <!-- local:item:1619 -->1619 | 破血魔镜（魔） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1476 |
| <!-- local:item:1620 -->1620 | 破血魔镜（镜） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1477 |
| <!-- local:item:1621 -->1621 | 烟花（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1596 |
| <!-- local:item:1622 -->1622 | 烟花（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1596 |
| <!-- local:item:1623 -->1623 | 烟花（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1596 |
| <!-- local:item:1624 -->1624 | 烟花（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1596 |
| <!-- local:item:1625 -->1625 | 桃源仙甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/2/6000 |
| <!-- local:item:1626 -->1626 | 桃源仙甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/2/6010 |
| <!-- local:item:1627 -->1627 | 护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/330 |
| <!-- local:item:1628 -->1628 | 至尊牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/75/79 |
| <!-- local:item:1629 -->1629 | 混元掌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/99/309 |
| <!-- local:item:1630 -->1630 | 混元掌（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/99/309 |
| <!-- local:item:1631 -->1631 | 透心链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/99/309 |
| <!-- local:item:1632 -->1632 | 透心链（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/99/309 |
| <!-- local:item:1633 -->1633 | 魔爆术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/99/309 |
| <!-- local:item:1634 -->1634 | 魔爆术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/99/309 |
| <!-- local:item:1635 -->1635 | 地狱魔焰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/99/309 |
| <!-- local:item:1636 -->1636 | 地狱魔焰（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/99/309 |
| <!-- local:item:1637 -->1637 | 屠龙斩 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/45/309 |
| <!-- local:item:1638 -->1638 | 屠龙斩（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/45/309 |
| <!-- local:item:1639 -->1639 | 旋风斩 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/99/309 |
| <!-- local:item:1640 -->1640 | 旋风斩（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/99/309 |
| <!-- local:item:1641 -->1641 | 君临步 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/45/309 |
| <!-- local:item:1642 -->1642 | 君临步（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/45/309 |
| <!-- local:item:1643 -->1643 | 魔光盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/99/309 |
| <!-- local:item:1644 -->1644 | 魔光盾（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/99/309 |
| <!-- local:item:1645 -->1645 | 焚魂魔功 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/99/309 |
| <!-- local:item:1646 -->1646 | 焚魂魔功（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/99/309 |
| <!-- local:item:1647 -->1647 | 神灵守护 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/99/309 |
| <!-- local:item:1648 -->1648 | 神灵守护（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/99/309 |
| <!-- local:item:1649 -->1649 | 隐魂术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/46/309 |
| <!-- local:item:1650 -->1650 | 隐魂术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/46/309 |
| <!-- local:item:1651 -->1651 | 月明波 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/51/309 |
| <!-- local:item:1652 -->1652 | 月明波（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/51/309 |
| <!-- local:item:1653 -->1653 | 艾娜专用剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/60/1051 |
| <!-- local:item:1661 -->1661 | 褐木白花 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/77 |
| <!-- local:item:1662 -->1662 | 诊断书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/170 |
| <!-- local:item:1663 -->1663 | 凤凰翎毛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/794 |
| <!-- local:item:1664 -->1664 | 白鹿犄角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/71 |
| <!-- local:item:1665 -->1665 | 冰水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/68 |
| <!-- local:item:1666 -->1666 | 震天之珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1335 |
| <!-- local:item:1667 -->1667 | 不死牌碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1147 |
| <!-- local:item:1668 -->1668 | 骷髅教主名册 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1459 |
| <!-- local:item:1669 -->1669 | 赤月之珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1552 |
| <!-- local:item:1670 -->1670 | 祖玛号角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/100 |
| <!-- local:item:1671 -->1671 | 灭绝之剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1591 |
| <!-- local:item:1672 -->1672 | 沙漠白雪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1452 |
| <!-- local:item:1678 -->1678 | 钱票 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/75 |
| <!-- local:item:1702 -->1702 | 修罗戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/551 |
| <!-- local:item:1703 -->1703 | 修罗手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/1/720 |
| <!-- local:item:1714 -->1714 | 修能秘录 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/309 |
| <!-- local:item:1715 -->1715 | 圣诞帽 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/20/356 |
| <!-- local:item:1716 -->1716 | 圣诞节（圣） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1322 |
| <!-- local:item:1717 -->1717 | 圣诞节（诞） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1322 |
| <!-- local:item:1718 -->1718 | 圣诞节（节） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1322 |
| <!-- local:item:1719 -->1719 | 圣诞节（快） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1322 |
| <!-- local:item:1720 -->1720 | 圣诞节（乐） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1322 |
| <!-- local:item:1721 -->1721 | 圣诞卡片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1322 |
| <!-- local:item:1727 -->1727 | 猎犬灵魂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1343 |
| <!-- local:item:1728 -->1728 | 犬公交换券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/264 |
| <!-- local:item:1729 -->1729 | 魔魂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3100 |
| <!-- local:item:1730 -->1730 | 挑战券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/207 |
| <!-- local:item:1742 -->1742 | 护身金甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/40/960 |
| <!-- local:item:1743 -->1743 | 护身金甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/40/970 |
| <!-- local:item:1744 -->1744 | 护身宝甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/40/961 |
| <!-- local:item:1745 -->1745 | 护身宝甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/40/971 |
| <!-- local:item:1746 -->1746 | 勇霖银甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/50/962 |
| <!-- local:item:1747 -->1747 | 勇霖银甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/50/972 |
| <!-- local:item:1748 -->1748 | 勇霖宝甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/52/963 |
| <!-- local:item:1749 -->1749 | 勇霖宝甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/52/973 |
| <!-- local:item:1750 -->1750 | 明光凤衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/52/964 |
| <!-- local:item:1751 -->1751 | 明光凤衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/52/974 |
| <!-- local:item:1752 -->1752 | 赤冠魔衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/52/965 |
| <!-- local:item:1753 -->1753 | 赤冠魔衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/52/975 |
| <!-- local:item:1754 -->1754 | 赤龙神甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/1/3323 |
| <!-- local:item:1755 -->1755 | 赤龙神甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/1/3333 |
| <!-- local:item:1756 -->1756 | 特殊药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/40 |
| <!-- local:item:1775 -->1775 | 地图指南 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/304 |
| <!-- local:item:1788 -->1788 | 付费地下城门票 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7301 |
| <!-- local:item:1789 -->1789 | 木剑（10） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/20/1042 |
| <!-- local:item:1792 -->1792 | 木制短剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/20/1042 |
| <!-- local:item:1793 -->1793 | 足球鞋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/1/1661 |
| <!-- local:item:1794 -->1794 | 足球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/1660 |
| <!-- local:item:1795 -->1795 | 世界杯卡片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1662 |
| <!-- local:item:1797 -->1797 | 黄牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1663 |
| <!-- local:item:1798 -->1798 | 红牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1664 |
| <!-- local:item:1818 -->1818 | 金刚套宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1681 |
| <!-- local:item:1819 -->1819 | 祈祷套宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1682 |
| <!-- local:item:1820 -->1820 | 虹膜套宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1683 |
| <!-- local:item:1821 -->1821 | 魔血套宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1684 |
| <!-- local:item:1822 -->1822 | 记忆套宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7175 |
| <!-- local:item:1823 -->1823 | 战士宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1592 |
| <!-- local:item:1824 -->1824 | 法师宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1592 |
| <!-- local:item:1825 -->1825 | 道士宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1592 |
| <!-- local:item:1826 -->1826 | 经验葫芦（50%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7060 |
| <!-- local:item:1827 -->1827 | 经验葫芦（80%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7061 |
| <!-- local:item:1828 -->1828 | 高级经验葫芦（每周限量） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7061 |
| <!-- local:item:1829 -->1829 | 高级经验葫芦（晚上限量） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7061 |
| <!-- local:item:1830 -->1830 | 经验葫芦（100%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7063 |
| <!-- local:item:1831 -->1831 | 经验葫芦（30%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7062 |
| <!-- local:item:1832 -->1832 | 幸运石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1690 |
| <!-- local:item:1833 -->1833 | 天山雪莲（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/29 |
| <!-- local:item:1834 -->1834 | 天山雪莲（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/10/29 |
| <!-- local:item:1835 -->1835 | 天山雪莲（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/20/29 |
| <!-- local:item:1836 -->1836 | 天山雪莲（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/30/29 |
| <!-- local:item:1837 -->1837 | 深海灵礁（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/39 |
| <!-- local:item:1838 -->1838 | 深海灵礁（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/10/39 |
| <!-- local:item:1839 -->1839 | 深海灵礁（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/20/39 |
| <!-- local:item:1840 -->1840 | 深海灵礁（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/30/39 |
| <!-- local:item:1841 -->1841 | 战士强化药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7030 |
| <!-- local:item:1842 -->1842 | 战士强化药水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/66 |
| <!-- local:item:1843 -->1843 | 法师强化药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7031 |
| <!-- local:item:1844 -->1844 | 法师强化药水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/68 |
| <!-- local:item:1845 -->1845 | 道士强化药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7032 |
| <!-- local:item:1846 -->1846 | 道士强化药水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/67 |
| <!-- local:item:1847 -->1847 | 攻击神水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/55/84 |
| <!-- local:item:1848 -->1848 | 疾风神水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/55/80 |
| <!-- local:item:1849 -->1849 | 自然神水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/55/82 |
| <!-- local:item:1850 -->1850 | 灵魂神水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/55/81 |
| <!-- local:item:1851 -->1851 | 体力强效神水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/55/85 |
| <!-- local:item:1852 -->1852 | 魔力强效神水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/83 |
| <!-- local:item:1853 -->1853 | 火焰护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/331 |
| <!-- local:item:1854 -->1854 | 寒气护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/332 |
| <!-- local:item:1855 -->1855 | 霹雷护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/333 |
| <!-- local:item:1856 -->1856 | 狂风护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/334 |
| <!-- local:item:1857 -->1857 | 暗黑护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/336 |
| <!-- local:item:1858 -->1858 | 传送卷轴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7255 |
| <!-- local:item:1859 -->1859 | 回生战水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/183 |
| <!-- local:item:1860 -->1860 | 回生丸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5040 |
| <!-- local:item:1861 -->1861 | 火魔石（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/50/340 |
| <!-- local:item:1862 -->1862 | 冰魔石（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/50/341 |
| <!-- local:item:1863 -->1863 | 雷魔石（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/50/342 |
| <!-- local:item:1864 -->1864 | 风魔石（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DarkStone/All/50/343 |
| <!-- local:item:1865 -->1865 | 破坏印记（限时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7440 |
| <!-- local:item:1866 -->1866 | 自然印记（限时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7441 |
| <!-- local:item:1867 -->1867 | 灵魂印记（限时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7442 |
| <!-- local:item:1868 -->1868 | 火之印记（限时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7443 |
| <!-- local:item:1869 -->1869 | 冰之印记（限时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7444 |
| <!-- local:item:1870 -->1870 | 雷之印记（限时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7445 |
| <!-- local:item:1871 -->1871 | 风之印记（限时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7446 |
| <!-- local:item:1872 -->1872 | 神圣印记（限时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7447 |
| <!-- local:item:1873 -->1873 | 暗黑印记（限时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7448 |
| <!-- local:item:1874 -->1874 | 首饰特修神水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7001 |
| <!-- local:item:1875 -->1875 | 服饰特修神水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7003 |
| <!-- local:item:1876 -->1876 | 特修神水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7002 |
| <!-- local:item:1877 -->1877 | 红色精炼石（武器） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | RefineSpecial/All/1/7460 |
| <!-- local:item:1878 -->1878 | 制炼石（专业） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/228 |
| <!-- local:item:1879 -->1879 | 灰色精炼石（首饰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | RefineSpecial/All/1/7463 |
| <!-- local:item:1880 -->1880 | 紫色精炼石（首饰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | RefineSpecial/All/1/7464 |
| <!-- local:item:1881 -->1881 | 解毒丸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7020 |
| <!-- local:item:1882 -->1882 | 回生神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7013 |
| <!-- local:item:1883 -->1883 | 回生神水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7013 |
| <!-- local:item:1884 -->1884 | 传音号角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/75 |
| <!-- local:item:1885 -->1885 | 传音书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/75 |
| <!-- local:item:1886 -->1886 | 玩家名称 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7264 |
| <!-- local:item:1887 -->1887 | 雕刻名字工具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7493 |
| <!-- local:item:1888 -->1888 | 改名凭证 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | System/All/1/7266 |
| <!-- local:item:1889 -->1889 | 性别更改凭证 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | System/All/1/7265 |
| <!-- local:item:1890 -->1890 | 沙巴克徽章 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/78 |
| <!-- local:item:1891 -->1891 | 沙漠土城徽章 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/78 |
| <!-- local:item:1896 -->1896 | 超级体力药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/44/83 |
| <!-- local:item:1897 -->1897 | 超级魔法药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/44/85 |
| <!-- local:item:1898 -->1898 | 超级灵魂药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/44/81 |
| <!-- local:item:1899 -->1899 | 超级自然药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/44/82 |
| <!-- local:item:1900 -->1900 | 超级攻击药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/44/84 |
| <!-- local:item:1901 -->1901 | 制炼石（强化） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/227 |
| <!-- local:item:1902 -->1902 | 高级怪物租用 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/207 |
| <!-- local:item:1903 -->1903 | 诺玛套宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1680 |
| <!-- local:item:1908 -->1908 | 召唤强化咒书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7253 |
| <!-- local:item:1909 -->1909 | 火银龙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/60/1051 |
| <!-- local:item:1910 -->1910 | 神符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1592 |
| <!-- local:item:1914 -->1914 | 额外库存 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1709 |
| <!-- local:item:1915 -->1915 | 额外仓库扩展 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7481 |
| <!-- local:item:1916 -->1916 | 白犬租赁卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/260 |
| <!-- local:item:1917 -->1917 | 疾风镐 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/22/1048 |
| <!-- local:item:1918 -->1918 | 武林名宿（证书） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/183 |
| <!-- local:item:1919 -->1919 | 仁义大侠（证书） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/183 |
| <!-- local:item:1920 -->1920 | 英雄豪杰（证书） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/183 |
| <!-- local:item:1921 -->1921 | 武林至尊（证书） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/183 |
| <!-- local:item:1922 -->1922 | 高级经验葫芦（1天） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7061 |
| <!-- local:item:1923 -->1923 | 高级经验葫芦（7天） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7061 |
| <!-- local:item:1924 -->1924 | 高级经验葫芦（14天） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7061 |
| <!-- local:item:1948 -->1948 | 衣服染色液 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | System/All/1/7014 |
| <!-- local:item:1949 -->1949 | 沐水璃殇佩 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/3/3571 |
| <!-- local:item:1953 -->1953 | 沐水手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/3/3569 |
| <!-- local:item:1954 -->1954 | 沐水霜晓戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/WarWizTao/3/3567 |
| <!-- local:item:1955 -->1955 | 沐水灭魂戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/3/3589 |
| <!-- local:item:1956 -->1956 | 沐水天靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/3/3568 |
| <!-- local:item:1957 -->1957 | 蝶恋清寒链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/4/3579 |
| <!-- local:item:1958 -->1958 | 玄云碎魄镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/4/3577 |
| <!-- local:item:1959 -->1959 | 鹰扬醉舞戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/WarWizTao/4/3575 |
| <!-- local:item:1960 -->1960 | 清寒浅浪戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/4/3590 |
| <!-- local:item:1961 -->1961 | 玄云靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/4/3576 |
| <!-- local:item:1962 -->1962 | 黄色玫瑰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/89 |
| <!-- local:item:1963 -->1963 | 绿玫瑰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Flower/All/1/98 |
| <!-- local:item:1964 -->1964 | 蓝玫瑰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Flower/All/1/99 |
| <!-- local:item:1965 -->1965 | 幻陌靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/5/1391 |
| <!-- local:item:1966 -->1966 | 包月收费 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1594 |
| <!-- local:item:1967 -->1967 | 神力戒指-兑换券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/173 |
| <!-- local:item:1968 -->1968 | 探测项链-兑换券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/173 |
| <!-- local:item:1969 -->1969 | 技巧项链-兑换券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/173 |
| <!-- local:item:1970 -->1970 | 传送戒指-兑换券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/173 |
| <!-- local:item:1971 -->1971 | 麻痹戒指-兑换券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/173 |
| <!-- local:item:1972 -->1972 | 护身戒指-兑换券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/173 |
| <!-- local:item:1973 -->1973 | 武器首饰制炼包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/133 |
| <!-- local:item:1974 -->1974 | 红铃铛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1670 |
| <!-- local:item:1975 -->1975 | 蓝铃铛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1671 |
| <!-- local:item:1976 -->1976 | 紫铃铛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1672 |
| <!-- local:item:1977 -->1977 | 冰煤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1436 |
| <!-- local:item:1978 -->1978 | 羽旗（龙） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1056 |
| <!-- local:item:1979 -->1979 | 圣诞手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/1/1673 |
| <!-- local:item:1980 -->1980 | 圣诞鞋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/1/1674 |
| <!-- local:item:1981 -->1981 | 圣诞袜子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1675 |
| <!-- local:item:1989 -->1989 | 饮料（绿） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1665 |
| <!-- local:item:1990 -->1990 | 饮料（蓝） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1666 |
| <!-- local:item:1991 -->1991 | 红色钱包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1323 |
| <!-- local:item:1992 -->1992 | 黄色钱包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1324 |
| <!-- local:item:1993 -->1993 | 神宫传送卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7255 |
| <!-- local:item:1994 -->1994 | 雪原冰宫传送卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/182 |
| <!-- local:item:1995 -->1995 | 神舰传送卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/182 |
| <!-- local:item:1996 -->1996 | 传送石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/4082 |
| <!-- local:item:1997 -->1997 | 防御药水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/11/1 |
| <!-- local:item:1998 -->1998 | 防御药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/22/2 |
| <!-- local:item:1999 -->1999 | 防御药水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/33/3 |
| <!-- local:item:2005 -->2005 | 赤龙佩刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/70/1094 |
| <!-- local:item:2006 -->2006 | 日月戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/AssWar/65/559 |
| <!-- local:item:2007 -->2007 | 日月手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/AssWar/65/689 |
| <!-- local:item:2008 -->2008 | 日月项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/AssWar/65/924 |
| <!-- local:item:2009 -->2009 | 天辉戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/65/560 |
| <!-- local:item:2010 -->2010 | 天辉手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Wizard/65/690 |
| <!-- local:item:2011 -->2011 | 天辉项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Wizard/65/925 |
| <!-- local:item:2012 -->2012 | 消魂戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Taoist/65/561 |
| <!-- local:item:2013 -->2013 | 消魂手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Taoist/65/691 |
| <!-- local:item:2014 -->2014 | 消魂项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/65/926 |
| <!-- local:item:2015 -->2015 | 赤龙戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/70/562 |
| <!-- local:item:2016 -->2016 | 赤龙手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/70/692 |
| <!-- local:item:2017 -->2017 | 赤龙项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/70/927 |
| <!-- local:item:2018 -->2018 | 赤龙靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/70/1392 |
| <!-- local:item:2019 -->2019 | 赤龙头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/1/416 |
| <!-- local:item:2020 -->2020 | 传送圣链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/877 |
| <!-- local:item:2021 -->2021 | 延期丸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/74 |
| <!-- local:item:2022 -->2022 | 玉液琼浆 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7065 |
| <!-- local:item:2023 -->2023 | 陈年佳酿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7064 |
| <!-- local:item:2024 -->2024 | 传奇包（30%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7190 |
| <!-- local:item:2025 -->2025 | 魔气的结晶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1350 |
| <!-- local:item:2026 -->2026 | 还魂花 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1741 |
| <!-- local:item:2027 -->2027 | 战士加强水（限量） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7030 |
| <!-- local:item:2028 -->2028 | 法师加强水（限量） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7031 |
| <!-- local:item:2029 -->2029 | 道士加强水（限量） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7032 |
| <!-- local:item:2034 -->2034 | 初学休眠包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1731 |
| <!-- local:item:2035 -->2035 | 名声号牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1742 |
| <!-- local:item:2036 -->2036 | 强化破坏印记 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1720 |
| <!-- local:item:2037 -->2037 | 强化自然印记 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1721 |
| <!-- local:item:2038 -->2038 | 强化灵魂印记 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1722 |
| <!-- local:item:2039 -->2039 | 强化火印记 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1723 |
| <!-- local:item:2040 -->2040 | 强化冰印记 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1724 |
| <!-- local:item:2041 -->2041 | 强化雷印记 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1725 |
| <!-- local:item:2042 -->2042 | 强化风印记 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1726 |
| <!-- local:item:2043 -->2043 | 强化神圣印记 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1727 |
| <!-- local:item:2044 -->2044 | 强化暗黑印记 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1728 |
| <!-- local:item:2045 -->2045 | 强化幻影印记 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1729 |
| <!-- local:item:2046 -->2046 | 战士技能药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1733 |
| <!-- local:item:2047 -->2047 | 道士技能药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1734 |
| <!-- local:item:2048 -->2048 | 法师技能药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1735 |
| <!-- local:item:2049 -->2049 | 幻影印记（限时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7449 |
| <!-- local:item:2050 -->2050 | 暗黑印记 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1740 |
| <!-- local:item:2051 -->2051 | 册本子（敌人） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/174 |
| <!-- local:item:2052 -->2052 | 册本子（蓝色） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/175 |
| <!-- local:item:2053 -->2053 | 旗子（虎） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1057 |
| <!-- local:item:2054 -->2054 | 幸运包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7191 |
| <!-- local:item:2055 -->2055 | 传送卷轴（合同制） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7255 |
| <!-- local:item:2056 -->2056 | 幸运号码项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7011 |
| <!-- local:item:2057 -->2057 | 幸运油 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7010 |
| <!-- local:item:2058 -->2058 | 冶炼增强箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7150 |
| <!-- local:item:2059 -->2059 | 师傅鞋箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7150 |
| <!-- local:item:2060 -->2060 | 彼岸花 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Flower/All/1/7420 |
| <!-- local:item:2061 -->2061 | 神仙花 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/7421 |
| <!-- local:item:2062 -->2062 | 图像处理芯片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1642 |
| <!-- local:item:2063 -->2063 | LCD支架 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1645 |
| <!-- local:item:2064 -->2064 | NDSL键盘 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1654 |
| <!-- local:item:2065 -->2065 | 存储条 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1652 |
| <!-- local:item:2066 -->2066 | NDSL | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1655 |
| <!-- local:item:2067 -->2067 | NDSLGame包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1656 |
| <!-- local:item:2068 -->2068 | 虎影戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Warrior/1/540 |
| <!-- local:item:2069 -->2069 | 永柳戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Taoist/1/500 |
| <!-- local:item:2070 -->2070 | 咒恶戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/1/517 |
| <!-- local:item:2071 -->2071 | 神魔手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/1/671 |
| <!-- local:item:2072 -->2072 | 纯白天甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/40/673 |
| <!-- local:item:2073 -->2073 | 超月天甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/40/675 |
| <!-- local:item:2074 -->2074 | 枫壁靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/40/1393 |
| <!-- local:item:2075 -->2075 | 神魔项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/928 |
| <!-- local:item:2076 -->2076 | 碧夜军甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/40/670 |
| <!-- local:item:2077 -->2077 | 洁白军甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/40/672 |
| <!-- local:item:2078 -->2078 | 赤月军甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/40/674 |
| <!-- local:item:2079 -->2079 | 凤凰牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/0/322 |
| <!-- local:item:2080 -->2080 | 随机发型 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | System/All/0/7494 |
| <!-- local:item:2081 -->2081 | 光火明珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7064 |
| <!-- local:item:2082 -->2082 | （男）超帅短发 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7494 |
| <!-- local:item:2083 -->2083 | （男）刺猬头型 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1715 |
| <!-- local:item:2084 -->2084 | （男）半扎辩子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7494 |
| <!-- local:item:2085 -->2085 | （女）兔尾辫子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7494 |
| <!-- local:item:2086 -->2086 | （女）兔耳头型 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1715 |
| <!-- local:item:2087 -->2087 | （女）半扎辩头型 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7494 |
| <!-- local:item:2088 -->2088 | 黑犬租赁卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/260 |
| <!-- local:item:2095 -->2095 | 海市蜃楼宝剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1050 |
| <!-- local:item:2096 -->2096 | 攻击水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7015 |
| <!-- local:item:2097 -->2097 | 幻月之书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/183 |
| <!-- local:item:2098 -->2098 | 幻月之剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1042 |
| <!-- local:item:2099 -->2099 | 幻月戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/530 |
| <!-- local:item:2102 -->2102 | 生锈的日月戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/559 |
| <!-- local:item:2103 -->2103 | 裂开的日月戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/559 |
| <!-- local:item:2104 -->2104 | 陈旧的日月戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/559 |
| <!-- local:item:2105 -->2105 | 生锈的日月手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/689 |
| <!-- local:item:2106 -->2106 | 裂开的日月手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/689 |
| <!-- local:item:2107 -->2107 | 陈旧的日月手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/689 |
| <!-- local:item:2108 -->2108 | 划痕之日月手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/689 |
| <!-- local:item:2109 -->2109 | 生锈的日月项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/924 |
| <!-- local:item:2110 -->2110 | 裂开的日月项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/924 |
| <!-- local:item:2111 -->2111 | 陈旧的日月项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/924 |
| <!-- local:item:2112 -->2112 | 生锈的消魂戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/561 |
| <!-- local:item:2113 -->2113 | 裂开的消魂戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/561 |
| <!-- local:item:2114 -->2114 | 陈旧的消魂戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/561 |
| <!-- local:item:2115 -->2115 | 生锈的消魂手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/691 |
| <!-- local:item:2116 -->2116 | 裂开的消魂手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/691 |
| <!-- local:item:2117 -->2117 | 陈旧的消魂手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/691 |
| <!-- local:item:2118 -->2118 | 划痕之消魂手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/691 |
| <!-- local:item:2119 -->2119 | 生锈的消魂项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/926 |
| <!-- local:item:2120 -->2120 | 裂开的消魂项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/926 |
| <!-- local:item:2121 -->2121 | 陈旧的消魂项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/926 |
| <!-- local:item:2122 -->2122 | 生锈的天辉戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/560 |
| <!-- local:item:2123 -->2123 | 裂开的天辉戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/560 |
| <!-- local:item:2124 -->2124 | 陈旧的天辉戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/560 |
| <!-- local:item:2125 -->2125 | 生锈的天辉手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/690 |
| <!-- local:item:2126 -->2126 | 裂开的天辉手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/690 |
| <!-- local:item:2127 -->2127 | 陈旧的天辉手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/690 |
| <!-- local:item:2128 -->2128 | 划痕之天辉手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/690 |
| <!-- local:item:2129 -->2129 | 生锈的天辉项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/925 |
| <!-- local:item:2130 -->2130 | 裂开的天辉项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/925 |
| <!-- local:item:2131 -->2131 | 陈旧的天辉项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/20/925 |
| <!-- local:item:2132 -->2132 | 饼干条 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/115 |
| <!-- local:item:2133 -->2133 | 桃子饼干条 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/116 |
| <!-- local:item:2134 -->2134 | 烫发 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7494 |
| <!-- local:item:2135 -->2135 | （男）碎发 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7494 |
| <!-- local:item:2136 -->2136 | （女）兔耳发型 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7494 |
| <!-- local:item:2137 -->2137 | （女）双辫发型 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7494 |
| <!-- local:item:2138 -->2138 | 龙轮酒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1760 |
| <!-- local:item:2139 -->2139 | 镜面朱砂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1761 |
| <!-- local:item:2140 -->2140 | 雷水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1763 |
| <!-- local:item:2141 -->2141 | 欲望的雷水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1762 |
| <!-- local:item:2142 -->2142 | 忠实的雷水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1764 |
| <!-- local:item:2143 -->2143 | 蚩尤的角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1767 |
| <!-- local:item:2144 -->2144 | 东蚩尤的角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1768 |
| <!-- local:item:2145 -->2145 | 西蚩尤的角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1769 |
| <!-- local:item:2146 -->2146 | 阎昆的绿色碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1766 |
| <!-- local:item:2147 -->2147 | 阎昆的红色碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1765 |
| <!-- local:item:2148 -->2148 | 蚩尤战剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/20/1055 |
| <!-- local:item:2149 -->2149 | 真龙幻剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/50/1050 |
| <!-- local:item:2154 -->2154 | 七面鸟肉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/280 |
| <!-- local:item:2155 -->2155 | 铁甲马铠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | HorseArmour/All/20/1802 |
| <!-- local:item:2156 -->2156 | 银质马铠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | HorseArmour/All/35/1801 |
| <!-- local:item:2157 -->2157 | 黄金马铠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | HorseArmour/All/45/1800 |
| <!-- local:item:2158 -->2158 | 传送助手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7254 |
| <!-- local:item:2159 -->2159 | 感谢包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7192 |
| <!-- local:item:2160 -->2160 | 圣诞祝炮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1595 |
| <!-- local:item:2161 -->2161 | 火焰强玉酒（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7330 |
| <!-- local:item:2162 -->2162 | 寒气强玉酒（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7331 |
| <!-- local:item:2163 -->2163 | 霹雷强玉酒（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7332 |
| <!-- local:item:2164 -->2164 | 狂风强玉酒（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7333 |
| <!-- local:item:2165 -->2165 | 神圣强玉酒（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7334 |
| <!-- local:item:2166 -->2166 | 暗黑强玉酒（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7335 |
| <!-- local:item:2167 -->2167 | 幻影强玉酒（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7336 |
| <!-- local:item:2168 -->2168 | 全效强玉酒（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7337 |
| <!-- local:item:2169 -->2169 | 火焰强玉酒（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7330 |
| <!-- local:item:2170 -->2170 | 寒气强玉酒（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7331 |
| <!-- local:item:2171 -->2171 | 霹雷强玉酒（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7332 |
| <!-- local:item:2172 -->2172 | 狂风强玉酒（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7333 |
| <!-- local:item:2173 -->2173 | 神圣强玉酒（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7334 |
| <!-- local:item:2174 -->2174 | 暗黑强玉酒（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7335 |
| <!-- local:item:2175 -->2175 | 幻影强玉酒（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7336 |
| <!-- local:item:2176 -->2176 | 全效强玉酒（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7337 |
| <!-- local:item:2177 -->2177 | 火焰强玉酒（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7330 |
| <!-- local:item:2178 -->2178 | 寒气强玉酒（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7331 |
| <!-- local:item:2179 -->2179 | 霹雷强玉酒（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7332 |
| <!-- local:item:2180 -->2180 | 狂风强玉酒（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7333 |
| <!-- local:item:2181 -->2181 | 神圣强玉酒（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7334 |
| <!-- local:item:2182 -->2182 | 暗黑强玉酒（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7335 |
| <!-- local:item:2183 -->2183 | 幻影强玉酒（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7336 |
| <!-- local:item:2184 -->2184 | 全效强玉酒（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7337 |
| <!-- local:item:2185 -->2185 | 烦恼药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7012 |
| <!-- local:item:2186 -->2186 | 破气米酒（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1770 |
| <!-- local:item:2187 -->2187 | 魔气米酒（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1771 |
| <!-- local:item:2188 -->2188 | 灵气米酒（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1772 |
| <!-- local:item:2189 -->2189 | 高级体练酒（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1773 |
| <!-- local:item:2190 -->2190 | 高级魔练酒（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1774 |
| <!-- local:item:2191 -->2191 | 狂风药水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1775 |
| <!-- local:item:2192 -->2192 | 战士宝玲水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/Warrior/0/7100 |
| <!-- local:item:2193 -->2193 | 道士宝玲水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/Taoist/0/7102 |
| <!-- local:item:2194 -->2194 | 法师宝玲水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/Wizard/0/7101 |
| <!-- local:item:2195 -->2195 | 召唤之书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1594 |
| <!-- local:item:2196 -->2196 | 心愿箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1506 |
| <!-- local:item:2197 -->2197 | 五龙牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/323 |
| <!-- local:item:2198 -->2198 | 感谢信 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1427 |
| <!-- local:item:2199 -->2199 | 感谢碎片（青） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/274 |
| <!-- local:item:2200 -->2200 | 感谢碎片（紫） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/276 |
| <!-- local:item:2201 -->2201 | 感谢碎片（黑） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/271 |
| <!-- local:item:2202 -->2202 | 感谢碎片（黄） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/272 |
| <!-- local:item:2203 -->2203 | 感谢碎片（红） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/273 |
| <!-- local:item:2204 -->2204 | 5周年纪念箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7150 |
| <!-- local:item:2210 -->2210 | 经验珠（100万） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/45/1833 |
| <!-- local:item:2211 -->2211 | 经验珠（500万） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/47/1832 |
| <!-- local:item:2212 -->2212 | 经验珠（1000万） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/50/1830 |
| <!-- local:item:2213 -->2213 | 50万经验丸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1346 |
| <!-- local:item:2214 -->2214 | 100万经验丸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1346 |
| <!-- local:item:2215 -->2215 | 月饼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/22/1456 |
| <!-- local:item:2249 -->2249 | 龙王项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/931 |
| <!-- local:item:2250 -->2250 | 阿修罗项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/930 |
| <!-- local:item:2251 -->2251 | 夜叉项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/929 |
| <!-- local:item:2255 -->2255 | 龙王戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/541 |
| <!-- local:item:2258 -->2258 | 焰魔召唤术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/50/309 |
| <!-- local:item:2259 -->2259 | 焰魔召唤术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/50/309 |
| <!-- local:item:2264 -->2264 | 污染的苦胆 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1553 |
| <!-- local:item:2265 -->2265 | 大老鼠血 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/50 |
| <!-- local:item:2266 -->2266 | 研究结果样本 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:2267 -->2267 | 嗜血魔兽的心脏 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1142 |
| <!-- local:item:2268 -->2268 | 大老鼠皮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/107 |
| <!-- local:item:2269 -->2269 | 小苗 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/104 |
| <!-- local:item:2270 -->2270 | 礼物箱1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1506 |
| <!-- local:item:2271 -->2271 | 短信 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1427 |
| <!-- local:item:2272 -->2272 | 礼物箱2 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1506 |
| <!-- local:item:2273 -->2273 | 花苗 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/104 |
| <!-- local:item:2277 -->2277 | 体力之铁手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/1/646 |
| <!-- local:item:2278 -->2278 | 魔法之铁手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/1/646 |
| <!-- local:item:2279 -->2279 | 体力之传统项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/3/873 |
| <!-- local:item:2280 -->2280 | 魔法之传统项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/3/873 |
| <!-- local:item:2281 -->2281 | 体力之古铜戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/7/530 |
| <!-- local:item:2282 -->2282 | 魔法之古铜戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/7/530 |
| <!-- local:item:2283 -->2283 | 体力之水晶魔戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/7/490 |
| <!-- local:item:2284 -->2284 | 魔法之水晶魔戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/7/490 |
| <!-- local:item:2285 -->2285 | 体力之六绝星环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/7/510 |
| <!-- local:item:2286 -->2286 | 魔法之六绝星环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/7/510 |
| <!-- local:item:2287 -->2287 | 锋利的匕首 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/3/1045 |
| <!-- local:item:2288 -->2288 | 准确青铜剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/5/1043 |
| <!-- local:item:2289 -->2289 | 速度青铜剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/7/1043 |
| <!-- local:item:2290 -->2290 | 体力之金项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/870 |
| <!-- local:item:2291 -->2291 | 魔法之金项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/870 |
| <!-- local:item:2292 -->2292 | 魔焰强解术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/52/309 |
| <!-- local:item:2293 -->2293 | 魔焰强解术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/52/309 |
| <!-- local:item:2294 -->2294 | 护身丸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/530 |
| <!-- local:item:2295 -->2295 | 体力之青铜头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/9/370 |
| <!-- local:item:2296 -->2296 | 准确之牛角戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/13/470 |
| <!-- local:item:2297 -->2297 | 体力之牛角戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/10/470 |
| <!-- local:item:2298 -->2298 | 准确之短剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/10/1054 |
| <!-- local:item:2299 -->2299 | 敏捷之青铜头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/15/370 |
| <!-- local:item:2300 -->2300 | 祝福之青铜斧 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/14/1060 |
| <!-- local:item:2301 -->2301 | 祝福之半月 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/14/1100 |
| <!-- local:item:2302 -->2302 | 祝福之海魂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/14/1080 |
| <!-- local:item:2303 -->2303 | 高级准确之炼狱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/33/1066 |
| <!-- local:item:2304 -->2304 | 守护之无名刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/33/1062 |
| <!-- local:item:2305 -->2305 | 守护之血饮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/33/1083 |
| <!-- local:item:2350 -->2350 | 信物（红） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1531 |
| <!-- local:item:2351 -->2351 | 信物（青） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1533 |
| <!-- local:item:2352 -->2352 | 信物（黄） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1534 |
| <!-- local:item:2353 -->2353 | 信物（绿） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1535 |
| <!-- local:item:2354 -->2354 | 信物（褐） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1536 |
| <!-- local:item:2355 -->2355 | 信物（紫） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1537 |
| <!-- local:item:2356 -->2356 | 1周年礼物箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1731 |
| <!-- local:item:2787 -->2787 | 龙血头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/66/417 |
| <!-- local:item:2788 -->2788 | 龙血宝甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/66/943 |
| <!-- local:item:2789 -->2789 | 龙血宝甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/66/953 |
| <!-- local:item:2790 -->2790 | 龙血项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/66/933 |
| <!-- local:item:2791 -->2791 | 龙血手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/66/693 |
| <!-- local:item:2792 -->2792 | 龙血戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/66/563 |
| <!-- local:item:2793 -->2793 | 龙血鞋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/1/1394 |
| <!-- local:item:2794 -->2794 | 玄灵天链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/67/929 |
| <!-- local:item:2795 -->2795 | 玄灵魔链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Wizard/67/930 |
| <!-- local:item:2796 -->2796 | 玄灵天环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Taoist/67/694 |
| <!-- local:item:2797 -->2797 | 玄灵魔环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Wizard/67/695 |
| <!-- local:item:2798 -->2798 | 玄灵天戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Taoist/67/564 |
| <!-- local:item:2799 -->2799 | 玄灵魔戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/67/565 |
| <!-- local:item:2800 -->2800 | 青龙原灵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/292 |
| <!-- local:item:2801 -->2801 | 朱雀原灵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/293 |
| <!-- local:item:2802 -->2802 | 玄武原灵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/294 |
| <!-- local:item:2803 -->2803 | 白虎原灵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/295 |
| <!-- local:item:2804 -->2804 | 司马血甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/62/944 |
| <!-- local:item:2805 -->2805 | 司马血甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/62/954 |
| <!-- local:item:2806 -->2806 | 龙魔石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/230 |
| <!-- local:item:2807 -->2807 | 宠物道具碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/231 |
| <!-- local:item:2808 -->2808 | 婚魔石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/232 |
| <!-- local:item:2809 -->2809 | 青铜石手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/3/164 |
| <!-- local:item:2810 -->2810 | 孔雀石手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/3/165 |
| <!-- local:item:2811 -->2811 | 黑檀石手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/3/166 |
| <!-- local:item:2812 -->2812 | 乌金石手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/3/167 |
| <!-- local:item:2813 -->2813 | 生锈魔灵刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/99/1110 |
| <!-- local:item:2814 -->2814 | 火焰魔灵刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1111 |
| <!-- local:item:2815 -->2815 | 寒气魔灵刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/38/1112 |
| <!-- local:item:2816 -->2816 | 霹雷魔灵刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/38/1113 |
| <!-- local:item:2817 -->2817 | 武林宗师的手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/35/761 |
| <!-- local:item:2818 -->2818 | 猫眼石的心脏 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/30/890 |
| <!-- local:item:2819 -->2819 | 玛瑙石手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/3/160 |
| <!-- local:item:2820 -->2820 | 青玉石手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/3/161 |
| <!-- local:item:2821 -->2821 | 水晶石手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/3/162 |
| <!-- local:item:2822 -->2822 | 虎眼石手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/3/163 |
| <!-- local:item:2823 -->2823 | 狂风魔灵刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/38/1114 |
| <!-- local:item:2824 -->2824 | 生锈魔灵枪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/99/1130 |
| <!-- local:item:2825 -->2825 | 火焰魔灵枪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/38/1131 |
| <!-- local:item:2826 -->2826 | 寒气魔灵枪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/38/1132 |
| <!-- local:item:2827 -->2827 | 霹雷魔灵枪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1133 |
| <!-- local:item:2828 -->2828 | 狂风魔灵枪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1134 |
| <!-- local:item:2829 -->2829 | 玄灵之月龙项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Warrior/67/931 |
| <!-- local:item:2830 -->2830 | 玄灵之紫月项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Assassin/67/932 |
| <!-- local:item:2831 -->2831 | 玄灵之月龙手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Warrior/67/696 |
| <!-- local:item:2832 -->2832 | 玄灵之紫月手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Assassin/67/697 |
| <!-- local:item:2833 -->2833 | 玄灵之月龙戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Warrior/67/566 |
| <!-- local:item:2834 -->2834 | 玄灵之紫月戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/67/567 |
| <!-- local:item:2835 -->2835 | 邪魔血刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/50/1123 |
| <!-- local:item:2837 -->2837 | 武林宗师牌（测试） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/40/78 |
| <!-- local:item:2900 -->2900 | 体验之急救丸（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/26 |
| <!-- local:item:2901 -->2901 | 体验之急救丸（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/27 |
| <!-- local:item:2902 -->2902 | 体验之急救丸（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/28 |
| <!-- local:item:2903 -->2903 | 体验之清心丸（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/36 |
| <!-- local:item:2904 -->2904 | 体验之清心丸（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/37 |
| <!-- local:item:2905 -->2905 | 体验之清心丸（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/38 |
| <!-- local:item:2908 -->2908 | 造化药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/54 |
| <!-- local:item:2909 -->2909 | GM道具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1742 |
| <!-- local:item:2910 -->2910 | 幸运水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7010 |
| <!-- local:item:2911 -->2911 | 幸运水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7010 |
| <!-- local:item:2912 -->2912 | 幸运水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7010 |
| <!-- local:item:2913 -->2913 | 幸运水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7010 |
| <!-- local:item:2914 -->2914 | 幸运水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7010 |
| <!-- local:item:2915 -->2915 | 魔法师神位 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/54 |
| <!-- local:item:2916 -->2916 | 收费西沙漠传送卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7301 |
| <!-- local:item:2917 -->2917 | 邪魔炎甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/62/944 |
| <!-- local:item:2918 -->2918 | 邪魔炎甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/62/954 |
| <!-- local:item:2919 -->2919 | 邪魔墨甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/62/944 |
| <!-- local:item:2920 -->2920 | 邪魔墨甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/62/954 |
| <!-- local:item:2921 -->2921 | 邪魔炎刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/50/1123 |
| <!-- local:item:2922 -->2922 | 邪魔墨刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/50/1123 |
| <!-- local:item:2923 -->2923 | 蓝书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/174 |
| <!-- local:item:2924 -->2924 | 自动售货机 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/174 |
| <!-- local:item:2925 -->2925 | 熟练之制造工具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1425 |
| <!-- local:item:2926 -->2926 | 达人之制造工具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1425 |
| <!-- local:item:2927 -->2927 | 名人之制造工具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1425 |
| <!-- local:item:2928 -->2928 | 传说之制造工具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1425 |
| <!-- local:item:2929 -->2929 | 强化护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/330 |
| <!-- local:item:2961 -->2961 | 高级灵魂护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/1150 |
| <!-- local:item:2962 -->2962 | 高级灵魂护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/1150 |
| <!-- local:item:2963 -->2963 | 造化宝轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/40/780 |
| <!-- local:item:2964 -->2964 | 铭刻经文轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/40/781 |
| <!-- local:item:2965 -->2965 | 悔悟轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/40/782 |
| <!-- local:item:2966 -->2966 | 金灵轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/40/783 |
| <!-- local:item:2967 -->2967 | 凡灵轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/40/784 |
| <!-- local:item:2968 -->2968 | 经验葫芦（30%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1686 |
| <!-- local:item:2969 -->2969 | 经验葫芦（60%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7060 |
| <!-- local:item:2970 -->2970 | 爆率葫芦（100%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1686 |
| <!-- local:item:2971 -->2971 | 物品葫芦（120%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7063 |
| <!-- local:item:2972 -->2972 | 超级冰泉圣水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/52 |
| <!-- local:item:2973 -->2973 | 白魔光片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1820 |
| <!-- local:item:2974 -->2974 | 红魔光片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1823 |
| <!-- local:item:2975 -->2975 | 黑魔光片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1821 |
| <!-- local:item:2976 -->2976 | 铁魔光片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1822 |
| <!-- local:item:2977 -->2977 | 青魔光片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1824 |
| <!-- local:item:2978 -->2978 | 润滑剂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/50 |
| <!-- local:item:2979 -->2979 | 圣诞老人 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7022 |
| <!-- local:item:2980 -->2980 | 圣诞节礼物箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7160 |
| <!-- local:item:2981 -->2981 | 长袜子礼物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1675 |
| <!-- local:item:2982 -->2982 | 普通牛骨剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1058 |
| <!-- local:item:2983 -->2983 | 普通牛骨头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/0/378 |
| <!-- local:item:2987 -->2987 | 龙王战靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/1/1387 |
| <!-- local:item:2988 -->2988 | 阿修罗战靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/1/1387 |
| <!-- local:item:2989 -->2989 | 夜叉战靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/1/1387 |
| <!-- local:item:2990 -->2990 | 火焰强玉酒（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7330 |
| <!-- local:item:2991 -->2991 | 寒气强玉酒（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7331 |
| <!-- local:item:2992 -->2992 | 霹雷强玉酒（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7332 |
| <!-- local:item:2993 -->2993 | 狂风强玉酒（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7333 |
| <!-- local:item:2994 -->2994 | 神圣强玉酒（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7334 |
| <!-- local:item:2995 -->2995 | 暗黑强玉酒（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7335 |
| <!-- local:item:2996 -->2996 | 幻影强玉酒（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7336 |
| <!-- local:item:2997 -->2997 | 全效强玉酒（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7337 |
| <!-- local:item:2998 -->2998 | 火焰强玉酒（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7330 |
| <!-- local:item:2999 -->2999 | 寒气强玉酒（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7331 |
| <!-- local:item:3000 -->3000 | 霹雷强玉酒（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7332 |
| <!-- local:item:3001 -->3001 | 狂风强玉酒（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7333 |
| <!-- local:item:3002 -->3002 | 神圣强玉酒（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7334 |
| <!-- local:item:3003 -->3003 | 暗黑强玉酒（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7335 |
| <!-- local:item:3004 -->3004 | 幻影强玉酒（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7336 |
| <!-- local:item:3005 -->3005 | 全效强玉酒（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7337 |
| <!-- local:item:3006 -->3006 | 破气米酒（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1770 |
| <!-- local:item:3007 -->3007 | 魔气米酒（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1771 |
| <!-- local:item:3008 -->3008 | 灵气米酒（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1772 |
| <!-- local:item:3009 -->3009 | 高级体练酒（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1773 |
| <!-- local:item:3010 -->3010 | 高级魔练酒（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1774 |
| <!-- local:item:3011 -->3011 | 狂风药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7095 |
| <!-- local:item:3012 -->3012 | 破气米酒（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1770 |
| <!-- local:item:3013 -->3013 | 魔气米酒（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1771 |
| <!-- local:item:3014 -->3014 | 灵气米酒（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1772 |
| <!-- local:item:3015 -->3015 | 高级体练酒（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1773 |
| <!-- local:item:3016 -->3016 | 高级魔练酒（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1774 |
| <!-- local:item:3017 -->3017 | 狂风药水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7095 |
| <!-- local:item:3018 -->3018 | 破气米酒（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1770 |
| <!-- local:item:3019 -->3019 | 魔气米酒（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1771 |
| <!-- local:item:3020 -->3020 | 灵气米酒（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1772 |
| <!-- local:item:3021 -->3021 | 高级体练酒（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1773 |
| <!-- local:item:3022 -->3022 | 高级魔练酒（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1774 |
| <!-- local:item:3023 -->3023 | 狂风药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7095 |
| <!-- local:item:3024 -->3024 | 破气米酒（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1770 |
| <!-- local:item:3025 -->3025 | 魔气米酒（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1771 |
| <!-- local:item:3026 -->3026 | 灵气米酒（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1772 |
| <!-- local:item:3027 -->3027 | 高级体练酒（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1773 |
| <!-- local:item:3028 -->3028 | 高级魔练酒（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1774 |
| <!-- local:item:3029 -->3029 | 狂风药水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7095 |
| <!-- local:item:3030 -->3030 | 大骷髅骨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/103 |
| <!-- local:item:3031 -->3031 | 银矿石结晶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/211 |
| <!-- local:item:3032 -->3032 | 报恩酒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7080 |
| <!-- local:item:3033 -->3033 | 酒灵球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1758 |
| <!-- local:item:3034 -->3034 | 报恩盒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7151 |
| <!-- local:item:3065 -->3065 | 赤龙城传送券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7255 |
| <!-- local:item:3066 -->3066 | 明光咒衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/50/962 |
| <!-- local:item:3067 -->3067 | 明光咒衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/50/972 |
| <!-- local:item:3068 -->3068 | 赤贯道衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/50/962 |
| <!-- local:item:3069 -->3069 | 赤贯道衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/50/972 |
| <!-- local:item:3070 -->3070 | 经验物品葫芦（50%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7062 |
| <!-- local:item:3071 -->3071 | 尊扬牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/85/328 |
| <!-- local:item:3072 -->3072 | 夏季包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7193 |
| <!-- local:item:3073 -->3073 | 帮派创建申请书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/75 |
| <!-- local:item:3074 -->3074 | 召唤书_护卫武士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1781 |
| <!-- local:item:3075 -->3075 | 召唤书_护卫左使 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1782 |
| <!-- local:item:3076 -->3076 | 经验贮存灌（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1841 |
| <!-- local:item:3077 -->3077 | 经验贮存灌工具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1844 |
| <!-- local:item:3079 -->3079 | 经验贮存灌（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1842 |
| <!-- local:item:3080 -->3080 | 经验贮存灌（中-5个） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7153 |
| <!-- local:item:3081 -->3081 | 经验贮存灌（中-10个） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7152 |
| <!-- local:item:3082 -->3082 | 经验贮存灌工具-重迭测试 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1844 |
| <!-- local:item:3087 -->3087 | 群体斗转星移（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/60/309 |
| <!-- local:item:3088 -->3088 | 铁布衫-强化（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/80/309 |
| <!-- local:item:3089 -->3089 | 护身冰环（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/58/309 |
| <!-- local:item:3090 -->3090 | 天之怒火（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/70/3043 |
| <!-- local:item:3091 -->3091 | 灵魂强化（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/80/309 |
| <!-- local:item:3092 -->3092 | 吸气魔功（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/62/309 |
| <!-- local:item:3093 -->3093 | 幻影护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/337 |
| <!-- local:item:3094 -->3094 | 幻影护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/337 |
| <!-- local:item:3095 -->3095 | 幻影护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/337 |
| <!-- local:item:3096 -->3096 | 幻影护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/337 |
| <!-- local:item:3097 -->3097 | 毒药瓶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Poison/All/1/60 |
| <!-- local:item:3098 -->3098 | 破坏印记（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7450 |
| <!-- local:item:3099 -->3099 | 自然印记（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7451 |
| <!-- local:item:3100 -->3100 | 灵魂印记（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7452 |
| <!-- local:item:3101 -->3101 | 灰色精炼石（首饰）（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | RefineSpecial/All/1/7463 |
| <!-- local:item:3102 -->3102 | 极尊牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/90/329 |
| <!-- local:item:3103 -->3103 | 泰尊牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/100/1870 |
| <!-- local:item:3201 -->3201 | 苹果 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionFood/All/1/86 |
| <!-- local:item:3202 -->3202 | 粽子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionFood/All/1/1321 |
| <!-- local:item:3203 -->3203 | 鲭鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/2850 |
| <!-- local:item:3204 -->3204 | 肉包子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionFood/All/1/2790 |
| <!-- local:item:3205 -->3205 | 鲜肉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionFood/All/1/7511 |
| <!-- local:item:3210 -->3210 | 华丽的皮包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionBag/All/1/7591 |
| <!-- local:item:3211 -->3211 | 高级木箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionBag/All/1/7592 |
| <!-- local:item:3212 -->3212 | 宠物小头带 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionHead/All/1/7570 |
| <!-- local:item:3213 -->3213 | 兔子头带 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionHead/All/1/7571 |
| <!-- local:item:3214 -->3214 | 月河攻击印记（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7440 |
| <!-- local:item:3215 -->3215 | 疾风太阳神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7100 |
| <!-- local:item:3216 -->3216 | 自然太阳神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7101 |
| <!-- local:item:3217 -->3217 | 灵魂太阳神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7102 |
| <!-- local:item:3218 -->3218 | 攻击太阳神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7103 |
| <!-- local:item:3219 -->3219 | 月河攻击强效药水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/83 |
| <!-- local:item:3220 -->3220 | 宠物小背带 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionBack/All/0/7580 |
| <!-- local:item:3221 -->3221 | 初级宠物背包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionBag/All/0/2770 |
| <!-- local:item:3222 -->3222 | 意识药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7024 |
| <!-- local:item:3223 -->3223 | 经验贮存灌（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1842 |
| <!-- local:item:3224 -->3224 | 完整的回收 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1844 |
| <!-- local:item:3225 -->3225 | 经验贮存灌（大-5个） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7153 |
| <!-- local:item:3226 -->3226 | 经验贮存灌（大-10个） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7152 |
| <!-- local:item:3227 -->3227 | 蓝色套装A | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7150 |
| <!-- local:item:3228 -->3228 | 蓝色套装B | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7150 |
| <!-- local:item:3229 -->3229 | 蓝色套装C | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7150 |
| <!-- local:item:3230 -->3230 | 龙穴藏宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1783 |
| <!-- local:item:3231 -->3231 | 高级药水套装 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7150 |
| <!-- local:item:3232 -->3232 | 额外伤害花蜜药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7015 |
| <!-- local:item:3233 -->3233 | 幸运油（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/63 |
| <!-- local:item:3235 -->3235 | 回归凭证 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/201 |
| <!-- local:item:3236 -->3236 | 破坏花蜜药水箱子（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1731 |
| <!-- local:item:3237 -->3237 | 自然花蜜药水箱子（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1731 |
| <!-- local:item:3238 -->3238 | 灵魂花蜜药水箱子（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1731 |
| <!-- local:item:3239 -->3239 | 体力花蜜药水箱子（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1731 |
| <!-- local:item:3240 -->3240 | 魔法花蜜药水箱子（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1731 |
| <!-- local:item:3241 -->3241 | 冬季包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7194 |
| <!-- local:item:3242 -->3242 | 宠物小红帽 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionHead/All/1/7572 |
| <!-- local:item:3243 -->3243 | 宠物小马甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionBack/All/0/7582 |
| <!-- local:item:3244 -->3244 | 服装染剂（白色） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1555 |
| <!-- local:item:3245 -->3245 | 服装染剂（黑色） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1555 |
| <!-- local:item:3246 -->3246 | 服装染剂（红色） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1555 |
| <!-- local:item:3247 -->3247 | 服装染剂（蓝色） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1555 |
| <!-- local:item:3248 -->3248 | 服装染剂（黄色） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1555 |
| <!-- local:item:3249 -->3249 | 服装染剂（绿色） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1555 |
| <!-- local:item:3250 -->3250 | 3月箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7141 |
| <!-- local:item:3251 -->3251 | 4月箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7141 |
| <!-- local:item:3252 -->3252 | 古代国王的密匙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1668 |
| <!-- local:item:3253 -->3253 | 准确花蜜药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7095 |
| <!-- local:item:3254 -->3254 | 灵魂护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/1150 |
| <!-- local:item:3255 -->3255 | 初级经验葫芦（50%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1686 |
| <!-- local:item:3256 -->3256 | 初级疾风太阳神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7100 |
| <!-- local:item:3257 -->3257 | 初级自然太阳神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7101 |
| <!-- local:item:3258 -->3258 | 初级灵魂太阳神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7102 |
| <!-- local:item:3259 -->3259 | 初级攻击太阳神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7103 |
| <!-- local:item:3260 -->3260 | 新手破坏印记（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7450 |
| <!-- local:item:3261 -->3261 | 新手自然印记（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7451 |
| <!-- local:item:3262 -->3262 | 新手灵魂印记（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7452 |
| <!-- local:item:3263 -->3263 | 准确强效药水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/11/62 |
| <!-- local:item:3264 -->3264 | 准确强效药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/22/62 |
| <!-- local:item:3265 -->3265 | 准确强效药水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/33/62 |
| <!-- local:item:3266 -->3266 | 准确强效药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/44/62 |
| <!-- local:item:3267 -->3267 | 强化药水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/11/66 |
| <!-- local:item:3268 -->3268 | 强化药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/22/66 |
| <!-- local:item:3269 -->3269 | 强化药水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/33/66 |
| <!-- local:item:3270 -->3270 | 强化药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/66 |
| <!-- local:item:3271 -->3271 | 强化药水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/66 |
| <!-- local:item:3272 -->3272 | 强化药水（限量） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/66 |
| <!-- local:item:3273 -->3273 | 8月箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7141 |
| <!-- local:item:3274 -->3274 | 湿的武功书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1144 |
| <!-- local:item:3275 -->3275 | 神虎手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/0/665 |
| <!-- local:item:3276 -->3276 | 神虎靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/0/1391 |
| <!-- local:item:3277 -->3277 | 神虎戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/577 |
| <!-- local:item:3278 -->3278 | 神虎项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/892 |
| <!-- local:item:3279 -->3279 | 中秋箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7141 |
| <!-- local:item:3280 -->3280 | 新手经验葫芦（50%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7060 |
| <!-- local:item:3281 -->3281 | 额外仓库II-KEY | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7481 |
| <!-- local:item:3282 -->3282 | 万圣节灯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7520 |
| <!-- local:item:3283 -->3283 | 白色的刀架 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1110 |
| <!-- local:item:3284 -->3284 | 白色的矛架 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1130 |
| <!-- local:item:3295 -->3295 | 传奇盒30天 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7141 |
| <!-- local:item:3296 -->3296 | 火焰宝玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/160 |
| <!-- local:item:3297 -->3297 | 冰霜宝玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/161 |
| <!-- local:item:3298 -->3298 | 雷神宝玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/162 |
| <!-- local:item:3299 -->3299 | 风神宝玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/163 |
| <!-- local:item:3300 -->3300 | 神秘的宝玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/167 |
| <!-- local:item:3301 -->3301 | 钻石水晶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1760 |
| <!-- local:item:3302 -->3302 | 白色打孔水晶（普通） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Drill/All/1/1141 |
| <!-- local:item:3303 -->3303 | 白色打孔水晶（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Drill/All/1/1141 |
| <!-- local:item:3304 -->3304 | 白色打孔水晶（稀世） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Drill/All/1/1141 |
| <!-- local:item:3305 -->3305 | 装备打孔水晶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Drill/All/1/7350 |
| <!-- local:item:3306 -->3306 | 宝石拆除水晶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Drill/All/1/7351 |
| <!-- local:item:3307 -->3307 | 初级准确石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3308 -->3308 | 低级准确石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3309 -->3309 | 中级准确石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3310 -->3310 | 高级准确石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3311 -->3311 | 顶级准确石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3312 -->3312 | 初级疾风石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/160 |
| <!-- local:item:3313 -->3313 | 低级疾风石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/160 |
| <!-- local:item:3314 -->3314 | 中级疾风石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/160 |
| <!-- local:item:3315 -->3315 | 高级疾风石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/160 |
| <!-- local:item:3316 -->3316 | 顶级疾风石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/160 |
| <!-- local:item:3317 -->3317 | 初级生命石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4000 |
| <!-- local:item:3318 -->3318 | 低级生命石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4000 |
| <!-- local:item:3319 -->3319 | 中级生命石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4000 |
| <!-- local:item:3320 -->3320 | 高级生命石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4000 |
| <!-- local:item:3321 -->3321 | 顶级生命石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4000 |
| <!-- local:item:3322 -->3322 | 初级魔法MP石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4001 |
| <!-- local:item:3323 -->3323 | 低级魔法MP石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4001 |
| <!-- local:item:3324 -->3324 | 中级魔法MP石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4001 |
| <!-- local:item:3325 -->3325 | 高级魔法MP石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4001 |
| <!-- local:item:3326 -->3326 | 最高级魔法MP石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4001 |
| <!-- local:item:3327 -->3327 | 初级敏捷石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4002 |
| <!-- local:item:3328 -->3328 | 低级敏捷石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4002 |
| <!-- local:item:3329 -->3329 | 中级敏捷石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4002 |
| <!-- local:item:3330 -->3330 | 高级敏捷石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4002 |
| <!-- local:item:3331 -->3331 | 顶级敏捷石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4002 |
| <!-- local:item:3332 -->3332 | 初级幸运石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/166 |
| <!-- local:item:3333 -->3333 | 低级幸运石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/166 |
| <!-- local:item:3334 -->3334 | 中级幸运石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/166 |
| <!-- local:item:3335 -->3335 | 高级幸运石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/166 |
| <!-- local:item:3336 -->3336 | 最高级幸运石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/166 |
| <!-- local:item:3337 -->3337 | 初级生命HP玉石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4005 |
| <!-- local:item:3338 -->3338 | 低级生命HP玉石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4005 |
| <!-- local:item:3339 -->3339 | 中级生命HP玉石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4005 |
| <!-- local:item:3340 -->3340 | 高级生命HP玉石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4005 |
| <!-- local:item:3341 -->3341 | 最高级生命HP玉石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4005 |
| <!-- local:item:3342 -->3342 | 初级魔法MP玉石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4004 |
| <!-- local:item:3343 -->3343 | 低级魔法MP玉石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4004 |
| <!-- local:item:3344 -->3344 | 中级魔法MP玉石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4004 |
| <!-- local:item:3345 -->3345 | 高级魔法MP玉石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4004 |
| <!-- local:item:3346 -->3346 | 最高级魔法MP玉石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4004 |
| <!-- local:item:3347 -->3347 | 初级防御上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4022 |
| <!-- local:item:3348 -->3348 | 低级防御上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4022 |
| <!-- local:item:3349 -->3349 | 中级防御上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4022 |
| <!-- local:item:3350 -->3350 | 高级防御上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4022 |
| <!-- local:item:3351 -->3351 | 最高级防御上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4022 |
| <!-- local:item:3352 -->3352 | 初级魔防下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4025 |
| <!-- local:item:3353 -->3353 | 低级魔防下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4025 |
| <!-- local:item:3354 -->3354 | 中级魔防下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4025 |
| <!-- local:item:3355 -->3355 | 高级魔防下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4025 |
| <!-- local:item:3356 -->3356 | 顶级魔防下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4025 |
| <!-- local:item:3357 -->3357 | 初级防御下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4023 |
| <!-- local:item:3358 -->3358 | 低级防御下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4023 |
| <!-- local:item:3359 -->3359 | 中级防御下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4023 |
| <!-- local:item:3360 -->3360 | 高级防御下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4023 |
| <!-- local:item:3361 -->3361 | 顶级防御下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4023 |
| <!-- local:item:3362 -->3362 | 初级魔防上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4024 |
| <!-- local:item:3363 -->3363 | 低级魔防上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4024 |
| <!-- local:item:3364 -->3364 | 中级魔防上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4024 |
| <!-- local:item:3365 -->3365 | 高级魔防上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4024 |
| <!-- local:item:3366 -->3366 | 最高级魔防上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4024 |
| <!-- local:item:3367 -->3367 | ★经验葫芦（80%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7060 |
| <!-- local:item:3368 -->3368 | 神圣的汁液 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/10 |
| <!-- local:item:3369 -->3369 | 初级月河攻击上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4032 |
| <!-- local:item:3370 -->3370 | 低级月河攻击上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4032 |
| <!-- local:item:3371 -->3371 | 中级月河攻击上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4032 |
| <!-- local:item:3372 -->3372 | 高级月河攻击上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4032 |
| <!-- local:item:3373 -->3373 | 最高级月河攻击上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4032 |
| <!-- local:item:3374 -->3374 | 初级月河防御上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4031 |
| <!-- local:item:3375 -->3375 | 低级月河防御上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4031 |
| <!-- local:item:3376 -->3376 | 中级月河防御上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4031 |
| <!-- local:item:3377 -->3377 | 高级月河防御上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4031 |
| <!-- local:item:3378 -->3378 | 最高级月河防御上限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4031 |
| <!-- local:item:3379 -->3379 | 初级月河防御下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4030 |
| <!-- local:item:3380 -->3380 | 低级月河防御下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4030 |
| <!-- local:item:3381 -->3381 | 中级月河防御下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4030 |
| <!-- local:item:3382 -->3382 | 高级月河防御下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4030 |
| <!-- local:item:3383 -->3383 | 最高级月河防御下限石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4030 |
| <!-- local:item:3384 -->3384 | 初级（技能MP减少）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4040 |
| <!-- local:item:3385 -->3385 | 低级（技能MP减少）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4040 |
| <!-- local:item:3386 -->3386 | 中级（技能MP减少）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4040 |
| <!-- local:item:3387 -->3387 | 高级（技能MP减少）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4040 |
| <!-- local:item:3388 -->3388 | 最高级（技能MP减少）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4040 |
| <!-- local:item:3389 -->3389 | 初级（烈火剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3390 -->3390 | 低级（烈火剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3391 -->3391 | 中级（烈火剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3392 -->3392 | 高级（烈火剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3393 -->3393 | 顶级（烈火剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3394 -->3394 | 初级（翔空剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3395 -->3395 | 低级（翔空剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3396 -->3396 | 中级（翔空剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3397 -->3397 | 高级（翔空剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3398 -->3398 | 最高级（翔空剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3399 -->3399 | 初级（莲月剑法法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3400 -->3400 | 低级（莲月剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3401 -->3401 | 中级（莲月剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3402 -->3402 | 高级（莲月剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3403 -->3403 | 最高级（莲月剑法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3404 -->3404 | 初级（十方斩）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3405 -->3405 | 低级（十方斩）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3406 -->3406 | 中级（十方斩）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3407 -->3407 | 高级（十方斩）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3408 -->3408 | 顶级（十方斩）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3409 -->3409 | 初级（快刀斩马）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3410 -->3410 | 低级（快刀斩马）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3411 -->3411 | 中级（快刀斩马）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3412 -->3412 | 高级（快刀斩马）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3413 -->3413 | 顶级（快刀斩马）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3414 -->3414 | 初级（火球术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3415 -->3415 | 低级（火球术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3416 -->3416 | 中级（火球术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3417 -->3417 | 高级（火球术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3418 -->3418 | 最高级（火球术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3419 -->3419 | 初级（大火球）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3420 -->3420 | 低级（大火球）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3421 -->3421 | 中级（大火球）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3422 -->3422 | 高级（大火球）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3423 -->3423 | 最高级（大火球）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3424 -->3424 | 初级（地狱火）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3425 -->3425 | 低级（地狱火）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3426 -->3426 | 中级（地狱火）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3427 -->3427 | 高级（地狱火）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3428 -->3428 | 最高级（地狱火）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3429 -->3429 | 初级（火墙）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3430 -->3430 | 低级（火墙）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3431 -->3431 | 中级（火墙）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3432 -->3432 | 高级（火墙）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3433 -->3433 | 最高级（火墙）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3434 -->3434 | 初级（爆裂火焰）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4041 |
| <!-- local:item:3435 -->3435 | 低级（爆裂火焰）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4041 |
| <!-- local:item:3436 -->3436 | 中级（爆裂火焰）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4041 |
| <!-- local:item:3437 -->3437 | 高级（爆裂火焰）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4041 |
| <!-- local:item:3438 -->3438 | 最高级（爆裂火焰）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4041 |
| <!-- local:item:3439 -->3439 | 初级（焰天火雨）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3440 -->3440 | 低级（焰天火雨）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3441 -->3441 | 中级（焰天火雨）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3442 -->3442 | 高级（焰天火雨）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3443 -->3443 | 顶级（焰天火雨）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3444 -->3444 | 初级（天之怒火）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3445 -->3445 | 低级（天之怒火）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3446 -->3446 | 中级（天之怒火）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3447 -->3447 | 高级（天之怒火）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3448 -->3448 | 最高级（天之怒火）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3449 -->3449 | 初级（冰月神掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3450 -->3450 | 低级（冰月神掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3451 -->3451 | 中级（冰月神掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3452 -->3452 | 高级（冰月神掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3453 -->3453 | 最高级（冰月神掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3454 -->3454 | 初级（冰月震天）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3455 -->3455 | 低级（冰月震天）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3456 -->3456 | 中级（冰月震天）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3457 -->3457 | 高级（冰月震天）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3458 -->3458 | 最高级（冰月震天）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3459 -->3459 | 初级（冰咆哮）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4042 |
| <!-- local:item:3460 -->3460 | 低级（冰咆哮）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4042 |
| <!-- local:item:3461 -->3461 | 中级（冰咆哮）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4042 |
| <!-- local:item:3462 -->3462 | 高级（冰咆哮）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4042 |
| <!-- local:item:3463 -->3463 | 最高级（冰咆哮）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4042 |
| <!-- local:item:3464 -->3464 | 初级（魄冰刺）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3465 -->3465 | 低级（魄冰刺）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3466 -->3466 | 中级（魄冰刺）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3467 -->3467 | 高级（魄冰刺）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3468 -->3468 | 最高级（魄冰刺）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3469 -->3469 | 初级（霹雳掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3470 -->3470 | 低级（霹雳掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3471 -->3471 | 中级（霹雳掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3472 -->3472 | 高级（霹雳掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3473 -->3473 | 最高级（霹雳掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3474 -->3474 | 初级（雷电术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3475 -->3475 | 低级（雷电术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3476 -->3476 | 中级（雷电术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3477 -->3477 | 高级（雷电术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3478 -->3478 | 顶级（雷电术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3479 -->3479 | 初级（疾光电影）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3480 -->3480 | 低级（疾光电影）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3481 -->3481 | 中级（疾光电影）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3482 -->3482 | 高级（疾光电影）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3483 -->3483 | 最高级（疾光电影）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3484 -->3484 | 初级（地狱雷光）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4043 |
| <!-- local:item:3485 -->3485 | 低级（地狱雷光）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4043 |
| <!-- local:item:3486 -->3486 | 中级（地狱雷光）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4043 |
| <!-- local:item:3487 -->3487 | 高级（地狱雷光）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4043 |
| <!-- local:item:3488 -->3488 | 最高级（地狱雷光）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4043 |
| <!-- local:item:3489 -->3489 | 初级（怒神霹雳）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3490 -->3490 | 低级（怒神霹雳）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3491 -->3491 | 中级（怒神霹雳）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3492 -->3492 | 高级（怒神霹雳）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3493 -->3493 | 顶级（怒神霹雳）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3494 -->3494 | 初级（天打雷劈）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3495 -->3495 | 低级（天打雷劈）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3496 -->3496 | 中级（天打雷劈）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3497 -->3497 | 高级（天打雷劈）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3498 -->3498 | 最高级（天打雷劈）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3499 -->3499 | 初级（电闪雷鸣）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3500 -->3500 | 低级（电闪雷鸣）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3501 -->3501 | 中级（电闪雷鸣）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3502 -->3502 | 高级（电闪雷鸣）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3503 -->3503 | 最高级（电闪雷鸣）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3504 -->3504 | 初级（风掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3505 -->3505 | 低级（风掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3506 -->3506 | 中级（风掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3507 -->3507 | 高级（风掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3508 -->3508 | 最高级（风掌）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3509 -->3509 | 初级（抗拒火环）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3510 -->3510 | 低级（抗拒火环）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3511 -->3511 | 中级（抗拒火环）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3512 -->3512 | 高级（抗拒火环）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3513 -->3513 | 最高级（抗拒火环）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3514 -->3514 | 初级（击风）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3515 -->3515 | 低级（击风）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3516 -->3516 | 中级（击风）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3517 -->3517 | 高级（击风）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3518 -->3518 | 最高级（击风）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3519 -->3519 | 初级（风震天）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3520 -->3520 | 低级（风震天）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3521 -->3521 | 中级（风震天）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3522 -->3522 | 高级（风震天）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3523 -->3523 | 最高级（风震天）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3524 -->3524 | 初级（龙卷风）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4044 |
| <!-- local:item:3525 -->3525 | 低级（龙卷风）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4044 |
| <!-- local:item:3526 -->3526 | 中级（龙卷风）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4044 |
| <!-- local:item:3527 -->3527 | 高级（龙卷风）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4044 |
| <!-- local:item:3528 -->3528 | 最高级（龙卷风）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4044 |
| <!-- local:item:3529 -->3529 | 初级（灵魂火符）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3530 -->3530 | 低级（灵魂火符）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3531 -->3531 | 中级（灵魂火符）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3532 -->3532 | 高级（灵魂火符）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3533 -->3533 | 顶级（灵魂火符）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3534 -->3534 | 初级（月魂断玉）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3535 -->3535 | 低级（月魂断玉）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3536 -->3536 | 中级（月魂断玉）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3537 -->3537 | 高级（月魂断玉）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3538 -->3538 | 最高级（月魂断玉）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3539 -->3539 | 初级（月魂灵波）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4045 |
| <!-- local:item:3540 -->3540 | 低级（月魂灵波）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4045 |
| <!-- local:item:3541 -->3541 | 中级（月魂灵波）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4045 |
| <!-- local:item:3542 -->3542 | 高级（月魂灵波）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4045 |
| <!-- local:item:3543 -->3543 | 顶级（月魂灵波）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4045 |
| <!-- local:item:3544 -->3544 | 初级（空拳刀法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3545 -->3545 | 低级（空拳刀法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3546 -->3546 | 中级（空拳刀法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3547 -->3547 | 高级（空拳刀法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3548 -->3548 | 最高级（空拳刀法）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3549 -->3549 | 初级（吸星术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3550 -->3550 | 低级（吸星术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3551 -->3551 | 中级（吸星术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3552 -->3552 | 高级（吸星术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3553 -->3553 | 最高级（吸星术）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3554 -->3554 | 初级（灭魂火符）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4046 |
| <!-- local:item:3555 -->3555 | 低级（灭魂火符）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4046 |
| <!-- local:item:3556 -->3556 | 中级（灭魂火符）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4046 |
| <!-- local:item:3557 -->3557 | 高级（灭魂火符）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4046 |
| <!-- local:item:3558 -->3558 | 最高级（灭魂火符）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4046 |
| <!-- local:item:3559 -->3559 | 初级（横扫千军）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3560 -->3560 | 低级（横扫千军）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3561 -->3561 | 中级（横扫千军）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3562 -->3562 | 高级（横扫千军）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3563 -->3563 | 最高级（横扫千军）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3564 -->3564 | 初级（吸气魔功）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3565 -->3565 | 低级（吸气魔功）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3566 -->3566 | 中级（吸气魔功）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3567 -->3567 | 高级（吸气魔功）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3568 -->3568 | 最高级（吸气魔功）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3569 -->3569 | 初级（盛开）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3570 -->3570 | 低级（盛开）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3571 -->3571 | 中级（盛开）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3572 -->3572 | 高级（盛开）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3573 -->3573 | 最高级（盛开）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3574 -->3574 | 初级（白莲）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3575 -->3575 | 低级（白莲）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3576 -->3576 | 中级（白莲）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3577 -->3577 | 高级（白莲）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3578 -->3578 | 最高级（白莲）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3579 -->3579 | 初级（红莲）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3580 -->3580 | 低级（红莲）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3581 -->3581 | 中级（红莲）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3582 -->3582 | 高级（红莲）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3583 -->3583 | 最高级（红莲）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3584 -->3584 | 初级（月季）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3585 -->3585 | 低级（月季）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3586 -->3586 | 中级（月季）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3587 -->3587 | 高级（月季）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3588 -->3588 | 最高级（月季）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3589 -->3589 | 初级（孽报）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3590 -->3590 | 低级（孽报）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3591 -->3591 | 中级（孽报）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3592 -->3592 | 高级（孽报）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3593 -->3593 | 最高级（孽报）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3594 -->3594 | 初级（狂涛涌泉）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3595 -->3595 | 低级（狂涛涌泉）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3596 -->3596 | 中级（狂涛涌泉）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3597 -->3597 | 高级（狂涛涌泉）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3598 -->3598 | 最高级（狂涛涌泉）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4048 |
| <!-- local:item:3599 -->3599 | 初级（日闪）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3600 -->3600 | 低级（日闪）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3601 -->3601 | 中级（日闪）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3602 -->3602 | 高级（日闪）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3603 -->3603 | 最高级（日闪）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3604 -->3604 | 初级（魔龙诀）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3605 -->3605 | 低级（魔龙诀）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3606 -->3606 | 中级（魔龙诀）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3607 -->3607 | 高级（魔龙诀）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3608 -->3608 | 最高级（魔龙诀）石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Gem/All/1/4003 |
| <!-- local:item:3609 -->3609 | 霹雷弹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DartWeapon/All/40/1850 |
| <!-- local:item:3610 -->3610 | 火焰弹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DartWeapon/All/40/1851 |
| <!-- local:item:3611 -->3611 | 白冰弹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DartWeapon/All/0/1852 |
| <!-- local:item:3612 -->3612 | 雷电弹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DartWeapon/All/40/1853 |
| <!-- local:item:3613 -->3613 | 飞风弹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DartWeapon/All/40/1854 |
| <!-- local:item:3614 -->3614 | 暗黑弹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DartWeapon/All/40/1855 |
| <!-- local:item:3615 -->3615 | 幻影弹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DartWeapon/All/40/1856 |
| <!-- local:item:3616 -->3616 | 束缚弹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DartWeapon/All/40/1857 |
| <!-- local:item:3617 -->3617 | 血管的心脏 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1858 |
| <!-- local:item:3618 -->3618 | 永龙血玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/231 |
| <!-- local:item:3619 -->3619 | 首饰冶炼锡 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7195 |
| <!-- local:item:3620 -->3620 | 首饰冶炼锡（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1601 |
| <!-- local:item:3621 -->3621 | 首饰冶炼锡（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1603 |
| <!-- local:item:3622 -->3622 | 首饰冶炼锡（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1603 |
| <!-- local:item:3623 -->3623 | 首饰冶炼锡（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1603 |
| <!-- local:item:3624 -->3624 | 炼制结晶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1602 |
| <!-- local:item:3625 -->3625 | 大韩的灯火 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1615 |
| <!-- local:item:3626 -->3626 | 首饰冶炼锡（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1601 |
| <!-- local:item:3631 -->3631 | 螭龙的血液 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/65 |
| <!-- local:item:3632 -->3632 | 审判司长的钥匙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1769 |
| <!-- local:item:3633 -->3633 | 首饰冶炼守护石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/212 |
| <!-- local:item:3634 -->3634 | 上贤的盒子（战士） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2941 |
| <!-- local:item:3635 -->3635 | 上贤的盒子（法师） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2941 |
| <!-- local:item:3636 -->3636 | 上贤的盒子（道士） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2941 |
| <!-- local:item:3637 -->3637 | 上贤的盒子（刺客） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2941 |
| <!-- local:item:3638 -->3638 | 新手技巧项链（限期） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/891 |
| <!-- local:item:3643 -->3643 | ♣经验葫芦（80%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1687 |
| <!-- local:item:3654 -->3654 | 副本重制卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7251 |
| <!-- local:item:3662 -->3662 | 黑龙包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7196 |
| <!-- local:item:3743 -->3743 | 天雷锤（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/70/3043 |
| <!-- local:item:3744 -->3744 | 离魂邪风（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/83/309 |
| <!-- local:item:3745 -->3745 | 定身斗术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/83/309 |
| <!-- local:item:3765 -->3765 | 神秘的金属雕塑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2639 |
| <!-- local:item:3766 -->3766 | 紫水晶的精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/217 |
| <!-- local:item:3767 -->3767 | 石榴石精华 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/218 |
| <!-- local:item:3768 -->3768 | 钢玉石碎石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/219 |
| <!-- local:item:3769 -->3769 | 硬玉的精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/220 |
| <!-- local:item:3770 -->3770 | 红毒之护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5280 |
| <!-- local:item:3771 -->3771 | 红毒之火护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5281 |
| <!-- local:item:3772 -->3772 | 红毒之冰护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5282 |
| <!-- local:item:3773 -->3773 | 红毒之雷护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5283 |
| <!-- local:item:3774 -->3774 | 红毒之风护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5284 |
| <!-- local:item:3775 -->3775 | 红毒之神圣护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5285 |
| <!-- local:item:3776 -->3776 | 红毒之暗黑护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5286 |
| <!-- local:item:3777 -->3777 | 红毒之幻影护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5287 |
| <!-- local:item:3778 -->3778 | 绿毒之护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5290 |
| <!-- local:item:3779 -->3779 | 绿毒之火护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5291 |
| <!-- local:item:3780 -->3780 | 绿毒之冰护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5292 |
| <!-- local:item:3781 -->3781 | 绿毒之雷护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5293 |
| <!-- local:item:3782 -->3782 | 绿毒之风护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5294 |
| <!-- local:item:3783 -->3783 | 绿毒之神圣护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5295 |
| <!-- local:item:3784 -->3784 | 绿毒之暗黑护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5296 |
| <!-- local:item:3785 -->3785 | 绿毒之幻影护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5297 |
| <!-- local:item:3786 -->3786 | 万能符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5300 |
| <!-- local:item:3787 -->3787 | 火万能符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5301 |
| <!-- local:item:3788 -->3788 | 冰万能符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5302 |
| <!-- local:item:3789 -->3789 | 雷万能符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5303 |
| <!-- local:item:3790 -->3790 | 风万能符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5304 |
| <!-- local:item:3791 -->3791 | 神圣万能符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5305 |
| <!-- local:item:3792 -->3792 | 暗黑万能符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5306 |
| <!-- local:item:3793 -->3793 | 幻影护身符（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5307 |
| <!-- local:item:3794 -->3794 | 红毒之护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5280 |
| <!-- local:item:3795 -->3795 | 红毒之火护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5281 |
| <!-- local:item:3796 -->3796 | 红毒之冰护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5282 |
| <!-- local:item:3797 -->3797 | 红毒之雷护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5283 |
| <!-- local:item:3798 -->3798 | 红毒之风护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5284 |
| <!-- local:item:3799 -->3799 | 红毒之神圣护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5285 |
| <!-- local:item:3800 -->3800 | 红毒之暗黑护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5286 |
| <!-- local:item:3801 -->3801 | 红毒之幻影护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5287 |
| <!-- local:item:3802 -->3802 | 绿毒之护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5290 |
| <!-- local:item:3803 -->3803 | 绿毒之火护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5291 |
| <!-- local:item:3804 -->3804 | 绿毒之冰护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5292 |
| <!-- local:item:3805 -->3805 | 绿毒之雷护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5293 |
| <!-- local:item:3806 -->3806 | 绿毒之风护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5294 |
| <!-- local:item:3807 -->3807 | 绿毒之神圣护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5295 |
| <!-- local:item:3808 -->3808 | 绿毒之暗黑护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5296 |
| <!-- local:item:3809 -->3809 | 绿毒之幻影护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5297 |
| <!-- local:item:3810 -->3810 | 万能符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5300 |
| <!-- local:item:3811 -->3811 | 火万能符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5301 |
| <!-- local:item:3812 -->3812 | 冰万能符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5302 |
| <!-- local:item:3813 -->3813 | 雷万能符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5303 |
| <!-- local:item:3814 -->3814 | 风万能符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5304 |
| <!-- local:item:3815 -->3815 | 神圣万能符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5305 |
| <!-- local:item:3816 -->3816 | 暗黑万能符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5306 |
| <!-- local:item:3817 -->3817 | 幻影护身符（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5307 |
| <!-- local:item:3818 -->3818 | 红毒之护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5280 |
| <!-- local:item:3819 -->3819 | 红毒之火护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5281 |
| <!-- local:item:3820 -->3820 | 红毒之冰护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5282 |
| <!-- local:item:3821 -->3821 | 红毒之雷护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5283 |
| <!-- local:item:3822 -->3822 | 红毒之风护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5284 |
| <!-- local:item:3823 -->3823 | 红毒之神圣护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5285 |
| <!-- local:item:3824 -->3824 | 红毒之暗黑护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5286 |
| <!-- local:item:3825 -->3825 | 红毒之幻影护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5287 |
| <!-- local:item:3826 -->3826 | 绿毒之护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5290 |
| <!-- local:item:3827 -->3827 | 绿毒之火护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5291 |
| <!-- local:item:3828 -->3828 | 绿毒之冰护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5292 |
| <!-- local:item:3829 -->3829 | 绿毒之雷护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5293 |
| <!-- local:item:3830 -->3830 | 绿毒之风护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5294 |
| <!-- local:item:3831 -->3831 | 绿毒之神圣护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5295 |
| <!-- local:item:3832 -->3832 | 绿毒之暗黑护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5296 |
| <!-- local:item:3833 -->3833 | 绿毒之幻影护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5297 |
| <!-- local:item:3834 -->3834 | 万能符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5300 |
| <!-- local:item:3835 -->3835 | 火万能符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5301 |
| <!-- local:item:3836 -->3836 | 冰万能符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5302 |
| <!-- local:item:3837 -->3837 | 雷万能符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5303 |
| <!-- local:item:3838 -->3838 | 风万能符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5304 |
| <!-- local:item:3839 -->3839 | 神圣万能符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5305 |
| <!-- local:item:3840 -->3840 | 暗黑万能符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5306 |
| <!-- local:item:3841 -->3841 | 幻影护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5307 |
| <!-- local:item:3842 -->3842 | 红毒之护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5280 |
| <!-- local:item:3843 -->3843 | 红毒之火护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5281 |
| <!-- local:item:3844 -->3844 | 红毒之冰护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5282 |
| <!-- local:item:3845 -->3845 | 红毒之雷护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5283 |
| <!-- local:item:3846 -->3846 | 红毒之风护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5284 |
| <!-- local:item:3847 -->3847 | 红毒之神圣护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5285 |
| <!-- local:item:3848 -->3848 | 红毒之暗黑护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5286 |
| <!-- local:item:3849 -->3849 | 红毒之幻影护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5287 |
| <!-- local:item:3850 -->3850 | 绿毒之护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5290 |
| <!-- local:item:3851 -->3851 | 绿毒之火护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5291 |
| <!-- local:item:3852 -->3852 | 绿毒之冰护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5292 |
| <!-- local:item:3853 -->3853 | 绿毒之雷护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5293 |
| <!-- local:item:3854 -->3854 | 绿毒之风护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5294 |
| <!-- local:item:3855 -->3855 | 绿毒之神圣护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5295 |
| <!-- local:item:3856 -->3856 | 绿毒之暗黑护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5296 |
| <!-- local:item:3857 -->3857 | 绿毒之幻影护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5297 |
| <!-- local:item:3858 -->3858 | 万能符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/7290 |
| <!-- local:item:3859 -->3859 | 火万能符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5301 |
| <!-- local:item:3860 -->3860 | 冰万能符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5302 |
| <!-- local:item:3861 -->3861 | 雷万能符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5303 |
| <!-- local:item:3862 -->3862 | 风万能符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5304 |
| <!-- local:item:3863 -->3863 | 神圣万能符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5305 |
| <!-- local:item:3864 -->3864 | 暗黑万能符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5306 |
| <!-- local:item:3865 -->3865 | 幻影护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5307 |
| <!-- local:item:3881 -->3881 | 无敌（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/58/309 |
| <!-- local:item:3882 -->3882 | 护身法盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/62/1860 |
| <!-- local:item:3883 -->3883 | 护身法盾（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/62/3043 |
| <!-- local:item:3884 -->3884 | 传染 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/65/309 |
| <!-- local:item:3885 -->3885 | 传染（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/65/309 |
| <!-- local:item:3935 -->3935 | 一个古老的月光箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1592 |
| <!-- local:item:4001 -->4001 | 平凡的鱼竿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/20/2800 |
| <!-- local:item:4010 -->4010 | 姜太公的保佑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7556 |
| <!-- local:item:4011 -->4011 | 基本的钓鱼钩 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Hook/All/1/2830 |
| <!-- local:item:4012 -->4012 | 荧光线轴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Reel/All/1/7555 |
| <!-- local:item:4013 -->4013 | 钓鱼初学者线轴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Reel/All/1/7552 |
| <!-- local:item:4014 -->4014 | 诱饵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bait/All/1/7553 |
| <!-- local:item:4015 -->4015 | 鱼群探测器 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Finder/All/1/7554 |
| <!-- local:item:4016 -->4016 | 加强的钓鱼钩 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Hook/All/1/2830 |
| <!-- local:item:4031 -->4031 | 钓鱼服（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/1/2810 |
| <!-- local:item:4032 -->4032 | 钓鱼服（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/1/2820 |
| <!-- local:item:4033 -->4033 | 泸鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/2851 |
| <!-- local:item:4034 -->4034 | 黄桑鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/2852 |
| <!-- local:item:4035 -->4035 | 虾虎鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/2853 |
| <!-- local:item:4036 -->4036 | 黄鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/2854 |
| <!-- local:item:4037 -->4037 | 未鉴定法-幻殇碧陌铠（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/5/3360 |
| <!-- local:item:4038 -->4038 | 未鉴定法-幻殇碧陌铠（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/5/3370 |
| <!-- local:item:4039 -->4039 | 未鉴定龙吟戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/5/3286 |
| <!-- local:item:4040 -->4040 | 未鉴定慧明之杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/5/3438 |
| <!-- local:item:4041 -->4041 | 未鉴定天赋神剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/5/6200 |
| <!-- local:item:4042 -->4042 | 未鉴定万古道兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/5/3441 |
| <!-- local:item:4043 -->4043 | 未鉴定圣火盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/5/3480 |
| <!-- local:item:4044 -->4044 | 未鉴定战-幻殇碧陌铠（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/5/3340 |
| <!-- local:item:4045 -->4045 | 未鉴定战-幻殇碧陌铠（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/5/3350 |
| <!-- local:item:4046 -->4046 | 未鉴定幻陌盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/5/3531 |
| <!-- local:item:4047 -->4047 | 未鉴定刺客-银月泣影甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/5/2004 |
| <!-- local:item:4048 -->4048 | 未鉴定刺客-银月泣影甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/5/2014 |
| <!-- local:item:4049 -->4049 | 未鉴定道-幻殇碧陌铠（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/5/3362 |
| <!-- local:item:4050 -->4050 | 未鉴定道-幻殇碧陌铠（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/5/3372 |
| <!-- local:item:4055 -->4055 | 海星 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/2991 |
| <!-- local:item:4056 -->4056 | 贝壳 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2995 |
| <!-- local:item:4057 -->4057 | 水草 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/2990 |
| <!-- local:item:4073 -->4073 | 回生神水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/64 |
| <!-- local:item:4074 -->4074 | 小天使头带 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionHead/All/1/2750 |
| <!-- local:item:4075 -->4075 | 小兔子发带 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionHead/All/1/2751 |
| <!-- local:item:4076 -->4076 | 天使的翅膀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionBack/All/0/2752 |
| <!-- local:item:4077 -->4077 | 罕见的红色鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2996 |
| <!-- local:item:4078 -->4078 | 罕见的蓝色鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2997 |
| <!-- local:item:4079 -->4079 | 小天使头带（1日） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionHead/All/0/2750 |
| <!-- local:item:4080 -->4080 | 天使的翅膀（1日） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionBack/All/0/2752 |
| <!-- local:item:4081 -->4081 | 小兔子发带（1日） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionHead/All/0/2751 |
| <!-- local:item:4082 -->4082 | 小龙虾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2994 |
| <!-- local:item:4083 -->4083 | 内功IP恢复药水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3090 |
| <!-- local:item:4084 -->4084 | 内功IP恢复药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3091 |
| <!-- local:item:4085 -->4085 | 内功IP恢复药水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3092 |
| <!-- local:item:4086 -->4086 | 内功IP恢复药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3093 |
| <!-- local:item:4087 -->4087 | 内功IP恢复药水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3094 |
| <!-- local:item:4361 -->4361 | 设计师的密匙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1448 |
| <!-- local:item:4362 -->4362 | 未知的项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/25/810 |
| <!-- local:item:4363 -->4363 | 未知的手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/25/648 |
| <!-- local:item:4364 -->4364 | 未知的戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/50/471 |
| <!-- local:item:4365 -->4365 | 月光镜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/50/2600 |
| <!-- local:item:4366 -->4366 | 月光轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/50/2620 |
| <!-- local:item:4367 -->4367 | 月光环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/50/2610 |
| <!-- local:item:4368 -->4368 | 空破斩（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/70/309 |
| <!-- local:item:4369 -->4369 | 联雷击（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/90/309 |
| <!-- local:item:4370 -->4370 | 暗鬼阵（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/70/3043 |
| <!-- local:item:4372 -->4372 | 赤龙门主袍（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/947 |
| <!-- local:item:4373 -->4373 | 赤龙门主袍（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/957 |
| <!-- local:item:4374 -->4374 | 移花接木-强化（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/82/309 |
| <!-- local:item:4375 -->4375 | 电闪雷鸣-强化（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/82/309 |
| <!-- local:item:4376 -->4376 | 阴阳法环-强化（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/82/309 |
| <!-- local:item:4378 -->4378 | 龙论族的血 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/2 |
| <!-- local:item:4379 -->4379 | 金刚石碎片（三） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1432 |
| <!-- local:item:4380 -->4380 | 金刚石碎片（型） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1432 |
| <!-- local:item:4381 -->4381 | 金刚石碎片（太） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1432 |
| <!-- local:item:4382 -->4382 | 金刚石碎片（阵） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1432 |
| <!-- local:item:4383 -->4383 | 金刚石碎片（干） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1432 |
| <!-- local:item:4384 -->4384 | 神秘的沙子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/130 |
| <!-- local:item:4385 -->4385 | 强盗的剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1043 |
| <!-- local:item:4386 -->4386 | 大老鼠指甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1340 |
| <!-- local:item:4387 -->4387 | 白马的血 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/31 |
| <!-- local:item:4388 -->4388 | 致命的蝎子尾巴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/112 |
| <!-- local:item:4389 -->4389 | 泰山红蛇皮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1765 |
| <!-- local:item:4396 -->4396 | 幸运硬币 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7504 |
| <!-- local:item:4397 -->4397 | 混沦盒子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7170 |
| <!-- local:item:4495 -->4495 | 千年冰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1452 |
| <!-- local:item:4496 -->4496 | 血色的千年冰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1563 |
| <!-- local:item:4497 -->4497 | 武林补给箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1425 |
| <!-- local:item:4498 -->4498 | 装备特殊属性修炼石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4011 |
| <!-- local:item:4499 -->4499 | 新手武器制炼石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/224 |
| <!-- local:item:4500 -->4500 | 新手祝福油 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/63 |
| <!-- local:item:4501 -->4501 | 新手战士头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Warrior/22/359 |
| <!-- local:item:4502 -->4502 | 新手法师头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Wizard/22/358 |
| <!-- local:item:4503 -->4503 | 新手道士头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Taoist/22/357 |
| <!-- local:item:4505 -->4505 | 新手旋风流星刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/22/1049 |
| <!-- local:item:4506 -->4506 | 新手嗜魂法杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/22/1085 |
| <!-- local:item:4507 -->4507 | 新手逍遥扇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/22/1107 |
| <!-- local:item:4509 -->4509 | 新手战士盔甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/22/983 |
| <!-- local:item:4510 -->4510 | 新手战士盔甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/22/993 |
| <!-- local:item:4511 -->4511 | 新手法师法衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/22/1023 |
| <!-- local:item:4512 -->4512 | 新手法师法衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/22/1033 |
| <!-- local:item:4513 -->4513 | 新手道士道衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/22/1003 |
| <!-- local:item:4514 -->4514 | 新手道士道衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/22/1013 |
| <!-- local:item:4517 -->4517 | 新手项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/22/875 |
| <!-- local:item:4518 -->4518 | 新手手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/22/675 |
| <!-- local:item:4519 -->4519 | 新手戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/22/551 |
| <!-- local:item:4520 -->4520 | 新手靴子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/22/1381 |
| <!-- local:item:4521 -->4521 | 传奇宝箱（5） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1506 |
| <!-- local:item:4522 -->4522 | 副本奖励 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7161 |
| <!-- local:item:4523 -->4523 | 蜷腹鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/3000 |
| <!-- local:item:4524 -->4524 | 红鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/3001 |
| <!-- local:item:4525 -->4525 | 海马 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/3002 |
| <!-- local:item:4526 -->4526 | 灯笼饿鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/3003 |
| <!-- local:item:4527 -->4527 | 紫珊瑚 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/3004 |
| <!-- local:item:4528 -->4528 | 饿鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/3005 |
| <!-- local:item:4529 -->4529 | 水蛇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/3006 |
| <!-- local:item:4530 -->4530 | 毒淡鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/3007 |
| <!-- local:item:4531 -->4531 | 水甲虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/3008 |
| <!-- local:item:4532 -->4532 | 角牛的遗骸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/103 |
| <!-- local:item:4533 -->4533 | 湖底蓝鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/3009 |
| <!-- local:item:4534 -->4534 | 归还包（通用） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7199 |
| <!-- local:item:4535 -->4535 | 稀世武器修炼石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | RefineSpecial/All/1/7460 |
| <!-- local:item:4631 -->4631 | 幻魔盔甲盒（3日） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1667 |
| <!-- local:item:4672 -->4672 | 赤矿石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/230 |
| <!-- local:item:4673 -->4673 | 鸡血石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/231 |
| <!-- local:item:4678 -->4678 | 初始化宝石（可选） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Drill/All/1/7351 |
| <!-- local:item:4679 -->4679 | 防御精通（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/70/309 |
| <!-- local:item:4680 -->4680 | 物理抵抗（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/80/309 |
| <!-- local:item:4681 -->4681 | 魔法抵抗（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/80/309 |
| <!-- local:item:4686 -->4686 | 虚弱化（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/80/309 |
| <!-- local:item:4687 -->4687 | 灵魂共鸣（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/84/309 |
| <!-- local:item:4688 -->4688 | 活体引燃（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/76/309 |
| <!-- local:item:4689 -->4689 | 冰雨（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/58/309 |
| <!-- local:item:4690 -->4690 | 炎狱精水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1418 |
| <!-- local:item:4691 -->4691 | 铁块 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/229 |
| <!-- local:item:4736 -->4736 | 半兽勇士的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4737 -->4737 | 巨型多角虫力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4738 -->4738 | 骷髅精灵的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4739 -->4739 | 尸王的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4740 -->4740 | 蚂蚁将军的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4741 -->4741 | 红甲虫的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4742 -->4742 | 沃玛卫士的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4743 -->4743 | 邪恶钳虫的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4744 -->4744 | 白野猪的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4745 -->4745 | 骨鬼将的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4746 -->4746 | 八角首领的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4747 -->4747 | 僵尸鬼的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4748 -->4748 | 吸血鬼的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4749 -->4749 | 大法老的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4750 -->4750 | 神鬼王的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4751 -->4751 | 护法天的力量精水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4752 -->4752 | 潘夜鬼将的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4753 -->4753 | 疯狂魔神盗的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4754 -->4754 | 黑度首将的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4755 -->4755 | 霸王守卫的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4756 -->4756 | 震天首将的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4757 -->4757 | 诺玛突击队长的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4758 -->4758 | 魔石守护神的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4759 -->4759 | 灵牛鬼将的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4760 -->4760 | 暗影鬼卒的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4761 -->4761 | 沃玛教主的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4762 -->4762 | 骷髅教主的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4763 -->4763 | 触龙神的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4764 -->4764 | 超级黑野猪的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4765 -->4765 | 赤月恶魔的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4766 -->4766 | 潘夜牛魔王的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4767 -->4767 | 祖玛教主的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4768 -->4768 | 霸王教主的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4769 -->4769 | 震天魔神的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4770 -->4770 | 火影的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4771 -->4771 | 天龙窝主的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4772 -->4772 | 魔王力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4773 -->4773 | 金牛大将军力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4774 -->4774 | 黎明女王的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4775 -->4775 | 赤龙魔王的力量精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3037 |
| <!-- local:item:4784 -->4784 | 高级武器修炼石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | RefineSpecial/All/1/7461 |
| <!-- local:item:4785 -->4785 | 石马死亡心脏 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1142 |
| <!-- local:item:4786 -->4786 | 坐标传送符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/7300 |
| <!-- local:item:4787 -->4787 | 坐标追加宝石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7530 |
| <!-- local:item:4790 -->4790 | 老指甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1453 |
| <!-- local:item:4791 -->4791 | 月族的勋章 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1142 |
| <!-- local:item:4792 -->4792 | 青岩龙的鳍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/112 |
| <!-- local:item:4793 -->4793 | 生锈的红龙戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Warrior/68/2612 |
| <!-- local:item:4794 -->4794 | 武功秘籍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/309 |
| <!-- local:item:4795 -->4795 | 水晶项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/3015 |
| <!-- local:item:4796 -->4796 | 水晶手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/0/3014 |
| <!-- local:item:4797 -->4797 | 桃之蓁蓁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/2/3295 |
| <!-- local:item:4798 -->4798 | 虎啸项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/WarWizTao/5/3259 |
| <!-- local:item:4799 -->4799 | 虎啸手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/WarWizTao/5/3014 |
| <!-- local:item:4800 -->4800 | 虎啸戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/WarWizTao/5/3296 |
| <!-- local:item:4801 -->4801 | 点火石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/160 |
| <!-- local:item:4802 -->4802 | 水晶原石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/222 |
| <!-- local:item:4803 -->4803 | 红绿色的夜明珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/3039 |
| <!-- local:item:4804 -->4804 | 蓝色水晶（初级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/5074 |
| <!-- local:item:4805 -->4805 | 蓝色水晶（低级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/5074 |
| <!-- local:item:4806 -->4806 | 蓝色水晶（中级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/5074 |
| <!-- local:item:4807 -->4807 | 蓝色水晶（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/5074 |
| <!-- local:item:4808 -->4808 | 蓝色水晶（最高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/5074 |
| <!-- local:item:4809 -->4809 | 锁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7483 |
| <!-- local:item:4810 -->4810 | 请求申请书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/174 |
| <!-- local:item:4891 -->4891 | 破甲斩（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/86/309 |
| <!-- local:item:4892 -->4892 | 尸爆术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/86/309 |
| <!-- local:item:4893 -->4893 | 聚风（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/86/309 |
| <!-- local:item:4895 -->4895 | 不稳定波动的碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/168 |
| <!-- local:item:4896 -->4896 | 波动的精髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/168 |
| <!-- local:item:4897 -->4897 | 血将令 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/3100 |
| <!-- local:item:4898 -->4898 | 将士魂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3100 |
| <!-- local:item:4899 -->4899 | 沐水天冠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/3/3511 |
| <!-- local:item:4900 -->4900 | 玄云盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/4/3470 |
| <!-- local:item:4902 -->4902 | 舒服的羊毛帽 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/0/3120 |
| <!-- local:item:4903 -->4903 | 太平羊毛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1326 |
| <!-- local:item:4904 -->4904 | 修炼药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7110 |
| <!-- local:item:4910 -->4910 | 召唤圆木训练 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1594 |
| <!-- local:item:4911 -->4911 | （宠物变身液）霸王教主 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2757 |
| <!-- local:item:4923 -->4923 | 圆领袍衫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/20/5340 |
| <!-- local:item:4924 -->4924 | 留仙裙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/20/5350 |
| <!-- local:item:4925 -->4925 | 礼服（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/947 |
| <!-- local:item:4926 -->4926 | 礼服（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/957 |
| <!-- local:item:4927 -->4927 | 随身仓库 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7501 |
| <!-- local:item:4951 -->4951 | 花红袍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/30/5341 |
| <!-- local:item:4952 -->4952 | 龙凤衣 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/30/5351 |
| <!-- local:item:4953 -->4953 | 异界连环明珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1468 |
| <!-- local:item:4955 -->4955 | 中国传统婚礼礼服盒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7151 |
| <!-- local:item:4956 -->4956 | 武器炼制增强剂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | RefineSpecial/All/1/7497 |
| <!-- local:item:4957 -->4957 | 西装 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/5343 |
| <!-- local:item:4958 -->4958 | 婚纱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/5353 |
| <!-- local:item:4959 -->4959 | 西洋婚纱礼服盒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7151 |
| <!-- local:item:4960 -->4960 | 武器炼制增强剂（5） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | RefineSpecial/All/1/7497 |
| <!-- local:item:4961 -->4961 | （宠物变身液）熊猫酒仙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2755 |
| <!-- local:item:4962 -->4962 | 齐天大圣甲胄（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/60/5344 |
| <!-- local:item:4963 -->4963 | 齐天大圣甲胄（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/60/5344 |
| <!-- local:item:4964 -->4964 | 齐天大圣铠甲盒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7151 |
| <!-- local:item:4965 -->4965 | BOSS探测符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7261 |
| <!-- local:item:4968 -->4968 | 火焰护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/331 |
| <!-- local:item:4969 -->4969 | 寒气护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/332 |
| <!-- local:item:4970 -->4970 | 霹雷护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/333 |
| <!-- local:item:4971 -->4971 | 狂风护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/334 |
| <!-- local:item:4972 -->4972 | 神圣护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/335 |
| <!-- local:item:4973 -->4973 | 暗黑护身符（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/336 |
| <!-- local:item:4974 -->4974 | 火焰护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/331 |
| <!-- local:item:4975 -->4975 | 寒气护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/332 |
| <!-- local:item:4976 -->4976 | 霹雷护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/333 |
| <!-- local:item:4977 -->4977 | 狂风护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/334 |
| <!-- local:item:4978 -->4978 | 神圣护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/335 |
| <!-- local:item:4979 -->4979 | 暗黑护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/336 |
| <!-- local:item:4980 -->4980 | 幻影护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/337 |
| <!-- local:item:4981 -->4981 | 普通捉马套索 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/90/1059 |
| <!-- local:item:4982 -->4982 | 高级捉马套索 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/90/7498 |
| <!-- local:item:4983 -->4983 | 宠物金牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2755 |
| <!-- local:item:5007 -->5007 | 空盒子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1511 |
| <!-- local:item:5008 -->5008 | 雪人 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1325 |
| <!-- local:item:5009 -->5009 | 雪块 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | DartWeapon/All/1/1320 |
| <!-- local:item:5010 -->5010 | 圣诞老人帽子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/356 |
| <!-- local:item:5011 -->5011 | 圣诞老人手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1673 |
| <!-- local:item:5012 -->5012 | 圣诞老人鞋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1674 |
| <!-- local:item:5013 -->5013 | 破烂人偶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1455 |
| <!-- local:item:5014 -->5014 | 破旧人偶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1455 |
| <!-- local:item:5015 -->5015 | 小人偶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1455 |
| <!-- local:item:5016 -->5016 | 牛骨剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/11/1058 |
| <!-- local:item:5017 -->5017 | 强化牛骨剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/11/1058 |
| <!-- local:item:5018 -->5018 | 祈愿剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1058 |
| <!-- local:item:5019 -->5019 | 牛骨头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/11/378 |
| <!-- local:item:5020 -->5020 | 桃源盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/2/6100 |
| <!-- local:item:5021 -->5021 | 祈愿头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/1/378 |
| <!-- local:item:5022 -->5022 | 鲜血 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/32 |
| <!-- local:item:5023 -->5023 | 牛头 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1586 |
| <!-- local:item:5024 -->5024 | 小牛角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/100 |
| <!-- local:item:5025 -->5025 | 牛油 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1589 |
| <!-- local:item:5026 -->5026 | 牛骨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1149 |
| <!-- local:item:5027 -->5027 | 牛皮碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1444 |
| <!-- local:item:5028 -->5028 | 牛筋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1587 |
| <!-- local:item:5029 -->5029 | 牛排骨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1588 |
| <!-- local:item:5030 -->5030 | 牛脆骨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/103 |
| <!-- local:item:5031 -->5031 | 牛尾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1585 |
| <!-- local:item:5032 -->5032 | 牛肉包子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/91 |
| <!-- local:item:5033 -->5033 | 年糕 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1584 |
| <!-- local:item:5034 -->5034 | 葱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1582 |
| <!-- local:item:5035 -->5035 | 强化牛筋 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1587 |
| <!-- local:item:5036 -->5036 | 强化牛皮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/108 |
| <!-- local:item:5037 -->5037 | 强化牛角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1767 |
| <!-- local:item:5038 -->5038 | 蛇骨年糕饺子汤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1544 |
| <!-- local:item:5039 -->5039 | 牛尾汤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1583 |
| <!-- local:item:5040 -->5040 | 右护卫绿玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/165 |
| <!-- local:item:5041 -->5041 | 右护卫黄玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/167 |
| <!-- local:item:5042 -->5042 | 右护卫黑玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/166 |
| <!-- local:item:5045 -->5045 | 长袍（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/1/946 |
| <!-- local:item:5046 -->5046 | 旗袍（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/1/956 |
| <!-- local:item:5047 -->5047 | 第一个补给盒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1667 |
| <!-- local:item:5048 -->5048 | 第二个补给盒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1667 |
| <!-- local:item:5049 -->5049 | 第三个补给盒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1667 |
| <!-- local:item:5068 -->5068 | 明感牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1560 |
| <!-- local:item:5069 -->5069 | 甜美箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/20/1514 |
| <!-- local:item:5070 -->5070 | 甜蜜箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/20/1514 |
| <!-- local:item:5072 -->5072 | 太极 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1610 |
| <!-- local:item:5073 -->5073 | 太极指环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/1616 |
| <!-- local:item:5074 -->5074 | 爱情棒棒糖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/20/1500 |
| <!-- local:item:5075 -->5075 | 爱情糖箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/20/1504 |
| <!-- local:item:5077 -->5077 | 黄金箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1667 |
| <!-- local:item:5078 -->5078 | 黄金钥匙盒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7141 |
| <!-- local:item:5079 -->5079 | 至尊牌强化秘籍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/201 |
| <!-- local:item:5080 -->5080 | 至尊牌抽奖券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/201 |
| <!-- local:item:5081 -->5081 | 至尊牌强化抽奖券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/201 |
| <!-- local:item:5082 -->5082 | 强化至尊牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/75/79 |
| <!-- local:item:5083 -->5083 | 黄金钥匙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/7482 |
| <!-- local:item:5084 -->5084 | 白夜珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1343 |
| <!-- local:item:5085 -->5085 | 暑期活动奖券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/192 |
| <!-- local:item:5086 -->5086 | 不稳定的干将宝玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/231 |
| <!-- local:item:5087 -->5087 | 干将宝玉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7400 |
| <!-- local:item:5088 -->5088 | 干将秘典 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7260 |
| <!-- local:item:5137 -->5137 | 顿悟之牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/308 |
| <!-- local:item:5138 -->5138 | 申请复职 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1751 |
| <!-- local:item:5139 -->5139 | 大赦证（结束） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1752 |
| <!-- local:item:5140 -->5140 | 经验火炬（10） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/291 |
| <!-- local:item:5141 -->5141 | 报恩之星（中秋） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1754 |
| <!-- local:item:5142 -->5142 | 幸运油（中秋） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/63 |
| <!-- local:item:5143 -->5143 | 额外伤害花蜜药水（中秋） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1558 |
| <!-- local:item:5144 -->5144 | （九）中秋节礼物箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1506 |
| <!-- local:item:5145 -->5145 | 中秋礼品盒兑换券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1751 |
| <!-- local:item:5146 -->5146 | 带纱的红色帽子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/356 |
| <!-- local:item:5147 -->5147 | 一条红色的披肩 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1676 |
| <!-- local:item:5148 -->5148 | 一个小冰球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1320 |
| <!-- local:item:5149 -->5149 | （活动）雪人娃娃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1325 |
| <!-- local:item:5150 -->5150 | 红参精华 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/65 |
| <!-- local:item:5151 -->5151 | 酒票兑换券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1330 |
| <!-- local:item:5153 -->5153 | 药丸（150000） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/38/1346 |
| <!-- local:item:5154 -->5154 | 香喷喷的年糕汤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/94 |
| <!-- local:item:5156 -->5156 | 新年交换券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/94 |
| <!-- local:item:5161 -->5161 | 经验火炬（5） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/291 |
| <!-- local:item:5162 -->5162 | 钓鱼兑换道具套装 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2855 |
| <!-- local:item:5163 -->5163 | 父亲礼包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1730 |
| <!-- local:item:5164 -->5164 | 升级礼包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1667 |
| <!-- local:item:5165 -->5165 | 虎王手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/0/665 |
| <!-- local:item:5166 -->5166 | 桃源靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shoes/All/2/3319 |
| <!-- local:item:5167 -->5167 | 虎王戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/0/577 |
| <!-- local:item:5168 -->5168 | 虎王项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/0/892 |
| <!-- local:item:5240 -->5240 | 黄金钓鱼箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1667 |
| <!-- local:item:5241 -->5241 | 垂钓者的专业工具箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7140 |
| <!-- local:item:5242 -->5242 | 钓鱼专用线轴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Reel/All/1/7552 |
| <!-- local:item:5243 -->5243 | 钓鱼专用鱼饵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bait/All/1/7553 |
| <!-- local:item:5244 -->5244 | 钓鱼专用探测器 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Finder/All/1/7554 |
| <!-- local:item:5245 -->5245 | 钓鱼专用高级鱼漂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Float/All/1/7555 |
| <!-- local:item:5246 -->5246 | 鱼粥（泸鱼） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2856 |
| <!-- local:item:5247 -->5247 | 鱼粥（黄鱼） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2856 |
| <!-- local:item:5248 -->5248 | 姜太公的鱼竿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/20/2801 |
| <!-- local:item:5260 -->5260 | 强化试剂（赤） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3 |
| <!-- local:item:5261 -->5261 | 强化试剂（靑） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7023 |
| <!-- local:item:5262 -->5262 | 特别将券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7260 |
| <!-- local:item:5263 -->5263 | 支持信 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/190 |
| <!-- local:item:5627 -->5627 | 红色的帽子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/356 |
| <!-- local:item:5628 -->5628 | 红色的披肩 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1676 |
| <!-- local:item:5629 -->5629 | 一个小雪球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1320 |
| <!-- local:item:5630 -->5630 | 召唤券（精灵猫） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/Taoist/600/7253 |
| <!-- local:item:5631 -->5631 | 鲁道夫召唤号角 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1767 |
| <!-- local:item:5632 -->5632 | 小雪人 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1325 |
| <!-- local:item:5634 -->5634 | 流氓兔（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/5363 |
| <!-- local:item:5635 -->5635 | 流氓兔（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/5373 |
| <!-- local:item:5636 -->5636 | 法师幻魔盔甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/7660 |
| <!-- local:item:5637 -->5637 | 法师幻魔盔甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/7661 |
| <!-- local:item:5638 -->5638 | 道士幻魔盔甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/7660 |
| <!-- local:item:5639 -->5639 | 道士幻魔盔甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/7661 |
| <!-- local:item:5640 -->5640 | 龙吟战甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/0/7660 |
| <!-- local:item:5641 -->5641 | 龙吟战甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/0/7661 |
| <!-- local:item:5642 -->5642 | 传奇御史牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1743 |
| <!-- local:item:5643 -->5643 | 新年感恩箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7140 |
| <!-- local:item:5657 -->5657 | 兔子腿项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/5042 |
| <!-- local:item:5658 -->5658 | 兔子腿戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/5043 |
| <!-- local:item:5659 -->5659 | 兔子腿手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/1/5044 |
| <!-- local:item:5660 -->5660 | 幸运的兔腿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5041 |
| <!-- local:item:5661 -->5661 | 三叶草 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5045 |
| <!-- local:item:5662 -->5662 | 四叶草 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5046 |
| <!-- local:item:5684 -->5684 | 疾风太阳神水包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7100 |
| <!-- local:item:5685 -->5685 | 自然太阳神水包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7101 |
| <!-- local:item:5686 -->5686 | 灵魂太阳神水包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7102 |
| <!-- local:item:5687 -->5687 | 攻击太阳神水包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7103 |
| <!-- local:item:5701 -->5701 | 惠氏的盒子（银） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7144 |
| <!-- local:item:5702 -->5702 | 惠氏的盒子（铜） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7144 |
| <!-- local:item:5703 -->5703 | 木刻的鱼竿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/2801 |
| <!-- local:item:5704 -->5704 | 神奇的果实 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/114 |
| <!-- local:item:5705 -->5705 | 活力的果实 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/114 |
| <!-- local:item:5715 -->5715 | 花束 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/77 |
| <!-- local:item:5716 -->5716 | 家和万事兴（家） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5250 |
| <!-- local:item:5717 -->5717 | 家和万事兴（和） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5251 |
| <!-- local:item:5718 -->5718 | 家和万事兴（万） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5252 |
| <!-- local:item:5719 -->5719 | 家和万事兴（事） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5253 |
| <!-- local:item:5720 -->5720 | 家和万事兴（兴） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5254 |
| <!-- local:item:5721 -->5721 | 祝愿的鞭炮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7521 |
| <!-- local:item:5722 -->5722 | 希望的爆竹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7522 |
| <!-- local:item:5723 -->5723 | 曼鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/2992 |
| <!-- local:item:5724 -->5724 | 钓鱼竿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/7550 |
| <!-- local:item:5726 -->5726 | 姜太公的祝福 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7556 |
| <!-- local:item:5728 -->5728 | 地下城洞口传送卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/182 |
| <!-- local:item:5738 -->5738 | 幻魔盔甲盒（1日） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1667 |
| <!-- local:item:5739 -->5739 | 祝福盒（银） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7144 |
| <!-- local:item:5740 -->5740 | 祝福盒（铜） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7144 |
| <!-- local:item:5741 -->5741 | 红毒之护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5280 |
| <!-- local:item:5742 -->5742 | 红毒之火护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5281 |
| <!-- local:item:5743 -->5743 | 红毒之冰护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5282 |
| <!-- local:item:5744 -->5744 | 红毒之雷护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5283 |
| <!-- local:item:5745 -->5745 | 红毒之风护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5284 |
| <!-- local:item:5746 -->5746 | 红毒之神圣护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5285 |
| <!-- local:item:5747 -->5747 | 红毒之暗黑护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5286 |
| <!-- local:item:5748 -->5748 | 红毒之幻影护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5287 |
| <!-- local:item:5749 -->5749 | 绿毒之护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5290 |
| <!-- local:item:5750 -->5750 | 绿毒之火护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5291 |
| <!-- local:item:5751 -->5751 | 绿毒之冰护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5292 |
| <!-- local:item:5752 -->5752 | 绿毒之雷护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5293 |
| <!-- local:item:5753 -->5753 | 绿毒之风护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5294 |
| <!-- local:item:5754 -->5754 | 绿毒之神圣护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5295 |
| <!-- local:item:5755 -->5755 | 绿毒之暗黑护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5296 |
| <!-- local:item:5756 -->5756 | 绿毒之幻影护身符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5297 |
| <!-- local:item:5757 -->5757 | 万能符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5300 |
| <!-- local:item:5758 -->5758 | 火之万能符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5301 |
| <!-- local:item:5759 -->5759 | 冰之万能符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5302 |
| <!-- local:item:5760 -->5760 | 雷之万能符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5303 |
| <!-- local:item:5761 -->5761 | 风之万能符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5304 |
| <!-- local:item:5762 -->5762 | 神圣之万能符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5305 |
| <!-- local:item:5763 -->5763 | 暗黑之万能符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5306 |
| <!-- local:item:5764 -->5764 | 幻影之万能符（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/5307 |
| <!-- local:item:5773 -->5773 | 算命盒子（1日） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7195 |
| <!-- local:item:5774 -->5774 | 算命盒子（3小时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7195 |
| <!-- local:item:5775 -->5775 | 幻影包（1日） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7151 |
| <!-- local:item:5776 -->5776 | 幻影包（3日） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7151 |
| <!-- local:item:5777 -->5777 | 书本籍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1730 |
| <!-- local:item:5778 -->5778 | 打孔盒子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1667 |
| <!-- local:item:5790 -->5790 | 田蜜的箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1506 |
| <!-- local:item:5791 -->5791 | 田蜜的巧克力棒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/116 |
| <!-- local:item:5792 -->5792 | 返回包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1730 |
| <!-- local:item:5793 -->5793 | 无限的盒子（回归） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1737 |
| <!-- local:item:5794 -->5794 | 可疑的箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2855 |
| <!-- local:item:5795 -->5795 | 华氏的钥匙串 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7481 |
| <!-- local:item:5796 -->5796 | 1经验囊 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1346 |
| <!-- local:item:5797 -->5797 | 500经验囊 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1346 |
| <!-- local:item:5798 -->5798 | 惠氏的盒子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1783 |
| <!-- local:item:5799 -->5799 | 召唤鲁道夫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/203 |
| <!-- local:item:5800 -->5800 | 圣诞老人召唤师 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/200 |
| <!-- local:item:5801 -->5801 | 可爱的雪人娃娃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5051 |
| <!-- local:item:5802 -->5802 | 圣诞树种子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/104 |
| <!-- local:item:5803 -->5803 | 圣诞礼物箱（A） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5020 |
| <!-- local:item:5804 -->5804 | 圣诞礼物箱（B） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5021 |
| <!-- local:item:5805 -->5805 | 圣诞礼物箱（C） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5022 |
| <!-- local:item:5806 -->5806 | 鲁道夫的铃铛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1670 |
| <!-- local:item:5807 -->5807 | 圣诞项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/5030 |
| <!-- local:item:5808 -->5808 | 圣诞手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/1/5032 |
| <!-- local:item:5809 -->5809 | 圣诞戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/5031 |
| <!-- local:item:5811 -->5811 | 冬天的密匙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/2950 |
| <!-- local:item:5812 -->5812 | 冬天的箱子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2940 |
| <!-- local:item:5813 -->5813 | 大黑龙的祝福牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/0/1744 |
| <!-- local:item:5814 -->5814 | 黑龙的祝福牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/0/1744 |
| <!-- local:item:5815 -->5815 | 黑龙奇石（原石） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1706 |
| <!-- local:item:5816 -->5816 | 黑龙奇石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/162 |
| <!-- local:item:5817 -->5817 | 黑龙宝珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/166 |
| <!-- local:item:5818 -->5818 | 桃源虎翼刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/2/3426 |
| <!-- local:item:5819 -->5819 | 桃源曜灵杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/2/3436 |
| <!-- local:item:5820 -->5820 | 桃源三焰扇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/2/3447 |
| <!-- local:item:5822 -->5822 | 好吃的年高汤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/94 |
| <!-- local:item:5823 -->5823 | 一个被盗的盒子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1730 |
| <!-- local:item:5824 -->5824 | 被盗箱子的密匙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2950 |
| <!-- local:item:5825 -->5825 | 春天的箱子（银） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7144 |
| <!-- local:item:5826 -->5826 | 音箱（万岁的呼声） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1712 |
| <!-- local:item:5827 -->5827 | 潜龙的黑龙牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/0/1744 |
| <!-- local:item:5828 -->5828 | 雅各科的黑龙牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/0/1744 |
| <!-- local:item:5829 -->5829 | 卡伦斯2的黑龙牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/0/1744 |
| <!-- local:item:5830 -->5830 | 米尔丹的黑龙牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/0/1744 |
| <!-- local:item:5831 -->5831 | 传奇宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7161 |
| <!-- local:item:5953 -->5953 | 赦免许可证 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7261 |
| <!-- local:item:5960 -->5960 | 蓝宝石石像（中级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1730 |
| <!-- local:item:5969 -->5969 | 黑岩龙牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/0/1744 |
| <!-- local:item:5970 -->5970 | 无限的盒子（一般） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3130 |
| <!-- local:item:5971 -->5971 | 无限的盒子（英雄） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3131 |
| <!-- local:item:5972 -->5972 | 无限的盒子（传说） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3132 |
| <!-- local:item:5973 -->5973 | 无限的盒子（神话） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3133 |
| <!-- local:item:5974 -->5974 | 无限的精华（一般） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3140 |
| <!-- local:item:5975 -->5975 | 无限的精华（英雄） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3141 |
| <!-- local:item:5976 -->5976 | 无限的精华（传说） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3142 |
| <!-- local:item:5977 -->5977 | 无限的精华（神话） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3143 |
| <!-- local:item:5978 -->5978 | 无限的标志（一般） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3150 |
| <!-- local:item:5979 -->5979 | 无限的标志（英雄） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3151 |
| <!-- local:item:5980 -->5980 | 无限的标志（传说） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3152 |
| <!-- local:item:5981 -->5981 | 无限的标志（神话） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3153 |
| <!-- local:item:5982 -->5982 | 旧的书籍（低级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1730 |
| <!-- local:item:5983 -->5983 | 旧的书籍（中级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1730 |
| <!-- local:item:5984 -->5984 | 贡献证书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1751 |
| <!-- local:item:5985 -->5985 | 无限塔征服（一般） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1752 |
| <!-- local:item:5986 -->5986 | 无限塔征服（英雄） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1752 |
| <!-- local:item:5987 -->5987 | 无限塔征服（传说） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1752 |
| <!-- local:item:5988 -->5988 | 无限塔征服（神话） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1752 |
| <!-- local:item:5989 -->5989 | 神秘的红色油 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1 |
| <!-- local:item:5990 -->5990 | 神秘的蓝色油 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/11 |
| <!-- local:item:5991 -->5991 | 青铜石药水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/54 |
| <!-- local:item:5992 -->5992 | 无限的项链（一般） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/5030 |
| <!-- local:item:5993 -->5993 | 无限的手镯（一般） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/1/5032 |
| <!-- local:item:5994 -->5994 | 无限的戒指（一般） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/5031 |
| <!-- local:item:5995 -->5995 | 无限的项链（英雄） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/5030 |
| <!-- local:item:5996 -->5996 | 无限的手镯（英雄） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/1/5032 |
| <!-- local:item:5997 -->5997 | 无限的戒指（英雄） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/5031 |
| <!-- local:item:5998 -->5998 | 无限项链（一般） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/5030 |
| <!-- local:item:5999 -->5999 | 无限手镯（一般） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/1/5032 |
| <!-- local:item:6000 -->6000 | 无限指环（一般） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/5031 |
| <!-- local:item:6001 -->6001 | Lv14师门-生命HP圣物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2898 |
| <!-- local:item:6002 -->6002 | Lv13师门-护身神器 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2901 |
| <!-- local:item:6003 -->6003 | Lv11师门-破坏圣物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2899 |
| <!-- local:item:6004 -->6004 | Lv16师门-魔法MP圣物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2895 |
| <!-- local:item:6005 -->6005 | Lv12师门-抵抗圣器 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2897 |
| <!-- local:item:6006 -->6006 | Lv9师门-魔法圣器 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2896 |
| <!-- local:item:6007 -->6007 | Lv7师门-固结圣器 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2894 |
| <!-- local:item:6008 -->6008 | Lv8师门-不悔圣物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2892 |
| <!-- local:item:6009 -->6009 | Lv6师门-龙牌圣物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2893 |
| <!-- local:item:6010 -->6010 | Lv25师门-25级师门令牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/2891 |
| <!-- local:item:6011 -->6011 | Lv20师门-20级师门令牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/2891 |
| <!-- local:item:6012 -->6012 | Lv15师门-15级师门令牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/2891 |
| <!-- local:item:6013 -->6013 | Lv10师门-10级师门令牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/2891 |
| <!-- local:item:6014 -->6014 | Lv5师门-5级师门令牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/2891 |
| <!-- local:item:6015 -->6015 | Lv1师门-1级师门令牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/2890 |
| <!-- local:item:6016 -->6016 | 灵芝生命HP恢复药（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/2 |
| <!-- local:item:6017 -->6017 | 灵芝生命HP恢复药（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3 |
| <!-- local:item:6018 -->6018 | 灵芝魔法MP恢复药（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/12 |
| <!-- local:item:6019 -->6019 | 灵芝魔法MP恢复药（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/13 |
| <!-- local:item:6020 -->6020 | 灵芝水仙花（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/20 |
| <!-- local:item:6021 -->6021 | 灵芝水仙花（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/21 |
| <!-- local:item:6022 -->6022 | Lv23师门-初出茅庐的项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/10/3012 |
| <!-- local:item:6023 -->6023 | Lv22师门-初出茅庐的戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/10/3010 |
| <!-- local:item:6024 -->6024 | Lv21师门-初出茅庐的手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/10/3011 |
| <!-- local:item:6025 -->6025 | Lv29师门-万人的师傅 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3020 |
| <!-- local:item:6026 -->6026 | Lv28师门-觉醒的牌子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1451 |
| <!-- local:item:6027 -->6027 | Lv27师门-师傅的召唤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3021 |
| <!-- local:item:6028 -->6028 | Lv26师门-徒弟的召唤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3022 |
| <!-- local:item:6029 -->6029 | Lv24师门-师徒的呼喊 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3023 |
| <!-- local:item:6030 -->6030 | 禁止战场进入 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1783 |
| <!-- local:item:6031 -->6031 | 内丹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3024 |
| <!-- local:item:6032 -->6032 | 护身符捆 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/338 |
| <!-- local:item:6033 -->6033 | 祝福圣水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/69 |
| <!-- local:item:6034 -->6034 | Lv17师门-师徒的灵丹妙药 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1770 |
| <!-- local:item:6035 -->6035 | Lv19师门-魔法MP之泉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3025 |
| <!-- local:item:6036 -->6036 | Lv18师门-生命HP之泉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3026 |
| <!-- local:item:6037 -->6037 | Lv30师门-鼓舞士气 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3027 |
| <!-- local:item:6038 -->6038 | 助力书（临时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/339 |
| <!-- local:item:6039 -->6039 | 八门金锁阵（门票） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1332 |
| <!-- local:item:6040 -->6040 | 芋头汤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1583 |
| <!-- local:item:6042 -->6042 | 流浪礼物箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1506 |
| <!-- local:item:6043 -->6043 | 栗子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1410 |
| <!-- local:item:6051 -->6051 | 门派庄园（千寿园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6052 -->6052 | 门派庄园（千花园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6053 -->6053 | 门派庄园（怡和园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6054 -->6054 | 门派庄园（光华园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6055 -->6055 | 门派庄园（阳明园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6056 -->6056 | 门派庄园（震儒园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6057 -->6057 | 门派庄园（圣火园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6058 -->6058 | 门派庄园（圣日园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6059 -->6059 | 门派庄园（珍味园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6060 -->6060 | 门派庄园（纪昌园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6061 -->6061 | 门派庄园（沧浪园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6062 -->6062 | 门派庄园（圆明园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6063 -->6063 | 门派庄园（年兆园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6064 -->6064 | 门派庄园（鉴修园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6065 -->6065 | 门派庄园（清天园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6066 -->6066 | 门派庄园（万柳园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6067 -->6067 | 门派庄园（儒家园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6068 -->6068 | 门派庄园（散士园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6069 -->6069 | 门派庄园（神机园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6070 -->6070 | 门派庄园（花香园）邀请劵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1561 |
| <!-- local:item:6071 -->6071 | 庄园蘑菇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1417 |
| <!-- local:item:6072 -->6072 | 雪人娃娃（雪白） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5051 |
| <!-- local:item:6073 -->6073 | 雪人娃娃（群吸） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5051 |
| <!-- local:item:6074 -->6074 | 雪人娃娃（恢复） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5051 |
| <!-- local:item:6075 -->6075 | 无限项链（英雄） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/5030 |
| <!-- local:item:6076 -->6076 | 无限手镯（英雄） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/1/5032 |
| <!-- local:item:6077 -->6077 | 无限戒指（英雄） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/5031 |
| <!-- local:item:6078 -->6078 | 无限的精华（Lv1） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3140 |
| <!-- local:item:6079 -->6079 | 无限的精华（Lv2） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3140 |
| <!-- local:item:6080 -->6080 | 无限的精华（Lv3） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3140 |
| <!-- local:item:6081 -->6081 | 无限的精华（Lv4） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3140 |
| <!-- local:item:6082 -->6082 | 无限的精华（Lv5） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3140 |
| <!-- local:item:6083 -->6083 | 无限的精华（Lv6） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3141 |
| <!-- local:item:6084 -->6084 | 无限的精华（Lv7） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3141 |
| <!-- local:item:6085 -->6085 | 无限的精华（Lv8） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3141 |
| <!-- local:item:6086 -->6086 | 无限的精华（Lv9） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3141 |
| <!-- local:item:6087 -->6087 | 无限的精华（Lv10） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3141 |
| <!-- local:item:6088 -->6088 | 文昌帝君医书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/339 |
| <!-- local:item:6094 -->6094 | 圣诞老人的礼物箱（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7161 |
| <!-- local:item:6095 -->6095 | 圣诞服（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/5342 |
| <!-- local:item:6096 -->6096 | 圣诞服（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/5352 |
| <!-- local:item:6098 -->6098 | 圣诞袜子（一般） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1677 |
| <!-- local:item:6099 -->6099 | 红色装饰球（初级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1830 |
| <!-- local:item:6100 -->6100 | 红色装饰球（低级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1830 |
| <!-- local:item:6101 -->6101 | 红色装饰球（中级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7340 |
| <!-- local:item:6102 -->6102 | 红色装饰球（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7340 |
| <!-- local:item:6103 -->6103 | 红色装饰球（最高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7340 |
| <!-- local:item:6104 -->6104 | 绿色装饰球（初级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1831 |
| <!-- local:item:6105 -->6105 | 绿色装饰球（低级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1831 |
| <!-- local:item:6106 -->6106 | 绿色装饰球（中级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1831 |
| <!-- local:item:6107 -->6107 | 绿色装饰球（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1831 |
| <!-- local:item:6108 -->6108 | 绿色装饰球（最高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1831 |
| <!-- local:item:6109 -->6109 | 黄色装饰球（初级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1832 |
| <!-- local:item:6110 -->6110 | 黄色装饰球（低级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1832 |
| <!-- local:item:6111 -->6111 | 黄色装饰球（中级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1832 |
| <!-- local:item:6112 -->6112 | 黄色装饰球（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1832 |
| <!-- local:item:6113 -->6113 | 黄色装饰球（最高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1832 |
| <!-- local:item:6114 -->6114 | 召唤鲁道夫（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/203 |
| <!-- local:item:6115 -->6115 | 圣诞老人的衣服 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7151 |
| <!-- local:item:6116 -->6116 | 幸运硬币（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7504 |
| <!-- local:item:6117 -->6117 | 新手攻击强效药水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/84 |
| <!-- local:item:6118 -->6118 | 新手疾风强效药水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/80 |
| <!-- local:item:6119 -->6119 | 新手体力强效药水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/85 |
| <!-- local:item:6120 -->6120 | 新手攻击强效药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/7/84 |
| <!-- local:item:6121 -->6121 | 新手自然强效药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/7/82 |
| <!-- local:item:6122 -->6122 | 新手灵魂强效药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/7/81 |
| <!-- local:item:6123 -->6123 | 新手疾风强效药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/7/80 |
| <!-- local:item:6124 -->6124 | 新手体力强效药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/7/85 |
| <!-- local:item:6125 -->6125 | 新手魔法强效药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/7/83 |
| <!-- local:item:6126 -->6126 | 新手攻击强效药水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/16/84 |
| <!-- local:item:6127 -->6127 | 新手自然强效药水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/16/82 |
| <!-- local:item:6128 -->6128 | 新手灵魂强效药水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/16/81 |
| <!-- local:item:6129 -->6129 | 新手疾风强效药水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/16/80 |
| <!-- local:item:6130 -->6130 | 新手体力强效药水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/16/85 |
| <!-- local:item:6131 -->6131 | 新手魔法强效药水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/16/83 |
| <!-- local:item:6132 -->6132 | 新手攻击强效药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/25/84 |
| <!-- local:item:6133 -->6133 | 新手自然强效药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/25/82 |
| <!-- local:item:6134 -->6134 | 新手灵魂强效药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/25/81 |
| <!-- local:item:6135 -->6135 | 新手疾风强效药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/25/80 |
| <!-- local:item:6136 -->6136 | 新手体力强效药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/25/85 |
| <!-- local:item:6137 -->6137 | 新手魔法强效药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/25/83 |
| <!-- local:item:6138 -->6138 | 新手经验葫芦（10%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/7/1686 |
| <!-- local:item:6139 -->6139 | 新手疾风太阳神水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/7/1776 |
| <!-- local:item:6140 -->6140 | 新手自然太阳神水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/7/1778 |
| <!-- local:item:6141 -->6141 | 新手灵魂太阳神水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/7/1777 |
| <!-- local:item:6142 -->6142 | 新手攻击太阳神水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/7/1780 |
| <!-- local:item:6143 -->6143 | 新手经验葫芦（20%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/16/1686 |
| <!-- local:item:6144 -->6144 | 新手疾风太阳神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/16/1776 |
| <!-- local:item:6145 -->6145 | 新手自然太阳神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/16/1778 |
| <!-- local:item:6146 -->6146 | 新手灵魂太阳神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/16/1777 |
| <!-- local:item:6147 -->6147 | 新手攻击太阳神水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/16/1780 |
| <!-- local:item:6148 -->6148 | 新手经验葫芦（30%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/25/1686 |
| <!-- local:item:6149 -->6149 | 新手疾风太阳神水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/25/1776 |
| <!-- local:item:6150 -->6150 | 新手自然太阳神水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/25/1778 |
| <!-- local:item:6151 -->6151 | 新手灵魂太阳神水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/25/1777 |
| <!-- local:item:6152 -->6152 | 新手攻击太阳神水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/25/1780 |
| <!-- local:item:6153 -->6153 | 新手经验葫芦（40%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/30/1686 |
| <!-- local:item:6154 -->6154 | 新手疾风太阳神水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/30/1776 |
| <!-- local:item:6155 -->6155 | 新手自然太阳神水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/30/1778 |
| <!-- local:item:6156 -->6156 | 新手灵魂太阳神水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/30/1777 |
| <!-- local:item:6157 -->6157 | 新手攻击太阳神水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/30/1780 |
| <!-- local:item:6273 -->6273 | 马如游龙（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/All/95/309 |
| <!-- local:item:6274 -->6274 | 跃马重系（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/All/99/309 |
| <!-- local:item:6379 -->6379 | 一本古老炼金术书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1458 |
| <!-- local:item:6380 -->6380 | 韩纸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/206 |
| <!-- local:item:6381 -->6381 | 铸造模具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1460 |
| <!-- local:item:6382 -->6382 | 火山灰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1556 |
| <!-- local:item:6383 -->6383 | 火焰光环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1343 |
| <!-- local:item:6384 -->6384 | 锻造锤子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1153 |
| <!-- local:item:6385 -->6385 | 燃烧的圣火 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2879 |
| <!-- local:item:6390 -->6390 | （新）夏季包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7193 |
| <!-- local:item:6395 -->6395 | 召唤券（地狱炎魔） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/Taoist/350/7250 |
| <!-- local:item:6396 -->6396 | 珠宝（普通） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/7360 |
| <!-- local:item:6397 -->6397 | 珠宝（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/7362 |
| <!-- local:item:6398 -->6398 | 珠宝（稀释） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/7361 |
| <!-- local:item:6399 -->6399 | 武器碎片（一般） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/1626 |
| <!-- local:item:6400 -->6400 | 武器碎片（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/1626 |
| <!-- local:item:6401 -->6401 | 武器碎片（稀释） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/1626 |
| <!-- local:item:6402 -->6402 | 红色魔法精水（初级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4090 |
| <!-- local:item:6403 -->6403 | 红色魔法精水（低级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4090 |
| <!-- local:item:6404 -->6404 | 红色魔法精水（中级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4090 |
| <!-- local:item:6405 -->6405 | 红色魔法精水（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4090 |
| <!-- local:item:6406 -->6406 | 红色魔法精水（最高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4090 |
| <!-- local:item:6407 -->6407 | 红色魔法精水（稀释） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4090 |
| <!-- local:item:6408 -->6408 | 蓝色魔法精水（初级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4091 |
| <!-- local:item:6409 -->6409 | 蓝色魔法精水（低级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4091 |
| <!-- local:item:6410 -->6410 | 蓝色魔法精水（中级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4091 |
| <!-- local:item:6411 -->6411 | 蓝色魔法精水（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4091 |
| <!-- local:item:6412 -->6412 | 蓝色魔法精水（最高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4091 |
| <!-- local:item:6413 -->6413 | 蓝色魔法精水（稀释） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4091 |
| <!-- local:item:6414 -->6414 | 黄色魔法精水（初级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4092 |
| <!-- local:item:6415 -->6415 | 黄色魔法精水（低级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4092 |
| <!-- local:item:6416 -->6416 | 黄色魔法精水（中级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4092 |
| <!-- local:item:6417 -->6417 | 黄色魔法精水（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4092 |
| <!-- local:item:6418 -->6418 | 黄色魔法精水（最高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4092 |
| <!-- local:item:6419 -->6419 | 黄色魔法精水（稀释） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4092 |
| <!-- local:item:6420 -->6420 | 海水珍珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4013 |
| <!-- local:item:6421 -->6421 | （新）冬季包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7194 |
| <!-- local:item:6424 -->6424 | 龙雀开山钺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/3/3421 |
| <!-- local:item:6425 -->6425 | 熔金落日刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/4/3428 |
| <!-- local:item:6426 -->6426 | 奕天破邪杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/3/3431 |
| <!-- local:item:6427 -->6427 | 龙破沧溟 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/4/1092 |
| <!-- local:item:6428 -->6428 | 秋水无痕剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/3/6220 |
| <!-- local:item:6429 -->6429 | 天雷真火扇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/4/3448 |
| <!-- local:item:6430 -->6430 | 碎情雾影环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/3/3455 |
| <!-- local:item:6431 -->6431 | 天星耀阳环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/4/3457 |
| <!-- local:item:6432 -->6432 | 未知的战士武器（稀释） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1074 |
| <!-- local:item:6433 -->6433 | 未知的法师武器（稀释） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1074 |
| <!-- local:item:6434 -->6434 | 未知的道士武器（稀释） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1074 |
| <!-- local:item:6435 -->6435 | 未知的刺客武器（稀释） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1074 |
| <!-- local:item:6436 -->6436 | 生锈的铜戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3010 |
| <!-- local:item:6437 -->6437 | 新手经验葫芦（300%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7060 |
| <!-- local:item:6466 -->6466 | 请铁锭 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/229 |
| <!-- local:item:6467 -->6467 | 龙鳞神魔的心脏 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1142 |
| <!-- local:item:6468 -->6468 | 斗宿（斗宿）珠子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1833 |
| <!-- local:item:6469 -->6469 | 贪欲（贪狼）心脏 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1858 |
| <!-- local:item:6470 -->6470 | 天玑（天玑）珠子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1834 |
| <!-- local:item:6471 -->6471 | 天玑（天玑）脑髓 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1764 |
| <!-- local:item:6472 -->6472 | 红色的布料 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1765 |
| <!-- local:item:6473 -->6473 | 绿色的布料 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1766 |
| <!-- local:item:6474 -->6474 | 兔肉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Meat/All/1/301 |
| <!-- local:item:6475 -->6475 | 鸭肉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Meat/All/1/301 |
| <!-- local:item:6481 -->6481 | （新）幸运包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7191 |
| <!-- local:item:6502 -->6502 | （新）将状包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7192 |
| <!-- local:item:6504 -->6504 | （新）黑龙包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1786 |
| <!-- local:item:6506 -->6506 | 梦幻纪念牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/1743 |
| <!-- local:item:6517 -->6517 | 御剑术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/95/309 |
| <!-- local:item:6518 -->6518 | 御剑术-强化（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/98/309 |
| <!-- local:item:6519 -->6519 | 御剑术-奥义（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/101/309 |
| <!-- local:item:6520 -->6520 | 龙旋风（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/95/309 |
| <!-- local:item:6521 -->6521 | 龙旋风-强化（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/98/309 |
| <!-- local:item:6522 -->6522 | 龙旋风-奥义（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/101/309 |
| <!-- local:item:6523 -->6523 | 僵尸召唤术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/50/309 |
| <!-- local:item:6524 -->6524 | 僵尸召唤术-强化（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/98/309 |
| <!-- local:item:6525 -->6525 | 僵尸召唤术-奥义（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/101/309 |
| <!-- local:item:6535 -->6535 | 转职（战士） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7266 |
| <!-- local:item:6536 -->6536 | 转职（法师） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7266 |
| <!-- local:item:6537 -->6537 | 转职（道士） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7266 |
| <!-- local:item:6538 -->6538 | 转职（刺客） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7266 |
| <!-- local:item:6557 -->6557 | 雪原老虎（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/5346 |
| <!-- local:item:6558 -->6558 | 雪原老虎（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/5346 |
| <!-- local:item:6559 -->6559 | 雪原小熊（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/5347 |
| <!-- local:item:6560 -->6560 | 雪原小熊（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/5347 |
| <!-- local:item:6574 -->6574 | 黄金骨头 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1847 |
| <!-- local:item:6575 -->6575 | 上级武器制作书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1860 |
| <!-- local:item:6576 -->6576 | 福实的毛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1422 |
| <!-- local:item:6577 -->6577 | 堕落的碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/4032 |
| <!-- local:item:6578 -->6578 | 雪原老虎的服装盒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7151 |
| <!-- local:item:6579 -->6579 | 雪原高美的服装盒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7151 |
| <!-- local:item:6580 -->6580 | 碎片仓库包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7505 |
| <!-- local:item:6581 -->6581 | 单身铜币 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2682 |
| <!-- local:item:6582 -->6582 | 战宠经验药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/40 |
| <!-- local:item:6583 -->6583 | 战宠经验药水（60） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/40 |
| <!-- local:item:6584 -->6584 | 足球狂姜太公 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7556 |
| <!-- local:item:6585 -->6585 | 应援道具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2862 |
| <!-- local:item:6586 -->6586 | 梦幻牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/2914 |
| <!-- local:item:6587 -->6587 | 梦幻精灵时装 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/1737 |
| <!-- local:item:6588 -->6588 | 梦幻精石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/164 |
| <!-- local:item:6589 -->6589 | 梦幻精水碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/5016 |
| <!-- local:item:6590 -->6590 | 神秘的梦幻箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2942 |
| <!-- local:item:6609 -->6609 | 黄金鳗鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/2998 |
| <!-- local:item:6610 -->6610 | 宠物经验药水（1520） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/40 |
| <!-- local:item:6611 -->6611 | 黄金鳗鱼（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/2998 |
| <!-- local:item:6612 -->6612 | 黄金鳗鱼（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fish/All/1/2998 |
| <!-- local:item:6630 -->6630 | 细工锤子（力） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3160 |
| <!-- local:item:6631 -->6631 | 细工锤子（风） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3161 |
| <!-- local:item:6632 -->6632 | 细工锤子（火） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3162 |
| <!-- local:item:6633 -->6633 | 细工锤子（魂） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3163 |
| <!-- local:item:6634 -->6634 | 血花落照的晶水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3170 |
| <!-- local:item:6635 -->6635 | 九宫云雾的晶水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3171 |
| <!-- local:item:6636 -->6636 | 黑天暗云的晶水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3172 |
| <!-- local:item:6637 -->6637 | 万里碧海的晶水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3173 |
| <!-- local:item:6638 -->6638 | 失去力量的混天刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1075 |
| <!-- local:item:6639 -->6639 | 诺玛勇士的古墓地图 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/200 |
| <!-- local:item:6665 -->6665 | 物品葫芦（150） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7063 |
| <!-- local:item:6666 -->6666 | 经验物品葫芦（60） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7062 |
| <!-- local:item:6667 -->6667 | 任务立即完成卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/7300 |
| <!-- local:item:6668 -->6668 | 梦幻精水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1558 |
| <!-- local:item:6669 -->6669 | 特殊制炼石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | RefineSpecial/All/1/228 |
| <!-- local:item:6672 -->6672 | 强力花油（盔甲） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/53 |
| <!-- local:item:6688 -->6688 | 幸运硬币箱（任务） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1667 |
| <!-- local:item:6689 -->6689 | 传奇标志箱（任务） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1737 |
| <!-- local:item:6690 -->6690 | 神秘石油箱（任务） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1757 |
| <!-- local:item:6691 -->6691 | 青铜石药水箱（任务） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1736 |
| <!-- local:item:6692 -->6692 | 幸运硬币（任务） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/2681 |
| <!-- local:item:6693 -->6693 | 传奇印记（任务） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/2685 |
| <!-- local:item:6694 -->6694 | 传奇硬币（任务） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2684 |
| <!-- local:item:6695 -->6695 | 诺玛补给箱（任务） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1680 |
| <!-- local:item:6696 -->6696 | 2020新春增益包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7202 |
| <!-- local:item:6697 -->6697 | 新春迷宫盒（活动） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/7161 |
| <!-- local:item:6698 -->6698 | 连接保持兑换卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/192 |
| <!-- local:item:7001 -->7001 | 古老的武功秘籍 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1332 |
| <!-- local:item:7002 -->7002 | 召唤战斗宠物 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3070 |
| <!-- local:item:7003 -->7003 | 假眼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1625 |
| <!-- local:item:7009 -->7009 | 宠物恢复药水（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3066 |
| <!-- local:item:7010 -->7010 | 战斗宠物盔甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3071 |
| <!-- local:item:7011 -->7011 | 战斗宠物经验 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3061 |
| <!-- local:item:7012 -->7012 | 战斗宠物提升（战斗力） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3060 |
| <!-- local:item:7013 -->7013 | 战斗宠物提升（护甲） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3069 |
| <!-- local:item:7014 -->7014 | 战斗宠物觉醒药水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3064 |
| <!-- local:item:7015 -->7015 | 战斗宠物解毒丸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3068 |
| <!-- local:item:7016 -->7016 | 宠物恢复药水（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3067 |
| <!-- local:item:7017 -->7017 | 宠物恢复药水（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3065 |
| <!-- local:item:7018 -->7018 | 战斗宠物特修神水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/52 |
| <!-- local:item:7019 -->7019 | 战斗宠物防御200 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3071 |
| <!-- local:item:7020 -->7020 | 战斗宠物攻击提升200 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3060 |
| <!-- local:item:7021 -->7021 | 战斗宠物护甲提升200 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3069 |
| <!-- local:item:7022 -->7022 | 战斗宠物魔法提升200 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3069 |
| <!-- local:item:7023 -->7023 | 战斗宠物战力提升200 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3069 |
| <!-- local:item:7024 -->7024 | 战斗宠物防御100 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3071 |
| <!-- local:item:7025 -->7025 | 战斗宠物攻击提升100 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3060 |
| <!-- local:item:7026 -->7026 | 战斗宠物护甲提升100 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3069 |
| <!-- local:item:7027 -->7027 | 战斗宠物魔法提升100 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3069 |
| <!-- local:item:7028 -->7028 | 战斗宠物战力提升100 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/3069 |
| <!-- local:item:7029 -->7029 | 4级技能橙色丹丸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3037 |
| <!-- local:item:7030 -->7030 | 4级技能蓝色丹丸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3036 |
| <!-- local:item:7031 -->7031 | 4级技能绿色丹丸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3035 |
| <!-- local:item:7032 -->7032 | 4级技能红色丹丸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3034 |
| <!-- local:item:7033 -->7033 | 4级技能橙色任务书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3033 |
| <!-- local:item:7034 -->7034 | 4级技能蓝色任务书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3032 |
| <!-- local:item:7035 -->7035 | 高级技能任务书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3031 |
| <!-- local:item:7036 -->7036 | 4级技能红色任务书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3030 |
| <!-- local:item:7037 -->7037 | 宠物恢复药水（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7021 |
| <!-- local:item:7038 -->7038 | 宠物恢复药水（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3065 |
| <!-- local:item:7039 -->7039 | 召唤强化咒书（时限） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/194 |
| <!-- local:item:8016 -->8016 | 稀世技能任务书 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3032 |
| <!-- local:item:8017 -->8017 | 惩罚的标志 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/859 |
| <!-- local:item:8018 -->8018 | 首领的标志 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/859 |
| <!-- local:item:8019 -->8019 | 铜色英雄的师祖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/859 |
| <!-- local:item:8020 -->8020 | 讨伐的进军者 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/859 |
| <!-- local:item:8021 -->8021 | 最后抵抗 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/52/309 |
| <!-- local:item:8576 -->8576 | 腐烂的包子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1553 |
| <!-- local:item:8577 -->8577 | 红色的包子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1151 |
| <!-- local:item:8578 -->8578 | 月莲草 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1741 |
| <!-- local:item:8579 -->8579 | 黑月莲草 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1741 |
| <!-- local:item:8580 -->8580 | 刺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2634 |
| <!-- local:item:8581 -->8581 | 爪子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1453 |
| <!-- local:item:8582 -->8582 | 有毒的刺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2634 |
| <!-- local:item:8583 -->8583 | 有毒的爪子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1453 |
| <!-- local:item:8584 -->8584 | 红色的刺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2633 |
| <!-- local:item:8585 -->8585 | 犬牙刺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1453 |
| <!-- local:item:8586 -->8586 | 红色的毒刺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2633 |
| <!-- local:item:8587 -->8587 | 有毒的犬牙刺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1453 |
| <!-- local:item:8588 -->8588 | 红色的岩石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/218 |
| <!-- local:item:8589 -->8589 | 壹颗不冷的心 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1142 |
| <!-- local:item:8590 -->8590 | 高连木的根 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/71 |
| <!-- local:item:8591 -->8591 | 高连木的刺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1338 |
| <!-- local:item:8592 -->8592 | 折磨灵魂的宝石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/230 |
| <!-- local:item:8593 -->8593 | 灵魂宝石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/231 |
| <!-- local:item:8594 -->8594 | 堕落的月下一族的遗骨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1554 |
| <!-- local:item:8595 -->8595 | 亡灵的刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1626 |
| <!-- local:item:8596 -->8596 | 亡灵的长矛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1152 |
| <!-- local:item:8597 -->8597 | 亡灵的箭 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/310 |
| <!-- local:item:8598 -->8598 | 腐烂的蛆虫体液 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/65 |
| <!-- local:item:8599 -->8599 | 小蝙蝠翅膀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2645 |
| <!-- local:item:8600 -->8600 | 大蝙蝠翅膀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2645 |
| <!-- local:item:8601 -->8601 | 硫磺蝎子尾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/112 |
| <!-- local:item:8602 -->8602 | 坚硬的树皮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/107 |
| <!-- local:item:8603 -->8603 | 犯人的枷锁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2640 |
| <!-- local:item:8604 -->8604 | 堕落的心 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/2635 |
| <!-- local:item:8605 -->8605 | 铜色的深渊结晶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/857 |
| <!-- local:item:8606 -->8606 | 怪物战利品基地31 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8607 -->8607 | 怪物战利品基地32 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8608 -->8608 | 怪物战利品基地33 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8609 -->8609 | 怪物战利品基地34 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8610 -->8610 | 怪物战利品基地35 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8611 -->8611 | 怪物战利品基地36 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8612 -->8612 | 怪物战利品基地37 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8613 -->8613 | 怪物战利品基地38 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8614 -->8614 | 怪物战利品基地39 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8615 -->8615 | 怪物战利品基地40 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8616 -->8616 | 顶级制造材料1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8617 -->8617 | 顶级制造材料2 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8618 -->8618 | 顶级制造材料3 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8619 -->8619 | 顶级制造材料4 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8620 -->8620 | 顶级制造材料5 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8621 -->8621 | 顶级制造材料6 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8622 -->8622 | 顶级制造材料7 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8623 -->8623 | 顶级制造材料8 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8624 -->8624 | 顶级制造材料9 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8625 -->8625 | 顶级制造材料10 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8626 -->8626 | 顶级制造材料11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8627 -->8627 | 顶级制造材料12 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8628 -->8628 | 顶级制造材料13 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8629 -->8629 | 顶级制造材料14 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8630 -->8630 | 顶级制造材料15 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/0 |
| <!-- local:item:8631 -->8631 | 防氧化油 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1465 |
| <!-- local:item:8632 -->8632 | 黑龙石溶剂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/54 |
| <!-- local:item:8633 -->8633 | 白龙石溶剂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/54 |
| <!-- local:item:8634 -->8634 | 甘龙石溶剂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/54 |
| <!-- local:item:8635 -->8635 | 黑龙石（初级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1821 |
| <!-- local:item:8636 -->8636 | 黑龙石（低级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1821 |
| <!-- local:item:8637 -->8637 | 黑龙石（中级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1821 |
| <!-- local:item:8638 -->8638 | 黑龙石（上级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1821 |
| <!-- local:item:8639 -->8639 | 黑龙石（最上级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1821 |
| <!-- local:item:8640 -->8640 | 黑龙石（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1821 |
| <!-- local:item:8641 -->8641 | 黑龙石（最高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1821 |
| <!-- local:item:8642 -->8642 | 白龙石（初级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1822 |
| <!-- local:item:8643 -->8643 | 白龙石（低级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1822 |
| <!-- local:item:8644 -->8644 | 白龙石（中级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1822 |
| <!-- local:item:8645 -->8645 | 白龙石（上级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1822 |
| <!-- local:item:8646 -->8646 | 白龙石（最上级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1822 |
| <!-- local:item:8647 -->8647 | 白龙石（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1822 |
| <!-- local:item:8648 -->8648 | 白龙石（最高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1822 |
| <!-- local:item:8649 -->8649 | 甘龙石（初级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1820 |
| <!-- local:item:8650 -->8650 | 甘龙石（低级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1820 |
| <!-- local:item:8651 -->8651 | 甘龙石（中级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1820 |
| <!-- local:item:8652 -->8652 | 甘龙石（上级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1820 |
| <!-- local:item:8653 -->8653 | 甘龙石（最上级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1820 |
| <!-- local:item:8654 -->8654 | 甘龙石（高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1820 |
| <!-- local:item:8655 -->8655 | 甘龙石（最高级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1820 |
| <!-- local:item:8768 -->8768 | 巴拉蒙德的钥匙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1668 |
| <!-- local:item:9001 -->9001 | 活动制炼石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/224 |
| <!-- local:item:9002 -->9002 | 团队经验葫芦（30%.10%） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7061 |
| <!-- local:item:9004 -->9004 | 生死刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/70/1050 |
| <!-- local:item:10000 -->10000 | 树根刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1042 |
| <!-- local:item:11002 -->11002 | 敏捷面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/9/2100 |
| <!-- local:item:11003 -->11003 | 力量面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/All/15/2100 |
| <!-- local:item:12002 -->12002 | 破荒无甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/65/986 |
| <!-- local:item:12003 -->12003 | 千雨火衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/65/986 |
| <!-- local:item:12004 -->12004 | 善极务衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/65/986 |
| <!-- local:item:12005 -->12005 | 暗影纹甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/65/2005 |
| <!-- local:item:12006 -->12006 | 破荒无甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/65/996 |
| <!-- local:item:12007 -->12007 | 千雨火衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/65/996 |
| <!-- local:item:12008 -->12008 | 善极务衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/65/996 |
| <!-- local:item:12009 -->12009 | 暗影纹甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/65/2015 |
| <!-- local:item:14002 -->14002 | 智慧之心 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/30/890 |
| <!-- local:item:14003 -->14003 | 预知项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/63/918 |
| <!-- local:item:14004 -->14004 | 勇气项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/66/932 |
| <!-- local:item:14005 -->14005 | 武林宗师护符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/56/1435 |
| <!-- local:item:14006 -->14006 | 彗星项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/1/797 |
| <!-- local:item:14007 -->14007 | 白雪项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/63/920 |
| <!-- local:item:15002 -->15002 | 武林宗师护腕 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/35/761 |
| <!-- local:item:15003 -->15003 | 善心手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/66/743 |
| <!-- local:item:15004 -->15004 | 沃玛寺庙手链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/20/627 |
| <!-- local:item:15005 -->15005 | 硬化的皮手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/40/642 |
| <!-- local:item:15006 -->15006 | 彗星手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/0/767 |
| <!-- local:item:15007 -->15007 | 白雪手链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/57/688 |
| <!-- local:item:15008 -->15008 | 八卦护身符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/1/1437 |
| <!-- local:item:16002 -->16002 | 暗黑戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/52/570 |
| <!-- local:item:16003 -->16003 | 光明戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/52/574 |
| <!-- local:item:16004 -->16004 | 生连丸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/65/573 |
| <!-- local:item:16005 -->16005 | 血统戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/66/542 |
| <!-- local:item:16006 -->16006 | 矿工戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/15/447 |
| <!-- local:item:16007 -->16007 | 憎恨的精神戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/20/450 |
| <!-- local:item:16008 -->16008 | 武林宗师指环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/25/551 |
| <!-- local:item:16009 -->16009 | 赤月戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/35/1342 |
| <!-- local:item:16010 -->16010 | 精炼防御戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/3585 |
| <!-- local:item:16011 -->16011 | 大师级备用戒指2 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/3587 |
| <!-- local:item:16012 -->16012 | 精炼麻痹戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/3584 |
| <!-- local:item:16013 -->16013 | 精炼复活戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/3583 |
| <!-- local:item:16014 -->16014 | 精炼护身戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/1/3586 |
| <!-- local:item:17002 -->17002 | 锋利的学徒手刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/3/2300 |
| <!-- local:item:17003 -->17003 | 大师的准确手刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/5/2300 |
| <!-- local:item:17004 -->17004 | 破损的大师手刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/7/2300 |
| <!-- local:item:17005 -->17005 | 破损的手刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/10/2300 |
| <!-- local:item:17006 -->17006 | 恐怖的祝福之爪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/14/2302 |
| <!-- local:item:17009 -->17009 | 炫的白莲长刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/33/2205 |
| <!-- local:item:17010 -->17010 | 炫的黑色龟甲之爪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/33/2305 |
| <!-- local:item:17011 -->17011 | 飞龙剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/1050 |
| <!-- local:item:17012 -->17012 | 毁灭之爪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/1/2309 |
| <!-- local:item:18002 -->18002 | 武林宗师徽章（外部） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/40/78 |
| <!-- local:item:18003 -->18003 | 武林宗师徽章（内部） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/0/78 |
| <!-- local:item:18004 -->18004 | 太阳射手（外部） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/66/322 |
| <!-- local:item:18005 -->18005 | 太阳射手（内部） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/0/322 |
| <!-- local:item:18006 -->18006 | 武林宗师的胸章 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/320 |
| <!-- local:item:18007 -->18007 | 武林宗师的马牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/321 |
| <!-- local:item:18008 -->18008 | 彗星守护牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/323 |
| <!-- local:item:18009 -->18009 | 维拉的琵琶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/50/1521 |
| <!-- local:item:18010 -->18010 | 帝国徽章 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/50/324 |
| <!-- local:item:18011 -->18011 | 情义徽章 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/60/325 |
| <!-- local:item:18012 -->18012 | 卓越徽章 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/70/326 |
| <!-- local:item:18013 -->18013 | 至尊徽章 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/80/327 |
| <!-- local:item:18014 -->18014 | 英雄牌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/90/2914 |
| <!-- local:item:18015 -->18015 | 极尊牌（英） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/99/2915 |
| <!-- local:item:20002 -->20002 | 灰星碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/10/271 |
| <!-- local:item:20003 -->20003 | 绿星碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/20/272 |
| <!-- local:item:20004 -->20004 | 红星碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/30/273 |
| <!-- local:item:20005 -->20005 | 蓝星碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/40/274 |
| <!-- local:item:50002 -->50002 | HP恢复石（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Medicament/All/0/7370 |
| <!-- local:item:50003 -->50003 | HP恢复石（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Medicament/All/0/7371 |
| <!-- local:item:50004 -->50004 | HP恢复石（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Medicament/All/0/7372 |
| <!-- local:item:50005 -->50005 | HP恢复石（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Medicament/All/0/7373 |
| <!-- local:item:50006 -->50006 | MP恢复石（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Medicament/All/0/7380 |
| <!-- local:item:50007 -->50007 | MP恢复石（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Medicament/All/0/7381 |
| <!-- local:item:50008 -->50008 | MP恢复石（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Medicament/All/0/7382 |
| <!-- local:item:50009 -->50009 | MP恢复石（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Medicament/All/0/7383 |
| <!-- local:item:50010 -->50010 | 新能源（小） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Medicament/All/0/7390 |
| <!-- local:item:50011 -->50011 | 新能源（中） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Medicament/All/0/7391 |
| <!-- local:item:50012 -->50012 | 新能源（大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Medicament/All/0/7392 |
| <!-- local:item:50013 -->50013 | 新能源（特） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Medicament/All/0/7393 |
| <!-- local:item:80001 -->80001 | 意识药水（3级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/3/3060 |
| <!-- local:item:80002 -->80002 | 意识药水（5级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/5/3061 |
| <!-- local:item:80003 -->80003 | 意识药水（7级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/7/3062 |
| <!-- local:item:80004 -->80004 | 意识药水（10级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/10/3069 |
| <!-- local:item:80005 -->80005 | 意识药水（11级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/11/3069 |
| <!-- local:item:80006 -->80006 | 意识药水（13级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/13/3069 |
| <!-- local:item:80007 -->80007 | 意识药水（15级） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/15/3069 |
| <!-- local:item:80008 -->80008 | 宠物自动粮仓券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/5013 |
| <!-- local:item:80009 -->80009 | 经验 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/5071 |
| <!-- local:item:80010 -->80010 | 游戏币 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/2683 |
| <!-- local:item:80011 -->80011 | 声望 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/0 |
| <!-- local:item:80012 -->80012 | 贡献 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/0 |
| <!-- local:item:80013 -->80013 | 宠物解锁券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/5013 |
| <!-- local:item:80014 -->80014 | 财富检查程序 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | System/All/0/1594 |
| <!-- local:item:80015 -->80015 | \[碎片\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | ItemPart/All/0/0 |
| <!-- local:item:80016 -->80016 | 武器模板 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/1110 |
| <!-- local:item:80017 -->80017 | 威武的狂战之刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1111 |
| <!-- local:item:80018 -->80018 | 不朽的法老之刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1112 |
| <!-- local:item:80019 -->80019 | 恐怖的亡灵之刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/1113 |
| <!-- local:item:80021 -->80021 | 黄色立方体 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3130 |
| <!-- local:item:80022 -->80022 | 蓝色立方体 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3131 |
| <!-- local:item:80023 -->80023 | 红色立方体 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3132 |
| <!-- local:item:80024 -->80024 | 紫色立方体 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3133 |
| <!-- local:item:80025 -->80025 | 绿色立方体 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3134 |
| <!-- local:item:80026 -->80026 | 灰色立方体 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3135 |
| <!-- local:item:80027 -->80027 | 黄色的球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3140 |
| <!-- local:item:80028 -->80028 | 蓝色的球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3141 |
| <!-- local:item:80029 -->80029 | 红色的球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3142 |
| <!-- local:item:80030 -->80030 | 紫色的球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3143 |
| <!-- local:item:80031 -->80031 | 绿色的球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3144 |
| <!-- local:item:80032 -->80032 | 灰色的球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3145 |
| <!-- local:item:80033 -->80033 | 黄色的饰品 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3150 |
| <!-- local:item:80034 -->80034 | 蓝色的饰品 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3151 |
| <!-- local:item:80035 -->80035 | 红色的饰品 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3152 |
| <!-- local:item:80036 -->80036 | 紫色的饰品 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3153 |
| <!-- local:item:80037 -->80037 | 绿色的饰品 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3154 |
| <!-- local:item:80038 -->80038 | 灰色的饰品 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/3155 |
| <!-- local:item:80039 -->80039 | 老哨子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3021 |
| <!-- local:item:80040 -->80040 | 白色口哨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/60/3022 |
| <!-- local:item:80041 -->80041 | 珠宝（武器） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3039 |
| <!-- local:item:80042 -->80042 | 虚空宝珠（武器） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3038 |
| <!-- local:item:80043 -->80043 | 珠宝（精炼） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3039 |
| <!-- local:item:80044 -->80044 | 虚空宝珠（精炼） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3038 |
| <!-- local:item:80045 -->80045 | 珠宝（衣服） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3039 |
| <!-- local:item:80046 -->80046 | 虚空宝珠（衣服） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3038 |
| <!-- local:item:80047 -->80047 | 珠宝（项链） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3039 |
| <!-- local:item:80048 -->80048 | 虚空宝珠（项链） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3038 |
| <!-- local:item:80049 -->80049 | 珠宝（手镯） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3039 |
| <!-- local:item:80050 -->80050 | 虚空宝珠（手镯） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3038 |
| <!-- local:item:80051 -->80051 | 珠宝（戒指） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3039 |
| <!-- local:item:80052 -->80052 | 虚空宝珠（戒指） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3038 |
| <!-- local:item:80053 -->80053 | 绿毒之风护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5294 |
| <!-- local:item:80054 -->80054 | 绿毒之神圣护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5295 |
| <!-- local:item:80055 -->80055 | 绿毒之暗黑护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5296 |
| <!-- local:item:80056 -->80056 | 绿毒之幻影护身符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/1/5297 |
| <!-- local:item:80057 -->80057 | 万能符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/7290 |
| <!-- local:item:80058 -->80058 | 万能符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/7290 |
| <!-- local:item:80059 -->80059 | 万能符（特大） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Amulet/All/0/7290 |
| <!-- local:item:80060 -->80060 | 同盟条约 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/74 |
| <!-- local:item:80061 -->80061 | 碎片包裹扩展 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1768 |
| <!-- local:item:80062 -->80062 | 挂机卷（1小时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1594 |
| <!-- local:item:80063 -->80063 | 挂机卷（3小时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1594 |
| <!-- local:item:80064 -->80064 | 宠物经验加速药水（限时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1787 |
| <!-- local:item:80065 -->80065 | 骸骨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1554 |
| <!-- local:item:80066 -->80066 | 江湖初出 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/4501 |
| <!-- local:item:80067 -->80067 | 新进高手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/4502 |
| <!-- local:item:80068 -->80068 | 江湖侠客 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/4503 |
| <!-- local:item:80069 -->80069 | 武林名宿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/4504 |
| <!-- local:item:80070 -->80070 | 仁义大侠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/4505 |
| <!-- local:item:80071 -->80071 | 善仁英雄 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/4506 |
| <!-- local:item:80072 -->80072 | 尊扬义侠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/4507 |
| <!-- local:item:80073 -->80073 | 英雄豪杰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/4508 |
| <!-- local:item:80074 -->80074 | 武林至尊 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/4509 |
| <!-- local:item:80075 -->80075 | 传奇盒子\[限时\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1732 |
| <!-- local:item:80076 -->80076 | 幸运币 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7504 |
| <!-- local:item:80077 -->80077 | 幸运护身符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1150 |
| <!-- local:item:80078 -->80078 | 竹子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1421 |
| <!-- local:item:80079 -->80079 | 火之道士头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/20/372 |
| <!-- local:item:80080 -->80080 | 冰之道士头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/20/372 |
| <!-- local:item:80081 -->80081 | 雷之道士头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/20/372 |
| <!-- local:item:80082 -->80082 | 风之道士头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/20/372 |
| <!-- local:item:80083 -->80083 | 神圣道士头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/20/372 |
| <!-- local:item:80084 -->80084 | 暗黑道士头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/20/372 |
| <!-- local:item:80085 -->80085 | 腐烂道士头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/20/372 |
| <!-- local:item:80086 -->80086 | 诅咒骷髅精灵头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/21/373 |
| <!-- local:item:80087 -->80087 | 腐烂骷髅头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/21/373 |
| <!-- local:item:80088 -->80088 | 幸运骷髅头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/22/373 |
| <!-- local:item:80089 -->80089 | 愤怒之钟（冰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Wizard/25/856 |
| <!-- local:item:80090 -->80090 | 双倍经验卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/180 |
| <!-- local:item:80091 -->80091 | 诅咒偃月 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/23/1311 |
| <!-- local:item:80092 -->80092 | 诅咒降魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/23/1161 |
| <!-- local:item:80093 -->80093 | 诅咒修罗 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/23/1251 |
| <!-- local:item:80094 -->80094 | 如来手镯（暗黑） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Taoist/0/663 |
| <!-- local:item:80095 -->80095 | 如来手镯（幻影） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Taoist/0/663 |
| <!-- local:item:80096 -->80096 | 猫眼（神圣） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/0/838 |
| <!-- local:item:80097 -->80097 | 猫眼（暗黑） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/0/838 |
| <!-- local:item:80098 -->80098 | 猫眼（幻影） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/0/838 |
| <!-- local:item:80099 -->80099 | 毁灭手镯（冰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Wizard/0/683 |
| <!-- local:item:80100 -->80100 | 毁灭手镯（雷） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Wizard/0/683 |
| <!-- local:item:80101 -->80101 | 毁灭手镯（风） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Wizard/0/683 |
| <!-- local:item:80102 -->80102 | 昏暗封印（风） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Wizard/0/816 |
| <!-- local:item:80103 -->80103 | 昏暗封印（雷） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Wizard/0/816 |
| <!-- local:item:80104 -->80104 | 昏暗封印（冰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Wizard/0/816 |
| <!-- local:item:80105 -->80105 | 怨恨项链（暗黑） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/0/815 |
| <!-- local:item:80106 -->80106 | 怨恨项链（幻影） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Taoist/0/815 |
| <!-- local:item:80107 -->80107 | 雷神戒指（雷） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/0/857 |
| <!-- local:item:80108 -->80108 | 雷神戒指（风） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/0/857 |
| <!-- local:item:80109 -->80109 | 雷神戒指（冰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Wizard/0/857 |
| <!-- local:item:80110 -->80110 | 师承戒指（幻影） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/All/45/538 |
| <!-- local:item:80111 -->80111 | 破荒项链（幻影） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/48/819 |
| <!-- local:item:80112 -->80112 | 金棱手镯（幻影） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/42/685 |
| <!-- local:item:80113 -->80113 | 传奇盒子\[永久\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1732 |
| <!-- local:item:80114 -->80114 | 幽蓝马铠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | HorseArmour/All/55/1804 |
| <!-- local:item:80115 -->80115 | 黑金马铠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | HorseArmour/All/65/1803 |
| <!-- local:item:80116 -->80116 | 金缕马甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | HorseArmour/All/1/7640 |
| <!-- local:item:80117 -->80117 | 汉服\(男\) | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/5/945 |
| <!-- local:item:80118 -->80118 | 汉服\(女\) | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/5/955 |
| <!-- local:item:80119 -->80119 | 唐装\(男\) | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/946 |
| <!-- local:item:80120 -->80120 | 唐装\(女\) | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/956 |
| <!-- local:item:80121 -->80121 | 足球服\(男\) | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/2870 |
| <!-- local:item:80122 -->80122 | 足球服\(女\) | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/0/2880 |
| <!-- local:item:80123 -->80123 | 初级武器修炼石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | RefineSpecial/All/0/1703 |
| <!-- local:item:80124 -->80124 | 虚空宝珠（鞋子） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3038 |
| <!-- local:item:80125 -->80125 | 虚空宝珠（头盔） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3038 |
| <!-- local:item:80126 -->80126 | 宠物觉醒药水（限时） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3064 |
| <!-- local:item:80127 -->80127 | 宽翅鱼衣\(男\) | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/50/5345 |
| <!-- local:item:80128 -->80128 | 宽翅鱼衣\(女\) | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Fashion/All/50/5345 |
| <!-- local:item:80129 -->80129 | 印记「盲盒」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7162 |
| <!-- local:item:80130 -->80130 | BUFF药水「盲盒」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7162 |
| <!-- local:item:80131 -->80131 | 宠物周边「盲盒」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7162 |
| <!-- local:item:80132 -->80132 | 附魔石「盲盒」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7162 |
| <!-- local:item:80133 -->80133 | 特殊药水「盲盒」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7162 |
| <!-- local:item:80134 -->80134 | 碎片「盲盒」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7162 |
| <!-- local:item:80135 -->80135 | 六色立方「盲盒」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7162 |
| <!-- local:item:80136 -->80136 | 技能书「盲盒」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7162 |
| <!-- local:item:80137 -->80137 | 声望贡献「盲盒」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7162 |
| <!-- local:item:80138 -->80138 | 初学弟子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4501 |
| <!-- local:item:80139 -->80139 | 无名之辈 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4501 |
| <!-- local:item:80140 -->80140 | 江湖新秀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4501 |
| <!-- local:item:80141 -->80141 | 仗剑天涯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4502 |
| <!-- local:item:80142 -->80142 | 江湖少侠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4502 |
| <!-- local:item:80143 -->80143 | 武林新贵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4502 |
| <!-- local:item:80144 -->80144 | 江湖大侠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4503 |
| <!-- local:item:80145 -->80145 | 江湖豪侠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4503 |
| <!-- local:item:80146 -->80146 | 人海孤鸿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4504 |
| <!-- local:item:80147 -->80147 | 人中龙凤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4504 |
| <!-- local:item:80148 -->80148 | 名震江湖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4505 |
| <!-- local:item:80149 -->80149 | 剑胆琴心 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4505 |
| <!-- local:item:80150 -->80150 | 自成一派 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4506 |
| <!-- local:item:80151 -->80151 | 一派掌门 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4506 |
| <!-- local:item:80152 -->80152 | 威震八方 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4507 |
| <!-- local:item:80153 -->80153 | 一代宗师 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4507 |
| <!-- local:item:80154 -->80154 | 武林盟主 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4508 |
| <!-- local:item:80155 -->80155 | 独孤求败 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4508 |
| <!-- local:item:80156 -->80156 | 飘然归隐 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4509 |
| <!-- local:item:80157 -->80157 | 笑傲江湖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | FameTitle/All/0/4509 |
| <!-- local:item:80158 -->80158 | 五阶民兵\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/78 |
| <!-- local:item:80159 -->80159 | 四阶民兵\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/78 |
| <!-- local:item:80160 -->80160 | 三阶民兵\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/78 |
| <!-- local:item:80161 -->80161 | 二阶民兵\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/78 |
| <!-- local:item:80162 -->80162 | 一阶民兵\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/78 |
| <!-- local:item:80163 -->80163 | 五阶军士\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/323 |
| <!-- local:item:80164 -->80164 | 四阶军士\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/323 |
| <!-- local:item:80165 -->80165 | 三阶军士\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/323 |
| <!-- local:item:80166 -->80166 | 二阶军士\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/323 |
| <!-- local:item:80167 -->80167 | 一阶军士\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/323 |
| <!-- local:item:80168 -->80168 | 五阶副将\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/322 |
| <!-- local:item:80169 -->80169 | 四阶副将\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/322 |
| <!-- local:item:80170 -->80170 | 三阶副将\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/322 |
| <!-- local:item:80171 -->80171 | 二阶副将\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/322 |
| <!-- local:item:80172 -->80172 | 一阶副将\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/322 |
| <!-- local:item:80173 -->80173 | 百人将\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/324 |
| <!-- local:item:80174 -->80174 | 牙门将\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/325 |
| <!-- local:item:80175 -->80175 | 都尉\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/326 |
| <!-- local:item:80176 -->80176 | 羽林中郎将\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/327 |
| <!-- local:item:80177 -->80177 | 虎贲中郎将\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/328 |
| <!-- local:item:80178 -->80178 | 偏将军\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/1744 |
| <!-- local:item:80179 -->80179 | 四征将军\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/1745 |
| <!-- local:item:80180 -->80180 | 骠骑将军\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/1743 |
| <!-- local:item:80181 -->80181 | 大将军\[军衔\] | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Emblem/All/1/1870 |
| <!-- local:item:80182 -->80182 | 1元红包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/5002 |
| <!-- local:item:80183 -->80183 | 2元红包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/5002 |
| <!-- local:item:80184 -->80184 | 5元红包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/5002 |
| <!-- local:item:80185 -->80185 | 10元红包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/5002 |
| <!-- local:item:80186 -->80186 | 50元红包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/5002 |
| <!-- local:item:80187 -->80187 | 100元红包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/5002 |
| <!-- local:item:80188 -->80188 | 五倍经验卷（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/180 |
| <!-- local:item:80189 -->80189 | 十倍经验卷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/180 |
| <!-- local:item:80190 -->80190 | 蓝莓糖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2931 |
| <!-- local:item:80191 -->80191 | 豌豆糖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2932 |
| <!-- local:item:80192 -->80192 | 地瓜糖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2933 |
| <!-- local:item:80193 -->80193 | 橘子糖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2934 |
| <!-- local:item:80194 -->80194 | 鱼子酱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2856 |
| <!-- local:item:80195 -->80195 | 经验药水「限时」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1686 |
| <!-- local:item:80196 -->80196 | 宝藏补品「限时」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1687 |
| <!-- local:item:80197 -->80197 | 经验爆率补药 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1687 |
| <!-- local:item:80198 -->80198 | 洞穴探险补品「限时」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1689 |
| <!-- local:item:80199 -->80199 | 破坏药水「限时」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1770 |
| <!-- local:item:80200 -->80200 | 自然药水「限时」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1771 |
| <!-- local:item:80201 -->80201 | 灵魂药水「限时」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1772 |
| <!-- local:item:80202 -->80202 | 生命药水「限时」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1773 |
| <!-- local:item:80203 -->80203 | 法力药水「限时」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1774 |
| <!-- local:item:80204 -->80204 | 疾风药水「限时」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1785 |
| <!-- local:item:80205 -->80205 | 敏捷药水「限时」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1775 |
| <!-- local:item:80206 -->80206 | 技能熟练药水「限时」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/69 |
| <!-- local:item:80207 -->80207 | 幸运药水「限时」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1779 |
| <!-- local:item:80208 -->80208 | 宠物快速收集药水「限时」 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2759 |
| <!-- local:item:80209 -->80209 | 玄铁马甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | HorseArmour/All/3/7641 |
| <!-- local:item:80210 -->80210 | 太阳水（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/20 |
| <!-- local:item:80211 -->80211 | 强效太阳水（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/21 |
| <!-- local:item:80212 -->80212 | 万年雪霜（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/70 |
| <!-- local:item:80213 -->80213 | 意识药水（3级）（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/3/3069 |
| <!-- local:item:80214 -->80214 | 意识药水（5级）（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/5/3069 |
| <!-- local:item:80215 -->80215 | 意识药水（7级）（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/7/3069 |
| <!-- local:item:80216 -->80216 | 意识药水（10级）（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/10/3069 |
| <!-- local:item:80217 -->80217 | 意识药水（11级）（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/11/3069 |
| <!-- local:item:80218 -->80218 | 意识药水（13级）（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/13/3069 |
| <!-- local:item:80219 -->80219 | 意识药水（15级）（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/15/3069 |
| <!-- local:item:80220 -->80220 | 宠物经验加速药水（限时）（10倍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/1787 |
| <!-- local:item:80221 -->80221 | BOSS探查符 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/7261 |
| <!-- local:item:80222 -->80222 | 超级夜明珠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/7344 |
| <!-- local:item:80223 -->80223 | 火罐 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shield/All/15/2886 |
| <!-- local:item:80224 -->80224 | 宠物背带 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionBack/All/1/7580 |
| <!-- local:item:80225 -->80225 | 宠物头带 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionHead/All/1/7570 |
| <!-- local:item:80226 -->80226 | 袖里乾坤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | CompanionBag/All/1/1551 |
| <!-- local:item:80227 -->80227 | 技能熟练药水「限时」（百倍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/69 |
| <!-- local:item:80228 -->80228 | 宠物快速收集药水「限时」（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/2759 |
| <!-- local:item:80229 -->80229 | 充值礼包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1667 |
| <!-- local:item:80230 -->80230 | 推广礼包 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1730 |
| <!-- local:item:80231 -->80231 | 新手祝福 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7202 |
| <!-- local:item:80232 -->80232 | 中毒免疫恢复神水 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1779 |
| <!-- local:item:80233 -->80233 | 火桶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shield/All/30/2888 |
| <!-- local:item:80234 -->80234 | 木盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shield/All/40/1900 |
| <!-- local:item:80235 -->80235 | 铁盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shield/All/50/1902 |
| <!-- local:item:80236 -->80236 | 精钢盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shield/All/60/1914 |
| <!-- local:item:80237 -->80237 | 寒铁晶盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shield/All/1/1924 |
| <!-- local:item:80238 -->80238 | 四叶草 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Torch/All/1/5046 |
| <!-- local:item:80239 -->80239 | 魔晶石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ore/All/0/224 |
| <!-- local:item:80240 -->80240 | BOSS宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/5022 |
| <!-- local:item:80242 -->80242 | 快刀斩马2 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Nothing/All/0/0 |
| <!-- local:item:80243 -->80243 | 邪恶之心 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1142 |
| <!-- local:item:80244 -->80244 | 宠物召唤券 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3070 |
| <!-- local:item:80245 -->80245 | 神秘时空符文 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1322 |
| <!-- local:item:80246 -->80246 | 经验珠（50万） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/40/1834 |
| <!-- local:item:80247 -->80247 | 翠虎飞龙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shield/All/2/1926 |
| <!-- local:item:80248 -->80248 | 翠虎飞龙碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1845 |
| <!-- local:item:80250 -->80250 | 桃之夭夭 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/WarWizTao/2/3293 |
| <!-- local:item:80251 -->80251 | 桃之灼灼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/All/2/3279 |
| <!-- local:item:80252 -->80252 | 桃源之心 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/All/2/3253 |
| <!-- local:item:80253 -->80253 | 武器特殊属性修炼石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4014 |
| <!-- local:item:80254 -->80254 | 首饰特殊属性修炼石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4010 |
| <!-- local:item:80255 -->80255 | 武器麻痹修炼石（弃用） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4011 |
| <!-- local:item:80256 -->80256 | 破空石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4040 |
| <!-- local:item:80257 -->80257 | 武器神圣元素修炼石（弃用） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/4012 |
| <!-- local:item:80258 -->80258 | 玄武盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shield/All/3/1927 |
| <!-- local:item:91340 -->91340 | 召唤券（田园犬） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/Warrior/700/7253 |
| <!-- local:item:91341 -->91341 | 召唤券（机灵鼠） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/Wizard/700/7253 |
| <!-- local:item:91342 -->91342 | 双倍经验卷（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/180 |
| <!-- local:item:91343 -->91343 | 垂柳舞（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/7/304 |
| <!-- local:item:91344 -->91344 | 潜行服\(男\) | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/1/2000 |
| <!-- local:item:91345 -->91345 | 潜行服\(女\) | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/1/2010 |
| <!-- local:item:91346 -->91346 | 入门暗杀之刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/1/2300 |
| <!-- local:item:91347 -->91347 | 蔓藤舞（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/10/304 |
| <!-- local:item:91348 -->91348 | 磨炼（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/12/304 |
| <!-- local:item:91349 -->91349 | 毒云（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/14/304 |
| <!-- local:item:91350 -->91350 | 盛开（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/19/304 |
| <!-- local:item:91351 -->91351 | 潜行（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/20/304 |
| <!-- local:item:91352 -->91352 | 白莲（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/22/304 |
| <!-- local:item:91353 -->91353 | 满月恶狼（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/22/304 |
| <!-- local:item:91354 -->91354 | 亡灵束缚（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/24/304 |
| <!-- local:item:91355 -->91355 | 红莲（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/24/304 |
| <!-- local:item:91356 -->91356 | 烈焰（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/26/304 |
| <!-- local:item:91357 -->91357 | 血禅（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/26/304 |
| <!-- local:item:91358 -->91358 | 血之盟约（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/26/304 |
| <!-- local:item:91359 -->91359 | 月季（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/27/304 |
| <!-- local:item:91360 -->91360 | 亡灵替身（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/30/304 |
| <!-- local:item:91361 -->91361 | 孽报（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/30/304 |
| <!-- local:item:91362 -->91362 | 亡灵之手（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/30/304 |
| <!-- local:item:91363 -->91363 | 残月之乱（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/32/304 |
| <!-- local:item:91364 -->91364 | 鬼灵步（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/32/304 |
| <!-- local:item:91365 -->91365 | 神机妙算（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/34/304 |
| <!-- local:item:91366 -->91366 | 新月爆炎龙（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/38/309 |
| <!-- local:item:91367 -->91367 | 盛开（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/38/304 |
| <!-- local:item:91368 -->91368 | 心机一转（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/40/304 |
| <!-- local:item:91369 -->91369 | 鹰击（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/43/309 |
| <!-- local:item:91370 -->91370 | 黄泉旅者（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/42/304 |
| <!-- local:item:91371 -->91371 | 狂涛涌泉（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/45/309 |
| <!-- local:item:91372 -->91372 | 修罗降临（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/45/304 |
| <!-- local:item:91373 -->91373 | 罗刹降临（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/45/304 |
| <!-- local:item:91374 -->91374 | 深渊苦海（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/45/304 |
| <!-- local:item:91375 -->91375 | 日闪（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/45/304 |
| <!-- local:item:91376 -->91376 | 风之闪避（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/50/309 |
| <!-- local:item:91377 -->91377 | 风之守护（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/52/309 |
| <!-- local:item:91378 -->91378 | 鬼气耳爪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/15/2302 |
| <!-- local:item:91379 -->91379 | 夜行衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/11/2000 |
| <!-- local:item:91380 -->91380 | 夜行衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/11/2010 |
| <!-- local:item:91381 -->91381 | 速战速决宝铠（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/22/2001 |
| <!-- local:item:91382 -->91382 | 速战速决宝铠（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/22/2011 |
| <!-- local:item:91383 -->91383 | 入门暗杀面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/9/2100 |
| <!-- local:item:91384 -->91384 | 初级暗杀面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/20/2100 |
| <!-- local:item:91385 -->91385 | 高级暗杀面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/30/2101 |
| <!-- local:item:91386 -->91386 | 特级暗杀面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/35/2102 |
| <!-- local:item:91387 -->91387 | 迷雾匕首 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/23/2202 |
| <!-- local:item:91388 -->91388 | 诡计之衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/25/2001 |
| <!-- local:item:91389 -->91389 | 诡计之衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/25/2011 |
| <!-- local:item:91390 -->91390 | 精细诡计之衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/26/2001 |
| <!-- local:item:91391 -->91391 | 精细诡计之衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/26/2011 |
| <!-- local:item:91392 -->91392 | 黑影战袍（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/33/2002 |
| <!-- local:item:91393 -->91393 | 黑影战袍（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/33/2012 |
| <!-- local:item:91394 -->91394 | 斩首宝甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/38/2002 |
| <!-- local:item:91395 -->91395 | 斩首宝甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/38/2012 |
| <!-- local:item:91396 -->91396 | 日天战袍（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/44/2003 |
| <!-- local:item:91397 -->91397 | 日天战袍（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/44/2013 |
| <!-- local:item:91398 -->91398 | 修罗战甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/1/3382 |
| <!-- local:item:91399 -->91399 | 修罗战甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/1/3392 |
| <!-- local:item:91400 -->91400 | 烟雨宝铠（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/40/2003 |
| <!-- local:item:91401 -->91401 | 烟雨宝铠（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/40/2013 |
| <!-- local:item:91402 -->91402 | 白莲面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/40/2101 |
| <!-- local:item:91403 -->91403 | 玄武刺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/33/2305 |
| <!-- local:item:91404 -->91404 | 暗杀之刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/3/2300 |
| <!-- local:item:91405 -->91405 | 进化暗杀之刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/10/2300 |
| <!-- local:item:91406 -->91406 | 烟雨指引 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/26/2301 |
| <!-- local:item:91407 -->91407 | 冰之心 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/29/2203 |
| <!-- local:item:91408 -->91408 | 霸王刺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/31/2304 |
| <!-- local:item:91409 -->91409 | 复仇者面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/40/2105 |
| <!-- local:item:91410 -->91410 | 猎鹰面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/50/2109 |
| <!-- local:item:91411 -->91411 | 黑乌鸦面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/55/2108 |
| <!-- local:item:91412 -->91412 | 先知面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/0/2120 |
| <!-- local:item:91413 -->91413 | 钢铁之手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/35/2306 |
| <!-- local:item:91414 -->91414 | 赤色决议 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/38/2307 |
| <!-- local:item:91415 -->91415 | 罗刹护甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/50/2004 |
| <!-- local:item:91416 -->91416 | 罗刹护甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/50/2014 |
| <!-- local:item:91417 -->91417 | 青莲刺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/45/2209 |
| <!-- local:item:91418 -->91418 | 天命 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/50/3452 |
| <!-- local:item:91419 -->91419 | 生死轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/1/3451 |
| <!-- local:item:91420 -->91420 | 锋翼剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/300/6230 |
| <!-- local:item:91421 -->91421 | 潜龙遁甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/58/2006 |
| <!-- local:item:91422 -->91422 | 潜龙遁甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/58/2016 |
| <!-- local:item:91423 -->91423 | 死神双剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/40/2540 |
| <!-- local:item:91424 -->91424 | 夜叉斑盔甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/52/2005 |
| <!-- local:item:91425 -->91425 | 夜叉斑盔甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/52/2015 |
| <!-- local:item:91426 -->91426 | 凤凰轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/50/2222 |
| <!-- local:item:91427 -->91427 | 最后抵抗（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/52/3040 |
| <!-- local:item:91428 -->91428 | 神魂湮灭剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/5/2550 |
| <!-- local:item:91429 -->91429 | 冰龙逆天杀刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/84/3455 |
| <!-- local:item:91430 -->91430 | 桃源斩轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/2/3454 |
| <!-- local:item:91431 -->91431 | 深渊之甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/62/2004 |
| <!-- local:item:91432 -->91432 | 深渊之甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/62/2014 |
| <!-- local:item:91433 -->91433 | 黄昏手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Assassin/82/3261 |
| <!-- local:item:91434 -->91434 | 修罗戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/1/3287 |
| <!-- local:item:91435 -->91435 | 黄昏项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Assassin/82/3241 |
| <!-- local:item:91436 -->91436 | 暗影艺术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/70/3043 |
| <!-- local:item:91437 -->91437 | 新手刺客面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/22/2120 |
| <!-- local:item:91438 -->91438 | 新手无敌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/22/2207 |
| <!-- local:item:91439 -->91439 | 新手日天甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/22/2003 |
| <!-- local:item:91440 -->91440 | 新手日天甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/22/2013 |
| <!-- local:item:91441 -->91441 | 龙盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Shield/All/5/1910 |
| <!-- local:item:91442 -->91442 | 蛇骨剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/94/6230 |
| <!-- local:item:91443 -->91443 | 龙吟项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Necklace/Assassin/5/3247 |
| <!-- local:item:91444 -->91444 | 龙吟手镯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Bracelet/Assassin/5/3271 |
| <!-- local:item:91445 -->91445 | 龙吟戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Ring/Assassin/5/3286 |
| <!-- local:item:91446 -->91446 | 黑玉战甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/2/6001 |
| <!-- local:item:91447 -->91447 | 黑玉战甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/2/6011 |
| <!-- local:item:91448 -->91448 | 亡灵呐喊 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/27/2202 |
| <!-- local:item:91449 -->91449 | 垂柳舞 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/7/304 |
| <!-- local:item:91450 -->91450 | 蔓藤舞 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/10/304 |
| <!-- local:item:91451 -->91451 | 磨炼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/12/304 |
| <!-- local:item:91452 -->91452 | 毒云 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/14/304 |
| <!-- local:item:91453 -->91453 | 盛开 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/19/304 |
| <!-- local:item:91454 -->91454 | 潜行 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/20/304 |
| <!-- local:item:91455 -->91455 | 白莲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/22/304 |
| <!-- local:item:91456 -->91456 | 满月恶狼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/22/304 |
| <!-- local:item:91457 -->91457 | 亡灵束缚 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/24/304 |
| <!-- local:item:91458 -->91458 | 红莲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/24/304 |
| <!-- local:item:91459 -->91459 | 烈焰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/26/304 |
| <!-- local:item:91460 -->91460 | 血禅 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/26/304 |
| <!-- local:item:91461 -->91461 | 血之盟约 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/26/304 |
| <!-- local:item:91462 -->91462 | 月季 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/27/304 |
| <!-- local:item:91463 -->91463 | 亡灵替身 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/30/304 |
| <!-- local:item:91464 -->91464 | 孽报 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/30/304 |
| <!-- local:item:91465 -->91465 | 亡灵之手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/30/304 |
| <!-- local:item:91466 -->91466 | 残月之乱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/32/304 |
| <!-- local:item:91467 -->91467 | 鬼灵步 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/32/304 |
| <!-- local:item:91468 -->91468 | 神机妙算 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/34/304 |
| <!-- local:item:91469 -->91469 | 新月爆炎龙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/38/309 |
| <!-- local:item:91470 -->91470 | 盛开 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/38/304 |
| <!-- local:item:91471 -->91471 | 心机一转 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/40/304 |
| <!-- local:item:91472 -->91472 | 鹰击 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/43/309 |
| <!-- local:item:91473 -->91473 | 黄泉旅者 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/42/304 |
| <!-- local:item:91474 -->91474 | 狂涛涌泉 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/45/309 |
| <!-- local:item:91475 -->91475 | 修罗降临 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/45/304 |
| <!-- local:item:91476 -->91476 | 罗刹降临 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/45/304 |
| <!-- local:item:91477 -->91477 | 深渊苦海 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/45/304 |
| <!-- local:item:91478 -->91478 | 日闪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/45/304 |
| <!-- local:item:91479 -->91479 | 风之闪避 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/50/309 |
| <!-- local:item:91480 -->91480 | 风之守护 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/52/309 |
| <!-- local:item:95181 -->95181 | 珠宝（鞋子） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3039 |
| <!-- local:item:95182 -->95182 | 珠宝（头盔） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/0/3039 |
| <!-- local:item:95184 -->95184 | 慧明之杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Wizard/5/3438 |
| <!-- local:item:95185 -->95185 | 天赋神剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Warrior/5/6200 |
| <!-- local:item:95186 -->95186 | 万古道兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Taoist/5/3441 |
| <!-- local:item:95187 -->95187 | 血火 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/38/304 |
| <!-- local:item:95188 -->95188 | 血火（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/38/304 |
| <!-- local:item:95189 -->95189 | 深渊 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/35/304 |
| <!-- local:item:95190 -->95190 | 深渊（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/35/304 |
| <!-- local:item:95191 -->95191 | 业火 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/65/1860 |
| <!-- local:item:95192 -->95192 | 业火（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/65/3043 |
| <!-- local:item:95193 -->95193 | 集中 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/55/309 |
| <!-- local:item:95194 -->95194 | 集中（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/55/309 |
| <!-- local:item:95195 -->95195 | 分身术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/52/309 |
| <!-- local:item:95196 -->95196 | 分身术（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/52/309 |
| <!-- local:item:95197 -->95197 | 施毒大法 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/65/1860 |
| <!-- local:item:95198 -->95198 | 施毒大法（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/65/3043 |
| <!-- local:item:95199 -->95199 | 暗鬼阵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Taoist/70/1860 |
| <!-- local:item:95200 -->95200 | 空破斩 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/65/309 |
| <!-- local:item:95201 -->95201 | 挑衅 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/60/1860 |
| <!-- local:item:95202 -->95202 | 挑衅（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/60/3043 |
| <!-- local:item:95205 -->95205 | 麒麟马甲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | HorseArmour/All/5/5000 |
| <!-- local:item:95206 -->95206 | 马铠碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/1/1626 |
| <!-- local:item:95207 -->95207 | 沃玛悔悟 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/Assassin/23/2301 |
| <!-- local:item:95208 -->95208 | 圣火盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/WarWizTao/5/3480 |
| <!-- local:item:95209 -->95209 | 战-幻殇碧陌铠（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/5/3340 |
| <!-- local:item:95210 -->95210 | 幻世衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/3/6001 |
| <!-- local:item:95211 -->95211 | 龙鳞暗光盔（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/0/6101 |
| <!-- local:item:95212 -->95212 | 龙鳞宝刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Weapon/All/0/6200 |
| <!-- local:item:95213 -->95213 | 战-幻殇碧陌铠（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Warrior/5/3350 |
| <!-- local:item:95214 -->95214 | 幻世衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/3/6011 |
| <!-- local:item:95215 -->95215 | 幻陌盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/5/3531 |
| <!-- local:item:95216 -->95216 | 龙鳞暗光盔（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Helmet/Assassin/0/6111 |
| <!-- local:item:95217 -->95217 | 凶陌圣甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/4/3381 |
| <!-- local:item:95218 -->95218 | 凶陌圣甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/4/3391 |
| <!-- local:item:95219 -->95219 | 幻世魔衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/3/2700 |
| <!-- local:item:95220 -->95220 | 幻世魔衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/3/2710 |
| <!-- local:item:95221 -->95221 | 沐水天衣（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/3/3325 |
| <!-- local:item:95222 -->95222 | 沐水天衣（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/3/3335 |
| <!-- local:item:95223 -->95223 | 玄云鸾暮铠（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/4/3324 |
| <!-- local:item:95224 -->95224 | 玄云鸾暮铠（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/4/3334 |
| <!-- local:item:95225 -->95225 | 炎狱魔神铠（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/0/3328 |
| <!-- local:item:95226 -->95226 | 炎狱魔神铠（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/All/0/3338 |
| <!-- local:item:95227 -->95227 | 锦绣仙袍（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/0/3342 |
| <!-- local:item:95228 -->95228 | 锦绣仙袍（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/WarWizTao/0/3352 |
| <!-- local:item:95229 -->95229 | 刺客-银月泣影甲（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/5/2004 |
| <!-- local:item:95230 -->95230 | 刺客-银月泣影甲（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Assassin/5/2014 |
| <!-- local:item:95231 -->95231 | 道-幻殇碧陌铠（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/5/3362 |
| <!-- local:item:95232 -->95232 | 道-幻殇碧陌铠（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Taoist/5/3372 |
| <!-- local:item:95233 -->95233 | 法-幻殇碧陌铠（男） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/5/3360 |
| <!-- local:item:95234 -->95234 | 法-幻殇碧陌铠（女） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Armour/Wizard/5/3370 |
| <!-- local:item:95235 -->95235 | 冰蚕丝 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/2878 |
| <!-- local:item:95236 -->95236 | 金缕玉衣碎片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/1765 |
| <!-- local:item:95237 -->95237 | 点化石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/3172 |
| <!-- local:item:95238 -->95238 | 高级技能残片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3031 |
| <!-- local:item:95239 -->95239 | 稀世技能残片 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Material/All/0/3033 |
| <!-- local:item:99133 -->99133 | 百花盛开 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/58/309 |
| <!-- local:item:99134 -->99134 | 百花盛开（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/58/3040 |
| <!-- local:item:99136 -->99136 | 天之怒火 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Wizard/70/1860 |
| <!-- local:item:99137 -->99137 | 破空斩 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/60/1860 |
| <!-- local:item:99138 -->99138 | 破空斩（秘籍） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/60/3043 |
| <!-- local:item:99139 -->99139 | 暗夜艺术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/65/3040 |
| <!-- local:item:99140 -->99140 | 新手关怀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/7204 |
| <!-- local:item:99141 -->99141 | 快乐加倍丸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1687 |
| <!-- local:item:110836 -->110836 | 天雷锤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Warrior/70/1860 |
| <!-- local:item:110837 -->110837 | 暗影艺术 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Book/Assassin/70/1860 |
| <!-- local:item:122538 -->122538 | 十倍经验卷（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/180 |
| <!-- local:item:122539 -->122539 | 经验爆率补药（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1687 |
| <!-- local:item:122540 -->122540 | 爆率葫芦（1000%）（绑定） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | Consumable/All/1/1686 |

## 官方怪物完整表

| 正式名 | 别名 | 类别/区域/组成 | 状态 | 引入版本 | 来源ID | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| 诺玛骑兵 |  | 诺玛遗址 | confirmed-145 | — | official-145-monsters-nooma | 官方目录“诺玛遗址怪物”表的独立条目。 |
| 诺玛装甲兵 |  | 诺玛遗址 | confirmed-145 | — | official-145-monsters-nooma | 官方目录“诺玛遗址怪物”表的独立条目。 |
| 诺玛抛石兵 |  | 诺玛遗址 | confirmed-145 | — | official-145-monsters-nooma | 官方目录“诺玛遗址怪物”表的独立条目。 |
| 诺玛司令 |  | 诺玛遗址 | confirmed-145 | — | official-145-monsters-nooma | 官方目录“诺玛遗址怪物”表的独立条目。 |
| 诺玛斧兵 |  | 诺玛遗址 | confirmed-145 | — | official-145-monsters-nooma | 官方目录“诺玛遗址怪物”表的独立条目。 |
| 诺玛教主 |  | 诺玛遗址 | confirmed-145 | — | official-145-monsters-nooma | 官方目录“诺玛遗址怪物”表的独立条目。 |
| 男性诺玛 |  | 未明示（页面分组：诺玛平民） | confirmed-145 | — | official-145-monsters-nooma | 官方目录“诺玛平民”表的独立条目；页面没有给出具体地图，故不补写地点。 |
| 女性诺玛 |  | 未明示（页面分组：诺玛平民） | confirmed-145 | — | official-145-monsters-nooma | 官方目录“诺玛平民”表的独立条目；页面没有给出具体地图，故不补写地点。 |
| 小诺玛 |  | 未明示（页面分组：诺玛平民） | confirmed-145 | — | official-145-monsters-nooma | 官方目录“诺玛平民”表的独立条目；页面没有给出具体地图，故不补写地点。 |
| 独臂诺玛 |  | 未明示（页面分组：诺玛平民） | confirmed-145 | — | official-145-monsters-nooma | 官方目录“诺玛平民”表的独立条目；页面没有给出具体地图，故不补写地点。 |
| 单腿诺玛 |  | 未明示（页面分组：诺玛平民） | confirmed-145 | — | official-145-monsters-nooma | 官方目录“诺玛平民”表的独立条目；页面没有给出具体地图，故不补写地点。 |

## 本服怪物完整对比表

| 快照索引 | 数据库原名 | 官方1.45名称 | 匹配状态 | 匹配方式 | 判断依据 | 证据来源 | 处理建议 | 本地字段（等级/AI/图像/Boss） |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| <!-- local:monster:10001 -->10001 | 鸡 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 2/1/2/False |
| <!-- local:monster:10002 -->10002 | 猪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 3/2/3/False |
| <!-- local:monster:10003 -->10003 | 鹿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 6/2/4/False |
| <!-- local:monster:10004 -->10004 | 牛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 4/2/5/False |
| <!-- local:monster:10005 -->10005 | 羊 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 5/2/6/False |
| <!-- local:monster:10006 -->10006 | 多钩猫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 10/0/7/False |
| <!-- local:monster:10007 -->10007 | 狼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 15/3/8/False |
| <!-- local:monster:10008 -->10008 | 森林雪人 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 13/0/9/False |
| <!-- local:monster:10009 -->10009 | 栗子树 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 10/4/10/False |
| <!-- local:monster:10010 -->10010 | 食人花 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 10/5/11/False |
| <!-- local:monster:10011 -->10011 | 半兽战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 13/0/12/False |
| <!-- local:monster:10012 -->10012 | 虎蛇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 15/0/13/False |
| <!-- local:monster:10013 -->10013 | 毒蜘蛛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 10/6/14/False |
| <!-- local:monster:10014 -->10014 | 稻草人 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 10/0/15/False |
| <!-- local:monster:10015 -->10015 | 半兽人 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 13/0/277/False |
| <!-- local:monster:10016 -->10016 | 多角虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 13/0/36/False |
| <!-- local:monster:10017 -->10017 | 猎鹰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 13/0/248/False |
| <!-- local:monster:10018 -->10018 | 威思尔小虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 13/6/37/False |
| <!-- local:monster:10019 -->10019 | 盔甲虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 13/0/35/False |
| <!-- local:monster:10020 -->10020 | 山洞蝙蝠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 18/0/17/False |
| <!-- local:monster:10021 -->10021 | 掷斧骷髅 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 18/7/21/False |
| <!-- local:monster:10022 -->10022 | 蝎子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 18/3/18/False |
| <!-- local:monster:10023 -->10023 | 骷髅战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 18/0/20/False |
| <!-- local:monster:10024 -->10024 | 骷髅 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 18/0/19/False |
| <!-- local:monster:10025 -->10025 | 骷髅战将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 18/0/22/False |
| <!-- local:monster:10026 -->10026 | 盔甲蚂蚁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 26/0/31/False |
| <!-- local:monster:10027 -->10027 | 蚂蚁战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 25/0/32/False |
| <!-- local:monster:10028 -->10028 | 蚂蚁道士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 27/12/33/False |
| <!-- local:monster:10029 -->10029 | 爆毒蚂蚁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 28/7/34/False |
| <!-- local:monster:10030 -->10030 | 洞蛆 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 20/8/24/False |
| <!-- local:monster:10032 -->10032 | 老道僵尸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 20/9/25/False |
| <!-- local:monster:10033 -->10033 | 僧侣僵尸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 20/10/26/False |
| <!-- local:monster:10034 -->10034 | 僵尸2 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 20/11/27/False |
| <!-- local:monster:10035 -->10035 | 僵尸3 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 20/11/28/False |
| <!-- local:monster:10036 -->10036 | 僵尸4 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 20/11/29/False |
| <!-- local:monster:10037 -->10037 | 多脚虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 20/0/38/False |
| <!-- local:monster:10038 -->10038 | 蜘蛛娃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 20/0/39/False |
| <!-- local:monster:10039 -->10039 | 胞眼虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 20/0/40/False |
| <!-- local:monster:10041 -->10041 | 浪子人鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 25/0/48/False |
| <!-- local:monster:10042 -->10042 | 腐蚀人鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 25/14/49/False |
| <!-- local:monster:10043 -->10043 | 骷髅弓箭手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 31/7/99/False |
| <!-- local:monster:10044 -->10044 | 骷髅武士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 32/0/100/False |
| <!-- local:monster:10045 -->10045 | 骷髅武将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 33/0/101/False |
| <!-- local:monster:10046 -->10046 | 骷髅士兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 30/42/102/False |
| <!-- local:monster:10047 -->10047 | 诺玛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 35/0/74/False |
| <!-- local:monster:10048 -->10048 | 诺玛法老 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 36/26/75/False |
| <!-- local:monster:10049 -->10049 | 诺玛将士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 37/0/76/False |
| <!-- local:monster:10050 -->10050 | 沙漠鱼魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 35/25/77/False |
| <!-- local:monster:10051 -->10051 | 沙漠石人 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 36/27/78/False |
| <!-- local:monster:10052 -->10052 | 沙漠风魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 38/28/79/False |
| <!-- local:monster:10053 -->10053 | 沙漠树魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 35/29/80/False |
| <!-- local:monster:10054 -->10054 | 暗黑战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 26/7/51/False |
| <!-- local:monster:10055 -->10055 | 粪虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 25/0/248/False |
| <!-- local:monster:10056 -->10056 | 沃玛战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 28/0/52/False |
| <!-- local:monster:10057 -->10057 | 火焰沃玛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 29/15/53/False |
| <!-- local:monster:10058 -->10058 | 角蝇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 30/44/104/False |
| <!-- local:monster:10059 -->10059 | 蝙蝠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 1/0/105/False |
| <!-- local:monster:10060 -->10060 | 楔蛾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 32/8/106/False |
| <!-- local:monster:10061 -->10061 | 红野猪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 34/0/107/False |
| <!-- local:monster:10062 -->10062 | 蝎蛇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 35/0/108/False |
| <!-- local:monster:10063 -->10063 | 黑野猪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 34/0/109/False |
| <!-- local:monster:10064 -->10064 | 跳跳蜂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 34/0/41/False |
| <!-- local:monster:10065 -->10065 | 蜈蚣 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 33/0/42/False |
| <!-- local:monster:10066 -->10066 | 钳虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 36/0/45/False |
| <!-- local:monster:10067 -->10067 | 蝴蝶虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 35/0/43/False |
| <!-- local:monster:10068 -->10068 | 黑色恶蛆 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 32/0/44/False |
| <!-- local:monster:10069 -->10069 | 月魔蜘蛛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 35/8/56/False |
| <!-- local:monster:10070 -->10070 | 幻影蜘蛛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 36/17/57/False |
| <!-- local:monster:10071 -->10071 | 爆裂蜘蛛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 6/18/58/False |
| <!-- local:monster:10072 -->10072 | 血巨人 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 40/0/59/False |
| <!-- local:monster:10073 -->10073 | 血金刚 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 41/0/60/False |
| <!-- local:monster:10074 -->10074 | 花色蜘蛛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 37/14/61/False |
| <!-- local:monster:10075 -->10075 | 黑角蜘蛛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 38/0/62/False |
| <!-- local:monster:10076 -->10076 | 祖玛弓箭手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 47/20/64/False |
| <!-- local:monster:10077 -->10077 | 祖玛雕像 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 48/21/65/False |
| <!-- local:monster:10078 -->10078 | 祖玛卫士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 49/21/66/False |
| <!-- local:monster:10079 -->10079 | 大老鼠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 45/0/67/False |
| <!-- local:monster:10080 -->10080 | 潘夜战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 46/0/91/False |
| <!-- local:monster:10081 -->10081 | 潘夜冰魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 47/35/92/False |
| <!-- local:monster:10082 -->10082 | 潘夜右护卫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 48/36/97/False |
| <!-- local:monster:10083 -->10083 | 潘夜云魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 47/37/93/False |
| <!-- local:monster:10084 -->10084 | 潘夜左护卫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 48/38/96/False |
| <!-- local:monster:10085 -->10085 | 潘夜风魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 47/39/95/False |
| <!-- local:monster:10086 -->10086 | 潘夜火魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 47/40/94/False |
| <!-- local:monster:10087 -->10087 | 东魔神怪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 45/0/69/False |
| <!-- local:monster:10088 -->10088 | 猿猴战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 42/23/70/False |
| <!-- local:monster:10089 -->10089 | 猿猴战将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 43/24/70/False |
| <!-- local:monster:10090 -->10090 | 巨象兽 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 44/25/71/False |
| <!-- local:monster:10091 -->10091 | 西魔神怪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 45/7/72/False |
| <!-- local:monster:10092 -->10092 | 亡灵武士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 90/0/100/False |
| <!-- local:monster:10093 -->10093 | 亡灵弓箭手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 90/7/99/False |
| <!-- local:monster:10094 -->10094 | 亡灵士兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 90/0/102/False |
| <!-- local:monster:10098 -->10098 | 黑度紫红女神 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 51/46/112/False |
| <!-- local:monster:10099 -->10099 | 黑度绿荫女神 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 51/47/113/False |
| <!-- local:monster:10100 -->10100 | 武力神将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 53/48/114/False |
| <!-- local:monster:10101 -->10101 | 犬猴魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 48/0/122/False |
| <!-- local:monster:10102 -->10102 | 轻甲守卫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 50/0/123/False |
| <!-- local:monster:10103 -->10103 | 爆毒神魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 52/56/124/False |
| <!-- local:monster:10104 -->10104 | 神舰守卫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 55/0/125/False |
| <!-- local:monster:10105 -->10105 | 触角神魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 51/57/126/False |
| <!-- local:monster:10106 -->10106 | 恶形鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 50/0/127/False |
| <!-- local:monster:10107 -->10107 | 海神将领 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 53/58/128/False |
| <!-- local:monster:10108 -->10108 | 红衣法师 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 54/59/129/False |
| <!-- local:monster:10109 -->10109 | 异界之门 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 100/30/81/False |
| <!-- local:monster:10110 -->10110 | 地牢紫红女神 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 52/46/112/False |
| <!-- local:monster:10111 -->10111 | 石像狮子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 48/49/115/False |
| <!-- local:monster:10112 -->10112 | 武力魔神将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 53/48/114/False |
| <!-- local:monster:10113 -->10113 | 火焰狮子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 50/50/116/False |
| <!-- local:monster:10114 -->10114 | 诺玛骑兵 | 诺玛骑兵 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-monsters-nooma | 确认保留 | 60/33/132/False |
| <!-- local:monster:10115 -->10115 | 诺玛司令 | 诺玛司令 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-monsters-nooma | 确认保留 | 58/62/133/False |
| <!-- local:monster:10116 -->10116 | 诺玛抛石兵 | 诺玛抛石兵 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-monsters-nooma | 确认保留 | 57/63/134/False |
| <!-- local:monster:10117 -->10117 | 诺玛斧兵 | 诺玛斧兵 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-monsters-nooma | 确认保留 | 56/48/135/False |
| <!-- local:monster:10118 -->10118 | 诺玛装甲兵 | 诺玛装甲兵 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-monsters-nooma | 确认保留 | 59/64/136/False |
| <!-- local:monster:10143 -->10143 | 变异刺骨蜥 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 62/0/83/False |
| <!-- local:monster:10144 -->10144 | 变异迅猛蜥 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 60/0/82/False |
| <!-- local:monster:10145 -->10145 | 变异丑蜥 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 61/0/84/False |
| <!-- local:monster:10146 -->10146 | 变异毒蜥 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 64/14/85/False |
| <!-- local:monster:10147 -->10147 | 魔石咆哮者 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 65/31/86/False |
| <!-- local:monster:10148 -->10148 | 魔石狂热者 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 65/33/87/False |
| <!-- local:monster:10149 -->10149 | 变异利爪蜥 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 63/34/88/False |
| <!-- local:monster:10160 -->10160 | 地牢绿荫女神 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 52/47/113/False |
| <!-- local:monster:10222 -->10222 | 黑狼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 15/3/8/False |
| <!-- local:monster:10610 -->10610 | 红蛇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 15/0/278/False |
| <!-- local:monster:10611 -->10611 | 半兽剑士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 15/0/207/False |
| <!-- local:monster:10612 -->10612 | 半兽法师 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 15/0/208/False |
| <!-- local:monster:10614 -->10614 | 劳动蚂蚁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 25/0/248/False |
| <!-- local:monster:20001 -->20001 | 半兽勇士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 50/0/16/True |
| <!-- local:monster:20002 -->20002 | 巨型多角虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 52/0/73/True |
| <!-- local:monster:20003 -->20003 | 骷髅精灵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 54/0/23/True |
| <!-- local:monster:20004 -->20004 | 尸王 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 55/0/30/True |
| <!-- local:monster:20005 -->20005 | 蚂蚁将军 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 56/0/31/True |
| <!-- local:monster:20006 -->20006 | 红甲虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 56/0/39/True |
| <!-- local:monster:20007 -->20007 | 沃玛卫士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 60/0/54/True |
| <!-- local:monster:20008 -->20008 | 邪恶钳虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 62/0/46/True |
| <!-- local:monster:20009 -->20009 | 白野猪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 70/0/110/True |
| <!-- local:monster:20010 -->20010 | 骨鬼将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 70/0/101/True |
| <!-- local:monster:20011 -->20011 | 八脚首领 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 75/0/62/True |
| <!-- local:monster:20012 -->20012 | 僵尸鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 65/0/50/True |
| <!-- local:monster:20013 -->20013 | 吸血鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 65/0/50/True |
| <!-- local:monster:20014 -->20014 | 大法老 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 78/26/75/True |
| <!-- local:monster:20015 -->20015 | 神鬼王 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/0/60/True |
| <!-- local:monster:20016 -->20016 | 护法天 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/21/66/True |
| <!-- local:monster:20017 -->20017 | 潘夜鬼将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/0/91/True |
| <!-- local:monster:20018 -->20018 | 疯狂魔神盗 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/0/69/True |
| <!-- local:monster:20019 -->20019 | 黑度首将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 85/48/114/True |
| <!-- local:monster:20020 -->20020 | 霸王守卫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 90/60/130/True |
| <!-- local:monster:20021 -->20021 | 震天首将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 86/48/114/True |
| <!-- local:monster:20022 -->20022 | 诺玛突击队长 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 88/48/135/True |
| <!-- local:monster:20023 -->20023 | 魔石守护神 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 90/0/89/True |
| <!-- local:monster:30001 -->30001 | 沃玛教主 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 100/16/55/True |
| <!-- local:monster:30002 -->30002 | 骷髅教主 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 105/43/103/True |
| <!-- local:monster:30003 -->30003 | 触龙神 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 110/13/47/True |
| <!-- local:monster:30004 -->30004 | 超级黑野猪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 115/45/111/True |
| <!-- local:monster:30005 -->30005 | 赤月恶魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/19/63/True |
| <!-- local:monster:30006 -->30006 | 潘夜牛魔王 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 125/41/98/True |
| <!-- local:monster:30007 -->30007 | 祖玛教主 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 130/22/68/True |
| <!-- local:monster:30009 -->30009 | 霸王教主 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 180/61/131/True |
| <!-- local:monster:30010 -->30010 | 震天魔神 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 155/78/159/True |
| <!-- local:monster:30011 -->30011 | 地天灭王 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 190/0/90/True |
| <!-- local:monster:30012 -->30012 | 黑度魔神 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 150/78/159/True |
| <!-- local:monster:30016 -->30016 | 诺玛教主 | 诺玛教主 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-monsters-nooma | 确认保留 | 200/70/248/True |
| <!-- local:monster:40002 -->40002 | 卫士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 150/-1/1/False |
| <!-- local:monster:40005 -->40005 | 沙巴克城门1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 125/1000/274/False |
| <!-- local:monster:40006 -->40006 | 沙巴克城门2 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 150/1000/275/False |
| <!-- local:monster:40007 -->40007 | 沙巴克城门3 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 150/1000/276/False |
| <!-- local:monster:40008 -->40008 | 沙巴克城门4 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 150/1000/248/False |
| <!-- local:monster:40015 -->40015 | 镜像 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/55/0/False |
| <!-- local:monster:40017 -->40017 | 变异骷髅 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 17/52/117/False |
| <!-- local:monster:40018 -->40018 | 神兽 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 30/53/118/False |
| <!-- local:monster:40020 -->40020 | 超强骷髅 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 33/52/248/False |
| <!-- local:monster:40023 -->40023 | 炎魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 45/103/119/False |
| <!-- local:monster:40024 -->40024 | 替身木偶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/51/0/False |
| <!-- local:monster:40029 -->40029 | 苦力猪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/149/False |
| <!-- local:monster:40030 -->40030 | 刺客【I】宠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/150/False |
| <!-- local:monster:40031 -->40031 | 战士【I】宠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/151/False |
| <!-- local:monster:40032 -->40032 | 法师【II】宠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/153/False |
| <!-- local:monster:40033 -->40033 | 道士【II】宠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/152/False |
| <!-- local:monster:40034 -->40034 | 战士【II】宠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/156/False |
| <!-- local:monster:40035 -->40035 | 刺客【III】宠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/157/False |
| <!-- local:monster:40038 -->40038 | 刺客【II】宠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/158/False |
| <!-- local:monster:40039 -->40039 | 道馆卫士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/-1/248/False |
| <!-- local:monster:40040 -->40040 | 图书馆卫士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/-1/248/False |
| <!-- local:monster:40041 -->40041 | 沙漠战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/-1/248/False |
| <!-- local:monster:40042 -->40042 | 法师【I】宠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/154/False |
| <!-- local:monster:40043 -->40043 | 道士【I】宠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/155/False |
| <!-- local:monster:100001 -->100001 | 沙巴克领主 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/78/159/False |
| <!-- local:monster:100003 -->100003 | 昂克战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/-1/248/False |
| <!-- local:monster:100004 -->100004 | 僧侣僵尸0 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 20/10/26/False |
| <!-- local:monster:100005 -->100005 | 尸王0 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 55/0/30/True |
| <!-- local:monster:100006 -->100006 | 七点白蛇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 60/0/279/True |
| <!-- local:monster:100007 -->100007 | 千年毒蛇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 15/0/248/False |
| <!-- local:monster:100008 -->100008 | 超级沃玛教主1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 150/16/55/True |
| <!-- local:monster:100009 -->100009 | 超级骷髅教主1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 155/43/103/True |
| <!-- local:monster:100010 -->100010 | 超级触龙神1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 160/13/47/True |
| <!-- local:monster:100011 -->100011 | 超级黑猪王1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 165/45/111/True |
| <!-- local:monster:100012 -->100012 | 超级赤月恶魔1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 170/19/63/True |
| <!-- local:monster:100013 -->100013 | 超级潘夜牛魔王1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 175/41/98/True |
| <!-- local:monster:100014 -->100014 | 超级祖玛教主1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 180/22/68/True |
| <!-- local:monster:100015 -->100015 | 超级霸王教主1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 200/61/131/True |
| <!-- local:monster:100016 -->100016 | 超级震天魔神1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 190/78/159/True |
| <!-- local:monster:100017 -->100017 | 超级地天灭王1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 210/0/90/True |
| <!-- local:monster:100018 -->100018 | 超级黑度魔神1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 185/78/159/True |
| <!-- local:monster:100019 -->100019 | 超级诺玛教主1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 220/70/248/True |
| <!-- local:monster:100020 -->100020 | 半兽勇士11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 50/0/16/False |
| <!-- local:monster:100021 -->100021 | 半兽人11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 13/0/12/False |
| <!-- local:monster:100022 -->100022 | 半兽战士11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 13/0/12/False |
| <!-- local:monster:100023 -->100023 | 半兽剑士11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 15/0/248/False |
| <!-- local:monster:100024 -->100024 | 半兽法师11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 15/26/208/False |
| <!-- local:monster:100025 -->100025 | 骷髅精灵11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 54/0/23/True |
| <!-- local:monster:100026 -->100026 | 掷斧骷髅11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 18/7/21/False |
| <!-- local:monster:100027 -->100027 | 骷髅战士11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 18/0/20/False |
| <!-- local:monster:100028 -->100028 | 骷髅战将11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 18/0/22/False |
| <!-- local:monster:100029 -->100029 | 僵尸王 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 73/0/30/True |
| <!-- local:monster:100030 -->100030 | 雷电僵尸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 25/9/25/False |
| <!-- local:monster:100031 -->100031 | 署箭 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 73/0/30/True |
| <!-- local:monster:100032 -->100032 | 沃玛战士11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 25/0/52/False |
| <!-- local:monster:100033 -->100033 | 火焰沃玛11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 25/15/53/False |
| <!-- local:monster:100034 -->100034 | 沃玛勇士11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 25/0/248/False |
| <!-- local:monster:100035 -->100035 | 沃玛战将11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 25/0/248/False |
| <!-- local:monster:100036 -->100036 | 沃玛教主11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 100/16/55/True |
| <!-- local:monster:100037 -->100037 | 暗黑战士11 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 25/7/51/False |
| <!-- local:monster:100038 -->100038 | 牛老道 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 74/0/54/False |
| <!-- local:monster:100039 -->100039 | 冰魂弓箭手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 71/34/137/False |
| <!-- local:monster:100040 -->100040 | 魄冰女神 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 69/65/138/False |
| <!-- local:monster:100041 -->100041 | 冰魂鬼武士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 72/67/139/False |
| <!-- local:monster:100042 -->100042 | 冰魂鬼武将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 73/66/140/False |
| <!-- local:monster:100043 -->100043 | 幽灵骑士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 68/25/141/False |
| <!-- local:monster:100044 -->100044 | 冰魂鬼卒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 70/0/142/False |
| <!-- local:monster:100045 -->100045 | 狼人 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 67/68/143/False |
| <!-- local:monster:100046 -->100046 | 雪狼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 66/23/144/False |
| <!-- local:monster:100047 -->100047 | 冰魂卫士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 73/24/145/False |
| <!-- local:monster:100048 -->100048 | 野猪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 65/0/146/False |
| <!-- local:monster:100049 -->100049 | 赤龙石门 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 125/69/147/True |
| <!-- local:monster:100050 -->100050 | 火影 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/70/148/True |
| <!-- local:monster:100051 -->100051 | 冰湖白魔兽 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 140/104/174/False |
| <!-- local:monster:100052 -->100052 | 卫护将军 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 74/0/161/False |
| <!-- local:monster:100053 -->100053 | 剑客神徒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 79/71/183/False |
| <!-- local:monster:100054 -->100054 | 烈火神徒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 79/106/185/False |
| <!-- local:monster:100055 -->100055 | 法术神徒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 79/105/184/False |
| <!-- local:monster:100056 -->100056 | 火系士兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/107/175/False |
| <!-- local:monster:100057 -->100057 | 冰系士兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/108/176/False |
| <!-- local:monster:100058 -->100058 | 雷系士兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/109/177/False |
| <!-- local:monster:100059 -->100059 | 风系士兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/110/178/False |
| <!-- local:monster:100060 -->100060 | 玄武天王1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/112/180/True |
| <!-- local:monster:100061 -->100061 | 青龙天王1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/113/181/True |
| <!-- local:monster:100062 -->100062 | 朱雀天王1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/111/179/True |
| <!-- local:monster:100063 -->100063 | 白虎天王1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/114/182/True |
| <!-- local:monster:100064 -->100064 | 封印盒1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 100/4/188/True |
| <!-- local:monster:100065 -->100065 | 魔灵神主 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 280/115/186/True |
| <!-- local:monster:100066 -->100066 | 魔法师 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 150/116/187/False |
| <!-- local:monster:100067 -->100067 | 血灵石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/4/189/False |
| <!-- local:monster:100068 -->100068 | 生灵石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/4/189/False |
| <!-- local:monster:100069 -->100069 | 魔灵石 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/4/189/False |
| <!-- local:monster:100070 -->100070 | 蓝乃霸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100071 -->100071 | 红乃霸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100072 -->100072 | 熊九戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100073 -->100073 | 稻草人№破坏 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100074 -->100074 | 稻草人№自然 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100075 -->100075 | 稻草人№灵魂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100076 -->100076 | 稻草人№神圣 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100077 -->100077 | 稻草人№风 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100078 -->100078 | 稻草人№幻影 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100079 -->100079 | 稻草人№冰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100080 -->100080 | 稻草人№暗黑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100081 -->100081 | 稻草人№雷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100082 -->100082 | 稻草人№火 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100083 -->100083 | 小老虎 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100084 -->100084 | 修炼圆木桩 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/143/272/False |
| <!-- local:monster:100085 -->100085 | 红衣舞姬 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 75/94/162/False |
| <!-- local:monster:100086 -->100086 | 绿衣舞姬 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 75/95/163/False |
| <!-- local:monster:100087 -->100087 | 黎明女王 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/96/164/True |
| <!-- local:monster:100088 -->100088 | 雾影魔卒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 76/97/165/False |
| <!-- local:monster:100089 -->100089 | 阎昆魔女 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 76/98/166/False |
| <!-- local:monster:100090 -->100090 | 魔小将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 77/97/165/False |
| <!-- local:monster:100091 -->100091 | 魔大将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 78/64/167/False |
| <!-- local:monster:100092 -->100092 | 真幻鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 76/99/168/False |
| <!-- local:monster:100093 -->100093 | 真幻鬼婢 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 75/26/169/False |
| <!-- local:monster:100094 -->100094 | 雾影魔将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 77/64/167/False |
| <!-- local:monster:100095 -->100095 | 阎昆魔君 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 78/0/170/False |
| <!-- local:monster:100096 -->100096 | 东蚩尤将军1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/100/171/True |
| <!-- local:monster:100098 -->100098 | 赤龙女王 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 200/101/172/True |
| <!-- local:monster:100099 -->100099 | 赤龙魔王 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/102/173/True |
| <!-- local:monster:100100 -->100100 | 诺玛总魔将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/0/74/False |
| <!-- local:monster:100101 -->100101 | 诺玛装甲魔将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 82/64/136/False |
| <!-- local:monster:100102 -->100102 | 诺玛少将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 83/0/74/False |
| <!-- local:monster:100103 -->100103 | 诺玛法老召唤兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 81/26/75/False |
| <!-- local:monster:100104 -->100104 | 诺玛司令大法师 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 82/62/133/False |
| <!-- local:monster:100105 -->100105 | 单腿诺玛 | 单腿诺玛 | 确认保留 | exact | 与官方正式名称精确匹配；官方条目状态：confirmed-145 | official-145-monsters-nooma | 确认保留 | 80/0/248/False |
| <!-- local:monster:100106 -->100106 | 诺玛卫士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 81/0/76/False |
| <!-- local:monster:100107 -->100107 | 诺玛将土 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/0/76/False |
| <!-- local:monster:100108 -->100108 | 诺玛总将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/0/74/False |
| <!-- local:monster:100109 -->100109 | 诺玛法老召唤师 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/26/75/False |
| <!-- local:monster:100110 -->100110 | 诺玛抛石士兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 85/63/134/False |
| <!-- local:monster:100111 -->100111 | 阿龙怪1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 150/48/248/True |
| <!-- local:monster:100112 -->100112 | 诺玛巡逻队长 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 82/0/76/False |
| <!-- local:monster:100113 -->100113 | 诺玛阻力军 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 82/0/74/False |
| <!-- local:monster:100114 -->100114 | 诺玛阻力兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 82/0/74/False |
| <!-- local:monster:100115 -->100115 | 诺玛族男人 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/0/248/False |
| <!-- local:monster:100116 -->100116 | 诺玛城教主 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 260/70/248/True |
| <!-- local:monster:100117 -->100117 | 小黑龙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100118 -->100118 | 蘑菇头 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100119 -->100119 | 雪人 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100120 -->100120 | 小红猴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100121 -->100121 | 小白鸡 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100122 -->100122 | 小狐狸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100123 -->100123 | 大天使 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100124 -->100124 | 冥血魔王 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 220/134/248/True |
| <!-- local:monster:100125 -->100125 | 幽灵船长 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 270/85/248/True |
| <!-- local:monster:100126 -->100126 | 异界犬猴魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 88/0/122/False |
| <!-- local:monster:100127 -->100127 | 异界轻甲守卫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 88/0/123/False |
| <!-- local:monster:100128 -->100128 | 异界爆毒神魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 89/56/124/False |
| <!-- local:monster:100129 -->100129 | 异界神舰守卫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 92/0/125/False |
| <!-- local:monster:100130 -->100130 | 异界触角神魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 89/57/126/False |
| <!-- local:monster:100131 -->100131 | 异界恶形鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 90/0/127/False |
| <!-- local:monster:100132 -->100132 | 异界海神将领 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 90/58/128/False |
| <!-- local:monster:100133 -->100133 | 异界红衣法师 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 91/59/129/False |
| <!-- local:monster:100134 -->100134 | 霸王傀儡守卫1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 145/117/248/True |
| <!-- local:monster:100135 -->100135 | 黄骠马 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/0/0/False |
| <!-- local:monster:100136 -->100136 | 的卢 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/0/0/False |
| <!-- local:monster:100137 -->100137 | 绝影 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/0/0/False |
| <!-- local:monster:100138 -->100138 | 赤兔马 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/0/0/False |
| <!-- local:monster:100139 -->100139 | 西蚩尤将军1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/100/171/True |
| <!-- local:monster:100140 -->100140 | 飞翔的鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 260/117/248/True |
| <!-- local:monster:100142 -->100142 | 丛林小兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 83/0/48/False |
| <!-- local:monster:100143 -->100143 | 丛林小将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 84/117/123/False |
| <!-- local:monster:100144 -->100144 | 丛林武将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 85/72/125/False |
| <!-- local:monster:100145 -->100145 | 鬼蜮萨满1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 140/87/248/True |
| <!-- local:monster:100146 -->100146 | 白毛泼猴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 81/129/249/False |
| <!-- local:monster:100147 -->100147 | 铁甲牛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 82/129/255/False |
| <!-- local:monster:100148 -->100148 | 大角象 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 82/129/256/False |
| <!-- local:monster:100149 -->100149 | 冰魔1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 100/72/248/True |
| <!-- local:monster:100150 -->100150 | 幽蓝 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 65/42/233/False |
| <!-- local:monster:100151 -->100151 | 青灵兽1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 105/95/248/True |
| <!-- local:monster:100152 -->100152 | 神魔战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 65/72/248/False |
| <!-- local:monster:100153 -->100153 | 神魔道士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 65/130/248/False |
| <!-- local:monster:100154 -->100154 | 神魔法师 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 65/108/248/False |
| <!-- local:monster:100155 -->100155 | 神魔刺客 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 68/131/248/False |
| <!-- local:monster:100156 -->100156 | 砍不死 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 70/106/198/False |
| <!-- local:monster:100157 -->100157 | 秋风 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 71/105/245/False |
| <!-- local:monster:100158 -->100158 | 破茧成蝶 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 72/107/269/False |
| <!-- local:monster:100159 -->100159 | 烧死你 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 73/135/248/False |
| <!-- local:monster:100160 -->100160 | 浮云 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 74/113/248/False |
| <!-- local:monster:100161 -->100161 | 飞雪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 75/111/248/False |
| <!-- local:monster:100162 -->100162 | BoBo | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 76/114/248/False |
| <!-- local:monster:100163 -->100163 | 小兔兔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 65/108/248/False |
| <!-- local:monster:100164 -->100164 | 大鸡鸡 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 66/109/248/False |
| <!-- local:monster:100165 -->100165 | 熊二 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 68/110/248/False |
| <!-- local:monster:100166 -->100166 | 憋大招1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 200/115/248/True |
| <!-- local:monster:100167 -->100167 | 迎客松 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 60/4/10/False |
| <!-- local:monster:100168 -->100168 | 废材树 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 60/4/10/False |
| <!-- local:monster:100169 -->100169 | 桃源骑兵统领1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 150/135/261/True |
| <!-- local:monster:100170 -->100170 | 桃源步兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 95/134/262/False |
| <!-- local:monster:100171 -->100171 | 桃源红花妖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 95/129/263/False |
| <!-- local:monster:100172 -->100172 | 桃源青花妖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 95/132/264/False |
| <!-- local:monster:100173 -->100173 | 桃源战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 96/0/219/False |
| <!-- local:monster:100174 -->100174 | 桃源勇士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 97/0/220/False |
| <!-- local:monster:100175 -->100175 | 桃源精锐 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 98/0/223/False |
| <!-- local:monster:100176 -->100176 | 桃源红力士1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 155/0/248/True |
| <!-- local:monster:100177 -->100177 | 桃源青力士1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 155/0/248/True |
| <!-- local:monster:100178 -->100178 | 堕落火冥鸢 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 270/138/248/True |
| <!-- local:monster:100179 -->100179 | 火冥鸢 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 280/138/265/True |
| <!-- local:monster:100180 -->100180 | 桃源弓手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 100/89/221/False |
| <!-- local:monster:100181 -->100181 | 桃源蘑菇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 92/130/248/False |
| <!-- local:monster:100182 -->100182 | 桃源小绿球 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 93/131/248/False |
| <!-- local:monster:100183 -->100183 | 桃源花灵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 99/89/248/False |
| <!-- local:monster:100184 -->100184 | 桃源步兵1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 95/134/262/False |
| <!-- local:monster:100185 -->100185 | 桃源红花妖1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 95/129/263/False |
| <!-- local:monster:100186 -->100186 | 桃源青花妖1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 95/132/264/False |
| <!-- local:monster:100187 -->100187 | 肥羊1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 200/0/248/True |
| <!-- local:monster:100188 -->100188 | 法师【III】宠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100189 -->100189 | 道士【III】宠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100190 -->100190 | 战士【III】宠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 0/-2/248/False |
| <!-- local:monster:100192 -->100192 | 地狱炎魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 50/103/119/False |
| <!-- local:monster:100568 -->100568 | 副本-赤月恶魔1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 160/19/63/True |
| <!-- local:monster:100569 -->100569 | 副本-沃玛教主1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 160/16/55/True |
| <!-- local:monster:100570 -->100570 | 副本-霸王教主1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 170/61/131/True |
| <!-- local:monster:100571 -->100571 | 副本-震天魔神1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 165/78/159/True |
| <!-- local:monster:100572 -->100572 | 副本-地天灭王1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 170/0/90/True |
| <!-- local:monster:100573 -->100573 | 赤翼教主1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 200/117/248/True |
| <!-- local:monster:100574 -->100574 | 蓝翼教主1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 200/131/248/True |
| <!-- local:monster:100575 -->100575 | 玛珐之主1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 210/85/248/True |
| <!-- local:monster:100576 -->100576 | 辣手将军1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 165/0/248/True |
| <!-- local:monster:100577 -->100577 | 摧花将军1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 165/0/248/True |
| <!-- local:monster:100578 -->100578 | 伯光兄1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 170/0/248/True |
| <!-- local:monster:100579 -->100579 | 蓝色背刺 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 78/0/248/False |
| <!-- local:monster:100580 -->100580 | 反手一刀 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/89/248/False |
| <!-- local:monster:100581 -->100581 | 石岩射手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 78/0/248/False |
| <!-- local:monster:100582 -->100582 | 经验美羊羊 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 20/0/248/False |
| <!-- local:monster:100583 -->100583 | 经验小兔兔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 30/0/248/False |
| <!-- local:monster:100584 -->100584 | 经验大鸡鸡 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 40/0/248/False |
| <!-- local:monster:100585 -->100585 | 精灵猫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 70/89/248/False |
| <!-- local:monster:100586 -->100586 | 田园犬 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 70/117/248/False |
| <!-- local:monster:100587 -->100587 | 机灵鼠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 70/106/248/False |
| <!-- local:monster:100588 -->100588 | 奔波儿灞 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/131/248/False |
| <!-- local:monster:100589 -->100589 | 奔波儿灞1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/131/248/False |
| <!-- local:monster:100590 -->100590 | 奔波儿灞2 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/131/248/False |
| <!-- local:monster:100591 -->100591 | 灞波儿奔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/133/248/False |
| <!-- local:monster:100592 -->100592 | 灞波儿奔1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/133/248/False |
| <!-- local:monster:100593 -->100593 | 灞波儿奔2 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/133/248/False |
| <!-- local:monster:100594 -->100594 | 红月教主1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 220/89/248/True |
| <!-- local:monster:100595 -->100595 | 蓝月教主1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 220/90/248/True |
| <!-- local:monster:100596 -->100596 | 飞羽卫1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 160/98/248/True |
| <!-- local:monster:100597 -->100597 | 麋鹿1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 100/92/248/True |
| <!-- local:monster:100598 -->100598 | 钻风小队 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/89/248/False |
| <!-- local:monster:100599 -->100599 | 钻风小队2 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/89/248/False |
| <!-- local:monster:100600 -->100600 | 沙漠蜥蜴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 118/0/202/False |
| <!-- local:monster:100601 -->100601 | 沙鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 119/27/203/False |
| <!-- local:monster:100602 -->100602 | 水晶傀儡 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 150/0/215/False |
| <!-- local:monster:100603 -->100603 | 尘土恶魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 122/0/216/False |
| <!-- local:monster:100604 -->100604 | 双尾蝎子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 123/119/217/False |
| <!-- local:monster:100605 -->100605 | 嗜血鼹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/0/218/False |
| <!-- local:monster:100606 -->100606 | 沙尘怪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 121/0/216/False |
| <!-- local:monster:100607 -->100607 | 剧毒蝎子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 122/119/217/False |
| <!-- local:monster:100608 -->100608 | 迷失飞鹰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 124/0/248/False |
| <!-- local:monster:100609 -->100609 | 迷失沙鱼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 124/25/77/False |
| <!-- local:monster:100610 -->100610 | 迷失蜥蜴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 124/0/202/False |
| <!-- local:monster:100611 -->100611 | 异魔族-战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 110/0/219/False |
| <!-- local:monster:100612 -->100612 | 异魔族-兵卒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 111/0/220/False |
| <!-- local:monster:100613 -->100613 | 异魔族-弓手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 112/89/221/False |
| <!-- local:monster:100614 -->100614 | 异魔族-骤术师 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 113/7/222/False |
| <!-- local:monster:100615 -->100615 | 异魔族-百夫长 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 115/0/223/False |
| <!-- local:monster:100616 -->100616 | 沙海邪魔-阿索格1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 200/0/224/True |
| <!-- local:monster:100617 -->100617 | 沙漠怪兽-绿巨人1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 200/0/225/True |
| <!-- local:monster:100618 -->100618 | 独眼蜘蛛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 113/0/226/False |
| <!-- local:monster:100619 -->100619 | 天狼蜘蛛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 113/46/227/False |
| <!-- local:monster:100620 -->100620 | 异魔族族长-丘鲛洛1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 190/117/228/True |
| <!-- local:monster:100621 -->100621 | 海滨王-狂怒龙虾1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 205/120/229/True |
| <!-- local:monster:100622 -->100622 | 水晶金魔像 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 155/0/235/False |
| <!-- local:monster:100623 -->100623 | 水晶小玄武1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/18/239/True |
| <!-- local:monster:100624 -->100624 | 水晶魔法狂徒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 154/111/237/False |
| <!-- local:monster:100625 -->100625 | 水晶蠕虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 151/125/232/False |
| <!-- local:monster:100626 -->100626 | 水晶魔像 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 153/59/234/False |
| <!-- local:monster:100627 -->100627 | 水晶火虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 150/121/231/False |
| <!-- local:monster:100628 -->100628 | 水晶蝙蝠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 150/42/233/False |
| <!-- local:monster:100629 -->100629 | 腐朽幽灵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/7/280/False |
| <!-- local:monster:100630 -->100630 | 腐败幽灵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 121/7/248/False |
| <!-- local:monster:100631 -->100631 | 水晶长枪狂徒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 152/88/236/False |
| <!-- local:monster:100632 -->100632 | 水晶守护树 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 310/124/240/True |
| <!-- local:monster:100633 -->100633 | 水晶玄武 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 320/122/238/True |
| <!-- local:monster:100634 -->100634 | 水晶金刚兽1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 210/117/235/True |
| <!-- local:monster:100635 -->100635 | 钻地锁魂妖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 135/10/248/False |
| <!-- local:monster:100636 -->100636 | 云里雾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 133/119/210/False |
| <!-- local:monster:100637 -->100637 | 妖化血侍-铁罗1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 200/9/211/True |
| <!-- local:monster:100638 -->100638 | 雾里云 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 134/0/248/False |
| <!-- local:monster:100639 -->100639 | 黑羽教主-钺皇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 300/10/248/True |
| <!-- local:monster:100640 -->100640 | 魔化-道士1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 132/126/245/True |
| <!-- local:monster:100641 -->100641 | 魔气化形-魔道1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 200/117/246/True |
| <!-- local:monster:100642 -->100642 | 怨魂僵尸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 130/0/243/False |
| <!-- local:monster:100643 -->100643 | 血灵僵尸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 131/0/244/False |
| <!-- local:monster:100644 -->100644 | 魔气大僵尸-陆江 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 300/127/247/True |
| <!-- local:monster:100645 -->100645 | 僵尸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 129/0/242/False |
| <!-- local:monster:100646 -->100646 | 小僵尸 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 128/10/241/False |
| <!-- local:monster:100647 -->100647 | 古代坟墓-士兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 140/139/266/False |
| <!-- local:monster:100648 -->100648 | 古代坟墓-矛兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 141/139/267/False |
| <!-- local:monster:100649 -->100649 | 古墓士兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 142/139/266/False |
| <!-- local:monster:100650 -->100650 | 古墓矛兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 143/139/267/False |
| <!-- local:monster:100651 -->100651 | 古墓骑兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 144/140/268/False |
| <!-- local:monster:100652 -->100652 | 古墓长矛骑兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 147/140/269/False |
| <!-- local:monster:100653 -->100653 | 古墓守护士兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 145/139/266/False |
| <!-- local:monster:100654 -->100654 | 古墓守护矛兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 146/139/267/False |
| <!-- local:monster:100655 -->100655 | 古墓守护骑兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 150/140/268/False |
| <!-- local:monster:100656 -->100656 | 古墓守护长矛骑兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 151/140/269/False |
| <!-- local:monster:100657 -->100657 | 古墓护卫士兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 152/139/266/False |
| <!-- local:monster:100658 -->100658 | 古墓护卫武士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 153/139/267/False |
| <!-- local:monster:100659 -->100659 | 古墓土偶士兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 154/140/266/False |
| <!-- local:monster:100660 -->100660 | 古墓土偶护卫武士1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 220/141/270/True |
| <!-- local:monster:100661 -->100661 | 古墓主人 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 310/142/271/True |
| <!-- local:monster:100662 -->100662 | 巴山虎 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 130/0/248/False |
| <!-- local:monster:100663 -->100663 | 精细鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 131/0/248/False |
| <!-- local:monster:100664 -->100664 | 伶俐虫 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 132/0/248/False |
| <!-- local:monster:100665 -->100665 | 奔马岛-青龙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 230/0/248/True |
| <!-- local:monster:100666 -->100666 | 野生黄骠马 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 15/0/248/False |
| <!-- local:monster:100667 -->100667 | 野生绝影 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 40/0/248/False |
| <!-- local:monster:100668 -->100668 | 野生的卢 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 30/0/248/False |
| <!-- local:monster:100669 -->100669 | 野生赤兔马 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 50/0/248/False |
| <!-- local:monster:100670 -->100670 | 奔马岛-金灵兽 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 156/0/248/False |
| <!-- local:monster:100671 -->100671 | 奔马岛-青岩龙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 155/0/248/False |
| <!-- local:monster:100672 -->100672 | 海马骑兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 164/72/248/False |
| <!-- local:monster:100673 -->100673 | 海马术士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 163/108/248/False |
| <!-- local:monster:100674 -->100674 | 珊瑚石头怪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 161/49/248/False |
| <!-- local:monster:100675 -->100675 | 小八爪怪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 165/0/248/False |
| <!-- local:monster:100676 -->100676 | 巨大蛤利 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 160/0/248/False |
| <!-- local:monster:100677 -->100677 | 软甲亚纲 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 162/0/248/False |
| <!-- local:monster:100678 -->100678 | 巨大蛤利1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 160/0/248/False |
| <!-- local:monster:100679 -->100679 | 靑石刺鬼1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 240/0/248/True |
| <!-- local:monster:100680 -->100680 | 八腕魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 350/13/248/True |
| <!-- local:monster:100681 -->100681 | 八碗魔的腿 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 200/0/248/False |
| <!-- local:monster:100682 -->100682 | 蛮族-死魂怪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 125/27/203/False |
| <!-- local:monster:100683 -->100683 | 蛮族-石岩怪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 126/0/215/False |
| <!-- local:monster:100684 -->100684 | 蛮族-邪风 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 127/0/216/False |
| <!-- local:monster:100685 -->100685 | 蛮族-蝎子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 128/119/217/False |
| <!-- local:monster:100686 -->100686 | 蛮族-蜥蜴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 129/0/202/False |
| <!-- local:monster:100687 -->100687 | 沙漠甲蚁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 110/0/31/False |
| <!-- local:monster:100688 -->100688 | 沙漠兵蚁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 110/0/32/False |
| <!-- local:monster:100689 -->100689 | 沙漠治疗蚁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 110/12/33/False |
| <!-- local:monster:100690 -->100690 | 沙漠猎蚁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 110/7/34/False |
| <!-- local:monster:100691 -->100691 | 石岩怪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 125/0/215/False |
| <!-- local:monster:100692 -->100692 | 光炎石岩怪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 130/0/215/False |
| <!-- local:monster:100693 -->100693 | 是兄弟就来砍我一刀1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 10/0/248/True |
| <!-- local:monster:100694 -->100694 | 龙光路守护将军-眞昌 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 260/100/171/False |
| <!-- local:monster:100695 -->100695 | 龙光路守护将军-光穆 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 260/100/171/False |
| <!-- local:monster:100696 -->100696 | 囚禁的魔王 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 200/21/248/True |
| <!-- local:monster:100697 -->100697 | 眞炎剑魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 300/21/248/False |
| <!-- local:monster:100698 -->100698 | 炎狱金刚 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 320/21/248/False |
| <!-- local:monster:100699 -->100699 | 龙光路守护大将-帝释魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 320/21/248/False |
| <!-- local:monster:100700 -->100700 | 纯虎 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 38/0/190/False |
| <!-- local:monster:100701 -->100701 | 黄虎 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 39/0/191/False |
| <!-- local:monster:100702 -->100702 | 褐虎 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 37/6/192/False |
| <!-- local:monster:100703 -->100703 | 雪虎 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 42/68/193/False |
| <!-- local:monster:100704 -->100704 | 黑虎 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 40/0/194/False |
| <!-- local:monster:100705 -->100705 | 黑翼虎1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/0/195/True |
| <!-- local:monster:100706 -->100706 | 白翼虎1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/68/196/True |
| <!-- local:monster:100707 -->100707 | 虎将军1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 70/129/197/True |
| <!-- local:monster:100708 -->100708 | 虎战领主 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 160/104/174/True |
| <!-- local:monster:100709 -->100709 | 岛屿-巨象 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 35/0/71/False |
| <!-- local:monster:100710 -->100710 | 岛屿-猿猴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 34/23/199/False |
| <!-- local:monster:100711 -->100711 | 岛屿-魔神怪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 36/0/69/False |
| <!-- local:monster:100712 -->100712 | 霜冻雪人 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 43/0/200/False |
| <!-- local:monster:100713 -->100713 | 邪恶毒蛇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 45/0/201/False |
| <!-- local:monster:106061 -->106061 | 副本-花妖1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/129/263/True |
| <!-- local:monster:106062 -->106062 | 副本-花怪1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 82/132/264/True |
| <!-- local:monster:106063 -->106063 | 副本-猿猴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 50/23/199/False |
| <!-- local:monster:106064 -->106064 | 副本-魔神怪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 50/0/69/False |
| <!-- local:monster:106065 -->106065 | 副本-半兽勇士1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 50/0/16/True |
| <!-- local:monster:106066 -->106066 | 副本-半兽剑客 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 20/0/248/False |
| <!-- local:monster:106067 -->106067 | 副本-半兽巫师 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 22/26/208/False |
| <!-- local:monster:106068 -->106068 | 副本-骷髅首领1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 55/0/23/True |
| <!-- local:monster:106069 -->106069 | 副本-飞斧手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 23/7/21/False |
| <!-- local:monster:106070 -->106070 | 副本-骷髅战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 24/0/20/False |
| <!-- local:monster:106071 -->106071 | 副本-骷髅战将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 25/0/22/False |
| <!-- local:monster:106072 -->106072 | 副本-沃玛战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 26/0/52/False |
| <!-- local:monster:106073 -->106073 | 副本-火焰沃玛 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 27/15/53/False |
| <!-- local:monster:106074 -->106074 | 副本-沃玛勇士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 28/0/248/False |
| <!-- local:monster:106075 -->106075 | 副本-沃玛战将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 29/0/248/False |
| <!-- local:monster:106076 -->106076 | 副本-百花王1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 78/16/248/True |
| <!-- local:monster:106077 -->106077 | 副本-暗黑战士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 30/7/51/False |
| <!-- local:monster:106078 -->106078 | 黄铜武士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 67/79/94/False |
| <!-- local:monster:106079 -->106079 | 黑耀武士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 67/79/95/False |
| <!-- local:monster:106080 -->106080 | 金阳武将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 69/80/96/False |
| <!-- local:monster:106081 -->106081 | 银月武将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 69/81/97/False |
| <!-- local:monster:106082 -->106082 | 狂牛鬼将 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 68/82/54/False |
| <!-- local:monster:106083 -->106083 | 火灵牛鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 66/83/53/False |
| <!-- local:monster:106084 -->106084 | 灵牛鬼将军1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 100/84/55/True |
| <!-- local:monster:106085 -->106085 | 金牛大将军 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 240/85/98/True |
| <!-- local:monster:106086 -->106086 | 凶恶火灵牛鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 65/86/53/False |
| <!-- local:monster:106087 -->106087 | 超强骷髅弓箭手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 70/89/99/False |
| <!-- local:monster:106624 -->106624 | 逃难的黑翼虎 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 77/0/195/False |
| <!-- local:monster:106625 -->106625 | 逃难的白翼虎 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 78/68/196/False |
| <!-- local:monster:106626 -->106626 | 逃难的虎将军 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 76/129/197/False |
| <!-- local:monster:106627 -->106627 | 逃难的虎战领主1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 180/104/174/True |
| <!-- local:monster:106628 -->106628 | 难民弓箭手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 75/89/99/False |
| <!-- local:monster:106629 -->106629 | 精英弓箭手 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/89/99/False |
| <!-- local:monster:106630 -->106630 | 沉鱼1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/89/248/True |
| <!-- local:monster:106631 -->106631 | 落雁1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/66/248/True |
| <!-- local:monster:106632 -->106632 | 羞花1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/95/248/True |
| <!-- local:monster:106633 -->106633 | 闭月1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/92/248/True |
| <!-- local:monster:106634 -->106634 | 红拂1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/117/248/True |
| <!-- local:monster:106635 -->106635 | 破碎虚空小怪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/134/248/False |
| <!-- local:monster:106636 -->106636 | 破碎虚空小怪1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/135/248/False |
| <!-- local:monster:106637 -->106637 | 破碎虚空小怪2 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/134/248/False |
| <!-- local:monster:106638 -->106638 | 破碎虚空小怪3 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 80/135/248/False |
| <!-- local:monster:106639 -->106639 | 雪原怪兽 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 200/104/174/True |
| <!-- local:monster:106640 -->106640 | 黎明教主 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 260/96/248/True |
| <!-- local:monster:106641 -->106641 | 黎明铁粉1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 110/95/248/True |
| <!-- local:monster:106642 -->106642 | 囚禁的魔王1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 220/21/248/True |
| <!-- local:monster:106643 -->106643 | 囚禁的魔王2 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 250/21/248/True |
| <!-- local:monster:106644 -->106644 | 囚禁的魔王3 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 300/21/248/True |
| <!-- local:monster:106645 -->106645 | 黑风寨寨主 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 290/117/248/True |
| <!-- local:monster:106646 -->106646 | 黑风寨剑客 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 116/0/248/False |
| <!-- local:monster:106647 -->106647 | 黑风寨术士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 116/0/248/False |
| <!-- local:monster:106648 -->106648 | 黑风寨喽啰 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 115/79/248/False |
| <!-- local:monster:106649 -->106649 | 黑风寨头领1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 195/105/248/True |
| <!-- local:monster:106650 -->106650 | 沙漠铁火蚁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 110/0/248/False |
| <!-- local:monster:106651 -->106651 | 沙漠蚁后1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 190/78/248/True |
| <!-- local:monster:106652 -->106652 | 沙漠牛头怪 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 113/0/248/False |
| <!-- local:monster:106653 -->106653 | 沙漠蝮蛇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 112/0/248/False |
| <!-- local:monster:106654 -->106654 | 沙漠地鼠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 111/0/248/False |
| <!-- local:monster:106655 -->106655 | 沙漠黑蛇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 115/0/248/False |
| <!-- local:monster:106656 -->106656 | 泰山战狼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 100/0/248/False |
| <!-- local:monster:106657 -->106657 | 泰山强盗1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 102/0/248/False |
| <!-- local:monster:106658 -->106658 | 泰山强盗2 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 103/0/248/False |
| <!-- local:monster:106659 -->106659 | 补给品马车 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 105/0/248/False |
| <!-- local:monster:106660 -->106660 | 泰山强盗3 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 104/79/248/False |
| <!-- local:monster:106661 -->106661 | 泰泰大王1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 180/117/248/True |
| <!-- local:monster:106662 -->106662 | 荒野首领1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 185/45/248/True |
| <!-- local:monster:106663 -->106663 | 白狼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 107/129/251/False |
| <!-- local:monster:106664 -->106664 | 赤狼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 108/129/252/False |
| <!-- local:monster:106665 -->106665 | 丛林白虎 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 109/129/253/False |
| <!-- local:monster:106666 -->106666 | 丛林黑虎 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 110/129/254/False |
| <!-- local:monster:106667 -->106667 | 荒野斩决鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 114/131/257/False |
| <!-- local:monster:106668 -->106668 | 荒野影软鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 114/131/258/False |
| <!-- local:monster:106669 -->106669 | 荒野盲鬼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 115/132/260/False |
| <!-- local:monster:106670 -->106670 | 蛮族首领1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 185/45/248/True |
| <!-- local:monster:106671 -->106671 | 黑风寨宝箱 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 100/4/248/False |
| <!-- local:monster:106672 -->106672 | 黑风寨精锐 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 118/72/248/False |
| <!-- local:monster:106673 -->106673 | 黑风寨精锐 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 119/67/248/False |
| <!-- local:monster:106674 -->106674 | 黑风寨精锐 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 120/66/248/False |
| <!-- local:monster:106675 -->106675 | 远古凶兽-吞天蟒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 300/117/248/True |
| <!-- local:monster:106676 -->106676 | 流窜山贼 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 125/0/248/False |
| <!-- local:monster:106677 -->106677 | 流窜溃兵 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 125/0/248/False |
| <!-- local:monster:106678 -->106678 | 奔马岛-独角马 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 157/0/248/False |
| <!-- local:monster:106679 -->106679 | 奔马岛-白毛狮王 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 158/0/248/False |
| <!-- local:monster:106680 -->106680 | 奔马岛-金毛狮王 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 158/0/248/False |
| <!-- local:monster:106681 -->106681 | 奔马岛-白玉麒麟 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 160/0/248/False |
| <!-- local:monster:106682 -->106682 | 鬼灵藤妖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 124/279/248/False |
| <!-- local:monster:106683 -->106683 | 鬼灵恶犬 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 125/0/248/False |
| <!-- local:monster:106684 -->106684 | 鬼灵恐怖撕裂 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 126/31/248/False |
| <!-- local:monster:106685 -->106685 | 鬼灵断骨獠牙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 127/31/248/False |
| <!-- local:monster:106686 -->106686 | 幽灵蝙蝠 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 124/95/248/False |
| <!-- local:monster:106687 -->106687 | 镇灵将军 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 260/117/248/True |
| <!-- local:monster:119757 -->119757 | 封印盒1 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 100/4/188/True |

## 官方套装表

| 正式名 | 别名 | 类别/区域/组成 | 状态 | 引入版本 | 来源ID | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| 诺马勇士套装 |  | 诺马勇气, 诺马智慧手镯, 诺马正义手镯, 诺马防御手套, 诺马魔法手套 | uncertain-version | — | s17173-kr-20040316-update-plan | 组成在韩服 3 月 16 日更新计划正文中逐项列出；该来源没有证明光通中国 1.45 部署，不能作为确认或删除依据。 |
| 金刚套装 |  | 金刚铃铛, 金刚防御手镯, 金刚魔法手镯, 金刚魔法戒指, 金刚精神戒指 | uncertain-version | — | s17173-kr-20040316-update-plan | 组成在韩服 3 月 16 日更新计划正文中逐项列出；该来源没有证明光通中国 1.45 部署，不能作为确认或删除依据。 |
| 祈祷套装 |  | 祈祷之刃, 祈祷头盔, 祈祷项链, 祈祷手镯, 祈祷戒指 | uncertain-version | — | s17173-kr-20040316-update-plan | 组成在韩服 3 月 16 日更新计划正文中逐项列出；该来源没有证明光通中国 1.45 部署，不能作为确认或删除依据。 |
| 魔血套装 |  | 魔血戒指, 魔血手镯, 魔血项链 | uncertain-version | — | s17173-20030820-moxue-set | 2003 同期正文逐项列出三件组成，但早于 1.45 且未证明持续适用；不能作为确认或删除依据。 |

## 本服套装对比表

| 快照索引 | 数据库原名 | 官方1.45名称 | 匹配状态 | 匹配方式 | 判断依据 | 证据来源 | 处理建议 | 数据库组成 | 官方组成 | 差异/缺失部件 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <!-- local:set:78 -->78 | 魔血 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 魔血\(3\): 魔血项链, 魔血手镯, 魔血戒指 | - | 无官方对照 |
| <!-- local:set:79 -->79 | 虹魔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 虹魔\(3\): 虹魔项链, 虹魔手镯, 虹魔戒指 | - | 无官方对照 |
| <!-- local:set:80 -->80 | 记忆 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 记忆\(4\): 记忆头盔, 记忆手镯, 记忆项链, 记忆戒指 | - | 无官方对照 |
| <!-- local:set:81 -->81 | 金刚 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 金刚\(5\): 金刚魔法手镯, 金刚防御手镯, 金刚精神戒指, 金刚魔法指环, 金刚铃铛 | - | 无官方对照 |
| <!-- local:set:82 -->82 | 诺玛勇士 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 诺玛\(5\): 正义之物, 智慧之物, 决断之物, 节制之物, 神勇之物 | - | 无官方对照 |
| <!-- local:set:83 -->83 | 祈祷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 祈祷\(5\): 祈祷头盔, 祈祷戒指, 祈祷项链, 祈祷手镯, 祈祷之刃 | - | 无官方对照 |
| <!-- local:set:87 -->87 | 英雄手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 英雄手套 | - | 无官方对照 |
| <!-- local:set:88 -->88 | 紫金环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 紫金环 | - | 无官方对照 |
| <!-- local:set:89 -->89 | 六棱戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 六棱戒 | - | 无官方对照 |
| <!-- local:set:90 -->90 | 武圣之戒 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 武圣之戒 | - | 无官方对照 |
| <!-- local:set:91 -->91 | 毁灭魔链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 毁灭魔链 | - | 无官方对照 |
| <!-- local:set:95 -->95 | 黑铁头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 黑铁头盔 | - | 无官方对照 |
| <!-- local:set:96 -->96 | 霸龙头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 霸龙头盔 | - | 无官方对照 |
| <!-- local:set:97 -->97 | 战神头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 战神头盔 | - | 无官方对照 |
| <!-- local:set:98 -->98 | 武神之靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 武神之靴 | - | 无官方对照 |
| <!-- local:set:99 -->99 | 屠龙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 屠龙 | - | 无官方对照 |
| <!-- local:set:100 -->100 | 霹雷 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 霹雷 | - | 无官方对照 |
| <!-- local:set:101 -->101 | 破山剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 破山剑 | - | 无官方对照 |
| <!-- local:set:102 -->102 | 铁轮 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 铁轮 | - | 无官方对照 |
| <!-- local:set:104 -->104 | 嗜魂法杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 嗜魂法杖 | - | 无官方对照 |
| <!-- local:set:105 -->105 | 逍遥扇 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 逍遥扇 | - | 无官方对照 |
| <!-- local:set:106 -->106 | 龙纹剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 龙纹剑 | - | 无官方对照 |
| <!-- local:set:109 -->109 | 心魔戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 心魔戒指 | - | 无官方对照 |
| <!-- local:set:110 -->110 | 虚空道环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 虚空道环 | - | 无官方对照 |
| <!-- local:set:111 -->111 | 虎面头盔 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 虎面头盔 | - | 无官方对照 |
| <!-- local:set:112 -->112 | 仙云靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 仙云靴 | - | 无官方对照 |
| <!-- local:set:113 -->113 | 无影靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 无影靴 | - | 无官方对照 |
| <!-- local:set:114 -->114 | 铁炼腕 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 铁炼腕 | - | 无官方对照 |
| <!-- local:set:115 -->115 | 气血项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 气血项链 | - | 无官方对照 |
| <!-- local:set:116 -->116 | 破坏项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 破坏项链 | - | 无官方对照 |
| <!-- local:set:117 -->117 | 昏暗封印 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 昏暗风印 | - | 无官方对照 |
| <!-- local:set:118 -->118 | 怨恨项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 怨恨项链 | - | 无官方对照 |
| <!-- local:set:119 -->119 | 七彩金环 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 七彩金环 | - | 无官方对照 |
| <!-- local:set:120 -->120 | 天机戒指 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 天机戒指 | - | 无官方对照 |
| <!-- local:set:121 -->121 | 流星项链 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 流星项链 | - | 无官方对照 |
| <!-- local:set:122 -->122 | 五行神镜 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 五行神镜 | - | 无官方对照 |
| <!-- local:set:123 -->123 | 乾坤一气 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 乾坤一气 | - | 无官方对照 |
| <!-- local:set:124 -->124 | 泰轮拂尘 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 泰轮拂尘 | - | 无官方对照 |
| <!-- local:set:125 -->125 | 天神法杖 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 天神法杖 | - | 无官方对照 |
| <!-- local:set:133 -->133 | 黑皮靴子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 黑皮靴子 | - | 无官方对照 |
| <!-- local:set:134 -->134 | 月光靴 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 月光鞋 | - | 无官方对照 |
| <!-- local:set:136 -->136 | 狂风 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 狂风\(2\): 狂风项链, 狂风戒指 | - | 无官方对照 |
| <!-- local:set:137 -->137 | 行者帽 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 行者帽 | - | 无官方对照 |
| <!-- local:set:145 -->145 | 护身烟雨 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 护身宝甲（男）, 护身宝甲（女）, 烟雨宝铠（女）, 烟雨宝铠（男） | - | 无官方对照 |
| <!-- local:set:146 -->146 | 天赐罗刹 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 天赐战甲（女）, 天赐战甲（男）, 罗刹护甲（男）, 罗刹护甲（女） | - | 无官方对照 |
| <!-- local:set:147 -->147 | 绝世潜龙 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 绝世战甲（女）, 绝世战甲（男）, 潜龙遁甲（男）, 潜龙遁甲（女） | - | 无官方对照 |
| <!-- local:set:162 -->162 | 沐水神兵（3转武器） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 龙雀开山钺, 奕天破邪杖, 秋水无痕剑, 碎情雾影环 | - | 无官方对照 |
| <!-- local:set:163 -->163 | 龙血之力 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(6\): 龙血戒指, 龙血手镯, 龙血项链, 龙血头盔 | - | 无官方对照 |
| <!-- local:set:165 -->165 | 影魅的呼唤 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 影魅之刃 | - | 无官方对照 |
| <!-- local:set:214 -->214 | 阎罗手套 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 阎罗手套 | - | 无官方对照 |
| <!-- local:set:225 -->225 | 黑暗之盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 盾牌\(1\): 火罐 | - | 无官方对照 |
| <!-- local:set:226 -->226 | 法术护盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 盾牌\(1\): 火桶 | - | 无官方对照 |
| <!-- local:set:227 -->227 | 风之障壁 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 盾牌\(1\): 木盾 | - | 无官方对照 |
| <!-- local:set:228 -->228 | 坚不可摧 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 盾牌\(1\): 铁盾 | - | 无官方对照 |
| <!-- local:set:229 -->229 | 坚定风采 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 盾牌\(1\): 精钢盾 | - | 无官方对照 |
| <!-- local:set:230 -->230 | 金刚之躯 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 盾牌\(1\): 寒铁晶盾 | - | 无官方对照 |
| <!-- local:set:231 -->231 | 缥缈套装 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 缥缈\(3\): 缥缈戒指, 缥缈项链, 缥缈手镯 | - | 无官方对照 |
| <!-- local:set:233 -->233 | 龙血深渊 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 司马血甲（男）, 司马血甲（女）, 邪魔炎甲（男）, 邪魔炎甲（女）, 邪魔墨甲（男）, 邪魔墨甲（女） | - | 无官方对照 |
| <!-- local:set:234 -->234 | 泣血之刃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 赤血宝剑 | - | 无官方对照 |
| <!-- local:set:235 -->235 | 神魔套装（1转首饰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 虎影戒, 永柳戒, 咒恶戒, 神魔手镯, 神魔项链, 修罗戒 | - | 无官方对照 |
| <!-- local:set:236 -->236 | 飞龙剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 飞龙剑 | - | 无官方对照 |
| <!-- local:set:237 -->237 | 飞龙剑（元素） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 飞龙剑（元素） | - | 无官方对照 |
| <!-- local:set:238 -->238 | 桃源之盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 盾牌\(1\): 翠虎飞龙 | - | 无官方对照 |
| <!-- local:set:239 -->239 | 桃源神兵（2转武器） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 桃源虎翼刀, 桃源曜灵杖, 桃源三焰扇, 桃源斩轮 | - | 无官方对照 |
| <!-- local:set:240 -->240 | 桃夭套装（2转首饰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 桃之夭夭, 桃之灼灼, 桃源之心, 桃之蓁蓁 | - | 无官方对照 |
| <!-- local:set:242 -->242 | 玄武神盾 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 盾牌\(1\): 玄武盾 | - | 无官方对照 |
| <!-- local:set:243 -->243 | 龙盾之力 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | 盾牌\(1\): 龙盾 | - | 无官方对照 |
| <!-- local:set:244 -->244 | 复仇者面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 复仇者面具 | - | 无官方对照 |
| <!-- local:set:245 -->245 | 猎鹰面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 猎鹰面具 | - | 无官方对照 |
| <!-- local:set:246 -->246 | 黑乌鸦面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 黑乌鸦面具 | - | 无官方对照 |
| <!-- local:set:247 -->247 | 先知面具 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 先知面具 | - | 无官方对照 |
| <!-- local:set:248 -->248 | 天掌靴子 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 天掌靴子 | - | 无官方对照 |
| <!-- local:set:249 -->249 | 初窥门径 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 幽灵手套, 思贝儿手镯, 生命项链, 天珠项链, 铂金戒指, 红宝石戒指, 幽灵项链, 红叶血环, 龙之戒指, 三眼手镯 | - | 无官方对照 |
| <!-- local:set:250 -->250 | 已有小成 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 骑士手镯, 绿色项链, 恶魔铃铛, 龙之手镯, 力量戒指, 心灵手镯, 紫碧螺, 泰坦戒指, 灵魂项链 | - | 无官方对照 |
| <!-- local:set:251 -->251 | 渐入佳境 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 雷神戒指, 毁灭手镯, 神谕项链, 润神戒指, 如来手镯, 猫眼, 复血, 帝王戒指, 武士手镯, 火玉手镯 | - | 无官方对照 |
| <!-- local:set:252 -->252 | 出类拔萃 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 魔灵戒指, 石榴戒指, 青摇戒指, 莲丸戒指, 铁系项链, 追魂项链, 追风项链, 魔令项链, 魔令手镯 | - | 无官方对照 |
| <!-- local:set:253 -->253 | 非同凡响 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 师承戒指, 龙马戒指, 青云戒指, 破荒项链, 魔云项链, 定心项链, 金棱手镯, 思过手镯, 世尊手镯, 影刺雷戒 | - | 无官方对照 |
| <!-- local:set:254 -->254 | 炉火纯青 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 旭日戒指, 霸王项链, 登天手镯, 三桓戒指, 避难项链, 云龙手镯, 继承戒指, 昆仑项链, 至善手镯 | - | 无官方对照 |
| <!-- local:set:255 -->255 | 臻至化境 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 三台项链, 三台手镯, 三台戒指, 天丛项链, 天丛戒指, 天丛手镯, 转轮项链, 转轮手镯, 转轮戒指 | - | 无官方对照 |
| <!-- local:set:256 -->256 | 超凡脱俗 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 杀魔血刀戒指, 师玉戒指, 九梦戒指, 杀魔血刀手镯, 师玉手镯, 九梦手镯, 杀魔血刀项链, 师玉项链, 九梦项链 | - | 无官方对照 |
| <!-- local:set:257 -->257 | 登峰造极 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 日月戒指, 日月手镯, 日月项链, 天辉戒指, 天辉项链, 天辉手镯, 消魂戒指, 消魂手镯, 消魂项链 | - | 无官方对照 |
| <!-- local:set:258 -->258 | 返璞归真 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 玄灵天链, 玄灵魔链, 玄灵天环, 玄灵魔环, 玄灵天戒, 玄灵魔戒, 玄灵之月龙项链, 玄灵之紫月项链, 玄灵之月龙手镯, 玄灵之紫月手镯, 玄灵之月龙戒指, 玄灵之紫月戒指 | - | 无官方对照 |
| <!-- local:set:259 -->259 | 虎啸龙吟（5转首饰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 虎啸项链, 虎啸手镯, 虎啸戒指, 龙吟项链, 龙吟手镯, 龙吟戒指 | - | 无官方对照 |
| <!-- local:set:262 -->262 | 神魔之刃（1转武器） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 生死轮, 阴阳刀, 拐杖, 天狼刀 | - | 无官方对照 |
| <!-- local:set:263 -->263 | 神兵利刃（5转武器） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 慧明之杖, 天赋神剑, 万古道兵, 神魂湮灭剑 | - | 无官方对照 |
| <!-- local:set:264 -->264 | 霸龙头盔（祝福） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 祝福霸龙头盔 | - | 无官方对照 |
| <!-- local:set:265 -->265 | 死神双剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 死神双剑 | - | 无官方对照 |
| <!-- local:set:266 -->266 | 天命 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 天命 | - | 无官方对照 |
| <!-- local:set:267 -->267 | 锋翼剑 | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 锋翼剑 | - | 无官方对照 |
| <!-- local:set:268 -->268 | 沐水仙踪（3转首饰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 沐水璃殇佩, 沐水手镯, 沐水霜晓戒, 沐水灭魂戒 | - | 无官方对照 |
| <!-- local:set:269 -->269 | 玄云沙海（4转首饰） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 鹰扬醉舞戒, 蝶恋清寒链, 玄云碎魄镯, 清寒浅浪戒 | - | 无官方对照 |
| <!-- local:set:270 -->270 | 神魔铠甲（1转盔甲） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 赤龙神甲（男）, 赤龙神甲（女）, 赤龙头盔, 龙血鞋, 修罗战甲（男）, 修罗战甲（女） | - | 无官方对照 |
| <!-- local:set:271 -->271 | 桃源神铠（2转盔甲） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 黑玉战甲（女）, 黑玉战甲（男）, 桃源靴, 桃源盔, 桃源仙甲（女）, 桃源仙甲（男） | - | 无官方对照 |
| <!-- local:set:272 -->272 | 沐水神铠（3转盔甲） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 沐水天靴, 沐水天冠, 幻世魔衣（男）, 幻世魔衣（女）, 沐水天衣（男）, 沐水天衣（女） | - | 无官方对照 |
| <!-- local:set:273 -->273 | 玄云神铠（4转盔甲） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 玄云靴, 玄云盔, 凶陌圣甲（男）, 凶陌圣甲（女）, 玄云鸾暮铠（男）, 玄云鸾暮铠（女） | - | 无官方对照 |
| <!-- local:set:274 -->274 | 虎啸龙吟神铠（5转盔甲） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(3\): 幻陌靴, 圣火盔, 战-幻殇碧陌铠（男）, 战-幻殇碧陌铠（女）, 刺客-银月泣影甲（男）, 刺客-银月泣影甲（女）, 道-幻殇碧陌铠（男）, 道-幻殇碧陌铠（女）, 法-幻殇碧陌铠（男）, 法-幻殇碧陌铠（女）, 幻陌盔 | - | 无官方对照 |
| <!-- local:set:275 -->275 | 玄海神兵（4转武器） | - | 版本不确定 | unmatched | 未在官方正式名称或显式别名中找到精确匹配 | - | 版本不确定 | \(1\): 熔金落日刀, 龙破沧溟, 天雷真火扇, 天星耀阳环 | - | 无官方对照 |

## 建议删除候选

| 类型 | 快照索引 | 数据库原名 | 官方名称 | 判断依据 |
| --- | ---: | --- | --- | --- |

当前没有满足严格证据条件的建议删除候选。

## 版本不确定项

| 类型 | 快照索引 | 数据库原名 | 官方名称 | 判断依据 |
| --- | ---: | --- | --- | --- |
| 物品 | 1 | 金币 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2 | 金创药（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3 | 魔法药（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4 | 鹿肉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5 | 布衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6 | 布衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7 | 木剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8 | 铁剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 9 | 青铜剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 10 | 轻型盔甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 11 | 轻型盔甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 12 | 干肉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 13 | 包子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 14 | 凝霜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 15 | 火球术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16 | 治愈术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 17 | 基本剑术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18 | 蜡烛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 19 | 短剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 20 | 精神力战法 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 21 | 青铜斧 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 22 | 重盔甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 23 | 魔法长袍（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 24 | 灵魂战衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 25 | 重盔甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 26 | 魔法长袍（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 27 | 灵魂战衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 28 | 大火球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 29 | 攻杀剑术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 30 | 施毒术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 31 | 匕首 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 32 | 井中月 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 33 | 银蛇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 34 | 海魂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 35 | 修罗 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 36 | 炼狱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 37 | 凌风 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 38 | 破魂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 39 | 斩马刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 40 | 食人花树叶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 41 | 毒蜘蛛牙齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 42 | 食人花果实 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 43 | 蝎子的尾巴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 44 | 蛆卵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 45 | 灰色药粉（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 46 | 黄色药粉（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 47 | 古铜戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 48 | 青铜头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 49 | 金项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 50 | 铁手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 51 | 灰色药粉（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 52 | 灰色药粉（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 53 | 黄色药粉（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 54 | 黄色药粉（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 55 | 乌木剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 56 | 魔杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 57 | 八荒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 58 | 鸡肉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 59 | 水晶魔戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 60 | 牛角戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 61 | 蓝色水晶戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 62 | 六绝星环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 63 | 黑檀项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 64 | 黄色水晶项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 65 | 黑色水晶项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 66 | 魔法头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 67 | 沃玛号角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 68 | 半月 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 69 | 皮制手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 70 | 坚固手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 71 | 钢手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 72 | 玄铁指环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 73 | 金戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 74 | 灯笼项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 75 | 白色虎齿项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 76 | 魅力戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 77 | 道德戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 78 | 白金项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 79 | 降妖除魔戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80 | 躲避手链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 81 | 地牢逃脱卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 82 | 偃月 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 83 | 降魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 84 | 传统项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 85 | 小手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 86 | 银手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 87 | 大手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 88 | 鹤嘴锄 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 89 | 隐身戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 90 | 抗拒火环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91 | 地狱火 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 92 | 雷电术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 93 | 疾光电影 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 94 | 灵魂火符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95 | 幽灵盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 96 | 神圣战甲术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 97 | 金创药（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 98 | 魔法药（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 99 | 黑色水晶戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 100 | 魔鬼项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 101 | 珊瑚戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 102 | 蓝翡翠项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 103 | 蛇眼戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 104 | 琥珀项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 105 | 护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 106 | 刺杀剑术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 107 | 放大镜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 108 | 红宝石戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 109 | 珍珠戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 110 | 竹笛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 111 | 铂金戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 112 | 骷髅戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 113 | 龙之戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 114 | 死神手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 115 | 骷髅头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 116 | 魔法手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 117 | 金手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 118 | 道士头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 119 | 传送戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 120 | 尽力手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 121 | 骑士手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 122 | 绿色项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 123 | 凤凰明珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 124 | 道士手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 125 | 三眼手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 126 | 灵魂项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 127 | 黑檀手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 128 | 思贝儿手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 129 | 恶魔铃铛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 130 | 铜矿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 131 | 铁矿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 132 | 银矿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 133 | 金矿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 134 | 战神油 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 135 | 回城卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 137 | 麻痹戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 138 | 复活戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 139 | 火焰戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 140 | 防御戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 142 | 护身戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 143 | 神力戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 144 | 技巧项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 145 | 狂风戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 146 | 夏普儿手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 147 | 狂风项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 148 | 辟邪手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 149 | 探测项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 150 | 困魔咒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 151 | 召唤骷髅 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 152 | 隐身术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 153 | 集体隐身术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 154 | 诱惑之光 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 155 | 瞬息移动 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 156 | 火墙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 157 | 爆裂火焰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 158 | 地狱雷光 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 159 | 半月弯刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 160 | 愤怒之钟（雷） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 161 | 愤怒之钟（风） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 162 | 太阳水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 163 | 祖玛头像 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 164 | 兑换卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 165 | 随机传送卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 166 | 无极棍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 167 | 血饮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 168 | 裁决之杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 169 | 记忆戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 170 | 记忆项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 171 | 记忆手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 172 | 记忆头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 173 | 祈祷之刃 | 祈祷之刃 | 与官方正式名称精确匹配；官方条目状态：uncertain-version |
| 物品 | 174 | 祈祷手镯 | 祈祷手镯 | 与官方正式名称精确匹配；官方条目状态：uncertain-version |
| 物品 | 175 | 祈祷项链 | 祈祷项链 | 与官方正式名称精确匹配；官方条目状态：uncertain-version |
| 物品 | 176 | 祈祷戒指 | 祈祷戒指 | 与官方正式名称精确匹配；官方条目状态：uncertain-version |
| 物品 | 177 | 祈祷头盔 | 祈祷头盔 | 与官方正式名称精确匹配；官方条目状态：uncertain-version |
| 物品 | 178 | 行会回城卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 179 | 修复油 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 180 | 金创药（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 181 | 魔法药（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 182 | 生命项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 183 | 力量戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 184 | 心灵手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 185 | 黑铁头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 186 | 烈火剑法 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 187 | 野蛮冲撞 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 188 | 心灵启示 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 189 | 群体治愈术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 190 | 召唤神兽 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 191 | 魔法盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 192 | 圣言术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 193 | 冰咆哮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 194 | 金创药（大）包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 195 | 魔法药（大）包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 196 | 强效太阳水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 197 | 骰子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 198 | 木料 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 199 | 黑铁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 200 | 彩票 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 201 | 祝福道士头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 205 | 命运之刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 206 | 屠龙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 207 | 骨玉权杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 208 | 龙纹剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 209 | 嗜魂法杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 210 | 火把 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 212 | 鹿茸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 213 | 命运之书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 214 | 紫碧螺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 215 | 泰坦戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 216 | 幽灵手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 217 | 阎罗手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 218 | 龙之手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 219 | 天珠项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 220 | 幽灵项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 221 | 米糕 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 222 | 金条 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 223 | 鹿血 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 224 | 神秘戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 225 | 神秘腰带 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 226 | 神秘头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 227 | 神水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 228 | 蓝包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 229 | 红包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 230 | 绿包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 231 | 人参 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 232 | 馒头 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 233 | 莲花宝镜（暗黑） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 234 | 莲花宝镜（幻影） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 235 | 五色项链（火） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 236 | 五色项链（冰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 237 | 五色项链（雷） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 238 | 五色项链（风） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 239 | 介绍信 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 240 | 红苹果 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 241 | 筹码 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 242 | 特殊药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 243 | 万年雪霜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 244 | 金创药（小）包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 245 | 魔法药（小）包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 246 | 金创药（中）包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 247 | 魔法药（中）包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 248 | 地牢逃脱卷包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 249 | 随机传送卷包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 250 | 回城卷包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 251 | 行会回城卷包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 252 | 筹码包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 253 | 参加活动卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 254 | 水饺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 255 | 攻击神水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 256 | 自然神水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 257 | 灵魂神水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 258 | 疾风神水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 259 | 体力强效神水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 260 | 魔力强效神水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 261 | 金条包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 262 | 金盒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 263 | 攻击神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 264 | 自然神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 265 | 灵魂神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 266 | 疾风神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 267 | 体力强效神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 268 | 魔力强效神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 269 | 攻击神水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 270 | 自然神水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 271 | 灵魂神水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 272 | 体力强效神水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 273 | 魔力强效神水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 274 | 攻击神水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 275 | 自然神水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 276 | 灵魂神水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 277 | 体力强效神水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 278 | 魔力强效神水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 279 | 疾风神水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 280 | 疾风神水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 281 | 青苹果 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 282 | 赤血宝剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 283 | 魔血戒指 | 魔血戒指 | 与官方正式名称精确匹配；官方条目状态：uncertain-version |
| 物品 | 284 | 魔血手镯 | 魔血手镯 | 与官方正式名称精确匹配；官方条目状态：uncertain-version |
| 物品 | 285 | 魔血项链 | 魔血项链 | 与官方正式名称精确匹配；官方条目状态：uncertain-version |
| 物品 | 286 | 虹魔戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 287 | 虹魔手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 288 | 虹魔项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 289 | 血剑碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 290 | 鉴定石一级 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 291 | 鉴定石二级 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 292 | 鉴定石三级 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 293 | 鉴定石四级 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 294 | 鉴定石五级 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 296 | 玉水晶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 297 | 血魔心脏 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 298 | 魔血油 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 299 | 生死宝刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 300 | 战神盔甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 301 | 战神盔甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 302 | 恶魔长袍（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 303 | 恶魔长袍（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 304 | 幽灵战衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 305 | 幽灵战衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 306 | 无名刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 307 | 袖里剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 308 | 标枪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 309 | 铁枪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 310 | 白马标志 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 311 | 马牌（黄骠马） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 312 | 马牌（的卢） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 313 | 古籍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 314 | 鸡血 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 315 | 烧酒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 316 | 毒蛇牙齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 317 | 王铁匠的铁锤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 318 | 角笛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 319 | 半块不死牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 320 | 不死牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 321 | 雷电僵尸骨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 322 | 僧侣僵尸骨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 323 | 毁灭护身符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 324 | 七点白蛇胆 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 325 | 斗笠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 326 | 翔空剑法 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 327 | 莲月剑法 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 328 | 空拳刀法 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 329 | 月魂断玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 330 | 冰月神掌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 331 | 冰月震天 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 332 | 霹雳掌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 333 | 月魂灵波 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 334 | 墨龙屠龙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 335 | 墨龙嗜魂法杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 336 | 墨龙龙纹剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 348 | 七点白蛇血 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 349 | 金刚铃铛 | 金刚铃铛 | 与官方正式名称精确匹配；官方条目状态：uncertain-version |
| 物品 | 350 | 金刚魔法指环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 351 | 金刚精神戒指 | 金刚精神戒指 | 与官方正式名称精确匹配；官方条目状态：uncertain-version |
| 物品 | 352 | 金刚防御手镯 | 金刚防御手镯 | 与官方正式名称精确匹配；官方条目状态：uncertain-version |
| 物品 | 353 | 金刚魔法手镯 | 金刚魔法手镯 | 与官方正式名称精确匹配；官方条目状态：uncertain-version |
| 物品 | 354 | 霹雷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 355 | 铁轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 356 | 逍遥扇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 357 | 劳动蚂蚁卵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 358 | 诺玛法老珍珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 360 | 雷神戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 361 | 毁灭手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 362 | 神谕项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 363 | 昏暗风印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 364 | 润神戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 365 | 如来手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 366 | 猫眼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 367 | 怨恨项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 368 | 尾毛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 369 | 生存游戏场地地图1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 370 | 信件 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 371 | 帐簿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 372 | 半兽人角笛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 373 | 不死骨头 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 374 | 尹老人的酒瓶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 375 | 姜铁匠的斧头 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 376 | 盔甲的蚂蚁卵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 377 | 七点白蛇胆汁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 378 | 邪恶钳虫皮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 379 | 腐蚀人鬼之泪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 380 | 沃玛勇士号角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 381 | 钳虫皮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 383 | 千年毒蛇牙齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 384 | 沃玛角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 385 | 骷髅精灵骨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 386 | 啊潘的信件 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 387 | 华玉的信件 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 388 | 比奇历史书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 389 | 魔灵牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 391 | 幻影蜘蛛线 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 394 | 血巨人心脏 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 395 | 触龙神皮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 396 | 法师神杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 397 | 航海日志 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 398 | 遗骸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 399 | 七点白蛇牙齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 400 | 魔幻戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 401 | 石头 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 402 | 箭 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 403 | 天机戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 404 | 巨龙戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 405 | 天鸣戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 406 | 火玉戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 407 | 五彩项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 408 | 遗魂项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 409 | 王大人的书信 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 410 | 葫芦 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 411 | 瓶中信 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 412 | 生锈牙轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 413 | 汤药 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 414 | 瓷器箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 415 | 旧扇子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 416 | 怀旧项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 418 | 水晶球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 419 | 锦秀的衣角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 420 | 万多罗的护身符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 421 | 万相的护身符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 422 | 三妹的护身符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 423 | 战士的证票 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 424 | 秘密医书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 425 | 黑野猪牙齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 426 | 七点白蛇的牙齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 427 | 祖玛卫士雕像 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 428 | 半兽利齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 430 | 千年毒蛇血 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 431 | 虎蛇血 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 432 | 黑檀雕像 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 433 | 波善的短剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 434 | 黑蝉项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 435 | 消魔的护身符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 436 | 陈氏护身符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 437 | 荣耀项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 438 | 愤怒之钟 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 439 | 莲花宝镜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 440 | 魔神怪手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 441 | 行者帽 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 442 | 战神头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 443 | 虎面头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 444 | 旋风流星刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 445 | 角剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 446 | 飞魂魔刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 447 | 虚空道环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 448 | 准确之炼狱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 449 | 红叶血环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 450 | 六棱戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 451 | 紫金环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 452 | 武圣之戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 453 | 基本剑术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 454 | 攻杀剑术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 455 | 刺杀剑术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 456 | 半月弯刀（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 457 | 野蛮冲撞（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 458 | 烈火剑法（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 459 | 莲月剑法（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 460 | 翔空剑法（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 461 | 火球术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 462 | 诱惑之光（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 463 | 抗拒火环（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 464 | 雷电术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 465 | 瞬息移动（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 466 | 大火球（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 467 | 地狱火（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 468 | 爆裂火焰（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 469 | 疾光电影（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 470 | 火墙（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 471 | 地狱雷光（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 472 | 魔法盾（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 473 | 圣言术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 474 | 冰咆哮（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 475 | 冰月神掌（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 476 | 冰月震天（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 477 | 霹雳掌（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 478 | 精神力战法（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 479 | 治愈术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 480 | 施毒术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 481 | 灵魂火符（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 482 | 幽灵盾（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 483 | 神圣战甲术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 484 | 召唤骷髅（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 485 | 困魔咒（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 486 | 隐身术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 487 | 集体隐身术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 488 | 七彩金环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 489 | 群体治愈术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 490 | 召唤神兽（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 491 | 空拳刀法（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 492 | 月魂断玉（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 493 | 月魂灵波（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 494 | 拓本 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 495 | 心魔戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 496 | 破真刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 497 | 纱王项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 498 | 灵魂明珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 499 | 花毒粉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 500 | 沃毒神精 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 501 | 连环明珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 502 | 祖玛卫士明珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 503 | 制灵水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 504 | 真实明镜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 505 | 祖玛明珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 506 | 安心石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 507 | 诸神道书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 508 | 宝玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 509 | 祖玛雕像号角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 510 | 制魔油 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 511 | 牛肉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 512 | 猪肉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 513 | 攻杀铁剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 514 | 道力护身符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 515 | 肉汤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 516 | 灵珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 517 | 无名药 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 518 | 千年毒蛇胆汁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 519 | 胆汁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 520 | 生存游戏场地地图2 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 521 | 战酒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 522 | 耐久轻型盔甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 523 | 耐久轻型盔甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 524 | 狼肉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 525 | 羊肉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 526 | 不死戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 527 | 起爆石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 528 | 树脂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 529 | 闪电石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 530 | 树脂魔法长袍（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 531 | 树脂魔法长袍（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 532 | 书信 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 533 | 诺玛石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 534 | 诺玛重盔甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 535 | 诺玛重盔甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 536 | 神奇灵魂战衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 537 | 神奇灵魂战衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 538 | 蚂蚁卵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 540 | 浪雨刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 541 | 波纹手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 542 | 白虎剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 543 | 灵魂护卫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 544 | 沃玛神铁锤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 545 | 无名日志 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 546 | 沃玛金牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 547 | 地狱神钟 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 548 | 黑珍珠戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 549 | 龙骨戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 550 | 天龙环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 551 | 魔家项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 552 | 流星天玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 553 | 月光石手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 554 | 天仙之珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 555 | 松笛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 556 | 八面太极戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 557 | 伏羲手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 558 | 中秋之夜（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 559 | 中秋之夜（秋） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 560 | 中秋之夜（之） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 561 | 中秋之夜（夜） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 562 | 中秋之夜（团） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 563 | 中秋之夜（圆） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 564 | 中秋之夜（美） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 565 | 中秋之夜（满） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 566 | 中秋之夜（幸） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 567 | 中秋之夜（福） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 572 | 成致日志 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 580 | 毒蛇胆汁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 581 | 千年毒蛇之牙齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 582 | 褐色栗子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 583 | 铜色栗子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 584 | 银色栗子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 585 | 金色栗子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 587 | 霸王教主雕像 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 588 | 老中医的医书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 589 | 未鉴定阴阳刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 590 | 未鉴定拐杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 591 | 未鉴定天狼刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 592 | 魔灵戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 593 | 石榴戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 594 | 青摇戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 595 | 火焰沃玛之角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 596 | 莲丸戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 597 | 冰沙掌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 598 | 铁系项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 599 | 追魂项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 600 | 追风项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 601 | 魔令项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 602 | 缥缈戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 603 | 尸王白骨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 604 | 魔令手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 605 | 宝藏岛地图3 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 607 | 未鉴定赤龙神甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 608 | 未鉴定赤龙神甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 609 | 未鉴定赤龙头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 610 | 未鉴定虎影戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 611 | 风掌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 612 | 未鉴定永柳戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 614 | 诺玛药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 615 | 气血项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 616 | 龙卷风 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 617 | 风震天 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 618 | 击风 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 619 | 流星项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 620 | 毁灭魔链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 621 | 回生术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 622 | 震天项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 623 | 五行神镜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 624 | 银镜项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 625 | 沙漠鱼魔牙齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 626 | 武器强化油 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 627 | 黑皮手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 628 | 铁炼腕 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 629 | 英雄手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 630 | 生存游戏场地地图4 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 632 | 诅咒之药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 633 | 强魔震法 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 634 | 月光鞋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 636 | 无影靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 637 | 五彩鞋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 638 | 猛虎强势 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 639 | 仙云靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 640 | 武神之靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 641 | 绝地靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 642 | 乾坤大挪移（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 645 | 野山花 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 646 | 盔甲蚂蚁卵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 647 | 阿才的书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 648 | 移形换位 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 650 | 斗转星移（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 651 | 红娥宝玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 652 | 破山剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 653 | 阴阳刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 654 | 拐杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 655 | 铁布衫（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 656 | 封魔剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 657 | 破血狂杀（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 658 | 花色蜘蛛毒药 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 660 | 冰沙掌（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 662 | 震天魔印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 663 | 思念珍珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 664 | 怒神霹雳（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 665 | 天神法杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 666 | 稻草人木剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 667 | 凝血离魂（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 668 | 云寂术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 669 | 复血 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 670 | 沃玛头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 671 | 天藤头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 672 | 移花接玉（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 673 | 妙影无踪（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 674 | 风掌（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 675 | 阴阳法环（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 676 | 双刃剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 677 | 石人心核 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 679 | 龙卷风（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 680 | 风震天（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 681 | 击风（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 684 | 回生术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 685 | 乾坤一气 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 690 | 乾坤大挪移 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 691 | 斗转星移 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 692 | 瑕疵黑檀手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 693 | 蛇谷老人手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 694 | 铁布衫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 695 | 破血狂杀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 696 | 强魔震法（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 699 | 润神戒指（暗黑） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 700 | 润神戒指（幻影） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 701 | 猛虎强势（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 711 | 移形换位（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 712 | 沃毒骷髅戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 713 | 白月银蛇戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 714 | 白眼珍珠戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 715 | 金刚黑檀手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 716 | 沃毒小手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 717 | 沃角手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 718 | 十方斩 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 719 | 魄冰刺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 720 | 怒神霹雳 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 721 | 凝血离魂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 722 | 云寂术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 723 | 移花接玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 724 | 蓝光凝霜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 725 | 红光偃月 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 726 | 黑光降魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 727 | 诺玛族修罗 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 728 | 诅咒银蛇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 729 | 诺玛族魔杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 731 | 腐烂骷髅头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 732 | 蓝竹笛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 733 | 腐烂竹笛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 740 | 旧放大镜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 741 | 旧蓝翡翠项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 742 | 幸运降妖除魔戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 743 | 炸铜炼狱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 744 | 潘夜命运之刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 745 | 潘夜银蛇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 746 | 潘夜魔杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 747 | 沃玛修罗 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 748 | 沃玛降魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 749 | 沃玛偃月 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 750 | 骷髅骨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 751 | 虎蛇牙齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 752 | 红蛇血 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 753 | 祖玛裁决之杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 754 | 祖玛无极棍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 755 | 祖玛骨玉权杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 756 | 童子像 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 757 | 竹棍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 758 | 牛毛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 759 | 苍蝇拍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 760 | 制魔宝玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 761 | 亮蜡烛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 762 | 焰火项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 763 | 焰火手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 764 | 闪电眼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 765 | 灵魂铁手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 766 | 幻影玉珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 767 | 黑除魔戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 768 | 神圣铂金戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 769 | 亮火把 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 770 | 草鞋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 771 | 皮靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 772 | 赤飞靴子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 773 | 黑皮靴子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 774 | 天掌靴子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 775 | 潘夜珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 776 | 潘夜之泪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 777 | 夜明珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 778 | 超强召唤骷髅 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 779 | 超强召唤骷髅（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 780 | 牙齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 781 | 祝福霸龙头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 782 | 古诗秘书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 783 | 蜘蛛线 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 784 | 浓烟黑檀项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 785 | 妙影无踪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 786 | 金创药（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 787 | 蝉翼刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 788 | 魔法药（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 789 | 金创药（特）包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 790 | 魔法药（特）包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 791 | 耐久铁手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 792 | 气霖证书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 793 | 玉指环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 794 | 威魂深怨护身符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 795 | 第一困魔石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 796 | 第二困魔石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 797 | 第三困魔石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 798 | 第四困魔石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 799 | 最后困魔石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 800 | 焱火剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 801 | 新火镜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 802 | 皮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 803 | 断交先生的书信 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 805 | 灵魂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 806 | 阴阳法环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 807 | 无名油 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 808 | 指甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 809 | 神灵雕像 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 810 | 僵尸骨头 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 811 | 护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 812 | 灵魂护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 813 | 灵魂护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 814 | 藏罪据证 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 817 | 焰天火雨（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 818 | 霸龙头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 821 | 紫水晶矿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 822 | 石榴石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 823 | 金刚石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 824 | 钢玉石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 825 | 风之鹤嘴锄 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 826 | 跳蚤皮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 827 | 诅咒海魂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 828 | 潘夜血饮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 829 | 诅咒半月 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 830 | 潘夜无极棍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 831 | 幸运青铜头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 832 | 幸运斗笠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 833 | 幸运骷髅头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 834 | 焰天火雨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 838 | 龙鳞战甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 839 | 龙鳞战甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 840 | 袁灵法衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 841 | 袁灵法衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 842 | 天极道衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 843 | 天极道衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 844 | 帝王戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 845 | 润神戒指（神圣） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 846 | 雷神戒指（火） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 847 | 武士手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 848 | 火玉手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 849 | 毁灭手镯（火） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 850 | 如来手镯（神圣） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 851 | 钻石项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 852 | 勇士项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 853 | 破坏项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 854 | 五色项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 855 | 愤怒之钟（火） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 856 | 昏暗封印（火） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 857 | 真善项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 858 | 莲花宝镜（神圣） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 859 | 怨恨项链（神圣） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 860 | 指环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 861 | 神圣护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 862 | 神圣护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 863 | 火焰护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 864 | 寒气护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 865 | 霹雷护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 866 | 狂风护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 867 | 号角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 868 | 雪球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 869 | 诺玛王雕像 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 888 | 箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 889 | 破军城堡雕像 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 890 | 泰轮拂尘 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 897 | 缥缈项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 901 | 缥缈手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 902 | 当啷戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 903 | 影刺雷戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 904 | 遗物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 905 | 神女书信 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 906 | 地图 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 907 | 密信 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 908 | 养颜长生果 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 909 | 比奇城主书信 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 910 | 诺玛族信物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 911 | 破损古书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 912 | 诺玛遗物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 913 | 寂幻之刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 914 | 血花落照 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 915 | 黑天暗云 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 916 | 九宫云雾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 917 | 万里碧海 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 918 | 影魅之刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 919 | 藏宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 920 | 红玫瑰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 922 | 喜袋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 923 | 血花落照（血） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 924 | 血花落照（花） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 925 | 血花落照（落） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 926 | 血花落照（照） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 927 | 黑天暗云（黑） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 928 | 黑天暗云（天） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 929 | 黑天暗云（暗） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 930 | 黑天暗云（云） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 931 | 九宫云雾（九） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 932 | 九宫云雾（宫） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 933 | 九宫云雾（云） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 934 | 九宫云雾（雾） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 935 | 万里碧海（万） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 936 | 万里碧海（里） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 937 | 万里碧海（碧） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 938 | 万里碧海（海） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 939 | 大族长角笛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 940 | 遗址雕像 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 944 | 通用卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 945 | 未鉴定咒恶戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 946 | 未鉴定神魔手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 947 | 未鉴定神魔项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 948 | 未鉴定龙血鞋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 949 | 未鉴定修罗战甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 950 | 未鉴定修罗战甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 951 | 未鉴定生死轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 952 | 未鉴定修罗戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 953 | 未鉴定桃源仙甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 954 | 未鉴定桃源仙甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 955 | 未鉴定桃之蓁蓁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 991 | 生锈师承戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 992 | 生锈龙马戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 993 | 生锈青云戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 994 | 生锈破荒项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 995 | 生锈魔云项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 996 | 生锈定心项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 997 | 生锈金棱手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 998 | 生锈思过手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 999 | 生锈世尊手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1000 | 火焰护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1001 | 寒气护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1002 | 霹雷护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1003 | 狂风护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1004 | 神圣护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1005 | 护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1007 | 任务索引 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1008 | 公文 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1009 | 肉块 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1010 | 毁灭之印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1012 | 尸骨项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1013 | 击退护身符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1014 | 未鉴定桃源盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1015 | 未鉴定桃源靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1016 | 未鉴定桃源虎翼刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1017 | 未鉴定桃源曜灵杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1018 | 未鉴定桃源三焰扇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1019 | 未鉴定桃之夭夭 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1020 | 未鉴定桃之灼灼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1021 | 元素糖果 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1022 | 攻击糖果 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1023 | 未鉴定桃源之心 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1024 | 未鉴定桃源斩轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1025 | 书籍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1026 | 神勇之物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1027 | 节制之物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1028 | 决断之物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1029 | 智慧之物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1030 | 正义之物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1031 | 投票单 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1032 | 青空石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1033 | 大地石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1034 | 太阳石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1035 | 月光石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1036 | 受胎石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1037 | 安息石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1038 | 活石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1039 | 心石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1040 | 神秘之印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1041 | 机关零件 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1042 | 霹雳手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1043 | 碧玉水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1044 | 猫眼石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1045 | 养神护身符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1046 | 冰洁石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1047 | 卷轴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1048 | 青蛇眼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1049 | 月影戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1050 | 灵气剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1051 | 绿水晶项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1052 | 冰月项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1053 | 恋风手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1054 | 呼风手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1055 | 种子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1056 | 树苗 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1057 | 肥料 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1058 | 无名书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1059 | 调查报告 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1060 | 祖玛宝典 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1061 | 乐透彩票 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1062 | 天赐战甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1063 | 天赐战甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1064 | 康乃馨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1065 | 百里香 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1066 | 财富之书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1067 | 解毒药 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1068 | 金令牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1069 | 恶狼之血 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1070 | 森林雪人指甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1071 | 家谱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1072 | 神秘油 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1073 | 圣人灵药 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1074 | 遗失的手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1075 | 灵药 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1076 | 史书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1077 | 遗失的斧子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1078 | 医术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1079 | 火焰沃玛号角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1080 | 蜜袋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1081 | 药箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1082 | 遗失的手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1083 | 震天魔镜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1084 | 遗失的项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1085 | 祖玛护法铁锤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1086 | 血巨人指甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1087 | 遗失的铁锄 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1088 | 遗失的头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1089 | 魔艳项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1090 | 遗失的护身符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1091 | 巨象兽牙齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1092 | 药草 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1093 | 除魔大师的秘传书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1094 | 素玉戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1095 | 名册 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1096 | 抛魂铃铛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1097 | 断了的琵琶弦 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1098 | 极乐琵琶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1099 | 噬魂铃铛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1100 | 麒麟宝铠（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1101 | 麒麟宝铠（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1102 | 仙风神袍（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1103 | 仙风神袍（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1104 | 阴阳圣衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1105 | 阴阳圣衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1106 | 飞龙剑（火） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1107 | 飞龙剑（冰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1108 | 飞龙剑（雷） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1109 | 飞龙剑（风） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1110 | 古书籍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1111 | 牛角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1112 | 地图书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1113 | 碧玉项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1114 | 旧锤子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1115 | 诺玛将士药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1116 | 咒书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1117 | 祖玛雕像碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1118 | 飞龙剑（神圣） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1119 | 飞龙剑（元素） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1120 | 飞龙剑（幻影） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1121 | 未鉴定黑玉战甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1122 | 未鉴定黑玉战甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1123 | 未鉴定沐水璃殇佩 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1124 | 未鉴定沐水手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1125 | 经书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1126 | 金属块 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1127 | 未鉴定沐水霜晓戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1128 | 未鉴定沐水灭魂戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1129 | 触龙神之钟 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1130 | 红野猪牙齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1131 | 飞龙剑碎片（火） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1132 | 飞龙剑碎片（冰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1133 | 飞龙剑碎片（雷） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1134 | 飞龙剑碎片（风） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1135 | 飞龙剑碎片（神圣） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1136 | 飞龙剑碎片（元素） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1137 | 飞龙剑碎片（幻影） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1138 | 绝世战甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1139 | 绝世战甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1140 | 头领证明书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1141 | 未鉴定沐水天靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1142 | 未鉴定沐水天冠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1143 | 未鉴定龙雀开山钺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1144 | 未鉴定奕天破邪杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1145 | 未鉴定秋水无痕剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1146 | 未鉴定碎情雾影环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1147 | 未鉴定幻世魔衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1148 | 未鉴定幻世魔衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1149 | 未鉴定沐水天衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1150 | 未鉴定沐水天衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1151 | 未鉴定蝶恋清寒链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1152 | 未鉴定玄云碎魄镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1153 | 未鉴定鹰扬醉舞戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1196 | 未鉴定清寒浅浪戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1255 | 虎齿刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1274 | 狂暴冲撞 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1275 | 狂暴冲撞（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1276 | 旋风墙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1277 | 旋风墙（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1278 | 灵魂分裂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1279 | 灵魂分裂（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1280 | 暗黑护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1281 | 暗黑护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1282 | 泣血花 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1283 | 急救丸（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1284 | 急救丸（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1285 | 急救丸（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1286 | 急救丸（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1287 | 清心丸（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1288 | 清心丸（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1289 | 清心丸（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1290 | 清心丸（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1291 | 金创药（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1292 | 急救丸（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1298 | 清心丹（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1299 | 清心丹（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1300 | 清心丹（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1301 | 清心丹（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1318 | 制炼石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1319 | 结晶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1320 | 魔光片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1321 | 杂货商的旧文件 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1322 | 木制零件 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1323 | 生锈钉子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1324 | 未鉴定玄云靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1325 | 未鉴定玄云盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1326 | 未鉴定熔金落日刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1327 | 未鉴定龙破沧溟 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1328 | 未鉴定天雷真火扇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1329 | 未鉴定天星耀阳环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1330 | 慧理的遗骸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1331 | 药剂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1332 | 老鼠指甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1333 | 旧香匣 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1334 | 旧羊皮纸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1335 | 未鉴定凶陌圣甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1336 | 未鉴定凶陌圣甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1337 | 未鉴定玄云鸾暮铠（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1338 | 旧梳子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1339 | 金属板 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1340 | 钉子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1341 | 旧箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1342 | 祖玛教主印记 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1343 | 生锈金属板 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1344 | 旧木雕 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1345 | 内伤治疗剂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1346 | 记忆之珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1347 | 结婚礼服 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1348 | 戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1349 | 疗伤丹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1350 | 海西秘记 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1356 | 金牛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1357 | 山参 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1358 | 夏马风屠龙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1359 | 夏马风龙纹剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1360 | 夏马风嗜魂法杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1361 | 期望之霹雷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1362 | 期望之逍遥扇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1363 | 期望之铁轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1364 | 潘夜嗜魂法杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1365 | 潘夜井中月 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1366 | 天狼刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1367 | 三台项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1368 | 三台手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1369 | 三台戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1370 | 天丛项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1371 | 天丛手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1372 | 天丛戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1373 | 转轮项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1374 | 转轮手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1375 | 转轮戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1376 | 礼物箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1381 | 玄武盾碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1382 | 稀有书籍残片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1383 | 代书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1384 | 催眠香 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1385 | 回信 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1386 | 金绿玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1387 | 破旧的地图碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1388 | 真天宫藏宝图 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1389 | 古月历 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1390 | 许可印证 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1391 | 黄昏泪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1392 | 黄昏项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1393 | 雪包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1394 | 凝血液 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1395 | 冰晶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1396 | 金面玉牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1397 | 赤眼红花蛇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1398 | 紫云剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1399 | 封印的乌木箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1400 | 未鉴定玄云鸾暮铠（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1401 | 未鉴定幻陌靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1402 | 未鉴定虎啸项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1403 | 未鉴定虎啸手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1404 | 未鉴定虎啸戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1405 | 未鉴定神魂湮灭剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1406 | 未鉴定龙吟项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1407 | 未鉴定龙吟手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1408 | 破碎的红印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1409 | 红印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1410 | 破碎的黑印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1411 | 黑印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1412 | 触角神魔皮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1413 | 破碎的白印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1414 | 白印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1415 | 破碎的绿印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1416 | 绿印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1417 | 无名项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1418 | 神人项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1425 | 鸡蛋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1434 | 煎鸡蛋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1435 | 黄金蛋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1436 | 珀玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1442 | 太极旗 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1443 | 旭日戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1444 | 霸王项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1445 | 登天手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1446 | 三桓戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1447 | 避难项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1448 | 云龙手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1449 | 继承戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1450 | 昆仑项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1451 | 至善手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1452 | 天狼头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1453 | 天狼靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1455 | 横扫千军 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1456 | 横扫千军（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1457 | 五星牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1458 | 紫色鸡蛋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1459 | 粉红色鸡蛋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1460 | 红色鸡蛋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1461 | 白色鸡蛋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1462 | 金色鸡蛋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1463 | 复活节鸡蛋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1469 | 祖玛葫芦 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1470 | 潘夜葫芦 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1471 | 赤月葫芦 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1472 | 震天葫芦 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1473 | 黑度葫芦 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1527 | 移花接木 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1528 | 移花接木（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1529 | 陨冰杀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1530 | 陨冰杀（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1531 | 焰魔石（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1532 | 焰魔石（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1533 | 焰魔石（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1534 | 焰魔石（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1535 | 马牌（绝影） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1536 | 马牌（赤兔马） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1537 | 征服者日志碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1538 | 比奇城设计图 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1539 | 封印宝剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1540 | 雷神灵珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1541 | 神圣灵珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1542 | 幻影灵珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1543 | 破坏护身符（雷） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1544 | 破坏护身符（神圣） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1545 | 破坏护身符（幻影） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1546 | 诺玛司令封印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1547 | 诺玛斧兵心脏 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1548 | 封印的灭绝刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1549 | 诺玛族宝物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1550 | 杀魔血刀戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1551 | 师玉戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1552 | 九梦戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1553 | 杀魔血刀手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1554 | 师玉手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1555 | 九梦手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1556 | 杀魔血刀项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1557 | 师玉项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1558 | 九梦项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1559 | 雷天鞋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1560 | 银光鞋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1561 | 灵云鞋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1562 | 金刚之躯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1563 | 金刚之躯（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1564 | 养生术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1565 | 养生术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1566 | 泰山压顶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1567 | 泰山压顶（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1568 | 快刀斩马 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1569 | 快刀斩马（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1570 | 运气术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1571 | 运气术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1572 | 天打雷劈 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1573 | 天打雷劈（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1574 | 电闪雷鸣 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1575 | 电闪雷鸣（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1576 | 新传染 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1577 | 新传染（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1578 | 吸星大法 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1579 | 吸星大法（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1580 | 迷魂大法 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1581 | 迷魂大法（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1584 | 光魔石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1585 | 白光魔石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1586 | 黑光魔石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1587 | 初级碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1588 | 中级碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1589 | 高级碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1590 | 超级碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1591 | 冰魔石（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1592 | 冰魔石（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1593 | 冰魔石（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1594 | 冰魔石（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1595 | 雷魔石（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1596 | 雷魔石（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1597 | 雷魔石（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1598 | 雷魔石（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1599 | 风魔石（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1600 | 风魔石（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1601 | 风魔石（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1602 | 风魔石（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1603 | 护身碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1604 | 麻痹碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1605 | 复活碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1606 | 防御碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1607 | 8级妖丹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1608 | 照妖镜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1609 | 佛像泪珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1610 | 铁链锁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1611 | 魔石狂热者牙齿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1612 | 自尊石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1613 | 赤龙剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1614 | 灵泉水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1615 | 南襄葫芦 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1616 | 破血魔镜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1617 | 破血魔镜（破） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1618 | 破血魔镜（血） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1619 | 破血魔镜（魔） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1620 | 破血魔镜（镜） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1621 | 烟花（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1622 | 烟花（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1623 | 烟花（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1624 | 烟花（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1625 | 桃源仙甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1626 | 桃源仙甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1627 | 护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1628 | 至尊牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1629 | 混元掌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1630 | 混元掌（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1631 | 透心链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1632 | 透心链（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1633 | 魔爆术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1634 | 魔爆术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1635 | 地狱魔焰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1636 | 地狱魔焰（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1637 | 屠龙斩 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1638 | 屠龙斩（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1639 | 旋风斩 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1640 | 旋风斩（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1641 | 君临步 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1642 | 君临步（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1643 | 魔光盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1644 | 魔光盾（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1645 | 焚魂魔功 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1646 | 焚魂魔功（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1647 | 神灵守护 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1648 | 神灵守护（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1649 | 隐魂术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1650 | 隐魂术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1651 | 月明波 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1652 | 月明波（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1653 | 艾娜专用剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1661 | 褐木白花 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1662 | 诊断书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1663 | 凤凰翎毛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1664 | 白鹿犄角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1665 | 冰水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1666 | 震天之珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1667 | 不死牌碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1668 | 骷髅教主名册 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1669 | 赤月之珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1670 | 祖玛号角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1671 | 灭绝之剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1672 | 沙漠白雪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1678 | 钱票 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1702 | 修罗戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1703 | 修罗手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1714 | 修能秘录 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1715 | 圣诞帽 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1716 | 圣诞节（圣） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1717 | 圣诞节（诞） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1718 | 圣诞节（节） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1719 | 圣诞节（快） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1720 | 圣诞节（乐） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1721 | 圣诞卡片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1727 | 猎犬灵魂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1728 | 犬公交换券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1729 | 魔魂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1730 | 挑战券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1742 | 护身金甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1743 | 护身金甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1744 | 护身宝甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1745 | 护身宝甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1746 | 勇霖银甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1747 | 勇霖银甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1748 | 勇霖宝甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1749 | 勇霖宝甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1750 | 明光凤衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1751 | 明光凤衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1752 | 赤冠魔衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1753 | 赤冠魔衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1754 | 赤龙神甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1755 | 赤龙神甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1756 | 特殊药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1775 | 地图指南 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1788 | 付费地下城门票 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1789 | 木剑（10） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1792 | 木制短剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1793 | 足球鞋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1794 | 足球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1795 | 世界杯卡片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1797 | 黄牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1798 | 红牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1818 | 金刚套宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1819 | 祈祷套宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1820 | 虹膜套宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1821 | 魔血套宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1822 | 记忆套宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1823 | 战士宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1824 | 法师宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1825 | 道士宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1826 | 经验葫芦（50%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1827 | 经验葫芦（80%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1828 | 高级经验葫芦（每周限量） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1829 | 高级经验葫芦（晚上限量） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1830 | 经验葫芦（100%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1831 | 经验葫芦（30%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1832 | 幸运石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1833 | 天山雪莲（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1834 | 天山雪莲（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1835 | 天山雪莲（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1836 | 天山雪莲（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1837 | 深海灵礁（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1838 | 深海灵礁（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1839 | 深海灵礁（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1840 | 深海灵礁（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1841 | 战士强化药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1842 | 战士强化药水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1843 | 法师强化药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1844 | 法师强化药水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1845 | 道士强化药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1846 | 道士强化药水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1847 | 攻击神水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1848 | 疾风神水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1849 | 自然神水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1850 | 灵魂神水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1851 | 体力强效神水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1852 | 魔力强效神水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1853 | 火焰护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1854 | 寒气护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1855 | 霹雷护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1856 | 狂风护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1857 | 暗黑护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1858 | 传送卷轴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1859 | 回生战水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1860 | 回生丸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1861 | 火魔石（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1862 | 冰魔石（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1863 | 雷魔石（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1864 | 风魔石（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1865 | 破坏印记（限时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1866 | 自然印记（限时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1867 | 灵魂印记（限时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1868 | 火之印记（限时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1869 | 冰之印记（限时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1870 | 雷之印记（限时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1871 | 风之印记（限时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1872 | 神圣印记（限时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1873 | 暗黑印记（限时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1874 | 首饰特修神水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1875 | 服饰特修神水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1876 | 特修神水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1877 | 红色精炼石（武器） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1878 | 制炼石（专业） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1879 | 灰色精炼石（首饰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1880 | 紫色精炼石（首饰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1881 | 解毒丸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1882 | 回生神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1883 | 回生神水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1884 | 传音号角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1885 | 传音书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1886 | 玩家名称 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1887 | 雕刻名字工具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1888 | 改名凭证 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1889 | 性别更改凭证 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1890 | 沙巴克徽章 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1891 | 沙漠土城徽章 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1896 | 超级体力药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1897 | 超级魔法药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1898 | 超级灵魂药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1899 | 超级自然药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1900 | 超级攻击药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1901 | 制炼石（强化） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1902 | 高级怪物租用 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1903 | 诺玛套宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1908 | 召唤强化咒书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1909 | 火银龙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1910 | 神符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1914 | 额外库存 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1915 | 额外仓库扩展 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1916 | 白犬租赁卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1917 | 疾风镐 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1918 | 武林名宿（证书） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1919 | 仁义大侠（证书） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1920 | 英雄豪杰（证书） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1921 | 武林至尊（证书） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1922 | 高级经验葫芦（1天） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1923 | 高级经验葫芦（7天） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1924 | 高级经验葫芦（14天） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1948 | 衣服染色液 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1949 | 沐水璃殇佩 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1953 | 沐水手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1954 | 沐水霜晓戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1955 | 沐水灭魂戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1956 | 沐水天靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1957 | 蝶恋清寒链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1958 | 玄云碎魄镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1959 | 鹰扬醉舞戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1960 | 清寒浅浪戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1961 | 玄云靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1962 | 黄色玫瑰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1963 | 绿玫瑰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1964 | 蓝玫瑰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1965 | 幻陌靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1966 | 包月收费 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1967 | 神力戒指-兑换券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1968 | 探测项链-兑换券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1969 | 技巧项链-兑换券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1970 | 传送戒指-兑换券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1971 | 麻痹戒指-兑换券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1972 | 护身戒指-兑换券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1973 | 武器首饰制炼包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1974 | 红铃铛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1975 | 蓝铃铛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1976 | 紫铃铛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1977 | 冰煤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1978 | 羽旗（龙） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1979 | 圣诞手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1980 | 圣诞鞋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1981 | 圣诞袜子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1989 | 饮料（绿） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1990 | 饮料（蓝） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1991 | 红色钱包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1992 | 黄色钱包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1993 | 神宫传送卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1994 | 雪原冰宫传送卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1995 | 神舰传送卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1996 | 传送石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1997 | 防御药水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1998 | 防御药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 1999 | 防御药水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2005 | 赤龙佩刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2006 | 日月戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2007 | 日月手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2008 | 日月项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2009 | 天辉戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2010 | 天辉手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2011 | 天辉项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2012 | 消魂戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2013 | 消魂手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2014 | 消魂项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2015 | 赤龙戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2016 | 赤龙手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2017 | 赤龙项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2018 | 赤龙靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2019 | 赤龙头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2020 | 传送圣链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2021 | 延期丸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2022 | 玉液琼浆 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2023 | 陈年佳酿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2024 | 传奇包（30%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2025 | 魔气的结晶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2026 | 还魂花 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2027 | 战士加强水（限量） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2028 | 法师加强水（限量） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2029 | 道士加强水（限量） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2034 | 初学休眠包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2035 | 名声号牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2036 | 强化破坏印记 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2037 | 强化自然印记 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2038 | 强化灵魂印记 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2039 | 强化火印记 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2040 | 强化冰印记 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2041 | 强化雷印记 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2042 | 强化风印记 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2043 | 强化神圣印记 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2044 | 强化暗黑印记 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2045 | 强化幻影印记 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2046 | 战士技能药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2047 | 道士技能药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2048 | 法师技能药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2049 | 幻影印记（限时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2050 | 暗黑印记 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2051 | 册本子（敌人） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2052 | 册本子（蓝色） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2053 | 旗子（虎） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2054 | 幸运包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2055 | 传送卷轴（合同制） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2056 | 幸运号码项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2057 | 幸运油 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2058 | 冶炼增强箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2059 | 师傅鞋箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2060 | 彼岸花 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2061 | 神仙花 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2062 | 图像处理芯片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2063 | LCD支架 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2064 | NDSL键盘 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2065 | 存储条 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2066 | NDSL | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2067 | NDSLGame包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2068 | 虎影戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2069 | 永柳戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2070 | 咒恶戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2071 | 神魔手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2072 | 纯白天甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2073 | 超月天甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2074 | 枫壁靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2075 | 神魔项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2076 | 碧夜军甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2077 | 洁白军甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2078 | 赤月军甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2079 | 凤凰牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2080 | 随机发型 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2081 | 光火明珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2082 | （男）超帅短发 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2083 | （男）刺猬头型 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2084 | （男）半扎辩子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2085 | （女）兔尾辫子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2086 | （女）兔耳头型 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2087 | （女）半扎辩头型 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2088 | 黑犬租赁卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2095 | 海市蜃楼宝剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2096 | 攻击水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2097 | 幻月之书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2098 | 幻月之剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2099 | 幻月戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2102 | 生锈的日月戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2103 | 裂开的日月戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2104 | 陈旧的日月戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2105 | 生锈的日月手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2106 | 裂开的日月手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2107 | 陈旧的日月手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2108 | 划痕之日月手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2109 | 生锈的日月项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2110 | 裂开的日月项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2111 | 陈旧的日月项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2112 | 生锈的消魂戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2113 | 裂开的消魂戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2114 | 陈旧的消魂戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2115 | 生锈的消魂手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2116 | 裂开的消魂手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2117 | 陈旧的消魂手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2118 | 划痕之消魂手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2119 | 生锈的消魂项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2120 | 裂开的消魂项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2121 | 陈旧的消魂项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2122 | 生锈的天辉戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2123 | 裂开的天辉戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2124 | 陈旧的天辉戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2125 | 生锈的天辉手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2126 | 裂开的天辉手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2127 | 陈旧的天辉手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2128 | 划痕之天辉手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2129 | 生锈的天辉项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2130 | 裂开的天辉项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2131 | 陈旧的天辉项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2132 | 饼干条 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2133 | 桃子饼干条 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2134 | 烫发 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2135 | （男）碎发 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2136 | （女）兔耳发型 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2137 | （女）双辫发型 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2138 | 龙轮酒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2139 | 镜面朱砂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2140 | 雷水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2141 | 欲望的雷水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2142 | 忠实的雷水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2143 | 蚩尤的角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2144 | 东蚩尤的角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2145 | 西蚩尤的角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2146 | 阎昆的绿色碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2147 | 阎昆的红色碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2148 | 蚩尤战剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2149 | 真龙幻剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2154 | 七面鸟肉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2155 | 铁甲马铠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2156 | 银质马铠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2157 | 黄金马铠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2158 | 传送助手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2159 | 感谢包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2160 | 圣诞祝炮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2161 | 火焰强玉酒（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2162 | 寒气强玉酒（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2163 | 霹雷强玉酒（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2164 | 狂风强玉酒（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2165 | 神圣强玉酒（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2166 | 暗黑强玉酒（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2167 | 幻影强玉酒（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2168 | 全效强玉酒（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2169 | 火焰强玉酒（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2170 | 寒气强玉酒（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2171 | 霹雷强玉酒（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2172 | 狂风强玉酒（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2173 | 神圣强玉酒（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2174 | 暗黑强玉酒（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2175 | 幻影强玉酒（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2176 | 全效强玉酒（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2177 | 火焰强玉酒（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2178 | 寒气强玉酒（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2179 | 霹雷强玉酒（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2180 | 狂风强玉酒（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2181 | 神圣强玉酒（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2182 | 暗黑强玉酒（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2183 | 幻影强玉酒（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2184 | 全效强玉酒（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2185 | 烦恼药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2186 | 破气米酒（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2187 | 魔气米酒（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2188 | 灵气米酒（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2189 | 高级体练酒（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2190 | 高级魔练酒（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2191 | 狂风药水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2192 | 战士宝玲水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2193 | 道士宝玲水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2194 | 法师宝玲水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2195 | 召唤之书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2196 | 心愿箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2197 | 五龙牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2198 | 感谢信 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2199 | 感谢碎片（青） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2200 | 感谢碎片（紫） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2201 | 感谢碎片（黑） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2202 | 感谢碎片（黄） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2203 | 感谢碎片（红） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2204 | 5周年纪念箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2210 | 经验珠（100万） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2211 | 经验珠（500万） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2212 | 经验珠（1000万） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2213 | 50万经验丸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2214 | 100万经验丸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2215 | 月饼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2249 | 龙王项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2250 | 阿修罗项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2251 | 夜叉项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2255 | 龙王戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2258 | 焰魔召唤术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2259 | 焰魔召唤术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2264 | 污染的苦胆 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2265 | 大老鼠血 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2266 | 研究结果样本 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2267 | 嗜血魔兽的心脏 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2268 | 大老鼠皮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2269 | 小苗 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2270 | 礼物箱1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2271 | 短信 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2272 | 礼物箱2 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2273 | 花苗 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2277 | 体力之铁手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2278 | 魔法之铁手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2279 | 体力之传统项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2280 | 魔法之传统项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2281 | 体力之古铜戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2282 | 魔法之古铜戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2283 | 体力之水晶魔戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2284 | 魔法之水晶魔戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2285 | 体力之六绝星环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2286 | 魔法之六绝星环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2287 | 锋利的匕首 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2288 | 准确青铜剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2289 | 速度青铜剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2290 | 体力之金项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2291 | 魔法之金项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2292 | 魔焰强解术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2293 | 魔焰强解术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2294 | 护身丸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2295 | 体力之青铜头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2296 | 准确之牛角戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2297 | 体力之牛角戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2298 | 准确之短剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2299 | 敏捷之青铜头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2300 | 祝福之青铜斧 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2301 | 祝福之半月 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2302 | 祝福之海魂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2303 | 高级准确之炼狱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2304 | 守护之无名刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2305 | 守护之血饮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2350 | 信物（红） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2351 | 信物（青） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2352 | 信物（黄） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2353 | 信物（绿） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2354 | 信物（褐） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2355 | 信物（紫） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2356 | 1周年礼物箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2787 | 龙血头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2788 | 龙血宝甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2789 | 龙血宝甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2790 | 龙血项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2791 | 龙血手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2792 | 龙血戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2793 | 龙血鞋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2794 | 玄灵天链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2795 | 玄灵魔链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2796 | 玄灵天环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2797 | 玄灵魔环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2798 | 玄灵天戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2799 | 玄灵魔戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2800 | 青龙原灵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2801 | 朱雀原灵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2802 | 玄武原灵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2803 | 白虎原灵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2804 | 司马血甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2805 | 司马血甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2806 | 龙魔石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2807 | 宠物道具碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2808 | 婚魔石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2809 | 青铜石手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2810 | 孔雀石手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2811 | 黑檀石手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2812 | 乌金石手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2813 | 生锈魔灵刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2814 | 火焰魔灵刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2815 | 寒气魔灵刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2816 | 霹雷魔灵刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2817 | 武林宗师的手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2818 | 猫眼石的心脏 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2819 | 玛瑙石手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2820 | 青玉石手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2821 | 水晶石手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2822 | 虎眼石手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2823 | 狂风魔灵刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2824 | 生锈魔灵枪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2825 | 火焰魔灵枪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2826 | 寒气魔灵枪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2827 | 霹雷魔灵枪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2828 | 狂风魔灵枪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2829 | 玄灵之月龙项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2830 | 玄灵之紫月项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2831 | 玄灵之月龙手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2832 | 玄灵之紫月手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2833 | 玄灵之月龙戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2834 | 玄灵之紫月戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2835 | 邪魔血刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2837 | 武林宗师牌（测试） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2900 | 体验之急救丸（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2901 | 体验之急救丸（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2902 | 体验之急救丸（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2903 | 体验之清心丸（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2904 | 体验之清心丸（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2905 | 体验之清心丸（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2908 | 造化药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2909 | GM道具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2910 | 幸运水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2911 | 幸运水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2912 | 幸运水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2913 | 幸运水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2914 | 幸运水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2915 | 魔法师神位 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2916 | 收费西沙漠传送卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2917 | 邪魔炎甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2918 | 邪魔炎甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2919 | 邪魔墨甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2920 | 邪魔墨甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2921 | 邪魔炎刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2922 | 邪魔墨刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2923 | 蓝书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2924 | 自动售货机 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2925 | 熟练之制造工具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2926 | 达人之制造工具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2927 | 名人之制造工具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2928 | 传说之制造工具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2929 | 强化护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2961 | 高级灵魂护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2962 | 高级灵魂护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2963 | 造化宝轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2964 | 铭刻经文轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2965 | 悔悟轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2966 | 金灵轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2967 | 凡灵轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2968 | 经验葫芦（30%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2969 | 经验葫芦（60%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2970 | 爆率葫芦（100%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2971 | 物品葫芦（120%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2972 | 超级冰泉圣水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2973 | 白魔光片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2974 | 红魔光片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2975 | 黑魔光片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2976 | 铁魔光片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2977 | 青魔光片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2978 | 润滑剂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2979 | 圣诞老人 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2980 | 圣诞节礼物箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2981 | 长袜子礼物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2982 | 普通牛骨剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2983 | 普通牛骨头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2987 | 龙王战靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2988 | 阿修罗战靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2989 | 夜叉战靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2990 | 火焰强玉酒（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2991 | 寒气强玉酒（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2992 | 霹雷强玉酒（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2993 | 狂风强玉酒（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2994 | 神圣强玉酒（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2995 | 暗黑强玉酒（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2996 | 幻影强玉酒（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2997 | 全效强玉酒（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2998 | 火焰强玉酒（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 2999 | 寒气强玉酒（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3000 | 霹雷强玉酒（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3001 | 狂风强玉酒（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3002 | 神圣强玉酒（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3003 | 暗黑强玉酒（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3004 | 幻影强玉酒（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3005 | 全效强玉酒（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3006 | 破气米酒（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3007 | 魔气米酒（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3008 | 灵气米酒（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3009 | 高级体练酒（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3010 | 高级魔练酒（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3011 | 狂风药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3012 | 破气米酒（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3013 | 魔气米酒（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3014 | 灵气米酒（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3015 | 高级体练酒（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3016 | 高级魔练酒（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3017 | 狂风药水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3018 | 破气米酒（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3019 | 魔气米酒（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3020 | 灵气米酒（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3021 | 高级体练酒（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3022 | 高级魔练酒（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3023 | 狂风药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3024 | 破气米酒（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3025 | 魔气米酒（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3026 | 灵气米酒（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3027 | 高级体练酒（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3028 | 高级魔练酒（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3029 | 狂风药水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3030 | 大骷髅骨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3031 | 银矿石结晶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3032 | 报恩酒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3033 | 酒灵球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3034 | 报恩盒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3065 | 赤龙城传送券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3066 | 明光咒衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3067 | 明光咒衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3068 | 赤贯道衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3069 | 赤贯道衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3070 | 经验物品葫芦（50%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3071 | 尊扬牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3072 | 夏季包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3073 | 帮派创建申请书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3074 | 召唤书_护卫武士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3075 | 召唤书_护卫左使 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3076 | 经验贮存灌（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3077 | 经验贮存灌工具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3079 | 经验贮存灌（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3080 | 经验贮存灌（中-5个） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3081 | 经验贮存灌（中-10个） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3082 | 经验贮存灌工具-重迭测试 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3087 | 群体斗转星移（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3088 | 铁布衫-强化（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3089 | 护身冰环（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3090 | 天之怒火（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3091 | 灵魂强化（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3092 | 吸气魔功（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3093 | 幻影护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3094 | 幻影护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3095 | 幻影护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3096 | 幻影护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3097 | 毒药瓶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3098 | 破坏印记（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3099 | 自然印记（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3100 | 灵魂印记（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3101 | 灰色精炼石（首饰）（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3102 | 极尊牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3103 | 泰尊牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3201 | 苹果 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3202 | 粽子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3203 | 鲭鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3204 | 肉包子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3205 | 鲜肉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3210 | 华丽的皮包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3211 | 高级木箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3212 | 宠物小头带 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3213 | 兔子头带 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3214 | 月河攻击印记（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3215 | 疾风太阳神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3216 | 自然太阳神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3217 | 灵魂太阳神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3218 | 攻击太阳神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3219 | 月河攻击强效药水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3220 | 宠物小背带 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3221 | 初级宠物背包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3222 | 意识药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3223 | 经验贮存灌（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3224 | 完整的回收 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3225 | 经验贮存灌（大-5个） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3226 | 经验贮存灌（大-10个） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3227 | 蓝色套装A | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3228 | 蓝色套装B | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3229 | 蓝色套装C | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3230 | 龙穴藏宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3231 | 高级药水套装 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3232 | 额外伤害花蜜药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3233 | 幸运油（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3235 | 回归凭证 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3236 | 破坏花蜜药水箱子（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3237 | 自然花蜜药水箱子（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3238 | 灵魂花蜜药水箱子（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3239 | 体力花蜜药水箱子（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3240 | 魔法花蜜药水箱子（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3241 | 冬季包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3242 | 宠物小红帽 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3243 | 宠物小马甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3244 | 服装染剂（白色） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3245 | 服装染剂（黑色） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3246 | 服装染剂（红色） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3247 | 服装染剂（蓝色） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3248 | 服装染剂（黄色） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3249 | 服装染剂（绿色） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3250 | 3月箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3251 | 4月箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3252 | 古代国王的密匙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3253 | 准确花蜜药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3254 | 灵魂护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3255 | 初级经验葫芦（50%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3256 | 初级疾风太阳神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3257 | 初级自然太阳神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3258 | 初级灵魂太阳神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3259 | 初级攻击太阳神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3260 | 新手破坏印记（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3261 | 新手自然印记（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3262 | 新手灵魂印记（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3263 | 准确强效药水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3264 | 准确强效药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3265 | 准确强效药水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3266 | 准确强效药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3267 | 强化药水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3268 | 强化药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3269 | 强化药水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3270 | 强化药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3271 | 强化药水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3272 | 强化药水（限量） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3273 | 8月箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3274 | 湿的武功书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3275 | 神虎手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3276 | 神虎靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3277 | 神虎戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3278 | 神虎项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3279 | 中秋箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3280 | 新手经验葫芦（50%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3281 | 额外仓库II-KEY | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3282 | 万圣节灯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3283 | 白色的刀架 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3284 | 白色的矛架 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3295 | 传奇盒30天 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3296 | 火焰宝玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3297 | 冰霜宝玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3298 | 雷神宝玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3299 | 风神宝玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3300 | 神秘的宝玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3301 | 钻石水晶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3302 | 白色打孔水晶（普通） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3303 | 白色打孔水晶（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3304 | 白色打孔水晶（稀世） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3305 | 装备打孔水晶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3306 | 宝石拆除水晶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3307 | 初级准确石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3308 | 低级准确石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3309 | 中级准确石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3310 | 高级准确石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3311 | 顶级准确石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3312 | 初级疾风石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3313 | 低级疾风石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3314 | 中级疾风石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3315 | 高级疾风石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3316 | 顶级疾风石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3317 | 初级生命石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3318 | 低级生命石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3319 | 中级生命石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3320 | 高级生命石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3321 | 顶级生命石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3322 | 初级魔法MP石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3323 | 低级魔法MP石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3324 | 中级魔法MP石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3325 | 高级魔法MP石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3326 | 最高级魔法MP石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3327 | 初级敏捷石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3328 | 低级敏捷石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3329 | 中级敏捷石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3330 | 高级敏捷石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3331 | 顶级敏捷石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3332 | 初级幸运石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3333 | 低级幸运石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3334 | 中级幸运石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3335 | 高级幸运石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3336 | 最高级幸运石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3337 | 初级生命HP玉石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3338 | 低级生命HP玉石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3339 | 中级生命HP玉石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3340 | 高级生命HP玉石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3341 | 最高级生命HP玉石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3342 | 初级魔法MP玉石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3343 | 低级魔法MP玉石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3344 | 中级魔法MP玉石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3345 | 高级魔法MP玉石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3346 | 最高级魔法MP玉石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3347 | 初级防御上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3348 | 低级防御上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3349 | 中级防御上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3350 | 高级防御上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3351 | 最高级防御上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3352 | 初级魔防下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3353 | 低级魔防下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3354 | 中级魔防下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3355 | 高级魔防下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3356 | 顶级魔防下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3357 | 初级防御下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3358 | 低级防御下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3359 | 中级防御下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3360 | 高级防御下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3361 | 顶级防御下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3362 | 初级魔防上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3363 | 低级魔防上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3364 | 中级魔防上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3365 | 高级魔防上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3366 | 最高级魔防上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3367 | ★经验葫芦（80%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3368 | 神圣的汁液 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3369 | 初级月河攻击上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3370 | 低级月河攻击上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3371 | 中级月河攻击上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3372 | 高级月河攻击上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3373 | 最高级月河攻击上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3374 | 初级月河防御上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3375 | 低级月河防御上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3376 | 中级月河防御上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3377 | 高级月河防御上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3378 | 最高级月河防御上限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3379 | 初级月河防御下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3380 | 低级月河防御下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3381 | 中级月河防御下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3382 | 高级月河防御下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3383 | 最高级月河防御下限石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3384 | 初级（技能MP减少）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3385 | 低级（技能MP减少）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3386 | 中级（技能MP减少）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3387 | 高级（技能MP减少）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3388 | 最高级（技能MP减少）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3389 | 初级（烈火剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3390 | 低级（烈火剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3391 | 中级（烈火剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3392 | 高级（烈火剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3393 | 顶级（烈火剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3394 | 初级（翔空剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3395 | 低级（翔空剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3396 | 中级（翔空剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3397 | 高级（翔空剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3398 | 最高级（翔空剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3399 | 初级（莲月剑法法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3400 | 低级（莲月剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3401 | 中级（莲月剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3402 | 高级（莲月剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3403 | 最高级（莲月剑法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3404 | 初级（十方斩）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3405 | 低级（十方斩）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3406 | 中级（十方斩）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3407 | 高级（十方斩）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3408 | 顶级（十方斩）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3409 | 初级（快刀斩马）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3410 | 低级（快刀斩马）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3411 | 中级（快刀斩马）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3412 | 高级（快刀斩马）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3413 | 顶级（快刀斩马）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3414 | 初级（火球术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3415 | 低级（火球术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3416 | 中级（火球术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3417 | 高级（火球术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3418 | 最高级（火球术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3419 | 初级（大火球）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3420 | 低级（大火球）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3421 | 中级（大火球）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3422 | 高级（大火球）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3423 | 最高级（大火球）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3424 | 初级（地狱火）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3425 | 低级（地狱火）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3426 | 中级（地狱火）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3427 | 高级（地狱火）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3428 | 最高级（地狱火）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3429 | 初级（火墙）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3430 | 低级（火墙）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3431 | 中级（火墙）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3432 | 高级（火墙）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3433 | 最高级（火墙）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3434 | 初级（爆裂火焰）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3435 | 低级（爆裂火焰）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3436 | 中级（爆裂火焰）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3437 | 高级（爆裂火焰）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3438 | 最高级（爆裂火焰）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3439 | 初级（焰天火雨）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3440 | 低级（焰天火雨）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3441 | 中级（焰天火雨）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3442 | 高级（焰天火雨）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3443 | 顶级（焰天火雨）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3444 | 初级（天之怒火）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3445 | 低级（天之怒火）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3446 | 中级（天之怒火）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3447 | 高级（天之怒火）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3448 | 最高级（天之怒火）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3449 | 初级（冰月神掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3450 | 低级（冰月神掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3451 | 中级（冰月神掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3452 | 高级（冰月神掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3453 | 最高级（冰月神掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3454 | 初级（冰月震天）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3455 | 低级（冰月震天）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3456 | 中级（冰月震天）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3457 | 高级（冰月震天）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3458 | 最高级（冰月震天）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3459 | 初级（冰咆哮）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3460 | 低级（冰咆哮）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3461 | 中级（冰咆哮）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3462 | 高级（冰咆哮）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3463 | 最高级（冰咆哮）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3464 | 初级（魄冰刺）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3465 | 低级（魄冰刺）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3466 | 中级（魄冰刺）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3467 | 高级（魄冰刺）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3468 | 最高级（魄冰刺）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3469 | 初级（霹雳掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3470 | 低级（霹雳掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3471 | 中级（霹雳掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3472 | 高级（霹雳掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3473 | 最高级（霹雳掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3474 | 初级（雷电术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3475 | 低级（雷电术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3476 | 中级（雷电术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3477 | 高级（雷电术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3478 | 顶级（雷电术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3479 | 初级（疾光电影）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3480 | 低级（疾光电影）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3481 | 中级（疾光电影）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3482 | 高级（疾光电影）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3483 | 最高级（疾光电影）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3484 | 初级（地狱雷光）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3485 | 低级（地狱雷光）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3486 | 中级（地狱雷光）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3487 | 高级（地狱雷光）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3488 | 最高级（地狱雷光）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3489 | 初级（怒神霹雳）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3490 | 低级（怒神霹雳）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3491 | 中级（怒神霹雳）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3492 | 高级（怒神霹雳）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3493 | 顶级（怒神霹雳）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3494 | 初级（天打雷劈）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3495 | 低级（天打雷劈）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3496 | 中级（天打雷劈）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3497 | 高级（天打雷劈）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3498 | 最高级（天打雷劈）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3499 | 初级（电闪雷鸣）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3500 | 低级（电闪雷鸣）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3501 | 中级（电闪雷鸣）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3502 | 高级（电闪雷鸣）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3503 | 最高级（电闪雷鸣）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3504 | 初级（风掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3505 | 低级（风掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3506 | 中级（风掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3507 | 高级（风掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3508 | 最高级（风掌）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3509 | 初级（抗拒火环）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3510 | 低级（抗拒火环）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3511 | 中级（抗拒火环）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3512 | 高级（抗拒火环）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3513 | 最高级（抗拒火环）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3514 | 初级（击风）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3515 | 低级（击风）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3516 | 中级（击风）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3517 | 高级（击风）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3518 | 最高级（击风）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3519 | 初级（风震天）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3520 | 低级（风震天）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3521 | 中级（风震天）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3522 | 高级（风震天）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3523 | 最高级（风震天）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3524 | 初级（龙卷风）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3525 | 低级（龙卷风）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3526 | 中级（龙卷风）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3527 | 高级（龙卷风）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3528 | 最高级（龙卷风）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3529 | 初级（灵魂火符）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3530 | 低级（灵魂火符）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3531 | 中级（灵魂火符）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3532 | 高级（灵魂火符）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3533 | 顶级（灵魂火符）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3534 | 初级（月魂断玉）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3535 | 低级（月魂断玉）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3536 | 中级（月魂断玉）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3537 | 高级（月魂断玉）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3538 | 最高级（月魂断玉）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3539 | 初级（月魂灵波）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3540 | 低级（月魂灵波）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3541 | 中级（月魂灵波）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3542 | 高级（月魂灵波）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3543 | 顶级（月魂灵波）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3544 | 初级（空拳刀法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3545 | 低级（空拳刀法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3546 | 中级（空拳刀法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3547 | 高级（空拳刀法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3548 | 最高级（空拳刀法）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3549 | 初级（吸星术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3550 | 低级（吸星术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3551 | 中级（吸星术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3552 | 高级（吸星术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3553 | 最高级（吸星术）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3554 | 初级（灭魂火符）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3555 | 低级（灭魂火符）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3556 | 中级（灭魂火符）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3557 | 高级（灭魂火符）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3558 | 最高级（灭魂火符）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3559 | 初级（横扫千军）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3560 | 低级（横扫千军）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3561 | 中级（横扫千军）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3562 | 高级（横扫千军）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3563 | 最高级（横扫千军）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3564 | 初级（吸气魔功）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3565 | 低级（吸气魔功）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3566 | 中级（吸气魔功）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3567 | 高级（吸气魔功）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3568 | 最高级（吸气魔功）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3569 | 初级（盛开）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3570 | 低级（盛开）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3571 | 中级（盛开）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3572 | 高级（盛开）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3573 | 最高级（盛开）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3574 | 初级（白莲）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3575 | 低级（白莲）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3576 | 中级（白莲）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3577 | 高级（白莲）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3578 | 最高级（白莲）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3579 | 初级（红莲）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3580 | 低级（红莲）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3581 | 中级（红莲）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3582 | 高级（红莲）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3583 | 最高级（红莲）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3584 | 初级（月季）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3585 | 低级（月季）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3586 | 中级（月季）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3587 | 高级（月季）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3588 | 最高级（月季）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3589 | 初级（孽报）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3590 | 低级（孽报）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3591 | 中级（孽报）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3592 | 高级（孽报）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3593 | 最高级（孽报）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3594 | 初级（狂涛涌泉）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3595 | 低级（狂涛涌泉）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3596 | 中级（狂涛涌泉）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3597 | 高级（狂涛涌泉）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3598 | 最高级（狂涛涌泉）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3599 | 初级（日闪）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3600 | 低级（日闪）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3601 | 中级（日闪）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3602 | 高级（日闪）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3603 | 最高级（日闪）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3604 | 初级（魔龙诀）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3605 | 低级（魔龙诀）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3606 | 中级（魔龙诀）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3607 | 高级（魔龙诀）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3608 | 最高级（魔龙诀）石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3609 | 霹雷弹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3610 | 火焰弹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3611 | 白冰弹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3612 | 雷电弹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3613 | 飞风弹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3614 | 暗黑弹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3615 | 幻影弹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3616 | 束缚弹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3617 | 血管的心脏 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3618 | 永龙血玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3619 | 首饰冶炼锡 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3620 | 首饰冶炼锡（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3621 | 首饰冶炼锡（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3622 | 首饰冶炼锡（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3623 | 首饰冶炼锡（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3624 | 炼制结晶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3625 | 大韩的灯火 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3626 | 首饰冶炼锡（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3631 | 螭龙的血液 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3632 | 审判司长的钥匙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3633 | 首饰冶炼守护石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3634 | 上贤的盒子（战士） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3635 | 上贤的盒子（法师） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3636 | 上贤的盒子（道士） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3637 | 上贤的盒子（刺客） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3638 | 新手技巧项链（限期） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3643 | ♣经验葫芦（80%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3654 | 副本重制卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3662 | 黑龙包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3743 | 天雷锤（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3744 | 离魂邪风（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3745 | 定身斗术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3765 | 神秘的金属雕塑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3766 | 紫水晶的精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3767 | 石榴石精华 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3768 | 钢玉石碎石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3769 | 硬玉的精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3770 | 红毒之护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3771 | 红毒之火护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3772 | 红毒之冰护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3773 | 红毒之雷护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3774 | 红毒之风护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3775 | 红毒之神圣护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3776 | 红毒之暗黑护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3777 | 红毒之幻影护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3778 | 绿毒之护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3779 | 绿毒之火护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3780 | 绿毒之冰护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3781 | 绿毒之雷护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3782 | 绿毒之风护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3783 | 绿毒之神圣护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3784 | 绿毒之暗黑护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3785 | 绿毒之幻影护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3786 | 万能符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3787 | 火万能符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3788 | 冰万能符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3789 | 雷万能符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3790 | 风万能符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3791 | 神圣万能符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3792 | 暗黑万能符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3793 | 幻影护身符（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3794 | 红毒之护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3795 | 红毒之火护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3796 | 红毒之冰护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3797 | 红毒之雷护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3798 | 红毒之风护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3799 | 红毒之神圣护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3800 | 红毒之暗黑护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3801 | 红毒之幻影护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3802 | 绿毒之护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3803 | 绿毒之火护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3804 | 绿毒之冰护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3805 | 绿毒之雷护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3806 | 绿毒之风护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3807 | 绿毒之神圣护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3808 | 绿毒之暗黑护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3809 | 绿毒之幻影护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3810 | 万能符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3811 | 火万能符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3812 | 冰万能符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3813 | 雷万能符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3814 | 风万能符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3815 | 神圣万能符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3816 | 暗黑万能符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3817 | 幻影护身符（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3818 | 红毒之护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3819 | 红毒之火护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3820 | 红毒之冰护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3821 | 红毒之雷护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3822 | 红毒之风护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3823 | 红毒之神圣护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3824 | 红毒之暗黑护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3825 | 红毒之幻影护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3826 | 绿毒之护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3827 | 绿毒之火护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3828 | 绿毒之冰护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3829 | 绿毒之雷护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3830 | 绿毒之风护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3831 | 绿毒之神圣护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3832 | 绿毒之暗黑护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3833 | 绿毒之幻影护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3834 | 万能符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3835 | 火万能符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3836 | 冰万能符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3837 | 雷万能符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3838 | 风万能符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3839 | 神圣万能符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3840 | 暗黑万能符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3841 | 幻影护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3842 | 红毒之护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3843 | 红毒之火护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3844 | 红毒之冰护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3845 | 红毒之雷护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3846 | 红毒之风护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3847 | 红毒之神圣护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3848 | 红毒之暗黑护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3849 | 红毒之幻影护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3850 | 绿毒之护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3851 | 绿毒之火护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3852 | 绿毒之冰护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3853 | 绿毒之雷护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3854 | 绿毒之风护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3855 | 绿毒之神圣护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3856 | 绿毒之暗黑护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3857 | 绿毒之幻影护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3858 | 万能符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3859 | 火万能符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3860 | 冰万能符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3861 | 雷万能符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3862 | 风万能符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3863 | 神圣万能符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3864 | 暗黑万能符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3865 | 幻影护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3881 | 无敌（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3882 | 护身法盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3883 | 护身法盾（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3884 | 传染 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3885 | 传染（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 3935 | 一个古老的月光箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4001 | 平凡的鱼竿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4010 | 姜太公的保佑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4011 | 基本的钓鱼钩 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4012 | 荧光线轴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4013 | 钓鱼初学者线轴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4014 | 诱饵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4015 | 鱼群探测器 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4016 | 加强的钓鱼钩 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4031 | 钓鱼服（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4032 | 钓鱼服（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4033 | 泸鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4034 | 黄桑鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4035 | 虾虎鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4036 | 黄鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4037 | 未鉴定法-幻殇碧陌铠（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4038 | 未鉴定法-幻殇碧陌铠（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4039 | 未鉴定龙吟戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4040 | 未鉴定慧明之杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4041 | 未鉴定天赋神剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4042 | 未鉴定万古道兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4043 | 未鉴定圣火盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4044 | 未鉴定战-幻殇碧陌铠（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4045 | 未鉴定战-幻殇碧陌铠（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4046 | 未鉴定幻陌盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4047 | 未鉴定刺客-银月泣影甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4048 | 未鉴定刺客-银月泣影甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4049 | 未鉴定道-幻殇碧陌铠（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4050 | 未鉴定道-幻殇碧陌铠（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4055 | 海星 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4056 | 贝壳 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4057 | 水草 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4073 | 回生神水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4074 | 小天使头带 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4075 | 小兔子发带 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4076 | 天使的翅膀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4077 | 罕见的红色鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4078 | 罕见的蓝色鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4079 | 小天使头带（1日） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4080 | 天使的翅膀（1日） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4081 | 小兔子发带（1日） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4082 | 小龙虾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4083 | 内功IP恢复药水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4084 | 内功IP恢复药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4085 | 内功IP恢复药水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4086 | 内功IP恢复药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4087 | 内功IP恢复药水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4361 | 设计师的密匙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4362 | 未知的项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4363 | 未知的手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4364 | 未知的戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4365 | 月光镜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4366 | 月光轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4367 | 月光环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4368 | 空破斩（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4369 | 联雷击（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4370 | 暗鬼阵（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4372 | 赤龙门主袍（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4373 | 赤龙门主袍（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4374 | 移花接木-强化（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4375 | 电闪雷鸣-强化（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4376 | 阴阳法环-强化（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4378 | 龙论族的血 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4379 | 金刚石碎片（三） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4380 | 金刚石碎片（型） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4381 | 金刚石碎片（太） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4382 | 金刚石碎片（阵） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4383 | 金刚石碎片（干） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4384 | 神秘的沙子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4385 | 强盗的剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4386 | 大老鼠指甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4387 | 白马的血 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4388 | 致命的蝎子尾巴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4389 | 泰山红蛇皮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4396 | 幸运硬币 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4397 | 混沦盒子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4495 | 千年冰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4496 | 血色的千年冰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4497 | 武林补给箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4498 | 装备特殊属性修炼石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4499 | 新手武器制炼石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4500 | 新手祝福油 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4501 | 新手战士头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4502 | 新手法师头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4503 | 新手道士头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4505 | 新手旋风流星刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4506 | 新手嗜魂法杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4507 | 新手逍遥扇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4509 | 新手战士盔甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4510 | 新手战士盔甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4511 | 新手法师法衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4512 | 新手法师法衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4513 | 新手道士道衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4514 | 新手道士道衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4517 | 新手项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4518 | 新手手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4519 | 新手戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4520 | 新手靴子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4521 | 传奇宝箱（5） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4522 | 副本奖励 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4523 | 蜷腹鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4524 | 红鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4525 | 海马 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4526 | 灯笼饿鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4527 | 紫珊瑚 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4528 | 饿鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4529 | 水蛇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4530 | 毒淡鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4531 | 水甲虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4532 | 角牛的遗骸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4533 | 湖底蓝鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4534 | 归还包（通用） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4535 | 稀世武器修炼石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4631 | 幻魔盔甲盒（3日） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4672 | 赤矿石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4673 | 鸡血石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4678 | 初始化宝石（可选） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4679 | 防御精通（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4680 | 物理抵抗（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4681 | 魔法抵抗（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4686 | 虚弱化（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4687 | 灵魂共鸣（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4688 | 活体引燃（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4689 | 冰雨（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4690 | 炎狱精水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4691 | 铁块 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4736 | 半兽勇士的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4737 | 巨型多角虫力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4738 | 骷髅精灵的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4739 | 尸王的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4740 | 蚂蚁将军的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4741 | 红甲虫的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4742 | 沃玛卫士的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4743 | 邪恶钳虫的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4744 | 白野猪的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4745 | 骨鬼将的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4746 | 八角首领的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4747 | 僵尸鬼的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4748 | 吸血鬼的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4749 | 大法老的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4750 | 神鬼王的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4751 | 护法天的力量精水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4752 | 潘夜鬼将的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4753 | 疯狂魔神盗的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4754 | 黑度首将的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4755 | 霸王守卫的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4756 | 震天首将的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4757 | 诺玛突击队长的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4758 | 魔石守护神的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4759 | 灵牛鬼将的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4760 | 暗影鬼卒的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4761 | 沃玛教主的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4762 | 骷髅教主的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4763 | 触龙神的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4764 | 超级黑野猪的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4765 | 赤月恶魔的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4766 | 潘夜牛魔王的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4767 | 祖玛教主的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4768 | 霸王教主的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4769 | 震天魔神的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4770 | 火影的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4771 | 天龙窝主的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4772 | 魔王力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4773 | 金牛大将军力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4774 | 黎明女王的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4775 | 赤龙魔王的力量精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4784 | 高级武器修炼石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4785 | 石马死亡心脏 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4786 | 坐标传送符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4787 | 坐标追加宝石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4790 | 老指甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4791 | 月族的勋章 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4792 | 青岩龙的鳍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4793 | 生锈的红龙戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4794 | 武功秘籍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4795 | 水晶项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4796 | 水晶手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4797 | 桃之蓁蓁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4798 | 虎啸项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4799 | 虎啸手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4800 | 虎啸戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4801 | 点火石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4802 | 水晶原石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4803 | 红绿色的夜明珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4804 | 蓝色水晶（初级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4805 | 蓝色水晶（低级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4806 | 蓝色水晶（中级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4807 | 蓝色水晶（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4808 | 蓝色水晶（最高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4809 | 锁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4810 | 请求申请书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4891 | 破甲斩（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4892 | 尸爆术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4893 | 聚风（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4895 | 不稳定波动的碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4896 | 波动的精髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4897 | 血将令 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4898 | 将士魂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4899 | 沐水天冠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4900 | 玄云盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4902 | 舒服的羊毛帽 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4903 | 太平羊毛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4904 | 修炼药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4910 | 召唤圆木训练 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4911 | （宠物变身液）霸王教主 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4923 | 圆领袍衫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4924 | 留仙裙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4925 | 礼服（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4926 | 礼服（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4927 | 随身仓库 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4951 | 花红袍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4952 | 龙凤衣 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4953 | 异界连环明珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4955 | 中国传统婚礼礼服盒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4956 | 武器炼制增强剂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4957 | 西装 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4958 | 婚纱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4959 | 西洋婚纱礼服盒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4960 | 武器炼制增强剂（5） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4961 | （宠物变身液）熊猫酒仙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4962 | 齐天大圣甲胄（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4963 | 齐天大圣甲胄（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4964 | 齐天大圣铠甲盒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4965 | BOSS探测符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4968 | 火焰护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4969 | 寒气护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4970 | 霹雷护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4971 | 狂风护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4972 | 神圣护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4973 | 暗黑护身符（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4974 | 火焰护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4975 | 寒气护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4976 | 霹雷护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4977 | 狂风护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4978 | 神圣护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4979 | 暗黑护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4980 | 幻影护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4981 | 普通捉马套索 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4982 | 高级捉马套索 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 4983 | 宠物金牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5007 | 空盒子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5008 | 雪人 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5009 | 雪块 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5010 | 圣诞老人帽子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5011 | 圣诞老人手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5012 | 圣诞老人鞋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5013 | 破烂人偶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5014 | 破旧人偶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5015 | 小人偶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5016 | 牛骨剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5017 | 强化牛骨剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5018 | 祈愿剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5019 | 牛骨头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5020 | 桃源盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5021 | 祈愿头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5022 | 鲜血 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5023 | 牛头 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5024 | 小牛角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5025 | 牛油 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5026 | 牛骨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5027 | 牛皮碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5028 | 牛筋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5029 | 牛排骨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5030 | 牛脆骨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5031 | 牛尾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5032 | 牛肉包子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5033 | 年糕 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5034 | 葱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5035 | 强化牛筋 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5036 | 强化牛皮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5037 | 强化牛角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5038 | 蛇骨年糕饺子汤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5039 | 牛尾汤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5040 | 右护卫绿玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5041 | 右护卫黄玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5042 | 右护卫黑玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5045 | 长袍（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5046 | 旗袍（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5047 | 第一个补给盒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5048 | 第二个补给盒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5049 | 第三个补给盒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5068 | 明感牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5069 | 甜美箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5070 | 甜蜜箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5072 | 太极 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5073 | 太极指环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5074 | 爱情棒棒糖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5075 | 爱情糖箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5077 | 黄金箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5078 | 黄金钥匙盒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5079 | 至尊牌强化秘籍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5080 | 至尊牌抽奖券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5081 | 至尊牌强化抽奖券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5082 | 强化至尊牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5083 | 黄金钥匙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5084 | 白夜珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5085 | 暑期活动奖券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5086 | 不稳定的干将宝玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5087 | 干将宝玉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5088 | 干将秘典 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5137 | 顿悟之牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5138 | 申请复职 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5139 | 大赦证（结束） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5140 | 经验火炬（10） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5141 | 报恩之星（中秋） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5142 | 幸运油（中秋） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5143 | 额外伤害花蜜药水（中秋） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5144 | （九）中秋节礼物箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5145 | 中秋礼品盒兑换券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5146 | 带纱的红色帽子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5147 | 一条红色的披肩 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5148 | 一个小冰球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5149 | （活动）雪人娃娃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5150 | 红参精华 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5151 | 酒票兑换券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5153 | 药丸（150000） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5154 | 香喷喷的年糕汤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5156 | 新年交换券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5161 | 经验火炬（5） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5162 | 钓鱼兑换道具套装 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5163 | 父亲礼包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5164 | 升级礼包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5165 | 虎王手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5166 | 桃源靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5167 | 虎王戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5168 | 虎王项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5240 | 黄金钓鱼箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5241 | 垂钓者的专业工具箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5242 | 钓鱼专用线轴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5243 | 钓鱼专用鱼饵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5244 | 钓鱼专用探测器 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5245 | 钓鱼专用高级鱼漂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5246 | 鱼粥（泸鱼） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5247 | 鱼粥（黄鱼） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5248 | 姜太公的鱼竿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5260 | 强化试剂（赤） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5261 | 强化试剂（靑） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5262 | 特别将券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5263 | 支持信 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5627 | 红色的帽子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5628 | 红色的披肩 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5629 | 一个小雪球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5630 | 召唤券（精灵猫） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5631 | 鲁道夫召唤号角 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5632 | 小雪人 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5634 | 流氓兔（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5635 | 流氓兔（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5636 | 法师幻魔盔甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5637 | 法师幻魔盔甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5638 | 道士幻魔盔甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5639 | 道士幻魔盔甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5640 | 龙吟战甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5641 | 龙吟战甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5642 | 传奇御史牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5643 | 新年感恩箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5657 | 兔子腿项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5658 | 兔子腿戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5659 | 兔子腿手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5660 | 幸运的兔腿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5661 | 三叶草 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5662 | 四叶草 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5684 | 疾风太阳神水包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5685 | 自然太阳神水包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5686 | 灵魂太阳神水包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5687 | 攻击太阳神水包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5701 | 惠氏的盒子（银） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5702 | 惠氏的盒子（铜） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5703 | 木刻的鱼竿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5704 | 神奇的果实 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5705 | 活力的果实 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5715 | 花束 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5716 | 家和万事兴（家） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5717 | 家和万事兴（和） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5718 | 家和万事兴（万） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5719 | 家和万事兴（事） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5720 | 家和万事兴（兴） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5721 | 祝愿的鞭炮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5722 | 希望的爆竹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5723 | 曼鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5724 | 钓鱼竿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5726 | 姜太公的祝福 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5728 | 地下城洞口传送卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5738 | 幻魔盔甲盒（1日） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5739 | 祝福盒（银） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5740 | 祝福盒（铜） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5741 | 红毒之护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5742 | 红毒之火护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5743 | 红毒之冰护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5744 | 红毒之雷护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5745 | 红毒之风护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5746 | 红毒之神圣护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5747 | 红毒之暗黑护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5748 | 红毒之幻影护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5749 | 绿毒之护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5750 | 绿毒之火护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5751 | 绿毒之冰护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5752 | 绿毒之雷护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5753 | 绿毒之风护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5754 | 绿毒之神圣护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5755 | 绿毒之暗黑护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5756 | 绿毒之幻影护身符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5757 | 万能符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5758 | 火之万能符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5759 | 冰之万能符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5760 | 雷之万能符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5761 | 风之万能符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5762 | 神圣之万能符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5763 | 暗黑之万能符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5764 | 幻影之万能符（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5773 | 算命盒子（1日） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5774 | 算命盒子（3小时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5775 | 幻影包（1日） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5776 | 幻影包（3日） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5777 | 书本籍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5778 | 打孔盒子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5790 | 田蜜的箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5791 | 田蜜的巧克力棒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5792 | 返回包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5793 | 无限的盒子（回归） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5794 | 可疑的箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5795 | 华氏的钥匙串 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5796 | 1经验囊 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5797 | 500经验囊 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5798 | 惠氏的盒子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5799 | 召唤鲁道夫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5800 | 圣诞老人召唤师 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5801 | 可爱的雪人娃娃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5802 | 圣诞树种子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5803 | 圣诞礼物箱（A） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5804 | 圣诞礼物箱（B） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5805 | 圣诞礼物箱（C） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5806 | 鲁道夫的铃铛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5807 | 圣诞项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5808 | 圣诞手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5809 | 圣诞戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5811 | 冬天的密匙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5812 | 冬天的箱子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5813 | 大黑龙的祝福牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5814 | 黑龙的祝福牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5815 | 黑龙奇石（原石） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5816 | 黑龙奇石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5817 | 黑龙宝珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5818 | 桃源虎翼刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5819 | 桃源曜灵杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5820 | 桃源三焰扇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5822 | 好吃的年高汤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5823 | 一个被盗的盒子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5824 | 被盗箱子的密匙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5825 | 春天的箱子（银） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5826 | 音箱（万岁的呼声） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5827 | 潜龙的黑龙牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5828 | 雅各科的黑龙牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5829 | 卡伦斯2的黑龙牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5830 | 米尔丹的黑龙牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5831 | 传奇宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5953 | 赦免许可证 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5960 | 蓝宝石石像（中级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5969 | 黑岩龙牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5970 | 无限的盒子（一般） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5971 | 无限的盒子（英雄） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5972 | 无限的盒子（传说） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5973 | 无限的盒子（神话） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5974 | 无限的精华（一般） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5975 | 无限的精华（英雄） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5976 | 无限的精华（传说） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5977 | 无限的精华（神话） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5978 | 无限的标志（一般） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5979 | 无限的标志（英雄） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5980 | 无限的标志（传说） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5981 | 无限的标志（神话） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5982 | 旧的书籍（低级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5983 | 旧的书籍（中级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5984 | 贡献证书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5985 | 无限塔征服（一般） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5986 | 无限塔征服（英雄） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5987 | 无限塔征服（传说） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5988 | 无限塔征服（神话） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5989 | 神秘的红色油 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5990 | 神秘的蓝色油 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5991 | 青铜石药水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5992 | 无限的项链（一般） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5993 | 无限的手镯（一般） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5994 | 无限的戒指（一般） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5995 | 无限的项链（英雄） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5996 | 无限的手镯（英雄） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5997 | 无限的戒指（英雄） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5998 | 无限项链（一般） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 5999 | 无限手镯（一般） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6000 | 无限指环（一般） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6001 | Lv14师门-生命HP圣物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6002 | Lv13师门-护身神器 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6003 | Lv11师门-破坏圣物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6004 | Lv16师门-魔法MP圣物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6005 | Lv12师门-抵抗圣器 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6006 | Lv9师门-魔法圣器 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6007 | Lv7师门-固结圣器 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6008 | Lv8师门-不悔圣物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6009 | Lv6师门-龙牌圣物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6010 | Lv25师门-25级师门令牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6011 | Lv20师门-20级师门令牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6012 | Lv15师门-15级师门令牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6013 | Lv10师门-10级师门令牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6014 | Lv5师门-5级师门令牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6015 | Lv1师门-1级师门令牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6016 | 灵芝生命HP恢复药（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6017 | 灵芝生命HP恢复药（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6018 | 灵芝魔法MP恢复药（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6019 | 灵芝魔法MP恢复药（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6020 | 灵芝水仙花（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6021 | 灵芝水仙花（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6022 | Lv23师门-初出茅庐的项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6023 | Lv22师门-初出茅庐的戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6024 | Lv21师门-初出茅庐的手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6025 | Lv29师门-万人的师傅 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6026 | Lv28师门-觉醒的牌子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6027 | Lv27师门-师傅的召唤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6028 | Lv26师门-徒弟的召唤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6029 | Lv24师门-师徒的呼喊 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6030 | 禁止战场进入 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6031 | 内丹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6032 | 护身符捆 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6033 | 祝福圣水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6034 | Lv17师门-师徒的灵丹妙药 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6035 | Lv19师门-魔法MP之泉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6036 | Lv18师门-生命HP之泉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6037 | Lv30师门-鼓舞士气 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6038 | 助力书（临时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6039 | 八门金锁阵（门票） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6040 | 芋头汤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6042 | 流浪礼物箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6043 | 栗子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6051 | 门派庄园（千寿园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6052 | 门派庄园（千花园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6053 | 门派庄园（怡和园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6054 | 门派庄园（光华园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6055 | 门派庄园（阳明园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6056 | 门派庄园（震儒园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6057 | 门派庄园（圣火园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6058 | 门派庄园（圣日园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6059 | 门派庄园（珍味园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6060 | 门派庄园（纪昌园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6061 | 门派庄园（沧浪园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6062 | 门派庄园（圆明园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6063 | 门派庄园（年兆园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6064 | 门派庄园（鉴修园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6065 | 门派庄园（清天园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6066 | 门派庄园（万柳园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6067 | 门派庄园（儒家园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6068 | 门派庄园（散士园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6069 | 门派庄园（神机园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6070 | 门派庄园（花香园）邀请劵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6071 | 庄园蘑菇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6072 | 雪人娃娃（雪白） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6073 | 雪人娃娃（群吸） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6074 | 雪人娃娃（恢复） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6075 | 无限项链（英雄） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6076 | 无限手镯（英雄） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6077 | 无限戒指（英雄） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6078 | 无限的精华（Lv1） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6079 | 无限的精华（Lv2） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6080 | 无限的精华（Lv3） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6081 | 无限的精华（Lv4） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6082 | 无限的精华（Lv5） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6083 | 无限的精华（Lv6） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6084 | 无限的精华（Lv7） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6085 | 无限的精华（Lv8） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6086 | 无限的精华（Lv9） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6087 | 无限的精华（Lv10） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6088 | 文昌帝君医书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6094 | 圣诞老人的礼物箱（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6095 | 圣诞服（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6096 | 圣诞服（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6098 | 圣诞袜子（一般） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6099 | 红色装饰球（初级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6100 | 红色装饰球（低级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6101 | 红色装饰球（中级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6102 | 红色装饰球（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6103 | 红色装饰球（最高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6104 | 绿色装饰球（初级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6105 | 绿色装饰球（低级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6106 | 绿色装饰球（中级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6107 | 绿色装饰球（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6108 | 绿色装饰球（最高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6109 | 黄色装饰球（初级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6110 | 黄色装饰球（低级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6111 | 黄色装饰球（中级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6112 | 黄色装饰球（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6113 | 黄色装饰球（最高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6114 | 召唤鲁道夫（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6115 | 圣诞老人的衣服 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6116 | 幸运硬币（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6117 | 新手攻击强效药水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6118 | 新手疾风强效药水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6119 | 新手体力强效药水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6120 | 新手攻击强效药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6121 | 新手自然强效药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6122 | 新手灵魂强效药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6123 | 新手疾风强效药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6124 | 新手体力强效药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6125 | 新手魔法强效药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6126 | 新手攻击强效药水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6127 | 新手自然强效药水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6128 | 新手灵魂强效药水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6129 | 新手疾风强效药水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6130 | 新手体力强效药水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6131 | 新手魔法强效药水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6132 | 新手攻击强效药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6133 | 新手自然强效药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6134 | 新手灵魂强效药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6135 | 新手疾风强效药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6136 | 新手体力强效药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6137 | 新手魔法强效药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6138 | 新手经验葫芦（10%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6139 | 新手疾风太阳神水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6140 | 新手自然太阳神水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6141 | 新手灵魂太阳神水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6142 | 新手攻击太阳神水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6143 | 新手经验葫芦（20%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6144 | 新手疾风太阳神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6145 | 新手自然太阳神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6146 | 新手灵魂太阳神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6147 | 新手攻击太阳神水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6148 | 新手经验葫芦（30%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6149 | 新手疾风太阳神水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6150 | 新手自然太阳神水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6151 | 新手灵魂太阳神水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6152 | 新手攻击太阳神水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6153 | 新手经验葫芦（40%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6154 | 新手疾风太阳神水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6155 | 新手自然太阳神水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6156 | 新手灵魂太阳神水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6157 | 新手攻击太阳神水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6273 | 马如游龙（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6274 | 跃马重系（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6379 | 一本古老炼金术书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6380 | 韩纸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6381 | 铸造模具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6382 | 火山灰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6383 | 火焰光环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6384 | 锻造锤子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6385 | 燃烧的圣火 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6390 | （新）夏季包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6395 | 召唤券（地狱炎魔） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6396 | 珠宝（普通） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6397 | 珠宝（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6398 | 珠宝（稀释） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6399 | 武器碎片（一般） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6400 | 武器碎片（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6401 | 武器碎片（稀释） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6402 | 红色魔法精水（初级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6403 | 红色魔法精水（低级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6404 | 红色魔法精水（中级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6405 | 红色魔法精水（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6406 | 红色魔法精水（最高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6407 | 红色魔法精水（稀释） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6408 | 蓝色魔法精水（初级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6409 | 蓝色魔法精水（低级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6410 | 蓝色魔法精水（中级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6411 | 蓝色魔法精水（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6412 | 蓝色魔法精水（最高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6413 | 蓝色魔法精水（稀释） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6414 | 黄色魔法精水（初级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6415 | 黄色魔法精水（低级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6416 | 黄色魔法精水（中级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6417 | 黄色魔法精水（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6418 | 黄色魔法精水（最高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6419 | 黄色魔法精水（稀释） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6420 | 海水珍珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6421 | （新）冬季包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6424 | 龙雀开山钺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6425 | 熔金落日刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6426 | 奕天破邪杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6427 | 龙破沧溟 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6428 | 秋水无痕剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6429 | 天雷真火扇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6430 | 碎情雾影环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6431 | 天星耀阳环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6432 | 未知的战士武器（稀释） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6433 | 未知的法师武器（稀释） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6434 | 未知的道士武器（稀释） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6435 | 未知的刺客武器（稀释） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6436 | 生锈的铜戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6437 | 新手经验葫芦（300%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6466 | 请铁锭 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6467 | 龙鳞神魔的心脏 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6468 | 斗宿（斗宿）珠子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6469 | 贪欲（贪狼）心脏 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6470 | 天玑（天玑）珠子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6471 | 天玑（天玑）脑髓 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6472 | 红色的布料 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6473 | 绿色的布料 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6474 | 兔肉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6475 | 鸭肉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6481 | （新）幸运包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6502 | （新）将状包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6504 | （新）黑龙包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6506 | 梦幻纪念牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6517 | 御剑术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6518 | 御剑术-强化（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6519 | 御剑术-奥义（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6520 | 龙旋风（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6521 | 龙旋风-强化（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6522 | 龙旋风-奥义（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6523 | 僵尸召唤术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6524 | 僵尸召唤术-强化（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6525 | 僵尸召唤术-奥义（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6535 | 转职（战士） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6536 | 转职（法师） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6537 | 转职（道士） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6538 | 转职（刺客） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6557 | 雪原老虎（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6558 | 雪原老虎（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6559 | 雪原小熊（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6560 | 雪原小熊（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6574 | 黄金骨头 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6575 | 上级武器制作书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6576 | 福实的毛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6577 | 堕落的碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6578 | 雪原老虎的服装盒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6579 | 雪原高美的服装盒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6580 | 碎片仓库包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6581 | 单身铜币 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6582 | 战宠经验药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6583 | 战宠经验药水（60） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6584 | 足球狂姜太公 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6585 | 应援道具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6586 | 梦幻牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6587 | 梦幻精灵时装 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6588 | 梦幻精石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6589 | 梦幻精水碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6590 | 神秘的梦幻箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6609 | 黄金鳗鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6610 | 宠物经验药水（1520） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6611 | 黄金鳗鱼（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6612 | 黄金鳗鱼（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6630 | 细工锤子（力） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6631 | 细工锤子（风） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6632 | 细工锤子（火） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6633 | 细工锤子（魂） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6634 | 血花落照的晶水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6635 | 九宫云雾的晶水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6636 | 黑天暗云的晶水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6637 | 万里碧海的晶水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6638 | 失去力量的混天刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6639 | 诺玛勇士的古墓地图 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6665 | 物品葫芦（150） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6666 | 经验物品葫芦（60） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6667 | 任务立即完成卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6668 | 梦幻精水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6669 | 特殊制炼石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6672 | 强力花油（盔甲） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6688 | 幸运硬币箱（任务） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6689 | 传奇标志箱（任务） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6690 | 神秘石油箱（任务） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6691 | 青铜石药水箱（任务） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6692 | 幸运硬币（任务） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6693 | 传奇印记（任务） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6694 | 传奇硬币（任务） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6695 | 诺玛补给箱（任务） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6696 | 2020新春增益包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6697 | 新春迷宫盒（活动） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 6698 | 连接保持兑换卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7001 | 古老的武功秘籍 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7002 | 召唤战斗宠物 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7003 | 假眼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7009 | 宠物恢复药水（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7010 | 战斗宠物盔甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7011 | 战斗宠物经验 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7012 | 战斗宠物提升（战斗力） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7013 | 战斗宠物提升（护甲） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7014 | 战斗宠物觉醒药水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7015 | 战斗宠物解毒丸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7016 | 宠物恢复药水（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7017 | 宠物恢复药水（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7018 | 战斗宠物特修神水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7019 | 战斗宠物防御200 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7020 | 战斗宠物攻击提升200 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7021 | 战斗宠物护甲提升200 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7022 | 战斗宠物魔法提升200 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7023 | 战斗宠物战力提升200 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7024 | 战斗宠物防御100 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7025 | 战斗宠物攻击提升100 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7026 | 战斗宠物护甲提升100 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7027 | 战斗宠物魔法提升100 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7028 | 战斗宠物战力提升100 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7029 | 4级技能橙色丹丸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7030 | 4级技能蓝色丹丸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7031 | 4级技能绿色丹丸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7032 | 4级技能红色丹丸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7033 | 4级技能橙色任务书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7034 | 4级技能蓝色任务书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7035 | 高级技能任务书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7036 | 4级技能红色任务书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7037 | 宠物恢复药水（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7038 | 宠物恢复药水（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 7039 | 召唤强化咒书（时限） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8016 | 稀世技能任务书 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8017 | 惩罚的标志 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8018 | 首领的标志 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8019 | 铜色英雄的师祖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8020 | 讨伐的进军者 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8021 | 最后抵抗 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8576 | 腐烂的包子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8577 | 红色的包子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8578 | 月莲草 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8579 | 黑月莲草 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8580 | 刺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8581 | 爪子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8582 | 有毒的刺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8583 | 有毒的爪子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8584 | 红色的刺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8585 | 犬牙刺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8586 | 红色的毒刺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8587 | 有毒的犬牙刺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8588 | 红色的岩石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8589 | 壹颗不冷的心 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8590 | 高连木的根 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8591 | 高连木的刺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8592 | 折磨灵魂的宝石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8593 | 灵魂宝石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8594 | 堕落的月下一族的遗骨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8595 | 亡灵的刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8596 | 亡灵的长矛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8597 | 亡灵的箭 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8598 | 腐烂的蛆虫体液 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8599 | 小蝙蝠翅膀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8600 | 大蝙蝠翅膀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8601 | 硫磺蝎子尾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8602 | 坚硬的树皮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8603 | 犯人的枷锁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8604 | 堕落的心 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8605 | 铜色的深渊结晶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8606 | 怪物战利品基地31 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8607 | 怪物战利品基地32 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8608 | 怪物战利品基地33 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8609 | 怪物战利品基地34 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8610 | 怪物战利品基地35 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8611 | 怪物战利品基地36 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8612 | 怪物战利品基地37 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8613 | 怪物战利品基地38 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8614 | 怪物战利品基地39 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8615 | 怪物战利品基地40 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8616 | 顶级制造材料1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8617 | 顶级制造材料2 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8618 | 顶级制造材料3 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8619 | 顶级制造材料4 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8620 | 顶级制造材料5 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8621 | 顶级制造材料6 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8622 | 顶级制造材料7 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8623 | 顶级制造材料8 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8624 | 顶级制造材料9 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8625 | 顶级制造材料10 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8626 | 顶级制造材料11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8627 | 顶级制造材料12 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8628 | 顶级制造材料13 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8629 | 顶级制造材料14 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8630 | 顶级制造材料15 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8631 | 防氧化油 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8632 | 黑龙石溶剂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8633 | 白龙石溶剂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8634 | 甘龙石溶剂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8635 | 黑龙石（初级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8636 | 黑龙石（低级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8637 | 黑龙石（中级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8638 | 黑龙石（上级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8639 | 黑龙石（最上级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8640 | 黑龙石（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8641 | 黑龙石（最高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8642 | 白龙石（初级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8643 | 白龙石（低级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8644 | 白龙石（中级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8645 | 白龙石（上级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8646 | 白龙石（最上级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8647 | 白龙石（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8648 | 白龙石（最高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8649 | 甘龙石（初级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8650 | 甘龙石（低级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8651 | 甘龙石（中级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8652 | 甘龙石（上级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8653 | 甘龙石（最上级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8654 | 甘龙石（高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8655 | 甘龙石（最高级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 8768 | 巴拉蒙德的钥匙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 9001 | 活动制炼石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 9002 | 团队经验葫芦（30%.10%） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 9004 | 生死刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 10000 | 树根刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 11002 | 敏捷面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 11003 | 力量面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 12002 | 破荒无甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 12003 | 千雨火衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 12004 | 善极务衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 12005 | 暗影纹甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 12006 | 破荒无甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 12007 | 千雨火衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 12008 | 善极务衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 12009 | 暗影纹甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 14002 | 智慧之心 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 14003 | 预知项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 14004 | 勇气项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 14005 | 武林宗师护符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 14006 | 彗星项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 14007 | 白雪项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 15002 | 武林宗师护腕 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 15003 | 善心手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 15004 | 沃玛寺庙手链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 15005 | 硬化的皮手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 15006 | 彗星手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 15007 | 白雪手链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 15008 | 八卦护身符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16002 | 暗黑戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16003 | 光明戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16004 | 生连丸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16005 | 血统戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16006 | 矿工戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16007 | 憎恨的精神戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16008 | 武林宗师指环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16009 | 赤月戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16010 | 精炼防御戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16011 | 大师级备用戒指2 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16012 | 精炼麻痹戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16013 | 精炼复活戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 16014 | 精炼护身戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 17002 | 锋利的学徒手刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 17003 | 大师的准确手刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 17004 | 破损的大师手刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 17005 | 破损的手刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 17006 | 恐怖的祝福之爪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 17009 | 炫的白莲长刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 17010 | 炫的黑色龟甲之爪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 17011 | 飞龙剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 17012 | 毁灭之爪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18002 | 武林宗师徽章（外部） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18003 | 武林宗师徽章（内部） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18004 | 太阳射手（外部） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18005 | 太阳射手（内部） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18006 | 武林宗师的胸章 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18007 | 武林宗师的马牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18008 | 彗星守护牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18009 | 维拉的琵琶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18010 | 帝国徽章 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18011 | 情义徽章 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18012 | 卓越徽章 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18013 | 至尊徽章 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18014 | 英雄牌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 18015 | 极尊牌（英） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 20002 | 灰星碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 20003 | 绿星碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 20004 | 红星碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 20005 | 蓝星碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 50002 | HP恢复石（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 50003 | HP恢复石（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 50004 | HP恢复石（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 50005 | HP恢复石（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 50006 | MP恢复石（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 50007 | MP恢复石（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 50008 | MP恢复石（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 50009 | MP恢复石（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 50010 | 新能源（小） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 50011 | 新能源（中） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 50012 | 新能源（大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 50013 | 新能源（特） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80001 | 意识药水（3级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80002 | 意识药水（5级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80003 | 意识药水（7级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80004 | 意识药水（10级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80005 | 意识药水（11级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80006 | 意识药水（13级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80007 | 意识药水（15级） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80008 | 宠物自动粮仓券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80009 | 经验 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80010 | 游戏币 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80011 | 声望 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80012 | 贡献 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80013 | 宠物解锁券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80014 | 财富检查程序 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80015 | \[碎片\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80016 | 武器模板 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80017 | 威武的狂战之刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80018 | 不朽的法老之刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80019 | 恐怖的亡灵之刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80021 | 黄色立方体 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80022 | 蓝色立方体 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80023 | 红色立方体 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80024 | 紫色立方体 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80025 | 绿色立方体 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80026 | 灰色立方体 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80027 | 黄色的球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80028 | 蓝色的球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80029 | 红色的球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80030 | 紫色的球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80031 | 绿色的球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80032 | 灰色的球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80033 | 黄色的饰品 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80034 | 蓝色的饰品 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80035 | 红色的饰品 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80036 | 紫色的饰品 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80037 | 绿色的饰品 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80038 | 灰色的饰品 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80039 | 老哨子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80040 | 白色口哨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80041 | 珠宝（武器） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80042 | 虚空宝珠（武器） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80043 | 珠宝（精炼） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80044 | 虚空宝珠（精炼） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80045 | 珠宝（衣服） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80046 | 虚空宝珠（衣服） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80047 | 珠宝（项链） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80048 | 虚空宝珠（项链） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80049 | 珠宝（手镯） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80050 | 虚空宝珠（手镯） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80051 | 珠宝（戒指） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80052 | 虚空宝珠（戒指） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80053 | 绿毒之风护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80054 | 绿毒之神圣护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80055 | 绿毒之暗黑护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80056 | 绿毒之幻影护身符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80057 | 万能符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80058 | 万能符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80059 | 万能符（特大） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80060 | 同盟条约 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80061 | 碎片包裹扩展 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80062 | 挂机卷（1小时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80063 | 挂机卷（3小时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80064 | 宠物经验加速药水（限时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80065 | 骸骨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80066 | 江湖初出 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80067 | 新进高手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80068 | 江湖侠客 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80069 | 武林名宿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80070 | 仁义大侠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80071 | 善仁英雄 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80072 | 尊扬义侠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80073 | 英雄豪杰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80074 | 武林至尊 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80075 | 传奇盒子\[限时\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80076 | 幸运币 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80077 | 幸运护身符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80078 | 竹子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80079 | 火之道士头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80080 | 冰之道士头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80081 | 雷之道士头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80082 | 风之道士头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80083 | 神圣道士头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80084 | 暗黑道士头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80085 | 腐烂道士头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80086 | 诅咒骷髅精灵头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80087 | 腐烂骷髅头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80088 | 幸运骷髅头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80089 | 愤怒之钟（冰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80090 | 双倍经验卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80091 | 诅咒偃月 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80092 | 诅咒降魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80093 | 诅咒修罗 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80094 | 如来手镯（暗黑） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80095 | 如来手镯（幻影） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80096 | 猫眼（神圣） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80097 | 猫眼（暗黑） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80098 | 猫眼（幻影） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80099 | 毁灭手镯（冰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80100 | 毁灭手镯（雷） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80101 | 毁灭手镯（风） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80102 | 昏暗封印（风） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80103 | 昏暗封印（雷） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80104 | 昏暗封印（冰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80105 | 怨恨项链（暗黑） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80106 | 怨恨项链（幻影） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80107 | 雷神戒指（雷） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80108 | 雷神戒指（风） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80109 | 雷神戒指（冰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80110 | 师承戒指（幻影） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80111 | 破荒项链（幻影） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80112 | 金棱手镯（幻影） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80113 | 传奇盒子\[永久\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80114 | 幽蓝马铠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80115 | 黑金马铠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80116 | 金缕马甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80117 | 汉服\(男\) | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80118 | 汉服\(女\) | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80119 | 唐装\(男\) | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80120 | 唐装\(女\) | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80121 | 足球服\(男\) | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80122 | 足球服\(女\) | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80123 | 初级武器修炼石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80124 | 虚空宝珠（鞋子） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80125 | 虚空宝珠（头盔） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80126 | 宠物觉醒药水（限时） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80127 | 宽翅鱼衣\(男\) | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80128 | 宽翅鱼衣\(女\) | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80129 | 印记「盲盒」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80130 | BUFF药水「盲盒」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80131 | 宠物周边「盲盒」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80132 | 附魔石「盲盒」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80133 | 特殊药水「盲盒」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80134 | 碎片「盲盒」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80135 | 六色立方「盲盒」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80136 | 技能书「盲盒」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80137 | 声望贡献「盲盒」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80138 | 初学弟子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80139 | 无名之辈 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80140 | 江湖新秀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80141 | 仗剑天涯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80142 | 江湖少侠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80143 | 武林新贵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80144 | 江湖大侠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80145 | 江湖豪侠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80146 | 人海孤鸿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80147 | 人中龙凤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80148 | 名震江湖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80149 | 剑胆琴心 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80150 | 自成一派 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80151 | 一派掌门 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80152 | 威震八方 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80153 | 一代宗师 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80154 | 武林盟主 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80155 | 独孤求败 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80156 | 飘然归隐 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80157 | 笑傲江湖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80158 | 五阶民兵\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80159 | 四阶民兵\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80160 | 三阶民兵\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80161 | 二阶民兵\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80162 | 一阶民兵\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80163 | 五阶军士\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80164 | 四阶军士\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80165 | 三阶军士\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80166 | 二阶军士\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80167 | 一阶军士\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80168 | 五阶副将\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80169 | 四阶副将\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80170 | 三阶副将\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80171 | 二阶副将\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80172 | 一阶副将\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80173 | 百人将\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80174 | 牙门将\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80175 | 都尉\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80176 | 羽林中郎将\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80177 | 虎贲中郎将\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80178 | 偏将军\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80179 | 四征将军\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80180 | 骠骑将军\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80181 | 大将军\[军衔\] | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80182 | 1元红包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80183 | 2元红包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80184 | 5元红包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80185 | 10元红包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80186 | 50元红包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80187 | 100元红包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80188 | 五倍经验卷（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80189 | 十倍经验卷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80190 | 蓝莓糖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80191 | 豌豆糖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80192 | 地瓜糖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80193 | 橘子糖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80194 | 鱼子酱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80195 | 经验药水「限时」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80196 | 宝藏补品「限时」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80197 | 经验爆率补药 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80198 | 洞穴探险补品「限时」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80199 | 破坏药水「限时」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80200 | 自然药水「限时」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80201 | 灵魂药水「限时」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80202 | 生命药水「限时」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80203 | 法力药水「限时」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80204 | 疾风药水「限时」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80205 | 敏捷药水「限时」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80206 | 技能熟练药水「限时」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80207 | 幸运药水「限时」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80208 | 宠物快速收集药水「限时」 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80209 | 玄铁马甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80210 | 太阳水（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80211 | 强效太阳水（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80212 | 万年雪霜（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80213 | 意识药水（3级）（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80214 | 意识药水（5级）（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80215 | 意识药水（7级）（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80216 | 意识药水（10级）（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80217 | 意识药水（11级）（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80218 | 意识药水（13级）（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80219 | 意识药水（15级）（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80220 | 宠物经验加速药水（限时）（10倍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80221 | BOSS探查符 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80222 | 超级夜明珠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80223 | 火罐 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80224 | 宠物背带 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80225 | 宠物头带 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80226 | 袖里乾坤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80227 | 技能熟练药水「限时」（百倍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80228 | 宠物快速收集药水「限时」（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80229 | 充值礼包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80230 | 推广礼包 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80231 | 新手祝福 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80232 | 中毒免疫恢复神水 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80233 | 火桶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80234 | 木盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80235 | 铁盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80236 | 精钢盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80237 | 寒铁晶盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80238 | 四叶草 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80239 | 魔晶石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80240 | BOSS宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80242 | 快刀斩马2 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80243 | 邪恶之心 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80244 | 宠物召唤券 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80245 | 神秘时空符文 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80246 | 经验珠（50万） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80247 | 翠虎飞龙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80248 | 翠虎飞龙碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80250 | 桃之夭夭 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80251 | 桃之灼灼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80252 | 桃源之心 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80253 | 武器特殊属性修炼石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80254 | 首饰特殊属性修炼石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80255 | 武器麻痹修炼石（弃用） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80256 | 破空石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80257 | 武器神圣元素修炼石（弃用） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 80258 | 玄武盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91340 | 召唤券（田园犬） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91341 | 召唤券（机灵鼠） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91342 | 双倍经验卷（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91343 | 垂柳舞（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91344 | 潜行服\(男\) | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91345 | 潜行服\(女\) | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91346 | 入门暗杀之刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91347 | 蔓藤舞（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91348 | 磨炼（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91349 | 毒云（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91350 | 盛开（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91351 | 潜行（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91352 | 白莲（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91353 | 满月恶狼（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91354 | 亡灵束缚（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91355 | 红莲（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91356 | 烈焰（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91357 | 血禅（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91358 | 血之盟约（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91359 | 月季（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91360 | 亡灵替身（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91361 | 孽报（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91362 | 亡灵之手（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91363 | 残月之乱（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91364 | 鬼灵步（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91365 | 神机妙算（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91366 | 新月爆炎龙（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91367 | 盛开（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91368 | 心机一转（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91369 | 鹰击（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91370 | 黄泉旅者（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91371 | 狂涛涌泉（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91372 | 修罗降临（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91373 | 罗刹降临（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91374 | 深渊苦海（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91375 | 日闪（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91376 | 风之闪避（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91377 | 风之守护（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91378 | 鬼气耳爪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91379 | 夜行衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91380 | 夜行衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91381 | 速战速决宝铠（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91382 | 速战速决宝铠（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91383 | 入门暗杀面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91384 | 初级暗杀面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91385 | 高级暗杀面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91386 | 特级暗杀面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91387 | 迷雾匕首 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91388 | 诡计之衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91389 | 诡计之衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91390 | 精细诡计之衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91391 | 精细诡计之衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91392 | 黑影战袍（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91393 | 黑影战袍（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91394 | 斩首宝甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91395 | 斩首宝甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91396 | 日天战袍（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91397 | 日天战袍（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91398 | 修罗战甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91399 | 修罗战甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91400 | 烟雨宝铠（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91401 | 烟雨宝铠（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91402 | 白莲面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91403 | 玄武刺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91404 | 暗杀之刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91405 | 进化暗杀之刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91406 | 烟雨指引 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91407 | 冰之心 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91408 | 霸王刺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91409 | 复仇者面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91410 | 猎鹰面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91411 | 黑乌鸦面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91412 | 先知面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91413 | 钢铁之手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91414 | 赤色决议 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91415 | 罗刹护甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91416 | 罗刹护甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91417 | 青莲刺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91418 | 天命 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91419 | 生死轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91420 | 锋翼剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91421 | 潜龙遁甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91422 | 潜龙遁甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91423 | 死神双剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91424 | 夜叉斑盔甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91425 | 夜叉斑盔甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91426 | 凤凰轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91427 | 最后抵抗（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91428 | 神魂湮灭剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91429 | 冰龙逆天杀刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91430 | 桃源斩轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91431 | 深渊之甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91432 | 深渊之甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91433 | 黄昏手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91434 | 修罗戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91435 | 黄昏项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91436 | 暗影艺术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91437 | 新手刺客面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91438 | 新手无敌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91439 | 新手日天甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91440 | 新手日天甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91441 | 龙盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91442 | 蛇骨剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91443 | 龙吟项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91444 | 龙吟手镯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91445 | 龙吟戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91446 | 黑玉战甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91447 | 黑玉战甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91448 | 亡灵呐喊 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91449 | 垂柳舞 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91450 | 蔓藤舞 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91451 | 磨炼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91452 | 毒云 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91453 | 盛开 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91454 | 潜行 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91455 | 白莲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91456 | 满月恶狼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91457 | 亡灵束缚 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91458 | 红莲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91459 | 烈焰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91460 | 血禅 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91461 | 血之盟约 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91462 | 月季 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91463 | 亡灵替身 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91464 | 孽报 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91465 | 亡灵之手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91466 | 残月之乱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91467 | 鬼灵步 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91468 | 神机妙算 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91469 | 新月爆炎龙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91470 | 盛开 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91471 | 心机一转 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91472 | 鹰击 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91473 | 黄泉旅者 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91474 | 狂涛涌泉 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91475 | 修罗降临 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91476 | 罗刹降临 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91477 | 深渊苦海 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91478 | 日闪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91479 | 风之闪避 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 91480 | 风之守护 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95181 | 珠宝（鞋子） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95182 | 珠宝（头盔） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95184 | 慧明之杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95185 | 天赋神剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95186 | 万古道兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95187 | 血火 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95188 | 血火（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95189 | 深渊 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95190 | 深渊（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95191 | 业火 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95192 | 业火（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95193 | 集中 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95194 | 集中（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95195 | 分身术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95196 | 分身术（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95197 | 施毒大法 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95198 | 施毒大法（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95199 | 暗鬼阵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95200 | 空破斩 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95201 | 挑衅 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95202 | 挑衅（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95205 | 麒麟马甲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95206 | 马铠碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95207 | 沃玛悔悟 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95208 | 圣火盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95209 | 战-幻殇碧陌铠（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95210 | 幻世衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95211 | 龙鳞暗光盔（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95212 | 龙鳞宝刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95213 | 战-幻殇碧陌铠（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95214 | 幻世衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95215 | 幻陌盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95216 | 龙鳞暗光盔（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95217 | 凶陌圣甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95218 | 凶陌圣甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95219 | 幻世魔衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95220 | 幻世魔衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95221 | 沐水天衣（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95222 | 沐水天衣（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95223 | 玄云鸾暮铠（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95224 | 玄云鸾暮铠（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95225 | 炎狱魔神铠（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95226 | 炎狱魔神铠（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95227 | 锦绣仙袍（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95228 | 锦绣仙袍（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95229 | 刺客-银月泣影甲（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95230 | 刺客-银月泣影甲（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95231 | 道-幻殇碧陌铠（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95232 | 道-幻殇碧陌铠（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95233 | 法-幻殇碧陌铠（男） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95234 | 法-幻殇碧陌铠（女） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95235 | 冰蚕丝 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95236 | 金缕玉衣碎片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95237 | 点化石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95238 | 高级技能残片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 95239 | 稀世技能残片 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 99133 | 百花盛开 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 99134 | 百花盛开（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 99136 | 天之怒火 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 99137 | 破空斩 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 99138 | 破空斩（秘籍） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 99139 | 暗夜艺术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 99140 | 新手关怀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 99141 | 快乐加倍丸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 110836 | 天雷锤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 110837 | 暗影艺术 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 122538 | 十倍经验卷（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 122539 | 经验爆率补药（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 物品 | 122540 | 爆率葫芦（1000%）（绑定） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10001 | 鸡 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10002 | 猪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10003 | 鹿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10004 | 牛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10005 | 羊 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10006 | 多钩猫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10007 | 狼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10008 | 森林雪人 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10009 | 栗子树 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10010 | 食人花 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10011 | 半兽战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10012 | 虎蛇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10013 | 毒蜘蛛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10014 | 稻草人 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10015 | 半兽人 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10016 | 多角虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10017 | 猎鹰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10018 | 威思尔小虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10019 | 盔甲虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10020 | 山洞蝙蝠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10021 | 掷斧骷髅 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10022 | 蝎子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10023 | 骷髅战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10024 | 骷髅 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10025 | 骷髅战将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10026 | 盔甲蚂蚁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10027 | 蚂蚁战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10028 | 蚂蚁道士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10029 | 爆毒蚂蚁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10030 | 洞蛆 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10032 | 老道僵尸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10033 | 僧侣僵尸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10034 | 僵尸2 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10035 | 僵尸3 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10036 | 僵尸4 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10037 | 多脚虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10038 | 蜘蛛娃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10039 | 胞眼虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10041 | 浪子人鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10042 | 腐蚀人鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10043 | 骷髅弓箭手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10044 | 骷髅武士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10045 | 骷髅武将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10046 | 骷髅士兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10047 | 诺玛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10048 | 诺玛法老 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10049 | 诺玛将士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10050 | 沙漠鱼魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10051 | 沙漠石人 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10052 | 沙漠风魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10053 | 沙漠树魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10054 | 暗黑战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10055 | 粪虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10056 | 沃玛战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10057 | 火焰沃玛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10058 | 角蝇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10059 | 蝙蝠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10060 | 楔蛾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10061 | 红野猪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10062 | 蝎蛇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10063 | 黑野猪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10064 | 跳跳蜂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10065 | 蜈蚣 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10066 | 钳虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10067 | 蝴蝶虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10068 | 黑色恶蛆 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10069 | 月魔蜘蛛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10070 | 幻影蜘蛛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10071 | 爆裂蜘蛛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10072 | 血巨人 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10073 | 血金刚 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10074 | 花色蜘蛛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10075 | 黑角蜘蛛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10076 | 祖玛弓箭手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10077 | 祖玛雕像 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10078 | 祖玛卫士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10079 | 大老鼠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10080 | 潘夜战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10081 | 潘夜冰魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10082 | 潘夜右护卫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10083 | 潘夜云魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10084 | 潘夜左护卫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10085 | 潘夜风魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10086 | 潘夜火魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10087 | 东魔神怪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10088 | 猿猴战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10089 | 猿猴战将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10090 | 巨象兽 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10091 | 西魔神怪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10092 | 亡灵武士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10093 | 亡灵弓箭手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10094 | 亡灵士兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10098 | 黑度紫红女神 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10099 | 黑度绿荫女神 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10100 | 武力神将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10101 | 犬猴魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10102 | 轻甲守卫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10103 | 爆毒神魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10104 | 神舰守卫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10105 | 触角神魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10106 | 恶形鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10107 | 海神将领 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10108 | 红衣法师 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10109 | 异界之门 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10110 | 地牢紫红女神 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10111 | 石像狮子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10112 | 武力魔神将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10113 | 火焰狮子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10143 | 变异刺骨蜥 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10144 | 变异迅猛蜥 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10145 | 变异丑蜥 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10146 | 变异毒蜥 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10147 | 魔石咆哮者 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10148 | 魔石狂热者 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10149 | 变异利爪蜥 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10160 | 地牢绿荫女神 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10222 | 黑狼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10610 | 红蛇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10611 | 半兽剑士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10612 | 半兽法师 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 10614 | 劳动蚂蚁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20001 | 半兽勇士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20002 | 巨型多角虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20003 | 骷髅精灵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20004 | 尸王 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20005 | 蚂蚁将军 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20006 | 红甲虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20007 | 沃玛卫士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20008 | 邪恶钳虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20009 | 白野猪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20010 | 骨鬼将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20011 | 八脚首领 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20012 | 僵尸鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20013 | 吸血鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20014 | 大法老 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20015 | 神鬼王 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20016 | 护法天 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20017 | 潘夜鬼将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20018 | 疯狂魔神盗 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20019 | 黑度首将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20020 | 霸王守卫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20021 | 震天首将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20022 | 诺玛突击队长 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 20023 | 魔石守护神 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 30001 | 沃玛教主 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 30002 | 骷髅教主 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 30003 | 触龙神 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 30004 | 超级黑野猪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 30005 | 赤月恶魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 30006 | 潘夜牛魔王 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 30007 | 祖玛教主 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 30009 | 霸王教主 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 30010 | 震天魔神 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 30011 | 地天灭王 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 30012 | 黑度魔神 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40002 | 卫士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40005 | 沙巴克城门1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40006 | 沙巴克城门2 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40007 | 沙巴克城门3 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40008 | 沙巴克城门4 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40015 | 镜像 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40017 | 变异骷髅 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40018 | 神兽 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40020 | 超强骷髅 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40023 | 炎魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40024 | 替身木偶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40029 | 苦力猪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40030 | 刺客【I】宠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40031 | 战士【I】宠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40032 | 法师【II】宠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40033 | 道士【II】宠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40034 | 战士【II】宠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40035 | 刺客【III】宠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40038 | 刺客【II】宠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40039 | 道馆卫士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40040 | 图书馆卫士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40041 | 沙漠战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40042 | 法师【I】宠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 40043 | 道士【I】宠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100001 | 沙巴克领主 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100003 | 昂克战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100004 | 僧侣僵尸0 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100005 | 尸王0 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100006 | 七点白蛇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100007 | 千年毒蛇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100008 | 超级沃玛教主1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100009 | 超级骷髅教主1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100010 | 超级触龙神1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100011 | 超级黑猪王1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100012 | 超级赤月恶魔1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100013 | 超级潘夜牛魔王1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100014 | 超级祖玛教主1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100015 | 超级霸王教主1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100016 | 超级震天魔神1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100017 | 超级地天灭王1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100018 | 超级黑度魔神1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100019 | 超级诺玛教主1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100020 | 半兽勇士11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100021 | 半兽人11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100022 | 半兽战士11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100023 | 半兽剑士11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100024 | 半兽法师11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100025 | 骷髅精灵11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100026 | 掷斧骷髅11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100027 | 骷髅战士11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100028 | 骷髅战将11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100029 | 僵尸王 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100030 | 雷电僵尸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100031 | 署箭 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100032 | 沃玛战士11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100033 | 火焰沃玛11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100034 | 沃玛勇士11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100035 | 沃玛战将11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100036 | 沃玛教主11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100037 | 暗黑战士11 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100038 | 牛老道 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100039 | 冰魂弓箭手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100040 | 魄冰女神 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100041 | 冰魂鬼武士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100042 | 冰魂鬼武将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100043 | 幽灵骑士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100044 | 冰魂鬼卒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100045 | 狼人 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100046 | 雪狼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100047 | 冰魂卫士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100048 | 野猪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100049 | 赤龙石门 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100050 | 火影 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100051 | 冰湖白魔兽 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100052 | 卫护将军 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100053 | 剑客神徒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100054 | 烈火神徒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100055 | 法术神徒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100056 | 火系士兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100057 | 冰系士兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100058 | 雷系士兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100059 | 风系士兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100060 | 玄武天王1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100061 | 青龙天王1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100062 | 朱雀天王1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100063 | 白虎天王1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100064 | 封印盒1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100065 | 魔灵神主 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100066 | 魔法师 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100067 | 血灵石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100068 | 生灵石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100069 | 魔灵石 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100070 | 蓝乃霸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100071 | 红乃霸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100072 | 熊九戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100073 | 稻草人№破坏 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100074 | 稻草人№自然 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100075 | 稻草人№灵魂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100076 | 稻草人№神圣 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100077 | 稻草人№风 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100078 | 稻草人№幻影 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100079 | 稻草人№冰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100080 | 稻草人№暗黑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100081 | 稻草人№雷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100082 | 稻草人№火 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100083 | 小老虎 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100084 | 修炼圆木桩 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100085 | 红衣舞姬 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100086 | 绿衣舞姬 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100087 | 黎明女王 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100088 | 雾影魔卒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100089 | 阎昆魔女 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100090 | 魔小将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100091 | 魔大将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100092 | 真幻鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100093 | 真幻鬼婢 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100094 | 雾影魔将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100095 | 阎昆魔君 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100096 | 东蚩尤将军1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100098 | 赤龙女王 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100099 | 赤龙魔王 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100100 | 诺玛总魔将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100101 | 诺玛装甲魔将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100102 | 诺玛少将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100103 | 诺玛法老召唤兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100104 | 诺玛司令大法师 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100106 | 诺玛卫士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100107 | 诺玛将土 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100108 | 诺玛总将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100109 | 诺玛法老召唤师 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100110 | 诺玛抛石士兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100111 | 阿龙怪1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100112 | 诺玛巡逻队长 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100113 | 诺玛阻力军 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100114 | 诺玛阻力兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100115 | 诺玛族男人 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100116 | 诺玛城教主 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100117 | 小黑龙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100118 | 蘑菇头 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100119 | 雪人 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100120 | 小红猴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100121 | 小白鸡 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100122 | 小狐狸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100123 | 大天使 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100124 | 冥血魔王 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100125 | 幽灵船长 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100126 | 异界犬猴魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100127 | 异界轻甲守卫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100128 | 异界爆毒神魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100129 | 异界神舰守卫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100130 | 异界触角神魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100131 | 异界恶形鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100132 | 异界海神将领 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100133 | 异界红衣法师 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100134 | 霸王傀儡守卫1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100135 | 黄骠马 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100136 | 的卢 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100137 | 绝影 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100138 | 赤兔马 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100139 | 西蚩尤将军1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100140 | 飞翔的鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100142 | 丛林小兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100143 | 丛林小将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100144 | 丛林武将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100145 | 鬼蜮萨满1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100146 | 白毛泼猴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100147 | 铁甲牛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100148 | 大角象 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100149 | 冰魔1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100150 | 幽蓝 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100151 | 青灵兽1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100152 | 神魔战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100153 | 神魔道士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100154 | 神魔法师 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100155 | 神魔刺客 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100156 | 砍不死 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100157 | 秋风 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100158 | 破茧成蝶 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100159 | 烧死你 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100160 | 浮云 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100161 | 飞雪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100162 | BoBo | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100163 | 小兔兔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100164 | 大鸡鸡 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100165 | 熊二 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100166 | 憋大招1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100167 | 迎客松 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100168 | 废材树 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100169 | 桃源骑兵统领1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100170 | 桃源步兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100171 | 桃源红花妖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100172 | 桃源青花妖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100173 | 桃源战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100174 | 桃源勇士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100175 | 桃源精锐 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100176 | 桃源红力士1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100177 | 桃源青力士1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100178 | 堕落火冥鸢 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100179 | 火冥鸢 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100180 | 桃源弓手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100181 | 桃源蘑菇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100182 | 桃源小绿球 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100183 | 桃源花灵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100184 | 桃源步兵1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100185 | 桃源红花妖1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100186 | 桃源青花妖1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100187 | 肥羊1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100188 | 法师【III】宠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100189 | 道士【III】宠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100190 | 战士【III】宠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100192 | 地狱炎魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100568 | 副本-赤月恶魔1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100569 | 副本-沃玛教主1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100570 | 副本-霸王教主1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100571 | 副本-震天魔神1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100572 | 副本-地天灭王1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100573 | 赤翼教主1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100574 | 蓝翼教主1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100575 | 玛珐之主1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100576 | 辣手将军1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100577 | 摧花将军1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100578 | 伯光兄1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100579 | 蓝色背刺 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100580 | 反手一刀 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100581 | 石岩射手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100582 | 经验美羊羊 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100583 | 经验小兔兔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100584 | 经验大鸡鸡 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100585 | 精灵猫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100586 | 田园犬 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100587 | 机灵鼠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100588 | 奔波儿灞 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100589 | 奔波儿灞1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100590 | 奔波儿灞2 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100591 | 灞波儿奔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100592 | 灞波儿奔1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100593 | 灞波儿奔2 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100594 | 红月教主1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100595 | 蓝月教主1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100596 | 飞羽卫1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100597 | 麋鹿1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100598 | 钻风小队 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100599 | 钻风小队2 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100600 | 沙漠蜥蜴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100601 | 沙鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100602 | 水晶傀儡 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100603 | 尘土恶魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100604 | 双尾蝎子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100605 | 嗜血鼹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100606 | 沙尘怪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100607 | 剧毒蝎子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100608 | 迷失飞鹰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100609 | 迷失沙鱼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100610 | 迷失蜥蜴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100611 | 异魔族-战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100612 | 异魔族-兵卒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100613 | 异魔族-弓手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100614 | 异魔族-骤术师 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100615 | 异魔族-百夫长 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100616 | 沙海邪魔-阿索格1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100617 | 沙漠怪兽-绿巨人1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100618 | 独眼蜘蛛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100619 | 天狼蜘蛛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100620 | 异魔族族长-丘鲛洛1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100621 | 海滨王-狂怒龙虾1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100622 | 水晶金魔像 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100623 | 水晶小玄武1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100624 | 水晶魔法狂徒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100625 | 水晶蠕虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100626 | 水晶魔像 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100627 | 水晶火虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100628 | 水晶蝙蝠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100629 | 腐朽幽灵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100630 | 腐败幽灵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100631 | 水晶长枪狂徒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100632 | 水晶守护树 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100633 | 水晶玄武 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100634 | 水晶金刚兽1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100635 | 钻地锁魂妖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100636 | 云里雾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100637 | 妖化血侍-铁罗1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100638 | 雾里云 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100639 | 黑羽教主-钺皇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100640 | 魔化-道士1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100641 | 魔气化形-魔道1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100642 | 怨魂僵尸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100643 | 血灵僵尸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100644 | 魔气大僵尸-陆江 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100645 | 僵尸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100646 | 小僵尸 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100647 | 古代坟墓-士兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100648 | 古代坟墓-矛兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100649 | 古墓士兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100650 | 古墓矛兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100651 | 古墓骑兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100652 | 古墓长矛骑兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100653 | 古墓守护士兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100654 | 古墓守护矛兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100655 | 古墓守护骑兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100656 | 古墓守护长矛骑兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100657 | 古墓护卫士兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100658 | 古墓护卫武士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100659 | 古墓土偶士兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100660 | 古墓土偶护卫武士1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100661 | 古墓主人 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100662 | 巴山虎 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100663 | 精细鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100664 | 伶俐虫 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100665 | 奔马岛-青龙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100666 | 野生黄骠马 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100667 | 野生绝影 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100668 | 野生的卢 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100669 | 野生赤兔马 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100670 | 奔马岛-金灵兽 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100671 | 奔马岛-青岩龙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100672 | 海马骑兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100673 | 海马术士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100674 | 珊瑚石头怪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100675 | 小八爪怪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100676 | 巨大蛤利 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100677 | 软甲亚纲 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100678 | 巨大蛤利1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100679 | 靑石刺鬼1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100680 | 八腕魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100681 | 八碗魔的腿 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100682 | 蛮族-死魂怪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100683 | 蛮族-石岩怪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100684 | 蛮族-邪风 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100685 | 蛮族-蝎子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100686 | 蛮族-蜥蜴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100687 | 沙漠甲蚁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100688 | 沙漠兵蚁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100689 | 沙漠治疗蚁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100690 | 沙漠猎蚁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100691 | 石岩怪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100692 | 光炎石岩怪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100693 | 是兄弟就来砍我一刀1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100694 | 龙光路守护将军-眞昌 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100695 | 龙光路守护将军-光穆 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100696 | 囚禁的魔王 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100697 | 眞炎剑魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100698 | 炎狱金刚 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100699 | 龙光路守护大将-帝释魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100700 | 纯虎 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100701 | 黄虎 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100702 | 褐虎 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100703 | 雪虎 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100704 | 黑虎 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100705 | 黑翼虎1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100706 | 白翼虎1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100707 | 虎将军1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100708 | 虎战领主 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100709 | 岛屿-巨象 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100710 | 岛屿-猿猴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100711 | 岛屿-魔神怪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100712 | 霜冻雪人 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 100713 | 邪恶毒蛇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106061 | 副本-花妖1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106062 | 副本-花怪1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106063 | 副本-猿猴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106064 | 副本-魔神怪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106065 | 副本-半兽勇士1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106066 | 副本-半兽剑客 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106067 | 副本-半兽巫师 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106068 | 副本-骷髅首领1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106069 | 副本-飞斧手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106070 | 副本-骷髅战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106071 | 副本-骷髅战将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106072 | 副本-沃玛战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106073 | 副本-火焰沃玛 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106074 | 副本-沃玛勇士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106075 | 副本-沃玛战将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106076 | 副本-百花王1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106077 | 副本-暗黑战士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106078 | 黄铜武士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106079 | 黑耀武士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106080 | 金阳武将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106081 | 银月武将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106082 | 狂牛鬼将 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106083 | 火灵牛鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106084 | 灵牛鬼将军1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106085 | 金牛大将军 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106086 | 凶恶火灵牛鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106087 | 超强骷髅弓箭手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106624 | 逃难的黑翼虎 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106625 | 逃难的白翼虎 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106626 | 逃难的虎将军 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106627 | 逃难的虎战领主1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106628 | 难民弓箭手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106629 | 精英弓箭手 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106630 | 沉鱼1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106631 | 落雁1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106632 | 羞花1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106633 | 闭月1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106634 | 红拂1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106635 | 破碎虚空小怪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106636 | 破碎虚空小怪1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106637 | 破碎虚空小怪2 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106638 | 破碎虚空小怪3 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106639 | 雪原怪兽 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106640 | 黎明教主 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106641 | 黎明铁粉1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106642 | 囚禁的魔王1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106643 | 囚禁的魔王2 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106644 | 囚禁的魔王3 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106645 | 黑风寨寨主 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106646 | 黑风寨剑客 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106647 | 黑风寨术士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106648 | 黑风寨喽啰 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106649 | 黑风寨头领1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106650 | 沙漠铁火蚁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106651 | 沙漠蚁后1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106652 | 沙漠牛头怪 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106653 | 沙漠蝮蛇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106654 | 沙漠地鼠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106655 | 沙漠黑蛇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106656 | 泰山战狼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106657 | 泰山强盗1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106658 | 泰山强盗2 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106659 | 补给品马车 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106660 | 泰山强盗3 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106661 | 泰泰大王1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106662 | 荒野首领1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106663 | 白狼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106664 | 赤狼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106665 | 丛林白虎 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106666 | 丛林黑虎 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106667 | 荒野斩决鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106668 | 荒野影软鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106669 | 荒野盲鬼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106670 | 蛮族首领1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106671 | 黑风寨宝箱 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106672 | 黑风寨精锐 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106673 | 黑风寨精锐 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106674 | 黑风寨精锐 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106675 | 远古凶兽-吞天蟒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106676 | 流窜山贼 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106677 | 流窜溃兵 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106678 | 奔马岛-独角马 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106679 | 奔马岛-白毛狮王 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106680 | 奔马岛-金毛狮王 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106681 | 奔马岛-白玉麒麟 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106682 | 鬼灵藤妖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106683 | 鬼灵恶犬 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106684 | 鬼灵恐怖撕裂 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106685 | 鬼灵断骨獠牙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106686 | 幽灵蝙蝠 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 106687 | 镇灵将军 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 怪物 | 119757 | 封印盒1 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 78 | 魔血 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 79 | 虹魔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 80 | 记忆 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 81 | 金刚 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 82 | 诺玛勇士 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 83 | 祈祷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 87 | 英雄手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 88 | 紫金环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 89 | 六棱戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 90 | 武圣之戒 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 91 | 毁灭魔链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 95 | 黑铁头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 96 | 霸龙头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 97 | 战神头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 98 | 武神之靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 99 | 屠龙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 100 | 霹雷 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 101 | 破山剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 102 | 铁轮 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 104 | 嗜魂法杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 105 | 逍遥扇 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 106 | 龙纹剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 109 | 心魔戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 110 | 虚空道环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 111 | 虎面头盔 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 112 | 仙云靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 113 | 无影靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 114 | 铁炼腕 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 115 | 气血项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 116 | 破坏项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 117 | 昏暗封印 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 118 | 怨恨项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 119 | 七彩金环 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 120 | 天机戒指 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 121 | 流星项链 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 122 | 五行神镜 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 123 | 乾坤一气 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 124 | 泰轮拂尘 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 125 | 天神法杖 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 133 | 黑皮靴子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 134 | 月光靴 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 136 | 狂风 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 137 | 行者帽 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 145 | 护身烟雨 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 146 | 天赐罗刹 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 147 | 绝世潜龙 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 162 | 沐水神兵（3转武器） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 163 | 龙血之力 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 165 | 影魅的呼唤 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 214 | 阎罗手套 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 225 | 黑暗之盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 226 | 法术护盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 227 | 风之障壁 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 228 | 坚不可摧 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 229 | 坚定风采 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 230 | 金刚之躯 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 231 | 缥缈套装 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 233 | 龙血深渊 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 234 | 泣血之刃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 235 | 神魔套装（1转首饰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 236 | 飞龙剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 237 | 飞龙剑（元素） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 238 | 桃源之盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 239 | 桃源神兵（2转武器） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 240 | 桃夭套装（2转首饰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 242 | 玄武神盾 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 243 | 龙盾之力 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 244 | 复仇者面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 245 | 猎鹰面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 246 | 黑乌鸦面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 247 | 先知面具 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 248 | 天掌靴子 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 249 | 初窥门径 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 250 | 已有小成 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 251 | 渐入佳境 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 252 | 出类拔萃 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 253 | 非同凡响 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 254 | 炉火纯青 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 255 | 臻至化境 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 256 | 超凡脱俗 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 257 | 登峰造极 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 258 | 返璞归真 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 259 | 虎啸龙吟（5转首饰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 262 | 神魔之刃（1转武器） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 263 | 神兵利刃（5转武器） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 264 | 霸龙头盔（祝福） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 265 | 死神双剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 266 | 天命 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 267 | 锋翼剑 | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 268 | 沐水仙踪（3转首饰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 269 | 玄云沙海（4转首饰） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 270 | 神魔铠甲（1转盔甲） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 271 | 桃源神铠（2转盔甲） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 272 | 沐水神铠（3转盔甲） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 273 | 玄云神铠（4转盔甲） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 274 | 虎啸龙吟神铠（5转盔甲） | - | 未在官方正式名称或显式别名中找到精确匹配 |
| 套装 | 275 | 玄海神兵（4转武器） | - | 未在官方正式名称或显式别名中找到精确匹配 |
