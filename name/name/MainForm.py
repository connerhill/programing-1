import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("French Script MT", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Aquamarine
        self._label1.Location = System.Drawing.Point(36, 352)
        self._label1.Name = "label1"
        self._label1.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label1.Size = System.Drawing.Size(150, 69)
        self._label1.TabIndex = 0
        self._label1.Text = "show"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("French Script MT", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Aquamarine
        self._label2.Location = System.Drawing.Point(410, 352)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(151, 69)
        self._label2.TabIndex = 1
        self._label2.Text = "clear"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label2.Click += self.Label2Click
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("French Script MT", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Aquamarine
        self._label3.Location = System.Drawing.Point(738, 352)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(157, 69)
        self._label3.TabIndex = 2
        self._label3.Text = "exit"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label3.Click += self.Label3Click
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("French Script MT", 72, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Aquamarine
        self._label4.Location = System.Drawing.Point(92, 41)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(780, 250)
        self._label4.TabIndex = 3
        self._label4.Text = " "
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label4.Click += self.Label4Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(1162, 440)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.ForeColor = System.Drawing.Color.White
        self.Name = "MainForm"
        self.Text = "name"
        self.ResumeLayout(False)


    def Label1Click(self, sender, e):
        self._label1.Text = "conner hill"

    def Label2Click(self, sender, e):
        self._label.Text = ""

    def Label3Click(self, sender, e):
        application.exit()