import sys
#from Components.welcome import WelcomePage
#from Components.welcome import WelcomePage
from Components.Main_Tab import MainTabPage
from PyQt6.QtCore import Qt,QRect,QTimer
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel,QLineEdit, QPushButton,QSizePolicy, QTextEdit,QVBoxLayout,QGridLayout, QWidget, QGroupBox,QHBoxLayout,QMainWindow,QComboBox,QRadioButton
#from Calculation.abs_path import absolute_path
#from Variables.var import Variables 
from Variables import var
# from DataBase.models import User
# from DataBase.DB_config import DB_config_class
# from Controller.auth import auth_user
from Controller.project_controller import create_new_project,create_project_output_tables,ProjectController


class Project_Selection(QWidget): #QMainWIndow
    def __init__(self):
        super().__init__()
       
        self.InitializeUI()
     

    def InitializeUI(self):

        # Set window title and size
        self.setWindowTitle("Project")
        self.setGeometry(300, 200, 400, 300)
        
        #Old or New Project
        self.lbl_new_old_project=QLabel("Project:")
        self.rb1_existing_project=QRadioButton("Existing")       
        #self.rb1_existing_project.setFixedWidth(100)
        self.rb2_new_project=QRadioButton("New")
        #self.rb2_new_project.setFixedWidth(50)
        self.rb1_existing_project.clicked.connect(self.update_UI)
        self.rb2_new_project.clicked.connect(self.update_UI)      

        
        
        
        self.hbox_layout=QHBoxLayout()
        self.hbox_layout.addWidget(self.lbl_new_old_project)
        self.hbox_layout.addWidget(self.rb1_existing_project)
        self.hbox_layout.addWidget(self.rb2_new_project)
        self.Hbox_parent_widget=QWidget() #This is added to just control the width of hbox_layout as we cant control size of a layout so we added this layout to a widget and we can control size of a widget
        self.Hbox_parent_widget.setLayout(self.hbox_layout)       
        self.Hbox_parent_widget.setFixedSize(200,40)
        self.Hbox_parent_widget.setStyleSheet('background-color:lightgreen')
        
        
        
        #For Project Detail
        self.lbl_select_existing_project=QLabel("Select Project")
        self.cmbbox_project_selection=QComboBox()
        self.existing_project_list=self.get_existing_projects_list()
        self.cmbbox_project_selection.addItems(self.existing_project_list)
        self.lbl_project_id=QLabel("Project ID")
        self.tb_project_id=QLineEdit("XXX-XXXX-XXX")
        self.lbl_project_desc=QLabel("Project Description")
        self.tb_project_desc=QLineEdit("XXXXXXX")
        self.lbl_customer_detail=QLabel("Customer Detail")
        self.tb_customer_detail=QLineEdit("XXXXXXX")
        self.lbl_project_Note=QLabel("Notes")
        self.tb_project_Note=QTextEdit("XXXXXXX")
        #self.tb_project_Note.setFixedHeight(50)
        
        #Add/Update/ Next Button
        self.btn_Create_Project=QPushButton("Create New Project")
        self.btn_Create_Project.clicked.connect(self.Create_New_Project)
        self.btn_Update_Project=QPushButton("Update Project Details")
        self.btn_Next=QPushButton("Next")
        self.btn_Next.setStyleSheet('background-color:lightgreen')
        self.btn_Next.clicked.connect(self.Show_MainTabPage)
       
        
        
        self.Grpbox_project_detail=QGroupBox("Project Detail")     
        self.grid_layout = QGridLayout()
        self.Grpbox_project_detail.setLayout(self.grid_layout)
        self.grid_layout.addWidget(self.lbl_select_existing_project,0,0)
        self.grid_layout.addWidget(self.cmbbox_project_selection,0,1)
        self.grid_layout.addWidget(self.lbl_project_id,1,0)
        self.grid_layout.addWidget(self.tb_project_id,1,1)
        self.grid_layout.addWidget(self.lbl_project_desc,2,0)
        self.grid_layout.addWidget(self.tb_project_desc,2,1)
        self.grid_layout.addWidget(self.lbl_customer_detail,3,0)
        self.grid_layout.addWidget(self.tb_customer_detail,3,1)
        self.grid_layout.addWidget(self.lbl_project_Note,4,0)
        self.grid_layout.addWidget(self.tb_project_Note,4,1)
        self.grid_layout.addWidget(self.btn_Create_Project,5,0)
        self.grid_layout.addWidget(self.btn_Update_Project,5,1)
        self.grid_layout.addWidget(self.btn_Next,5,3)
        
        self.V_mainlayout = QVBoxLayout()
        #self.V_mainlayout.addLayout(self.hbox_layout)
        self.V_mainlayout.addWidget(self.Hbox_parent_widget,alignment=Qt.AlignmentFlag.AlignHCenter,stretch=0)
        self.V_mainlayout.addWidget(self.Grpbox_project_detail)
        self.setLayout(self.V_mainlayout)
        
        self.rb1_existing_project.setChecked(True)
        self.rb1_existing_project.click()#This will Trigger the Update UI on form load
        #self.update_UI()
        
    def get_existing_projects_list(self):
        return ["AA","BB","CC"] 
    
    def update_UI(self):
        if self.rb1_existing_project.isChecked():
            self.cmbbox_project_selection.setVisible(True)
            self.lbl_select_existing_project.setVisible(True)            
            self.tb_customer_detail.setEnabled(False)
            self.tb_project_id.setEnabled(False)
            self.tb_project_desc.setEnabled(False)
            self.tb_project_Note.setEnabled(False)
            self.tb_project_Note.clear()
            self.btn_Create_Project.setVisible(False)
            
        if self.rb2_new_project.isChecked():
            self.cmbbox_project_selection.setVisible(False)
            self.lbl_select_existing_project.setVisible(False)            
            self.tb_customer_detail.setEnabled(True)
            self.tb_project_id.setEnabled(True)
            self.tb_project_desc.setEnabled(True)
            self.tb_project_Note.setEnabled(True)
            self.btn_Create_Project.setVisible(True)
    
    def Create_New_Project(self):
        project_id=self.generate_project_id()        
        project_name=self.tb_project_desc.text()
        user=var.uname
        
        create_new_project(proj_id=project_id,proj_name=project_name,user=user)
        #Save Current_projectid in vars
        var.project_id=project_id
        _ProjectController=ProjectController()
        _ProjectController.create_project_output_tables(project_id=var.project_id) #If New Project Creation is succesfull
       
        
       
        
    def generate_project_id(self):
        
        project_id="ENQ-23-09-01-00"
        
        return project_id
                
    def Show_MainTabPage(self):
        self.main_tab_page=MainTabPage()
        self.main_tab_page.show()
        self.hide()#Hide Project Selection Page
                 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle("Fusion")
    project_page = Project_Selection()
    project_page.show()
    sys.exit(app.exec())

      
        

    
        