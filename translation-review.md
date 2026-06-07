# RNGReporter Chinese Localization Review

请校对以下迁移或新增翻译。`safe-copy` 表示整文件来自旧汉化且目标新版未改动该文件。

## 术语基准

宝可梦专有名词优先对齐 52Poké / 神奇宝贝百科；RNG 工具术语如 `Seed`、`Frame`、`Delay`、`PID`、`SID`、`TID`、`IV` 保留社区常用写法。

- `C-Gear` -> `Ｃ装置`: https://wiki.52poke.com/wiki/%EF%BC%A3%E8%A3%85%E7%BD%AE
- `Entralink` -> `连入`, `Entree Forest` -> `连入之森`, `Pass Power` -> `释出之力`: https://wiki.52poke.com/wiki/%E8%BF%9E%E5%85%A5
- `Chatot` -> `聒噪鸟`: https://wiki.52poke.com/wiki/%E8%81%92%E5%99%AA%E9%B8%9F
- `Honey` -> `甜甜蜜`: https://wiki.52poke.com/wiki/%E7%94%9C%E7%94%9C%E8%9C%9C%EF%BC%88%E9%81%93%E5%85%B7%EF%BC%89
- `Sweet Scent` -> `甜甜香气`: https://wiki.52poke.com/wiki/%E7%94%9C%E7%94%9C%E9%A6%99%E6%B0%94%EF%BC%88%E6%8B%9B%E5%BC%8F%EF%BC%89
- `Shiny Charm` -> `闪耀护符`: https://wiki.52poke.com/wiki/%E9%97%AA%E8%80%80%E6%8A%A4%E7%AC%A6%EF%BC%88%E9%81%93%E5%85%B7%EF%BC%89
- `Celestial Tower` -> `天堂之塔`: https://wiki.52poke.com/wiki/%E5%A4%A9%E5%A0%82%E4%B9%8B%E5%A1%94

| File | Kind | English / Source | Chinese / Proposed |
| --- | --- | --- | --- |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `label20.Text` | 16/32-Bit Seed | 16/32位 Seed |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `buttonGenerate.Text` | Find | 计算 |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `Time.HeaderText` | Time | 时间 |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `Seconds.HeaderText` | Seconds | 秒数 |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `label1.Text` | This feature only works for Ruby/Sapphire with a live battery | 此功能仅适用于有电时钟的红/蓝宝石 |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `label2.Text` | Year | 年份 |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `label3.Text` | Enter a 16-bit seed | 输入16位的seed |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `label4.Text` | Or 32-bit seed for closest 16-bit match | 或32位seed，用于查找最接近的16位来匹配 |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `literal` | 16/32-Bit Seed | 16/32位 Seed |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `literal` | Find | 计算 |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `literal` | Time | 时间 |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `literal` | Seconds | 秒数 |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `literal` | This feature only works for Ruby/Sapphire with a live battery | 此功能仅适用于有电时钟的红/蓝宝石 |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `literal` | Year | 年份 |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `literal` | Enter a 16-bit seed | 输入16位的seed |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `literal` | Or 32-bit seed for closest 16-bit match | 或32位seed，用于查找最接近的16位来匹配 |
| `RNGReporter/3rdGenSeedToTime.Designer.cs` | `literal` | 16-Bit Seed to Time | Seed to Time（有电红/蓝宝石） |
| `RNGReporter/3rdGenSeedToTime.cs` | `literal` | Please enter a year between 2000 and 2037 | 请输入2000到2037之间的年份 |
| `RNGReporter/Adjacents.Designer.cs` | `copySeedToClipboardToolStripMenuItem1.Text` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/Adjacents.Designer.cs` | `generateTimesToolStripMenuItem.Text` | Generate More Times ... | 复制seed到seed to time |
| `RNGReporter/Adjacents.Designer.cs` | `generateAdjacentSeedsFrame1ToolStripMenuItem.Text` | Generate Adjacent Seeds (Frame 1) | 计算相邻的 Seeds (1帧) |
| `RNGReporter/Adjacents.Designer.cs` | `generateAdjacentSeedsToolStripMenuItem.Text` | Generate Adjacent Seeds (Current Frame) | 计算相邻的 Seeds (当前帧) |
| `RNGReporter/Adjacents.Designer.cs` | `outputCapResultsToTXTToolStripMenuItem.Text` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/Adjacents.Designer.cs` | `label2.Text` | Date\\Time | 日期\\时间 |
| `RNGReporter/Adjacents.Designer.cs` | `labelCapMonthDelay.Text` | Keypresses | 按键 |
| `RNGReporter/Adjacents.Designer.cs` | `label8.Text` | Seconds +\\- | 秒数 +\\- |
| `RNGReporter/Adjacents.Designer.cs` | `label30.Text` | Method | 算法 |
| `RNGReporter/Adjacents.Designer.cs` | `label52.Text` | Encounter Type | 相遇类型 |
| `RNGReporter/Adjacents.Designer.cs` | `label3.Text` | Chatot Pitches | 聒噪鸟音高 |
| `RNGReporter/Adjacents.Designer.cs` | `label4.Text` | Lead Ability | 主特性 |
| `RNGReporter/Adjacents.Designer.cs` | `labelMaxFrame.Text` | Max Frame | 最大帧 |
| `RNGReporter/Adjacents.Designer.cs` | `labelMinFrame.Text` | Min Frame | 最小帧 |
| `RNGReporter/Adjacents.Designer.cs` | `groupBoxConfiguration.Text` | Configuration | 基本配置 |
| `RNGReporter/Adjacents.Designer.cs` | `buttonEditProfile.Text` | Edit | 编辑 |
| `RNGReporter/Adjacents.Designer.cs` | `SeedTime.HeaderText` | Date\\Time | 日期\\时间 |
| `RNGReporter/Adjacents.Designer.cs` | `CapOffset.HeaderText` | Frame | 帧数 |
| `RNGReporter/Adjacents.Designer.cs` | `EncounterSlot.HeaderText` | Encounter Slot | 遭遇槽位 |
| `RNGReporter/Adjacents.Designer.cs` | `Shiny.HeaderText` | !!! | 异色 |
| `RNGReporter/Adjacents.Designer.cs` | `Nature.HeaderText` | Nature | 性格 |
| `RNGReporter/Adjacents.Designer.cs` | `Ability.HeaderText` | Ability | 特性 |
| `RNGReporter/Adjacents.Designer.cs` | `CapHP.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/Adjacents.Designer.cs` | `CapAtk.HeaderText` | Atk | 攻击 |
| `RNGReporter/Adjacents.Designer.cs` | `CapDef.HeaderText` | Def | 防御 |
| `RNGReporter/Adjacents.Designer.cs` | `CapSpA.HeaderText` | SpA | 特攻 |
| `RNGReporter/Adjacents.Designer.cs` | `CapSpD.HeaderText` | SpD | 特防 |
| `RNGReporter/Adjacents.Designer.cs` | `CapSpe.HeaderText` | Spe | 速度 |
| `RNGReporter/Adjacents.Designer.cs` | `Synchable.HeaderText` | Synchronized | 同步 |
| `RNGReporter/Adjacents.Designer.cs` | `buttonSeedGenerate.Text` | Generate | 计算 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Generate More Times ... | 复制seed到seed to time |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Generate Adjacent Seeds (Frame 1) | 计算相邻的 Seeds (1帧) |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Generate Adjacent Seeds (Current Frame) | 计算相邻的 Seeds (当前帧) |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Date\\Time | 日期\\时间 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Keypresses | 按键 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Seconds +\\- | 秒数 +\\- |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Method | 算法 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Encounter Type | 相遇类型 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Chatot Pitches | 聒噪鸟音高 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Lead Ability | 主特性 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Max Frame | 最大帧 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Min Frame | 最小帧 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Configuration | 基本配置 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Edit | 编辑 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Offset | 偏移 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Frame | 帧数 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Encounter Slot | 遭遇槽位 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | !!! | 异色 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Nature | 性格 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Ability | 特性 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Synchable | 同步能力 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Synchronized | 同步 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | None | 无 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | R | 雷公 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | L | 拉帝欧斯\\拉迪亚斯 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Generate | 计算 |
| `RNGReporter/Adjacents.Designer.cs` | `literal` | Adjacent Seed Tool | 相邻 Seed 工具 |
| `RNGReporter/Adjacents.cs` | `literal` | IVs (Standard Seed) | 个体值（普通的Seed） |
| `RNGReporter/Adjacents.cs` | `literal` | Eggs | 蛋 |
| `RNGReporter/Adjacents.cs` | `literal` | Wondercard | 神秘卡片 |
| `RNGReporter/Adjacents.cs` | `literal` | Wild Pokémon | 野生宝可梦 |
| `RNGReporter/Adjacents.cs` | `literal` | Wild Pokémon (Swarm) | 野生宝可梦（虫之预感） |
| `RNGReporter/Adjacents.cs` | `literal` | Wild Pokémon (Shaking Grass) | 野生宝可梦（摇动草丛） |
| `RNGReporter/Adjacents.cs` | `literal` | Wild Pokémon (Bubble Spot) | 野生宝可梦（水纹水面） |
| `RNGReporter/Adjacents.cs` | `literal` | Wild Pokémon (Cave Spot) | 野生宝可梦（卷尘地面） |
| `RNGReporter/Adjacents.cs` | `literal` | Stationary Pokémon | 定点宝可梦 |
| `RNGReporter/Adjacents.cs` | `literal` | Gift Pokémon | 礼物宝可梦 |
| `RNGReporter/Adjacents.cs` | `literal` | Larvesta Egg | 燃烧虫的蛋 |
| `RNGReporter/Adjacents.cs` | `literal` | None | 无 |
| `RNGReporter/Adjacents.cs` | `literal` | Synchronize | 同步 |
| `RNGReporter/Adjacents.cs` | `literal` | Cute Charm | 迷人之躯 |
| `RNGReporter/Adjacents.cs` | `literal` | Suction Cups | 吸盘 |
| `RNGReporter/Adjacents.cs` | `literal` | Unsupported for now. | 暂不支持。 |
| `RNGReporter/Adjacents.cs` | `literal` | Synchable | 同步能力 |
| `RNGReporter/Adjacents.cs` | `literal` | Save Output to TXT | 保存输出到 TXT |
| `RNGReporter/Adjacents.cs` | `literal` | TXT Files\|*.txt | TXT 文件\|*.txt |
| `RNGReporter/Adjacents.cs` | `literal` | Min Frame | 最小帧 |
| `RNGReporter/Adjacents.cs` | `literal` | Max Frame | 最大帧 |
| `RNGReporter/Adjacents.cs` | `literal` | This RNG handles IVs only. | 此 RNG 仅处理 IV。 |
| `RNGReporter/Adjacents.cs` | `literal` | Min Advances | 最小帧 |
| `RNGReporter/Adjacents.cs` | `literal` | Max Advances | 最大帧 |
| `RNGReporter/Adjacents.cs` | `literal` | This RNG handles natures, gender, encounter slot, and shininess only. | 此 RNG 仅处理性格、性别、遭遇槽和闪光。 |
| `RNGReporter/Adjacents.cs` | `literal` | Most Mystery Gifts use this method.  However, Mystery Gifts that can have any nature but are locked into a single gender  | 大多数神秘礼物都使用这种算法。神秘礼物宝可梦可以是任何性格，但仅限于单一性别。 |
| `RNGReporter/Adjacents.cs` | `literal` | must use the GLAN (Gender Locked, Any Nature) Wondercard method. | 必须使用GLAN（锁性别，任意性格）神秘卡片算法 |
| `RNGReporter/Adjacents.cs` | `literal` | Frames listed with a grey background are from seeds adjacent to the target. | 灰色背景的帧数是目标附近的seed |
| `RNGReporter/Adjacents.resx` | `resx:textBoxChatot.ToolTip` | A Chatot with a recorded Chatter (not its normal cry) advances the RNG<br>by 1 frame every time its call is heard on the status screen.<br>The pitch of the cry also different for each frame.  By listening<br>carefully to the pitches, it is possible to determine the current frame.<br><br>"Low" indicates a low pitch and "High" a higher pitch.  The numbers<br>in parentheses indicate slight variations in pitch that may be detectable<br>by a well-trained ear.<br><br>L = Low, ML = Mid-Low, M = Mid, MH = Mid-High, H = High | 一只聒噪鸟有一个录音后的喋喋不休（不是原本的叫声）则可以用来推进帧数<br>	每次在这只聒噪鸟的状态面板查看时，听到他发出你的录音（不用听完），则帧数+1。<br>	每一帧的叫声音高也不同。通过倾听仔细地分辨出音高，才有可能确定当前的帧数<br><br>    "Low"表示低音，"High"表示高音。这些括号内的数字表示可以听到音高的细微区别，这可能被训练有素的耳朵察觉到<br><br>    L = Low, ML = Mid-Low(中低音), M = Mid(中音), MH = Mid-High(中高音), H = High |
| `RNGReporter/CgearCalibrator.Designer.cs` | `label1.Text` | Target Seed | 目标 Seed |
| `RNGReporter/CgearCalibrator.Designer.cs` | `label2.Text` | IV Frame | IV 帧 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `btnSearch.Text` | Search | 搜索 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `label3.Text` | Target Delay | 目标 Delay |
| `RNGReporter/CgearCalibrator.Designer.cs` | `label10.Text` | HP | 觉醒力量 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `label11.Text` | Atk | 攻击 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `label12.Text` | Def | 防御 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `label13.Text` | SpA | 特攻 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `label14.Text` | SpD | 特防 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `label15.Text` | Spe | 速度 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `InfoBox.Text` | RNG Info | RNG 信息 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `WildIVs.Text` | Wild IVs | 野生 IV |
| `RNGReporter/CgearCalibrator.Designer.cs` | `Difference.HeaderText` | Difference | 差值 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `NewDelay.HeaderText` | New Delay | 新 Delay |
| `RNGReporter/CgearCalibrator.Designer.cs` | `HP.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `Atk.HeaderText` | Atk | 攻击 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `Def.HeaderText` | Def | 防御 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `SpA.HeaderText` | SpA | 特攻 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `SpD.HeaderText` | SpD | 特防 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `Spe.HeaderText` | Spe | 速度 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | Target Seed | 目标 Seed |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | IV Frame | IV 帧 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | Search | 搜索 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | Target Delay | 目标 Delay |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | RNG Info | RNG 信息 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | Wild IVs | 野生 IV |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | Difference | 差值 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | New Delay | 新 Delay |
| `RNGReporter/CgearCalibrator.Designer.cs` | `literal` | C-Gear Calibrator | Ｃ装置校准器 |
| `RNGReporter/ChainToSID.Designer.cs` | `buttonCalculate.Text` | Calculate | 计算 |
| `RNGReporter/ChainToSID.Designer.cs` | `label10.Text` | Nature | 性格 |
| `RNGReporter/ChainToSID.Designer.cs` | `label15.Text` | Spe | 速度 |
| `RNGReporter/ChainToSID.Designer.cs` | `label16.Text` | SpD | 特防 |
| `RNGReporter/ChainToSID.Designer.cs` | `label17.Text` | SpA | 特攻 |
| `RNGReporter/ChainToSID.Designer.cs` | `label18.Text` | Def | 防御 |
| `RNGReporter/ChainToSID.Designer.cs` | `label19.Text` | Atk | 攻击 |
| `RNGReporter/ChainToSID.Designer.cs` | `label20.Text` | HP | 觉醒力量 |
| `RNGReporter/ChainToSID.Designer.cs` | `label1.Text` | Ability | 特性 |
| `RNGReporter/ChainToSID.Designer.cs` | `label2.Text` | Gender / Gender Ratio | 性别比例 |
| `RNGReporter/ChainToSID.Designer.cs` | `buttonClear.Text` | Clear | 清空 |
| `RNGReporter/ChainToSID.Designer.cs` | `label3.Text` | Possibilities: | 异色概率： |
| `RNGReporter/ChainToSID.Designer.cs` | `buttonOk.Text` | OK | 确定 |
| `RNGReporter/ChainToSID.Designer.cs` | `ivs.HeaderText` | Pokemon IVs | 个体值 |
| `RNGReporter/ChainToSID.Designer.cs` | `PokemonNature.HeaderText` | Nature | 性格 |
| `RNGReporter/ChainToSID.Designer.cs` | `PokemonAbility.HeaderText` | Ability | 特性 |
| `RNGReporter/ChainToSID.Designer.cs` | `PokemonGender.HeaderText` | Gender | 性别 |
| `RNGReporter/ChainToSID.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Calculate | 计算 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Nature | 性格 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Single Ability | 只有一个特性 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Ability | 特性 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Gender / Gender Ratio | 性别比例 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Clear | 清空 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Possibilities: | 异色概率： |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | OK | 确定 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Pokemon IVs | 个体值 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Gender | 性别 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/ChainToSID.Designer.cs` | `literal` | Chain To SID | 根据连锁异色计算SID（DPPt） |
| `RNGReporter/ChainToSID.cs` | `literal` | SID Found -  | 计算出SID： |
| `RNGReporter/Controls/CheckBoxComboBox.cs` | `literal` | Search | 搜索 |
| `RNGReporter/Controls/GlassButton.cs` | `literal` | Black | 黑 |
| `RNGReporter/Controls/GlassButton.cs` | `literal` | White | 白 |
| `RNGReporter/Controls/GlassComboBox.cs` | `literal` | Black | 黑 |
| `RNGReporter/Controls/GlassComboBox.cs` | `literal` | White | 白 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `btnClearSpD.Text` | Clear | 清空 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `btnClearSpA.Text` | Clear | 清空 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `lblSpe.Text` | Spe | 速度 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `btnClearDef.Text` | Clear | 清空 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `btnClearAtk.Text` | Clear | 清空 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `lblHP.Text` | HP | 觉醒力量 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `btnClearHP.Text` | Clear | 清空 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `lblAtk.Text` | Atk | 攻击 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `lblDef.Text` | Def | 防御 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `lblSpA.Text` | SpA | 特攻 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `btnClearSpe.Text` | Clear | 清空 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `lblSpD.Text` | SpD | 特防 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `literal` | None | 无 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `literal` | E | 炎帝 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `literal` | Clear | 清空 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/Controls/IVFilters.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/Controls/SetIVs.Designer.cs` | `glassButton18.Text` | Clear | 清空 |
| `RNGReporter/Controls/SetIVs.Designer.cs` | `literal` | Clear | 清空 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label2.Text` | Min | 最小 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label3.Text` | Max | 最大 |
| `RNGReporter/DSIDWizard.Designer.cs` | `lblSeconds.Text` | Seconds | 秒数 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label8.Text` | Version | 游戏版本 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label10.Text` | HP | 觉醒力量 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label11.Text` | Atk | 攻击 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label12.Text` | Def | 防御 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label13.Text` | Speed | 速度 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label14.Text` | SpDef | 特防 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label15.Text` | SpAtk | 特攻 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label17.Text` | Minute | 分钟 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label18.Text` | Hour | 时 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label19.Text` | Date | 日期 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label25.Text` | Seconds | 秒数 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label26.Text` | DS MAC Address | DS MAC地址 |
| `RNGReporter/DSIDWizard.Designer.cs` | `buttonCalcIVs.Text` | Calculate IVs from Stats | 点我打开-个体值计算器 |
| `RNGReporter/DSIDWizard.Designer.cs` | `checkBoxRoamer.Text` | Use IVs from roaming Thundurus\\Tornadus | 使用游走雷电云/龙卷云的个体 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label1.Text` | Max | 最大 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label4.Text` | Min | 最小 |
| `RNGReporter/DSIDWizard.Designer.cs` | `checkBoxHalfSeed.Text` | First Half Only | 仅前半部分 |
| `RNGReporter/DSIDWizard.Designer.cs` | `groupBox2.Text` | Seed Encryption Variables | Seed加密变量 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label6.Text` | Language | 游戏语言 |
| `RNGReporter/DSIDWizard.Designer.cs` | `cbGxStat.Text` | Only Search Min&&Max GxStat | 仅搜索最小值和最大值之间的GxStat |
| `RNGReporter/DSIDWizard.Designer.cs` | `label5.Text` | DS Type | DS机型 |
| `RNGReporter/DSIDWizard.Designer.cs` | `checkBoxSoftReset.Text` | Soft Reset | 软复位 |
| `RNGReporter/DSIDWizard.Designer.cs` | `label100.Text` | Held Buttons | 按下的按键 |
| `RNGReporter/DSIDWizard.Designer.cs` | `buttonSearch.Text` | Search | 计算 |
| `RNGReporter/DSIDWizard.Designer.cs` | `Results.Text` | Results | 计算结果 |
| `RNGReporter/DSIDWizard.Designer.cs` | `clmnActualSeconds.HeaderText` | Actual Seconds | 实际击中秒数 |
| `RNGReporter/DSIDWizard.Designer.cs` | `buttonClose.Text` | Close Window | 关闭该窗口 |
| `RNGReporter/DSIDWizard.Designer.cs` | `btnSendTimeFinder.Text` | Send Results To Profile | 将结果发送到存档信息 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Min | 最小 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Max | 最大 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Seconds | 秒数 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Version | 游戏版本 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Speed | 速度 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | SpDef | 特防 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | SpAtk | 特攻 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Minute | 分钟 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Hour | 时 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Date | 日期 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | DS MAC Address | DS MAC地址 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Calculate IVs from Stats | 点我打开-个体值计算器 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Use IVs from roaming Thundurus\\Tornadus | 使用游走雷电云/龙卷云的个体 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | First Half Only | 仅前半部分 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Seed Encryption Variables | Seed加密变量 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Language | 游戏语言 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Only Search Min&&Max GxStat | 仅搜索最小值和最大值之间的GxStat |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | DS Type | DS机型 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | None | 无 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | R | 雷公 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | L | 拉帝欧斯\\拉迪亚斯 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Soft Reset | 软复位 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Held Buttons | 按下的按键 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Black | 黑 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | White | 白 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Black 2 | 黑2 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | White 2 | 白2 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Search | 计算 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Results | 计算结果 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Actual Seconds | 实际击中秒数 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Close Window | 关闭该窗口 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | Send Results To Profile | 将结果发送到存档信息 |
| `RNGReporter/DSIDWizard.Designer.cs` | `literal` | DS Parameter Finder | 校准DS参数计算（GEN5） |
| `RNGReporter/DSIDWizard.cs` | `literal` | Your MAC address is missing some digits.  Double-check your MAC address. | MAC 地址缺少部分数字，请再次检查 MAC 地址。 |
| `RNGReporter/DSIDWizard.cs` | `literal` | There were too many combinations of IV possibilities to accurately find your intitial seed ( | 存在太多的个体值可能性组合，因此无法准确地找到您的初始seed。 ( |
| `RNGReporter/DSIDWizard.cs` | `literal` | ) please try with a higher level Pokemon, | ) 请尝试使用更高等级的宝可梦, |
| `RNGReporter/DSIDWizard.cs` | `literal` | Too many IV Combinations | 太多个体值组合啦 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `label1.Text` | Pokémon | 宝可梦 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `label10.Text` | Level | 等级 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `label11.Text` | Nature | 性格 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `label12.Text` | Characteristic | 个性 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `label13.Text` | Spe | 速度 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `label14.Text` | SpD | 特防 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `label15.Text` | SpA | 特攻 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `label16.Text` | Def | 防御 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `label17.Text` | Atk | 攻击 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `label18.Text` | HP | 觉醒力量 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `buttonCheck.Text` | Check IVs | 计算个体 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `buttonOk.Text` | OK | 确定 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | Pokémon | 宝可梦 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | Level | 等级 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | Nature | 性格 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | Characteristic | 个性 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | Check IVs | 计算个体 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | OK | 确定 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/DSParametersIVCheck.Designer.cs` | `literal` | IV Checker | 个体计算器（GEN5） |
| `RNGReporter/DSParametersIVCheck.cs` | `literal` | The IV ranges you have listed produce a large amount of IV combinations.  It is recommended that you narrow down the IVs to avoid false positives in parameter searches. | 您输入的个体值范围产生了大量的个体值组合。建议缩小个体值的范围，以避免在参数搜索中出现误报。 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label1.Text` | Pokémon | 宝可梦 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label5.Text` | Base HP | 基础 HP |
| `RNGReporter/DexIVCheck.Designer.cs` | `label6.Text` | Base Atk | 攻击 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label2.Text` | Base Def | 防御 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label3.Text` | Base SpA | 特攻 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label4.Text` | Base SpD | 特防 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label7.Text` | Base Spe | 速度 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label8.Text` | Ability 0 | 特性0 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label9.Text` | Ability 1 | 特性1\n\n以上是宝可梦的种族值和特性\n\n左侧选择对应宝可梦则可显示 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label10.Text` | Level | 等级 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label11.Text` | Nature | 性格 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label12.Text` | Characteristic | 个性 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label13.Text` | Spe | 速度 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label14.Text` | SpD | 特防 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label15.Text` | SpA | 特攻 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label16.Text` | Def | 防御 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label17.Text` | Atk | 攻击 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label18.Text` | HP | 觉醒力量 |
| `RNGReporter/DexIVCheck.Designer.cs` | `buttonCheck.Text` | Find IVs | 计算个体 |
| `RNGReporter/DexIVCheck.Designer.cs` | `btnCgearIVs.Text` | Find C-Gear Seed by IVs | 通过 IV 查找 Ｃ装置 Seed |
| `RNGReporter/DexIVCheck.Designer.cs` | `WildIVs.Text` | Wild IVs | 野生 IV |
| `RNGReporter/DexIVCheck.Designer.cs` | `label19.Text` | Spe | 速度 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label20.Text` | SpD | 特防 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label21.Text` | SpA | 特攻 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label22.Text` | Def | 防御 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label23.Text` | Atk | 攻击 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label24.Text` | HP | 觉醒力量 |
| `RNGReporter/DexIVCheck.Designer.cs` | `InfoBox.Text` | RNG Info | RNG 信息 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label31.Text` | Target Seed | 目标 Seed |
| `RNGReporter/DexIVCheck.Designer.cs` | `label32.Text` | IV Frame | IV 帧 |
| `RNGReporter/DexIVCheck.Designer.cs` | `label33.Text` | Target Delay | 目标 Delay |
| `RNGReporter/DexIVCheck.Designer.cs` | `Difference.HeaderText` | Difference | 差值 |
| `RNGReporter/DexIVCheck.Designer.cs` | `NewDelay.HeaderText` | New Delay | 新 Delay |
| `RNGReporter/DexIVCheck.Designer.cs` | `HP.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/DexIVCheck.Designer.cs` | `Atk.HeaderText` | Atk | 攻击 |
| `RNGReporter/DexIVCheck.Designer.cs` | `Def.HeaderText` | Def | 防御 |
| `RNGReporter/DexIVCheck.Designer.cs` | `SpA.HeaderText` | SpA | 特攻 |
| `RNGReporter/DexIVCheck.Designer.cs` | `SpD.HeaderText` | SpD | 特防 |
| `RNGReporter/DexIVCheck.Designer.cs` | `Spe.HeaderText` | Spe | 速度 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Pokémon | 宝可梦 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Base HP | 基础 HP |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Base Atk | 攻击 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Base Def | 防御 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Base SpA | 特攻 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Base SpD | 特防 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Base Spe | 速度 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Ability 0 | 特性0 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Ability 1 | 特性1\n\n以上是宝可梦的种族值和特性\n\n左侧选择对应宝可梦则可显示 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Level | 等级 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Nature | 性格 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Characteristic | 个性 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Find IVs | 计算个体 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Find C-Gear Seed by IVs | 通过 IV 查找 Ｃ装置 Seed |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Wild IVs | 野生 IV |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | RNG Info | RNG 信息 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Target Seed | 目标 Seed |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | IV Frame | IV 帧 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Target Delay | 目标 Delay |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Difference | 差值 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | New Delay | 新 Delay |
| `RNGReporter/DexIVCheck.Designer.cs` | `literal` | IV Checker / Mini Dex | 个体计算器/迷你图鉴 |
| `RNGReporter/DonationBox.Designer.cs` | `buttonOk.Text` | Okay! | 好的！ |
| `RNGReporter/DonationBox.Designer.cs` | `linkLabel1.Text` | Please consider making a donation | 请考虑赞助给原作者 |
| `RNGReporter/DonationBox.Designer.cs` | `label2.Text` | via PayPal | 通过 PayPal |
| `RNGReporter/DonationBox.Designer.cs` | `literal` | Okay! | 好的！ |
| `RNGReporter/DonationBox.Designer.cs` | `literal` | Please consider making a donation | 请考虑赞助给原作者 |
| `RNGReporter/DonationBox.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/DonationBox.Designer.cs` | `literal` | via PayPal | 通过 PayPal |
| `RNGReporter/DonationBox.resx` | `resx:label1.Text` | Thanks for using RNG Reporter!  I hope you've enjoyed using it as much<br>as I've enjoyed programming it.<br><br>Please consider making a donation to support the continued development of RNG Reporter, especially if<br>it helped you build a tournament team, saved you tedious hours of soft-resetting, or allowed you<br>get that seemingly-impossible flawless shiny Pokémon.<br><br>There are many great features planned for future RNG Reporters, and with your support you'll be able to:<br>• Breed shiny eggs in Emerald<br>• Get flawless chained shinies - with a chain of 1<br>• Get flawless Colosseum\XD Pokémon on a real Gamecube or Wii<br>• Get the perfect Entralink Pokémon without trying over and over for the right nature<br>• Make your item farming with Pickup, Thief, or swirling dust spots quick and easy<br>• Manage all your different DS parameters and games with RNG profiles<br>• And much more!<br><br>NOTE: RNG Reporter will NEVER link directly to any donation sites - always to the RNG help thread on Smogon.<br>This is done to protect you from phishing attempts.<br><br>New features in this version: | 感谢您使用RNG Reporter！希望您使用它的感受和我一样，编程它的过程让我非常享受。<br><br>请考虑进行捐赠以支持RNG Reporter的持续开发，特别是如果它帮助您组建了比赛队伍、节省了您无数次繁琐的软重置时间，<br>或者让您得到了那看似不可能出现的完美闪光宝可梦。<br><br>未来的RNG Reporter计划了许多出色的新功能，您的支持将使您能够：<br>• 在《绿宝石》中培育闪光蛋<br>• 轻松获得完美的连锁闪光宝可梦——仅需连锁1次<br>• 在真实的Gamecube或Wii上获得完美的Colosseum/XD宝可梦<br>• 不再需要反复尝试即可获得完美的Entralink宝可梦<br>• 使您使用拾荒、小偷或旋风尘埃点的物品收集变得既快速又轻松<br>• 使用RNG配置文件管理所有不同的DS参数和游戏<br>• 还有更多！<br><br>注意：RNG Reporter永远不会直接链接到任何捐赠网站——它总是链接到Smogon的RNG帮助帖子。<br>这是为了保护您免受网络钓鱼攻击。<br><br>此版本的新功能包括： |
| `RNGReporter/EggParents.Designer.cs` | `labelIVRNG.Text` | IVs from RNG | 乱数获取的个体 |
| `RNGReporter/EggParents.Designer.cs` | `labelParentA.Text` | Female Parent | 母方个体 |
| `RNGReporter/EggParents.Designer.cs` | `labelParentB.Text` | Male Parent | 父方个体 |
| `RNGReporter/EggParents.Designer.cs` | `label6.Text` | Spe | 速度 |
| `RNGReporter/EggParents.Designer.cs` | `label5.Text` | SpD | 特防 |
| `RNGReporter/EggParents.Designer.cs` | `label4.Text` | SpA | 特攻 |
| `RNGReporter/EggParents.Designer.cs` | `label3.Text` | Def | 防御 |
| `RNGReporter/EggParents.Designer.cs` | `label2.Text` | Atk | 攻击 |
| `RNGReporter/EggParents.Designer.cs` | `label1.Text` | HP | 觉醒力量 |
| `RNGReporter/EggParents.Designer.cs` | `buttonOk1.Text` | OK | 确定 |
| `RNGReporter/EggParents.Designer.cs` | `buttonCancel1.Text` | Cancel | 关闭 |
| `RNGReporter/EggParents.Designer.cs` | `buttonRetrieveIVs.Text` | Get IVs from RNG | 计算乱数获取的个体 |
| `RNGReporter/EggParents.Designer.cs` | `literal` | IVs from RNG | 乱数获取的个体 |
| `RNGReporter/EggParents.Designer.cs` | `literal` | Female Parent | 母方个体 |
| `RNGReporter/EggParents.Designer.cs` | `literal` | Male Parent | 父方个体 |
| `RNGReporter/EggParents.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/EggParents.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/EggParents.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/EggParents.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/EggParents.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/EggParents.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/EggParents.Designer.cs` | `literal` | OK | 确定 |
| `RNGReporter/EggParents.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/EggParents.Designer.cs` | `literal` | Get IVs from RNG | 计算乱数获取的个体 |
| `RNGReporter/EggParents.Designer.cs` | `literal` | Display Parent IVs | 显示父母个体值 |
| `RNGReporter/EggParents.cs` | `literal` | Get IVs from IVRNG (Frame 8) | 从 IVRNG 获取 IV（第 8 帧） |
| `RNGReporter/EggParents.cs` | `literal` | Parent A | 父母A |
| `RNGReporter/EggParents.cs` | `literal` | Parent B | 父母B |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `copySeedToClipboardToolStripMenuItem1.Text` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `generateTimesToolStripMenuItem.Text` | Generate More Times ... | 复制seed到seed to time |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `generateAdjacentSeedsFrame1ToolStripMenuItem.Text` | Generate Adjacent Seeds (Frame 1) | 计算相邻的 Seeds (1帧) |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `generateAdjacentSeedsToolStripMenuItem.Text` | Generate Adjacent Seeds (Current Frame) | 计算相邻的 Seeds (当前帧) |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `outputCapResultsToTXTToolStripMenuItem.Text` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `labelMaxFrame.Text` | Max Advances | 最大帧 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `labelMinFrame.Text` | Min Advances | 最小帧 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `label3.Text` | Chatot Pitches | 聒噪鸟音高 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `label20.Text` | Year | 年份 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `label12.Text` | C-Gear Seed (Hex) | Ｃ装置 Seed (16进制) |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `label13.Text` | Nature | 性格 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `checkBoxGenderless.Text` | Genderless Target | 目标宝可梦无性别 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `label2.Text` | C-Gear Seed Frame | Ｃ装置 Seed 帧数 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `label4.Text` | Min Cluster Size | 最小集群大小 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `label5.Text` | Delay Calibration | 校准Delay |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `buttonAnyNature.Text` | Any | 任意 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `SeedTime.HeaderText` | Date\\Time | 日期\\时间 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `CSeedTime.HeaderText` | C-Gear Date\\Time | Ｃ装置日期\\时间 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `CapOffset.HeaderText` | Frame | 帧 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `Nature.HeaderText` | Nature | 性格 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `CapHP.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `CapAtk.HeaderText` | Atk | 攻击 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `CapDef.HeaderText` | Def | 防御 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `CapSpA.HeaderText` | SpA | 特攻 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `CapSpD.HeaderText` | SpD | 特防 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `CapSpe.HeaderText` | Spe | 速度 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `Keypresses.HeaderText` | Keypresses | 按键 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `buttonSeedGenerate.Text` | Search | 计算 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `groupBoxConfiguration.Text` | Configuration | 基本配置 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `buttonEditProfile.Text` | Edit | 编辑 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Generate More Times ... | 复制seed到seed to time |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Generate Adjacent Seeds (Frame 1) | 计算相邻的 Seeds (1帧) |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Generate Adjacent Seeds (Current Frame) | 计算相邻的 Seeds (当前帧) |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Max Advances | 最大帧 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Min Advances | 最小帧 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Chatot Pitches | 聒噪鸟音高 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Year | 年份 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | C-Gear Seed (Hex) | Ｃ装置 Seed (16进制) |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Nature | 性格 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Genderless Target | 目标宝可梦无性别 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | C-Gear Seed Frame | Ｃ装置 Seed 帧数 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Min Cluster Size | 最小集群大小 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Delay Calibration | 校准Delay |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Any | 任意 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Date\\Time | 日期\\时间 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | C-Gear Date\\Time | Ｃ装置日期\\时间 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Offset | 偏移 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Frame | 帧 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/EntralinkSeedSearch.Designer.cs` | `literal` | Entralink Seed Search | 连入之森Seed计算（GEN5） |
| `RNGReporter/EntralinkSeedSearch.cs` | `literal` | Any | 任意 |
| `RNGReporter/EntralinkSeedSearch.cs` | `literal` | Please select a specific list of natures. | 请选择具体的性格列表。 |
| `RNGReporter/EntralinkSeedSearch.cs` | `literal` | Year must be a value between 2000 and 2099, inclusive. | 年份必须是 2000 到 2099 之间的值（含端点）。 |
| `RNGReporter/EntralinkSeedSearch.cs` | `literal` | This seed is invalid, please verify that you have entered it correctly and try again. | 这个Seed无效，请确认您是否正确输入，并再试一次 |
| `RNGReporter/EntralinkSeedSearch.cs` | `literal` | Invalid Seed | 无效Seed |
| `RNGReporter/EntralinkSeedSearch.cs` | `literal` | Save Output to TXT | 保存输出到 TXT |
| `RNGReporter/EntralinkSeedSearch.cs` | `literal` | TXT Files\|*.txt | TXT 文件\|*.txt |
| `RNGReporter/EntralinkSeedSearch.resx` | `resx:textBoxChatot.ToolTip` | A Chatot with a recorded Chatter (not its normal cry) advances the RNG<br>by 1 frame every time its call is heard on the status screen.<br>The pitch of the cry also different for each frame.  By listening<br>carefully to the pitches, it is possible to determine the current frame.<br><br>"Low" indicates a low pitch and "High" a higher pitch.  The numbers<br>in parentheses indicate slight variations in pitch that may be detectable<br>by a well-trained ear.<br><br>L = Low, ML = Mid-Low, M = Mid, MH = Mid-High, H = High | 一只聒噪鸟有一个录音后的喋喋不休（不是原本的叫声）则可以用来推进帧数<br>	每次在这只聒噪鸟的状态面板查看时，听到他发出你的录音（不用听完），则帧数+1。<br>	每一帧的叫声音高也不同。通过倾听仔细地分辨出音高，才有可能确定当前的帧数<br><br>    "Low"表示低音，"High"表示高音。这些括号内的数字表示可以听到音高的细微区别，这可能被训练有素的耳朵察觉到<br><br>    L = Low, ML = Mid-Low(中低音), M = Mid(中音), MH = Mid-High(中高音), H = High |
| `RNGReporter/GameCube.Designer.cs` | `Shiny_Check.Text` | Shiny Only | 仅异色 |
| `RNGReporter/GameCube.Designer.cs` | `L_ball.Text` | HP | 觉醒力量 |
| `RNGReporter/GameCube.Designer.cs` | `L_sex.Text` | Gender | 性别比例 |
| `RNGReporter/GameCube.Designer.cs` | `L_ability.Text` | Ability | 特性 |
| `RNGReporter/GameCube.Designer.cs` | `copySeed.Text` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/GameCube.Designer.cs` | `outputResultsToTXTToolStripMenuItem.Text` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/GameCube.Designer.cs` | `L_search_S.Text` | Spe | 速度 |
| `RNGReporter/GameCube.Designer.cs` | `L_search_D.Text` | SpD | 特防 |
| `RNGReporter/GameCube.Designer.cs` | `L_search_C.Text` | SpA | 特攻 |
| `RNGReporter/GameCube.Designer.cs` | `L_search_B.Text` | Def | 防御 |
| `RNGReporter/GameCube.Designer.cs` | `L_search_A.Text` | Atk | 攻击 |
| `RNGReporter/GameCube.Designer.cs` | `L_search_H.Text` | HP | 觉醒力量 |
| `RNGReporter/GameCube.Designer.cs` | `L_mezapa.Text` | Nature | 性格 |
| `RNGReporter/GameCube.Designer.cs` | `status.Text` | Awaiting Command | 等待操作... |
| `RNGReporter/GameCube.Designer.cs` | `label3.Text` | Search Method | 算法 |
| `RNGReporter/GameCube.Designer.cs` | `shadowCheck.Text` | Shadows | 黑暗宝可梦 |
| `RNGReporter/GameCube.Designer.cs` | `wshMkr.Text` | Wishmkr Jirachi | Wishmkr的基拉祈 |
| `RNGReporter/GameCube.Designer.cs` | `tabPage1.Text` | Spread Finder | 搜索Seed |
| `RNGReporter/GameCube.Designer.cs` | `cancel.Text` | Cancel | 取消 |
| `RNGReporter/GameCube.Designer.cs` | `search.Text` | Search | 计算 |
| `RNGReporter/GameCube.Designer.cs` | `speClear.Text` | Clear | 清空 |
| `RNGReporter/GameCube.Designer.cs` | `spdClear.Text` | Clear | 清空 |
| `RNGReporter/GameCube.Designer.cs` | `spaClear.Text` | Clear | 清空 |
| `RNGReporter/GameCube.Designer.cs` | `defClear.Text` | Clear | 清空 |
| `RNGReporter/GameCube.Designer.cs` | `atkClear.Text` | Clear | 清空 |
| `RNGReporter/GameCube.Designer.cs` | `hpClear.Text` | Clear | 清空 |
| `RNGReporter/GameCube.Designer.cs` | `anyHiddenPower.Text` | Any | 任意 |
| `RNGReporter/GameCube.Designer.cs` | `anyAbility.Text` | Any | 任意 |
| `RNGReporter/GameCube.Designer.cs` | `anyGender.Text` | Any | 任意 |
| `RNGReporter/GameCube.Designer.cs` | `anyNature.Text` | Any | 任意 |
| `RNGReporter/GameCube.Designer.cs` | `tabPage2.Text` | Shadow Checker | 黑暗宝可梦 |
| `RNGReporter/GameCube.Designer.cs` | `label5.Text` | Game | 游戏版本 |
| `RNGReporter/GameCube.Designer.cs` | `generateShadow.Text` | Generate | 计算 |
| `RNGReporter/GameCube.Designer.cs` | `Frame.HeaderText` | Frame | 帧数 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn15.HeaderText` | Nature | 性格 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn16.HeaderText` | Ability | 特性 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn17.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn18.HeaderText` | Atk | 攻击 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn19.HeaderText` | Def | 防御 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn20.HeaderText` | SpA | 特攻 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn21.HeaderText` | SpD | 特防 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn22.HeaderText` | Spe | 速度 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn23.HeaderText` | Hidden | 觉醒力量 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn24.HeaderText` | Power | 觉醒力量威力 |
| `RNGReporter/GameCube.Designer.cs` | `label21.Text` | Method | 算法 |
| `RNGReporter/GameCube.Designer.cs` | `label20.Text` | any shiny changes from TID and SID | 任何因 TID 和 SID 造成的闪光变化 |
| `RNGReporter/GameCube.Designer.cs` | `label19.Text` | Shadow Checker does not account for | 黑暗宝可梦不会考虑TID和SID引起的任何闪光变化 |
| `RNGReporter/GameCube.Designer.cs` | `label17.Text` | Starting Frame | 初始帧 |
| `RNGReporter/GameCube.Designer.cs` | `label18.Text` | Max Results | 最大结果帧 |
| `RNGReporter/GameCube.Designer.cs` | `label15.Text` | Shadow | 黑暗宝可梦 |
| `RNGReporter/GameCube.Designer.cs` | `label11.Text` | Ability | 特性 |
| `RNGReporter/GameCube.Designer.cs` | `label12.Text` | Gender | 性别比例 |
| `RNGReporter/GameCube.Designer.cs` | `label13.Text` | HP | 觉醒力量 |
| `RNGReporter/GameCube.Designer.cs` | `label14.Text` | Nature | 性格 |
| `RNGReporter/GameCube.Designer.cs` | `label4.Text` | HP | 觉醒力量 |
| `RNGReporter/GameCube.Designer.cs` | `label6.Text` | Atk | 攻击 |
| `RNGReporter/GameCube.Designer.cs` | `label7.Text` | Def | 防御 |
| `RNGReporter/GameCube.Designer.cs` | `label8.Text` | SpA | 特攻 |
| `RNGReporter/GameCube.Designer.cs` | `label9.Text` | SpD | 特防 |
| `RNGReporter/GameCube.Designer.cs` | `label10.Text` | Spe | 速度 |
| `RNGReporter/GameCube.Designer.cs` | `anyHPShadow.Text` | Any | 任意 |
| `RNGReporter/GameCube.Designer.cs` | `anyAbilityShadow.Text` | Any | 任意 |
| `RNGReporter/GameCube.Designer.cs` | `anyGenderShadow.Text` | Any | 任意 |
| `RNGReporter/GameCube.Designer.cs` | `anyNatureShadow.Text` | Any | 任意 |
| `RNGReporter/GameCube.Designer.cs` | `speClearShadow.Text` | Clear | 清空 |
| `RNGReporter/GameCube.Designer.cs` | `spdClearShadow.Text` | Clear | 清空 |
| `RNGReporter/GameCube.Designer.cs` | `spaClearShadow.Text` | Clear | 清空 |
| `RNGReporter/GameCube.Designer.cs` | `defClearShadow.Text` | Clear | 清空 |
| `RNGReporter/GameCube.Designer.cs` | `atkClearShadow.Text` | Clear | 清空 |
| `RNGReporter/GameCube.Designer.cs` | `hpClearShadow.Text` | Clear | 清空 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn2.HeaderText` | !!! | 异色 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn3.HeaderText` | Nature | 性格 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn4.HeaderText` | Ability | 特性 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn5.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn6.HeaderText` | Atk | 攻击 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn7.HeaderText` | Def | 防御 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn8.HeaderText` | SpA | 特攻 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn9.HeaderText` | SpD | 特防 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn10.HeaderText` | Spe | 速度 |
| `RNGReporter/GameCube.Designer.cs` | `dataGridViewTextBoxColumn11.HeaderText` | Hidden | 觉醒力量 |
| `RNGReporter/GameCube.Designer.cs` | `HiddenPowerPower.HeaderText` | Power | 觉醒力量威力 |
| `RNGReporter/GameCube.Designer.cs` | `Reason.HeaderText` | Reason | 原因 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Shiny Only | 仅异色 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Don\'t Care / Genderless | 不考虑/无性别 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Male (100% Male) | ♂(只有♂) |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Female (100% Female) | ♀(只有♀) |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Gender | 性别比例 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Ability | 特性 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Any | 任意 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Nature | 性格 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Awaiting Command | 等待操作... |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Gales | XD暗之旋风 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Colo | 圆形竞技场 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Channel | 宝可梦频道 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Search Method | 算法 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Shadows | 黑暗宝可梦 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Wishmkr Jirachi | Wishmkr的基拉祈 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Spread Finder | 搜索Seed |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Cancel | 取消 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Search | 计算 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Clear | 清空 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Shadow Checker | 黑暗宝可梦 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Game | 游戏版本 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Generate | 计算 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Frame | 帧 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Frame | 帧数 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Hidden | 觉醒 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Hidden | 觉醒力量 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Power | 威力 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Power | 觉醒力量威力 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Method | 算法 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | any shiny changes from TID and SID | 任何因 TID 和 SID 造成的闪光变化 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Shadow Checker does not account for | 黑暗宝可梦不会考虑TID和SID引起的任何闪光变化 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Starting Frame | 初始帧 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Max Results | 最大结果帧 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Shadow | 黑暗宝可梦 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | None | 无 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | !!! | 异色 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | Reason | 原因 |
| `RNGReporter/GameCube.Designer.cs` | `literal` | GameCube RNG | NGC乱数 |
| `RNGReporter/GameCube.cs` | `literal` | Hardy | 勤奋 |
| `RNGReporter/GameCube.cs` | `literal` | Lonely | 怕寂寞 |
| `RNGReporter/GameCube.cs` | `literal` | Brave | 勇敢 |
| `RNGReporter/GameCube.cs` | `literal` | Adamant | 固执 |
| `RNGReporter/GameCube.cs` | `literal` | Naughty | 顽皮 |
| `RNGReporter/GameCube.cs` | `literal` | Bold | 大胆 |
| `RNGReporter/GameCube.cs` | `literal` | Docile | 坦率 |
| `RNGReporter/GameCube.cs` | `literal` | Relaxed | 悠闲 |
| `RNGReporter/GameCube.cs` | `literal` | Impish | 淘气 |
| `RNGReporter/GameCube.cs` | `literal` | Lax | 乐天 |
| `RNGReporter/GameCube.cs` | `literal` | Timid | 胆小 |
| `RNGReporter/GameCube.cs` | `literal` | Hasty | 急躁 |
| `RNGReporter/GameCube.cs` | `literal` | Serious | 认真 |
| `RNGReporter/GameCube.cs` | `literal` | Jolly | 爽朗 |
| `RNGReporter/GameCube.cs` | `literal` | Naive | 天真 |
| `RNGReporter/GameCube.cs` | `literal` | Modest | 内敛 |
| `RNGReporter/GameCube.cs` | `literal` | Mild | 慢吞吞 |
| `RNGReporter/GameCube.cs` | `literal` | Quiet | 冷静 |
| `RNGReporter/GameCube.cs` | `literal` | Bashful | 害羞 |
| `RNGReporter/GameCube.cs` | `literal` | Rash | 马虎 |
| `RNGReporter/GameCube.cs` | `literal` | Calm | 温和 |
| `RNGReporter/GameCube.cs` | `literal` | Gentle | 温顺 |
| `RNGReporter/GameCube.cs` | `literal` | Sassy | 自大 |
| `RNGReporter/GameCube.cs` | `literal` | Careful | 慎重 |
| `RNGReporter/GameCube.cs` | `literal` | Quirky | 浮躁 |
| `RNGReporter/GameCube.cs` | `literal` | Fighting | 格斗 |
| `RNGReporter/GameCube.cs` | `literal` | Flying | 飞行 |
| `RNGReporter/GameCube.cs` | `literal` | Poison | 毒 |
| `RNGReporter/GameCube.cs` | `literal` | Ground | 地面 |
| `RNGReporter/GameCube.cs` | `literal` | Rock | 岩石 |
| `RNGReporter/GameCube.cs` | `literal` | Bug | 虫 |
| `RNGReporter/GameCube.cs` | `literal` | Ghost | 幽灵 |
| `RNGReporter/GameCube.cs` | `literal` | Steel | 钢 |
| `RNGReporter/GameCube.cs` | `literal` | Fire | 火 |
| `RNGReporter/GameCube.cs` | `literal` | Water | 水 |
| `RNGReporter/GameCube.cs` | `literal` | Grass | 草 |
| `RNGReporter/GameCube.cs` | `literal` | Electric | 电 |
| `RNGReporter/GameCube.cs` | `literal` | Psychic | 超能 |
| `RNGReporter/GameCube.cs` | `literal` | Ice | 冰 |
| `RNGReporter/GameCube.cs` | `literal` | Dragon | 龙 |
| `RNGReporter/GameCube.cs` | `literal` | Dark | 恶 |
| `RNGReporter/GameCube.cs` | `literal` | Cancelled. - Awaiting Command | 取消了 -等待操作... |
| `RNGReporter/GameCube.cs` | `literal` | Previous search is still running | 上一个计算仍在运行 |
| `RNGReporter/GameCube.cs` | `literal` | HP: Lower limit > Upper limit | HP：下限 > 上限 |
| `RNGReporter/GameCube.cs` | `literal` | Atk: Lower limit > Upper limit | 攻击：下限 > 上限 |
| `RNGReporter/GameCube.cs` | `literal` | Def: Lower limit > Upper limit | 防御：下限 > 上限 |
| `RNGReporter/GameCube.cs` | `literal` | SpA: Lower limit > Upper limit | 特攻：下限 > 上限 |
| `RNGReporter/GameCube.cs` | `literal` | SpD: Lower limit > Upper limit | 特防：下限 > 上限 |
| `RNGReporter/GameCube.cs` | `literal` | Spe: Lower limit > Upper limit | 速度：下限 > 上限 |
| `RNGReporter/GameCube.cs` | `literal` | Any | 任意 |
| `RNGReporter/GameCube.cs` | `literal` | Searching | 计算中 |
| `RNGReporter/GameCube.cs` | `literal` | Done. - Awaiting Command | 完成了 -等待操作... |
| `RNGReporter/GameCube.cs` | `literal` | !!! | 异色 |
| `RNGReporter/GameCube.cs` | `literal` | Altaria | 七夕青鸟 |
| `RNGReporter/GameCube.cs` | `literal` | Arbok | 阿柏怪 |
| `RNGReporter/GameCube.cs` | `literal` | Articuno | 急冻鸟 |
| `RNGReporter/GameCube.cs` | `literal` | Baltoy (Citadark) | 天秤偶（镍暗岛） |
| `RNGReporter/GameCube.cs` | `literal` | Baltoy (Initial) | 天秤偶（初始的） |
| `RNGReporter/GameCube.cs` | `literal` | Baltoy (Phenac) | 天秤偶（矽铍市） |
| `RNGReporter/GameCube.cs` | `literal` | Banette | 诅咒娃娃 |
| `RNGReporter/GameCube.cs` | `literal` | Beedrill | 大针蜂 |
| `RNGReporter/GameCube.cs` | `literal` | Butterfree | 巴大蝶 |
| `RNGReporter/GameCube.cs` | `literal` | Carvanha | 利牙鱼 |
| `RNGReporter/GameCube.cs` | `literal` | Chansey | 吉利蛋 |
| `RNGReporter/GameCube.cs` | `literal` | Delcatty | 优雅猫 |
| `RNGReporter/GameCube.cs` | `literal` | Dodrio | 嘟嘟利 |
| `RNGReporter/GameCube.cs` | `literal` | Dragonite | 快龙 |
| `RNGReporter/GameCube.cs` | `literal` | Dugtrio | 三地鼠 |
| `RNGReporter/GameCube.cs` | `literal` | Duskull | 夜巡灵 |
| `RNGReporter/GameCube.cs` | `literal` | Electabuzz | 电击兽 |
| `RNGReporter/GameCube.cs` | `literal` | Eevee | 伊布 |
| `RNGReporter/GameCube.cs` | `literal` | Exeggutor | 椰蛋树 |
| `RNGReporter/GameCube.cs` | `literal` | Farfetch'd | 大葱鸭 |
| `RNGReporter/GameCube.cs` | `literal` | Golduck | 哥达鸭 |
| `RNGReporter/GameCube.cs` | `literal` | Grimer | 臭泥 |
| `RNGReporter/GameCube.cs` | `literal` | Growlithe | 卡蒂狗 |
| `RNGReporter/GameCube.cs` | `literal` | Gulpin (Citadark) | 溶食兽（镍暗岛） |
| `RNGReporter/GameCube.cs` | `literal` | Gulpin (Initial) | 溶食兽（初始的） |
| `RNGReporter/GameCube.cs` | `literal` | Gulpin (Phenac) | 溶食兽（矽铍市） |
| `RNGReporter/GameCube.cs` | `literal` | Hitmonchan | 快拳郎 |
| `RNGReporter/GameCube.cs` | `literal` | Hitmonlee | 飞腿郎 |
| `RNGReporter/GameCube.cs` | `literal` | Houndour (Citadark) | 戴鲁比（镍暗岛） |
| `RNGReporter/GameCube.cs` | `literal` | Houndour (Initial) | 戴鲁比（初始的） |
| `RNGReporter/GameCube.cs` | `literal` | Houndour (Phenac) | 戴鲁比（矽铍市） |
| `RNGReporter/GameCube.cs` | `literal` | Hypno | 引梦貘人 |
| `RNGReporter/GameCube.cs` | `literal` | Kangaskhan | 袋兽 |
| `RNGReporter/GameCube.cs` | `literal` | Lapras | 拉普拉斯 |
| `RNGReporter/GameCube.cs` | `literal` | Ledyba | 芭瓢虫 |
| `RNGReporter/GameCube.cs` | `literal` | Lickitung | 大舌头 |
| `RNGReporter/GameCube.cs` | `literal` | Lugia | 洛奇亚 |
| `RNGReporter/GameCube.cs` | `literal` | Lunatone | 月石 |
| `RNGReporter/GameCube.cs` | `literal` | Magcargo | 熔岩蜗牛 |
| `RNGReporter/GameCube.cs` | `literal` | Magmar | 鸭嘴火兽 |
| `RNGReporter/GameCube.cs` | `literal` | Magneton | 三合一磁怪 |
| `RNGReporter/GameCube.cs` | `literal` | Makuhita | 幕下力士 |
| `RNGReporter/GameCube.cs` | `literal` | Manectric | 雷电兽 |
| `RNGReporter/GameCube.cs` | `literal` | Mareep (Citadark) | 咩利羊（镍暗岛） |
| `RNGReporter/GameCube.cs` | `literal` | Mareep (Initial) | 咩利羊（初始的） |
| `RNGReporter/GameCube.cs` | `literal` | Mareep (Phenac) | 咩利羊（矽铍市） |
| `RNGReporter/GameCube.cs` | `literal` | Marowak | 嘎啦嘎啦 |
| `RNGReporter/GameCube.cs` | `literal` | Mawile | 大嘴娃 |
| `RNGReporter/GameCube.cs` | `literal` | Meowth | 喵喵 |
| `RNGReporter/GameCube.cs` | `literal` | Moltres | 火焰鸟 |
| `RNGReporter/GameCube.cs` | `literal` | Mr. Mime | 魔墙人偶 |
| `RNGReporter/GameCube.cs` | `literal` | Natu | 天然雀 |
| `RNGReporter/GameCube.cs` | `literal` | Nosepass | 朝北鼻 |
| `RNGReporter/GameCube.cs` | `literal` | Numel | 呆火驼 |
| `RNGReporter/GameCube.cs` | `literal` | Paras | 派拉斯 |
| `RNGReporter/GameCube.cs` | `literal` | Pidgeotto | 比比鸟 |
| `RNGReporter/GameCube.cs` | `literal` | Pineco | 榛果球 |
| `RNGReporter/GameCube.cs` | `literal` | Pinsir | 凯罗斯 |
| `RNGReporter/GameCube.cs` | `literal` | Poliwrath | 蚊香泳士 |
| `RNGReporter/GameCube.cs` | `literal` | Poochyena | 土狼犬 |
| `RNGReporter/GameCube.cs` | `literal` | Primeape | 火暴猴 |
| `RNGReporter/GameCube.cs` | `literal` | Ralts | 拉鲁拉丝 |
| `RNGReporter/GameCube.cs` | `literal` | Rapidash | 烈焰马 |
| `RNGReporter/GameCube.cs` | `literal` | Raticate | 拉达 |
| `RNGReporter/GameCube.cs` | `literal` | Rhydon | 钻角犀兽 |
| `RNGReporter/GameCube.cs` | `literal` | Roselia | 毒蔷薇 |
| `RNGReporter/GameCube.cs` | `literal` | Sableye | 勾魂眼 |
| `RNGReporter/GameCube.cs` | `literal` | Salamence | 暴飞龙 |
| `RNGReporter/GameCube.cs` | `literal` | Scyther | 飞天螳螂 |
| `RNGReporter/GameCube.cs` | `literal` | Seedot (Citadark) | 橡实果（镍暗岛） |
| `RNGReporter/GameCube.cs` | `literal` | Seedot (Initial) | 橡实果（初始的） |
| `RNGReporter/GameCube.cs` | `literal` | Seedot (Phenac) | 橡实果（矽铍市） |
| `RNGReporter/GameCube.cs` | `literal` | Seel | 小海狮 |
| `RNGReporter/GameCube.cs` | `literal` | Shellder | 大舌贝 |
| `RNGReporter/GameCube.cs` | `literal` | Shroomish | 蘑蘑菇 |
| `RNGReporter/GameCube.cs` | `literal` | Snorlax | 卡比兽 |
| `RNGReporter/GameCube.cs` | `literal` | Snorunt | 雪童子 |
| `RNGReporter/GameCube.cs` | `literal` | Solrock | 太阳岩 |
| `RNGReporter/GameCube.cs` | `literal` | Spearow | 烈雀 |
| `RNGReporter/GameCube.cs` | `literal` | Spheal (Citadark) | 海豹球（镍暗岛） |
| `RNGReporter/GameCube.cs` | `literal` | Spheal (Initial) | 海豹球（初始的） |
| `RNGReporter/GameCube.cs` | `literal` | Spheal (Phenac) | 海豹球（矽铍市） |
| `RNGReporter/GameCube.cs` | `literal` | Spinarak | 圆丝蛛 |
| `RNGReporter/GameCube.cs` | `literal` | Starmie | 宝石海星 |
| `RNGReporter/GameCube.cs` | `literal` | Swellow | 大王燕 |
| `RNGReporter/GameCube.cs` | `literal` | Swinub | 小山猪 |
| `RNGReporter/GameCube.cs` | `literal` | Tangela | 蔓藤怪 |
| `RNGReporter/GameCube.cs` | `literal` | Tauros | 肯泰罗 |
| `RNGReporter/GameCube.cs` | `literal` | Teddiursa | 熊宝宝 |
| `RNGReporter/GameCube.cs` | `literal` | Togepi | 波克比 |
| `RNGReporter/GameCube.cs` | `literal` | Venomoth | 摩鲁蛾 |
| `RNGReporter/GameCube.cs` | `literal` | Voltorb | 霹雳电球 |
| `RNGReporter/GameCube.cs` | `literal` | Vulpix | 六尾 |
| `RNGReporter/GameCube.cs` | `literal` | Weepinbell | 口呆花 |
| `RNGReporter/GameCube.cs` | `literal` | Zangoose | 猫鼬斩 |
| `RNGReporter/GameCube.cs` | `literal` | Zapdos | 闪电鸟 |
| `RNGReporter/GameCube.cs` | `literal` | Gligar | 天蝎 |
| `RNGReporter/GameCube.cs` | `literal` | Heracross | 赫拉克罗斯 |
| `RNGReporter/GameCube.cs` | `literal` | Murkrow | 黑暗鸦 |
| `RNGReporter/GameCube.cs` | `literal` | Ursaring | 圈圈熊 |
| `RNGReporter/GameCube.cs` | `literal` | Shiny\t | 异色\t |
| `RNGReporter/GameCube.cs` | `literal` | Nature\t | 性格\t |
| `RNGReporter/GameCube.cs` | `literal` | Ability\t | 特性\t |
| `RNGReporter/GameCube.cs` | `literal` | Atk\t | 攻击\t |
| `RNGReporter/GameCube.cs` | `literal` | Def\t | 防御\t |
| `RNGReporter/GameCube.cs` | `literal` | SpA\t | 通过\t |
| `RNGReporter/GameCube.cs` | `literal` | SpD\t | 特防\t |
| `RNGReporter/GameCube.cs` | `literal` | Spe\t | 速度\t |
| `RNGReporter/GameCube.cs` | `literal` | Results exported to folder with RNGReporter.exe | 计算结果导出到带有RNGReporter.exe的文件夹 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `label1.Text` | Seed at 1/1/2000 at 00:00:00 | 在2000年1月1日00:00:00时的Seed |
| `RNGReporter/GameCubeRTC.Designer.cs` | `label2.Text` | Target seed | 目标seed |
| `RNGReporter/GameCubeRTC.Designer.cs` | `label3.Text` | Min frame | 最小帧 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `label4.Text` | Max frame | 最大帧 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `searchText.Text` | Awaiting command | 等待操作... |
| `RNGReporter/GameCubeRTC.Designer.cs` | `cancel.Text` | Cancel | 取消计算 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `buttonSearch.Text` | Search | 计算 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `Time.HeaderText` | Time | 时间 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `Frame.HeaderText` | Frame | 帧数 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `copySeed.Text` | Copy Seed to Clipboard | 复制种子到剪贴板 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `literal` | Seed at 1/1/2000 at 00:00:00 | 在2000年1月1日00:00:00时的Seed |
| `RNGReporter/GameCubeRTC.Designer.cs` | `literal` | Target seed | 目标seed |
| `RNGReporter/GameCubeRTC.Designer.cs` | `literal` | Min frame | 最小帧 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `literal` | Max frame | 最大帧 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `literal` | Awaiting command | 等待操作... |
| `RNGReporter/GameCubeRTC.Designer.cs` | `literal` | Cancel | 取消计算 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `literal` | Search | 计算 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `literal` | Copy Seed to Clipboard | 复制种子到剪贴板 |
| `RNGReporter/GameCubeRTC.Designer.cs` | `literal` | GameCube RTC Calculator | NGC RTC 时间计算 |
| `RNGReporter/GameCubeRTC.cs` | `literal` | Previous search running | 上一次搜索仍在运行 |
| `RNGReporter/GameCubeRTC.cs` | `literal` | Please enter your seed in proper hex format. | 请用正确的16进制输入您的seed |
| `RNGReporter/GameCubeRTC.cs` | `literal` | Initial and target seed are the same. Please change one of them. | 初始seed和目标seed相同，请更改其中一个 |
| `RNGReporter/GameCubeRTC.cs` | `literal` | Minutes added to RTC:  | 添加到RTC时钟的分钟数:  |
| `RNGReporter/GameCubeRTC.cs` | `literal` | Finish. Awaiting command | 完成了 -等待操作... |
| `RNGReporter/GameCubeRTC.cs` | `literal` | Search cancelled | 已取消计算 |
| `RNGReporter/Gen5FrameFinder.cs` | `literal` | High | 高 |
| `RNGReporter/Gen5FrameFinder.cs` | `literal` | Mid-High | 中高 |
| `RNGReporter/Gen5FrameFinder.cs` | `literal` | Mid | 中 |
| `RNGReporter/Gen5FrameFinder.cs` | `literal` | Mid-Low | 中低 |
| `RNGReporter/Gen5FrameFinder.cs` | `literal` | Low | 低 |
| `RNGReporter/Gen5FrameFinder.cs` | `literal` | L | 拉帝欧斯\\拉迪亚斯 |
| `RNGReporter/Gen5FrameFinder.cs` | `literal` | You need to select a target frame in the preview! | 你需要在预览中选择目标帧！ |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `tpChatotSearch.Text` | Chatot Pitches | 聒噪鸟音高 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `btnAny.Text` | Any | 任意 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `btnMidLow_Low.Text` | Mid-Low / Low | 中低 / 低 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `btnMid_MidLow.Text` | Mid / Mid-Low | 中 / 中低 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `btbMidHigh_Mid.Text` | Mid-High / Mid | 中高 / 中 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `btnHigh_MidHigh.Text` | High / Mid-High | 高 / 中高 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `btnJumpToFrame.Text` | Jump to selected frame | 跳转到所选帧 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `lblResults.Text` | Possible Results: | 可能结果: |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `btnLow.Text` | Low | 低 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `btnMidLow.Text` | Mid-Low | 中低 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `btnMid.Text` | Mid | 中 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `btnHigh.Text` | High | 高 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `btnMidHigh.Text` | Mid-High | 中高 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `btnClear.Text` | Clear | 清除 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `btnRemove.Text` | Remove | 移除 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Chatot Pitches | 聒噪鸟音高 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Any | 任意 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Mid-Low / Low | 中低 / 低 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Mid / Mid-Low | 中 / 中低 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Mid-High / Mid | 中高 / 中 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | High / Mid-High | 高 / 中高 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Jump to selected frame | 跳转到所选帧 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Possible Results: | 可能结果: |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Low | 低 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Mid-Low | 中低 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Mid | 中 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | High | 高 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Mid-High | 中高 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Clear | 清除 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Remove | 移除 |
| `RNGReporter/Gen5FrameFinder.designer.cs` | `literal` | Gen 5 Frame Finder | 第五世代帧查找器 |
| `RNGReporter/GenderRatioLookup.Designer.cs` | `label1.Text` | Pokémon | 宝可梦 |
| `RNGReporter/GenderRatioLookup.Designer.cs` | `buttonOk.Text` | OK | 确定 |
| `RNGReporter/GenderRatioLookup.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/GenderRatioLookup.Designer.cs` | `literal` | Pokémon | 宝可梦 |
| `RNGReporter/GenderRatioLookup.Designer.cs` | `literal` | OK | 确定 |
| `RNGReporter/GenderRatioLookup.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/GenderRatioLookup.Designer.cs` | `literal` | Gender Ratio Lookup | 性别比例查询 |
| `RNGReporter/IVstoFrame.Designer.cs` | `groupBox1.Text` |  Frame Finder | 帧数计算 |
| `RNGReporter/IVstoFrame.Designer.cs` | `Frame.HeaderText` | Frame | 帧 |
| `RNGReporter/IVstoFrame.Designer.cs` | `copyToolStripMenuItem.Text` | Copy | 复制 |
| `RNGReporter/IVstoFrame.Designer.cs` | `glassButton1.Text` | Search | 计算 |
| `RNGReporter/IVstoFrame.Designer.cs` | `groupBox2.Text` | Config | 配置参数 |
| `RNGReporter/IVstoFrame.Designer.cs` | `label9.Text` | Initial seed | 初始seed |
| `RNGReporter/IVstoFrame.Designer.cs` | `label10.Text` | Starting Frame | 初始帧 |
| `RNGReporter/IVstoFrame.Designer.cs` | `label11.Text` | Max Frame | 最大帧 |
| `RNGReporter/IVstoFrame.Designer.cs` | `glassButton2_3.Text` | Clear | 清空 |
| `RNGReporter/IVstoFrame.Designer.cs` | `label1.Text` | Method | 算法 |
| `RNGReporter/IVstoFrame.Designer.cs` | `label8.Text` | Spe | 速度 |
| `RNGReporter/IVstoFrame.Designer.cs` | `label7.Text` | Spd | 特防 |
| `RNGReporter/IVstoFrame.Designer.cs` | `label6.Text` | Spa | 特攻 |
| `RNGReporter/IVstoFrame.Designer.cs` | `label5.Text` | Def | 防御 |
| `RNGReporter/IVstoFrame.Designer.cs` | `label4.Text` | Atk | 攻击 |
| `RNGReporter/IVstoFrame.Designer.cs` | `literal` | Colosseum\\XD | 圆形竞技场\\XD暗之旋风 |
| `RNGReporter/IVstoFrame.Designer.cs` | `literal` | Clear | 清空 |
| `RNGReporter/IVstoFrame.Designer.cs` | `literal` | FRLG/RSE IVs to Frame | 火红叶绿/三宝石 根据个体计算帧数 |
| `RNGReporter/IVstoFrame.cs` | `literal` | Please fill all the fields | 请填写所有的参数 |
| `RNGReporter/IVstoFrame.cs` | `literal` | Error | 错误 |
| `RNGReporter/IVstoFrame.cs` | `literal` | Please select the frame | 请选择一个帧数 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `buttonGenerate.Text` | Find | 计算 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `label10.Text` | Nature | 性格 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `label15.Text` | Spe | 速度 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `label16.Text` | SpD | 特防 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `label17.Text` | SpA | 特攻 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `label18.Text` | Def | 防御 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `label19.Text` | Atk | 攻击 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `label20.Text` | HP | 觉醒力量 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `Method.HeaderText` | Method | 算法 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `Ability.HeaderText` | Ability | 特性 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `setSeedToolStripMenuItem.Text` | Set Seed | 设置Seed到下方显示 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `setSIDToolStripMenuItem.Text` | Set SID | 设置SID到下方显示 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `copyPIDToolStripMenuItem.Text` | Copy PID | 复制PID |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `buttonOk.Text` | OK | 确定 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `label4.Text` | This tool cannot be used for 5th Generation Pokémon. | 此工具不能用于GEN5宝可梦 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | Find | 计算 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | Nature | 性格 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | Set Seed | 设置Seed到下方显示 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | Set SID | 设置SID到下方显示 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | Copy PID | 复制PID |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | OK | 确定 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | This tool cannot be used for 5th Generation Pokémon. | 此工具不能用于GEN5宝可梦 |
| `RNGReporter/IVtoPID_SID_SEED.Designer.cs` | `literal` | IVs to PID / SEED | 根据个体值计算PID/SEED |
| `RNGReporter/JirachiGeneration.Designer.cs` | `literal` | Generate | buttonGenerate |
| `RNGReporter/MainForm.Designer.cs` | `label3.Text` | Method | 随机数算法 |
| `RNGReporter/MainForm.Designer.cs` | `checkBoxShinyOnly.Text` | Shiny Only | 仅异色 |
| `RNGReporter/MainForm.Designer.cs` | `lockFrameToolStripMenuItem.Text` | Set as Target Frame | 设为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `jumpFrameToolStripMenuItem.Text` | Jump to Target Frame | 跳至目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `centerTo1SecondToolStripMenuItem.Text` | Center to +/- 1 Second and Set as Target Frame | 居中至 +/- 1 秒并设置为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `centerTo2SecondsToolStripMenuItem.Text` | Center to +/- 2 Seconds and Set as Target Frame | 居中至 +/- 2 秒并设置为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `centerTo3SecondsToolStripMenuItem.Text` | Center to +/- 3 Seconds and Set as Target Frame | 居中至 +/- 3 秒并设置为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `centerTo5SecondsToolStripMenuItem.Text` | Center to +/- 5 Seconds and Set as Target Frame | 居中至 +/- 5 秒并设置为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `centerTo10SecondsToolStripMenuItem.Text` | Center to +/- 10 Seconds and Set as Target Frame | 居中至 +/- 10 秒并设置为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `centerTp1MinuteToolStripMenuItem.Text` | Center to +/- 1 Minute and Set as Target Frame | 居中至 +/- 1 分钟并设置为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `removeCenteringToolStripMenuItem.Text` | Remove Centering | 清空帧数 |
| `RNGReporter/MainForm.Designer.cs` | `calculatePoketechTapsToolStripMenuItem.Text` | Calculate Poketech Taps ... | 计算宝可表轻触次数 ... |
| `RNGReporter/MainForm.Designer.cs` | `searchCoinFlipsToolStripMenuItem.Text` | Search Coin Flips ... | 搜索投硬币 ... |
| `RNGReporter/MainForm.Designer.cs` | `searchNaturesToolStripMenuItem.Text` | Search Natures ... | 搜索性格 ... |
| `RNGReporter/MainForm.Designer.cs` | `searchElmToolStripMenuItem.Text` | Search Elm Responses ... | 搜索Elm打电话的结果 ... |
| `RNGReporter/MainForm.Designer.cs` | `gen5FrameFinderToolStripMenuItem.Text` | Gen 5 FrameFinder | 第五世代帧查找器 |
| `RNGReporter/MainForm.Designer.cs` | `displayParentsInSearchToolStripMenuItem.Text` | Display Parents in Search... | 在搜索中显示父母... |
| `RNGReporter/MainForm.Designer.cs` | `resetParentsToolStripMenuItem.Text` | Reset Parents | 重置父母 |
| `RNGReporter/MainForm.Designer.cs` | `outputResultsToTXTToolStripMenuItem.Text` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/MainForm.Designer.cs` | `label11.Text` | Min Frame | 初始帧 |
| `RNGReporter/MainForm.Designer.cs` | `label13.Text` | Nature | 性格 |
| `RNGReporter/MainForm.Designer.cs` | `label14.Text` | Target Frame: | 目标帧： |
| `RNGReporter/MainForm.Designer.cs` | `labelTargetFrame.Text` | None | 无 |
| `RNGReporter/MainForm.Designer.cs` | `label16.Text` | Ability | 特性 |
| `RNGReporter/MainForm.Designer.cs` | `label17.Text` | Coin Flips for Seed: | 投硬币获取Seed： |
| `RNGReporter/MainForm.Designer.cs` | `label19.Text` | Elm Responses for Seed: | Elm打电话的结果获取Seed： |
| `RNGReporter/MainForm.Designer.cs` | `checkBoxRPresent.Text` | R | 雷公 |
| `RNGReporter/MainForm.Designer.cs` | `checkBoxEPresent.Text` | E | 炎帝 |
| `RNGReporter/MainForm.Designer.cs` | `checkBoxLPresent.Text` | L | 拉帝欧斯\\拉迪亚斯 |
| `RNGReporter/MainForm.Designer.cs` | `label18.Text` | Roaming Pokemon Locations: | 游走宝可梦位置： |
| `RNGReporter/MainForm.Designer.cs` | `label20.Text` | Encounter Slot | 遭遇槽位 |
| `RNGReporter/MainForm.Designer.cs` | `checkBoxDreamWorld.Text` | Dream World Egg Only | 仅梦世界的蛋 |
| `RNGReporter/MainForm.Designer.cs` | `menuStrip1.Text` | menuStrip1 | 菜单栏1 |
| `RNGReporter/MainForm.Designer.cs` | `pokedexIVCheckerToolStripMenuItem.Text` | Pokédex-IV Checker | 个体计算器/迷你图鉴 |
| `RNGReporter/MainForm.Designer.cs` | `rdGenToolsToolStripMenuItem.Text` | 3rd Gen Tools | GEN3工具集 |
| `RNGReporter/MainForm.Designer.cs` | `tIDSIDManipulationPandorasBoxToolStripMenuItem2.Text` | TID\\SID Manipulation (\"Pandora\'s Box\") | TID\\SID 计算器 （\"潘多拉魔盒\"） |
| `RNGReporter/MainForm.Designer.cs` | `bitSeedToTimeToolStripMenuItem.Text` | 16-Bit Seed to Time | Seed to Time（有电红/蓝宝石） |
| `RNGReporter/MainForm.Designer.cs` | `jirachiGenerationToolStripMenuItem.Text` | Jirachi Generation | 基拉祈计算器 |
| `RNGReporter/MainForm.Designer.cs` | `pIDToIVsToolStripMenuItem.Text` | PID to IVs | 根据PID计算个体值 |
| `RNGReporter/MainForm.Designer.cs` | `iVsToFrameToolStripMenuItem.Text` | IVs to Frame | 根据个体值计算帧数 |
| `RNGReporter/MainForm.Designer.cs` | `gameCubeRTCToolStripMenuItem.Text` | GameCube RTC | NGC RTC计算器 |
| `RNGReporter/MainForm.Designer.cs` | `pokespotToolStripMenuItem.Text` | Pokespot | Pokespot(XD)计算器 |
| `RNGReporter/MainForm.Designer.cs` | `rubyEncounterTableToolStripMenuItem.Text` | Ruby Encounter Table | 红宝石野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `sapphireEncounterTableToolStripMenuItem.Text` | Sapphire Encounter Table | 蓝宝石野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `emeraldEncounterTableToolStripMenuItem.Text` | Emerald Encounter Table | 绿宝石野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `fireRedEncounterTableToolStripMenuItem.Text` | Fire Red Encounter Table | 火红野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `leafGreenEncounterTableToolStripMenuItem.Text` | Leaf Green Encounter Table | 叶绿野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `thGenToolsToolStripMenuItem.Text` | 4th Gen Tools | GEN4工具集 |
| `RNGReporter/MainForm.Designer.cs` | `iVsToPIDToolStripMenuItem.Text` | Calculate PID from IVs | 根据个体值计算PID |
| `RNGReporter/MainForm.Designer.cs` | `findSIDFromChainedShiniesToolStripMenuItem.Text` | Find SID from Chained Shinies | 根据连锁异色计算SID |
| `RNGReporter/MainForm.Designer.cs` | `seedToTimeToolStripMenuItem.Text` | Seed to Time | Seed 转时间 |
| `RNGReporter/MainForm.Designer.cs` | `tIDSIDManipulationPandorasBoxToolStripMenuItem.Text` | TID\\SID Manipulation (\"Pandora\'s Box\") | TID\\SID 计算器 (\"潘多拉魔盒\") |
| `RNGReporter/MainForm.Designer.cs` | `findSeedByIVsToolStripMenuItem.Text` | Find Seed by IVs | 根据个体计算Seed |
| `RNGReporter/MainForm.Designer.cs` | `findSeedByStatsToolStripMenuItem.Text` | Find Seed by Stats | 根据宝可梦能力值计算Seed |
| `RNGReporter/MainForm.Designer.cs` | `findSeedByIVRangeToolStripMenuItem.Text` | Find Seed by IV Range | 根据宝可梦个体值范围计算Seed |
| `RNGReporter/MainForm.Designer.cs` | `simpleSeedGeneratorToolStripMenuItem.Text` | Simple Seed Generator | 简易版Seed计算器 |
| `RNGReporter/MainForm.Designer.cs` | `diamondEncounterTableToolStripMenuItem.Text` | Diamond Encounter Table | 钻石野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `pearlEncounterTableToolStripMenuItem.Text` | Pearl Encounter Table | 珍珠野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `platinumEncounterTableToolStripMenuItem.Text` | Platinum Encounter Table | 白金野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `heartGoldEncounterTableToolStripMenuItem.Text` | Heart Gold Encounter Table | 心金野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `soulSilverEncounterTableToolStripMenuItem.Text` | Soul Silver Encounter Table | 魂银野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `thGenToolsToolStripMenuItem1.Text` | 5th Gen Tools | GEN5工具集 |
| `RNGReporter/MainForm.Designer.cs` | `findDSParametersToolStripMenuItem.Text` | Find DS Parameters (Standard Seeds) | 计算DS参数 (普通Seed) |
| `RNGReporter/MainForm.Designer.cs` | `unovaLinkParametersToolStripMenuItem.Text` | Unova Link Parameters | 计算合众连接参数 |
| `RNGReporter/MainForm.Designer.cs` | `seedToTimeCGearSeedsToolStripMenuItem.Text` | Seed to Time (C-Gear Seeds) | Seed 转时间（Ｃ装置 Seeds） |
| `RNGReporter/MainForm.Designer.cs` | `tIDSIDManipulationPandorasBoxToolStripMenuItem1.Text` | TID\\SID Manipulation (\"Pandora\'s Box\") | TID\\SID 计算器 (\"潘多拉魔盒\") |
| `RNGReporter/MainForm.Designer.cs` | `simpleSeedGeneratorToolStripMenuItem1.Text` | Simple Seed Generator | 简易版Seed计算器 |
| `RNGReporter/MainForm.Designer.cs` | `adjacentSeedToolToolStripMenuItem.Text` | Adjacent Seed Tool | 目标附近Seed计算器 |
| `RNGReporter/MainForm.Designer.cs` | `entralinkSeedToolToolStripMenuItem.Text` | Entralink Seed Search | 连入之森Seed计算器 |
| `RNGReporter/MainForm.Designer.cs` | `blackEncounterTableToolStripMenuItem.Text` | Black Encounter Table | 黑野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `whiteEncounterTableToolStripMenuItem.Text` | White Encounter Table | 白野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `black2EncounterTableToolStripMenuItem.Text` | Black 2 Encounter Table | 黑2野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `white2EncounterTableToolStripMenuItem.Text` | White 2 Encounter Table | 白2野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `hiddenGrottoEncounterTablesToolStripMenuItem.Text` | Hidden Grotto Encounter Tables | 隐藏洞穴宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `performanceOptionsToolStripMenuItem.Text` | Options | 设置 |
| `RNGReporter/MainForm.Designer.cs` | `numberOfCPUCoresToolStripMenuItem.Text` | Number of CPU Cores | 用于计算CPU的核数 |
| `RNGReporter/MainForm.Designer.cs` | `pIDDisplayToolStripMenuItem.Text` | PID Display | 显示PID |
| `RNGReporter/MainForm.Designer.cs` | `hexToolStripMenuItem.Text` | Hex | 16进制 |
| `RNGReporter/MainForm.Designer.cs` | `decimalToolStripMenuItem.Text` | Decimal | 10进制 |
| `RNGReporter/MainForm.Designer.cs` | `showToolTipsToolStripMenuItem.Text` | Show ToolTips | 显示工具提示 |
| `RNGReporter/MainForm.Designer.cs` | `researcherToolStripMenuItem.Text` | Researcher | 算法研究计算器 |
| `RNGReporter/MainForm.Designer.cs` | `languageToolStripMenuItem.Text` | Language | 语言 |
| `RNGReporter/MainForm.Designer.cs` | `profilesToolStripMenuItem.Text` | Profiles | 存档信息管理 |
| `RNGReporter/MainForm.Designer.cs` | `checkBoxDittoParent.Text` | Ditto Parent | 父母含百变怪 |
| `RNGReporter/MainForm.Designer.cs` | `checkBoxSynchOnly.Text` | Synch Frames Only | 仅同步生效帧 |
| `RNGReporter/MainForm.Designer.cs` | `label52.Text` | Encounter Type | 相遇类型 |
| `RNGReporter/MainForm.Designer.cs` | `label21.Text` | required for Black\\White Standard Seeds | 黑白普通seed所需 |
| `RNGReporter/MainForm.Designer.cs` | `labelCalcWarning.Text` | Note: frame prediction will not be\naccurate if there are NPCs in the area | 注意:如果区域内有npc，帧预测将会不准确 |
| `RNGReporter/MainForm.Designer.cs` | `checkBoxRoamerReleased.Text` | Active Roamer | 游走已触发 |
| `RNGReporter/MainForm.Designer.cs` | `label41.Text` | Gender | 性别比例 |
| `RNGReporter/MainForm.Designer.cs` | `FifthGenerationTimeFinderToolStripMenuItem.Text` | 5th Generation Time Finder | 第五世代时间查找器 |
| `RNGReporter/MainForm.Designer.cs` | `FourthGenerationTimeFinderToolStripMenuItem.Text` | 4th Generation Time Finder | 第四世代时间查找器 |
| `RNGReporter/MainForm.Designer.cs` | `ThirdGenerationTimeFinderToolStripMenuItem.Text` | 3rd Generation Time Finder | 第三世代时间查找器 |
| `RNGReporter/MainForm.Designer.cs` | `GameCubeTimeFinderToolStripMenuItem.Text` | GameCube Time Finder | GameCube 时间查找器 |
| `RNGReporter/MainForm.Designer.cs` | `toolTipDataGrid.ToolTipTitle` | Chatot Pitch | 聒噪鸟音高 |
| `RNGReporter/MainForm.Designer.cs` | `checkBoxBW2.Text` | Black White 2 | 黑 白 2? |
| `RNGReporter/MainForm.Designer.cs` | `cbNidoBeat.Text` | Nidoran/Volbeat | 尼多一家/电萤虫 |
| `RNGReporter/MainForm.Designer.cs` | `cbShinyCharm.Text` | Shiny Charm | 迷人之躯异色 |
| `RNGReporter/MainForm.Designer.cs` | `checkBoxMemoryLink.Text` | Memory Link Activated | 记忆连接? |
| `RNGReporter/MainForm.Designer.cs` | `checkBoxTrigger.Text` | Battle Trigger by Moving | 移动触发对战 |
| `RNGReporter/MainForm.Designer.cs` | `Gen5GroupBox.Text` | Gen 5 Settings | 第五世代设置 |
| `RNGReporter/MainForm.Designer.cs` | `labelLuckyPower.Text` | Lucky Power | 幸运之力 |
| `RNGReporter/MainForm.Designer.cs` | `labelMinMaxLevel.Text` | Min / Max Level | 最小 / 最大等级 |
| `RNGReporter/MainForm.Designer.cs` | `buttonCalcInitialFrame.Text` | Calculate Initial PIDRNG Frame | 计算 PIDRNG 初始帧 |
| `RNGReporter/MainForm.Designer.cs` | `buttonDSParameters.Text` | DS Parameters Search | 校准计算DS参数 |
| `RNGReporter/MainForm.Designer.cs` | `label4.Text` | Max Advances | 最大帧 |
| `RNGReporter/MainForm.Designer.cs` | `MainImportWC.Text` | Import Wonder Card | 导入神秘卡 |
| `RNGReporter/MainForm.Designer.cs` | `buttonRoamerMap.Text` | Map | 地图 |
| `RNGReporter/MainForm.Designer.cs` | `buttonAnySlot.Text` | Any | 任意 |
| `RNGReporter/MainForm.Designer.cs` | `buttonFindTime.Text` | Time Finder | 时间查找 |
| `RNGReporter/MainForm.Designer.cs` | `buttonAnyNature.Text` | Any | 任意 |
| `RNGReporter/MainForm.Designer.cs` | `buttonGenerate.Text` | Generate | 计算 |
| `RNGReporter/MainForm.Designer.cs` | `Frame.HeaderText` | Frame | 帧数 |
| `RNGReporter/MainForm.Designer.cs` | `Offset.HeaderText` | Occidentary | 偶然值Occidentary |
| `RNGReporter/MainForm.Designer.cs` | `Time.HeaderText` | Time | 时间 |
| `RNGReporter/MainForm.Designer.cs` | `Elm.HeaderText` | Elm | Elm电话 |
| `RNGReporter/MainForm.Designer.cs` | `Chatot.HeaderText` | Chatot Pitch | 聒噪鸟音高 |
| `RNGReporter/MainForm.Designer.cs` | `Ratio.HeaderText` | Ratio | 比例 |
| `RNGReporter/MainForm.Designer.cs` | `EncType.HeaderText` | Encounter Type | 遭遇类型 |
| `RNGReporter/MainForm.Designer.cs` | `EncounterSlot.HeaderText` | Encounter Slot | 遭遇槽位 |
| `RNGReporter/MainForm.Designer.cs` | `Level.HeaderText` | Level | 等级 |
| `RNGReporter/MainForm.Designer.cs` | `ItemCalc.HeaderText` | Item Percent | 道具概率 |
| `RNGReporter/MainForm.Designer.cs` | `CaveSpot.HeaderText` | Cave Spot | 卷尘地面 |
| `RNGReporter/MainForm.Designer.cs` | `Shiny.HeaderText` | !!! | 异色 |
| `RNGReporter/MainForm.Designer.cs` | `Nature.HeaderText` | Nature | 性格 |
| `RNGReporter/MainForm.Designer.cs` | `Ability.HeaderText` | Ability | 特性 |
| `RNGReporter/MainForm.Designer.cs` | `Dream.HeaderText` | Dream World | 梦世界 |
| `RNGReporter/MainForm.Designer.cs` | `Coin.HeaderText` | Coin | 硬币结果 |
| `RNGReporter/MainForm.Designer.cs` | `HP.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/MainForm.Designer.cs` | `Atk.HeaderText` | Atk | 攻击 |
| `RNGReporter/MainForm.Designer.cs` | `Def.HeaderText` | Def | 防御 |
| `RNGReporter/MainForm.Designer.cs` | `SpA.HeaderText` | SpA | 特攻 |
| `RNGReporter/MainForm.Designer.cs` | `SpD.HeaderText` | SpD | 特防 |
| `RNGReporter/MainForm.Designer.cs` | `Spe.HeaderText` | Spe | 速度 |
| `RNGReporter/MainForm.Designer.cs` | `ColumnItem1.HeaderText` | Item 1 | 道具 1 |
| `RNGReporter/MainForm.Designer.cs` | `ColumnItem2.HeaderText` | Item 2 | 道具 2 |
| `RNGReporter/MainForm.Designer.cs` | `ColumnItem3.HeaderText` | Item 3 | 道具 3 |
| `RNGReporter/MainForm.Designer.cs` | `ColumnItem4.HeaderText` | Item 4 | 道具 4 |
| `RNGReporter/MainForm.Designer.cs` | `ColumnItem5.HeaderText` | Item 5 | 道具 5 |
| `RNGReporter/MainForm.Designer.cs` | `ColumnItem6.HeaderText` | Item 6 | 道具 6 |
| `RNGReporter/MainForm.Designer.cs` | `HiddenPower.HeaderText` | Hidden | 觉醒力量 |
| `RNGReporter/MainForm.Designer.cs` | `HiddenPowerPower.HeaderText` | Power | 觉醒力量威力 |
| `RNGReporter/MainForm.Designer.cs` | `Characteristic.HeaderText` | Characteristic | 个性 |
| `RNGReporter/MainForm.Designer.cs` | `MaleOnlySpecies.HeaderText` | Species | 种族 |
| `RNGReporter/MainForm.Designer.cs` | `Synchable.HeaderText` | Synchable | 同步能力 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Method | 随机数算法 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Shiny Only | 仅异色 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Set as Target Frame | 设为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Jump to Target Frame | 跳至目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Center to +/- 1 Second and Set as Target Frame | 居中至 +/- 1 秒并设置为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Center to +/- 2 Seconds and Set as Target Frame | 居中至 +/- 2 秒并设置为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Center to +/- 3 Seconds and Set as Target Frame | 居中至 +/- 3 秒并设置为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Center to +/- 5 Seconds and Set as Target Frame | 居中至 +/- 5 秒并设置为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Center to +/- 10 Seconds and Set as Target Frame | 居中至 +/- 10 秒并设置为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Center to +/- 1 Minute and Set as Target Frame | 居中至 +/- 1 分钟并设置为目标帧 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Remove Centering | 清空帧数 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Calculate Poketech Taps ... | 计算宝可表轻触次数 ... |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Search Coin Flips ... | 搜索投硬币 ... |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Search Natures ... | 搜索性格 ... |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Search Elm Responses ... | 搜索Elm打电话的结果 ... |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Gen 5 FrameFinder | 第五世代帧查找器 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Display Parents in Search... | 在搜索中显示父母... |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Reset Parents | 重置父母 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Min Frame | 初始帧 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Nature | 性格 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Target Frame: | 目标帧： |
| `RNGReporter/MainForm.Designer.cs` | `literal` | None | 无 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Ability | 特性 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Coin Flips for Seed: | 投硬币获取Seed： |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Elm Responses for Seed: | Elm打电话的结果获取Seed： |
| `RNGReporter/MainForm.Designer.cs` | `literal` | R | 雷公 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | E | 炎帝 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | L | 拉帝欧斯\\拉迪亚斯 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Roaming Pokemon Locations: | 游走宝可梦位置： |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Encounter Slot | 遭遇槽位 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Dream World Egg Only | 仅梦世界的蛋 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | menuStrip1 | 菜单栏1 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Pokédex-IV Checker | 个体计算器/迷你图鉴 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | 3rd Gen Tools | GEN3工具集 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | TID\\SID Manipulation (\"Pandora\'s Box\") | TID\\SID 计算器 （\"潘多拉魔盒\"） |
| `RNGReporter/MainForm.Designer.cs` | `literal` | 16-Bit Seed to Time | Seed to Time（有电红/蓝宝石） |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Jirachi Generation | 基拉祈计算器 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | PID to IVs | 根据PID计算个体值 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | IVs to Frame | 根据个体值计算帧数 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | GameCube RTC | NGC RTC计算器 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Pokespot | Pokespot(XD)计算器 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Ruby Encounter Table | 红宝石野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Sapphire Encounter Table | 蓝宝石野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Emerald Encounter Table | 绿宝石野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Fire Red Encounter Table | 火红野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Leaf Green Encounter Table | 叶绿野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | 4th Gen Tools | GEN4工具集 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Calculate PID from IVs | 根据个体值计算PID |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Find SID from Chained Shinies | 根据连锁异色计算SID |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Seed to Time | Seed 转时间 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | TID\\SID Manipulation (\"Pandora\'s Box\") | TID\\SID 计算器 (\"潘多拉魔盒\") |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Find Seed by IVs | 根据个体计算Seed |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Find Seed by Stats | 根据宝可梦能力值计算Seed |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Find Seed by IV Range | 根据宝可梦个体值范围计算Seed |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Simple Seed Generator | 简易版Seed计算器 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Diamond Encounter Table | 钻石野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Pearl Encounter Table | 珍珠野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Platinum Encounter Table | 白金野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Heart Gold Encounter Table | 心金野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Soul Silver Encounter Table | 魂银野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | 5th Gen Tools | GEN5工具集 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Find DS Parameters (Standard Seeds) | 计算DS参数 (普通Seed) |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Unova Link Parameters | 计算合众连接参数 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Seed to Time (C-Gear Seeds) | Seed 转时间（Ｃ装置 Seeds） |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Adjacent Seed Tool | 目标附近Seed计算器 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Entralink Seed Search | 连入之森Seed计算器 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Black Encounter Table | 黑野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | White Encounter Table | 白野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Black 2 Encounter Table | 黑2野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | White 2 Encounter Table | 白2野生宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Hidden Grotto Encounter Tables | 隐藏洞穴宝可梦遭遇表 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Options | 设置 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Number of CPU Cores | 用于计算CPU的核数 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | PID Display | 显示PID |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Hex | 16进制 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Decimal | 10进制 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Show ToolTips | 显示工具提示 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Researcher | 算法研究计算器 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Language | 语言 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Profiles | 存档信息管理 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Ditto Parent | 父母含百变怪 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Synch Frames Only | 仅同步生效帧 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Encounter Type | 相遇类型 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | required for Black\\White Standard Seeds | 黑白普通seed所需 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Note: frame prediction will not be\naccurate if there are NPCs in the area | 注意:如果区域内有npc，帧预测将会不准确 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Active Roamer | 游走已触发 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Gender | 性别比例 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | 5th Generation Time Finder | 第五世代时间查找器 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | 4th Generation Time Finder | 第四世代时间查找器 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | 3rd Generation Time Finder | 第三世代时间查找器 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | GameCube Time Finder | GameCube 时间查找器 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Chatot Pitch | 聒噪鸟音高 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Black White 2 | 黑 白 2? |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Nidoran/Volbeat | 尼多一家/电萤虫 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Shiny Charm | 迷人之躯异色 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Memory Link Activated | 记忆连接? |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Battle Trigger by Moving | 移动触发对战 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Gen 5 Settings | 第五世代设置 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Lucky Power | 幸运之力 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Min / Max Level | 最小 / 最大等级 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Calculate Initial PIDRNG Frame | 计算 PIDRNG 初始帧 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | DS Parameters Search | 校准计算DS参数 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Max Advances | 最大帧 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Import Wonder Card | 导入神秘卡 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Map | 地图 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Any | 任意 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Wild Pokémon | 野生宝可梦 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Wild Pokémon (Bubble Spot) | 野生宝可梦（水纹水面） |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Wild Pokémon (Shaking Grass) | 野生宝可梦（摇动草丛） |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Wild Pokémon (Cave Spot) | 野生宝可梦（卷尘地面） |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Stationary Pokémon | 定点宝可梦 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Gift Pokémon (Non-Mystery Gift) | 礼物宝可梦 (非神秘礼物) |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Safari Zone | 狩猎地带 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Time Finder | 时间查找 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Generate | 计算 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Frame | 帧数 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Frame | 帧 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Offset | 偏移 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Occidentary | 偶然值Occidentary |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Time | 时间 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Elm | Elm电话 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Ratio | 比例 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Encounter Type | 遭遇类型 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Level | 等级 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Item Percent | 道具概率 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Cave Spot | 卷尘地面 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | !!! | 异色 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Dream World | 梦世界 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Coin | 硬币结果 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Item 1 | 道具 1 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Item 2 | 道具 2 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Item 3 | 道具 3 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Item 4 | 道具 4 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Item 5 | 道具 5 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Item 6 | 道具 6 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Hidden | 觉醒力量 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Power | 觉醒力量威力 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Characteristic | 个性 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Species | 种族 |
| `RNGReporter/MainForm.Designer.cs` | `literal` | Synchable | 同步能力 |
| `RNGReporter/MainForm.Designer.cs` | `literal` |  RNG Reporter 10.3.4 |  RNG Reporter 10.3.4[汉化by:自然公園/白白不是公主/Hakuhiro] |
| `RNGReporter/MainForm.cs` | `literal` | Method J (DPPt) | Method J（钻石珍珠白金） |
| `RNGReporter/MainForm.cs` | `literal` | Method K (HGSS) | Method K（心金魂银） |
| `RNGReporter/MainForm.cs` | `literal` | Gen 5 IVs (Standard Seed) | GEN5个体值（普通的Seed） |
| `RNGReporter/MainForm.cs` | `literal` | Gen 5 IVs (C-Gear Seed) | GEN5个体值（Ｃ装置 Seed） |
| `RNGReporter/MainForm.cs` | `literal` | Chained Shiny | 连锁异色 |
| `RNGReporter/MainForm.cs` | `literal` | Gen 4 Egg PID (Normal) | GEN4蛋PID（普通的） |
| `RNGReporter/MainForm.cs` | `literal` | Gen 4 Egg PID (International) | GEN4蛋PID（异国） |
| `RNGReporter/MainForm.cs` | `literal` | Breeding (Emerald No Splits) | 孵蛋（绿宝石 普通遗传） |
| `RNGReporter/MainForm.cs` | `literal` | Breeding (Emerald Splits) | 孵蛋（绿宝石 分裂遗传） |
| `RNGReporter/MainForm.cs` | `literal` | Breeding (Emerald Alternate) | 孵蛋（绿宝石 交替遗传） |
| `RNGReporter/MainForm.cs` | `literal` | Breeding (RSUpper) | 孵蛋（红蓝宝石） |
| `RNGReporter/MainForm.cs` | `literal` | Breeding (DPPt) | 孵蛋（钻石珍珠白金） |
| `RNGReporter/MainForm.cs` | `literal` | Breeding (HGSS) | 孵蛋（心金魂银） |
| `RNGReporter/MainForm.cs` | `literal` | Breeding (BW) | 孵蛋（黑白） |
| `RNGReporter/MainForm.cs` | `literal` | Breeding (BW, International) | 孵蛋（黑白，异国） |
| `RNGReporter/MainForm.cs` | `literal` | Wondercard IVs (4th Gen) | 神秘卡片个体值（GEN4） |
| `RNGReporter/MainForm.cs` | `literal` | Wondercard (5th Gen) | 神秘卡片（GEN5） |
| `RNGReporter/MainForm.cs` | `literal` | Colosseum\\XD | 圆形竞技场\\XD暗之旋风 |
| `RNGReporter/MainForm.cs` | `literal` | Channel | 宝可梦频道 |
| `RNGReporter/MainForm.cs` | `literal` | Male Lead (50% F Target) | 首发♂（目标50%♀) |
| `RNGReporter/MainForm.cs` | `literal` | Male Lead (75% F Target) | 首发♂（目标75%♀) |
| `RNGReporter/MainForm.cs` | `literal` | Male Lead (25% F Target) | 首发♂（目标25%♀) |
| `RNGReporter/MainForm.cs` | `literal` | Male Lead (12.5% F Target) | 首发♂（目标12.5%♀) |
| `RNGReporter/MainForm.cs` | `literal` | Female Lead (50% M Target) | 首发♀（目标50%♂) |
| `RNGReporter/MainForm.cs` | `literal` | Female Lead (75% M Target) | 首发♀（目标75%♂) |
| `RNGReporter/MainForm.cs` | `literal` | Female Lead (25% M Target) | 首发♀（目标25%♂) |
| `RNGReporter/MainForm.cs` | `literal` | Female Lead (87.5% M Target) | 首发♀（目标87.5%♂) |
| `RNGReporter/MainForm.cs` | `literal` | Any | 任意 |
| `RNGReporter/MainForm.cs` | `literal` | RNG Reporter has detected a corrupt configuration file, which has been deleted.  RNG Reporter must be restarted. | RNG Reporter检测到一个损坏的配置文件，该文件已被删除。RNG Reporter必须重启。 |
| `RNGReporter/MainForm.cs` | `literal` | RNG Reporter now has a new profile manager.\r\nPlease save your information in a profile. | RNG Reporter 现在有新的存档信息管理器。\r\n请将你的信息保存到存档信息中。 |
| `RNGReporter/MainForm.cs` | `literal` | Your version of RNG Reporter is outdated.  The latest version is  | 你的 RNG Reporter 版本已过期。最新版本是  |
| `RNGReporter/MainForm.cs` | `literal` | What's new:  | 新内容： |
| `RNGReporter/MainForm.cs` | `literal` | Would you like to download and install the latest version now? | 是否立即下载并安装最新版本？ |
| `RNGReporter/MainForm.cs` | `literal` | !!! | 异色 |
| `RNGReporter/MainForm.cs` | `literal` | Ratio | 比例 |
| `RNGReporter/MainForm.cs` | `literal` | Nature | 性格 |
| `RNGReporter/MainForm.cs` | `literal` | Synchable | 同步能力 |
| `RNGReporter/MainForm.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/MainForm.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/MainForm.cs` | `literal` | Def | 防御 |
| `RNGReporter/MainForm.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/MainForm.cs` | `literal` | SpD | 特防 |
| `RNGReporter/MainForm.cs` | `literal` | Spe | 速度 |
| `RNGReporter/MainForm.cs` | `literal` | You need to adjust settings in Time Finder first. | 你需要先在 Time Finder 中调整设置。 |
| `RNGReporter/MainForm.cs` | `literal` | Frame | 帧 |
| `RNGReporter/MainForm.cs` | `literal` | Occidentary | 偶然值Occidentary |
| `RNGReporter/MainForm.cs` | `literal` | This method requires you to copy the Full Seed from the Time Finder window. | 此方法需要你从 Time Finder 窗口复制 Full Seed。 |
| `RNGReporter/MainForm.cs` | `literal` | Frame(s) Advanced:  | 游走消耗的帧数:  |
| `RNGReporter/MainForm.cs` | `literal` | You need to import a Wonder Card (.pgf file) first. Import one now? | 你需要先导入神秘卡片（.pgf 文件）。现在导入吗？ |
| `RNGReporter/MainForm.cs` | `literal` | Warning | 警告 |
| `RNGReporter/MainForm.cs` | `literal` | Time | 时间 |
| `RNGReporter/MainForm.cs` | `literal` | Cave Spot | 卷尘地面 |
| `RNGReporter/MainForm.cs` | `literal` | Bubble Spot | 水纹水面 |
| `RNGReporter/MainForm.cs` | `literal` | Fishing Spot | 钓鱼点 |
| `RNGReporter/MainForm.cs` | `literal` | Shaking Grass | 摇动草丛 |
| `RNGReporter/MainForm.cs` | `literal` | Display Characteristics in Search... | 在计算结果中显示个性 |
| `RNGReporter/MainForm.cs` | `literal` | Reset Characteristics | 重置个性 |
| `RNGReporter/MainForm.cs` | `literal` | Display Parents in Search... | 在搜索中显示父母... |
| `RNGReporter/MainForm.cs` | `literal` | Reset Parents | 重置父母 |
| `RNGReporter/MainForm.cs` | `literal` | None | 无 |
| `RNGReporter/MainForm.cs` | `literal` | No matches found for the sequence of responses entered. | 输入的响应序列未找到匹配项。 |
| `RNGReporter/MainForm.cs` | `literal` | No Match Found | 未找到匹配项 |
| `RNGReporter/MainForm.cs` | `literal` | Save Output to TXT | 保存输出到 TXT |
| `RNGReporter/MainForm.cs` | `literal` | TXT Files\|*.txt | TXT 文件\|*.txt |
| `RNGReporter/MainForm.cs` | `literal` | Wild Pokémon (Old Rod) | 野生宝可梦（破旧钓竿） |
| `RNGReporter/MainForm.cs` | `literal` | Wild Pokémon (Good Rod) | 野生宝可梦（好钓竿） |
| `RNGReporter/MainForm.cs` | `literal` | Wild Pokémon (Super Rod) | 野生宝可梦（厉害钓竿） |
| `RNGReporter/MainForm.cs` | `literal` | Stationary Pokémon | 定点宝可梦 |
| `RNGReporter/MainForm.cs` | `literal` | Safari Zone | 狩猎地带 |
| `RNGReporter/MainForm.cs` | `literal` | Headbutt | 头锤树 |
| `RNGReporter/MainForm.cs` | `literal` | Wild Pokémon (Swarm) | 野生宝可梦（虫之预感） |
| `RNGReporter/MainForm.cs` | `literal` | Wild Pokémon (Shaking Grass) | 野生宝可梦（摇动草丛） |
| `RNGReporter/MainForm.cs` | `literal` | Wild Pokémon (Bubble Spot) | 野生宝可梦（水纹水面） |
| `RNGReporter/MainForm.cs` | `literal` | Wild Pokémon (Cave Spot) | 野生宝可梦（卷尘地面） |
| `RNGReporter/MainForm.cs` | `literal` | Gift Pokémon | 礼物宝可梦 |
| `RNGReporter/MainForm.cs` | `literal` | Entralink Pokémon | 连入之森宝可梦 |
| `RNGReporter/MainForm.cs` | `literal` | Normal Wondercard | 普通神秘卡片 |
| `RNGReporter/MainForm.cs` | `literal` | Manaphy Egg | 玛纳霏的蛋 |
| `RNGReporter/MainForm.cs` | `literal` | Cannot display Japanese without a Japanese-supported font. | 没有支持日文的字体，无法显示日文。 |
| `RNGReporter/MainForm.cs` | `literal` | Unsupported Language | 不支持的语言 |
| `RNGReporter/MainForm.cs` | `literal` | Cannot display Korean without a Korean-supported font. | 没有支持韩文的字体，无法显示韩文。 |
| `RNGReporter/MainForm.cs` | `literal` | Chatot Pitch | 聒噪鸟音高 |
| `RNGReporter/MainForm.cs` | `literal` | Greyed-out natures are natures with no competitive value. | 灰色字体的性格是没有竞争价值的性格。 |
| `RNGReporter/MainForm.cs` | `literal` | A !!! in this column indicates the frame will be shiny. | 如果该帧的异色列有!!!则说明该帧是异色 |
| `RNGReporter/MainForm.cs` | `literal` | Offset | 偏移 |
| `RNGReporter/MainForm.cs` | `literal` | The frame of the RNG after a battle is equal to the occidentary + 6. | 该值是对战结束后的帧数，宝可梦对战后的帧数等于偶然值+6，该值一般作用于大湿地等场景 |
| `RNGReporter/MainForm.cs` | `literal` | Encounter Slot | 遭遇槽 |
| `RNGReporter/MainForm.cs` | `literal` | Possible Cave Spot | 可能的洞穴尘点 |
| `RNGReporter/MainForm.cs` | `literal` | Possible Bubble Spot | 可能的水泡点 |
| `RNGReporter/MainForm.cs` | `literal` | Possible Shaking Grass | 可能的摇晃草丛 |
| `RNGReporter/MainForm.cs` | `literal` | Entralink Time | 连入之森时间 |
| `RNGReporter/MainForm.cs` | `literal` | 5th Gen Wonder Card \|*.pgf | 第五世代神秘卡片 \|*.pgf |
| `RNGReporter/MainForm.cs` | `literal` | Select a Wonder Card File | 选择神秘卡片文件 |
| `RNGReporter/MainForm.cs` | `literal` | Wonder Card loaded successfully: | 神秘卡片加载成功： |
| `RNGReporter/MainForm.cs` | `literal` | Nature:  | 性格:  |
| `RNGReporter/MainForm.cs` | `literal` | Random | 随机 |
| `RNGReporter/MainForm.cs` | `literal` | Ability:  | 特性:  |
| `RNGReporter/MainForm.cs` | `literal` | Gender:  | 性别:  |
| `RNGReporter/MainForm.cs` | `literal` | Male | 雄性 |
| `RNGReporter/MainForm.cs` | `literal` | Female | 雌性 |
| `RNGReporter/MainForm.cs` | `literal` | Shininess:  | 闪光:  |
| `RNGReporter/MainForm.cs` | `literal` | May be Shiny | 可能闪光 |
| `RNGReporter/MainForm.cs` | `literal` | Never Shiny | 不可能异色 |
| `RNGReporter/MainForm.cs` | `literal` | Always Shiny | 必定异色 |
| `RNGReporter/MainForm.cs` | `literal` | Atk:  | 攻击:  |
| `RNGReporter/MainForm.cs` | `literal` | Def:  | 防御:  |
| `RNGReporter/MainForm.cs` | `literal` | SpA:  | 特攻:  |
| `RNGReporter/MainForm.cs` | `literal` | SpD:  | 特防:  |
| `RNGReporter/MainForm.cs` | `literal` | Spe:  | 速度:  |
| `RNGReporter/MainForm.cs` | `literal` | Info | 信息 |
| `RNGReporter/Objects/CSVWriter.cs` | `literal` | Flip Sequence | 硬币序列 |
| `RNGReporter/Objects/CalculateChainSid.cs` | `literal` | Single Ability | 只有一个特性 |
| `RNGReporter/Objects/DisplayList.cs` | `literal` | Nature | 性格 |
| `RNGReporter/Objects/DisplayList.cs` | `literal` | Ability | 特性 |
| `RNGReporter/Objects/DisplayList.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/Objects/DisplayList.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/Objects/DisplayList.cs` | `literal` | Def | 防御 |
| `RNGReporter/Objects/DisplayList.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/Objects/DisplayList.cs` | `literal` | SpD | 特防 |
| `RNGReporter/Objects/DisplayList.cs` | `literal` | Spe | 速度 |
| `RNGReporter/Objects/DisplayList.cs` | `literal` | Power | 威力 |
| `RNGReporter/Objects/EggSeedSearcher.cs` | `literal` | You do not have enough free memory to load {0} for the fast egg search. | 可用内存不足，无法为快速蛋搜索加载 {0}。 |
| `RNGReporter/Objects/EggSeedSearcher.cs` | `literal` | Problem loading {0} for the fast egg search:\r\n{1} | 为快速蛋搜索加载 {0} 时出现问题：\r\n{1} |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | None | 无 |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Synchronize | 同步 |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Cute Charm | 迷人之躯 |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Suction Cups | 吸盘 |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Compoundeyes | 复眼 |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Everstone | 不变之石 |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Wild Pokémon (Old Rod) | 野生宝可梦（破旧钓竿） |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Wild Pokémon (Good Rod) | 野生宝可梦（好钓竿） |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Wild Pokémon (Super Rod) | 野生宝可梦（厉害钓竿） |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Wild Pokémon (Swarm) | 野生宝可梦（虫之预感） |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Wild Pokémon (Shaking Grass) | 野生宝可梦（摇动草丛） |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Wild Pokémon (Bubble Spot) | 野生宝可梦（水纹水面） |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Wild Pokémon (Cave Spot) | 野生宝可梦（卷尘地面） |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Stationary Pokémon | 定点宝可梦 |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Gift Pokémon | 礼物宝可梦 |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Entralink Pokémon | 连入之森宝可梦 |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Safari Zone | 狩猎地带 |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Manaphy Egg | 玛纳霏的蛋 |
| `RNGReporter/Objects/EncounterMods.cs` | `literal` | Headbutt | 头锤树 |
| `RNGReporter/Objects/Frame.cs` | `literal` | None | 无 |
| `RNGReporter/Objects/Frame.cs` | `literal` | !!! | 异色 |
| `RNGReporter/Objects/Functions.cs` | `literal` | None | 无 |
| `RNGReporter/Objects/Functions.cs` | `literal` | R | 雷公 |
| `RNGReporter/Objects/Functions.cs` | `literal` | L | 拉帝欧斯\\拉迪亚斯 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Any | 任意 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Hardy | 勤奋 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Lonely | 怕寂寞 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Brave | 勇敢 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Adamant | 固执 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Naughty | 顽皮 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Bold | 大胆 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Docile | 坦率 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Relaxed | 悠闲 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Impish | 淘气 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Lax | 乐天 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Timid | 胆小 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Hasty | 急躁 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Serious | 认真 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Jolly | 爽朗 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Naive | 天真 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Modest | 内敛 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Mild | 慢吞吞 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Quiet | 冷静 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Bashful | 害羞 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Rash | 马虎 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Calm | 温和 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Gentle | 温顺 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Sassy | 自大 |
| `RNGReporter/Objects/Functions.cs` | `literal` | Careful | 慎重 |
| `RNGReporter/Objects/GenderGenderRatio.cs` | `literal` | Genderless | 无性别 |
| `RNGReporter/Objects/GenderGenderRatio.cs` | `literal` | Male (100% Male) | ♂(只有♂) |
| `RNGReporter/Objects/GenderGenderRatio.cs` | `literal` | Female (100% Female) | ♀(只有♀) |
| `RNGReporter/Objects/GenderGenderRatio.cs` | `literal` | Don't Care / Genderless / Fixed Gender | 不考虑/无性别/固定性别 |
| `RNGReporter/Objects/GenderGenderRatio.cs` | `literal` | Don't Care / Genderless | 不考虑/无性别 |
| `RNGReporter/Objects/IDList.cs` | `literal` | Seconds | 秒数 |
| `RNGReporter/Objects/IDList.cs` | `literal` | Initial Frame | 初始帧 |
| `RNGReporter/Objects/IDList.cs` | `literal` | Frame | 帧 |
| `RNGReporter/Objects/IFrameCapture.cs` | `literal` | Hour | 时 |
| `RNGReporter/Objects/IFrameCapture.cs` | `literal` | Offset | 偏移 |
| `RNGReporter/Objects/IFrameCapture.cs` | `literal` | Ability | 特性 |
| `RNGReporter/Objects/IFrameCapture.cs` | `literal` | Nature | 性格 |
| `RNGReporter/Objects/IFrameCapture.cs` | `literal` | Ratio | 比例 |
| `RNGReporter/Objects/IFrameCapture.cs` | `literal` | Level | 等级 |
| `RNGReporter/Objects/IFrameCapture.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/Objects/IFrameCapture.cs` | `literal` | Def | 防御 |
| `RNGReporter/Objects/IFrameCapture.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/Objects/IFrameCapture.cs` | `literal` | SpD | 特防 |
| `RNGReporter/Objects/IFrameCapture.cs` | `literal` | Spe | 速度 |
| `RNGReporter/Objects/IFrameEggPID.cs` | `literal` | !!! | 异色 |
| `RNGReporter/Objects/IFrameEggPID.cs` | `literal` | Offset | 偏移 |
| `RNGReporter/Objects/IFrameEggPID.cs` | `literal` | Ability | 特性 |
| `RNGReporter/Objects/IFrameEggPID.cs` | `literal` | Nature | 性格 |
| `RNGReporter/Objects/IFrameEggPID.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/Objects/IFrameEggPID.cs` | `literal` | Def | 防御 |
| `RNGReporter/Objects/IFrameEggPID.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/Objects/IFrameEggPID.cs` | `literal` | SpD | 特防 |
| `RNGReporter/Objects/IFrameEggPID.cs` | `literal` | Spe | 速度 |
| `RNGReporter/Objects/IFrameRSEggPID.cs` | `literal` | !!! | 异色 |
| `RNGReporter/Objects/IFrameRSEggPID.cs` | `literal` | Frame | 帧 |
| `RNGReporter/Objects/IVCheck.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/Objects/IVCheck.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/Objects/IVCheck.cs` | `literal` | Def | 防御 |
| `RNGReporter/Objects/IVCheck.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/Objects/IVCheck.cs` | `literal` | SpD | 特防 |
| `RNGReporter/Objects/IVCheck.cs` | `literal` | Spe | 速度 |
| `RNGReporter/Objects/IVCheck.cs` | `literal` | Invalid | 无效 |
| `RNGReporter/Objects/Language.cs` | `literal` | Fighting | 格斗 |
| `RNGReporter/Objects/Language.cs` | `literal` | Flying | 飞行 |
| `RNGReporter/Objects/Language.cs` | `literal` | Poison | 毒 |
| `RNGReporter/Objects/Language.cs` | `literal` | Ground | 地面 |
| `RNGReporter/Objects/Language.cs` | `literal` | Rock | 岩石 |
| `RNGReporter/Objects/Language.cs` | `literal` | Bug | 虫 |
| `RNGReporter/Objects/Language.cs` | `literal` | Ghost | 幽灵 |
| `RNGReporter/Objects/Language.cs` | `literal` | Steel | 钢 |
| `RNGReporter/Objects/Language.cs` | `literal` | Fire | 火 |
| `RNGReporter/Objects/Language.cs` | `literal` | Water | 水 |
| `RNGReporter/Objects/Language.cs` | `literal` | Grass | 草 |
| `RNGReporter/Objects/Language.cs` | `literal` | Electric | 电 |
| `RNGReporter/Objects/Language.cs` | `literal` | Psychic | 超能 |
| `RNGReporter/Objects/Language.cs` | `literal` | Ice | 冰 |
| `RNGReporter/Objects/Language.cs` | `literal` | Dragon | 龙 |
| `RNGReporter/Objects/Language.cs` | `literal` | Dark | 恶 |
| `RNGReporter/Objects/Language.cs` | `literal` | Mild | 慢吞吞 |
| `RNGReporter/Objects/Language.cs` | `literal` | Brave | 勇敢 |
| `RNGReporter/Objects/Language.cs` | `literal` | Docile | 坦率 |
| `RNGReporter/Objects/Language.cs` | `literal` | Everstone | 不变之石 |
| `RNGReporter/Objects/Language.cs` | `literal` | Butterfree | 巴大蝶 |
| `RNGReporter/Objects/Language.cs` | `literal` | Beedrill | 大针蜂 |
| `RNGReporter/Objects/Language.cs` | `literal` | Pidgeotto | 比比鸟 |
| `RNGReporter/Objects/Language.cs` | `literal` | Raticate | 拉达 |
| `RNGReporter/Objects/Language.cs` | `literal` | Spearow | 烈雀 |
| `RNGReporter/Objects/Language.cs` | `literal` | Arbok | 阿柏怪 |
| `RNGReporter/Objects/Language.cs` | `literal` | Vulpix | 六尾 |
| `RNGReporter/Objects/Language.cs` | `literal` | Paras | 派拉斯 |
| `RNGReporter/Objects/Language.cs` | `literal` | Venomoth | 摩鲁蛾 |
| `RNGReporter/Objects/Language.cs` | `literal` | Dugtrio | 三地鼠 |
| `RNGReporter/Objects/Language.cs` | `literal` | Meowth | 喵喵 |
| `RNGReporter/Objects/Language.cs` | `literal` | Golduck | 哥达鸭 |
| `RNGReporter/Objects/Language.cs` | `literal` | Primeape | 火暴猴 |
| `RNGReporter/Objects/Language.cs` | `literal` | Growlithe | 卡蒂狗 |
| `RNGReporter/Objects/Language.cs` | `literal` | Poliwrath | 蚊香泳士 |
| `RNGReporter/Objects/Language.cs` | `literal` | Weepinbell | 口呆花 |
| `RNGReporter/Objects/Language.cs` | `literal` | Rapidash | 烈焰马 |
| `RNGReporter/Objects/Language.cs` | `literal` | Magneton | 三合一磁怪 |
| `RNGReporter/Objects/Language.cs` | `literal` | Farfetch'd | 大葱鸭 |
| `RNGReporter/Objects/Language.cs` | `literal` | Dodrio | 嘟嘟利 |
| `RNGReporter/Objects/Language.cs` | `literal` | Seel | 小海狮 |
| `RNGReporter/Objects/Language.cs` | `literal` | Grimer | 臭泥 |
| `RNGReporter/Objects/Language.cs` | `literal` | Shellder | 大舌贝 |
| `RNGReporter/Objects/Language.cs` | `literal` | Hypno | 引梦貘人 |
| `RNGReporter/Objects/Language.cs` | `literal` | Voltorb | 霹雳电球 |
| `RNGReporter/Objects/Language.cs` | `literal` | Exeggutor | 椰蛋树 |
| `RNGReporter/Objects/Language.cs` | `literal` | Marowak | 嘎啦嘎啦 |
| `RNGReporter/Objects/Language.cs` | `literal` | Hitmonlee | 飞腿郎 |
| `RNGReporter/Objects/Language.cs` | `literal` | Hitmonchan | 快拳郎 |
| `RNGReporter/Objects/Language.cs` | `literal` | Lickitung | 大舌头 |
| `RNGReporter/Objects/Language.cs` | `literal` | Rhydon | 钻角犀兽 |
| `RNGReporter/Objects/Language.cs` | `literal` | Chansey | 吉利蛋 |
| `RNGReporter/Objects/Language.cs` | `literal` | Tangela | 蔓藤怪 |
| `RNGReporter/Objects/Language.cs` | `literal` | Kangaskhan | 袋兽 |
| `RNGReporter/Objects/Language.cs` | `literal` | Starmie | 宝石海星 |
| `RNGReporter/Objects/Language.cs` | `literal` | Mr. Mime | 魔墙人偶 |
| `RNGReporter/Objects/Language.cs` | `literal` | Scyther | 飞天螳螂 |
| `RNGReporter/Objects/Language.cs` | `literal` | Electabuzz | 电击兽 |
| `RNGReporter/Objects/Language.cs` | `literal` | Magmar | 鸭嘴火兽 |
| `RNGReporter/Objects/Language.cs` | `literal` | Pinsir | 凯罗斯 |
| `RNGReporter/Objects/Language.cs` | `literal` | Tauros | 肯泰罗 |
| `RNGReporter/Objects/Language.cs` | `literal` | Lapras | 拉普拉斯 |
| `RNGReporter/Objects/Language.cs` | `literal` | Eevee | 伊布 |
| `RNGReporter/Objects/Language.cs` | `literal` | Snorlax | 卡比兽 |
| `RNGReporter/Objects/Language.cs` | `literal` | Articuno | 急冻鸟 |
| `RNGReporter/Objects/Language.cs` | `literal` | Zapdos | 闪电鸟 |
| `RNGReporter/Objects/Language.cs` | `literal` | Moltres | 火焰鸟 |
| `RNGReporter/Objects/Language.cs` | `literal` | Dragonite | 快龙 |
| `RNGReporter/Objects/Language.cs` | `literal` | Ledyba | 芭瓢虫 |
| `RNGReporter/Objects/Language.cs` | `literal` | Spinarak | 圆丝蛛 |
| `RNGReporter/Objects/Language.cs` | `literal` | Togepi | 波克比 |
| `RNGReporter/Objects/Language.cs` | `literal` | Natu | 天然雀 |
| `RNGReporter/Objects/Language.cs` | `literal` | Murkrow | 黑暗鸦 |
| `RNGReporter/Objects/Language.cs` | `literal` | Pineco | 榛果球 |
| `RNGReporter/Objects/Language.cs` | `literal` | Gligar | 天蝎 |
| `RNGReporter/Objects/Language.cs` | `literal` | Heracross | 赫拉克罗斯 |
| `RNGReporter/Objects/Language.cs` | `literal` | Teddiursa | 熊宝宝 |
| `RNGReporter/Objects/Language.cs` | `literal` | Ursaring | 圈圈熊 |
| `RNGReporter/Objects/Language.cs` | `literal` | Magcargo | 熔岩蜗牛 |
| `RNGReporter/Objects/Language.cs` | `literal` | Swinub | 小山猪 |
| `RNGReporter/Objects/Language.cs` | `literal` | Lugia | 洛奇亚 |
| `RNGReporter/Objects/Language.cs` | `literal` | Poochyena | 土狼犬 |
| `RNGReporter/Objects/Language.cs` | `literal` | Swellow | 大王燕 |
| `RNGReporter/Objects/Language.cs` | `literal` | Ralts | 拉鲁拉丝 |
| `RNGReporter/Objects/Language.cs` | `literal` | Shroomish | 蘑蘑菇 |
| `RNGReporter/Objects/Language.cs` | `literal` | Makuhita | 幕下力士 |
| `RNGReporter/Objects/Language.cs` | `literal` | Nosepass | 朝北鼻 |
| `RNGReporter/Objects/Language.cs` | `literal` | Delcatty | 优雅猫 |
| `RNGReporter/Objects/Language.cs` | `literal` | Sableye | 勾魂眼 |
| `RNGReporter/Objects/Language.cs` | `literal` | Mawile | 大嘴娃 |
| `RNGReporter/Objects/Language.cs` | `literal` | Manectric | 雷电兽 |
| `RNGReporter/Objects/Language.cs` | `literal` | Roselia | 毒蔷薇 |
| `RNGReporter/Objects/Language.cs` | `literal` | Carvanha | 利牙鱼 |
| `RNGReporter/Objects/Language.cs` | `literal` | Numel | 呆火驼 |
| `RNGReporter/Objects/Language.cs` | `literal` | Altaria | 七夕青鸟 |
| `RNGReporter/Objects/Language.cs` | `literal` | Zangoose | 猫鼬斩 |
| `RNGReporter/Objects/Language.cs` | `literal` | Lunatone | 月石 |
| `RNGReporter/Objects/Language.cs` | `literal` | Solrock | 太阳岩 |
| `RNGReporter/Objects/Language.cs` | `literal` | Banette | 诅咒娃娃 |
| `RNGReporter/Objects/Language.cs` | `literal` | Duskull | 夜巡灵 |
| `RNGReporter/Objects/Language.cs` | `literal` | Snorunt | 雪童子 |
| `RNGReporter/Objects/Language.cs` | `literal` | Salamence | 暴飞龙 |
| `RNGReporter/Objects/Language.cs` | `literal` | Compoundeyes | 复眼 |
| `RNGReporter/Objects/Language.cs` | `literal` | Cute Charm | 迷人之躯 |
| `RNGReporter/Objects/Language.cs` | `literal` | Pickup | 拾取 |
| `RNGReporter/Objects/Language.cs` | `literal` | Suction Cups | 吸盘 |
| `RNGReporter/Objects/Language.cs` | `literal` | Synchronize | 同步 |
| `RNGReporter/Objects/Nature.cs` | `literal` | Any | 任意 |
| `RNGReporter/Objects/Profiles.cs` | `literal` | Corrupt or old format profiles detected. Unable to load. | 检测到损坏或旧格式的存档信息，无法加载。 |
| `RNGReporter/Objects/Profiles.cs` | `literal` | None | 无 |
| `RNGReporter/Objects/Responses.cs` | `literal` | E | 炎帝 |
| `RNGReporter/Objects/Responses.cs` | `literal` |  skipped)    |  跳过这几个电话序列)    |
| `RNGReporter/Objects/Searchers/Gen3Searcher.cs` | `literal` | Any | 任意 |
| `RNGReporter/Objects/Searchers/Gen3Searcher.cs` | `literal` | Offset | 偏移 |
| `RNGReporter/Objects/Searchers/HiddenGrottoSearcher.cs` | `literal` | It's impossible to hit hollow number {0} with {1} open hollows! | 有 {1} 个开放隐藏洞穴时无法命中第 {0} 个洞穴！ |
| `RNGReporter/Objects/Searchers/HiddenGrottoSearcher.cs` | `literal` | Error | 错误 |
| `RNGReporter/PIDToIVs.Designer.cs` | `copySeed.Text` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/PIDToIVs.Designer.cs` | `moveResultToMainForm.Text` | Move result to main window | 将该计算所有结果移动到主界面 |
| `RNGReporter/PIDToIVs.Designer.cs` | `moveIVsToMainForm.Text` | Move IVs to main window | 仅将该个体值结果移动到主界面 |
| `RNGReporter/PIDToIVs.Designer.cs` | `buttonGenerate.Text` | Generate | 计算 |
| `RNGReporter/PIDToIVs.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/PIDToIVs.Designer.cs` | `literal` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/PIDToIVs.Designer.cs` | `literal` | Move result to main window | 将该计算所有结果移动到主界面 |
| `RNGReporter/PIDToIVs.Designer.cs` | `literal` | Move IVs to main window | 仅将该个体值结果移动到主界面 |
| `RNGReporter/PIDToIVs.Designer.cs` | `literal` | Generate | 计算 |
| `RNGReporter/PIDToIVs.Designer.cs` | `literal` | PID To IVs | 根据PID计算个体值 |
| `RNGReporter/PIDToIVs.cs` | `literal` | Channel | 宝可梦频道 |
| `RNGReporter/Pandora.Designer.cs` | `grpShiny.Text` | Shiny PID | 异色PID（迷人之躯） |
| `RNGReporter/Pandora.Designer.cs` | `cbxShinyInf.Text` | Infinite Search | 无限地计算 |
| `RNGReporter/Pandora.Designer.cs` | `lblShinyTrainerID.Text` | Desired Trainer ID: | 想要的TID： |
| `RNGReporter/Pandora.Designer.cs` | `cbxSearchID.Text` | Search for Trainer ID | 搜索想要的TID（表ID） |
| `RNGReporter/Pandora.Designer.cs` | `btnShinyCancel.Text` | Cancel | 取消计算 |
| `RNGReporter/Pandora.Designer.cs` | `btnShinyGo.Text` | Find Compatible Seeds | 计算目标seed |
| `RNGReporter/Pandora.Designer.cs` | `lblShinyMaxDelay.Text` | Maximum Delay: | 最大Delay： |
| `RNGReporter/Pandora.Designer.cs` | `lblShinyMinDelay.Text` | Minimum Delay: | 最小Delay： |
| `RNGReporter/Pandora.Designer.cs` | `lblShinyYr.Text` | Year: | 年份： |
| `RNGReporter/Pandora.Designer.cs` | `lblShinyPID.Text` | Desired PID (Hex): | 想要的PID（Hex） |
| `RNGReporter/Pandora.Designer.cs` | `grpID.Text` | Trainer ID | TID（表ID） |
| `RNGReporter/Pandora.Designer.cs` | `cbxIDInf.Text` | Infinite Search | 无限地计算 |
| `RNGReporter/Pandora.Designer.cs` | `btnIDCancel.Text` | Cancel | 取消计算 |
| `RNGReporter/Pandora.Designer.cs` | `btnIDGo.Text` | Find Compatible Seeds | 计算目标seed |
| `RNGReporter/Pandora.Designer.cs` | `lblIDMaxDelay.Text` | Maximum Delay: | 最大Delay： |
| `RNGReporter/Pandora.Designer.cs` | `lblIDMinDelay.Text` | Minimum Delay: | 最小Delay： |
| `RNGReporter/Pandora.Designer.cs` | `lblIDYr.Text` | Year: | 年份： |
| `RNGReporter/Pandora.Designer.cs` | `lblSecretID.Text` | Desired Secret ID: | 想要的SID： |
| `RNGReporter/Pandora.Designer.cs` | `cbxSearchSID.Text` | Search for SID | 搜索想要的SID（里ID） |
| `RNGReporter/Pandora.Designer.cs` | `lblTrainerID.Text` | Desired Trainer ID: | 想要的TID |
| `RNGReporter/Pandora.Designer.cs` | `grpSeed.Text` | Seed Finder | 反查seed |
| `RNGReporter/Pandora.Designer.cs` | `lblSeedMaxDelay.Text` | Maximum Delay: | 最大Delay： |
| `RNGReporter/Pandora.Designer.cs` | `lblSeedMinDelay.Text` | Minimum Delay: | 最小Delay： |
| `RNGReporter/Pandora.Designer.cs` | `lblMinute.Text` | Minute: | 分钟： |
| `RNGReporter/Pandora.Designer.cs` | `lblHour.Text` | Hour: | 时： |
| `RNGReporter/Pandora.Designer.cs` | `lblSeedYr.Text` | Year: | 年份： |
| `RNGReporter/Pandora.Designer.cs` | `lblDay.Text` | Day: | 日： |
| `RNGReporter/Pandora.Designer.cs` | `btnSeedGo.Text` | Find Compatible Seeds | 反查目标seed |
| `RNGReporter/Pandora.Designer.cs` | `lblMonth.Text` | Month: | 月份： |
| `RNGReporter/Pandora.Designer.cs` | `lblIDObtained.Text` | Trainer ID Obtained: | 击中的TID： |
| `RNGReporter/Pandora.Designer.cs` | `lblAction.Text` | Awaiting Command | 等待操作... |
| `RNGReporter/Pandora.Designer.cs` | `copySeedToClipboardToolStripMenuItem1.Text` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/Pandora.Designer.cs` | `generateTimesToolStripMenuItem.Text` | Generate More Times ... | 复制seed到seed to time |
| `RNGReporter/Pandora.Designer.cs` | `lblSimple.Text` | Simple Seed to ID/SID Calculator | 根据seed简单地计算ID/SID |
| `RNGReporter/Pandora.Designer.cs` | `lblSeed.Text` | Seed (Hex): | Seed （16进制） |
| `RNGReporter/Pandora.Designer.cs` | `tabXDColo.Text` | XD/Colo | XD暗之旋风/圆形竞技场 |
| `RNGReporter/Pandora.Designer.cs` | `labelXDColo.Text` | This feature will only work for Gales of Darkness and Colosseum. | 此功能只适用于XD暗之旋风和Colo竞技场。 |
| `RNGReporter/Pandora.Designer.cs` | `genCancelXDColo.Text` | Cancel | 取消计算 |
| `RNGReporter/Pandora.Designer.cs` | `searchGenXDColo.Text` | Find ID Frames | 计算目标ID帧数 |
| `RNGReporter/Pandora.Designer.cs` | `groupBox7.Text` | Search Parameters | 计算参数 |
| `RNGReporter/Pandora.Designer.cs` | `label16.Text` | Min Frame: | 最小帧： |
| `RNGReporter/Pandora.Designer.cs` | `label17.Text` | Max Frame: | 最大帧： |
| `RNGReporter/Pandora.Designer.cs` | `groupBox6.Text` | Search By | 计算条件 |
| `RNGReporter/Pandora.Designer.cs` | `tabGen3FRLGE.Text` | Gen III FRLGE | GEN3 火红叶绿绿宝石 |
| `RNGReporter/Pandora.Designer.cs` | `label11.Text` | This feature will only work for Fire Red, Leaf Green, and Emerald. | 此功能只适用于火红，叶绿和绿宝石。 |
| `RNGReporter/Pandora.Designer.cs` | `groupBox5.Text` | Search Parameters | 计算参数 |
| `RNGReporter/Pandora.Designer.cs` | `label12.Text` | Min Frame: | 最小帧： |
| `RNGReporter/Pandora.Designer.cs` | `label14.Text` | Max Frame: | 最大帧： |
| `RNGReporter/Pandora.Designer.cs` | `groupBox2.Text` | Search By | 计算条件 |
| `RNGReporter/Pandora.Designer.cs` | `genCancelFRLGE.Text` | Cancel | 取消计算 |
| `RNGReporter/Pandora.Designer.cs` | `genSearchFRLGE.Text` | Find ID Frames | 计算目标ID帧数 |
| `RNGReporter/Pandora.Designer.cs` | `tabGen3RS.Text` | Gen III RS | GEN3 红/蓝宝石 |
| `RNGReporter/Pandora.Designer.cs` | `buttonIIICancel.Text` | Cancel | 取消计算 |
| `RNGReporter/Pandora.Designer.cs` | `groupBox4.Text` | Search Parameters | 计算参数 |
| `RNGReporter/Pandora.Designer.cs` | `radioButton1.Text` | Initial Seed: | 初始Seed： |
| `RNGReporter/Pandora.Designer.cs` | `radioButton2.Text` | Date: | 日期： |
| `RNGReporter/Pandora.Designer.cs` | `checkIIIClock.Text` | Dead Battery | 电池没电 |
| `RNGReporter/Pandora.Designer.cs` | `label5.Text` | Minute: | 分钟： |
| `RNGReporter/Pandora.Designer.cs` | `label6.Text` | Min Frame: | 最小帧： |
| `RNGReporter/Pandora.Designer.cs` | `label8.Text` | Hour: | 时： |
| `RNGReporter/Pandora.Designer.cs` | `label7.Text` | Max Frame: | 最大帧： |
| `RNGReporter/Pandora.Designer.cs` | `groupBox3.Text` | Search By | 计算条件 |
| `RNGReporter/Pandora.Designer.cs` | `buttonIIIFindFrames.Text` | Find ID Frames | 计算目标ID帧数 |
| `RNGReporter/Pandora.Designer.cs` | `labelBy.Text` | By WildEep | 由WildEep开发 |
| `RNGReporter/Pandora.Designer.cs` | `btnCredits.Text` | Credits | 感谢名单 |
| `RNGReporter/Pandora.Designer.cs` | `buttonVFindSeedHit.Text` | Find Seed Hit | 反查击中seed |
| `RNGReporter/Pandora.Designer.cs` | `groupVSeedFinder.Text` | Seed Finder | 反查seed |
| `RNGReporter/Pandora.Designer.cs` | `labelTIDReceived.Text` | ID Received | 击中的TID |
| `RNGReporter/Pandora.Designer.cs` | `labelVMinute.Text` | Minute: | 分钟： |
| `RNGReporter/Pandora.Designer.cs` | `labelVHour.Text` | Hour: | 时： |
| `RNGReporter/Pandora.Designer.cs` | `label1.Text` | Min/Max Sec: | 最小/最大秒数 |
| `RNGReporter/Pandora.Designer.cs` | `label3.Text` | Date: | 日期： |
| `RNGReporter/Pandora.Designer.cs` | `label2.Text` | Min/Max Frame: | 最小/最大帧： |
| `RNGReporter/Pandora.Designer.cs` | `groupVDSParams.Text` | DS Parameters | DS配置参数 |
| `RNGReporter/Pandora.Designer.cs` | `label4.Text` | Please note: only the min Timer0 is used. | 请注意:只使用最小的Timer0。 |
| `RNGReporter/Pandora.Designer.cs` | `buttonEditProfile.Text` | Edit | 编辑 |
| `RNGReporter/Pandora.Designer.cs` | `groupVPID.Text` | Search By | 计算条件 |
| `RNGReporter/Pandora.Designer.cs` | `labelVMaxFrame.Text` | Max Advances: | 最大帧： |
| `RNGReporter/Pandora.Designer.cs` | `checkVMonth.Text` | Search Entire Month | 日期范围改为整个月 |
| `RNGReporter/Pandora.Designer.cs` | `labelVDate.Text` | Date: | 日期： |
| `RNGReporter/Pandora.Designer.cs` | `buttonVFindSeeds.Text` | Search | 计算目标seed |
| `RNGReporter/Pandora.Designer.cs` | `buttonVCancel.Text` | Cancel | 取消计算 |
| `RNGReporter/Pandora.Designer.cs` | `clmFrame.HeaderText` | Frame | 帧 |
| `RNGReporter/Pandora.Designer.cs` | `clmInitialFrame.HeaderText` | Initial Frame | 初始帧 |
| `RNGReporter/Pandora.Designer.cs` | `clmSeconds.HeaderText` | Seconds | 秒数 |
| `RNGReporter/Pandora.Designer.cs` | `clmStarter.HeaderText` | Starter | 初始宝可梦 |
| `RNGReporter/Pandora.Designer.cs` | `clmDate.HeaderText` | Date | 日期 |
| `RNGReporter/Pandora.Designer.cs` | `clmTime.HeaderText` | Time | 时间 |
| `RNGReporter/Pandora.Designer.cs` | `clmButton.HeaderText` | Buttons | 按键 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Shiny PID | 异色PID（迷人之躯） |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Infinite Search | 无限地计算 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Desired Trainer ID: | 想要的TID： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Search for Trainer ID | 搜索想要的TID（表ID） |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Cancel | 取消计算 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Find Compatible Seeds | 计算目标seed |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Maximum Delay: | 最大Delay： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Minimum Delay: | 最小Delay： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Year: | 年份： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Desired PID (Hex): | 想要的PID（Hex） |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Trainer ID | TID（表ID） |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Desired Secret ID: | 想要的SID： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Search for SID | 搜索想要的SID（里ID） |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Desired Trainer ID: | 想要的TID |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Seed Finder | 反查seed |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Minute: | 分钟： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Hour: | 时： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Day: | 日： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Find Compatible Seeds | 反查目标seed |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Month: | 月份： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Trainer ID Obtained: | 击中的TID： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Awaiting Command | 等待操作... |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Generate More Times ... | 复制seed到seed to time |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Simple Seed to ID/SID Calculator | 根据seed简单地计算ID/SID |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Seed (Hex): | Seed （16进制） |
| `RNGReporter/Pandora.Designer.cs` | `literal` | XD/Colo | XD暗之旋风/圆形竞技场 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | This feature will only work for Gales of Darkness and Colosseum. | 此功能只适用于XD暗之旋风和Colo竞技场。 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Find ID Frames | 计算目标ID帧数 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Search Parameters | 计算参数 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Min Frame: | 最小帧： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Max Frame: | 最大帧： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Search By | 计算条件 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Enter the PID you want shiny. | 输入你想要的异色PID |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Enter the current PRNG state. | 进入当前PRNG状态 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Gen III FRLGE | GEN3 火红叶绿绿宝石 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | This feature will only work for Fire Red, Leaf Green, and Emerald. | 此功能只适用于火红，叶绿和绿宝石。 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Enter the TID you obtained. | 输入你获取的TID |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Gen III RS | GEN3 红/蓝宝石 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Initial Seed: | 初始Seed： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Date: | 日期： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Dead Battery | 电池没电 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Enter TID to search for here. | 在这里输入TID进行搜索 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Enter the full seed given by RNG Reporter. | 输入RNG Reporter给出的完整seed |
| `RNGReporter/Pandora.Designer.cs` | `literal` | By WildEep | 由WildEep开发 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Credits | 感谢名单 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Find Seed Hit | 反查击中seed |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Enter the minute you started your game/ | 输入你开始游戏的分钟数 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Enter the hour that you started the game. | 输入你开始游戏的时数 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | ID Received | 击中的TID |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Enter the ID you received here to see what seed you hit. | 输入你在这里获取的ID，看看你击中了什么seed |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Min/Max Sec: | 最小/最大秒数 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Min/Max Frame: | 最小/最大帧： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | DS Parameters | DS配置参数 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Please note: only the min Timer0 is used. | 请注意:只使用最小的Timer0。 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Edit | 编辑 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Max Advances: | 最大帧： |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Search Entire Month | 日期范围改为整个月 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Choose any day during the month you want to search. | 在一个月内选择您想要搜索的任何一天 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Search | 计算目标seed |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Frame | 帧 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Initial Frame | 初始帧 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Seconds | 秒数 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Starter | 初始宝可梦 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Date | 日期 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Time | 时间 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Keypress | 按键 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | Buttons | 按键 |
| `RNGReporter/Pandora.Designer.cs` | `literal` | \"Pandora\'s Box\" - ID\\SID Manipulation Tool | TID\\SID 计算器 （\"潘多拉魔盒\"） |
| `RNGReporter/Pandora.cs` | `literal` | Trainer ID | TID（表ID） |
| `RNGReporter/Pandora.cs` | `literal` | Seconds | 秒数 |
| `RNGReporter/Pandora.cs` | `literal` | No profiles were detected. Please setup a profile first. | 没有检测到GEN5的存档信息，请先新增一个存档信息。 |
| `RNGReporter/Pandora.cs` | `literal` | Many thanks to: | 特别感谢： |
| `RNGReporter/Pandora.cs` | `literal` | TCCPhreak, for the major research into Trainer ID generation | TCCPhreak，感谢其对训练家 ID 生成的主要研究 |
| `RNGReporter/Pandora.cs` | `literal` | LightningFusion, for providing a sample seed/ID combo for testing | LightningFusion，感谢其提供用于测试的 Seed/ID 示例组合 |
| `RNGReporter/Pandora.cs` | `literal` | mingot, for an easy way to search only viable seeds and other valuable coding advice | mingot，感谢其提供只搜索可行 Seed 的简便方法和其他宝贵编码建议 |
| `RNGReporter/Pandora.cs` | `literal` | http://hocomcast.net/~charltoncr/mt19937ar.htm for providing Mersenne Twister Code | http://hocomcast.net/~charltoncr/mt19937ar.htm，感谢其提供 Mersenne Twister 代码 |
| `RNGReporter/Pandora.cs` | `literal` | You, for downloading and enjoying this program | 你，感谢你下载并使用这个程序 |
| `RNGReporter/Pandora.cs` | `literal` | Credits! | 鸣谢！ |
| `RNGReporter/Pandora.cs` | `literal` | A recommended minimum delay value is 5000. | 推荐的最小Delay为5000 |
| `RNGReporter/Pandora.cs` | `literal` | Year must be between 2000 and 2099, inclusive. | 年份必须在2000年到2099年之间 |
| `RNGReporter/Pandora.cs` | `literal` | Trainer ID must be a value betwwen 0 and 65535, inclusive. | TID必须是一个介于0到65535之间（包括0和65535）的值 |
| `RNGReporter/Pandora.cs` | `literal` | Trainer ID must be between 0 and 65535. | TID必须是一个介于0到65535之间（包括0和65535）的值 |
| `RNGReporter/Pandora.cs` | `literal` | Secret ID must be between 0 and 65535. | SID必须是一个介于0到65535之间（包括0和65535）的值。 |
| `RNGReporter/Pandora.cs` | `literal` | Max delay must be greater than or equal to min delay. | 最大Delay必须大于或等于最小Delay。 |
| `RNGReporter/Pandora.cs` | `literal` | At least one of the required fields does not contain a number | 至少有一个必填字段不包含数字 |
| `RNGReporter/Pandora.cs` | `literal` | Invalid Year (2000 <= Year <= 2099) | 请输入正确输入年份（2000<=年份<=2099） |
| `RNGReporter/Pandora.cs` | `literal` | Invalid Trainer ID (0 <= ID <= 65535) | 请正确输入TID（0<=TID<=65535） |
| `RNGReporter/Pandora.cs` | `literal` | Invalid Month (1 <= Month <= 12) | 请正确输入月份（1<=月份<=12） |
| `RNGReporter/Pandora.cs` | `literal` | Invalid Day | 请正确输入日期 |
| `RNGReporter/Pandora.cs` | `literal` | Invalid Hour (0 <= Hour <= 23) | 请正确输入小时（0<=时<=23） |
| `RNGReporter/Pandora.cs` | `literal` | Invalid Minute (0 <= Minute <= 59) | 请正确输入分钟（0<=分钟<=59） |
| `RNGReporter/Pandora.cs` | `literal` | Error(s) Occurred | 发生错误 |
| `RNGReporter/Pandora.cs` | `literal` | Searching for Obtained ID Seeds... Seeds Found:  | 搜索已获得的ID seeds...已找到数量： |
| `RNGReporter/Pandora.cs` | `literal` | Desired Obtained Seed Search Completed! Seeds Found:  | 想要的已获取的seed搜索已完成！已找到数量： |
| `RNGReporter/Pandora.cs` | `literal` | Searching for Shiny Seeds (0% Complete)... Seeds Found:  | 搜索异色seed（已完成0%）...已找到数量： |
| `RNGReporter/Pandora.cs` | `literal` | % Complete)... Seeds Found:  | %）...已找到数量： |
| `RNGReporter/Pandora.cs` | `literal` | An error occurred. | 发生错误 |
| `RNGReporter/Pandora.cs` | `literal` | Shiny Seed Search Canceled. Seeds Found:  | 异色seed搜索已取消，已找到数量： |
| `RNGReporter/Pandora.cs` | `literal` | Shiny Seed Search Completed! Seeds Found:  | 异色seed搜索已完成！已找到数量： |
| `RNGReporter/Pandora.cs` | `literal` | Searching for Desired ID Seeds (0% Complete)... Seeds Found:  | 搜索想要的ID seed（已完成0%）...已找到数量： |
| `RNGReporter/Pandora.cs` | `literal` | Searching for Desired ID Seeds ( | 搜索想要的ID seed（已完成 |
| `RNGReporter/Pandora.cs` | `literal` | Desired ID Seed Search Canceled. Seeds Found:  | 想要的ID seed搜索已取消，已找到数量： |
| `RNGReporter/Pandora.cs` | `literal` | Desired ID Seed Search Completed! Seeds Found:  | 想要的ID seed搜索已完成！已找到数量： |
| `RNGReporter/Pandora.cs` | `literal` | Searching for Desired ID Seeds (Through 0 Delay, 0% Complete)... Seeds Found:  | 搜索想要的ID seed（已经过0Delay，0%）...已找到数量： |
| `RNGReporter/Pandora.cs` | `literal` | Searching for Desired ID Seeds (Through  | 搜索想要的ID seed（已经过 |
| `RNGReporter/Pandora.cs` | `literal` | Searching for Desired ID Seeds (Through | 搜索想要的ID seed（已经过 |
| `RNGReporter/Pandora.cs` | `literal` | An error occurred. Seeds Searched:  | 发生错误，已搜索seed： |
| `RNGReporter/Pandora.cs` | `literal` |  Delay), Seeds Found:  |  Delay），已找到数量： |
| `RNGReporter/Pandora.cs` | `literal` | Desired ID Seed Search Canceled. Seeds Searched:  | 想要的ID seed搜索已取消，已搜索seed： |
| `RNGReporter/Pandora.cs` | `literal` | Desired ID Seed Search Completed! Seeds Searched:  | 想要的ID seed搜索已完成！已搜索seed： |
| `RNGReporter/Pandora.cs` | `literal` | The seed field was left blank. | 请输入seed！ |
| `RNGReporter/Pandora.cs` | `literal` | Simple Seed to ID/SID conversion complete! | 简单的seed到ID/SID转换已完成！ |
| `RNGReporter/Pandora.cs` | `literal` | Searching for Shiny Seeds (Through 0 Delay, 0% Complete)... Seeds Found:  | 正在搜索异色seed（已经过0Delay，已完成0%）...已找到数量： |
| `RNGReporter/Pandora.cs` | `literal` | Searching for Shiny Seeds (Through  | 正在搜索异色seed（已经过 |
| `RNGReporter/Pandora.cs` | `literal` | The previous search is still running. | 上一次搜索仍在运行。 |
| `RNGReporter/Pandora.cs` | `literal` | IDs can only be between 0 and 65535 | ID 只能在 0 到 65535 之间 |
| `RNGReporter/Pandora.cs` | `literal` | Searching.. | 搜索中... |
| `RNGReporter/Pandora.cs` | `literal` | Something went wrong | 出错了 |
| `RNGReporter/Pandora.cs` | `literal` | Search stopped - results max reached. Narrow your search for better results. | 搜索已停止 - 结果已达上限，缩小搜索范围以获得更好的结果 |
| `RNGReporter/Pandora.cs` | `literal` | Done. - Awaiting Command | 完成了 -等待操作... |
| `RNGReporter/Pandora.cs` | `literal` | Something went wrong.\rMake sure all inputs necessary inputs contain a value. | 出错了\r请确保所有输入框都已经填入输入值 |
| `RNGReporter/Pandora.cs` | `literal` | Cancelled. - Awaiting Command | 取消了 -等待操作... |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `buttonOk.Text` | Ok | 确认 |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `label3.Text` | Min / Max Frames | 最小/最大帧 |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `label8.Text` | Seconds +\\- | 秒数+\\- |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `label2.Text` | Date Filter | 筛选日期 |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `label5.Text` | Select your target date\\time from the list. | 从列表中选择您的目标日期/时间 |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `Date.HeaderText` | Date | 日期 |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `Time.HeaderText` | Time | 时间 |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `literal` | Ok | 确认 |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `literal` | Min / Max Frames | 最小/最大帧 |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `literal` | Seconds +\\- | 秒数+\\- |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `literal` | Date Filter | 筛选日期 |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `literal` | Select your target date\\time from the list. | 从列表中选择您的目标日期/时间 |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/PlatinumTimeAdjacent.Designer.cs` | `literal` | Find Adjacent Spreads | 反查附近的差值（Pt） |
| `RNGReporter/PokeSpot.Designer.cs` | `L_mezapa.Text` | Nature | 性格 |
| `RNGReporter/PokeSpot.Designer.cs` | `L_sex.Text` | Gender | 性别比例 |
| `RNGReporter/PokeSpot.Designer.cs` | `L_ability.Text` | Ability | 特性 |
| `RNGReporter/PokeSpot.Designer.cs` | `Shiny_Check.Text` | Shiny Only | 仅异色 |
| `RNGReporter/PokeSpot.Designer.cs` | `label3.Text` | PokeSpot Type | 宝可场所类型 |
| `RNGReporter/PokeSpot.Designer.cs` | `label5.Text` | Max Frame | 最大帧 |
| `RNGReporter/PokeSpot.Designer.cs` | `Frame.HeaderText` | Frame | 帧数 |
| `RNGReporter/PokeSpot.Designer.cs` | `dataGridViewTextBoxColumn2.HeaderText` | !!! | 异色 |
| `RNGReporter/PokeSpot.Designer.cs` | `Type.HeaderText` | Type | 类型 |
| `RNGReporter/PokeSpot.Designer.cs` | `dataGridViewTextBoxColumn3.HeaderText` | Nature | 性格 |
| `RNGReporter/PokeSpot.Designer.cs` | `dataGridViewTextBoxColumn4.HeaderText` | Ability | 特性 |
| `RNGReporter/PokeSpot.Designer.cs` | `anyPokeSpot.Text` | Any | 任意 |
| `RNGReporter/PokeSpot.Designer.cs` | `anyNature.Text` | Any | 任意 |
| `RNGReporter/PokeSpot.Designer.cs` | `anyGender.Text` | Any | 任意 |
| `RNGReporter/PokeSpot.Designer.cs` | `anyAbility.Text` | Any | 任意 |
| `RNGReporter/PokeSpot.Designer.cs` | `search.Text` | Generate | 计算 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Nature | 性格 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Don\'t Care / Genderless | 不考虑/无性别 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Male (100% Male) | ♂(只有♂) |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Female (100% Female) | ♀(只有♀) |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Gender | 性别比例 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Ability | 特性 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Any | 任意 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Ability 0 | 特性0 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Ability 1 | 特性1 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Shiny Only | 仅异色 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | PokeSpot Type | 宝可场所类型 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Max Frame | 最大帧 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Frame | 帧 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Frame | 帧数 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | !!! | 异色 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Type | 类型 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | Generate | 计算 |
| `RNGReporter/PokeSpot.Designer.cs` | `literal` | PokeSpot | 宝可场所PokeSpot（XD暗之旋风专属） |
| `RNGReporter/PokeSpot.cs` | `literal` | Hardy | 勤奋 |
| `RNGReporter/PokeSpot.cs` | `literal` | Lonely | 怕寂寞 |
| `RNGReporter/PokeSpot.cs` | `literal` | Brave | 勇敢 |
| `RNGReporter/PokeSpot.cs` | `literal` | Adamant | 固执 |
| `RNGReporter/PokeSpot.cs` | `literal` | Naughty | 顽皮 |
| `RNGReporter/PokeSpot.cs` | `literal` | Bold | 大胆 |
| `RNGReporter/PokeSpot.cs` | `literal` | Docile | 坦率 |
| `RNGReporter/PokeSpot.cs` | `literal` | Relaxed | 悠闲 |
| `RNGReporter/PokeSpot.cs` | `literal` | Impish | 淘气 |
| `RNGReporter/PokeSpot.cs` | `literal` | Lax | 乐天 |
| `RNGReporter/PokeSpot.cs` | `literal` | Timid | 胆小 |
| `RNGReporter/PokeSpot.cs` | `literal` | Hasty | 急躁 |
| `RNGReporter/PokeSpot.cs` | `literal` | Serious | 认真 |
| `RNGReporter/PokeSpot.cs` | `literal` | Jolly | 爽朗 |
| `RNGReporter/PokeSpot.cs` | `literal` | Naive | 天真 |
| `RNGReporter/PokeSpot.cs` | `literal` | Modest | 内敛 |
| `RNGReporter/PokeSpot.cs` | `literal` | Mild | 慢吞吞 |
| `RNGReporter/PokeSpot.cs` | `literal` | Quiet | 冷静 |
| `RNGReporter/PokeSpot.cs` | `literal` | Bashful | 害羞 |
| `RNGReporter/PokeSpot.cs` | `literal` | Rash | 马虎 |
| `RNGReporter/PokeSpot.cs` | `literal` | Calm | 温和 |
| `RNGReporter/PokeSpot.cs` | `literal` | Gentle | 温顺 |
| `RNGReporter/PokeSpot.cs` | `literal` | Sassy | 自大 |
| `RNGReporter/PokeSpot.cs` | `literal` | Careful | 慎重 |
| `RNGReporter/PokeSpot.cs` | `literal` | Quirky | 浮躁 |
| `RNGReporter/PokeSpot.cs` | `literal` | Any | 任意 |
| `RNGReporter/PokeSpot.cs` | `literal` | Common | 常见的 |
| `RNGReporter/PokeSpot.cs` | `literal` | Uncommon | 不常见的 |
| `RNGReporter/PokeSpot.cs` | `literal` | Rare | 稀有的 |
| `RNGReporter/PokeSpot.cs` | `literal` | !!! | 异色 |
| `RNGReporter/Poketech.Designer.cs` | `label2.Text` | Happiness Application Double Taps: | 双击亲密度检测器： |
| `RNGReporter/Poketech.Designer.cs` | `label3.Text` | Coin Flip Application Taps: | 点击掷硬币： |
| `RNGReporter/Poketech.Designer.cs` | `buttonOk.Text` | Ok | 确定 |
| `RNGReporter/Poketech.Designer.cs` | `literal` | Happiness Application Double Taps: | 双击亲密度检测器： |
| `RNGReporter/Poketech.Designer.cs` | `literal` | Coin Flip Application Taps: | 点击掷硬币： |
| `RNGReporter/Poketech.Designer.cs` | `literal` | Ok | 确定 |
| `RNGReporter/Poketech.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/Poketech.Designer.cs` | `literal` | Poketech Taps | 点击宝可表（DPPt） |
| `RNGReporter/Poketech.cs` | `literal` | DO NOT SWITCH TO THE HAPPINESS APPLICATION AT ALL | 请勿切换到亲密度检测器 |
| `RNGReporter/Poketech.cs` | `literal` | SWITCH TO THE HAPPINESS APPLICATION ONCE BUT DO NOT CLICK | 切换到亲密度检测器，但不要点击 |
| `RNGReporter/ProfileEditor.Designer.cs` | `checkBoxSkipLR.Text` | Skip L\\R Buttons | 跳过含L\\R按键的搜索结果 |
| `RNGReporter/ProfileEditor.Designer.cs` | `btnParameters.Text` | Find DS Parameters | 校准计算DS参数 |
| `RNGReporter/ProfileEditor.Designer.cs` | `label71.Text` | DS Type | DS机型 |
| `RNGReporter/ProfileEditor.Designer.cs` | `label49.Text` | Timer0 Min | 最小Timer0 |
| `RNGReporter/ProfileEditor.Designer.cs` | `label53.Text` | Timer0 Max | 最大Timer0 |
| `RNGReporter/ProfileEditor.Designer.cs` | `label51.Text` | Keypresses | 按键 |
| `RNGReporter/ProfileEditor.Designer.cs` | `label50.Text` | Version | 游戏版本 |
| `RNGReporter/ProfileEditor.Designer.cs` | `checkBoxSoftReset.Text` | Soft Reset | 软复位 |
| `RNGReporter/ProfileEditor.Designer.cs` | `labelMACAddress.Text` | DS MAC Address | DS MAC 地址 |
| `RNGReporter/ProfileEditor.Designer.cs` | `label41.Text` | Profile Name | 存档名称 |
| `RNGReporter/ProfileEditor.Designer.cs` | `btnOK.Text` | &OK | 确认 |
| `RNGReporter/ProfileEditor.Designer.cs` | `btnCancel.Text` | &Cancel | 关闭 |
| `RNGReporter/ProfileEditor.Designer.cs` | `checkBoxMemoryLink.Text` | Memory Link Activated | 记忆连接 |
| `RNGReporter/ProfileEditor.Designer.cs` | `label1.Text` | Language | 游戏语言 |
| `RNGReporter/ProfileEditor.Designer.cs` | `checkBoxShinyCharm.Text` | Shiny Charm | 闪耀护符 |
| `RNGReporter/ProfileEditor.Designer.cs` | `label2.Text` | Lucky Power Level | 幸运之力等级 |
| `RNGReporter/ProfileEditor.Designer.cs` | `labelLuckyPower.Text` | Lucky Power Note | 幸运之力备注 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Skip L\\R Buttons | 跳过含L\\R按键的搜索结果 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Find DS Parameters | 校准计算DS参数 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Any | 任意 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | None | 无 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | DS Type | DS机型 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Timer0 Min | 最小Timer0 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Timer0 Max | 最大Timer0 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Keypresses | 按键 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Version | 游戏版本 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Soft Reset | 软复位 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Black | 黑 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | White | 白 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Black 2 | 黑2 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | White 2 | 白2 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | DS MAC Address | DS MAC 地址 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Profile Name | 存档名称 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | &OK | 确认 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | &Cancel | 关闭 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Memory Link Activated | 记忆连接 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Language | 游戏语言 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Shiny Charm | 闪耀护符 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Lucky Power Level | 幸运之力等级 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | Lucky Power Note | 幸运之力备注 |
| `RNGReporter/ProfileEditor.Designer.cs` | `literal` | ProfileEditor | 存档信息编辑（GEN5） |
| `RNGReporter/ProfileEditor.cs` | `literal` | Note: Use this field only if you \nare willing to use Pass Powers \nthrough Entralink. | 注意: 仅当你愿意通过连入\n使用释出之力时才填写此字段。 |
| `RNGReporter/ProfileEditor.cs` | `literal` | The inputed profile data in invalid. The profile can not be saved.\r\nWould you like to continue editing this profile? | 输入的配置文件数据无效，无法保存配置文件。\r\n您要继续编辑此配置文件吗？ |
| `RNGReporter/ProfileEditor.cs` | `literal` | Warning | 警告 |
| `RNGReporter/ProfileEditor.cs` | `literal` | Warning: this version of the game is currently unsupported. | 警告：目前不支持此版本的游戏 |
| `RNGReporter/ProfileEditor.cs` | `literal` | Unsupported game:  | 不支持的游戏： |
| `RNGReporter/ProfileEditor.cs` | `literal` | We currently do not have information to be able to support this version of the game. Would you like to help out with adding support? | 我们目前没有能够支持这个版本的游戏的信息。你愿意帮忙增加支持吗? |
| `RNGReporter/ProfilesManager.Designer.cs` | `menuStrip1.Text` | menuStrip | 菜单栏 |
| `RNGReporter/ProfilesManager.Designer.cs` | `fileToolStripMenuItem.Text` | &File | 文件 |
| `RNGReporter/ProfilesManager.Designer.cs` | `newToolStripMenuItem.Text` | &New | 新建 |
| `RNGReporter/ProfilesManager.Designer.cs` | `openToolStripMenuItem.Text` | &Open | 打开 |
| `RNGReporter/ProfilesManager.Designer.cs` | `saveToolStripMenuItem.Text` | &Save | 保存 |
| `RNGReporter/ProfilesManager.Designer.cs` | `openFileDialogXml.Filter` | XML Profiles\|*.xml\|All files\|*.* | XML 存档信息\|*.xml\|所有文件\|*.* |
| `RNGReporter/ProfilesManager.Designer.cs` | `buttonDuplicate.Text` | Duplicate | 复制 |
| `RNGReporter/ProfilesManager.Designer.cs` | `buttonEdit.Text` | Edit | 编辑 |
| `RNGReporter/ProfilesManager.Designer.cs` | `buttonDelete.Text` | Delete | 删除 |
| `RNGReporter/ProfilesManager.Designer.cs` | `buttonNew.Text` | New | 新建 |
| `RNGReporter/ProfilesManager.Designer.cs` | `profileName.HeaderText` | Name | 名称 |
| `RNGReporter/ProfilesManager.Designer.cs` | `profileMAC.HeaderText` | MAC Address | MAC地址 |
| `RNGReporter/ProfilesManager.Designer.cs` | `profileVersion.HeaderText` | Version | 游戏版本 |
| `RNGReporter/ProfilesManager.Designer.cs` | `DSType.HeaderText` | DSType | DS机型 |
| `RNGReporter/ProfilesManager.Designer.cs` | `profileTimer0Min.HeaderText` | Timer0 Min | 最小Timer0 |
| `RNGReporter/ProfilesManager.Designer.cs` | `profileTimer0Max.HeaderText` | Timer0 Max | 最大Timer0 |
| `RNGReporter/ProfilesManager.Designer.cs` | `profileKeypresses.HeaderText` | Keypresses | 按键 |
| `RNGReporter/ProfilesManager.Designer.cs` | `SkipLR.HeaderText` | Skip L\\R | 跳过L\\R按键 |
| `RNGReporter/ProfilesManager.Designer.cs` | `profileSoftReset.HeaderText` | Soft-Reset | 软复位 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | Save Profiles... | 保存存档信息... |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | menuStrip1 | 菜单栏1 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | menuStrip | 菜单栏 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | &File | 文件 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | &New | 新建 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | &Open | 打开 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | &Save | 保存 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | XML Profiles\|*.xml\|All files\|*.* | XML 存档信息\|*.xml\|所有文件\|*.* |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | Open Profiles... | 打开存档信息... |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | Duplicate | 复制 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | Edit | 编辑 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | Delete | 删除 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | New | 新建 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | Name | 名称 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | MAC Address | MAC地址 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | Version | 游戏版本 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | DSType | DS机型 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | Timer0 Min | 最小Timer0 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | Timer0 Max | 最大Timer0 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | Keypresses | 按键 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | Skip L\\R | 跳过L\\R按键 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | Soft-Reset | 软复位 |
| `RNGReporter/ProfilesManager.Designer.cs` | `literal` | RNG Profiles | 存档信息管理（GEN5） |
| `RNGReporter/Progress.Designer.cs` | `label1.Text` | Found | 找到目标的数量 |
| `RNGReporter/Progress.Designer.cs` | `label2.Text` | Searched | 计算数量 |
| `RNGReporter/Progress.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/Progress.Designer.cs` | `buttonPause.Text` | Pause | 暂停 |
| `RNGReporter/Progress.Designer.cs` | `literal` | Found | 找到目标的数量 |
| `RNGReporter/Progress.Designer.cs` | `literal` | Searched | 计算数量 |
| `RNGReporter/Progress.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/Progress.Designer.cs` | `literal` | Pause | 暂停 |
| `RNGReporter/Progress.Designer.cs` | `literal` | Time Finder Progress | Time Finder 计算进度 |
| `RNGReporter/Progress.cs` | `literal` | Operation Cancelled | 操作被取消 |
| `RNGReporter/Progress.cs` | `literal` | Pause | 暂停 |
| `RNGReporter/Progress.cs` | `literal` | Resume | 重新开始 |
| `RNGReporter/Properties/Settings.Designer.cs` | `literal` | Year | 年份 |
| `RNGReporter/Properties/Settings.Designer.cs` | `literal` | Month | 月份 |
| `RNGReporter/Properties/Settings.Designer.cs` | `literal` | Date | 日期 |
| `RNGReporter/Properties/Settings.Designer.cs` | `literal` | Seconds | 秒数 |
| `RNGReporter/Researcher.Designer.cs` | `radioButtonCommon.Text` | Common RNGs | 常见的 RNGs |
| `RNGReporter/Researcher.Designer.cs` | `copyItemToolStripMenuItem.Text` | Copy Item | 复制Item |
| `RNGReporter/Researcher.Designer.cs` | `copySelectedColumnsToolStripMenuItem.Text` | Copy Selected Columns | 复制选中的列 |
| `RNGReporter/Researcher.Designer.cs` | `copyColumnToolStripMenuItem.Text` | Copy Row from Selected Columns | 从选定列复制行 |
| `RNGReporter/Researcher.Designer.cs` | `outputResultsToTXTToolStripMenuItem.Text` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/Researcher.Designer.cs` | `outputSelectedColumnsToTXTToolStripMenuItem.Text` | Output Selected Columns to TXT... | 将选定列输出到TXT文本文件... |
| `RNGReporter/Researcher.Designer.cs` | `radioButtonCustom.Text` | Custom | 自定义 |
| `RNGReporter/Researcher.Designer.cs` | `label3.Text` | Custom 1 | 自定义 1 |
| `RNGReporter/Researcher.Designer.cs` | `label4.Text` | Custom 2 | 自定义 2 |
| `RNGReporter/Researcher.Designer.cs` | `label5.Text` | Custom 3 | 自定义 3 |
| `RNGReporter/Researcher.Designer.cs` | `label6.Text` | Custom 4 | 自定义 4 |
| `RNGReporter/Researcher.Designer.cs` | `label10.Text` | Max Results | 最大帧 |
| `RNGReporter/Researcher.Designer.cs` | `checkBoxCustom1Hex.Text` | Hex | 16进制 |
| `RNGReporter/Researcher.Designer.cs` | `checkBoxCustom2Hex.Text` | Hex | 16进制 |
| `RNGReporter/Researcher.Designer.cs` | `checkBoxCustom3Hex.Text` | Hex | 16进制 |
| `RNGReporter/Researcher.Designer.cs` | `checkBoxCustom4Hex.Text` | Hex | 16进制 |
| `RNGReporter/Researcher.Designer.cs` | `checkBoxCustom5Hex.Text` | Hex | 16进制 |
| `RNGReporter/Researcher.Designer.cs` | `label7.Text` | Custom 5 | 自定义 5 |
| `RNGReporter/Researcher.Designer.cs` | `checkBoxCustom6Hex.Text` | Hex | 16进制 |
| `RNGReporter/Researcher.Designer.cs` | `label8.Text` | Custom 6 | 自定义 6 |
| `RNGReporter/Researcher.Designer.cs` | `checkBoxCustom7Hex.Text` | Hex | 16进制 |
| `RNGReporter/Researcher.Designer.cs` | `label9.Text` | Custom 7 | 自定义 7 |
| `RNGReporter/Researcher.Designer.cs` | `fileToolStripMenuItem.Text` | File | 文件 |
| `RNGReporter/Researcher.Designer.cs` | `newToolStripMenuItem.Text` | &New | 新建 |
| `RNGReporter/Researcher.Designer.cs` | `openToolStripMenuItem.Text` | &Open | 打开 |
| `RNGReporter/Researcher.Designer.cs` | `saveToolStripMenuItem.Text` | &Save | 保存 |
| `RNGReporter/Researcher.Designer.cs` | `checkBoxCustom8Hex.Text` | Hex | 16进制 |
| `RNGReporter/Researcher.Designer.cs` | `label11.Text` | Custom 8 | 自定义 8 |
| `RNGReporter/Researcher.Designer.cs` | `checkBoxCustom9Hex.Text` | Hex | 16进制 |
| `RNGReporter/Researcher.Designer.cs` | `label13.Text` | Custom 9 | 自定义 9 |
| `RNGReporter/Researcher.Designer.cs` | `checkBoxCustom10Hex.Text` | Hex | 16进制 |
| `RNGReporter/Researcher.Designer.cs` | `label14.Text` | Custom 10 | 自定义 10 |
| `RNGReporter/Researcher.Designer.cs` | `label15.Text` | Search Seed (Hex) | 计算Seed (Hex) |
| `RNGReporter/Researcher.Designer.cs` | `buttonNext.Text` | Next | 下一个 |
| `RNGReporter/Researcher.Designer.cs` | `buttonSearch.Text` | Search | 计算 |
| `RNGReporter/Researcher.Designer.cs` | `ColumnFrame.HeaderText` | Frame | 帧数 |
| `RNGReporter/Researcher.Designer.cs` | `Column32BitHigh.HeaderText` | 32BitHigh | 32位高位 |
| `RNGReporter/Researcher.Designer.cs` | `Column32BitLow.HeaderText` | 32BitLow | 32位低位 |
| `RNGReporter/Researcher.Designer.cs` | `Column16BitHigh.HeaderText` | 16BitHigh | 16位高位 |
| `RNGReporter/Researcher.Designer.cs` | `Column16BitLow.HeaderText` | 16BitLow | 16位低位 |
| `RNGReporter/Researcher.Designer.cs` | `Custom1.HeaderText` | Custom1 | 自定义1 |
| `RNGReporter/Researcher.Designer.cs` | `Custom2.HeaderText` | Custom2 | 自定义2 |
| `RNGReporter/Researcher.Designer.cs` | `Custom3.HeaderText` | Custom3 | 自定义3 |
| `RNGReporter/Researcher.Designer.cs` | `Custom4.HeaderText` | Custom4 | 自定义4 |
| `RNGReporter/Researcher.Designer.cs` | `Custom5.HeaderText` | Custom5 | 自定义5 |
| `RNGReporter/Researcher.Designer.cs` | `Custom6.HeaderText` | Custom6 | 自定义6 |
| `RNGReporter/Researcher.Designer.cs` | `Custom7.HeaderText` | Custom7 | 自定义7 |
| `RNGReporter/Researcher.Designer.cs` | `Custom8.HeaderText` | Custom8 | 自定义8 |
| `RNGReporter/Researcher.Designer.cs` | `Custom9.HeaderText` | Custom9 | 自定义9 |
| `RNGReporter/Researcher.Designer.cs` | `Custom10.HeaderText` | Custom10 | 自定义10 |
| `RNGReporter/Researcher.Designer.cs` | `buttonGenerate.Text` | Generate | 计算 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Common RNGs | 常见的 RNGs |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Copy Item | 复制Item |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Copy Selected Columns | 复制选中的列 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Copy Row from Selected Columns | 从选定列复制行 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Output Selected Columns to TXT... | 将选定列输出到TXT文本文件... |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom | 自定义 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom 1 | 自定义 1 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom 2 | 自定义 2 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom 3 | 自定义 3 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom 4 | 自定义 4 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Max Results | 最大帧 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Hex | 16进制 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom 5 | 自定义 5 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom 6 | 自定义 6 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom 7 | 自定义 7 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | File | 文件 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | &New | 新建 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | &Open | 打开 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | &Save | 保存 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Open Researcher Profile | 打开 Researcher 配置 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Save Researcher Profile | 保存研究文件 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom 8 | 自定义 8 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom 9 | 自定义 9 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom 10 | 自定义 10 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Search Seed (Hex) | 计算Seed (Hex) |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Next | 下一个 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | 16BitHigh | 16位高位 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | 16BitLow | 16位低位 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Frame | 帧 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Search | 计算 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | None | 无 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Frame | 帧数 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | 32BitHigh | 32位高位 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | 32BitLow | 32位低位 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom1 | 自定义1 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom2 | 自定义2 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom3 | 自定义3 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom4 | 自定义4 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom5 | 自定义5 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom6 | 自定义6 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom7 | 自定义7 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom8 | 自定义8 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom9 | 自定义9 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Custom10 | 自定义10 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Generate | 计算 |
| `RNGReporter/Researcher.Designer.cs` | `literal` | Researcher | 算法研究计算器 |
| `RNGReporter/Researcher.cs` | `literal` | You must check off the Hex box in order to calculate using hex values. | 您必须勾选16进制框才能使用16进制值进行计算 |
| `RNGReporter/Researcher.cs` | `literal` | None | 无 |
| `RNGReporter/Researcher.cs` | `literal` | Custom 1 | 自定义 1 |
| `RNGReporter/Researcher.cs` | `literal` | Custom 2 | 自定义 2 |
| `RNGReporter/Researcher.cs` | `literal` | Custom 3 | 自定义 3 |
| `RNGReporter/Researcher.cs` | `literal` | Custom 4 | 自定义 4 |
| `RNGReporter/Researcher.cs` | `literal` | Custom 5 | 自定义 5 |
| `RNGReporter/Researcher.cs` | `literal` | Custom 6 | 自定义 6 |
| `RNGReporter/Researcher.cs` | `literal` | Custom 7 | 自定义 7 |
| `RNGReporter/Researcher.cs` | `literal` | Custom 8 | 自定义 8 |
| `RNGReporter/Researcher.cs` | `literal` | Custom 9 | 自定义 9 |
| `RNGReporter/Researcher.cs` | `literal` | Custom 10 | 自定义 10 |
| `RNGReporter/Researcher.cs` | `literal` | Copy  | 复制 |
| `RNGReporter/Researcher.cs` | `literal` | Save Output to TXT | 保存输出到 TXT |
| `RNGReporter/Researcher.cs` | `literal` | TXT Files\|*.txt | TXT 文件\|*.txt |
| `RNGReporter/Researcher.cs` | `literal` | Corrupt profile detected | 检测到损坏的配置文件 |
| `RNGReporter/Researcher.cs` | `literal` | Frame | 帧 |
| `RNGReporter/Researcher.cs` | `literal` | The Frame research accepts only decimal numbers. | 请输入10进制的帧数 |
| `RNGReporter/Researcher.cs` | `literal` | Error | 错误 |
| `RNGReporter/Researcher.cs` | `literal` | 32BitHigh | 32位高位 |
| `RNGReporter/Researcher.cs` | `literal` | 32BitLow | 32位低位 |
| `RNGReporter/RoamerMap.Designer.cs` | `label1.Text` | Raikou | 雷公 |
| `RNGReporter/RoamerMap.Designer.cs` | `label2.Text` | Entei | 炎帝 |
| `RNGReporter/RoamerMap.Designer.cs` | `label3.Text` | Latias / Latios | 拉帝亚斯/拉帝欧斯 |
| `RNGReporter/RoamerMap.Designer.cs` | `literal` | Raikou | 雷公 |
| `RNGReporter/RoamerMap.Designer.cs` | `literal` | Entei | 炎帝 |
| `RNGReporter/RoamerMap.Designer.cs` | `literal` | Latias / Latios | 拉帝亚斯/拉帝欧斯 |
| `RNGReporter/RoamerMap.Designer.cs` | `literal` | Roamer Map | 游走神兽Map（HGSS） |
| `RNGReporter/SearchElm.Designer.cs` | `buttonE.Text` | E | 炎帝 |
| `RNGReporter/SearchElm.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/SearchElm.Designer.cs` | `buttonOk.Text` | OK | 确认结果 |
| `RNGReporter/SearchElm.Designer.cs` | `label1.Text` | L | 拉帝欧斯\\拉迪亚斯 |
| `RNGReporter/SearchElm.Designer.cs` | `label2.Text` | E | 炎帝 |
| `RNGReporter/SearchElm.Designer.cs` | `label3.Text` | R | 雷公 |
| `RNGReporter/SearchElm.Designer.cs` | `groupBox1.Text` | Call Responses | 电话回复序列 |
| `RNGReporter/SearchElm.Designer.cs` | `labelEIrwin.Text` | E - Hearing about your escapades rocks my soul! It sure does! | E - 听说你的冒险事迹真让我热血沸腾！确实如此！ |
| `RNGReporter/SearchElm.Designer.cs` | `radioButtonIrwin.Text` | Irwin | 麦克 |
| `RNGReporter/SearchElm.Designer.cs` | `radioButtonElm.Text` | Elm | 空木博士 |
| `RNGReporter/SearchElm.Designer.cs` | `labelResults.Text` | Number of possible results: | 可能的结果数量： |
| `RNGReporter/SearchElm.Designer.cs` | `groupBox2.Text` | Roamer Locations (Optional) | 游走位置 (可选) |
| `RNGReporter/SearchElm.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/SearchElm.Designer.cs` | `literal` | E | 炎帝 |
| `RNGReporter/SearchElm.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/SearchElm.Designer.cs` | `literal` | OK | 确认结果 |
| `RNGReporter/SearchElm.Designer.cs` | `literal` | L | 拉帝欧斯\\拉迪亚斯 |
| `RNGReporter/SearchElm.Designer.cs` | `literal` | R | 雷公 |
| `RNGReporter/SearchElm.Designer.cs` | `literal` | Call Responses | 电话回复序列 |
| `RNGReporter/SearchElm.Designer.cs` | `literal` | E - Hearing about your escapades rocks my soul! It sure does! | E - 听说你的冒险事迹真让我热血沸腾！确实如此！ |
| `RNGReporter/SearchElm.Designer.cs` | `literal` | Irwin | 麦克 |
| `RNGReporter/SearchElm.Designer.cs` | `literal` | Elm | 空木博士 |
| `RNGReporter/SearchElm.Designer.cs` | `literal` | Number of possible results: | 可能的结果数量： |
| `RNGReporter/SearchElm.Designer.cs` | `literal` | Roamer Locations (Optional) | 游走位置 (可选) |
| `RNGReporter/SearchElm.Designer.cs` | `literal` | Search Call Responses | 打电话反查（HGSS） |
| `RNGReporter/SearchElm.cs` | `literal` | E | 炎帝 |
| `RNGReporter/SearchElm.cs` | `literal` | Possible Results:  | 可能的结果数量： |
| `RNGReporter/SearchElmV.Designer.cs` | `buttonPos1E.Text` | E | 炎帝 |
| `RNGReporter/SearchElmV.Designer.cs` | `buttonPos2E.Text` | E | 炎帝 |
| `RNGReporter/SearchElmV.Designer.cs` | `buttonPos3E.Text` | E | 炎帝 |
| `RNGReporter/SearchElmV.Designer.cs` | `buttonPos4E.Text` | E | 炎帝 |
| `RNGReporter/SearchElmV.Designer.cs` | `buttonPos5E.Text` | E | 炎帝 |
| `RNGReporter/SearchElmV.Designer.cs` | `buttonPos6E.Text` | E | 炎帝 |
| `RNGReporter/SearchElmV.Designer.cs` | `buttonPos7E.Text` | E | 炎帝 |
| `RNGReporter/SearchElmV.Designer.cs` | `buttonPos8E.Text` | E | 炎帝 |
| `RNGReporter/SearchElmV.Designer.cs` | `buttonPos9E.Text` | E | 炎帝 |
| `RNGReporter/SearchElmV.Designer.cs` | `buttonPos10E.Text` | E | 炎帝 |
| `RNGReporter/SearchElmV.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/SearchElmV.Designer.cs` | `buttonOk.Text` | OK | 确认 |
| `RNGReporter/SearchElmV.Designer.cs` | `literal` | E | 炎帝 |
| `RNGReporter/SearchElmV.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/SearchElmV.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/SearchElmV.Designer.cs` | `literal` | OK | 确认 |
| `RNGReporter/SearchElmV.Designer.cs` | `literal` | Search Elm Responses | 多次打电话反查（HGSS） |
| `RNGReporter/SearchFlips.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/SearchFlips.Designer.cs` | `buttonOk.Text` | OK | 确认结果 |
| `RNGReporter/SearchFlips.Designer.cs` | `label1.Text` | Click the buttons to match your coin flip pattern. | 游戏中进行掷硬币，然后每次都点击对应的花色记录下序列，直到下面的结果为1 |
| `RNGReporter/SearchFlips.Designer.cs` | `labelResults.Text` | Number of possible results: | 可能的结果数量： |
| `RNGReporter/SearchFlips.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/SearchFlips.Designer.cs` | `literal` | OK | 确认结果 |
| `RNGReporter/SearchFlips.Designer.cs` | `literal` | Click the buttons to match your coin flip pattern. | 游戏中进行掷硬币，然后每次都点击对应的花色记录下序列，直到下面的结果为1 |
| `RNGReporter/SearchFlips.Designer.cs` | `literal` | Number of possible results: | 可能的结果数量： |
| `RNGReporter/SearchFlips.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/SearchFlips.Designer.cs` | `literal` | Search Coin Flips | 掷硬币反查（DPPt） |
| `RNGReporter/SearchIVs.Designer.cs` | `label1.Text` | HP | 觉醒力量 |
| `RNGReporter/SearchIVs.Designer.cs` | `label2.Text` | Attack | 攻击 |
| `RNGReporter/SearchIVs.Designer.cs` | `label3.Text` | Defense | 防御 |
| `RNGReporter/SearchIVs.Designer.cs` | `label4.Text` | SpAttk | 特攻 |
| `RNGReporter/SearchIVs.Designer.cs` | `label5.Text` | SpDef | 特防 |
| `RNGReporter/SearchIVs.Designer.cs` | `label6.Text` | Speed | 速度 |
| `RNGReporter/SearchIVs.Designer.cs` | `buttonOK.Text` | OK | 确认 |
| `RNGReporter/SearchIVs.Designer.cs` | `label7.Text` | Enter the IVs of the Pokémon caught immediately\r\nafter turning on the C-Gear. | 输入在开启Ｃ装置之后立即捕捉到的宝可梦的个体值 |
| `RNGReporter/SearchIVs.Designer.cs` | `buttonCancel.Text` | Cancel | 取消 |
| `RNGReporter/SearchIVs.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/SearchIVs.Designer.cs` | `literal` | Attack | 攻击 |
| `RNGReporter/SearchIVs.Designer.cs` | `literal` | Defense | 防御 |
| `RNGReporter/SearchIVs.Designer.cs` | `literal` | SpAttk | 特攻 |
| `RNGReporter/SearchIVs.Designer.cs` | `literal` | SpDef | 特防 |
| `RNGReporter/SearchIVs.Designer.cs` | `literal` | Speed | 速度 |
| `RNGReporter/SearchIVs.Designer.cs` | `literal` | OK | 确认 |
| `RNGReporter/SearchIVs.Designer.cs` | `literal` | Enter the IVs of the Pokémon caught immediately\r\nafter turning on the C-Gear. | 输入在开启Ｃ装置之后立即捕捉到的宝可梦的个体值 |
| `RNGReporter/SearchIVs.Designer.cs` | `literal` | Cancel | 取消 |
| `RNGReporter/SearchIVs.Designer.cs` | `literal` | Search IVs | 计算个体值 |
| `RNGReporter/SearchNature.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/SearchNature.Designer.cs` | `buttonOk.Text` | OK | 确认 |
| `RNGReporter/SearchNature.Designer.cs` | `label1.Text` | Nature 1 | 性格1 |
| `RNGReporter/SearchNature.Designer.cs` | `label2.Text` | Nature 2 | 性格2 |
| `RNGReporter/SearchNature.Designer.cs` | `label3.Text` | Nature 3 | 性格3 |
| `RNGReporter/SearchNature.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/SearchNature.Designer.cs` | `literal` | OK | 确认 |
| `RNGReporter/SearchNature.Designer.cs` | `literal` | Nature 1 | 性格1 |
| `RNGReporter/SearchNature.Designer.cs` | `literal` | Nature 2 | 性格2 |
| `RNGReporter/SearchNature.Designer.cs` | `literal` | Nature 3 | 性格3 |
| `RNGReporter/SearchNature.Designer.cs` | `literal` | Search Natures | 计算性格 |
| `RNGReporter/SearchRoamers.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/SearchRoamers.Designer.cs` | `buttonOk.Text` | OK | 确认 |
| `RNGReporter/SearchRoamers.Designer.cs` | `label3.Text` | R | 雷公 |
| `RNGReporter/SearchRoamers.Designer.cs` | `label2.Text` | E | 炎帝 |
| `RNGReporter/SearchRoamers.Designer.cs` | `label1.Text` | L | 拉帝欧斯\\拉迪亚斯 |
| `RNGReporter/SearchRoamers.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/SearchRoamers.Designer.cs` | `literal` | OK | 确认 |
| `RNGReporter/SearchRoamers.Designer.cs` | `literal` | R | 雷公 |
| `RNGReporter/SearchRoamers.Designer.cs` | `literal` | E | 炎帝 |
| `RNGReporter/SearchRoamers.Designer.cs` | `literal` | L | 拉帝欧斯\\拉迪亚斯 |
| `RNGReporter/SearchRoamers.Designer.cs` | `literal` | Search Roamers | 通过游走神兽来反查搜索（HGSS） |
| `RNGReporter/SeedFinder.Designer.cs` | `buttonOk.Text` | OK | 确认 |
| `RNGReporter/SeedFinder.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/SeedFinder.Designer.cs` | `label1.Text` | Year | 年份 |
| `RNGReporter/SeedFinder.Designer.cs` | `label2.Text` | Month | 月份  |
| `RNGReporter/SeedFinder.Designer.cs` | `label3.Text` | Date | 日期 |
| `RNGReporter/SeedFinder.Designer.cs` | `label4.Text` | Hour | 时 |
| `RNGReporter/SeedFinder.Designer.cs` | `label6.Text` | Second | 秒 |
| `RNGReporter/SeedFinder.Designer.cs` | `label7.Text` | Minute | 分 |
| `RNGReporter/SeedFinder.Designer.cs` | `buttonSimpleSeed.Text` | Create | 计算 |
| `RNGReporter/SeedFinder.Designer.cs` | `tabPage1.Text` | Find Seed by IVs | 根据个体计算seed |
| `RNGReporter/SeedFinder.Designer.cs` | `radioButton_SIV_OPEN.Text` | Open | 打开 |
| `RNGReporter/SeedFinder.Designer.cs` | `radioButton_SIV_CUSTOM.Text` | Custom | 自定义 |
| `RNGReporter/SeedFinder.Designer.cs` | `checkBoxLowDelay.Text` | Delay Below 10000 | Delay低于10000 |
| `RNGReporter/SeedFinder.Designer.cs` | `label_SIV_MaxDelay.Text` | Max Delay | 最大Delay |
| `RNGReporter/SeedFinder.Designer.cs` | `label_SIV_MinDelay.Text` | Min Delay | 最小Delay |
| `RNGReporter/SeedFinder.Designer.cs` | `label_a_y.Text` | Year | 年份 |
| `RNGReporter/SeedFinder.Designer.cs` | `Type.HeaderText` | Type | 类型 |
| `RNGReporter/SeedFinder.Designer.cs` | `Frame.HeaderText` | Method 1 Frame | Method 1 帧数 |
| `RNGReporter/SeedFinder.Designer.cs` | `Secs.HeaderText` | Seconds | 秒数 |
| `RNGReporter/SeedFinder.Designer.cs` | `buttonFind_A.Text` | Find | 计算 |
| `RNGReporter/SeedFinder.Designer.cs` | `label10.Text` | Nature | 性格 |
| `RNGReporter/SeedFinder.Designer.cs` | `label15.Text` | Spe | 速度 |
| `RNGReporter/SeedFinder.Designer.cs` | `label_a_min.Text` | Minute (0-59) | 分（0-59） |
| `RNGReporter/SeedFinder.Designer.cs` | `label16.Text` | SpD | 特防 |
| `RNGReporter/SeedFinder.Designer.cs` | `label17.Text` | SpA | 特攻 |
| `RNGReporter/SeedFinder.Designer.cs` | `label_a_h.Text` | Hour (0-23) | 时（0-23） |
| `RNGReporter/SeedFinder.Designer.cs` | `label18.Text` | Def | 防御 |
| `RNGReporter/SeedFinder.Designer.cs` | `label_a_m.Text` | Month | 月份 |
| `RNGReporter/SeedFinder.Designer.cs` | `label19.Text` | Atk | 攻击 |
| `RNGReporter/SeedFinder.Designer.cs` | `label_a_d.Text` | Date | 日期 |
| `RNGReporter/SeedFinder.Designer.cs` | `label20.Text` | HP | 觉醒力量 |
| `RNGReporter/SeedFinder.Designer.cs` | `tabPage3.Text` | Find Seed by Stats | 根据能力值计算seed |
| `RNGReporter/SeedFinder.Designer.cs` | `radioButton_SS_CUSTOM.Text` | Custom | 自定义 |
| `RNGReporter/SeedFinder.Designer.cs` | `label_SS_MaxDelay.Text` | Max Delay | 最大Delay |
| `RNGReporter/SeedFinder.Designer.cs` | `label_SS_MinDelay.Text` | Min Delay | 最小Delay |
| `RNGReporter/SeedFinder.Designer.cs` | `buttonFind_Stat.Text` | Find | 计算 |
| `RNGReporter/SeedFinder.Designer.cs` | `label32.Text` | Year | 年份 |
| `RNGReporter/SeedFinder.Designer.cs` | `label33.Text` | Minute (0-59) | 分（0-59） |
| `RNGReporter/SeedFinder.Designer.cs` | `label34.Text` | Hour (0-23) | 时（0-23） |
| `RNGReporter/SeedFinder.Designer.cs` | `label35.Text` | Month | 月份 |
| `RNGReporter/SeedFinder.Designer.cs` | `label36.Text` | Date | 日期 |
| `RNGReporter/SeedFinder.Designer.cs` | `dataGridViewTextBoxColumn1.HeaderText` | Type | 类型 |
| `RNGReporter/SeedFinder.Designer.cs` | `OffsetStat.HeaderText` | Offset | 偏差 |
| `RNGReporter/SeedFinder.Designer.cs` | `dataGridViewTextBoxColumn4.HeaderText` | Seconds | 秒数 |
| `RNGReporter/SeedFinder.Designer.cs` | `label22.Text` | Spe | 速度 |
| `RNGReporter/SeedFinder.Designer.cs` | `label23.Text` | SpD | 特防 |
| `RNGReporter/SeedFinder.Designer.cs` | `label24.Text` | SpA | 特攻 |
| `RNGReporter/SeedFinder.Designer.cs` | `label25.Text` | Def | 防御 |
| `RNGReporter/SeedFinder.Designer.cs` | `label26.Text` | Atk | 攻击 |
| `RNGReporter/SeedFinder.Designer.cs` | `label27.Text` | HP | 觉醒力量 |
| `RNGReporter/SeedFinder.Designer.cs` | `label28.Text` | Characteristic | 个性 |
| `RNGReporter/SeedFinder.Designer.cs` | `label29.Text` | Nature | 性格 |
| `RNGReporter/SeedFinder.Designer.cs` | `label30.Text` | Level | 等级 |
| `RNGReporter/SeedFinder.Designer.cs` | `label31.Text` | Pokemon | 宝可梦 |
| `RNGReporter/SeedFinder.Designer.cs` | `tabPage4.Text` | Find Seed by IV Range | 根据个体范围计算seed |
| `RNGReporter/SeedFinder.Designer.cs` | `buttonFind_ByIVRange.Text` | Find | 计算 |
| `RNGReporter/SeedFinder.Designer.cs` | `label96.Text` | Max | 最大 |
| `RNGReporter/SeedFinder.Designer.cs` | `label97.Text` | Min | 最小 |
| `RNGReporter/SeedFinder.Designer.cs` | `dataGridViewTextBoxColumn14.HeaderText` | Type | 类型 |
| `RNGReporter/SeedFinder.Designer.cs` | `dataGridViewTextBoxColumn16.HeaderText` | Method 1 Frame | Method 1 帧数 |
| `RNGReporter/SeedFinder.Designer.cs` | `dataGridViewTextBoxColumn17.HeaderText` | Seconds | 秒数 |
| `RNGReporter/SeedFinder.Designer.cs` | `label37.Text` | Year | 年份 |
| `RNGReporter/SeedFinder.Designer.cs` | `label38.Text` | Nature | 性格 |
| `RNGReporter/SeedFinder.Designer.cs` | `label39.Text` | Spe | 速度 |
| `RNGReporter/SeedFinder.Designer.cs` | `label40.Text` | Minute (0-59) | 分（0-59） |
| `RNGReporter/SeedFinder.Designer.cs` | `label41.Text` | SpD | 特防 |
| `RNGReporter/SeedFinder.Designer.cs` | `label42.Text` | SpA | 特攻 |
| `RNGReporter/SeedFinder.Designer.cs` | `label43.Text` | Hour (0-23) | 时（0-23） |
| `RNGReporter/SeedFinder.Designer.cs` | `label44.Text` | Def | 防御 |
| `RNGReporter/SeedFinder.Designer.cs` | `label45.Text` | Month | 月份  |
| `RNGReporter/SeedFinder.Designer.cs` | `label46.Text` | Atk | 攻击 |
| `RNGReporter/SeedFinder.Designer.cs` | `label47.Text` | Date | 日期 |
| `RNGReporter/SeedFinder.Designer.cs` | `label48.Text` | HP | 觉醒力量 |
| `RNGReporter/SeedFinder.Designer.cs` | `tabPage2.Text` | Simple Seed Generator | 简易版seed计算器 |
| `RNGReporter/SeedFinder.Designer.cs` | `label14.Text` | Language | 游戏语言 |
| `RNGReporter/SeedFinder.Designer.cs` | `label104.Text` | Held Button 7 | 按住的按键 7 |
| `RNGReporter/SeedFinder.Designer.cs` | `label105.Text` | Held Button 6 | 按住的按键 6 |
| `RNGReporter/SeedFinder.Designer.cs` | `label107.Text` | Held Button 5 | 按住的按键 5 |
| `RNGReporter/SeedFinder.Designer.cs` | `label101.Text` | DS Type | DS机型 |
| `RNGReporter/SeedFinder.Designer.cs` | `checkBoxSoftReset.Text` | Soft Reset | 软复位 |
| `RNGReporter/SeedFinder.Designer.cs` | `label11.Text` | Held Button 4 | 按住的按键 4 |
| `RNGReporter/SeedFinder.Designer.cs` | `label13.Text` | Held Button 3 | 按住的按键 3 |
| `RNGReporter/SeedFinder.Designer.cs` | `label84.Text` | Held Button 2 | 按住的按键 2 |
| `RNGReporter/SeedFinder.Designer.cs` | `label100.Text` | Held Button 1 | 按住的按键 1 |
| `RNGReporter/SeedFinder.Designer.cs` | `radioButton5thGenNonCGear.Text` | 5th Gen (non C-Gear) | GEN5（非Ｃ装置） |
| `RNGReporter/SeedFinder.Designer.cs` | `radioButton5thGenCGear.Text` | 5th Gen (C-Gear) | GEN5（Ｃ装置） |
| `RNGReporter/SeedFinder.Designer.cs` | `label9.Text` | Version | 游戏版本 |
| `RNGReporter/SeedFinder.Designer.cs` | `label8.Text` | DS MAC Address | DS MAC地址 |
| `RNGReporter/SeedFinder.Designer.cs` | `label21.Text` | If you are looking for your initial seed you may ignore this tab completely.  | 如果你正在寻找你的初始seed，你可以完全忽略这个标签。 |
| `RNGReporter/SeedFinder.Designer.cs` | `checkBoxShowMonster.Text` | Show Monster | 显示宝可梦 |
| `RNGReporter/SeedFinder.Designer.cs` | `checkBox1.Text` | Open Search | 打开搜索 |
| `RNGReporter/SeedFinder.Designer.cs` | `label49.Text` | Year | 年份 |
| `RNGReporter/SeedFinder.Designer.cs` | `dataGridViewTextBoxColumn2.HeaderText` | Type | 类型 |
| `RNGReporter/SeedFinder.Designer.cs` | `dataGridViewTextBoxColumn7.HeaderText` | Seconds | 秒数 |
| `RNGReporter/SeedFinder.Designer.cs` | `label50.Text` | Nature | 性格 |
| `RNGReporter/SeedFinder.Designer.cs` | `label51.Text` | Spe | 速度 |
| `RNGReporter/SeedFinder.Designer.cs` | `label52.Text` | Minute (0-59) | 分（0-59） |
| `RNGReporter/SeedFinder.Designer.cs` | `label53.Text` | SpD | 特防 |
| `RNGReporter/SeedFinder.Designer.cs` | `label54.Text` | SpA | 特攻 |
| `RNGReporter/SeedFinder.Designer.cs` | `label55.Text` | Hour (0-23) | 时（0-23） |
| `RNGReporter/SeedFinder.Designer.cs` | `label56.Text` | Def | 防御 |
| `RNGReporter/SeedFinder.Designer.cs` | `label57.Text` | Month | 月份  |
| `RNGReporter/SeedFinder.Designer.cs` | `label58.Text` | Atk | 攻击 |
| `RNGReporter/SeedFinder.Designer.cs` | `label59.Text` | Date | 日期 |
| `RNGReporter/SeedFinder.Designer.cs` | `label60.Text` | HP | 觉醒力量 |
| `RNGReporter/SeedFinder.Designer.cs` | `button2.Text` | Find | 计算 |
| `RNGReporter/SeedFinder.Designer.cs` | `label61.Text` | Year | 年份 |
| `RNGReporter/SeedFinder.Designer.cs` | `label62.Text` | Minute (0-59) | 分（0-59） |
| `RNGReporter/SeedFinder.Designer.cs` | `label63.Text` | Hour (0-23) | 时（0-23） |
| `RNGReporter/SeedFinder.Designer.cs` | `label64.Text` | Month | 月份  |
| `RNGReporter/SeedFinder.Designer.cs` | `label65.Text` | Date | 日期 |
| `RNGReporter/SeedFinder.Designer.cs` | `dataGridViewTextBoxColumn9.HeaderText` | Type | 类型 |
| `RNGReporter/SeedFinder.Designer.cs` | `dataGridViewTextBoxColumn11.HeaderText` | Offset | 偏移 |
| `RNGReporter/SeedFinder.Designer.cs` | `dataGridViewTextBoxColumn12.HeaderText` | Seconds | 秒数 |
| `RNGReporter/SeedFinder.Designer.cs` | `label66.Text` | Spe | 速度 |
| `RNGReporter/SeedFinder.Designer.cs` | `label67.Text` | SpD | 特防 |
| `RNGReporter/SeedFinder.Designer.cs` | `label68.Text` | SpA | 特攻 |
| `RNGReporter/SeedFinder.Designer.cs` | `label69.Text` | Def | 防御 |
| `RNGReporter/SeedFinder.Designer.cs` | `label70.Text` | Atk | 攻击 |
| `RNGReporter/SeedFinder.Designer.cs` | `label71.Text` | HP | 觉醒力量 |
| `RNGReporter/SeedFinder.Designer.cs` | `label72.Text` | Characteristic | 个性 |
| `RNGReporter/SeedFinder.Designer.cs` | `label73.Text` | Nature | 性格 |
| `RNGReporter/SeedFinder.Designer.cs` | `label74.Text` | Level | 等级 |
| `RNGReporter/SeedFinder.Designer.cs` | `label75.Text` | Pokemon | 宝可梦 |
| `RNGReporter/SeedFinder.Designer.cs` | `label76.Text` | If you are looking for your initial seed you may ignore this tab completely.  | 如果你正在寻找你的初始seed，你可以完全忽略这个标签。 |
| `RNGReporter/SeedFinder.Designer.cs` | `label77.Text` | Year | 年份 |
| `RNGReporter/SeedFinder.Designer.cs` | `label78.Text` | Month | 月份  |
| `RNGReporter/SeedFinder.Designer.cs` | `label79.Text` | Minute | 分 |
| `RNGReporter/SeedFinder.Designer.cs` | `label80.Text` | Date | 日期 |
| `RNGReporter/SeedFinder.Designer.cs` | `label81.Text` | Second | 秒数 |
| `RNGReporter/SeedFinder.Designer.cs` | `label82.Text` | Hour | 时 |
| `RNGReporter/SeedFinder.Designer.cs` | `label85.Text` | Nature | 性格 |
| `RNGReporter/SeedFinder.Designer.cs` | `label86.Text` | Spe | 速度 |
| `RNGReporter/SeedFinder.Designer.cs` | `label87.Text` | Minute (0-59) | 分（0-59） |
| `RNGReporter/SeedFinder.Designer.cs` | `label88.Text` | SpD | 特防 |
| `RNGReporter/SeedFinder.Designer.cs` | `label89.Text` | SpA | 特攻 |
| `RNGReporter/SeedFinder.Designer.cs` | `label90.Text` | Hour (0-23) | 时（0-23） |
| `RNGReporter/SeedFinder.Designer.cs` | `label91.Text` | Def | 防御 |
| `RNGReporter/SeedFinder.Designer.cs` | `label92.Text` | Month | 月份  |
| `RNGReporter/SeedFinder.Designer.cs` | `label93.Text` | Atk | 攻击 |
| `RNGReporter/SeedFinder.Designer.cs` | `label94.Text` | Date | 日期 |
| `RNGReporter/SeedFinder.Designer.cs` | `label95.Text` | HP | 觉醒力量 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | OK | 确认 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Year | 年份 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Month | 月份  |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Date | 日期 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Hour | 时 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Second | 秒 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Minute | 分 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Create | 计算 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Find Seed by IVs | 根据个体计算seed |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Open | 打开 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Custom | 自定义 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Delay Below 10000 | Delay低于10000 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Max Delay | 最大Delay |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Min Delay | 最小Delay |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Type | 类型 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Offset | 偏移 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Method 1 Frame | Method 1 帧数 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Frame | 帧 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Seconds | 秒数 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Find | 计算 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Nature | 性格 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Minute (0-59) | 分（0-59） |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Hour (0-23) | 时（0-23） |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Month | 月份 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Find Seed by Stats | 根据能力值计算seed |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Offset | 偏差 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Characteristic | 个性 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Level | 等级 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Pokemon | 宝可梦 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Find Seed by IV Range | 根据个体范围计算seed |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Max | 最大 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Min | 最小 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Simple Seed Generator | 简易版seed计算器 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Language | 游戏语言 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Held Button 7 | 按住的按键 7 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | None | 无 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | R | 雷公 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | L | 拉帝欧斯\\拉迪亚斯 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Held Button 6 | 按住的按键 6 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Held Button 5 | 按住的按键 5 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | DS Type | DS机型 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Soft Reset | 软复位 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Held Button 4 | 按住的按键 4 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Held Button 3 | 按住的按键 3 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Held Button 2 | 按住的按键 2 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Held Button 1 | 按住的按键 1 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | 5th Gen (non C-Gear) | GEN5（非Ｃ装置） |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | 5th Gen (C-Gear) | GEN5（Ｃ装置） |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Black | 黑 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | White | 白 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Black 2 | 黑2 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | White 2 | 白2 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Version | 游戏版本 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | DS MAC Address | DS MAC地址 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | If you are looking for your initial seed you may ignore this tab completely.  | 如果你正在寻找你的初始seed，你可以完全忽略这个标签。 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Show Monster | 显示宝可梦 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Open Search | 打开搜索 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | Second | 秒数 |
| `RNGReporter/SeedFinder.Designer.cs` | `literal` | 4th Gen Seed Finder / Generator | GEN4 Seed查找/计算 |
| `RNGReporter/SeedFinder.cs` | `literal` | seconds | 秒 |
| `RNGReporter/SeedFinder.cs` | `literal` | No matches found for the IVs entered.  Please check and try again. | 未找到与输入 IV 匹配的结果，请检查后重试。 |
| `RNGReporter/SeedFinder.cs` | `literal` | No Data Found | 未找到数据 |
| `RNGReporter/SeedFinder.cs` | `literal` | No reasonable initial seed found. Please check your DATE and TIME. | 未找到合理的初始 seed。请检查日期和时间。 |
| `RNGReporter/SeedFinder.cs` | `literal` | There was a problem with the stats/nature/Pokemon you have entered.  Please check them and try again.  | 你输入的能力值、性格或宝可梦有问题。请检查后重试。 |
| `RNGReporter/SeedFinder.cs` | `literal` | Invalid Stats | 能力值无效 |
| `RNGReporter/SeedFinder.cs` | `literal` | There were too many combinations of IV possibilities to accurately find your intitial seed ( | 存在太多的个体值可能性组合，因此无法准确地找到您的初始seed。 ( |
| `RNGReporter/SeedFinder.cs` | `literal` | ) please try with a higher level Pokemon, | ) 请尝试使用更高等级的宝可梦, |
| `RNGReporter/SeedFinder.cs` | `literal` | To many IV Combinations | IV 组合过多 |
| `RNGReporter/SeedFinder.cs` | `literal` | Too many IV Combinations | 太多个体值组合啦 |
| `RNGReporter/SeedToTime.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/SeedToTime.Designer.cs` | `buttonOk.Text` | OK | 确认 |
| `RNGReporter/SeedToTime.Designer.cs` | `label20.Text` | Year | 年份 |
| `RNGReporter/SeedToTime.Designer.cs` | `buttonGenerate.Text` | Generate | 计算 |
| `RNGReporter/SeedToTime.Designer.cs` | `Date.HeaderText` | Date | 日期 |
| `RNGReporter/SeedToTime.Designer.cs` | `Time.HeaderText` | Time | 时间 |
| `RNGReporter/SeedToTime.Designer.cs` | `label1.Text` | Seconds | 秒数 |
| `RNGReporter/SeedToTime.Designer.cs` | `copySeedToClipboardToolStripMenuItem.Text` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/SeedToTime.Designer.cs` | `generateTXTFileToolStripMenuItem.Text` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/SeedToTime.Designer.cs` | `buttonGenerateAdjacents.Text` | Generate | 计算 |
| `RNGReporter/SeedToTime.Designer.cs` | `label2.Text` | Seconds | 秒数 |
| `RNGReporter/SeedToTime.Designer.cs` | `label5.Text` | Delays | Delay |
| `RNGReporter/SeedToTime.Designer.cs` | `buttonSearch.Text` | Search Results | 掷硬币反查 |
| `RNGReporter/SeedToTime.Designer.cs` | `labelVerificationType.Text` | Coin Flips for Seed: | 掷硬币序列： |
| `RNGReporter/SeedToTime.Designer.cs` | `checkBoxEPresent.Text` | E | 炎帝 |
| `RNGReporter/SeedToTime.Designer.cs` | `checkBoxRPresent.Text` | R | 雷公 |
| `RNGReporter/SeedToTime.Designer.cs` | `checkBoxLPresent.Text` | L | 拉帝欧斯/拉帝亚斯 |
| `RNGReporter/SeedToTime.Designer.cs` | `label18.Text` | Roaming Pokemon Locations: | 游走宝可梦位置： |
| `RNGReporter/SeedToTime.Designer.cs` | `buttonRoamerMap.Text` | Map | 地图 |
| `RNGReporter/SeedToTime.Designer.cs` | `checkBoxOddEven.Text` | Odd / Even should match the seed\'s delay | 筛选与seed的delay相同奇偶的结果 |
| `RNGReporter/SeedToTime.Designer.cs` | `radioBtnBW.Text` | BW (C-Gear Seed) | BW（Ｃ装置 Seed） |
| `RNGReporter/SeedToTime.Designer.cs` | `labelMAC.Text` | Profile | 存档信息 |
| `RNGReporter/SeedToTime.Designer.cs` | `radioButton1.Text` | BW (Standard Seed) | BW (普通Seed) |
| `RNGReporter/SeedToTime.Designer.cs` | `labelMaxFrame.Text` | Max | 最大 |
| `RNGReporter/SeedToTime.Designer.cs` | `labelMinFrame.Text` | Min | 最小 |
| `RNGReporter/SeedToTime.Designer.cs` | `label10.Text` | Frame | 帧数 |
| `RNGReporter/SeedToTime.Designer.cs` | `checkBoxRoamer.Text` | Roamer | 存在游走 |
| `RNGReporter/SeedToTime.Designer.cs` | `buttonSearchRoamers.Text` | Search Roamers | 查看游走反查 |
| `RNGReporter/SeedToTime.Designer.cs` | `dataGridViewTextBoxColumn1.HeaderText` | Date | 日期 |
| `RNGReporter/SeedToTime.Designer.cs` | `dataGridViewTextBoxColumn2.HeaderText` | Time | 时间 |
| `RNGReporter/SeedToTime.Designer.cs` | `ColumnFlipSequence.HeaderText` | Flip Sequence | 掷硬币序列 |
| `RNGReporter/SeedToTime.Designer.cs` | `ColumnElmResponse.HeaderText` | Elm Responses | 打电话序列 |
| `RNGReporter/SeedToTime.Designer.cs` | `ColumnRoamers.HeaderText` | Roamers | 游走位置 |
| `RNGReporter/SeedToTime.Designer.cs` | `ColumnGen5IVs.HeaderText` | IVs (Black & White) | 个体值（黑&白） |
| `RNGReporter/SeedToTime.Designer.cs` | `ColumnCGearAdjust.HeaderText` | C-Gear Seed Displayed | Ｃ装置 Seed 显示 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | OK | 确认 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Year | 年份 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Generate | 计算 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Date | 日期 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Time | 时间 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Seconds | 秒数 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Delays | Delay |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Search Results | 掷硬币反查 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Coin Flips for Seed: | 掷硬币序列： |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | E | 炎帝 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | R | 雷公 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | L | 拉帝欧斯/拉帝亚斯 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Roaming Pokemon Locations: | 游走宝可梦位置： |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Map | 地图 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Odd / Even should match the seed\'s delay | 筛选与seed的delay相同奇偶的结果 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | BW (C-Gear Seed) | BW（Ｃ装置 Seed） |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Profile | 存档信息 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | BW (Standard Seed) | BW (普通Seed) |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Max | 最大 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Min | 最小 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Frame | 帧数 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Roamer | 存在游走 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Search Roamers | 查看游走反查 |
| `RNGReporter/SeedToTime.Designer.cs` | `literal` | Seed To Times / Adjacent Finder | Seed To Times/附近查找 |
| `RNGReporter/SeedToTime.cs` | `literal` | You must enter a year. | 你必须输入年份。 |
| `RNGReporter/SeedToTime.cs` | `literal` | Please Enter a Year | 请输入年份 |
| `RNGReporter/SeedToTime.cs` | `literal` | You must enter a seconds value. | 你必须输入秒数。 |
| `RNGReporter/SeedToTime.cs` | `literal` | Please Enter Seconds | 请输入秒数 |
| `RNGReporter/SeedToTime.cs` | `literal` | Coin Flips for Seed: | 投硬币获取Seed： |
| `RNGReporter/SeedToTime.cs` | `literal` | Elm Responses for Seed: | Elm打电话的结果获取Seed： |
| `RNGReporter/SeedToTime.cs` | `literal` | Frame(s) Advanced:  | 游走消耗的帧数:  |
| `RNGReporter/SeedToTime.cs` | `literal` | First 10 IVs in Seed: | Seed 的前 10 个 IV: |
| `RNGReporter/SeedToTime.cs` | `literal` | This seed is invalid, please verify that you have entered it correctly and try again. | 这个Seed无效，请确认您是否正确输入，并再试一次 |
| `RNGReporter/SeedToTime.cs` | `literal` | Invalid Seed | 无效Seed |
| `RNGReporter/SeedToTime.cs` | `literal` | No match was found for your flips. | 未找到匹配的翻硬币结果。 |
| `RNGReporter/SeedToTime.cs` | `literal` | No Match | 未找到匹配项 |
| `RNGReporter/SeedToTime.cs` | `literal` | No match was found for your Elm responses. | 未找到匹配的空木博士响应。 |
| `RNGReporter/SeedToTime.cs` | `literal` | No match was found for your IVs. | 未找到匹配的 IV。 |
| `RNGReporter/SeedToTime.cs` | `literal` | No match was found for your Roaming Pokemon. | 未找到匹配的游走宝可梦。 |
| `RNGReporter/SeedToTime.cs` | `literal` | Save Output to TXT | 保存输出到 TXT |
| `RNGReporter/SeedToTime.cs` | `literal` | TXT Files\|*.txt | TXT 文件\|*.txt |
| `RNGReporter/SeedToTime.cs` | `literal` | Search Calls | 打电话反查 |
| `RNGReporter/SeedToTime.cs` | `literal` | Search Flips | 掷硬币反查 |
| `RNGReporter/SeedToTime.cs` | `literal` | Search IVs | 个体值反查 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `label17.Text` | Coin Flips for Seed: | 投硬币获取Seed： |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `buttonSearchFlips.Text` | Search Flips | 搜索投掷数 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `label5.Text` | Delays | Delay |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `label2.Text` | Seconds | 秒数 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `buttonGenerateAdjacents.Text` | Generate | 计算 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `dataGridViewTextBoxColumn1.HeaderText` | Date | 日期 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `dataGridViewTextBoxColumn2.HeaderText` | Time | 时间 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `ColumnFlipSequence.HeaderText` | Flip Sequence | 硬币序列 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `buttonCancel.Text` | Cancel | 关闭 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `buttonOk.Text` | OK | 确认 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `label1.Text` | Target Time: | 目标时间： |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `label8.Text` | Target Seed: | 目标Seed： |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `label9.Text` | Happiness Taps: | 点击亲密度检测器： |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `label10.Text` | Remaining Coin Flips: | 剩余掷硬币数： |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Coin Flips for Seed: | 投硬币获取Seed： |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Search Flips | 搜索投掷数 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Delays | Delay |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Seconds | 秒数 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Generate | 计算 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Date | 日期 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Time | 时间 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Flip Sequence | 硬币序列 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Cancel | 关闭 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | OK | 确认 |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Target Time: | 目标时间： |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Target Seed: | 目标Seed： |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Happiness Taps: | 点击亲密度检测器： |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Remaining Coin Flips: | 剩余掷硬币数： |
| `RNGReporter/SeedToTimeEgg.Designer.cs` | `literal` | Seed to Time | Seed to Time（蛋） |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `outputShiny3rdResultsToTXTToolStripMenuItem.Text` | Output Results to TXT... | 输出结果至TXT文本文件 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `tabPageXD.Text` | XD Capture | XD暗之旋风 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `groupBox2.Text` | Spread Search | 扩散搜索 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `button5.Text` | Start Timer | 开始时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `btnGetCurrentTick.Text` | Get Current Tick | 获取当前Tick |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label91.Text` | Ability | 特性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `radioButton4.Text` | Snagged Pokémon (with nature lock) | 捕捉的宝可梦（锁性格） |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `radioButton6.Text` | Snagged Pokémon (first position) | 捕捉的宝可梦（初见） |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label98.Text` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label100.Text` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label102.Text` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label103.Text` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label104.Text` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label105.Text` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn3.HeaderText` | Ticks | 时刻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn5.HeaderText` | Time (s) | 时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn6.HeaderText` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn8.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn9.HeaderText` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn10.HeaderText` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn11.HeaderText` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn12.HeaderText` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn13.HeaderText` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `button11.Text` | Search Spreads | 扩散搜索 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label106.Text` | Max | 最大 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label107.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label108.Text` | Min | 最小 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `groupBox1.Text` | Calibration | 校准 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label90.Text` | This feature is not working yet. | 这个功能还不能使用 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `buttonXDTickReset.Text` | Reset | 重置 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label89.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `btnSetGCTick.Text` | Set Tick | 设置Tick |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `buttonXDSetStats.Text` | Confirm Stats | 确认数据 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label88.Text` | Gender | 性别比例 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label82.Text` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label83.Text` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label84.Text` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label85.Text` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label77.Text` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label86.Text` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label76.Text` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label87.Text` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label75.Text` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label74.Text` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label73.Text` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label72.Text` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `XDTicks.HeaderText` | Ticks | 时刻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `XDTime.HeaderText` | Time (s) | 时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `XDNature.HeaderText` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `XDHp.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `XDAtk.HeaderText` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `XDDef.HeaderText` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `XDSpa.HeaderText` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `XDSpd.HeaderText` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `XDSpe.HeaderText` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `buttonGenerateXD.Text` | Search Spreads | 扩散搜索 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label80.Text` | Max | 最大 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label78.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label79.Text` | Min | 最小 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `copySeed.Text` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `tabPageCapture.Text` | Capture | 正常捕捉 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label101.Text` | Date | 日期 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `rbEmerald.Text` | Emerald | 绿宝石 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `rbRS.Text` | Ruby\\Sapphire | 红宝石\\蓝宝石 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label12.Text` | Synch Nature | 同步性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `chkSynchOnly.Text` | Synchronize Only | 仅同步 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label11.Text` | Min / Max Minute | 最小/最大分钟 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label8.Text` | Min / Max Hour | 最小/最大时 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `cbDeadBattery.Text` | Dead Battery | 电池没电 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `labelCapMinMaxFrame.Text` | Min / Max Frame | 最小/最大帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label7.Text` | Gender | 性别比例 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `SeedTime.HeaderText` | Seed Time | Seed时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `CapNumber.HeaderText` | Frame | 帧数 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `Offset.HeaderText` | Occidentary | 偶然值Occidentary |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `FrameTime.HeaderText` | Frame Time | 过帧时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `EncounterSlot.HeaderText` | Encounter Slot | 遭遇槽位 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `Shiny.HeaderText` | !!! | 异色 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `cNature.HeaderText` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `Ability.HeaderText` | Ability | 特性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `CapHP.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `CapAtk.HeaderText` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `CapDef.HeaderText` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `CapSpA.HeaderText` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `CapSpD.HeaderText` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `CapSpe.HeaderText` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `HiddenPower.HeaderText` | Hidden | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `HiddenPowerPower.HeaderText` | Power | 觉醒力量威力 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label54.Text` | Encounter Slot | 遭遇槽位 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label52.Text` | Encounter Type | 相遇类型 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label30.Text` | Method | 算法 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label10.Text` | Ability | 特性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `chkShinyOnly.Text` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label21.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `btnAnySlot.Text` | Any | 任意 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `btnCapGenerate.Text` | Generate | 计算 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `btnClearNatures.Text` | Any | 任意 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `tabPageIVEEgg.Text` | Emerald Egg IVs | 绿宝石蛋个体值 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `radioButtonEIVNormal.Text` | Normal Spreads | 普通遗传 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `radioButtonEIVSplit.Text` | Split Spreads | 分裂遗传 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `radioButtonEIVAlternate.Text` | Alternate Spreads | 交替遗传 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label33.Text` | Max | 最大 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label34.Text` | Frame | 帧数 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label35.Text` | Min | 最小 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label36.Text` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label37.Text` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label38.Text` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label39.Text` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label40.Text` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label46.Text` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `checkEIVInheritance.Text` | Show Inheritance | 显示遗传来源 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label55.Text` | Parent B | 父母B |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label63.Text` | Parent A | 父母A |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn38.HeaderText` | Egg Pickup Frame | 蛋领取帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn39.HeaderText` | Egg Pickup Time | 蛋领取时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `EIVHP.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `EIVAtk.HeaderText` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `EIVDef.HeaderText` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `EIVSpA.HeaderText` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `EIVSpD.HeaderText` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `EIVSpe.HeaderText` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `buttonEIVSwapParents.Text` | Swap Parents | 交换父母数值 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `buttonGenerateEIVs.Text` | Generate | 计算 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `tabPageShinyEEgg.Text` | Emerald Shiny Egg | 绿宝石异色蛋 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `tabPageShinyEEgg.ToolTipText` | This value is typically 13 + number of pokemon in party | 这个值通常是13+背包中宝可梦的数量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `labelCalibration.Text` | Calibration | 校准值 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label1.Text` | Everstone | 不变之石 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label2.Text` | Redraws | 查看图鉴次数 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label3.Text` | Gender | 性别比例 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label4.Text` | Max | 最大 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label6.Text` | Min | 最小 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label13.Text` | Frame | 帧数 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label20.Text` | Compatibility | 相性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `checkEPIDShiny.Text` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label23.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label24.Text` | Ability | 特性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `EPIDFrame.HeaderText` | Egg Held Frame | 蛋生成帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn7.HeaderText` | Egg Held Time | 蛋生成时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn18.HeaderText` | Redraws | 查看图鉴次数 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `Advances.HeaderText` | Advances | 帧数 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn22.HeaderText` | !!! | 异色 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `EPIDNature.HeaderText` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn24.HeaderText` | Ability | 特性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `buttonEPIDNature.Text` | Any | 任意 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `buttonGenerateEPIDs.Text` | Generate | 计算 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `buttonEPIDAbility.Text` | Any | 任意 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `tabPageShinyRSEgg.Text` | Ruby\\Sapphire Shiny Egg | 红\\蓝宝石异色蛋 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `radioButton2.Text` | Date | 日期 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `radioButton1.Text` | Initial Seed | 初始seed |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label110.Text` | Min / Max Minute | 最小/最大分钟 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label111.Text` | Min / Max Hour | 最小/最大时 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `checkBox1.Text` | Dead Battery | 电池没电 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `buttonAnyNature.Text` | Any | 任意 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label41.Text` | Gender | 性别比例 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `buttonSwapParents.Text` | Swap Parents | 交换父母数值 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label96.Text` | Max | 最大 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label95.Text` | Pickup Frame | 蛋领取帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label94.Text` | Min | 最小 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label70.Text` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label69.Text` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label68.Text` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label67.Text` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label45.Text` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label42.Text` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label66.Text` | Frame Held | 蛋生成帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `buttonShiny3rdGenerate.Text` | Generate | 计算 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label58.Text` | Compatibility | 相性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `checkBoxShiny3rdShinyOnly.Text` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `checkBoxShiny3rdShowInheritance.Text` | Show Inheritance | 显示遗传来源 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label56.Text` | Parent B | 父母B |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label57.Text` | Parent A | 父母A |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `buttonAnyAbility.Text` | Any | 任意 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label43.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label44.Text` | Ability | 特性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `Seed_Time.HeaderText` | Seed Time | Seed时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `shiny3rdLowerPIDFrame.HeaderText` | Egg Held Frame | 蛋生成帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `shiny3rdLowerPIDTime.HeaderText` | Egg Held Time | 蛋生成时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `shiny3rdUpperPIDFrame.HeaderText` | Egg Pickup Frame | 蛋领取帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `shiny3rdUpperPIDTime.HeaderText` | Egg Pickup Time | 蛋领取时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `Shiny3rdShinyDisplay.HeaderText` | !!! | 异色 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `shiny3rdNature.HeaderText` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `shiny3rdAbility.HeaderText` | Ability | 特性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `shiny3rdHP.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `shiny3rdAtk.HeaderText` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `shiny3rdDef.HeaderText` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `shiny3rdSpA.HeaderText` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `shiny3rdSpD.HeaderText` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `shiny3rdSpe.HeaderText` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `tabPageShinyFRLGEgg.Text` | FRLG Shiny Egg | 火红叶绿异色蛋 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `lowerHalfBox.Text` | Lower Half PID | PID 低半部分 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label97.Text` | Initial Seed | 初始seed |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `anyNatureFRLG.Text` | Any | 任意 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label16.Text` | Gender | 性别比例 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `swapParentsFRLG.Text` | Swap Parents | 交换父母数值 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label29.Text` | Max | 最大 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label32.Text` | Pickup Frame | 蛋领取帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label47.Text` | Min | 最小 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label48.Text` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label49.Text` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label50.Text` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label51.Text` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label53.Text` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label59.Text` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label60.Text` | Frame Held | 蛋生成帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `generateFRLGEggShiny.Text` | Generate | 计算 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label61.Text` | Compatibility | 相性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `shinyOnlyFRLG.Text` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `inheritanceFRLG.Text` | Show Inheritance | 显示遗传来源 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label62.Text` | Parent B | 父母B |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label64.Text` | Parent A | 父母A |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `anyAbilityFRLG.Text` | Any | 任意 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label65.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label71.Text` | Ability | 特性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn42.HeaderText` | Egg Held Frame | 蛋生成帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn43.HeaderText` | Egg Held Time | 蛋生成时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn44.HeaderText` | Egg Pickup Frame | 蛋领取帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn45.HeaderText` | Egg Pickup Time | 蛋领取时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn47.HeaderText` | !!! | 异色 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn48.HeaderText` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn49.HeaderText` | Ability | 特性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn50.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn51.HeaderText` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn52.HeaderText` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn53.HeaderText` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn54.HeaderText` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn55.HeaderText` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `tabPageWild.Text` | Wild | 野生宝可梦 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `checkBoxWildSynchCharm.Text` | Include Synch/Charm | 首发同步/迷人之躯 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `speClear.Text` | Clear | 清空 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `spdClear.Text` | Clear | 清空 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `spaClear.Text` | Clear | 清空 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `defClear.Text` | Clear | 清空 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `atkClear.Text` | Clear | 清空 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `hpClear.Text` | Clear | 清空 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `cancel.Text` | Cancel | 取消 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `anySlots.Text` | Any | 任意 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label15.Text` | Type | 类型 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label5.Text` | Slots | 槽位 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `status.Text` | Awaiting Command | 等待操作... |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `anyHiddenPower.Text` | Any | 任意 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `L_ball.Text` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `Lead.HeaderText` | Lead | 首发 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `WildEncounterSlot.HeaderText` | Slot | 槽位 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn19.HeaderText` | !!! | 异色 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn20.HeaderText` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn21.HeaderText` | Ability | 特性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn23.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn25.HeaderText` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn26.HeaderText` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn27.HeaderText` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn28.HeaderText` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn29.HeaderText` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn30.HeaderText` | Hidden | 觉醒力量威力 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `dataGridViewTextBoxColumn35.HeaderText` | Power | 觉醒力量威力 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `L_search_S.Text` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `L_search_D.Text` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `L_search_C.Text` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `L_search_B.Text` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `L_search_A.Text` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `L_search_H.Text` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label14.Text` | Gender | 性别比例 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label17.Text` | Method | 算法 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label22.Text` | Ability | 特性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `checkBoxShiny.Text` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `label25.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `searchWild.Text` | Generate | 计算 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `anyNature.Text` | Any | 任意 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Output Results to TXT... | 输出结果至TXT文本文件 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | XD Capture | XD暗之旋风 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Spread Search | 扩散搜索 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Start Timer | 开始时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Get Current Tick | 获取当前Tick |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Any | 任意 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Ability | 特性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Snagged Pokémon (with nature lock) | 捕捉的宝可梦（锁性格） |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Snagged Pokémon (first position) | 捕捉的宝可梦（初见） |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Ticks | 时刻 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Time | 时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Time (s) | 时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Nature | 性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Search Spreads | 扩散搜索 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Max | 最大 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Min | 最小 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Hardy | 勤奋 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Lonely | 怕寂寞 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Brave | 勇敢 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Adamant | 固执 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Naughty | 顽皮 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Bold | 大胆 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Docile | 坦率 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Relaxed | 悠闲 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Impish | 淘气 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Lax | 乐天 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Timid | 胆小 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Hasty | 急躁 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Serious | 认真 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Jolly | 爽朗 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Naive | 天真 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Modest | 内敛 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Mild | 慢吞吞 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Quiet | 冷静 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Bashful | 害羞 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Rash | 马虎 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Calm | 温和 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Gentle | 温顺 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Sassy | 自大 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Careful | 慎重 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Quirky | 浮躁 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Calibration | 校准 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | This feature is not working yet. | 这个功能还不能使用 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Reset | 重置 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Set Tick | 设置Tick |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Confirm Stats | 确认数据 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Don\'t Care/Fixed Gender/Genderless | 不考虑/固定性别/无性别 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Gender | 性别比例 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Capture | 正常捕捉 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Date | 日期 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Emerald | 绿宝石 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Ruby\\Sapphire | 红宝石\\蓝宝石 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Synch Nature | 同步性格 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Synchronize Only | 仅同步 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Min / Max Minute | 最小/最大分钟 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Min / Max Hour | 最小/最大时 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Dead Battery | 电池没电 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Min / Max Frame | 最小/最大帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Seed Time | Seed时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Frame | 帧数 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Offset | 偏移 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Occidentary | 偶然值Occidentary |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Frame Time | 过帧时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Encounter Slot | 遭遇槽位 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | !!! | 异色 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Hidden | 觉醒力量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Power | 觉醒力量威力 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Encounter Type | 相遇类型 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Method | 算法 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Male | 雄性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Female | 雌性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Stationary\\Gift Pokémon | 定点\\礼物宝可梦 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Generate | 计算 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Emerald Egg IVs | 绿宝石蛋个体值 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Normal Spreads | 普通遗传 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Split Spreads | 分裂遗传 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Alternate Spreads | 交替遗传 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Show Inheritance | 显示遗传来源 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Parent B | 父母B |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Parent A | 父母A |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Egg Pickup Frame | 蛋领取帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Egg Pickup Time | 蛋领取时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Swap Parents | 交换父母数值 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Emerald Shiny Egg | 绿宝石异色蛋 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | This value is typically 13 + number of pokemon in party | 这个值通常是13+背包中宝可梦的数量 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Calibration | 校准值 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Everstone | 不变之石 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Redraws | 查看图鉴次数 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Compatibility | 相性 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Egg Held Frame | 蛋生成帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Egg Held Time | 蛋生成时间 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Advances | 帧数 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Ruby\\Sapphire Shiny Egg | 红\\蓝宝石异色蛋 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Initial Seed | 初始seed |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Pickup Frame | 蛋领取帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Frame Held | 蛋生成帧 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | FRLG Shiny Egg | 火红叶绿异色蛋 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Lower Half PID | PID 低半部分 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Wild | 野生宝可梦 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Include Synch/Charm | 首发同步/迷人之躯 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Clear | 清空 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Cancel | 取消 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Type | 类型 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Slots | 槽位 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Awaiting Command | 等待操作... |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Lead | 首发 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Slot | 槽位 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Hidden | 觉醒 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Hidden | 觉醒力量威力 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Power | 威力 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Don\'t Care / Genderless | 不考虑/无性别 |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Male (100% Male) | ♂(只有♂) |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | Female (100% Female) | ♀(只有♀) |
| `RNGReporter/TimeFinder3rd.Designer.cs` | `literal` | 3rd Generation Time Finder | 第三世代时间查找器 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Hardy | 勤奋 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Lonely | 怕寂寞 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Brave | 勇敢 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Adamant | 固执 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Naughty | 顽皮 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Bold | 大胆 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Docile | 坦率 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Relaxed | 悠闲 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Impish | 淘气 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Lax | 乐天 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Timid | 胆小 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Hasty | 急躁 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Serious | 认真 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Jolly | 爽朗 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Naive | 天真 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Modest | 内敛 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Mild | 慢吞吞 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Quiet | 冷静 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Bashful | 害羞 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Rash | 马虎 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Calm | 温和 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Gentle | 温顺 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Sassy | 自大 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Careful | 慎重 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Quirky | 浮躁 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Fighting | 格斗 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Flying | 飞行 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Poison | 毒 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Ground | 地面 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Rock | 岩石 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Bug | 虫 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Ghost | 幽灵 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Steel | 钢 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Fire | 火 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Water | 水 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Grass | 草 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Electric | 电 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Psychic | 超能 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Ice | 冰 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Dragon | 龙 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Dark | 恶 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Any | 任意 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Wild Pokémon | 野生宝可梦 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Wild Pokémon (Old Rod) | 野生宝可梦（破旧钓竿） |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Wild Pokémon (Good Rod) | 野生宝可梦（好钓竿） |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Wild Pokémon (Super Rod) | 野生宝可梦（厉害钓竿） |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Stationary Pokémon | 定点宝可梦 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Safari Zone | 狩猎地带 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Frame | 帧 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Save Output to TXT | 保存输出到 TXT |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | TXT Files\|*.txt | TXT 文件\|*.txt |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | The parent IVs you have listed cannot produce your desired search results. | 你列出的父母 IV 无法产生期望的搜索结果。 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | HP: Lower limit > Upper limit | HP：下限 > 上限 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Atk: Lower limit > Upper limit | 攻击：下限 > 上限 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Def: Lower limit > Upper limit | 防御：下限 > 上限 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | SpA: Lower limit > Upper limit | 特攻：下限 > 上限 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | SpD: Lower limit > Upper limit | 特防：下限 > 上限 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Spe: Lower limit > Upper limit | 速度：下限 > 上限 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Searching | 计算中 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Done. - Awaiting Command | 完成了 -等待操作... |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | None | 无 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Cute Charm | 迷人之躯 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | !!! | 异色 |
| `RNGReporter/TimeFinder3rd.cs` | `literal` | Cancelled. - Awaiting Command | 取消了 -等待操作... |
| `RNGReporter/TimeFinder4th.Designer.cs` | `copySeedToClipboardToolStripMenuItem2.Text` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `generateTimeToolStripMenuItem.Text` | Generate More Times ... | 复制seed到seed to time |
| `RNGReporter/TimeFinder4th.Designer.cs` | `outputResultsToTXTToolStripMenuItem1.Text` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `copySeedToClipboardToolStripMenuItem.Text` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `setAsTargetFrameToolStripMenuItem.Text` | Set as Target Frame | 设为目标帧 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `jumpToTargetFrameToolStripMenuItem.Text` | Jump to Target Frame | 跳至目标帧 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `generateAdjacentToolStripMenuItem.Text` | Generate Adjacent Results ... | 计算相邻结果... |
| `RNGReporter/TimeFinder4th.Designer.cs` | `returnToResultsToolStripMenuItem.Text` | Return to Results | 返回至结果 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `outputResultsToTXTToolStripMenuItem.Text` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `tabPageEggIVs.Text` | Egg IVs | 蛋个体值 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `radioButtonEggHGSS.Text` | Heart Gold\\Soul Silver | 心金\\魂银 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `radioButtonEggDPPt.Text` | Diamond\\Pearl\\Platinum | 钻石\\珍珠\\白金 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `checkBoxShowInheritance.Text` | Show Inheritance | 显示遗传来源 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label29.Text` | Spe | 速度 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label27.Text` | SpD | 特防 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label25.Text` | SpA | 特攻 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label24.Text` | Def | 防御 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label12.Text` | Atk | 攻击 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label11.Text` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `lblIVB.Text` | Parent B | 父母B |
| `RNGReporter/TimeFinder4th.Designer.cs` | `lblIVA.Text` | Parent A | 父母A |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label14.Text` | Year | 年份 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label5.Text` | Min / Max Delay | 最小/最大Delay |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label3.Text` | Min / Max Frame | 最小/最大帧 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `tabPageShinyEgg.Text` | Shiny Egg | 异色蛋 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `checkBoxNoHappiness.Text` | Avoid Happiness Checker | 不轻触亲密度检测器 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label8.Text` | Max Taps | 最大轻触下屏次数 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `checkBoxIntlParents.Text` | International Parents | 国际婚姻 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `radioButtonHGSS.Text` | Heart Gold\\Soul Silver | 心金\\魂银 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `radioButtonDPPt.Text` | Diamond\\Pearl\\Platinum | 钻石\\珍珠\\白金 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label92.Text` | Gender | 性别比例 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `checkBoxShinyShinyOnly.Text` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `labelShinyNature.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `labelShinyAbility.Text` | Ability | 特性 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `labelShinyDelay.Text` | Min / Max Delay | 最小/最大Delay |
| `RNGReporter/TimeFinder4th.Designer.cs` | `labelShinyYear.Text` | Year | 年份 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `tabPageCapture.Text` | Capture | 正常捕捉 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label2.Text` | Ratio | 比例 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label31.Text` | Gender | 性别 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `copySeedToClipboardToolStripMenuItem1.Text` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `generateTimesToolStripMenuItem.Text` | Generate More Times ... | 复制seed到seed to time |
| `RNGReporter/TimeFinder4th.Designer.cs` | `outputCapResultsToTXTToolStripMenuItem.Text` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label54.Text` | Encounter Slot | 遭遇槽位 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label52.Text` | Encounter Type | 相遇类型 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `labelCapMinMaxFrame.Text` | Min / Max Frame | 最小/最大帧 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label22.Text` | Min / Max Delay | 最小/最大Delay |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label20.Text` | Year | 年份 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label30.Text` | Method | 算法  |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label23.Text` | Ability | 特性 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `checkBoxShinyOnly.Text` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `label21.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `toolTipDataGrid.ToolTipTitle` | Gender Ratio | 性别比例 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `toolTipGenderRatio.ToolTipTitle` | Gender Ratio | 性别比例 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `buttonAnySlot.Text` | Any | 任意 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `buttonCapGenerate.Text` | Generate | 计算 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `buttonAnyNature.Text` | Any | 任意 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `ShinyOffset.HeaderText` | Frame | 帧数 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `shinyShinyDisplay.HeaderText` | !!! | 异色 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `ShinyNature.HeaderText` | Nature | 性格 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `dataGridViewTextBoxColumn4.HeaderText` | Ability | 特性 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `ShinyFlipSequence.HeaderText` | Flip Sequence | 硬币序列 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `ShinyTaps.HeaderText` | Taps | 轻触下屏次数 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `ShinyFlips.HeaderText` | Additional Flips | 还需掷硬币次数 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `buttonShinyClearAbility.Text` | Any | 任意 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `buttonShinyGenerate.Text` | Generate | 计算 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `buttonShinyClearNature.Text` | Any | 任意 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `Date.HeaderText` | Date | 日期 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `Offset.HeaderText` | Frame | 帧数 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `HP.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `Atk.HeaderText` | Atk | 攻击 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `Def.HeaderText` | Def | 防御 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `SpA.HeaderText` | SpA | 特攻 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `SpD.HeaderText` | SpD | 特防 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `Spe.HeaderText` | Spe | 速度 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `Flips.HeaderText` | Flip Sequence | 硬币序列 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `button1.Text` | Search Flips | 硬币反查 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `buttonEggGenerate.Text` | Generate | 计算 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `ShinyPatchFrame.HeaderText` | ✨Patch Frame | ✨补丁帧 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `CapOffset.HeaderText` | Frame | 帧数 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `Hour.HeaderText` | Hour | 时 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `EncounterMod.HeaderText` | Required Lead | 需要首发 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `EncounterSlot.HeaderText` | Encounter Slot | 遭遇槽位 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `Shiny.HeaderText` | !!! | 异色 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `Nature.HeaderText` | Nature | 性格 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `Ability.HeaderText` | Ability | 特性 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `CapHP.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `CapAtk.HeaderText` | Atk | 攻击 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `CapDef.HeaderText` | Def | 防御 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `CapSpA.HeaderText` | SpA | 特攻 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `CapSpD.HeaderText` | SpD | 特防 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `CapSpe.HeaderText` | Spe | 速度 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `HiddenPower.HeaderText` | Hidden | 觉醒力量 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `HiddenPowerPower.HeaderText` | Power | 觉醒力量威力 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Generate More Times ... | 复制seed到seed to time |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Set as Target Frame | 设为目标帧 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Jump to Target Frame | 跳至目标帧 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Generate Adjacent Results ... | 计算相邻结果... |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Return to Results | 返回至结果 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Egg IVs | 蛋个体值 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Heart Gold\\Soul Silver | 心金\\魂银 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Diamond\\Pearl\\Platinum | 钻石\\珍珠\\白金 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Show Inheritance | 显示遗传来源 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Parent B | 父母B |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Parent A | 父母A |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Year | 年份 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Min / Max Delay | 最小/最大Delay |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Min / Max Frame | 最小/最大帧 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Shiny Egg | 异色蛋 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Avoid Happiness Checker | 不轻触亲密度检测器 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Max Taps | 最大轻触下屏次数 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | International Parents | 国际婚姻 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Gender | 性别比例 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Nature | 性格 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Ability | 特性 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Capture | 正常捕捉 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Ratio | 比例 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Gender | 性别 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Encounter Slot | 遭遇槽位 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Encounter Type | 相遇类型 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Method | 算法  |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Gender Ratio | 性别比例 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | All Ratios | 所有比例 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Fixed Gender | 固定性别 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Any | 任意 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Male | 雄性 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Female | 雌性 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Stationary\\Gift Pokémon | 定点\\礼物宝可梦 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Generate | 计算 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Offset | 偏移 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Frame | 帧数 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | !!! | 异色 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Flip Sequence | 硬币序列 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Taps | 轻触下屏次数 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Additional Flips | 还需掷硬币次数 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Don\'t Care/Fixed Gender/Genderless | 不考虑/固定性别/无性别 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Date | 日期 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Search Flips | 硬币反查 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | ✨Patch Frame | ✨补丁帧 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Hour | 时 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Required Lead | 需要首发 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Hidden | 觉醒力量 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | Power | 觉醒力量威力 |
| `RNGReporter/TimeFinder4th.Designer.cs` | `literal` | 4th Generation Time Finder | 第四世代时间查找器 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Any | 任意 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | You must enter a year greater than 1999. | 你必须输入大于 1999 的年份。 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Please Enter a Valid Year | 请输入一个有效年份 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Flip Sequence | 硬币序列 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Elm Sequence | 电话序列 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Def | 防御 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | SpD | 特防 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Spe | 速度 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Save Output to TXT | 保存输出到 TXT |
| `RNGReporter/TimeFinder4th.cs` | `literal` | TXT Files\|*.txt | TXT 文件\|*.txt |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Wild Pokémon | 野生宝可梦 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Wild Pokémon (Old Rod) | 野生宝可梦（破旧钓竿） |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Wild Pokémon (Good Rod) | 野生宝可梦（好钓竿） |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Wild Pokémon (Super Rod) | 野生宝可梦（厉害钓竿） |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Stationary Pokémon | 定点宝可梦 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Safari Zone | 狩猎地带 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Headbutt | 头锤树 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Stationary\\Gift Pokémon | 定点\\礼物宝可梦 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Synchronize | 同步 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Cute Charm | 迷人之躯 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Suction Cups | 吸盘 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Nature | 性格 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Greyed-out natures are natures with no competitive value. | 灰色字体的性格是没有竞争价值的性格。 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | !!! | 异色 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | A !!! in this column indicates the frame will be shiny. | 如果该帧的异色列有!!!则说明该帧是异色 |
| `RNGReporter/TimeFinder4th.cs` | `literal` | Encounter Slot | 遭遇槽 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `copySeedToClipboardToolStripMenuItem1.Text` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `copyCgearToClipboard.Text` | Copy C-Gear Seed to Clipboard | 复制 Ｃ装置 Seed 到剪贴板 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `calibrateDelayIVs.Text` | Calibrate C-Gear Delay by Wild IVs | 通过野生 IV 校准 Ｃ装置 Delay |
| `RNGReporter/TimeFinder5th.Designer.cs` | `generateTimesToolStripMenuItem.Text` | Generate More Times ... | 复制seed到seed to time |
| `RNGReporter/TimeFinder5th.Designer.cs` | `generateAdjacentSeedsToolStripMenuItem.Text` | Generate Adjacent Seeds ... | 计算附近的Seed... |
| `RNGReporter/TimeFinder5th.Designer.cs` | `generateEntralinkNatureSeedsToolStripMenuItem.Text` | Generate Entralink Nature Seeds ... | 计算连入之森特性的Seed... |
| `RNGReporter/TimeFinder5th.Designer.cs` | `outputCapResultsToTXTToolStripMenuItem.Text` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `copySeedToClipboardToolStripMenuItem2.Text` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `generateAdjacentSeedsToolStripMenuItem1.Text` | Generate Adjacent Seeds... | 计算附近的Seed... |
| `RNGReporter/TimeFinder5th.Designer.cs` | `outputResultsToTXTToolStripMenuItem1.Text` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `tabPageShinyEgg.Text` | Eggs | 蛋 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `cbShinyCharm.Text` | Shiny Charm | 闪耀护符 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `cbNidoBeat.Text` | Nidoran/Volbeat | 尼多一家/电萤虫 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label8.Text` | Spe | 速度 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label7.Text` | SpD | 特防 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label5.Text` | SpA | 特攻 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label4.Text` | Def | 防御 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label3.Text` | Atk | 攻击 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label2.Text` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxIntlParents.Text` | International Parents | 国际婚姻 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label92.Text` | Gender | 性别比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxShinyShinyOnly.Text` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxShowInheritance.Text` | Show Inheritance | 显示遗传来源 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `labelShinyFatherIVs.Text` | Father IVs | 父亲个体 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxShinyDittoParent.Text` | Ditto Parent | 百变怪 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label33.Text` | Everstone | 不变之石 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `labelShinyMinMaxFrame.Text` | Min / Max Advances | 最小/最大帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxShinyDreamWorld.Text` | Dream World Ability Only | 仅梦特性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `labelShinyMotherIVs.Text` | Mother IVs | 母亲个体 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `labelShinyNature.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `labelShinyAbility.Text` | Ability | 特性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `labelShinyMonth.Text` | Month | 月份  |
| `RNGReporter/TimeFinder5th.Designer.cs` | `labelShinyYear.Text` | Year | 年份 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `buttonLoadEggSeeds.Text` | Load eggseeds.dat | 加载蛋seed数据 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ShinyOffset.HeaderText` | Frame | 帧数 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `shinyShinyDisplay.HeaderText` | !!! | 异色 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ShinyNature.HeaderText` | Nature | 性格 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn4.HeaderText` | Ability | 特性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ShinyDreamAbility.HeaderText` | Dream Ability | 梦特性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ShinyHP.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ShinyAtk.HeaderText` | Atk | 攻击 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ShinyDef.HeaderText` | Def | 防御 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ShinySpA.HeaderText` | SpA | 特攻 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ShinySpD.HeaderText` | SpD | 特防 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ShinySpe.HeaderText` | Spe | 速度 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ShinyHidden.HeaderText` | Hidden | 觉醒力量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ShinyPower.HeaderText` | Power | 觉醒力量威力 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ColumnEggDate.HeaderText` | Date\\Time | 日期\\时间 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `shinyKeypress.HeaderText` | Keypress | 按键 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `buttonShinyGenerate.Text` | Generate | 计算 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `buttonShinyClearNature.Text` | Any | 任意 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `tabPageCapture.Text` | Capture | 正常捕捉 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `PrefGroupBox.Text` | Preferences | 偏好 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label21.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxTriggerBattle.Text` | Battle Trigger | 对战触发 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label23.Text` | Ability | 特性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `buttonCapGenerate.Text` | Search | 计算 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label54.Text` | Slot | 遭遇槽位 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `LevelLabel.Text` | Level | 等级 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label1.Text` | Gender | 性别 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxShinyOnly.Text` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `buttonAnyNature.Text` | Any | 任意 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxSynchOnly.Text` | Sync Success | 仅同步生效帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `buttonAnySlot.Text` | Any | 任意 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `SettingsGroupBox.Text` | Settings | 设置 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxDelay.Text` | Calibrate Delay | 校准 Delay |
| `RNGReporter/TimeFinder5th.Designer.cs` | `labelDelay.Text` | Min / Max Delay | 最小/最大Delay |
| `RNGReporter/TimeFinder5th.Designer.cs` | `labelMaxShiny.Text` | Min / Max Shiny Advances | 最大异色帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `labelCapMonth.Text` | Month | 月份 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `labelCapMinMaxLevel.Text` | Min / Max Level | 最小 / 最大等级 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label30.Text` | Method | 算法 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label20.Text` | Year | 年份 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `labelCapMinMaxFrame.Text` | Min / Max IV Frame | 最小/最大帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label9.Text` | IV filters... | 个体值筛选未设置为允许快速搜索\r\n请尝试搜索常见的分配方案\r\n如完美分配或戏法空间的分配方案 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label52.Text` | Encounter Type | 相遇类型 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label10.Text` | Gender Ratio | 比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `tabEvent.Text` | Wondercard | 神秘卡片 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EventFrame.HeaderText` | Frame | 帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EventShiny.HeaderText` | !!! | 异色 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EventNature.HeaderText` | Nature | 性格 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EventAbility.HeaderText` | Ability | 特性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EventHP.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EventAtk.HeaderText` | Atk | 攻击 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EventDef.HeaderText` | Def | 防御 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EventSpA.HeaderText` | SpA | 特攻 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EventSpD.HeaderText` | SpD | 特防 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EventSpe.HeaderText` | Spe | 速度 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn50.HeaderText` | Hidden | 觉醒 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn51.HeaderText` | Power | 威力 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EventDateTime.HeaderText` | Date\\Time | 日期\\时间 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EventKeys.HeaderText` | Keypresses | 按键 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `groupBoxPref.Text` | Preferences | 偏好 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label32.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label34.Text` | Ability | 特性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `buttonEventGenerate.Text` | Search | 搜索 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label38.Text` | Gender | 性别 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `shinyOnlyEvent.Text` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `AnyNatureEvent.Text` | Any | 任意 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `groupBoxSettings.Text` | Settings | 设置 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `SpeciesDex.Text` | Species | 种族 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxGender.Text` | Gender | 性别 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `buttonImportWondercard.Text` | Import | 导入 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxAbility.Text` | Ability | 特性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label36.Text` | Event TID / SID | 活动 TID / SID |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxNatureLock.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxSpe.Text` | Spe | 速度 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxSpD.Text` | SpD | 特防 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxSpA.Text` | SpA | 特攻 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxDef.Text` | Def | 防御 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxAtk.Text` | Atk | 攻击 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxHP.Text` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label29.Text` | Min / Max Advances | 最小 / 最大推进 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label31.Text` | Month | 月份 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label35.Text` | Year | 年份 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label40.Text` | Shininess | 异色情况 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label39.Text` | Gender Ratio | 性别比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `tabPageHiddenGrotto.Text` | Hidden Grotto | 隐藏洞穴 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label18.Text` | Gender Ratio (% F) | 性别比例(%♀) |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label17.Text` | Gender | 性别比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label16.Text` | SubSlot | 子槽位 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label14.Text` | Slot | 槽位 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label15.Text` | Grotto Number | 洞穴数量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label13.Text` | Open Hollows | 空洞穴 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label6.Text` | Max Advances | 最大帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label11.Text` | Year | 年份 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label12.Text` | Month | 月份  |
| `RNGReporter/TimeFinder5th.Designer.cs` | `btnHHGenerate.Text` | Generate | 计算 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn8.HeaderText` | Hollow Number | 空洞穴数量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn2.HeaderText` | Starting Frame | 初始帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn3.HeaderText` | Frame | 帧数 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn5.HeaderText` | Slot | 槽位 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn7.HeaderText` | Sub Slot | 子槽位 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn9.HeaderText` | Gender | 性别比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn23.HeaderText` | Date\\Time | 日期\\时间 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn25.HeaderText` | Keypresses | 按键 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `toolStripMenuItem1.Text` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `toolStripMenuItem2.Text` | Generate Adjacent Seeds... | 计算附近的Seed... |
| `RNGReporter/TimeFinder5th.Designer.cs` | `toolStripMenuItem4.Text` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `tabPageDreamRadar.Text` | Dream Radar | 宝可梦AR搜寻器 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label19.Text` | Shininess | 异色情况 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label22.Text` | Ratio | 比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label24.Text` | Gender | 性别 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label25.Text` | Min / Max Frame | 最小/最大帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label26.Text` | Year | 年份 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label27.Text` | Month | 月份  |
| `RNGReporter/TimeFinder5th.Designer.cs` | `cbDRShiny.Text` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label28.Text` | Nature | 性格 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `btnDRGenerate.Text` | Generate | 计算 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `btnDRAnyNature.Text` | Any | 任意 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn10.HeaderText` | Frame | 帧数 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn12.HeaderText` | !!! | 异色 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn13.HeaderText` | Nature | 性格 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn16.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn17.HeaderText` | Atk | 攻击 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn18.HeaderText` | Def | 防御 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn26.HeaderText` | SpA | 特攻 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn27.HeaderText` | SpD | 特防 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn28.HeaderText` | Spe | 速度 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn29.HeaderText` | Hidden | 觉醒力量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn30.HeaderText` | Power | 觉醒力量威力 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn35.HeaderText` | Date\\Time | 日期\\时间 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn36.HeaderText` | Keypress | 按键 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `tabPagePickup.Text` | Pickup | 拾取 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label45.Text` | 1. Use Honey / Sweet Scent at the frame indicated, then defeat the wild Pokémon. | 1. 在指定帧使用甜甜蜜/甜甜香气，然后击败野生宝可梦。 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label44.Text` | Celestial Tower rooftop is recommended since it also has no NPCs. | 推荐天堂之塔塔顶，因为那里也没有 NPC。 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label43.Text` | 4. Wild Pokémon that have a chance of holding an item, affect the frame hit. | 4. 可能携带道具的野生宝可梦会影响命中帧。 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label42.Text` | 2. An \"Active Roamer\" (BW only) affects the initial frame. | 2. 活动游走宝可梦（仅 BW）会影响初始帧。 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label37.Text` | Notes: | 备注: |
| `RNGReporter/TimeFinder5th.Designer.cs` | `cbActiveRoamer.Text` | Active Roamer | 活动游走宝可梦 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn32.HeaderText` | Frame | 帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `colItem1.HeaderText` | Item 1 | 道具 1 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `colItem2.HeaderText` | Item 2 | 道具 2 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `colItem3.HeaderText` | Item 3 | 道具 3 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `colItem4.HeaderText` | Item 4 | 道具 4 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `colItem5.HeaderText` | Item 5 | 道具 5 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `colItem6.HeaderText` | Item 6 | 道具 6 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn69.HeaderText` | Date\\Time | 日期\\时间 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `dataGridViewTextBoxColumn71.HeaderText` | Keypresses | 按键 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `buttonPickupSearch.Text` | Search | 搜索 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `groupBox2.Text` | Target Item | 目标道具 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ClearList6.Text` | Clear | 清除 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ClearList5.Text` | Clear | 清除 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ClearList4.Text` | Clear | 清除 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ClearList3.Text` | Clear | 清除 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ClearList2.Text` | Clear | 清除 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `ClearList1.Text` | Clear | 清除 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `groupBox1.Text` | Level | 等级 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxParty6.Text` | Party 6 | 队伍 6 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxParty5.Text` | Party 5 | 队伍 5 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxParty4.Text` | Party 4 | 队伍 4 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxParty3.Text` | Party 3 | 队伍 3 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxParty2.Text` | Party 2 | 队伍 2 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `checkBoxParty1.Text` | Party 1 | 队伍 1 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label49.Text` | Min / Max Advances | 最小 / 最大推进 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label47.Text` | Year | 年份 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `label48.Text` | Month | 月份 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `toolTipGenderRatio.ToolTipTitle` | Gender Ratio | 性别比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `toolTipDataGrid.ToolTipTitle` | Gender Ratio | 性别比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `groupBoxConfiguration.Text` | Configuration | 基本配置 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `buttonEditProfile.Text` | Edit | 编辑 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `CapOffset.HeaderText` | IV Frame | 帧数 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EncounterMod.HeaderText` | Required Lead | 需要首发 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `LuckyLevel.HeaderText` | Lucky Power | 幸运之力 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `NearestShiny.HeaderText` | Shiny Frame | 异色帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EncounterRatio.HeaderText` | Encounter Ratio | 遇敌比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EncType.HeaderText` | Encounter Type | 遭遇类型 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `EncounterSlot.HeaderText` | Encounter Slot | 遭遇槽位 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `Lvl.HeaderText` | Level | 等级 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `Shiny.HeaderText` | !!! | 异色 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `Nature.HeaderText` | Nature | 性格 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `Ability.HeaderText` | Ability | 特性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `CapHP.HeaderText` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `CapAtk.HeaderText` | Atk | 攻击 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `CapDef.HeaderText` | Def | 防御 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `CapSpA.HeaderText` | SpA | 特攻 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `CapSpD.HeaderText` | SpD | 特防 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `CapSpe.HeaderText` | Spe | 速度 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `HiddenPower.HeaderText` | Hidden | 觉醒力量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `HiddenPowerPower.HeaderText` | Power | 觉醒力量威力 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `CapDateTime.HeaderText` | Date\\Time | 日期\\时间 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `CapKeypress.HeaderText` | Keypresses | 按键 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `Synchable.HeaderText` | Synchronized | 同步 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `CgearSeed.HeaderText` | C-Gear Seed | Ｃ装置 Seed |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Copy Seed to Clipboard | 复制Seed到剪贴板 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Copy C-Gear Seed to Clipboard | 复制 Ｃ装置 Seed 到剪贴板 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Calibrate C-Gear Delay by Wild IVs | 通过野生 IV 校准 Ｃ装置 Delay |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Generate More Times ... | 复制seed到seed to time |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Generate Adjacent Seeds ... | 计算附近的Seed... |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Generate Entralink Nature Seeds ... | 计算连入之森特性的Seed... |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Output Results to TXT ... | 输出结果至TXT文本文件 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Generate Adjacent Seeds... | 计算附近的Seed... |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Eggs | 蛋 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Shiny Charm | 闪耀护符 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Nidoran/Volbeat | 尼多一家/电萤虫 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Spe | 速度 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | SpD | 特防 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | SpA | 特攻 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Def | 防御 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Atk | 攻击 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | HP | 觉醒力量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | International Parents | 国际婚姻 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Gender | 性别比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Show Inheritance | 显示遗传来源 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Father IVs | 父亲个体 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Ditto Parent | 百变怪 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Everstone | 不变之石 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Min / Max Advances | 最小/最大帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Dream World Ability Only | 仅梦特性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Mother IVs | 母亲个体 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Nature | 性格 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Ability | 特性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Month | 月份  |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Year | 年份 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Load eggseeds.dat | 加载蛋seed数据 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Offset | 偏移 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Frame | 帧数 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | !!! | 异色 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Dream Ability | 梦特性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Hidden | 觉醒力量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Power | 觉醒力量威力 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Date\\Time | 日期\\时间 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Keypress | 按键 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Don\'t Care/Fixed Gender/Genderless | 不考虑/固定性别/无性别 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Any | 任意 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Generate | 计算 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Capture | 正常捕捉 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Preferences | 偏好 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Male | 雄性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Female | 雌性 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Battle Trigger | 对战触发 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Search | 计算 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Slot | 遭遇槽位 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Level | 等级 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Gender | 性别 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Sync Success | 仅同步生效帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Settings | 设置 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Calibrate Delay | 校准 Delay |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Min / Max Delay | 最小/最大Delay |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Min / Max Shiny Advances | 最大异色帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Month | 月份 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Min / Max Level | 最小 / 最大等级 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Method | 算法 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Min / Max IV Frame | 最小/最大帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | IV filters... | 个体值筛选未设置为允许快速搜索\r\n请尝试搜索常见的分配方案\r\n如完美分配或戏法空间的分配方案 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Encounter Type | 相遇类型 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | All Ratios | 所有比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Fixed Gender | 固定性别 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Gender Ratio | 比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Wondercard | 神秘卡片 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Frame | 帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Hidden | 觉醒 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Power | 威力 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Keypresses | 按键 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Search | 搜索 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Species | 种族 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Import | 导入 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Event TID / SID | 活动 TID / SID |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Hardy | 勤奋 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Lonely | 怕寂寞 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Brave | 勇敢 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Adamant | 固执 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Naughty | 顽皮 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Bold | 大胆 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Docile | 坦率 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Relaxed | 悠闲 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Impish | 淘气 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Lax | 乐天 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Timid | 胆小 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Hasty | 急躁 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Serious | 认真 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Jolly | 爽朗 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Naive | 天真 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Modest | 内敛 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Mild | 慢吞吞 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Quiet | 冷静 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Bashful | 害羞 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Rash | 马虎 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Calm | 温和 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Gentle | 温顺 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Sassy | 自大 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Careful | 慎重 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Quirky | 浮躁 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Never Shiny | 不可能异色 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | May Be Shiny | 可能异色 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Always Shiny | 必定异色 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Min / Max Advances | 最小 / 最大推进 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Shininess | 异色情况 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Gender Ratio | 性别比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Hidden Grotto | 隐藏洞穴 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Gender Ratio (% F) | 性别比例(%♀) |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | SubSlot | 子槽位 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Slot | 槽位 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Grotto Number | 洞穴数量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Open Hollows | 空洞穴 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Max Advances | 最大帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Hollow Number | 空洞穴数量 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Starting Frame | 初始帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Sub Slot | 子槽位 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Dream Radar | 宝可梦AR搜寻器 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Ratio | 比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Min / Max Frame | 最小/最大帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Pickup | 拾取 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | 1. Use Honey / Sweet Scent at the frame indicated, then defeat the wild Pokémon. | 1. 在指定帧使用甜甜蜜/甜甜香气，然后击败野生宝可梦。 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Celestial Tower rooftop is recommended since it also has no NPCs. | 推荐天堂之塔塔顶，因为那里也没有 NPC。 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | 4. Wild Pokémon that have a chance of holding an item, affect the frame hit. | 4. 可能携带道具的野生宝可梦会影响命中帧。 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | 2. An \"Active Roamer\" (BW only) affects the initial frame. | 2. 活动游走宝可梦（仅 BW）会影响初始帧。 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Notes: | 备注: |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Active Roamer | 活动游走宝可梦 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Item 1 | 道具 1 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Item 2 | 道具 2 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Item 3 | 道具 3 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Item 4 | 道具 4 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Item 5 | 道具 5 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Item 6 | 道具 6 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Target Item | 目标道具 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Clear | 清除 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Party 6 | 队伍 6 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Party 5 | 队伍 5 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Party 4 | 队伍 4 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Party 3 | 队伍 3 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Party 2 | 队伍 2 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Party 1 | 队伍 1 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Configuration | 基本配置 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Edit | 编辑 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | IV Frame | 帧数 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Required Lead | 需要首发 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Lucky Power | 幸运之力 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Shiny Frame | 异色帧 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Encounter Ratio | 遇敌比例 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Encounter Type | 遭遇类型 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Encounter Slot | 遭遇槽位 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Synchable | 同步能力 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | Synchronized | 同步 |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | C-Gear Seed | Ｃ装置 Seed |
| `RNGReporter/TimeFinder5th.Designer.cs` | `literal` | 5th Generation Time Finder | 第五世代时间查找器 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Any | 任意 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Shaking Grass | 摇动草丛 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Bubble Spot | 水纹水面 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Fishing Spot | 钓鱼点 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Cave Spot | 卷尘地面 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Gift Pokémon | 礼物宝可梦 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | No profiles were detected. Please setup a profile first. | 没有检测到GEN5的存档信息，请先新增一个存档信息。 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | This method is not possible in BW2. | 此方法在 BW2 中不可用。 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Error | 错误 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | You must enter a year greater than 1999. | 你必须输入大于 1999 的年份。 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Please Enter a Valid Year | 请输入一个有效年份 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | error in loading roamer tables | 加载游走宝可梦表时出错 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | error in loading hashtables | 加载hash表时出错 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Min / Max Frame | 最小/最大帧 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Shiny Only | 仅异色 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Synchable | 同步能力 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Save Output to TXT | 保存输出到 TXT |
| `RNGReporter/TimeFinder5th.cs` | `literal` | TXT Files\|*.txt | TXT 文件\|*.txt |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Synchronize | 同步 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Cute Charm | 迷人之躯 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Suction Cups | 吸盘 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Compoundeyes | 复眼 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Nature | 性格 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Greyed-out natures are natures with no competitive value. | 灰色字体的性格是没有竞争价值的性格。 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | !!! | 异色 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | A !!! in this column indicates the frame will be shiny. | 如果该帧的异色列有!!!则说明该帧是异色 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Encounter Slot | 遭遇槽 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | 5th Gen Wonder Card \|*.pgf | 第五世代神秘卡片 \|*.pgf |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Select a Wonder Card File | 选择神秘卡片文件 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Unable to have Ditto parent and Dream World ability at the same time. | 不能同时拥有同上父母和梦特性。 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Year must be between 2000 and 2099. | 年份必须在2000到2099之间 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | The parent IVs you have listed cannot produce your desired search results. | 你列出的父母 IV 无法产生期望的搜索结果。 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | IV filters are set for fast searching. | IV 筛选已设置为快速搜索。 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Currently not supported for this method. | 当前不支持此方法。 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Loading the seeds file. Please be patient and wait for it to finish. | 正在加载 seed 文件，请耐心等待完成。 |
| `RNGReporter/TimeFinder5th.cs` | `literal` | Seeds successfully loaded. | seed记载成功 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `groupBox1.Text` | Stage One | 第一阶段 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `checkBox1.Text` | Countdown Beep | 倒计时提示音 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `label9.Text` | seconds | 秒 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `groupBox2.Text` | Stage Two | 第二阶段 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `checkBox2.Text` | Countdown Beep | 倒计时提示音 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `label3.Text` | seconds | 秒 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `label1.Text` | frames | 帧 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `button2.Text` | START | 开始 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `groupBox3.Text` | Game Entry Seconds (4th Gen) | 进入游戏秒数（第四世代） |
| `RNGReporter/TwoStageTimer.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `literal` | Stage One | 第一阶段 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `literal` | Countdown Beep | 倒计时提示音 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `literal` | seconds | 秒 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `literal` | Stage Two | 第二阶段 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `literal` | frames | 帧 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `literal` | START | 开始 |
| `RNGReporter/TwoStageTimer.Designer.cs` | `literal` | Game Entry Seconds (4th Gen) | 进入游戏秒数（第四世代） |
| `RNGReporter/TwoStageTimer.Designer.cs` | `literal` | Two-Stage Timer | 双阶段计时器 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `gbSeed.Text` | Seed Encryption Variables | Seed加密变量 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `cbMemoryLink.Text` | Memory Link | 记忆连接 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `label18.Text` | Hour | 时 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `label17.Text` | Minute | 分钟 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `label19.Text` | Date | 日期 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `label25.Text` | Seconds | 秒数 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `label6.Text` | Language | 游戏语言 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `cbGxStat.Text` | Only Search Min&&Max GxStat | 只搜索最小和最大GxStat |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `label5.Text` | DS Type | DS机型 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `checkBoxSoftReset.Text` | Soft Reset | 软复位 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `label100.Text` | Held Buttons | 按键 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `label2.Text` | Min | 最小 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `label3.Text` | Max | 最大 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `label26.Text` | DS MAC Address | DS MAC地址 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `lblSeconds.Text` | Seconds | 秒数 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `label8.Text` | Version | 游戏版本 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `gbSpins.Text` | Link Spins | 进入连接方向序列 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `btnReset.Text` | Reset | 重置 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `btnSearch.Text` | Search | 计算 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `clmnActualSeconds.HeaderText` | Actual Seconds | 实际秒数 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `btnSendProfile.Text` | Send Results to Profile | 结果发送到存档信息 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Seed Encryption Variables | Seed加密变量 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Memory Link | 记忆连接 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Hour | 时 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Minute | 分钟 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Date | 日期 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Seconds | 秒数 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Language | 游戏语言 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Only Search Min&&Max GxStat | 只搜索最小和最大GxStat |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | DS Type | DS机型 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | None | 无 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | R | 雷公 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | L | 拉帝欧斯\\拉迪亚斯 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Soft Reset | 软复位 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Held Buttons | 按键 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Min | 最小 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Max | 最大 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | DS MAC Address | DS MAC地址 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Black 2 | 黑2 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | White 2 | 白2 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Version | 游戏版本 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Microsoft Sans Serif | 宋体 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Reset | 重置 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Search | 计算 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | Actual Seconds | 实际秒数 |
| `RNGReporter/UnovaLinkCalibration.Designer.cs` | `literal` | UnovaLinkCalibration | 通过合众连接校准 |
| `RNGReporter/UnovaLinkCalibration.cs` | `literal` | Your MAC address is missing some digits.  Double-check your MAC address. | MAC 地址缺少部分数字，请再次检查 MAC 地址。 |
| `RNGReporter/WarningSZ.Designer.cs` | `buttonOk.Text` | OK | 确定 |
| `RNGReporter/WarningSZ.Designer.cs` | `label2.Text` | BOLD. | 加粗。 |
| `RNGReporter/WarningSZ.Designer.cs` | `literal` | OK | 确定 |
| `RNGReporter/WarningSZ.Designer.cs` | `literal` | BOLD. | 加粗。 |
| `RNGReporter/WarningSZ.Designer.cs` | `literal` | Warning | 提示 |
