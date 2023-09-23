import sys
#from Components.welcome import WelcomePage
from Components.Main_Tab import MainTabPage
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout,QMainWindow
from Calculation.abs_path import absolute_path
#from Variables.var import Variables 
from Variables import var
from DataBase.common_models import User
from DataBase.DB_config import DB_config_class
from Controller.auth_controller import auth_user
#from Controller.project_controller import create_project_op_tables
from Components.project_selection import Project_Selection




class LoginPage(QWidget): #QMainWIndow
    def __init__(self):
        super().__init__()
       
        self.InitializeUI()
     

    def InitializeUI(self):

        # Set window title and size
        self.setWindowTitle("Login")
        self.setGeometry(300, 200, 400, 300)

        # Load organization image
        logo_path = absolute_path("Resources/Images/logo.jpg")
        pv_img_path =absolute_path("Resources/Images/PV1.jpg")
        organization_image = QPixmap(logo_path)
        organization_img_label = QLabel(self)
        organization_img_label.setPixmap(organization_image)
        #organization_label.setScaledContents(True)
        organization_img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        pv_img = QPixmap(pv_img_path)
        pv_img=pv_img.scaled(150, 300)
        pv_img_view_label=QLabel(self)
        pv_img_view_label.setPixmap(pv_img)
        pv_img_view_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
       
        




        label_description = QLabel("Engineering Material Estimation For Pressure Vessels", self)
        # label_description.move(1000,1000)
        # label_description.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create login widgets
        username_label = QLabel("Username:")
        self.username_field = QLineEdit()
        self.username_field.setPlaceholderText("Enter your Staff No. as Username")
        self.username_field.setText(var.uname)
        password_label = QLabel("Password:")
        self.password_field = QLineEdit()
        self.password_field.setText(var.pwd)
        self.password_field.setEchoMode(QLineEdit.EchoMode.Password)
        login_button = QPushButton("Login")

        # Create V_mainlayout and add widgets
        self.V_mainlayout = QVBoxLayout()

        self.V_mainlayout.addWidget(organization_img_label)
        self.V_mainlayout.addWidget(label_description)
        

        H_layout1 = QHBoxLayout()
        H_layout1.addWidget(username_label)
        H_layout1.addWidget(self.username_field)

        H_layout2 = QHBoxLayout()
        H_layout2.addWidget(password_label)
        H_layout2.addWidget(self.password_field)

        # V_mainlayout.addWidget(username_label)
        # V_mainlayout.addWidget(self.username_field)
        # V_mainlayout.addWidget(password_label)
        # V_mainlayout.addWidget(self.password_field)

        self.V_mainlayout.addLayout(H_layout1)
        self.V_mainlayout.addLayout(H_layout2)

        self.V_mainlayout.addWidget(login_button)
        
        self.error_label = QLabel("")#To display error message
        self.V_mainlayout.addWidget(self.error_label)
        self.error_label.setHidden(True)#Default error label is hidden ,not visible



        H_mainlayout = QHBoxLayout()
        H_mainlayout.addLayout(self.V_mainlayout)
        H_mainlayout.addWidget(pv_img_view_label)

        '''Can use below two Methods'''

        '''IF Login Page inherits Qwidget Class then we can directly set self.setlayout and pass H_mainlayout'''
        # Set the H_mainlayout
        #self.setLayout(H_mainlayout)

        '''If Login page inherits QMainwindow class then we can display our layout in cental widget of QmainWIndow
        but setcentral widget only accepts widget/widgets as parameter not the layout so we make a dummy Qwidget and sets its layout
        with H_mainlayout & then pass this dummy widget to setCentral widgetClass of QMainwindow
        '''
        #QWidget_ = QWidget()
        #QWidget_.setLayout(H_mainlayout)
        #self.setCentralWidget(QWidget_)
        self.setLayout(H_mainlayout)

        # Connect login button to the login function
        login_button.clicked.connect(self.login)

    def login(self):
        # Get the entered username and password
        username = self.username_field.text()
        password = self.password_field.text()
        var.uname, var.pwd = username, password



        # Perform login verification (replace with your own logic)
        try:
            
           # session=DB_config_class.session
            #user=session.query(User).filter_by(staffNo=username).first()
            
            user=auth_user(username)
            if (user):
            #print(user.staffNo,user.pwd)
                if user.pwd==password:
                    #project=create_new_project()
                    #print(row)
                    # Successful login, navigate to the welcome page
                    self.hide()  # Hide the login page
                    self.project_Selection=Project_Selection()
                    self.project_Selection.show()
                    # self.welcomePage = WelcomePage()
                    # self.welcomePage.show()
                    
                    
                else:
                    self.error_label.setText("Password is wrong")
                    self.error_label.setHidden(False)
                        
            else:
                self.error_label.setText("User Doesn't Exist")
                self.error_label.setHidden(False)
               
        except Exception as e:
           
            #error_label = QLabel("Invalid username or password!")
            self.error_label.setText("EXception,Check Network connectivity")
            self.error_label.setHidden(False)
            raise e
        
        # else:
        #     # Failed login, display an error message (replace with your own error handling)
        #     self.error_label.setText("TRy Else-Password is wrong")
        #     self.error_label.setHidden(False)
           
        
        
     

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
   

#     # Create and show the login page
#     login_page = LoginPage()
#     login_page.show()

#     sys.exit(app.exec())
