using RNGReporter.Objects;
using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace RNGReporter
{
    public partial class SearchElm : Form
    {
        private readonly List<Adjacent> _adjacents;

        public SearchElm()
        {
            ReturnElm = "";
            RoamerText = "";
            InitializeComponent();
            ApplyLocalizedPhoneText();
            labelResults.Visible = false;
        }

        public SearchElm(List<Adjacent> adjacents)
        {
            ReturnElm = "";
            RoamerText = "";
            _adjacents = adjacents;
            InitializeComponent();
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

        private void ApplyLocalizedPhoneText()
        {
            labelKElm.Text = ElmCallText.ElmK;
            labelEElm.Text = ElmCallText.ElmE;
            labelPElm.Text = ElmCallText.ElmP;
            labelKIrwin.Text = ElmCallText.IrwinK;
            labelEIrwin.Text = ElmCallText.IrwinE;
            labelPIrwin.Text = ElmCallText.IrwinP;

            const int helpHeight = 62;
            labelKElm.Top = labelKIrwin.Top = 139;
            labelEElm.Top = labelEIrwin.Top = 205;
            labelPElm.Top = labelPIrwin.Top = 271;
            labelKElm.Height = labelEElm.Height = labelPElm.Height = helpHeight;
            labelKIrwin.Height = labelEIrwin.Height = labelPIrwin.Height = helpHeight;
            groupBox1.Height = 338;
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

    internal static class ElmCallText
    {
        public const string ElmK =
            "K - 中：关都地区应该还有我不知道的宝可梦。也许还有我不熟悉的进化方式，我应该换个角度继续调查！\r\n" +
            "    日：カントー地方には、まだ私の知らないポケモンがいるはずだ。進化にも、まだ知らない方法があるかもしれないね。\r\n" +
            "    英：I expect there are some Pokémon in the Kanto region that I don't know. There are probably methods of evolution that I'm not familiar with yet.";

        public const string ElmE =
            "E - 中：宝可梦的进化方式真是多种多样，不是吗？！有些宝可梦甚至要先满足特定条件才会进化！\r\n" +
            "    日：ポケモンの進化には本当にいろいろな方法があるんだよ！なかには、ある条件を満たさないと進化しないポケモンもいるんだ！\r\n" +
            "    英：There are so many different ways that Pokémon evolve, aren't there?! Some Pokémon don't even evolve until they meet certain conditions first!";

        public const string ElmP =
            "P - 中：感染过宝可病毒的宝可梦似乎升级时成长得更好。我们还不太清楚原因……\r\n" +
            "    日：ポケルスに感染したポケモンは、レベルアップしたときの成長がよくなるようだね。理由はまだよく分かっていないんだ……\r\n" +
            "    英：It seems that Pokémon that have been infected with Pokérus level up better. We're not quite sure why...";

        public const string IrwinK =
            "K - 中：你打电话来我真高兴！我正好也想打给你！看来我们很合得来！\r\n" +
            "    日：電話してくれてうれしいよ！ぼくもちょうど電話しようとしてたんだ！ぼくたち相性ばっちりだね！\r\n" +
            "    英：I'm so glad you called! I was just about to call you, too! I guess we must be a good match!";

        public const string IrwinE =
            "E - 中：听说你的冒险事迹真让我热血沸腾！确实如此！\r\n" +
            "    日：きみの冒険の話を聞くと、本当に元気が出るよ！ほんとだよ！\r\n" +
            "    英：Hearing about your escapades really inspires me! It sure does!";

        public const string IrwinP =
            "P - 中：你好吗？在做什么？在哪里？现在有几枚徽章了？存了多少钱？妈妈好吗？抓了很多宝可梦吗？明天天气会晴吗？啊啊，想聊的太多了！这样根本聊不完！\r\n" +
            "    日：元気？何してる？どこにいる？バッジはいくつ？お金はどれくらいたまった？お母さんは元気？ポケモンはたくさんいる？明日は晴れるかな？ああ、話したいことが多すぎる！\r\n" +
            "    英：How are you? What are you doing? Where are you? How many Badges do you have now? How much money have you saved? How's your mom? Have you got lots of Pokémon? Is it going to be sunny tomorrow?";
    }
}
