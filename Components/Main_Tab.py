import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QWidget, \
    QTabWidget,QGroupBox,QHBoxLayout
    
from PyQt6.QtCore import Qt    
from Variables import var

#from Components.Insert_plt_Misc import Shell
from Components.Base_Comp_Ring import Tab_Base_Comp_Ring
#from Components.Shell import Tab2_Shell
#from Components.DishEnd import Tab1_DEnd
from Components.DishEnd import Tab_DEnd
from Components.BOM import Tab4_BOM
from Components.Shell import Tab_Shell
from Components.Misc import Tab_Misc
from Components.Skirt import Tab_Skirt
from Components.Saddles import Tab_Saddles
from Components.Fire_inslulation import Tab_Fire_Insl
from Components.WireMesh_Demister import Tab_WireMesh_Demister
from Components.BB_TSR import Tab_BB_TSR
from Components.Nozzle import Tab_Nozzle



class MainTabPage(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Welcome")
        self.setGeometry(0, 0,950,800)
        self.setFixedHeight(800)

        # Create tab widget
        tab_widget = QTabWidget()

        # Create tabs
        DishEnd_tab = Tab_DEnd()
        Shell_tab=Tab_Shell()
        Misc=Tab_Misc()
        Skirt_tab=Tab_Skirt()
        Base_comp_ring_tab=Tab_Base_Comp_Ring()
        Saddles=Tab_Saddles()
        Fire_Insl=Tab_Fire_Insl()
        WireMesh_Demister=Tab_WireMesh_Demister()
        BB_TSR=Tab_BB_TSR()
        Nozzle=Tab_Nozzle()
        
        BOM_tab = Tab4_BOM()
        

        

        # Add tabs to the tab widget
        tab_widget.addTab(DishEnd_tab, "Dish End")
        tab_widget.addTab(Shell_tab, "Shell")        
        tab_widget.addTab(Skirt_tab, "Skirt")
        tab_widget.addTab(Base_comp_ring_tab, "Base Comp. Ring DEnd_Nozzle")
        tab_widget.addTab(Saddles, "Saddle")
        tab_widget.addTab(Fire_Insl, "Fire Insul.")
        tab_widget.addTab(WireMesh_Demister, "WireMesh Demister")
        tab_widget.addTab(BB_TSR, "BB TSR")
        tab_widget.addTab(Nozzle, "Nozzle")
        
        tab_widget.addTab(Misc, "Misc.")
        tab_widget.addTab(BOM_tab, "BOM")

        
        #Display Current Project ID/WorkOrder on top of Tab        
        lbl_ProjectID_or_WO=QLabel(f"Project ID (WO): {var.project_id}  {var.project_name}")
        lbl_ProjectID_or_WO.setStyleSheet('background-color:lightgreen;font:bold')
        

        # Create main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(lbl_ProjectID_or_WO,0,Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(tab_widget)

        # Set the main layout
        self.setLayout(main_layout)
        self.setStyleSheet(tab_style)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     # Create and show the welcome page
#     main_tab_page = MainTabPage()
#     main_tab_page.show()
#     #welcome_page.setStyleSheet('background-color:lightgrey')

#     sys.exit(app.exec())

tab_style="""
QTabWidget::pane { /* The tab widget frame */
    border-top: 2px solid #C2C7CB;
}

QTabWidget::tab-bar {
    left: 5px; /* move to the right by 5px */
}

/* Style the tab using the tab sub-control. Note that
    it reads QTabBar _not_ QTabWidget */
QTabBar::tab {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
    border: 2px solid #C4C4C3;
    border-bottom-color: #C2C7CB; /* same as the pane color */
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    min-width: 8ex;
    padding: 2px;
}

QTabBar::tab:selected, QTabBar::tab:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
}

QTabBar::tab:selected {
    border-color: #9B9B9B;
    border-bottom-color: #C2C7CB; /* same as pane color */
}

QTabBar::tab:!selected {
    margin-top: 2px; /* make non-selected tabs look smaller */
}

/* make use of negative margins for overlapping tabs */
QTabBar::tab:selected {
    /* expand/overlap to the left and right by 4px */
    margin-left: -4px;
    margin-right: -4px;
}

QTabBar::tab:first:selected {
    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */
}

QTabBar::tab:last:selected {
    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */
}

QTabBar::tab:only-one {
    margin: 0; /* if there is only one tab, we don't want overlapping margins */
}
"""