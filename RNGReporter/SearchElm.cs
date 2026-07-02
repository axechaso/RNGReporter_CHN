using RNGReporter.Objects;
using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace RNGReporter
{
    public partial class SearchElm : Form
    {
        private readonly List<Adjacent> _adjacents;
        private GlassButton buttonLanguage;
        private PhoneHelpLanguage phoneHelpLanguage = PhoneHelpLanguage.Japanese;

        public SearchElm()
        {
            ReturnElm = "";
            RoamerText = "";
            InitializeComponent();
            InitializeLanguageButton();
            ApplyLocalizedPhoneText();
            labelResults.Visible = false;
        }

        public SearchElm(List<Adjacent> adjacents)
        {
            ReturnElm = "";
            RoamerText = "";
            _adjacents = adjacents;
            InitializeComponent();
            InitializeLanguageButton();
            ApplyLocalizedPhoneText();
            UpdatePossible();
        }

        public string ReturnElm { get; private set; }

        public int ReturnE { get; private set; }

        public int ReturnR { get; private set; }

        public int ReturnL { get; private set; }

        public string RoamerText { get; private set; }

        public List<Adjacent> Possible { get; private set; }

        private void buttonOk_Click(object sender, EventArgs e)
        {
            ReturnElm = textBoxResponses.Text;

            if (maskedTextBoxERoute.Text != "")
                ReturnE = int.Parse(maskedTextBoxERoute.Text);

            if (maskedTextBoxRRoute.Text != "")
                ReturnR = int.Parse(maskedTextBoxRRoute.Text);

            if (maskedTextBoxLRoute.Text != "")
                ReturnL = int.Parse(maskedTextBoxLRoute.Text);
        }

        private void buttonK_Click(object sender, EventArgs e)
        {
            AddLetter("K");
        }

        private void buttonE_Click(object sender, EventArgs e)
        {
            AddLetter("E");
        }

        private void InitializeLanguageButton()
        {
            buttonLanguage = new GlassButton
            {
                Anchor = AnchorStyles.Top | AnchorStyles.Right,
                BackColor = System.Drawing.Color.AntiqueWhite,
                ForeColor = System.Drawing.Color.Black,
                Location = new System.Drawing.Point(471, 110),
                Name = "buttonLanguage",
                OuterBorderColor = System.Drawing.Color.Transparent,
                ShineColor = System.Drawing.SystemColors.Window,
                Size = new System.Drawing.Size(75, 21),
                TabIndex = 61
            };
            buttonLanguage.Click += buttonLanguage_Click;
            groupBox1.Controls.Add(buttonLanguage);
        }

        private void buttonLanguage_Click(object sender, EventArgs e)
        {
            phoneHelpLanguage = ElmCallText.NextLanguage(phoneHelpLanguage);
            ApplyLocalizedPhoneText();
        }

        private void ApplyLocalizedPhoneText()
        {
            labelKElm.Text = ElmCallText.ElmK(phoneHelpLanguage);
            labelEElm.Text = ElmCallText.ElmE(phoneHelpLanguage);
            labelPElm.Text = ElmCallText.ElmP(phoneHelpLanguage);
            labelKIrwin.Text = ElmCallText.IrwinK(phoneHelpLanguage);
            labelEIrwin.Text = ElmCallText.IrwinE(phoneHelpLanguage);
            labelPIrwin.Text = ElmCallText.IrwinP(phoneHelpLanguage);
            buttonLanguage.Text = ElmCallText.LanguageButtonText(phoneHelpLanguage);

            int kHeight = phoneHelpLanguage == PhoneHelpLanguage.Japanese ? 72 : 52;
            int eHeight = phoneHelpLanguage == PhoneHelpLanguage.Japanese ? 52 : 52;
            int pHeight = phoneHelpLanguage == PhoneHelpLanguage.Japanese ? 132 : 64;
            labelKElm.Top = labelKIrwin.Top = 139;
            labelKElm.Height = labelKIrwin.Height = kHeight;
            labelEElm.Top = labelEIrwin.Top = labelKElm.Bottom + 4;
            labelEElm.Height = labelEIrwin.Height = eHeight;
            labelPElm.Top = labelPIrwin.Top = labelEElm.Bottom + 4;
            labelPElm.Height = labelPIrwin.Height = pHeight;
            groupBox1.Height = labelPElm.Bottom + 10;
            groupBox2.Top = groupBox1.Bottom + 7;
            buttonOk.Top = groupBox2.Bottom + 10;
            buttonCancel.Top = buttonOk.Top;
            ClientSize = new System.Drawing.Size(ClientSize.Width, buttonOk.Bottom + 11);
        }

        private void buttonP_Click(object sender, EventArgs e)
        {
            AddLetter("P");
        }

        private void AddLetter(string s)
        {
            textBoxResponses.Text += textBoxResponses.Text == "" ? s : ", " + s;
        }

        private void textBoxResponses_TextChanged(object sender, EventArgs e)
        {
            UpdatePossible();
        }

        private void UpdatePossible()
        {
            if (_adjacents == null || _adjacents.Count == 0) return;
            Possible = _adjacents.FindAll(HasElms);
            labelResults.Text = "可能的结果数量：" + Possible.Count;
        }

        private bool HasElms(Adjacent adjacent)
        {
            return adjacent.ElmResponses.Contains(textBoxResponses.Text) &&
                   (RoamerText == "" || RoamerText == adjacent.RoamerLocations);
        }

        private void maskedTextBoxRoute_TextChanged(object sender, EventArgs e)
        {
            if (maskedTextBoxRRoute.Text == "" && maskedTextBoxRRoute.Text == "" && maskedTextBoxRRoute.Text == "")
            {
                RoamerText = "";
                return;
            }
            bool firstDisplay = true;
            if (maskedTextBoxRRoute.Text != "")
            {
                RoamerText += "R: " + maskedTextBoxRRoute.Text;
                firstDisplay = false;
            }

            if ((maskedTextBoxERoute.Text != ""))
            {
                if (!firstDisplay)
                    RoamerText += "  ";

                RoamerText += "E: " + maskedTextBoxERoute.Text;
                firstDisplay = false;
            }

            if ((maskedTextBoxLRoute.Text != ""))
            {
                if (!firstDisplay)
                    RoamerText += "  ";

                RoamerText += "L: " + maskedTextBoxLRoute.Text;
            }
        }

        private void radioButtonElm_CheckedChanged(object sender, EventArgs e)
        {
            labelKElm.Visible = radioButtonElm.Checked;
            labelEElm.Visible = radioButtonElm.Checked;
            labelPElm.Visible = radioButtonElm.Checked;
        }

        private void radioButtonIrwin_CheckedChanged(object sender, EventArgs e)
        {
            labelKIrwin.Visible = radioButtonIrwin.Checked;
            labelEIrwin.Visible = radioButtonIrwin.Checked;
            labelPIrwin.Visible = radioButtonIrwin.Checked;
        }

        private void labelKIrwin_Click(object sender, EventArgs e)
        {

        }
    }

    internal enum PhoneHelpLanguage
    {
        Japanese,
        Chinese,
        English
    }

    internal static class ElmCallText
    {
        private static readonly string[] ElmKText =
        {
            "K - カントーには まだ ぼくの しらない ポケモンが いるだろうし、\r\n" +
            "ぼくの しらない しんかの ほうほうが あるかも しれないね。\r\n" +
            "そのめで しっかり いろんなものを みておいで！",
            "K - 关都地区应该还有我不知道的宝可梦。也许还有我不熟悉的进化方式，我应该换个角度继续调查！",
            "K - I expect there are some Pokémon in the Kanto region that I don't know. There are probably methods of evolution that I'm not familiar with yet."
        };

        private static readonly string[] ElmEText =
        {
            "E - ポケモンの しんかというのは ほんとうに おくが ふかいよねぇ！ あるじょうけんを みたしたときだけ しんかする ポケモンも いるみたい！",
            "E - 宝可梦的进化方式真是多种多样，不是吗？！有些宝可梦甚至要先满足特定条件才会进化！",
            "E - There are so many different ways that Pokémon evolve, aren't there?! Some Pokémon don't even evolve until they meet certain conditions first!"
        };

        private static readonly string[] ElmPText =
        {
            "P - ポケルスが くっついた ポケモンは どうやら そだちが よくなる みたい げんいんは わからないけど……",
            "P - 感染过宝可病毒的宝可梦似乎升级时成长得更好。我们还不太清楚原因……",
            "P - It seems that Pokémon that have been infected with Pokérus level up better. We're not quite sure why..."
        };

        private static readonly string[] IrwinKText =
        {
            "K - でんわ うれしいなあ！\r\n" +
            "ちょうど ぼくも いま\r\n" +
            "かけようとしてた ところなんだ！\r\n" +
            "きが あうんだね ぼくたち！",
            "K - 你打电话来我真高兴！我正好也想打给你！看来我们很合得来！",
            "K - I'm so glad you called! I was just about to call you, too! I guess we must be a good match!"
        };

        private static readonly string[] IrwinEText =
        {
            "E - きみの かつやくを きいて\r\n" +
            "きょうも しびれているよ！",
            "E - 听说你的冒险事迹真让我热血沸腾！确实如此！",
            "E - Hearing about your escapades really inspires me! It sure does!"
        };

        private static readonly string[] IrwinPText =
        {
            "P - げんきかい？\r\n" +
            "なにしてるの？\r\n" +
            "いま どこにいるの？\r\n" +
            "バッジは いくつ あつまったの？\r\n" +
            "おこづかい どのくらい たまった？\r\n" +
            "おかあさん げんき？\r\n" +
            "ポケモン いっぱい あつめたかい？\r\n" +
            "あしたの てんきは はれかな？\r\n" +
            "ああ もう ききたいこと だらけで はなしが すすまぬ わ！",
            "P - 你好吗？在做什么？在哪里？现在有几枚徽章了？存了多少钱？妈妈好吗？抓了很多宝可梦吗？明天天气会晴吗？啊啊，想聊的太多了！",
            "P - How are you? What are you doing? Where are you? How many Badges do you have now? How much money have you saved? How's your mom? Have you got lots of Pokémon? Is it going to be sunny tomorrow?"
        };

        public static string ElmK(PhoneHelpLanguage language)
        {
            return ElmKText[(int) language];
        }

        public static string ElmE(PhoneHelpLanguage language)
        {
            return ElmEText[(int) language];
        }

        public static string ElmP(PhoneHelpLanguage language)
        {
            return ElmPText[(int) language];
        }

        public static string IrwinK(PhoneHelpLanguage language)
        {
            return IrwinKText[(int) language];
        }

        public static string IrwinE(PhoneHelpLanguage language)
        {
            return IrwinEText[(int) language];
        }

        public static string IrwinP(PhoneHelpLanguage language)
        {
            return IrwinPText[(int) language];
        }

        public static PhoneHelpLanguage NextLanguage(PhoneHelpLanguage language)
        {
            return (PhoneHelpLanguage) (((int) language + 1) % 3);
        }

        public static string LanguageButtonText(PhoneHelpLanguage language)
        {
            switch (language)
            {
                case PhoneHelpLanguage.Chinese:
                    return "中文";
                case PhoneHelpLanguage.English:
                    return "English";
                default:
                    return "日语";
            }
        }
    }
}
