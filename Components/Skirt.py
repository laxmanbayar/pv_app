import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout,QWidget, \
    QTabWidget,QGroupBox,QTableWidget,QTableWidgetItem,QGridLayout,QScrollArea,QSpacerItem,QSizePolicy
from Variables import var
from PyQt6.QtCore import Qt
import math
import Controller.project_controller as DBController
from Controller.project_controller import ProjectController

#Global Vriables
Skirt_ID=0.0
Skirt_thk=0.0
Skirt_mat_density=0.0 

class Tab_Skirt(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
    def InitializeUI(self):
        #H_box_layout= QHBoxLayout() 
        skirt=Skirt()
        skirt_AO=Skirt_AO() 

        V_box_main_layout=QVBoxLayout()
        V_box_main_layout.addWidget(skirt)
        V_box_main_layout.addWidget(skirt_AO)
        #V_box_main_layout.addLayout(H_box_layout)       

        self.setLayout(V_box_main_layout)


class Skirt(QWidget):
    def __init__(self):  
        super().__init__()    
        self.InitializeUI() 
        
    def InitializeUI(self):
        #Variable to hold all shell() class instances 
        self.skirt_sec_instances=[]
       
        self.lbl_skirt_ID=QLabel("Skirt ID")
        self.tb_skirt_ID=QLineEdit("1650")
        self.lbl_skirt_thk=QLabel("Skirt Thk")
        self.tb_skirt_thk=QLineEdit("12")
        self.lbl_skirt_mat_density =QLabel("Density")
        self.tb_skirt_mat_density =QLineEdit("7.85")
        self.Set_global_varriables()
        self.tb_skirt_ID.textChanged.connect(self.Set_global_varriables)
        self.tb_skirt_thk.textChanged.connect(self.Set_global_varriables)
       
        
        self.lbl_No_of_skirt_sec=QLabel("No. Of Skirt Sections")
        #self.lbl_No_of_skirt_sec.setStyleSheet("font: bold; font-size: 16px;")    
        self.cmbbox_No_of_skirt_sec=QComboBox()
        #self.cmbbox_No_of_skirt_sec.setStyleSheet("font: bold; font-size: 16px;")    
        self.cmbbox_No_of_skirt_sec.addItems(([str(x) for x in range(1,5,1)]))       
        self.cmbbox_No_of_skirt_sec.currentIndexChanged.connect(self.Set_No_of_Skirt_Sec) 
        
               
         #Gridlayout for skirt sec count label and combobox
        self.gridlayout=QGridLayout()
        self.gridlayout.addWidget(self.lbl_skirt_ID,0,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout.addWidget(self.tb_skirt_ID,0,1,alignment=Qt.AlignmentFlag.AlignLeft)
        self.gridlayout.addWidget(self.lbl_skirt_thk,1,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout.addWidget(self.tb_skirt_thk,1,1,alignment=Qt.AlignmentFlag.AlignLeft)
        self.gridlayout.addWidget(self.lbl_skirt_mat_density,2,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout.addWidget(self.tb_skirt_mat_density,2,1,alignment=Qt.AlignmentFlag.AlignLeft)
        self.gridlayout.addWidget(self.lbl_No_of_skirt_sec,3,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout.addWidget(self.cmbbox_No_of_skirt_sec,3,1,alignment=Qt.AlignmentFlag.AlignLeft)
        
        self.groupbox_skirt_ip=QGroupBox("Skirt(Input)")
        self.groupbox_skirt_ip.setFixedHeight(150)
        self.groupbox_skirt_ip.setStyleSheet(set_styles.ip_grpbox1_style)
        self.groupbox_skirt_ip.setLayout(self.gridlayout)
        
   

        #V_box_layout holds gridpayout and all the skirt sec widget(hbox_shells)
        self.V_box_layout=QVBoxLayout()
        #self.V_box_layout.addLayout(self.gridlayout)
        self.V_box_layout.addWidget(self.groupbox_skirt_ip)
        
        #hbox_skirt sec_layout holds all the skirt sec widgets (based on combobox value)
        self.hbox_skirt_sec_layout=QHBoxLayout()       
        self.V_box_layout.addLayout(self.hbox_skirt_sec_layout)
      
        # add one container widget and set its Lsyout as "V_box_layout"
        self.container_widget = QWidget()
        self.container_widget.setLayout(self.V_box_layout)
        #self.container_widget.setFixedHeight(400)

        # Create new Scroll area and set it as resizable
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        # Set the container widget as the widget for the scroll area
        self.scroll_area.setWidget(self.container_widget)
       

        # Add the scroll area to the main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.scroll_area)
        #main_v_box.addLayout(self.V_box_layout)

        self.setLayout(main_v_box)
        self.cmbbox_No_of_skirt_sec.setCurrentIndex(1)#Default Value of No_skirt_sec=2

    def Set_No_of_Skirt_Sec(self):
        
        for i in reversed(range(self.hbox_skirt_sec_layout.count())):
            widget = self.hbox_skirt_sec_layout.itemAt(i).widget()
            if widget is not None:
                widget.close()
       
        no_of_skirt_sec=int(self.cmbbox_No_of_skirt_sec.currentText())
        #ID=float(self.tb_skirt_ID.text())
        #Thk=float(self.tb_skirt_thk.text())
        for i in range(0,no_of_skirt_sec):
            skirt_sec=Skirt_Section(i+1)
            self.skirt_sec_instances.append(skirt_sec)         
            self.hbox_skirt_sec_layout.addWidget(skirt_sec)
    
    #This Function sets the Global Variables so that other Instances of all the child classes can use it
    def Set_global_varriables(self):
        global Skirt_ID,Skirt_thk,Skirt_mat_density
        Skirt_ID = float(self.tb_skirt_ID.text())
        var.Skirt_ID=Skirt_ID
        var.Skirt_thk=Skirt_thk
        Skirt_thk = float(self.tb_skirt_thk.text()) 
        Skirt_mat_density=float(self.tb_skirt_mat_density.text())
            
   
class Skirt_Section(QWidget):
    def __init__(self,Number):
        super().__init__()
        self.Number=Number
        self.InitiailizeUI()
        
    def InitiailizeUI(self):
        self.grpbox_skirt_sec=QGroupBox(f"Skirt Sec{self.Number}")
        self.grpbox_skirt_sec.setStyleSheet(set_styles.ip_grpbox1_style)
        self.gridlayout_skirt_sec=QGridLayout()
        self.gridlayout_skirt_sec.setVerticalSpacing(20)
        self.grpbox_skirt_sec.setLayout(self.gridlayout_skirt_sec)
        self.SetUp_Skirt_Sec_UI()
        
        self.Vbox_layout_skirt_sec=QVBoxLayout()
        self.Vbox_layout_skirt_sec.addWidget(self.grpbox_skirt_sec)
        self.setLayout(self.Vbox_layout_skirt_sec)
        
    def SetUp_Skirt_Sec_UI(self):
        
        #Input        
        self.lbl_skirt_sec_len=QLabel("Skirt Section Len")
        self.tb_skirt_sec_len=QLineEdit("1650")
        self.material_list = var.master_mat_list
        self.lbl_skirt_sec_material =QLabel("Material")
        self.cmbbox_skirt_sec_material=QComboBox()        
        self.cmbbox_skirt_sec_material.addItems(self.material_list)  
        self.btn_calc_skirt_sec_op=QPushButton("Calculate")
        self.btn_calc_skirt_sec_op.clicked.connect(self.Calc_Skirt_Sec_op)
        
        #Output
        self.lbl_skirt_sec_wt=QLabel("Skirt Section Wt")
        self.tb_skirt_sec_wt=QLineEdit("XX")
        self.tb_skirt_sec_wt.setEnabled(False)
        self.btn_add_to_BOM_skirt_sec_Wt=QPushButton("Add to BOM")
        self.btn_add_to_BOM_skirt_sec_Wt.clicked.connect(self.Add_to_BOM_Wt)
        self.lbl_skirt_sec_surfaceArea=QLabel("Skirt Section Surface Area")
        self.tb_skirt_sec_surfaceArea=QLineEdit("XX")
        self.tb_skirt_sec_surfaceArea.setEnabled(False)
        self.btn_add_to_BOM_skirt_sec_SurfaceArea=QPushButton("Add to BOM")
        self.btn_add_to_BOM_skirt_sec_SurfaceArea.clicked.connect(self.Add_to_BOM_SurfaceArea)
        
        #Input layout set
        #self.gridlayout_skirt_sec.addWidget(self.lbl_mat_density,0,0)
        #self.gridlayout_skirt_sec.addWidget(self.tb_mat_density,0,1)
        self.gridlayout_skirt_sec.addWidget(self.lbl_skirt_sec_material,1,0)
        self.gridlayout_skirt_sec.addWidget(self.cmbbox_skirt_sec_material,1,1)
        self.gridlayout_skirt_sec.addWidget(self.lbl_skirt_sec_len,2,0)
        self.gridlayout_skirt_sec.addWidget(self.tb_skirt_sec_len,2,1)
        self.gridlayout_skirt_sec.addWidget(self.btn_calc_skirt_sec_op,3,1)
        
        #Output layout set
        self.gridlayout_skirt_sec.addWidget(self.lbl_skirt_sec_wt,5,0)
        self.gridlayout_skirt_sec.addWidget(self.tb_skirt_sec_wt,5,1)
        self.gridlayout_skirt_sec.addWidget(self.btn_add_to_BOM_skirt_sec_Wt,5,2)
        self.gridlayout_skirt_sec.addWidget(self.lbl_skirt_sec_surfaceArea,6,0)
        self.gridlayout_skirt_sec.addWidget(self.tb_skirt_sec_surfaceArea,6,1)
        self.gridlayout_skirt_sec.addWidget(self.btn_add_to_BOM_skirt_sec_SurfaceArea,6,2)
        
        
        
    def Calc_Skirt_Sec_op(self):        
        self.Skirt_ID=Skirt_ID
        self.Skirt_Thk=Skirt_thk
        self.Skirt_mat_density=Skirt_mat_density
        print(Skirt_ID,Skirt_thk)
        skirt_len=float(self.tb_skirt_sec_len.text())
        density=Skirt_mat_density*0.000001 
        skirt_sec_Wt=round(math.pi*(self.Skirt_ID+self.Skirt_Thk)*skirt_len*self.Skirt_Thk*density,1)
        skirt_sec_SurfaceArea=round(math.pi*(self.Skirt_ID+self.Skirt_Thk)*skirt_len/1000000,1)
        
        self.tb_skirt_sec_wt.setText(str(skirt_sec_Wt))
        self.tb_skirt_sec_surfaceArea.setText(str(skirt_sec_SurfaceArea))
        
           
    def Add_to_BOM_Wt(self):
        _ProjectConroller=ProjectController()        
        _ProjectConroller.add_update_item(item="Skirt",
                                          item_name= f"Skirt_Sec{self.Number}",
                                          wt=self.tb_skirt_sec_wt.text(),
                                          material=self.cmbbox_skirt_sec_material.currentText()) 
        self.change_button_color_green()
        
           
    def Add_to_BOM_SurfaceArea(self):
        _ProjectConroller=ProjectController()        
        _ProjectConroller.add_update_surface_area(item="Skirt",
                                          item_name= f"Skirt_Sec{self.Number}",
                                          surface_area=self.tb_skirt_sec_surfaceArea.text())  
        self.change_button_color_green()
    
     #This function changes the coor of sender button to green
    def change_button_color_green(self):
        button = self.sender()
        button.setStyleSheet("background-color: green; color: white;")

    #This Function reset the color of "button" passed as an argument.
    def reset_button_color_default(self,button):
        #button = self.sender()
        button.setStyleSheet("") 
        
    
    
class Skirt_AO(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.InitializeUI()
        
    def InitializeUI(self):
        #Input GroupBox and Layout
        self.grpbox_sec_AO_ip=QGroupBox("Section Access Opening(AO) Input")
        self.grpbox_sec_AO_ip.setStyleSheet(set_styles.ip_grpbox1_style)
        self.gridlayout_sec_AO_ip=QGridLayout()
        self.grpbox_sec_AO_ip.setLayout(self.gridlayout_sec_AO_ip)
        
        #Output GroupBox and Layout
        self.grpbox_sec_AO_op=QGroupBox("Section Access Opening(AO) Output")
        self.grpbox_sec_AO_op.setStyleSheet(set_styles.ip_grpbox1_style)
        self.gridlayout_sec_AO_op=QGridLayout()
        self.grpbox_sec_AO_op.setLayout(self.gridlayout_sec_AO_op)
        
        #main layout
        self.Vboxlayout_sec_AO =QVBoxLayout()
        self.Vboxlayout_sec_AO.addWidget(self.grpbox_sec_AO_ip)
        self.Vboxlayout_sec_AO.addWidget(self.grpbox_sec_AO_op) 
        
        
        #Code to add scroll bar
        
        # add one container widget and set its Lsyout as "Vboxlayout_sec_AO"
        self.container_widget = QWidget()
        self.container_widget.setLayout(self.Vboxlayout_sec_AO)       

        # Create new Scroll area and set it as resizable
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
      
        # Set the container widget as the widget for the scroll area
        self.scroll_area.setWidget(self.container_widget)
       

        # Add the scroll area to the main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.scroll_area)
        #main_v_box.addLayout(self.V_box_layout)

        self.setLayout(main_v_box)
        
        self.SetUp_Sec_AO_Ip_UI()
        self.SetUp_Sec_AO_Op_UI()
        
        
    def SetUp_Sec_AO_Ip_UI(self):
        
        #Input
        self.lbl_Insulation_thk=QLabel("Inslulation Thk")
        self.tb_Insulation_thk=QLineEdit("50")
        self.lbl_FireProof_thk=QLabel("Fire Proof. Thk")
        self.tb_FireProof_thk=QLineEdit("0")
        self.lbl_AO_inside_dia=QLabel("AO inside Dia")
        self.tb_AO_inside_dia=QLineEdit("500")
        self.lbl_len_of_AO=QLabel("Length of AO")
        self.tb_len_of_AO=QLineEdit("350")
        self.lbl_No_of_AO=QLabel("No. of AO")
        self.tb_No_of_AO=QLineEdit("1")
        self.lbl_pad_thk=QLabel("Pad Thk")
        self.tb_pad_thk=QLineEdit("12")
        self.lbl_AO_cvr_plt_thk=QLabel("AO Cover Plt Thk")
        self.tb_AO_cvr_plt_thk=QLineEdit("3")
        self.lbl_No_of_AO_handles=QLabel("No. of AO Handles")
        self.tb_No_of_AO_handles=QLineEdit("2")
        self.btn_calculate_sec_AO_op=QPushButton("Calculate")
        self.btn_calculate_sec_AO_op.clicked.connect(self.Calc_btn_Sec_AO_op)
        
        #Intermediate OP
        self.lbl_thk_of_AO=QLabel("Thk. of AO")
        self.tb_thk_of_AO=QLineEdit("XXX")
        self.tb_thk_of_AO.setEnabled(False)
        self.lbl_pad_wdth=QLabel("Pad Width")
        self.tb_pad_wdth=QLineEdit("XX")
        self.tb_pad_wdth.setEnabled(False)
        self.lbl_pad_len=QLabel("Pad Len")
        self.tb_pad_len=QLineEdit("XX")
        self.tb_pad_len.setEnabled(False)
        self.lbl_in_out_projection=QLabel("In/Out Projection")
        self.tb_in_out_projection=QLineEdit("xx")
        self.tb_in_out_projection.setEnabled(False)
        self.lbl_AO_cvr_plt_dia=QLabel("AO Cover Plt Dia")
        self.tb_AO_cvr_plt_dia=QLineEdit("XX")
        self.tb_AO_cvr_plt_dia.setEnabled(False)
        self.lbl_AO_handle_size=QLabel("AO Handle Size")
        self.tb_AO_handle_size=QLineEdit("XX")
        self.tb_AO_handle_size.setEnabled(False)
        self.lbl_AO_cvr_side_ring=QLabel("AO CoverSide Ring")
        self.tb_AO_cvr_side_ring=QLineEdit("XX")
        self.tb_AO_cvr_side_ring.setEnabled(False)
        
        #Set Gridlayout
        #Input
        a=0
        lbl_AO_input=QLabel("AO Input")
        lbl_AO_input.setStyleSheet("font:bold")
        self.gridlayout_sec_AO_ip.addWidget(lbl_AO_input,a,0)
        a+=1
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_Insulation_thk,a,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_Insulation_thk,a,1)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_FireProof_thk,a,2)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_FireProof_thk,a,3)
        a+=1
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_AO_inside_dia,a,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_AO_inside_dia,a,1)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_len_of_AO,a,2)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_len_of_AO,a,3)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_No_of_AO,a,4)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_No_of_AO,a,5)
        a+=1
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_pad_thk,a,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_pad_thk,a,1)
        a+=1
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_AO_cvr_plt_thk,a,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_AO_cvr_plt_thk,a,1)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_No_of_AO_handles,a,2)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_No_of_AO_handles,a,3)  
        a+=1     
        self.gridlayout_sec_AO_ip.addWidget(self.btn_calculate_sec_AO_op,a,2,alignment=Qt.AlignmentFlag.AlignCenter)
        
        #Intermediate OP  
        a+=1      
        self.gridlayout_sec_AO_ip.addItem(QSpacerItem(30, 30),a, 0,alignment=Qt.AlignmentFlag.AlignCenter)
        a+=1
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_thk_of_AO,a,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_thk_of_AO,a,1)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_pad_wdth,a,2)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_pad_wdth,a,3)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_pad_len,a,4)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_pad_len,a,5)
        a+=1
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_in_out_projection,a,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_in_out_projection,a,1)
        a+=1
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_AO_cvr_plt_dia,a,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_AO_cvr_plt_dia,a,1)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_AO_handle_size,a,2)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_AO_handle_size,a,3)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_AO_cvr_side_ring,a,4)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_AO_cvr_side_ring,a,5)
        
                 
           
    def SetUp_Sec_AO_Op_UI(self):
        
        #AO Pipe
        self.lbl_AO_pipe_thk=QLabel("AO Pipe thk")
        self.tb_AO_pipe_thk=QLineEdit("XX")
        self.tb_AO_pipe_thk.setEnabled(False)
        self.lbl_AO_pipe_wdth=QLabel("AO Pipe Width")
        self.tb_AO_pipe_wdth=QLineEdit("XX")
        self.tb_AO_pipe_wdth.setEnabled(False)
        self.lbl_AO_pipe_len=QLabel("AO Pipe Length")
        self.tb_AO_pipe_len=QLineEdit("XX")
        self.tb_AO_pipe_len.setEnabled(False)
        self.lbl_AO_pipe_Wt=QLabel("AO Pipe Weight")
        self.tb_AO_pipe_Wt=QLineEdit("XX")
        self.tb_AO_pipe_Wt.setEnabled(False)
        self.material_list = var.master_mat_list
        self.lbl_AO_pipe_material =QLabel("Material")
        self.cmbbox_AO_pipe_material=QComboBox()
        self.cmbbox_AO_pipe_material.addItems(self.material_list)
        self.lbl_AO_pipe_Wt_BOM=QLabel("AO Pipe Weight BOM")
        self.tb_AO_pipe_Wt_BOM=QLineEdit("XX")
        self.tb_AO_pipe_Wt_BOM.setEnabled(False)
      
        #buttons
        self.btn_add_AO_pipe_wt=QPushButton("Add to BOM")
        self.btn_add_AO_pipe_wt.clicked.connect(self.Add_to_BOM)
        self.btn_add_AO_pipe_wt_BOM=QPushButton("Add to BOM")
        self.btn_add_AO_pipe_wt_BOM.clicked.connect(self.Add_to_BOM)
        
        
        #AO Pad
        self.lbl_AO_pad_thk=QLabel("AO Pad thk")
        self.tb_AO_pad_thk=QLineEdit("XX")
        self.tb_AO_pad_thk.setEnabled(False)
        self.lbl_AO_pad_wdth=QLabel("AO Pad Width")
        self.tb_AO_pad_wdth=QLineEdit("XX")
        self.tb_AO_pad_wdth.setEnabled(False)
        self.lbl_AO_pad_len=QLabel("AO Pad Length")
        self.tb_AO_pad_len=QLineEdit("XX")
        self.tb_AO_pad_len.setEnabled(False)
        self.lbl_AO_pad_Wt=QLabel("AO Pad Weight")
        self.tb_AO_pad_Wt=QLineEdit("XX")
        self.tb_AO_pad_Wt.setEnabled(False)
        self.lbl_AO_pad_Wt_BOM=QLabel("AO Pad Weight BOM")
        self.tb_AO_pad_Wt_BOM=QLineEdit("XX")
        self.tb_AO_pad_Wt_BOM.setEnabled(False)
        self.lbl_AO_pad_material =QLabel("Material")
        self.cmbbox_AO_pad_material=QComboBox()
        self.cmbbox_AO_pad_material.addItems(self.material_list)
        #buttons
        self.btn_add_AO_pad_wt=QPushButton("Add to BOM")
        self.btn_add_AO_pad_wt.clicked.connect(self.Add_to_BOM)
        self.btn_add_AO_pad_wt_BOM=QPushButton("Add to BOM")
        self.btn_add_AO_pad_wt_BOM.clicked.connect(self.Add_to_BOM)
        
        #AO COver
        self.lbl_AO_cover_Wt=QLabel("AO Cover Weight")
        self.tb_AO_cover_Wt=QLineEdit("XX")
        self.tb_AO_cover_Wt.setEnabled(False)
        self.lbl_AO_cover_handle_Wt=QLabel("AO cover Handle Weight")
        self.tb_AO_cover_handle_Wt=QLineEdit("XX")
        self.tb_AO_cover_handle_Wt.setEnabled(False)
        self.lbl_AO_cover_material =QLabel("Material")
        self.cmbbox_AO_cover_material=QComboBox()
        self.cmbbox_AO_cover_material.addItems(self.material_list)
        self.lbl_AO_cover_handle_material =QLabel("Material")
        self.cmbbox_AO_cover_handle_material=QComboBox()
        self.cmbbox_AO_cover_handle_material.addItems(self.material_list)
        #buttons
        self.btn_add_AO_cover_wt=QPushButton("Add to BOM")
        self.btn_add_AO_cover_wt.clicked.connect(self.Add_to_BOM)
        self.btn_add_AO_cover_handle_Wt=QPushButton("Add to BOM")
        self.btn_add_AO_cover_handle_Wt.clicked.connect(self.Add_to_BOM)
        
        #Total AO Surface Area
        self.lbl_AO_surface_area=QLabel("AO Surface Area")
        self.lbl_AO_surface_area.setStyleSheet("font:bold")
        self.tb_AO_surface_area=QLineEdit("XXX")
        self.tb_AO_surface_area.setStyleSheet("font:bold")
        self.tb_AO_surface_area.setEnabled(False)
        self.btn_add_AO_SurfaceArea=QPushButton("Add to BOM")
        self.btn_add_AO_SurfaceArea.clicked.connect(self.Add_to_BOM)
        
        
        ####Layout Setting
        
        #AO Pipe Layout
        a=0
        lbl_AO_pipe=QLabel("AO Pipe")
        lbl_AO_pipe.setStyleSheet("font:bold")
        self.gridlayout_sec_AO_op.addWidget(lbl_AO_pipe,a,0)
        a+=1
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_pipe_thk,a,0)
        self.gridlayout_sec_AO_op.addWidget(self.tb_AO_pipe_thk,a,1)
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_pipe_wdth,a,2)
        self.gridlayout_sec_AO_op.addWidget(self.tb_AO_pipe_wdth,a,3)
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_pipe_len,a,4)
        self.gridlayout_sec_AO_op.addWidget(self.tb_AO_pipe_len,a,5)
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_pipe_material,a,6)
        self.gridlayout_sec_AO_op.addWidget(self.cmbbox_AO_pipe_material,a,7)
        a+=1
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_pipe_Wt,a,0)
        self.gridlayout_sec_AO_op.addWidget(self.tb_AO_pipe_Wt,a,1)        
        self.gridlayout_sec_AO_op.addWidget(self.btn_add_AO_pipe_wt,a,2)
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_pipe_Wt_BOM,a,0)
        self.gridlayout_sec_AO_op.addWidget(self.tb_AO_pipe_Wt_BOM,a,1)
        self.gridlayout_sec_AO_op.addWidget(self.btn_add_AO_pipe_wt_BOM,a,2)
        
        ##AO Pad layout
        a+=1
        lbl_AO_pad=QLabel("AO Pad")
        lbl_AO_pad.setStyleSheet("font:bold")
        self.gridlayout_sec_AO_op.addWidget(lbl_AO_pad,a,0)
        a+=1
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_pad_thk,a,0)
        self.gridlayout_sec_AO_op.addWidget(self.tb_AO_pad_thk,a,1)
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_pad_wdth,a,2)
        self.gridlayout_sec_AO_op.addWidget(self.tb_AO_pad_wdth,a,3)
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_pad_len,a,4)
        self.gridlayout_sec_AO_op.addWidget(self.tb_AO_pad_len,a,5)
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_pad_material,a,6)
        self.gridlayout_sec_AO_op.addWidget(self.cmbbox_AO_pad_material,a,7)
        a+=1
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_pad_Wt,a,0)
        self.gridlayout_sec_AO_op.addWidget(self.tb_AO_pad_Wt,a,1)      
        self.gridlayout_sec_AO_op.addWidget(self.btn_add_AO_pad_wt,a,2)
        a+=1
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_pad_Wt_BOM,a,0)
        self.gridlayout_sec_AO_op.addWidget(self.tb_AO_pad_Wt_BOM,a,1)
        self.gridlayout_sec_AO_op.addWidget(self.btn_add_AO_pad_wt_BOM,a,2)
        
        
        #AO Cover hand Handle Layout
        a+=1
        lbl_AO_cover_and_handle=QLabel("AO Cover & Handle")
        lbl_AO_cover_and_handle.setStyleSheet("font:bold")
        self.gridlayout_sec_AO_op.addWidget(lbl_AO_cover_and_handle,a,0)
        a+=1
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_cover_Wt,a,0)
        self.gridlayout_sec_AO_op.addWidget(self.tb_AO_cover_Wt,a,1)
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_cover_material,a,2)
        self.gridlayout_sec_AO_op.addWidget(self.cmbbox_AO_cover_material,a,3)
        self.gridlayout_sec_AO_op.addWidget(self.btn_add_AO_cover_wt,a,4)
        a+=1
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_cover_handle_Wt,a,0)
        self.gridlayout_sec_AO_op.addWidget(self.tb_AO_cover_handle_Wt,a,1)
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_cover_handle_material,a,2)
        self.gridlayout_sec_AO_op.addWidget(self.cmbbox_AO_cover_handle_material,a,3)
        self.gridlayout_sec_AO_op.addWidget(self.btn_add_AO_cover_handle_Wt,a,4)
        
        a+=1
        self.gridlayout_sec_AO_op.addItem(QSpacerItem(30, 30),a, 0,alignment=Qt.AlignmentFlag.AlignCenter)
        a+=1
        self.gridlayout_sec_AO_op.addWidget(self.lbl_AO_surface_area,a,0)
        self.gridlayout_sec_AO_op.addWidget(self.tb_AO_surface_area,a,1)
        self.gridlayout_sec_AO_op.addWidget(self.btn_add_AO_SurfaceArea,a,2)
        
   
        
    def Calc_btn_Sec_AO_op(self):
        
        #Intermediate Calc
        
        #print(Skirt_ID,Skirt_thk)
        self.Skirt_thk=Skirt_thk
        self.Skirt_ID=Skirt_ID
        self.Skirt_mat_density=Skirt_mat_density
        self.AO_thk=min(14,self.Skirt_thk+2)        
        self.AO_inside_dia=float(self.tb_AO_inside_dia.text())
        self.pad_wdth= self.AO_inside_dia/2       
        self.In_out_projection=max(float(self.tb_Insulation_thk.text())+30, float(self.tb_FireProof_thk.text())+30, 50)        
        self.AO_cvr_plt_dia=float(self.tb_AO_inside_dia.text())+2*self.AO_thk+2*float(self.tb_AO_cvr_plt_thk.text())        
        self.pad_thk=float(self.tb_pad_thk.text())
        self.pad_len= self.IPad_Lg(self.Skirt_ID,self.AO_inside_dia,self.AO_thk,self.pad_thk,self.pad_wdth)
       
        #Update Textbox value
        self.tb_thk_of_AO.setText(str(self.AO_thk))
        self.tb_pad_wdth.setText(str(self.pad_wdth))
        self.tb_in_out_projection.setText(str(self.In_out_projection))
        self.tb_AO_cvr_plt_dia.setText(str(self.AO_cvr_plt_dia))
        self.tb_AO_handle_size.setText("Ø12" + " x " + "Lg " + str(round(150+2*80+(2*90*math.pi/180*6),0)))        
        self.tb_AO_cvr_side_ring.setText("3 Thk" + " x " + "25 Wd" + " x " + str(round(math.pi*(self.AO_inside_dia+2*self.AO_thk+2*3+2*1.5),0)) + " Lg")
        self.tb_pad_len.setText(str(self.pad_len))
        
        
        ## AO pipe and AO Pad Calc
        #AO Pipe
        self.AO_pipe_thk=self.AO_thk
        self.AO_pipe_wd=round(math.sqrt(((self.Skirt_ID+2*self.Skirt_thk)/2)**2-(self.AO_inside_dia/2)**2)-math.sqrt((self.Skirt_ID/2)**2-(self.AO_inside_dia/2)**2)+2*self.In_out_projection,1)
        self.AO_pipe_len=round(math.pi*self.AO_inside_dia,1)
        self.AO_pipe_wt_BOM=round(self.AO_pipe_thk*self.AO_pipe_wd*self.AO_pipe_len*self.Skirt_mat_density*0.000001,1)*int(self.tb_No_of_AO.text())
        self.AO_pipe_wt=round(self.AO_pipe_wt_BOM*1.05,1)
        #Update TextBoxes
        self.tb_AO_pipe_thk.setText(str(self.AO_pipe_thk))
        self.tb_AO_pipe_wdth.setText(str(self.AO_pipe_wd))
        self.tb_AO_pipe_len.setText(str(self.AO_pipe_len))
        self.tb_AO_pipe_Wt.setText(str(self.AO_pipe_wt))
        self.tb_AO_pipe_Wt_BOM.setText(str(self.AO_pipe_wt_BOM))
        
        #AO Pad
        self.AO_pad_thk=self.pad_thk
        self.AO_pad_wd=round(self.AO_inside_dia+2*self.pad_thk+2*self.pad_wdth,1)
        self.AO_pad_len=self.pad_len
        self.AO_pad_wt=round(self.AO_pad_thk*self.AO_pad_wd*self.AO_pad_len*self.Skirt_mat_density*0.000001,1)*int(self.tb_No_of_AO.text())
        self.AO_pad_wt_BOM=round(self.AO_pad_wt-math.pi/4*(self.AO_inside_dia+2*self.pad_thk)**2*self.pad_thk*self.Skirt_mat_density*0.000001*int(self.tb_No_of_AO.text()),1)
        #Update TextBoxes
        self.tb_AO_pad_thk.setText(str(self.AO_pad_thk))
        self.tb_AO_pad_wdth.setText(str(self.AO_pad_wd))
        self.tb_AO_pad_len.setText(str(self.AO_pad_len))
        self.tb_AO_pad_Wt.setText(str(self.AO_pad_wt))
        self.tb_AO_pad_Wt_BOM.setText(str(self.AO_pad_wt_BOM))
        
        
        #AO COver and Handle
        self.AO_cover_wt=round((self.AO_inside_dia+2*self.pad_thk+2*3)**2*3*self.Skirt_mat_density*0.000001+math.pi*(self.AO_inside_dia+2*self.pad_thk+2*6)*25*3*self.Skirt_mat_density*0.000001*int(self.tb_No_of_AO.text()),1)
        self.AO_cover_handle_wt=round(350*2*math.pi/4*12**2*self.Skirt_mat_density*0.000001*int(self.tb_No_of_AO.text()),1)
        self.tb_AO_cover_Wt.setText(str(self.AO_cover_wt))
        self.tb_AO_cover_handle_Wt.setText(str(self.AO_cover_handle_wt))
        
        ##AO SUrface ARea calc
        self.AO_pipe_surface_area=self.AO_pipe_wt_BOM/self.Skirt_mat_density/self.AO_pipe_thk*2
        self.AO_pad_surface_area=self.AO_pad_wt_BOM/self.Skirt_mat_density/self.AO_pad_thk
        self.AO_cover_plt_surface_area=(self.AO_cover_wt+self.AO_cover_handle_wt)/self.Skirt_mat_density/self.pad_thk*2
        self.AO_SurfaceArea=round(self.AO_pipe_surface_area+self.AO_pad_surface_area+self.AO_cover_plt_surface_area,1)
        self.tb_AO_surface_area.setText(str(self.AO_SurfaceArea))
    
    
    def Add_to_BOM(self):
        _projectcontroller=ProjectController()
        #print(self.sender() is QPushButton)
        if(self.sender()==self.btn_add_AO_pipe_wt):
            _projectcontroller.add_update_item(item="AO Pipe",item_name="AO Pipe",wt=self.tb_AO_pipe_Wt.text(),material=self.cmbbox_AO_pipe_material.currentText())
        elif(self.sender()==self.btn_add_AO_pipe_wt_BOM):
            _projectcontroller.add_update_item(item="AO Pipe",item_name="AO Pipe BOM",wt=self.tb_AO_pipe_Wt_BOM.text(),material=self.cmbbox_AO_pipe_material.currentText())
        elif(self.sender()==self.btn_add_AO_pad_wt):
            _projectcontroller.add_update_item(item="AO Pad",item_name="AO Pad",wt=self.tb_AO_pad_Wt.text(),material=self.cmbbox_AO_pad_material.currentText())
        elif(self.sender()==self.btn_add_AO_pad_wt_BOM):
            _projectcontroller.add_update_item(item="AO Pad",item_name="AO Pad BOM",wt=self.tb_AO_pad_Wt_BOM.text(),material=self.cmbbox_AO_pad_material.currentText())    
        elif(self.sender()==self.btn_add_AO_cover_wt) :
            _projectcontroller.add_update_item(item="AO Cover",item_name="AO Cover",wt=self.tb_AO_cover_Wt.text(),material=self.cmbbox_AO_cover_material.currentText())     
        elif(self.sender()==self.btn_add_AO_cover_handle_Wt) :
            _projectcontroller.add_update_item(item="AO Cover Handle",item_name="AO Cover Handle",wt=self.tb_AO_cover_handle_Wt.text(),material=self.cmbbox_AO_cover_handle_material.currentText())  
   
        self.change_button_color_green()
    @staticmethod
    def IPad_Lg(ID, AOID, T1, T, W):
        #' ID = Inner Dia of Shell, AOID = Access Opening ID, T1 = Thickness of Ao, T = Thickenss of Pad, W = Pad Width 
        #'Pi = 22 / 7
        IRs = ID / 2
        Orn = AOID / 2 + T1
        dy = math.sqrt(IRs ** 2 - Orn ** 2)
        Z = Orn / dy
        alpha = math.atan(Z)
      
        MR = IRs - (T / 2)
        Lg = (2 * alpha * MR) + (2 * W)
        IPad_Lg = round(Lg + 0.5, 0) 
        return IPad_Lg  
    
     #This function changes the coor of sender button to green
    def change_button_color_green(self):
        button = self.sender()
        button.setStyleSheet("background-color: green; color: white;")

    #This Function reset the color of "button" passed as an argument.
    def reset_button_color_default(self,button):
        #button = self.sender()
        button.setStyleSheet("") 
        
        
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