import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("French Script MT", 72, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Aquamarine
        self._label4.Location = System.Drawing.Point(92, 41)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(780, 250)
        self._label4.TabIndex = 3
        self._label4.Text = "   "
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Mistral", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Aquamarine
        self._button1.Location = System.Drawing.Point(40, 352)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(142, 69)
        self._button1.TabIndex = 4
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Mistral", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Aquamarine
        self._button2.Location = System.Drawing.Point(420, 352)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(138, 69)
        self._button2.TabIndex = 5
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Mistral", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Aquamarine
        self._button3.Location = System.Drawing.Point(796, 352)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(118, 69)
        self._button3.TabIndex = 6
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(1162, 440)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.ForeColor = System.Drawing.Color.White
        self.Name = "MainForm"
        self.Text = "name"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label4.Text="conner hill"

    def Button2Click(self, sender, e):
        self._label4.Text=""

    def Button3Click(self, sender, e):
        Application.Exit()