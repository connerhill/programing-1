import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Black
        self._button1.Font = System.Drawing.Font("Gigi", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Aquamarine
        self._button1.Location = System.Drawing.Point(12, 357)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(226, 71)
        self._button1.TabIndex = 0
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Black
        self._button2.Font = System.Drawing.Font("Gigi", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Aquamarine
        self._button2.Location = System.Drawing.Point(376, 357)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(226, 71)
        self._button2.TabIndex = 1
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Black
        self._button3.Font = System.Drawing.Font("Gigi", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Aquamarine
        self._button3.Location = System.Drawing.Point(727, 357)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(226, 71)
        self._button3.TabIndex = 2
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Gigi", 27.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Aquamarine
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(339, 110)
        self._label1.TabIndex = 3
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Gigi", 27.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Aquamarine
        self._label2.Location = System.Drawing.Point(363, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(339, 110)
        self._label2.TabIndex = 4
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Gigi", 27.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Aquamarine
        self._label3.Location = System.Drawing.Point(12, 119)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(339, 110)
        self._label3.TabIndex = 5
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Gigi", 27.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.Aquamarine
        self._label4.Location = System.Drawing.Point(363, 110)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(339, 110)
        self._label4.TabIndex = 6
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(965, 440)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "about me"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "i like reading"
        self._label2.Text = "i like snakes"
        self._label3.Text = "i like programing"
        self._label4.Text = "i like sleep"

    def Button2Click(self, sender, e):
        self._label1.Text = " "
        self._label2.Text = " "
        self._label3.Text = " "
        self._label4.Text = " "

    def Button3Click(self, sender, e):
        Application.Exit()