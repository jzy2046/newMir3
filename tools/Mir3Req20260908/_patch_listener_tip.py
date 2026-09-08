import sys
sys.stdout.reconfigure(encoding="utf-8")
# Add listener for NPC 5657
path = r"D:\newMir3\Scripts\Npc\管理中心.py"
t = open(path, encoding="utf-8").read()
if "5657" not in t:
    t = t.replace(
        'NpcEvent.add_listener(335,"OnClick",OnClick)\nNpcEvent.add_listener(134,"OnClick",OnClick)',
        'NpcEvent.add_listener(335,"OnClick",OnClick)\nNpcEvent.add_listener(134,"OnClick",OnClick)\nNpcEvent.add_listener(5657,"OnClick",OnClick)  # 道馆综合服务拷贝 20260908'
    )
    if "5657" not in t:
        # try alternate spacing
        t = t.replace(
            'NpcEvent.add_listener(134,"OnClick",OnClick)',
            'NpcEvent.add_listener(134,"OnClick",OnClick)\nNpcEvent.add_listener(5657,"OnClick",OnClick)  # 道馆综合服务拷贝 20260908'
        )
    open(path,"w",encoding="utf-8").write(t)
    print("listener 5657", "5657" in open(path,encoding="utf-8").read())
else:
    print("already has 5657")

# Tip divider: skip mid dividers for non-equipment in CreateItemLabel
# Patch both 145Client and Mobile GameScene.cs — guard AddItemLabelDivider at lines after header for non-equip
import re, shutil, os
equip_check = '''bool IsEquipmentItemType(ItemType t)
        {
            switch (t)
            {
                case ItemType.Weapon:
                case ItemType.Armour:
                case ItemType.Helmet:
                case ItemType.Necklace:
                case ItemType.Bracelet:
                case ItemType.Ring:
                case ItemType.Shoes:
                case ItemType.Shield:
                case ItemType.Torch:
                case ItemType.Fashion:
                    return true;
                default:
                    return false;
            }
        }

        '''

for gs in [
    r"D:\newMir3\Source\145Client\Scenes\GameScene.cs",
    r"D:\newMir3\Source\Mir3.Mobile\Scenes\GameScene.cs",
]:
    if not os.path.exists(gs):
        print("miss", gs); continue
    src = open(gs, encoding="utf-8").read()
    if "IsEquipmentItemType" in src:
        print("already patched", gs); continue
    # insert helper before AddItemLabelDivider method
    if "private void AddItemLabelDivider()" not in src:
        print("no divider method", gs); continue
    src = src.replace(
        "        private void AddItemLabelDivider()",
        equip_check + "        private void AddItemLabelDivider()"
    )
    # Change the mid dividers at attribute section: after durability block AddItemLabelDivider before 属性, and before 穿戴限制
    # Make CreateItemLabel skip mid dividers for non-equipment.
    # Safer approach: wrap the two mid calls (3026 and 3100 area) — use unique context
    # After first divider (header) keep it; guard subsequent ones in CreateItemLabel only via a flag.

    # Simpler: change AddItemLabelDivider to no-op when MouseItem is non-equipment — but first call is also mid-ish after header.
    # Req: 非装备 tip 不要中部分割线. Header divider after name is also a divider. "无中部分割线" = no mid divider.
    # Keep first (after name), skip later ones for non-equip.

    # Replace body of AddItemLabelDivider to accept optional / use call-site counter — too fragile.
    # Instead replace the specific mid calls with guarded versions.
    src2 = src
    # Only guard calls that appear after "#region 属性" and "#region 穿戴限制" and set item — use unique preceding lines
    src2 = src2.replace(
        """            #endregion

            AddItemLabelDivider();
            #region 属性""",
        """            #endregion

            if (IsEquipmentItemType(displayInfo.ItemType))
                AddItemLabelDivider();
            #region 属性"""
    )
    src2 = src2.replace(
        """            #endregion

            AddItemLabelDivider();
            #region 穿戴限制""",
        """            #endregion

            if (IsEquipmentItemType(displayInfo.ItemType))
                AddItemLabelDivider();
            #region 穿戴限制"""
    )
    if src2 == src:
        print("WARN context replace failed", gs)
        # fallback: make AddItemLabelDivider itself skip when non-equip — then ALSO skip header. User said 中部分割线.
        # count AddItemLabelDivider in CreateItemLabel by adding a field — skip.
    else:
        src = src2
        print("guarded mid dividers", gs)
    open(gs, "w", encoding="utf-8").write(src)
    print("wrote", gs, "IsEquipment", "IsEquipmentItemType" in src)
