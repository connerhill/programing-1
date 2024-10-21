import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.Fuchsia
        self._listBox1.Font = System.Drawing.Font("Microsoft Himalaya", 24, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.ForeColor = System.Drawing.Color.Aquamarine
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 32
        self._listBox1.Location = System.Drawing.Point(13, 13)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(400, 324)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Fuchsia
        self._button1.Font = System.Drawing.Font("Microsoft Himalaya", 26.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Aquamarine
        self._button1.Location = System.Drawing.Point(13, 384)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(129, 62)
        self._button1.TabIndex = 1
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Fuchsia
        self._button2.Font = System.Drawing.Font("Microsoft Himalaya", 26.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Aquamarine
        self._button2.Location = System.Drawing.Point(149, 384)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(129, 62)
        self._button2.TabIndex = 2
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Fuchsia
        self._button3.Font = System.Drawing.Font("Microsoft Himalaya", 26.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Aquamarine
        self._button3.Location = System.Drawing.Point(284, 384)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(129, 62)
        self._button3.TabIndex = 3
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(425, 458)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog162b"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e): # Calc
        heading = "Year\t\tPopulation (in mil.)"
        self._listBox1.Items.Add(heading)
        pop = 243
        for year in range(1990, 2016):
            line = str(year) + "\t\t" + str(int(pop))
            self._listBox1.Item.Add(line)
            pop*= 1.029 # pop = pop * 1.029

    def Button2Click(self, sender, e): # Clear
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e): # Exit
        Application.Exit()