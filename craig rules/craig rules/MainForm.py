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
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Monotype Corsiva", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Aquamarine
        self._button1.Location = System.Drawing.Point(36, 338)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(151, 70)
        self._button1.TabIndex = 4
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Monotype Corsiva", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Aquamarine
        self._button2.Location = System.Drawing.Point(386, 338)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(136, 70)
        self._button2.TabIndex = 5
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Monotype Corsiva", 36, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Aquamarine
        self._button3.Location = System.Drawing.Point(780, 338)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(136, 69)
        self._button3.TabIndex = 6
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.ForeColor = System.Drawing.Color.Aquamarine
        self._label1.Location = System.Drawing.Point(57, 32)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(847, 244)
        self._label1.TabIndex = 7
        self._label1.Text = " "
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(976, 420)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "craig rules"
        self.ResumeLayout(False)

    def Button1Click(self, sender, e):
        show._label1.Text = "craig rules"

    def Button2Click(self, sender, e):
        self._label1.Text = " "

    def Button3Click(self, sender, e):
        application.exit()