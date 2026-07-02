using System;
using System.Windows.Forms;

namespace RNGReporter
{
    public partial class SearchElmV : Form
    {
        private readonly string[] returnArray = new string[10];
        private GlassButton buttonLanguage;
        private PhoneHelpLanguage phoneHelpLanguage = PhoneHelpLanguage.Japanese;

        public SearchElmV()
        {
            InitializeComponent();
            InitializeLanguageButton();
            ApplyLocalizedPhoneText();
        }

        public string[] ReturnArray
        {
            get { return returnArray; }
        }

        private void buttonPos1K_Click(object sender, EventArgs e)
        {
            labelPos1.Text = ((Button)sender).Text;
        }

        private void buttonPos1E_Click(object sender, EventArgs e)
        {
            labelPos1.Text = ((Button)sender).Text;
        }

        private void buttonPos1P_Click(object sender, EventArgs e)
        {
            labelPos1.Text = ((Button)sender).Text;
        }

        private void buttonPos2K_Click(object sender, EventArgs e)
        {
            labelPos2.Text = ((Button)sender).Text;
        }

        private void buttonPos2E_Click(object sender, EventArgs e)
        {
            labelPos2.Text = ((Button)sender).Text;
        }

        private void buttonPos2P_Click(object sender, EventArgs e)
        {
            labelPos2.Text = ((Button)sender).Text;
        }

        private void buttonPos3K_Click(object sender, EventArgs e)
        {
            labelPos3.Text = ((Button)sender).Text;
        }

        private void buttonPos3E_Click(object sender, EventArgs e)
        {
            labelPos3.Text = ((Button)sender).Text;
        }

        private void buttonPos3P_Click(object sender, EventArgs e)
        {
            labelPos3.Text = ((Button)sender).Text;
        }

        private void buttonPos4K_Click(object sender, EventArgs e)
        {
            labelPos4.Text = ((Button)sender).Text;
        }

        private void buttonPos4E_Click(object sender, EventArgs e)
        {
            labelPos4.Text = ((Button)sender).Text;
        }

        private void buttonPos4P_Click(object sender, EventArgs e)
        {
            labelPos4.Text = ((Button)sender).Text;
        }

        private void buttonPos5K_Click(object sender, EventArgs e)
        {
            labelPos5.Text = ((Button)sender).Text;
        }

        private void buttonPos5E_Click(object sender, EventArgs e)
        {
            labelPos5.Text = ((Button)sender).Text;
        }

        private void buttonPos5P_Click(object sender, EventArgs e)
        {
            labelPos5.Text = ((Button)sender).Text;
        }

        private void buttonPos6K_Click(object sender, EventArgs e)
        {
            labelPos6.Text = ((Button)sender).Text;
        }

        private void buttonPos6E_Click(object sender, EventArgs e)
        {
            labelPos6.Text = ((Button)sender).Text;
        }

        private void buttonPos6P_Click(object sender, EventArgs e)
        {
            labelPos6.Text = ((Button)sender).Text;
        }

        private void buttonPos7K_Click(object sender, EventArgs e)
        {
            labelPos7.Text = ((Button)sender).Text;
        }

        private void buttonPos7E_Click(object sender, EventArgs e)
        {
            labelPos7.Text = ((Button)sender).Text;
        }

        private void buttonPos7P_Click(object sender, EventArgs e)
        {
            labelPos7.Text = ((Button)sender).Text;
        }

        private void buttonPos8K_Click(object sender, EventArgs e)
        {
            labelPos8.Text = ((Button)sender).Text;
        }

        private void buttonPos8E_Click(object sender, EventArgs e)
        {
            labelPos8.Text = ((Button)sender).Text;
        }

        private void buttonPos8P_Click(object sender, EventArgs e)
        {
            labelPos8.Text = ((Button)sender).Text;
        }

        private void buttonPos9K_Click(object sender, EventArgs e)
        {
            labelPos9.Text = ((Button)sender).Text;
        }

        private void buttonPos9E_Click(object sender, EventArgs e)
        {
            labelPos9.Text = ((Button)sender).Text;
        }

        private void buttonPos9P_Click(object sender, EventArgs e)
        {
            labelPos9.Text = ((Button)sender).Text;
        }

        private void buttonPos10K_Click(object sender, EventArgs e)
        {
            labelPos10.Text = ((Button)sender).Text;
        }

        private void buttonPos10E_Click(object sender, EventArgs e)
        {
            labelPos10.Text = ((Button)sender).Text;
        }

        private void buttonPos10P_Click(object sender, EventArgs e)
        {
            labelPos10.Text = ((Button)sender).Text;
        }

        private void buttonOk_Click(object sender, EventArgs e)
        {
            returnArray[0] = labelPos1.Text;
            returnArray[1] = labelPos2.Text;
            returnArray[2] = labelPos3.Text;
            returnArray[3] = labelPos4.Text;
            returnArray[4] = labelPos5.Text;
            returnArray[5] = labelPos6.Text;
            returnArray[6] = labelPos7.Text;
            returnArray[7] = labelPos8.Text;
            returnArray[8] = labelPos9.Text;
            returnArray[9] = labelPos10.Text;
        }

        private void InitializeLanguageButton()
        {
            buttonLanguage = new GlassButton
            {
                Anchor = AnchorStyles.Top | AnchorStyles.Right,
                BackColor = System.Drawing.Color.AntiqueWhite,
                ForeColor = System.Drawing.Color.Black,
                Location = new System.Drawing.Point(441, 94),
                Name = "buttonLanguage",
                OuterBorderColor = System.Drawing.Color.Transparent,
                ShineColor = System.Drawing.SystemColors.Window,
                Size = new System.Drawing.Size(75, 21),
                TabIndex = 73
            };
            buttonLanguage.Click += buttonLanguage_Click;
            Controls.Add(buttonLanguage);
        }

        private void buttonLanguage_Click(object sender, EventArgs e)
        {
            phoneHelpLanguage = ElmCallText.NextLanguage(phoneHelpLanguage);
            ApplyLocalizedPhoneText();
        }

        private void ApplyLocalizedPhoneText()
        {
            label8.Text = ElmCallText.ElmK(phoneHelpLanguage);
            label9.Text = ElmCallText.ElmE(phoneHelpLanguage);
            label10.Text = ElmCallText.ElmP(phoneHelpLanguage);
            buttonLanguage.Text = ElmCallText.LanguageButtonText(phoneHelpLanguage);

            int kHeight = phoneHelpLanguage == PhoneHelpLanguage.Japanese ? 72 : 52;
            int eHeight = 52;
            int pHeight = phoneHelpLanguage == PhoneHelpLanguage.Japanese ? 64 : 52;
            label8.Top = 123;
            label8.Height = kHeight;
            label9.Top = label8.Bottom + 4;
            label9.Height = eHeight;
            label10.Top = label9.Bottom + 4;
            label10.Height = pHeight;
            buttonOk.Top = label10.Bottom + 10;
            buttonCancel.Top = buttonOk.Top;
            ClientSize = new System.Drawing.Size(ClientSize.Width, buttonOk.Bottom + 11);
        }
    }
}
