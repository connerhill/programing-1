import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self.SuspendLayout()
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Fuchsia
        self.ClientSize = System.Drawing.Size(605, 459)
        self.Name = "MainForm"
        self.Text = "Lang54c"
        self.ResumeLayout(False)

