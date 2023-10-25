import sys
#from Components.welcome import WelcomePage
#from Components.welcome import WelcomePage
from Components.Main_Tab import MainTabPage
from PyQt6.QtCore import Qt,QRect,QTimer
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel,QLineEdit,QMessageBox, QPushButton,QSizePolicy, QTextEdit,QVBoxLayout,QGridLayout, QWidget, QGroupBox,QHBoxLayout,QMainWindow,QComboBox,QRadioButton
#from Calculation.abs_path import absolute_path
#from Variables.var import Variables 
from Variables import var
# from DataBase.models import User
# from DataBase.DB_config import DB_config_class
# from Controller.auth import auth_user
from Controller.project_controller import ProjectController,create_new_project,Get_all_existing_projects,get_current_project_details


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
        self.cmbbox_project_selection.currentIndexChanged.connect(self.cmbbox_proj_changed)
        self.lbl_project_id=QLabel("WorkOrder No.")
        self.tb_project_id=QLineEdit("XXX-XXXX-XXX")
        self.lbl_project_desc=QLabel("Project Description")
        self.tb_project_name=QLineEdit("XXXXXXX")
        #self.lbl_customer_detail=QLabel("Customer Detail")
        #self.tb_customer_detail=QLineEdit("XXXXXXX")
        self.lbl_project_Note=QLabel("Notes")
        self.tb_project_Note=QTextEdit("XXXXXXX")
        #self.tb_project_Note.setFixedHeight(50)
        
        #Add/Update/ Next Button
        #self.btn_Create_Project=QPushButton("Create New Project")
        #self.btn_Create_Project.clicked.connect(self.Create_New_Project)
        #self.btn_Update_Project=QPushButton("Update Project Details")
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
        self.grid_layout.addWidget(self.tb_project_name,2,1)
        #self.grid_layout.addWidget(self.lbl_customer_detail,3,0)
        #self.grid_layout.addWidget(self.tb_customer_detail,3,1)
        self.grid_layout.addWidget(self.lbl_project_Note,4,0)
        self.grid_layout.addWidget(self.tb_project_Note,4,1)
        #self.grid_layout.addWidget(self.btn_Create_Project,5,0)
        #self.grid_layout.addWidget(self.btn_Update_Project,5,1)
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
        
        existing_projects_list=Get_all_existing_projects()
        print(existing_projects_list)
        
        return existing_projects_list#["AA","BB","CC"] 
    
    
    #Based On Radio Button Selection Update Form UI
    def update_UI(self):        
        #Select Existing Project RadiButton Checked
        if self.rb1_existing_project.isChecked():
            self.cmbbox_project_selection.setVisible(True)
            self.lbl_select_existing_project.setVisible(True)            
            #self.tb_customer_detail.setEnabled(False)
            self.tb_project_id.setEnabled(False)
            self.tb_project_name.setEnabled(False)
            self.tb_project_Note.setEnabled(False)
            self.tb_project_Note.clear()
            #self.btn_Create_Project.setVisible(False)
        
        #Select New Project RadiButton Checked    
        if self.rb2_new_project.isChecked():
            self.cmbbox_project_selection.setVisible(False)
            self.lbl_select_existing_project.setVisible(False)            
            #self.tb_customer_detail.setEnabled(True)
            self.tb_project_id.setEnabled(True)
            self.tb_project_name.setEnabled(True)
            self.tb_project_Note.setEnabled(True)
            #self.btn_Create_Project.setVisible(True)
    
    def Set_Project(self):
        if self.rb2_new_project.isChecked():        
            project_id=self.tb_project_id.text()#self.generate_project_id()        
            #project_name=self.tb_project_name.text()
        elif self.rb1_existing_project.isChecked():
            project_id=self.cmbbox_project_selection.currentText()
            
        project_name=self.tb_project_name.text()
        project_note=self.tb_project_Note.toPlainText()
            
            
        var.project_id=project_id 
        var.project_name=project_name       
        user=var.uname
        
        #Check if Project exists DO nothing
        if(self.rb2_new_project.isChecked() and get_current_project_details(project_id=project_id)):
            Show_MessageBox(self,"Project with Given WorkOrder Already Exists")
        
        elif(project_id):        
            create_new_project(proj_id=var.project_id,proj_name=project_name,project_note=project_note,user=user)        
            _ProjectController=ProjectController(project_id=var.project_id)
            _ProjectController.create_project_output_tables() #If New Project Creation is succesfull
            return True
        else:
            Show_MessageBox(self,"Pls Check Work Order")
            #self.close() 

        
    # def generate_project_id(self):
        
    #     project_id=str.lower("ENQ-23-09-01-00")
        
    #     return project_id
                
    def Show_MainTabPage(self):
       #WIll create New Project If Diesnt exists and also creates Projects output Estimation/Surface Table for the project,
       # If ALready exists then it does nothing        
        result = self.Set_Project()
        if result:
            self.main_tab_page=MainTabPage()
            self.main_tab_page.show()
            self.hide()#Hide Project Selection Page
    
    def cmbbox_proj_changed(self):
        current_project=self.cmbbox_project_selection.currentText()
        if(current_project):
            project_detail=get_current_project_details(current_project)
            self.tb_project_id.setText(current_project)
            self.tb_project_name.setText(project_detail.project_name)
            #self.tb_customer_detail.setText("NTPC")
            self.tb_project_Note.setText(project_detail.project_note)
    
def Show_MessageBox(sender,msg:str):
    message_box = QMessageBox(sender)
    message_box.setIcon(QMessageBox.Icon.Information)
    message_box.setText(msg)
    message_box.setWindowTitle("Information")
    message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    message_box.exec()                
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     #app.setStyle("Fusion")
#     project_page = Project_Selection()
#     project_page.show()
#     sys.exit(app.exec())

      
        

    
        