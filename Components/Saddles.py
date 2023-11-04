
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QLayout, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout,QWidget, \
    QTabWidget,QGroupBox,QTableWidget,QTableWidgetItem,QGridLayout,QScrollArea,QSpacerItem
from Variables import var
from PyQt6.QtCore import Qt,QRect
import math
from Controller.project_controller import ProjectController,Get_Shell_ODs_from_Saddle_Data,Get_Saddle_Data,Get_Saddle_Dim_Data,Get_Vessel_Data

class Tab_Saddles(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
        
    def InitializeUI(self):
        
        #Variable to hold all saddle support class instances 
        #self.saddle_support_instances=[]
        
        self.Vbox_layout=QVBoxLayout()
        saddle_support= Saddle_Support()
        bracket_support_for_vessels=Bracket_Support_for_Vessel()
        self.Vbox_layout.addWidget(saddle_support)
        self.Vbox_layout.addWidget(bracket_support_for_vessels)
       
       
        self.container_widget = QWidget()
        self.container_widget.setLayout(self.Vbox_layout)

        # Create new Scroll area and set it as resizable
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
       

        # Set the container widget as the widget for the scroll area
        self.scroll_area.setWidget(self.container_widget)
       

        # Add the scroll area to the main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.scroll_area)

        self.setLayout(main_v_box)
        #self.cmbbox_No_of_shell.setCurrentIndex(1)

    # def Set_No_of_Shell(self):
        
    #     for i in reversed(range(self.hbox_shells_layout.count())):
    #         widget = self.hbox_shells_layout.itemAt(i).widget()
    #         if widget is not None:
    #             widget.close()
       
    #     no_of_shells=int(self.cmbbox_No_of_shell.currentText())
    #     for _ in range(0,no_of_shells):
    #         shell=Shell()
    #         self.saddle_support_instances.append(shell)         
    #         self.hbox_shells_layout.addWidget(shell)
        
        
        
class Saddle_Support(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
            
    def InitializeUI(self):
        self.set_ui_layout() 
                      
    def set_ui_layout(self):
        self.grpbox_saddle_support=QGroupBox("Saddle Support")
        self.grpbox_saddle_support.setFixedWidth(850)
        self.grpbox_saddle_support.setStyleSheet(set_styles.ip_grpbox1_style)        
        self.Vbox_main_saddle_support=QVBoxLayout()
        self.Vbox_main_saddle_support.addWidget(self.grpbox_saddle_support)
        self.setLayout(self.Vbox_main_saddle_support)
        
        self.set_grpbox_UI()
        
    def set_grpbox_UI(self):
        
        #Gridlayout
        self.gridlayout_saddle_support=QGridLayout()
        self.grpbox_saddle_support.setLayout(self.gridlayout_saddle_support)
        
        #Input
        self.lbl_mat_density =QLabel("Density")
        self.tb_mat_density =QLineEdit("7.85")
        self.lbl_shell_OD =QLabel("Suitable Shell OD")
        self.cmb_box_shell_OD = QComboBox()
        possible_shell_od_list=self.get_shell_od_list_from_saddle_data()
        self.cmb_box_shell_OD.addItems([str(od) for od in possible_shell_od_list])
       
       
        self.lbl_wrp_plt_angle=QLabel("Wrp Plate Angle")
        self.tb_wrp_plt_angle =QLineEdit("162")
        self.lbl_No_of_Saddle=QLabel("No. of Saddles")
        self.cmbbox_No_of_Saddle=QComboBox()
        #self.cmbbox_No_of_Saddle.setStyleSheet("font: bold; font-size: 16px;")    
        self.cmbbox_No_of_Saddle.addItems(([str(x) for x in range(1,5,1)]))
        self.lbl_Saddle_Base_plt_material=QLabel("Base Plt Material")
        self.cmbbox_Saddle_Base_plt_material=QComboBox()          
        self.cmbbox_Saddle_Base_plt_material.addItems(var.master_mat_list) 
        self.lbl_Saddle_Web_plt_material=QLabel("Base Plt Material")        
        self.cmbbox_Saddle_Web_plt_material=QComboBox()           
        self.cmbbox_Saddle_Web_plt_material.addItems(var.master_mat_list)
        self.lbl_Saddle_Wrp_plt_material=QLabel("Wrp Plt Material")
        self.cmbbox_Saddle_Wrp_plt_material=QComboBox()           
        self.cmbbox_Saddle_Wrp_plt_material.addItems(var.master_mat_list)          
        self.btn_calculate_wt=QPushButton("Calculate")
        self.btn_calculate_wt.clicked.connect(self.Calculate_btn_clicked)
        
        #Output
        self.lbl_op =QLabel("Output")
        self.lbl_op.setStyleSheet("font:bold;font-size:16px")        
        self.lbl_saddle_type=QLabel("Saddle Type")
        self.tb_saddle_type =QLineEdit("XX")
        self.tb_saddle_type.setEnabled(False)
        #Base Plt
        self.lbl_base_plt_op =QLabel("Base Plt")
        self.lbl_base_plt_op.setStyleSheet("font:bold;font-size:16px")
        self.lbl_base_plt_thk=QLabel("Base Plt Thk")
        self.tb_base_plt_thk =QLineEdit("XXx")
        self.tb_base_plt_thk.setEnabled(False)
        self.lbl_base_plt_wd=QLabel("Base Plt Width")
        self.tb_base_plt_wd =QLineEdit("XXx")
        self.tb_base_plt_wd.setEnabled(False)
        self.lbl_base_plt_Lg=QLabel("Base Plt Lg")
        self.tb_base_plt_Lg =QLineEdit("XXx")
        self.tb_base_plt_Lg.setEnabled(False)
        self.lbl_base_plt_Wt=QLabel("Base Plt Wt.")
        self.tb_base_plt_Wt =QLineEdit("XXx")
        self.tb_base_plt_Wt.setEnabled(False)
        
        #Web Plt
        self.lbl_web_plt_op =QLabel("Web Plt")
        self.lbl_web_plt_op.setStyleSheet("font:bold;font-size:16px")
        self.lbl_web_plt_thk=QLabel("Web Plt Thk")
        self.tb_web_plt_thk =QLineEdit("XXx")
        self.tb_web_plt_thk.setEnabled(False)
        self.lbl_web_plt_wd=QLabel("Web Plt Width")
        self.tb_web_plt_wd =QLineEdit("XXx")
        self.tb_web_plt_wd.setEnabled(False)
        self.lbl_web_plt_Lg=QLabel("Web Plt Lg")
        self.tb_web_plt_Lg =QLineEdit("XXx")
        self.tb_web_plt_Lg.setEnabled(False)
        self.lbl_web_plt_Wt=QLabel("Web Plt Wt.")
        self.tb_web_plt_Wt =QLineEdit("XXx")
        self.tb_web_plt_Wt.setEnabled(False)
        
          #Wrp Plt
        self.lbl_wrp_plt_op =QLabel("Wrp Plt")
        self.lbl_wrp_plt_op.setStyleSheet("font:bold;font-size:16px")  
        self.lbl_wrp_plt_thk=QLabel("Wrp Plt Thk")
        self.tb_wrp_plt_thk =QLineEdit("XXx")
        self.tb_wrp_plt_thk.setEnabled(False)
        self.lbl_wrp_plt_wd=QLabel("Wrp Plt Width")
        self.tb_wrp_plt_wd =QLineEdit("XXx")
        self.tb_wrp_plt_wd.setEnabled(False)
        self.lbl_wrp_plt_Lg=QLabel("Wrp Plt Lg")
        self.tb_wrp_plt_Lg =QLineEdit("XXx")
        self.tb_wrp_plt_Lg.setEnabled(False)
        self.lbl_wrp_plt_Wt=QLabel("Wrp Plt Wt.")
        self.tb_wrp_plt_Wt =QLineEdit("XXx")
        self.tb_wrp_plt_Wt.setEnabled(False)
        
        #Rib
        self.lbl_rib_Wt=QLabel("Rib Wt.")
        self.tb_rib_Wt =QLineEdit("XXX")
        self.tb_rib_Wt.setEnabled(False)
        
        #Saddle Surface Area
        self.lbl_saddle_surfaceArea=QLabel("Surface Area")
        self.tb_saddle_surfaceArea =QLineEdit("XXx")
        self.tb_saddle_surfaceArea.setEnabled(False)
        
        #Add Material Buttin
        self.btn_add_material=QPushButton("Add Material to BOM")        
        self.btn_add_material.clicked.connect(self.Add_material_to_BOM)
        
        
        #Input Layout
        
        
        a=2
        self.gridlayout_saddle_support.addWidget(self.lbl_mat_density,a,0)
        self.gridlayout_saddle_support.addWidget(self.tb_mat_density,a,1)
        self.gridlayout_saddle_support.addWidget(self.lbl_shell_OD,a,2)
        self.gridlayout_saddle_support.addWidget(self.cmb_box_shell_OD,a,3)
        self.gridlayout_saddle_support.addWidget(self.lbl_wrp_plt_angle,a,4)
        self.gridlayout_saddle_support.addWidget(self.tb_wrp_plt_angle,a,5)
        self.gridlayout_saddle_support.addWidget(self.lbl_No_of_Saddle,a,6)
        self.gridlayout_saddle_support.addWidget(self.cmbbox_No_of_Saddle,a,7)
        
        b=3
        self.gridlayout_saddle_support.addWidget(self.lbl_Saddle_Base_plt_material,b,0)
        self.gridlayout_saddle_support.addWidget(self.cmbbox_Saddle_Base_plt_material,b,1)
        self.gridlayout_saddle_support.addWidget(self.lbl_Saddle_Web_plt_material,b,2)
        self.gridlayout_saddle_support.addWidget(self.cmbbox_Saddle_Web_plt_material,b,3)
        self.gridlayout_saddle_support.addWidget(self.lbl_Saddle_Wrp_plt_material,b,4)
        self.gridlayout_saddle_support.addWidget(self.cmbbox_Saddle_Wrp_plt_material,b,5)
        
        c0=4
        self.gridlayout_saddle_support.addItem(QSpacerItem(100,30),c0,0)
        c1=5
        self.gridlayout_saddle_support.addWidget(self.btn_calculate_wt,c1,3,Qt.AlignmentFlag.AlignHCenter)

       
        
        #Output Layout 
        d=7            
        self.gridlayout_saddle_support.addWidget(self.lbl_op,d,0) 
        e=8              
        self.gridlayout_saddle_support.addWidget(self.lbl_saddle_type,e,0)
        self.gridlayout_saddle_support.addWidget(self.tb_saddle_type,e,1)
        #Base Plt
        f=9
        self.gridlayout_saddle_support.addWidget(self.lbl_base_plt_op,f,0)
        g=10
        self.gridlayout_saddle_support.addWidget(self.lbl_base_plt_thk,g,0)
        self.gridlayout_saddle_support.addWidget(self.tb_base_plt_thk,g,1)
        self.gridlayout_saddle_support.addWidget(self.lbl_base_plt_wd,g,2)
        self.gridlayout_saddle_support.addWidget(self.tb_base_plt_wd,g,3)
        self.gridlayout_saddle_support.addWidget(self.lbl_base_plt_Lg,g,4)
        self.gridlayout_saddle_support.addWidget(self.tb_base_plt_Lg,g,5)
        self.gridlayout_saddle_support.addWidget(self.lbl_base_plt_Wt,g,6)
        self.gridlayout_saddle_support.addWidget(self.tb_base_plt_Wt,g,7)
        
        #Web Plt
        h=11
        self.gridlayout_saddle_support.addWidget(self.lbl_web_plt_op,h,0)
        i=12
        self.gridlayout_saddle_support.addWidget(self.lbl_web_plt_thk,i,0)
        self.gridlayout_saddle_support.addWidget(self.tb_web_plt_thk,i,1)
        self.gridlayout_saddle_support.addWidget(self.lbl_web_plt_wd,i,2)
        self.gridlayout_saddle_support.addWidget(self.tb_web_plt_wd,i,3)
        self.gridlayout_saddle_support.addWidget(self.lbl_web_plt_Lg,i,4)
        self.gridlayout_saddle_support.addWidget(self.tb_web_plt_Lg,i,5)
        self.gridlayout_saddle_support.addWidget(self.lbl_web_plt_Wt,i,6)
        self.gridlayout_saddle_support.addWidget(self.tb_web_plt_Wt,i,7)
        
             #Wrp Plt
        j=13    
        self.gridlayout_saddle_support.addWidget(self.lbl_wrp_plt_op,j,0)
        k=14
        self.gridlayout_saddle_support.addWidget(self.lbl_wrp_plt_thk,k,0)
        self.gridlayout_saddle_support.addWidget(self.tb_wrp_plt_thk,k,1)
        self.gridlayout_saddle_support.addWidget(self.lbl_wrp_plt_wd,k,2)
        self.gridlayout_saddle_support.addWidget(self.tb_wrp_plt_wd,k,3)
        self.gridlayout_saddle_support.addWidget(self.lbl_wrp_plt_Lg,k,4)
        self.gridlayout_saddle_support.addWidget(self.tb_wrp_plt_Lg,k,5)
        self.gridlayout_saddle_support.addWidget(self.lbl_wrp_plt_Wt,k,6)
        self.gridlayout_saddle_support.addWidget(self.tb_wrp_plt_Wt,k,7)
        
        #Rib 
        l=15
        self.gridlayout_saddle_support.addWidget(self.lbl_rib_Wt,l,0)
        self.gridlayout_saddle_support.addWidget(self.tb_rib_Wt,l,1)
        
        #Surface Aere
        m=l
        self.gridlayout_saddle_support.addWidget(self.lbl_saddle_surfaceArea,m,2)
        self.gridlayout_saddle_support.addWidget(self.tb_saddle_surfaceArea,m,3) 
        
        n=m+1 
        self.gridlayout_saddle_support.addItem(QSpacerItem(100,30),n,0)      
        self.gridlayout_saddle_support.addWidget(self.btn_add_material,n,3,Qt.AlignmentFlag.AlignHCenter)
       
        self.Set_all_TextBox_Width()
        self.btn_add_material.setFixedWidth(150) 
        
        #self.Set_button_functionality()     
        
    # def Set_button_functionality(self):        
    #     self.btn_add_material.clicked.connect(lambda:self.Add_material_to_BOM(item))
        
    def Set_all_TextBox_Width(self):
        # Get the QGridLayout widget
        #layout = self.findChild(QGridLayout)

        # Iterate over all of the widgets in the QGridLayout
        for i in range(self.gridlayout_saddle_support.rowCount()):
            for j in range(self.gridlayout_saddle_support.columnCount()):
                widget_item = self.gridlayout_saddle_support.itemAtPosition(i, j)
                if widget_item is not None:
                    widget = widget_item.widget()
                    # If the widget is a QLineEdit widget, set its width
                    if (isinstance(widget, QLineEdit) or isinstance(widget,QComboBox)):
                        widget.setFixedWidth(100)

    def get_shell_od_list_from_saddle_data(self):
       shell_od_list= Get_Shell_ODs_from_Saddle_Data()
       return shell_od_list
       
   
    def Add_material_to_BOM(self):
        
        _ProjectCOntroller=ProjectController()
        _ProjectCOntroller.add_update_item(item='Saddle Base Plate',item_name="Saddle Base Plate",wt=self.tb_base_plt_Wt.text(),material=self.cmbbox_Saddle_Base_plt_material.currentText())
        _ProjectCOntroller.add_update_item(item='Saddle Web Plate',item_name="Saddle Web Plate",wt=self.tb_web_plt_Wt.text(),material=self.cmbbox_Saddle_Web_plt_material.currentText())
        _ProjectCOntroller.add_update_item(item='Saddle Wrp Plate',item_name="Saddle Wrp Plate",wt=self.tb_wrp_plt_Wt.text(),material=self.cmbbox_Saddle_Wrp_plt_material.currentText())
        _ProjectCOntroller.add_update_surface_area(item='Saddle',item_name="Saddle",surface_area=self.tb_saddle_surfaceArea.text())
        #print("Add Shell Material to BOM Pressed")
        self.change_button_color_green()

    def Calculate_btn_clicked(self):
        self.No_of_saddle=int(self.cmbbox_No_of_Saddle.currentText())
        self.shell_OD=int(self.cmb_box_shell_OD.currentText())
        
        #Base Plt
        self.Saddle_Data=Get_Saddle_Data(self.shell_OD)#self.shell_OD
        self.Saddle_type=self.Saddle_Data.Type        
        self.Saddle_Dim_data=Get_Saddle_Dim_Data(self.Saddle_type)
        self.Base_plt_thk=float(self.Saddle_Dim_data.t2)
        self.Base_plt_wd=170 if self.Saddle_type=="A" else 250
        self.Base_plt_Lg=float(self.Saddle_Data.LB)
        self.Base_plt_Wt=(self.No_of_saddle*self.Base_plt_Lg*self.Base_plt_thk*self.Base_plt_wd)*float(self.tb_mat_density.text())*0.000001
        self.Base_plt_Wt=round(self.Base_plt_Wt,1)
        self.tb_saddle_type.setText(self.Saddle_type)
        self.tb_base_plt_thk.setText(str(self.Base_plt_thk))
        self.tb_base_plt_wd.setText(str(self.Base_plt_wd))
        self.tb_base_plt_Lg.setText(str(self.Base_plt_Lg))
        self.tb_base_plt_Wt.setText(str(self.Base_plt_Wt))
        
        
        #Wrp Plt
        self.Wrp_plt_thk=float(self.Saddle_Dim_data.t3)
        self.Wrp_plt_wd=float(self.Saddle_Dim_data.L3)
        self.Wrp_plt_Lg=self.shell_OD/2*float(self.tb_wrp_plt_angle.text())*math.pi/180+100
        self.Wrp_plt_Lg=round(self.Wrp_plt_Lg,2)
        self.Wrp_plt_Wt=(self.No_of_saddle*self.Wrp_plt_Lg*self.Wrp_plt_thk*self.Wrp_plt_wd)*float(self.tb_mat_density.text())*0.000001
        self.Wrp_plt_Wt=round(self.Wrp_plt_Wt,2)
        self.tb_wrp_plt_thk.setText(str(self.Wrp_plt_thk))
        self.tb_wrp_plt_wd.setText(str(self.Wrp_plt_wd))
        self.tb_wrp_plt_Lg.setText(str(self.Wrp_plt_Lg))
        self.tb_wrp_plt_Wt.setText(str(self.Wrp_plt_Wt))
        
        
        #Web Plt
        self.Web_plt_thk=float(self.Saddle_Dim_data.t1)
        self.Web_plt_wd=float(self.Saddle_Data.H)-(math.sqrt(((self.shell_OD+2*self.Wrp_plt_thk)/2)**2-(float(self.Saddle_Data.LB)/2)**2))+100
        self.Web_plt_wd=round(self.Web_plt_wd,2)
        self.Web_plt_Lg=self.Base_plt_Lg
        self.Web_plt_Wt=(self.No_of_saddle*self.Web_plt_Lg*self.Web_plt_thk*self.Web_plt_wd)*float(self.tb_mat_density.text())*0.000001
        self.Web_plt_Wt=round(self.Web_plt_Wt,2)
        self.tb_web_plt_thk.setText(str(self.Web_plt_thk))
        self.tb_web_plt_wd.setText(str(self.Web_plt_wd))
        self.tb_web_plt_Lg.setText(str(self.Web_plt_Lg))
        self.tb_web_plt_Wt.setText(str(self.Web_plt_Wt))
        
        #Rib
        self.tb_rib_Wt.setText(self.Saddle_Data.rib_wt)
        
        #Surface ARea
        self.Saddle_Surface_area=round((self.Wrp_plt_Wt/self.Wrp_plt_thk+2*self.Web_plt_Wt/self.Web_plt_thk+2*self.Base_plt_Wt/self.Base_plt_thk)/7.85,2)
        self.tb_saddle_surfaceArea.setText(str(self.Saddle_Surface_area))
        
      
        
        self.reset_button_color_default(self.btn_add_material) #Reset the color of Add Material to BOM as Weight value got changed.
        
            
    def roundup_to_next100(self,num):
       return  math.ceil(num/100)*100
        
    def change_button_color_green(self):
        button = self.sender()
        button.setStyleSheet("background-color: green; color: white;")

    #This Function reset the color of "button" passed as an argument.
    def reset_button_color_default(self,button):
        #button = self.sender()
        button.setStyleSheet("")       


    
class Bracket_Support_for_Vessel(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
            
    def InitializeUI(self):
        self.set_ui_layout() 
                      
    def set_ui_layout(self):
        self.grpbox_vessel_bracket_support=QGroupBox("Bracket Supoort For Vessel")
        self.grpbox_vessel_bracket_support.setStyleSheet(set_styles.ip_grpbox1_style)        
        self.Vbox_main_vessel_bracket_support=QVBoxLayout()
        self.Vbox_main_vessel_bracket_support.addWidget(self.grpbox_vessel_bracket_support)
        self.setLayout(self.Vbox_main_vessel_bracket_support)
        
        self.set_grpbox_UI()
        
    def set_grpbox_UI(self):
        
        #Gridlayout
        self.gridlayout_vessel_bracket_support=QGridLayout()
        self.grpbox_vessel_bracket_support.setLayout(self.gridlayout_vessel_bracket_support)
        
        #Input
        self.lbl_mat_density =QLabel("Density")
        self.tb_mat_density =QLineEdit("7.85")
        self.lbl_shell_OD =QLabel("Shell OD")
        self.tb_shell_OD = QLineEdit("2500")       
        self.lbl_shell_thk=QLabel("Shell Thk")
        self.tb_shell_thk =QLineEdit("25")
        self.lbl_pad_thk =QLabel("Pad Thk")
        self.tb_pad_thk = QLineEdit("xx")
        self.tb_pad_thk.setEnabled(False)
        self.lbl_No_of_Brackets=QLabel("No. of Brackets")
        self.cmbbox_No_of_Brackets=QComboBox()      
        self.cmbbox_No_of_Brackets.addItems(([str(i) for i in range(1,10)]))
         
        self.lbl_Anchor_bolt_size=QLabel("Anchor Bolt Size")
        self.cmbbox_Anchor_bolt_size=QComboBox()      
        self.cmbbox_Anchor_bolt_size.addItems((['M30','M32','M36','M42']))
        self.lbl_Anchor_bolt_material=QLabel("Anchor Bolt Material")        
        self.cmbbox_Anchor_bolt_material=QComboBox() 
        self.cmbbox_Anchor_bolt_material.addItems(var.master_mat_list) 
        
        self.lbl_Pad_plt_material=QLabel("Pad Material")        
        self.cmbbox_Pad_material=QComboBox() 
        self.cmbbox_Pad_material.addItems(var.master_mat_list) 
        self.lbl_Gusset_material=QLabel("Gusset Material")
        self.cmbbox_Gusset_material=QComboBox()           
        self.cmbbox_Gusset_material.addItems(var.master_mat_list) 
        self.lbl_Base_plt_material=QLabel("Base Plt Material")
        self.cmbbox_Base_plt_material=QComboBox()          
        self.cmbbox_Base_plt_material.addItems(var.master_mat_list)       
        
        #Calculate Button
        self.btn_calculate_wt=QPushButton("Calculate")
        self.btn_calculate_wt.clicked.connect(self.Calculate_btn_clicked)
        
        #Output
        self.lbl_op =QLabel("Output")
        self.lbl_op.setStyleSheet("font:bold;font-size:16px") 
        self.lbl_value_of_x=QLabel("Value of x")
        self.tb_value_of_x = QLineEdit("xxx")
        self.tb_value_of_x .setEnabled(False) 
        self.lbl_Pad_Wt=QLabel("Pad Weight")        
        self.tb_Pad_Wt=QLineEdit("xx")
        self.tb_Pad_Wt.setEnabled(False)
        self.lbl_Gusset_Wt=QLabel("Gusset Weight")        
        self.tb_Gusset_Wt=QLineEdit("xx")
        self.tb_Gusset_Wt.setEnabled(False) 
        self.lbl_Base_plt_Wt=QLabel("Base Plate Weight")        
        self.tb_Base_plt_Wt=QLineEdit("xx")
        self.tb_Base_plt_Wt.setEnabled(False) 
        self.lbl_No_of_anchor_bolt=QLabel("No. of Anchor Bolts")
        self.tb_No_of_anchor_bolt = QLineEdit("xxx") 
        self.tb_No_of_anchor_bolt.setEnabled(False)        
            
       
        #Surface Area
        self.lbl_vessel_bracket_support_surfaceArea=QLabel("Surface Area")
        self.tb_vessel_bracket_support_surfaceArea =QLineEdit("XXx")
        self.tb_vessel_bracket_support_surfaceArea.setEnabled(False)
        
        #Add Material Buttin
        self.btn_add_material=QPushButton("Add Material to BOM")
        self.btn_add_material.setMaximumWidth(150)
        self.btn_add_material.clicked.connect(self.Add_material_to_BOM)
        
        
        #Input Layout
        
        a=2
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_mat_density,a,0)
        self.gridlayout_vessel_bracket_support.addWidget(self.tb_mat_density,a,1)
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_shell_OD,a,2)
        self.gridlayout_vessel_bracket_support.addWidget(self.tb_shell_OD,a,3)        
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_shell_thk,a,4)
        self.gridlayout_vessel_bracket_support.addWidget(self.tb_shell_thk,a,5)
        
        b=a+1
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_pad_thk,b,0)
        self.gridlayout_vessel_bracket_support.addWidget(self.tb_pad_thk,b,1)
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_No_of_Brackets,b,2)
        self.gridlayout_vessel_bracket_support.addWidget(self.cmbbox_No_of_Brackets,b,3)  
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_Anchor_bolt_size,b,4)
        self.gridlayout_vessel_bracket_support.addWidget(self.cmbbox_Anchor_bolt_size,b,5)
        
        c=b+1
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_Pad_plt_material,c,0)
        self.gridlayout_vessel_bracket_support.addWidget(self.cmbbox_Pad_material,c,1)
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_Gusset_material,c,2)
        self.gridlayout_vessel_bracket_support.addWidget(self.cmbbox_Gusset_material,c,3)
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_Base_plt_material,c,4)
        self.gridlayout_vessel_bracket_support.addWidget(self.cmbbox_Base_plt_material,c,5)
        
        c1=c+1
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_Anchor_bolt_material,c1,0)
        self.gridlayout_vessel_bracket_support.addWidget(self.cmbbox_Anchor_bolt_material,c1,1)
        
        d=c1+1
        self.gridlayout_vessel_bracket_support.addItem(QSpacerItem(100,30),d,0)
        e=d+1
        self.gridlayout_vessel_bracket_support.addWidget(self.btn_calculate_wt,e,3,Qt.AlignmentFlag.AlignHCenter)

        
        #Output Layout 
        f=e+1           
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_op,f,0) 
        g=f+1              
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_value_of_x,g,0)
        self.gridlayout_vessel_bracket_support.addWidget(self.tb_value_of_x,g,1)
        
        h=g+1
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_Pad_Wt,h,0)
        self.gridlayout_vessel_bracket_support.addWidget(self.tb_Pad_Wt,h,1)
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_Gusset_Wt,h,2)
        self.gridlayout_vessel_bracket_support.addWidget(self.tb_Gusset_Wt,h,3)
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_Base_plt_Wt,h,4)
        self.gridlayout_vessel_bracket_support.addWidget(self.tb_Base_plt_Wt,h,5)
       
        
        #Surface Aere
        i=h+1
        self.gridlayout_vessel_bracket_support.addWidget(self.lbl_vessel_bracket_support_surfaceArea,i,0)
        self.gridlayout_vessel_bracket_support.addWidget(self.tb_vessel_bracket_support_surfaceArea,i,1) 
        
        j=i+1 
        self.gridlayout_vessel_bracket_support.addItem(QSpacerItem(100,30),j,0)      
        self.gridlayout_vessel_bracket_support.addWidget(self.btn_add_material,j,2,Qt.AlignmentFlag.AlignHCenter)
       
        self.Set_all_TextBox_Width() 
        
 
        
    def Set_all_TextBox_Width(self):
        # Get the QGridLayout widget
        #layout = self.findChild(QGridLayout)

        # Iterate over all of the widgets in the QGridLayout
        for i in range(self.gridlayout_vessel_bracket_support.rowCount()):
            for j in range(self.gridlayout_vessel_bracket_support.columnCount()):
                widget_item = self.gridlayout_vessel_bracket_support.itemAtPosition(i, j)
                if widget_item is not None:
                    widget = widget_item.widget()
                    # If the widget is a QLineEdit widget, set its width
                    if (isinstance(widget, QLineEdit) or isinstance(widget,QComboBox)):
                        widget.setFixedWidth(100)

   
    def Add_material_to_BOM(self):
        
        _ProjectCOntroller=ProjectController()
        _ProjectCOntroller.add_update_item(item='Vessel Bracket Support Pad',item_name="Vessel Bracket Support Pad",wt=self.tb_Pad_Wt.text(),material=self.cmbbox_Pad_material.currentText())
        _ProjectCOntroller.add_update_item(item='Vessel Bracket Support Gusset',item_name="Vessel Bracket Support Gusset",wt=self.tb_Gusset_Wt.text(),material=self.cmbbox_Gusset_material.currentText())
        _ProjectCOntroller.add_update_item(item='Vessel Bracket Support Base Plt',item_name="Vessel Bracket Support Base Plt",wt=self.tb_Base_plt_Wt.text(),material=self.cmbbox_Base_plt_material.currentText())
        _ProjectCOntroller.add_update_item(item='Vessel Bracket Support Anchor Bolts',item_name="Vessel Bracket Support Anchor Bolts",wt=self.tb_No_of_anchor_bolt.text(),material=self.cmbbox_Base_plt_material.currentText())
        _ProjectCOntroller.add_update_surface_area(item='Vessel Bracket SupporAnchor',item_name="Vessel Bracket Support",surface_area=self.tb_vessel_bracket_support_surfaceArea.text())
        #print("Add Shell Material to BOM Pressed")
        self.change_button_color_green()

    def Calculate_btn_clicked(self):
       
        self.tb_pad_thk.setText(self.tb_shell_thk.text())
        self.Vessel_OD= float(self.tb_shell_OD.text())+2*float(self.tb_shell_thk.text())        
        self.Vessel_data=Get_Vessel_Data(self.Vessel_OD)
        self.value_x=float(self.Vessel_data.X)
        self.tb_value_of_x.setText(str(self.value_x))
        
        self.density=float(self.tb_mat_density.text())*0.000001
        #Pad
        self.Pad_Wt=float(self.Vessel_data.A)*float(self.Vessel_data.B)*float(self.tb_pad_thk.text())*float(self.cmbbox_No_of_Brackets.currentText())*self.density
        self.Pad_Wt=round(self.Pad_Wt,1)
        self.tb_Pad_Wt.setText(str(self.Pad_Wt))
        #Gusset
        self.Gusset_Wt=(float(self.Vessel_data.Min_M)+self.value_x)*(25+25+float(self.Vessel_data.E))*float(self.Vessel_data.G)*2*float(self.cmbbox_No_of_Brackets.currentText())*self.density
        self.Gusset_Wt=round(self.Gusset_Wt,1)
        self.tb_Gusset_Wt.setText(str(self.Gusset_Wt))
        #Base Plate
        self.Base_plt_Wt=float(self.Vessel_data.C)*float(self.Vessel_data.F)*(float(self.Vessel_data.Min_M)+self.value_x)*float(self.cmbbox_No_of_Brackets.currentText())*self.density
        self.Base_plt_Wt=round(self.Base_plt_Wt,1)
        self.tb_Base_plt_Wt.setText(str(self.Base_plt_Wt))
        
        #No_of_ANchor_bolts
        self.tb_No_of_anchor_bolt.setText(f"{self.cmbbox_Anchor_bolt_size.currentText()} X {self.cmbbox_No_of_Brackets.currentText()} No.")
        
        #Surface ARea
        self.vessel_bracket_support_surfaceArea=round((self.Pad_Wt+2*self.Gusset_Wt+2*self.Base_plt_Wt)/float(self.tb_shell_thk.text())/7.85,2)
        self.tb_vessel_bracket_support_surfaceArea.setText(str(self.vessel_bracket_support_surfaceArea))
        
        self.reset_button_color_default(self.btn_add_material) #Reset the color of Add Material to BOM as Weight value got changed.
        
            
    def roundup_to_next100(self,num):
       return  math.ceil(num/100)*100
        
    def change_button_color_green(self):
        button = self.sender()
        button.setStyleSheet("background-color: green; color: white;")

    #This Function reset the color of "button" passed as an argument.
    def reset_button_color_default(self,button):
        #button = self.sender()
        button.setStyleSheet("")       
    
    pass

class set_styles:    
    op_vbox_style="""
                QVBoxLayout {
                    font: bold;
                    font-size:14px;
                    padding: 15px;
                    border: 1px solid silver;
                    border-radius: 6px;
                    margin-top: 5px;
                    background-color:lightgrey                     

                }
             
              
                """   
    ip_grpbox1_style="""
                QGroupBox {
                    font: bold;
                    font-size:14px;
                    padding: 15px;
                    border: 1px solid silver;
                    border-radius: 6px;
                    background-color:#ccffcc
                                        
                }
                          
                """


