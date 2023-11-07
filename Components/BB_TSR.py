
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QLayout, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout,QWidget, \
    QTabWidget,QGroupBox,QTableWidget,QTableWidgetItem,QGridLayout,QScrollArea,QSpacerItem
from Variables import var
from PyQt6.QtCore import Qt,QRect
import math
from Controller.project_controller import ProjectController,Get_DownComer_Data
import re

class Tab_BB_TSR(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
        
    def InitializeUI(self):
       
        self.main_gridlayout=QGridLayout()
        
        self.Vbox_layout=QVBoxLayout()
        part1= Part1()
        part2=Part2()
        pipe_devit=Pipe_Devit()
        manhole_devit=ManHole_Devit()
        
        self.main_gridlayout.addWidget(part1,0,0,1,2)
        self.main_gridlayout.addWidget(part2,1,0,1,1)
        self.main_gridlayout.addWidget(pipe_devit,1,1,1,1)
        self.main_gridlayout.addWidget(manhole_devit,2,0,1,1)
        
        # self.Vbox_layout.addWidget(part1)
        # self.Vbox_layout.addWidget(part2)
        
        self.Vbox_layout.addLayout(self.main_gridlayout)
        
        
       
       
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
        
        
        
class Part1(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
            
    def InitializeUI(self):
        self.set_ui_layout() 
                      
    def set_ui_layout(self):
        self.grpbox=QGroupBox("XXXXX")
        self.grpbox.setFixedWidth(880)
        self.grpbox.setStyleSheet(set_styles.ip_grpbox1_style)        
        self.Vbox_layout=QVBoxLayout()
        self.Vbox_layout.addWidget(self.grpbox)
        self.setLayout(self.Vbox_layout)
        
        self.set_grpbox_UI()
        
        
    def set_grpbox_UI(self):
        
        #Gridlayout
        self.gridlayout=QGridLayout()
        self.grpbox.setLayout(self.gridlayout)
        
        #Input
        self.lbl_description =QLabel("Description")
        self.lbl_description.setStyleSheet("font:bold")
        self.tb_description =QLineEdit("XXXXXXXXXXX")
        self.tb_description.setStyleSheet("font:bold")
        
        self.lbl_density =QLabel("density")
        self.tb_density=QLineEdit("7.89")
        self.lbl_vessel_ID =QLabel("Vessel ID")
        self.tb_vessel_ID =QLineEdit("2200")
        self.lbl_corrosion_allwnc=QLabel("Corrosion allwnc")
        self.tb_corrosion_allwnc =QLineEdit("6")
        
        self.lb1_type_of_tray_pass_count =QLabel("Type of Tray/No.of Pass")
        self.cmbbox_type_of_tray_pass_count = QComboBox()
        self.cmbbox_type_of_tray_pass_count.addItems([str(i) for i in range(1,5)]) 
        
        self.lbl_type_of_downcomer =QLabel("Type of Tray/No.of Pass")
        self.cmbbox_type_of_downcomer = QComboBox()
        self.cmbbox_type_of_downcomer.addItems(["Center/Off Center","Side"]) 
        
        self.lbl_No_of_trays=QLabel("No. of Trays")
        self.tb_No_of_trays =QLineEdit("25")
        self.lbl_dist_btw_trays=QLabel("Dist.Between Trays")
        self.tb_dist_btw_trays =QLineEdit("800")
        
        self.lbl_No_of_joints=QLabel("No. of Joints")
        self.tb_No_of_joints =QLineEdit("00")
        self.lbl_S_ring_plt_wdth=QLabel("S Ring Plate Width")
        self.tb_S_ring_plt_wdth =QLineEdit("XX")
        self.lbl_S_ring_plt_len=QLabel("S Ring Plate Length")
        self.tb_S_ring_plt_len =QLineEdit("XX")
        self.lbl_S_ring_plt_thk=QLabel("S Ring Plate Thk")
        self.tb_S_ring_plt_thk =QLineEdit("XX")
        self.lbl_S_ring_plt_Wt=QLabel("S Ring Plate Wt.")
        self.tb_S_ring_plt_Wt =QLineEdit("XX")
        self.lbl_S_ring_plt_material=QLabel("S Ring Plate Wt.")
        self.cmbbox_S_ring_plt_material =QComboBox()
        self.cmbbox_S_ring_plt_material.addItems(var.master_mat_list)
        self.btn_add_mat_S_ring=QPushButton("Add to BOM")
        self.btn_add_mat_S_ring.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_Bolting_Bar_plt_wdth=QLabel("Bolting Bar Width")
        self.tb_Bolting_Bar_plt_wdth =QLineEdit("XX")        
        self.lbl_Bolting_Bar_plt_thk=QLabel("Bolting Bar Thk")
        self.tb_Bolting_Bar_plt_thk =QLineEdit("XX")
        self.lbl_Bolting_Bar_plt_Wt=QLabel("Bolting BarWt.")
        self.tb_Bolting_Bar_plt_Wt =QLineEdit("XX")
        self.lbl_Bolting_Bar_plt_material=QLabel("Bolting Bar Wt.")
        self.cmbbox_Bolting_Bar_plt_material =QComboBox()
        self.cmbbox_Bolting_Bar_plt_material.addItems(var.master_mat_list)
        self.btn_add_mat_Bolting_Bar=QPushButton("Add to BOM")
        self.btn_add_mat_Bolting_Bar.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_thk=QLabel("Thkiness")
        self.tb_thk =QLineEdit("18")
        self.lbl_Ring_ht=QLabel("Ring Height")
        self.tb_Ring_ht =QLineEdit("50")
        self.lbl_Ring_thk=QLabel("Ring Thk")
        self.tb_Ring_thk =QLineEdit("18")
        
        disabled_tb_list=[self.tb_S_ring_plt_len,self.tb_S_ring_plt_wdth,self.tb_S_ring_plt_thk,
                          self.tb_S_ring_plt_Wt,self.tb_Bolting_Bar_plt_wdth,self.tb_Bolting_Bar_plt_thk,
                          self.tb_Bolting_Bar_plt_Wt]
        material_cmbbox_list=[self.cmbbox_Bolting_Bar_plt_material,self.cmbbox_S_ring_plt_material]
        for cmbbox in material_cmbbox_list:
            cmbbox.setStyleSheet("background-color:lightgreen;font:bold")
        
        for tb in disabled_tb_list:
            tb.setEnabled(False)
        
        self.btn_calculate_wt=QPushButton("Calculate")
        self.btn_calculate_wt.clicked.connect(self.Calculate_btn_clicked)
        
               
        #Layout
        
        a=2
        self.gridlayout.addWidget(self.lbl_description,a,1)
        self.gridlayout.addWidget(self.tb_description,a,2)
        
        a=a+2
        self.gridlayout.addWidget(self.lbl_density,a,0)
        self.gridlayout.addWidget(self.tb_density,a,1)
        self.gridlayout.addWidget(self.lbl_vessel_ID,a,2)
        self.gridlayout.addWidget(self.tb_vessel_ID,a,3)
        self.gridlayout.addWidget(self.lbl_corrosion_allwnc,a,4)
        self.gridlayout.addWidget(self.tb_corrosion_allwnc,a,5)
        
        a=a+1
        self.gridlayout.addWidget(self.lb1_type_of_tray_pass_count,a,0)
        self.gridlayout.addWidget(self.cmbbox_type_of_tray_pass_count,a,1)
        self.gridlayout.addWidget(self.lbl_type_of_downcomer,a,2)
        self.gridlayout.addWidget(self.cmbbox_type_of_downcomer,a,3)
        
        
        a=a+1
        self.gridlayout.addWidget(self.lbl_No_of_trays,a,0)
        self.gridlayout.addWidget(self.tb_No_of_trays,a,1)       
        self.gridlayout.addWidget(self.lbl_dist_btw_trays,a,2)
        self.gridlayout.addWidget(self.tb_dist_btw_trays,a,3)
        
        a=a+1
        self.gridlayout.addWidget(self.lbl_No_of_joints,a,0)
        self.gridlayout.addWidget(self.tb_No_of_joints,a,1)
        
        a=a+1
        self.gridlayout.addWidget(self.btn_calculate_wt,a,2,Qt.AlignmentFlag.AlignHCenter)
        
        a=a+1
        self.gridlayout.addItem(QSpacerItem(100,30),a,0)
        
         #Output Layout 
        a=a+1           
        self.gridlayout.addWidget(QLabel("Output"),a,0) 
        
        a=a+1
        self.gridlayout.addWidget(self.lbl_S_ring_plt_wdth,a,0)
        self.gridlayout.addWidget(self.tb_S_ring_plt_wdth,a,1)
        self.gridlayout.addWidget(self.lbl_S_ring_plt_len,a,2)
        self.gridlayout.addWidget(self.tb_S_ring_plt_len,a,3)        
        self.gridlayout.addWidget(self.lbl_S_ring_plt_thk,a,4)
        self.gridlayout.addWidget(self.tb_S_ring_plt_thk,a,5) 
        
        a=a+1        
        self.gridlayout.addWidget(self.lbl_S_ring_plt_Wt,a,0)
        self.gridlayout.addWidget(self.tb_S_ring_plt_Wt,a,1) 
        self.gridlayout.addWidget(self.cmbbox_S_ring_plt_material,a,2)  
        self.gridlayout.addWidget(self.btn_add_mat_S_ring,a,3)      
        
        a=a+1       
        self.gridlayout.addWidget(self.lbl_Bolting_Bar_plt_wdth,a,0)
        self.gridlayout.addWidget(self.tb_Bolting_Bar_plt_wdth,a,1)        
        self.gridlayout.addWidget(self.lbl_Bolting_Bar_plt_thk,a,2)
        self.gridlayout.addWidget(self.tb_Bolting_Bar_plt_thk,a,3) 
        
        a=a+1
        self.gridlayout.addWidget(self.lbl_Bolting_Bar_plt_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Bolting_Bar_plt_Wt,a,1) 
        self.gridlayout.addWidget(self.cmbbox_Bolting_Bar_plt_material,a,2) 
        self.gridlayout.addWidget(self.btn_add_mat_Bolting_Bar,a,3)  
        
       
        self.Set_all_TextBox_Width()
        #self.btn_add_SurfaceArea.setFixedWidth(150)
        # self.btn_calculate_wt.setFixedSize(150,30) 
        self.tb_description.setFixedWidth(120)
       
        
    def Set_all_TextBox_Width(self):
        # Get the QGridLayout widget
        #layout = self.findChild(QGridLayout)

        # Iterate over all of the widgets in the QGridLayout
        for i in range(self.gridlayout.rowCount()):
            for j in range(self.gridlayout.columnCount()):
                widget_item = self.gridlayout.itemAtPosition(i, j)
                if widget_item is not None:
                    widget = widget_item.widget()
                    # If the widget is a QLineEdit widget, set its width
                    if (isinstance(widget, QLineEdit) ):
                        widget.setFixedWidth(80)
                    if (isinstance(widget,QComboBox)):
                        pass   
                    elif(isinstance(widget,QPushButton)):                            
                        widget.setStyleSheet("background-color:lightgray;")

   
    def Add_material_to_BOM(self):
        _ProjectCOntroller=ProjectController()
        if(self.sender()==self.btn_add_mat_S_ring):           
            _ProjectCOntroller.add_update_item(item='S.Ring',item_name="S.Ring Tray Downcomer",wt=self.tb_S_ring_plt_Wt.text(),material=self.cmbbox_S_ring_plt_material.currentText())
        elif(self.sender()==self.btn_add_mat_Bolting_Bar):           
            _ProjectCOntroller.add_update_item(item='Bolting Bar',item_name="Bolting Bar Downcomer",wt=self.tb_Bolting_Bar_plt_Wt.text(),material=self.cmbbox_Bolting_Bar_plt_material.currentText())
        self.change_button_color_green()
        
    def Calculate_btn_clicked(self):
        
        self.density=float(self.tb_density.text())*0.000001
        self.vessel_ID=float(self.tb_vessel_ID.text())
        self.is_side= True if(self.cmbbox_type_of_downcomer=="Side") else False
        self.DownComer_Data=Get_DownComer_Data(self.vessel_ID,self.is_side)
        
        self.S_ring_plt_wdth=float(self.DownComer_Data.Support_Ring_Width)+5
        self.S_ring_plt_len=round(math.pi*self.vessel_ID+500,0)
        self.S_ring_plt_thk= 6 if(self.vessel_ID<2001)  else 10
        self.No_of_trays=float(self.tb_No_of_trays.text())
        self.S_ring_plt_Wt=round(self.No_of_trays*self.S_ring_plt_len*self.S_ring_plt_wdth*self.S_ring_plt_thk*self.density,1)
        
        self.Bolting_Bar_plt_thk=self.S_ring_plt_thk
        self.Bolting_Bar_plt_wdth=float(self.DownComer_Data.Bolting_Bar_Width)+5
        self.dist_btw_trays=float(self.tb_dist_btw_trays.text())
        
        self.No_of_Bolting_bars=[0,2,4,6,8]
        self.No_of_pass=int(self.cmbbox_type_of_tray_pass_count.currentText())
        self.Bolting_Bar_plt_Wt=round(self.Bolting_Bar_plt_wdth*self.Bolting_Bar_plt_thk*self.dist_btw_trays*self.No_of_trays*self.density*self.No_of_Bolting_bars[self.No_of_pass],1)
        
        self.tb_S_ring_plt_wdth.setText(str(self.S_ring_plt_wdth))
        self.tb_S_ring_plt_len.setText(str(self.S_ring_plt_len))
        self.tb_S_ring_plt_thk.setText(str(self.S_ring_plt_thk))
        self.tb_S_ring_plt_Wt.setText(str(self.S_ring_plt_Wt))
        
        self.tb_Bolting_Bar_plt_thk.setText(str(self.Bolting_Bar_plt_thk))
        self.tb_Bolting_Bar_plt_wdth.setText(str(self.Bolting_Bar_plt_wdth))
        self.tb_Bolting_Bar_plt_Wt.setText(str(self.Bolting_Bar_plt_Wt))
        
        
     
        #self.reset_button_color_default(self.btn_add_SurfaceArea) #Reset the color of Add Material to BOM as Weight value got changed.
        
            
    def roundup_to_next100(self,num):
       return  math.ceil(num/100)*100
        
    def change_button_color_green(self):
        button = self.sender()
        button.setStyleSheet("background-color: green; color: white;")

    #This Function reset the color of "button" passed as an argument.
    def reset_button_color_default(self,button):
        #button = self.sender()
        button.setStyleSheet("")
        button.setStyleSheet("background-color:lightgrey")       

class Part2(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
            
    def InitializeUI(self):
        self.set_ui_layout() 
                      
    def set_ui_layout(self):
        self.grpbox=QGroupBox("XXXXX")
        self.grpbox.setFixedWidth(440)
        self.grpbox.setStyleSheet(set_styles.ip_grpbox1_style)        
        self.Vbox_layout=QVBoxLayout()
        self.Vbox_layout.addWidget(self.grpbox)
        self.setLayout(self.Vbox_layout)
        
        self.set_grpbox_UI()
        
        
    def set_grpbox_UI(self):
        
        #Gridlayout
        self.gridlayout=QGridLayout()
        self.grpbox.setLayout(self.gridlayout)
        
        #Input
        self.lbl_description =QLabel("Description")
        self.lbl_description.setStyleSheet("font:bold")
        self.tb_description =QLineEdit("XXXXXXXXXXX")
        self.tb_description.setStyleSheet("font:bold")
        
        self.lbl_density =QLabel("density")
        self.tb_density=QLineEdit("7.85")
        self.lbl_vessel_ID =QLabel("Vessel ID")
        self.tb_vessel_ID =QLineEdit("1900")
        self.lbl_support_size=QLabel("Support_size")
        self.tb_support_size =QLineEdit("ISA XX x XX x XX")
        
        self.lbl_No_of_supports =QLabel("No. of Supports")
        self.tb_No_of_supports = QLineEdit("XX")
       #self.tb_No_of_supports.addItems([str(i) for i in range(1,5)]) 
      
        self.lbl_Strl_spider_support_Wt=QLabel("Strl. Spider Support Weight")
        self.tb_Strl_spider_support_Wt =QLineEdit("XX")
        self.cmbbox_Strl_spider_support_material =QComboBox()
        self.cmbbox_Strl_spider_support_material.addItems(var.master_mat_list)
        self.btn_add_mat_Strl_spider_support_Wt=QPushButton("Add to BOM")
        self.btn_add_mat_Strl_spider_support_Wt.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_Support_plt_Wt=QLabel("Support Plt Weight.")       
        self.tb_Support_plt_Wt=QLineEdit("XXX")
        self.cmbbox_Support_plt_material =QComboBox()
        self.cmbbox_Support_plt_material.addItems(var.master_mat_list)
        self.btn_add_mat_Support_plt_Wt=QPushButton("Add to BOM")
        self.btn_add_mat_Support_plt_Wt.clicked.connect(self.Add_material_to_BOM)
        
      
        self.lbl_Center_plt_Wt=QLabel("Center Plate Weight")
        self.tb_Center_plt_Wt =QLineEdit("XX")
        self.lbl_Center_plt_material=QLabel("Center Plate Weight Material")
        self.cmbbox_Center_plt_material =QComboBox()
        self.cmbbox_Center_plt_material.addItems(var.master_mat_list)
        self.btn_add_mat_Center_plt=QPushButton("Add to BOM")
        self.btn_add_mat_Center_plt.clicked.connect(self.Add_material_to_BOM)
        
       
        disabled_tb_list=[self.tb_support_size,self.tb_No_of_supports,self.tb_Strl_spider_support_Wt,
                          self.tb_Support_plt_Wt,self.tb_Center_plt_Wt]
        for tb in disabled_tb_list:
            tb.setEnabled(False)
            
        material_cmbbox_list=[self.cmbbox_Support_plt_material,self.cmbbox_Center_plt_material,self.cmbbox_Strl_spider_support_material]
        for cmbbox in material_cmbbox_list:
            cmbbox.setStyleSheet("background-color:lightgreen;font:bold")
        
       
        
        self.btn_calculate_wt=QPushButton("Calculate")
        self.btn_calculate_wt.clicked.connect(self.Calculate_btn_clicked)
        
               
        #Layout
        
        a=2
        self.gridlayout.addWidget(self.lbl_description,a,0)
        self.gridlayout.addWidget(self.tb_description,a,1)
        
        a=a+1
        # self.gridlayout.addWidget(self.lbl_density,a,0)
        # self.gridlayout.addWidget(self.tb_density,a,1)
        self.gridlayout.addWidget(self.lbl_vessel_ID,a,0)
        self.gridlayout.addWidget(self.tb_vessel_ID,a,1)
        
        
        
        a=a+1
        self.gridlayout.addWidget(self.lbl_support_size,a,0)
        self.gridlayout.addWidget(self.tb_support_size,a,1)        
        self.gridlayout.addWidget(self.lbl_No_of_supports,a,2)
        self.gridlayout.addWidget(self.tb_No_of_supports,a,3)
       
        a=a+1
        self.gridlayout.addWidget(self.btn_calculate_wt,a,1,Qt.AlignmentFlag.AlignHCenter)
        
        a=a+1
        self.gridlayout.addItem(QSpacerItem(100,30),a,0)
        
        
        
          #Output Layout 
        a=a+1           
        self.gridlayout.addWidget(QLabel("Output"),a,0) 
         
        a=a+1
        self.gridlayout.addWidget(self.lbl_Strl_spider_support_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Strl_spider_support_Wt,a,1)       
        self.gridlayout.addWidget(self.cmbbox_Strl_spider_support_material,a,2)
        self.gridlayout.addWidget(self.btn_add_mat_Strl_spider_support_Wt,a,3)
        
      
        a=a+1        
        self.gridlayout.addWidget(self.lbl_Support_plt_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Support_plt_Wt,a,1) 
        self.gridlayout.addWidget(self.cmbbox_Support_plt_material,a,2)  
        self.gridlayout.addWidget(self.btn_add_mat_Support_plt_Wt,a,3)      
        
        a=a+1
        self.gridlayout.addWidget(self.lbl_Center_plt_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Center_plt_Wt,a,1) 
        self.gridlayout.addWidget(self.cmbbox_Center_plt_material,a,2) 
        self.gridlayout.addWidget(self.btn_add_mat_Center_plt,a,3)  
        
       
        self.Set_all_TextBox_Width()
        #self.btn_add_SurfaceArea.setFixedWidth(150)
        # self.btn_calculate_wt.setFixedSize(150,30) 
        self.tb_description.setFixedWidth(120)
       
        
    def Set_all_TextBox_Width(self):
        # Get the QGridLayout widget
        #layout = self.findChild(QGridLayout)

        # Iterate over all of the widgets in the QGridLayout
        for i in range(self.gridlayout.rowCount()):
            for j in range(self.gridlayout.columnCount()):
                widget_item = self.gridlayout.itemAtPosition(i, j)
                if widget_item is not None:
                    widget = widget_item.widget()
                    # If the widget is a QLineEdit widget, set its width
                    if (isinstance(widget, QLineEdit) ):
                        widget.setFixedWidth(100)
                    if (isinstance(widget,QComboBox)):
                        pass   
                    elif(isinstance(widget,QPushButton)):                            
                        widget.setStyleSheet("background-color:lightgray;")

   
    def Add_material_to_BOM(self):
        _ProjectCOntroller=ProjectController()
        if(self.sender()==self.btn_add_mat_Strl_spider_support_Wt):           
            _ProjectCOntroller.add_update_item(item='Strl Spider Plt for Tranportaion',item_name="Strl Spider Plt for Tranportaion",wt=self.tb_Strl_spider_support_Wt.text(),material=self.cmbbox_Strl_spider_support_material.currentText())
        elif(self.sender()==self.btn_add_mat_Support_plt_Wt):           
            _ProjectCOntroller.add_update_item(item='Support Plate for Transportaion',item_name="Support Plate for Transportaion",wt=self.tb_Support_plt_Wt.text(),material=self.cmbbox_Support_plt_material.currentText())
        elif(self.sender()==self.btn_add_mat_Center_plt):           
            _ProjectCOntroller.add_update_item(item='Center Plate for Transportaion',item_name="Center Plate for Transportaion",wt=self.tb_Center_plt_Wt.text(),material=self.cmbbox_Center_plt_material.currentText())
        self.change_button_color_green()
        
    def Calculate_btn_clicked(self):
        
        self.Vessel_ID=float(self.tb_vessel_ID.text())
        self.Supoort_size= "ISA 80 x 80 x 8" if(self.Vessel_ID<2000) else "ISA 100 x 100 x 10"
        self.No_of_supports= 2 if( self.Vessel_ID<2000) else 4
        self.Strl_strip_support_Wt= round(9.6*self.Vessel_ID*2/1000,1) if(self.Vessel_ID<2000) else round(self.Vessel_ID*14.9*4/1000,1)
        self.Support_plt_Wt=round(10*200*200*self.No_of_supports*2*0.00000785,1)
        self.Center_plt_Wt= 0 if( self.Vessel_ID<2000) else round(10*0.5*0.5*7.85,1)
        
        self.tb_support_size.setText(self.Supoort_size)
        self.tb_No_of_supports.setText(str(self.No_of_supports))
        self.tb_Strl_spider_support_Wt.setText(str(self.Strl_strip_support_Wt))
        self.tb_Support_plt_Wt.setText(str(self.Support_plt_Wt))
        self.tb_Center_plt_Wt.setText(str(self.Center_plt_Wt))
        
     
        #self.reset_button_color_default(self.btn_add_SurfaceArea) #Reset the color of Add Material to BOM as Weight value got changed.
        
            
    def roundup_to_next100(self,num):
       return  math.ceil(num/100)*100
        
    def change_button_color_green(self):
        button = self.sender()
        button.setStyleSheet("background-color: green; color: white;")

    #This Function reset the color of "button" passed as an argument.
    def reset_button_color_default(self,button):
        #button = self.sender()
        button.setStyleSheet("")
        button.setStyleSheet("background-color:lightgrey")       

class Pipe_Devit(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
            
    def InitializeUI(self):
        self.set_ui_layout() 
                      
    def set_ui_layout(self):        
        self.grpbox=QGroupBox("Pipe Devit")
        self.grpbox.setFixedWidth(440)
        self.grpbox.setStyleSheet(set_styles.ip_grpbox1_style)        
        self.Vbox_layout=QVBoxLayout()
        self.Vbox_layout.addWidget(self.grpbox)
        self.setLayout(self.Vbox_layout)
        
        self.set_grpbox_UI()
        
        
    def set_grpbox_UI(self):
        
        #Gridlayout
        #Gridlayout
        self.gridlayout=QGridLayout()
        self.grpbox.setLayout(self.gridlayout)
        
        #Input
        self.lbl_description =QLabel("Description")
        self.lbl_description.setStyleSheet("font:bold")
        self.tb_description =QLineEdit("Pipe Devit")
        self.tb_description.setStyleSheet("font:bold")
        
        self.lbl_devit_capacity=QLabel("Devit Capacity(Kg)")
        self.cmbbox_devit_capacity=QComboBox()
        self.cmbbox_devit_capacity.addItems(["500","1000"])
        self.lbl_A=QLabel("Horz Dimension")
        self.tb_A=QLineEdit("1000")
        self.lbl_B=QLabel("Top Vert. Dim.")
        self.tb_B=QLineEdit("3000")
        self.lbl_C=QLabel("Bottom Vert. Dim.")
        self.tb_C=QLineEdit("1000")
        self.lbl_Pipe_size=QLabel("Pipe Size")        
        self.tb_Pipe_size=QLineEdit("---NB X SCH--")
        self.lbl_Pipe_size=QLabel("Pipe Size")
        
        self.lbl_Pipe_Wt=QLabel("Pipe Weight.")       
        self.tb_Pipe_Wt=QLineEdit("XXX")
        self.cmbbox_Pipe_material =QComboBox()
        self.cmbbox_Pipe_material.addItems(var.master_mat_list)
        self.btn_add_mat_Pipe_Wt=QPushButton("Add to BOM")
        self.btn_add_mat_Pipe_Wt.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_Angle_Wt=QLabel("Pipe Weight.")       
        self.tb_Angle_Wt=QLineEdit("XXX")
        self.cmbbox_Angle_material =QComboBox()
        self.cmbbox_Angle_material.addItems(var.master_mat_list)
        self.btn_add_mat_Angle_Wt=QPushButton("Add to BOM")
        self.btn_add_mat_Angle_Wt.clicked.connect(self.Add_material_to_BOM)
        
        
        disabled_tb_list=[self.tb_Pipe_size,self.tb_Pipe_Wt,self.tb_Angle_Wt]
        for tb in disabled_tb_list:
            tb.setEnabled(False)
            
        material_cmbbox_list=[self.cmbbox_Pipe_material,self.cmbbox_Angle_material]
        for cmbbox in material_cmbbox_list:
            cmbbox.setStyleSheet("background-color:lightgreen;font:bold")
        
       
        
        self.btn_calculate_wt=QPushButton("Calculate")
        self.btn_calculate_wt.clicked.connect(self.Calculate_btn_clicked)
        
          
        a=0
        self.gridlayout.addWidget(self.lbl_description,a,0)
        self.gridlayout.addWidget(self.tb_description,a,1)
        
        a+=1 
        self.gridlayout.addWidget(self.lbl_devit_capacity,a,0)
        self.gridlayout.addWidget(self.cmbbox_devit_capacity,a,1)
        
        a+=1
        self.gridlayout.addWidget(self.lbl_A,a,0)
        self.gridlayout.addWidget(self.tb_A,a,1)        
        self.gridlayout.addWidget(self.lbl_B,a,2)
        self.gridlayout.addWidget(self.tb_B,a,3)
        
        a+=1
        self.gridlayout.addWidget(self.lbl_C,a,0)
        self.gridlayout.addWidget(self.tb_C,a,1)
        self.gridlayout.addWidget(self.lbl_Pipe_size,a,2)
        self.gridlayout.addWidget(self.tb_Pipe_size,a,3)
        
        a+=1
        self.gridlayout.addItem(QSpacerItem(100,30),a,0)
        
        a+=1
        self.gridlayout.addWidget(self.btn_calculate_wt,a,1,Qt.AlignmentFlag.AlignHCenter)
        
        a+=1
        self.gridlayout.addItem(QSpacerItem(100,30),a,0)
        
        a+=1
        self.gridlayout.addWidget(self.lbl_Pipe_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Pipe_Wt,a,1)
        self.gridlayout.addWidget(self.cmbbox_Pipe_material,a,2)
        self.gridlayout.addWidget(self.btn_add_mat_Pipe_Wt,a,3)
        
        a+=1
        self.gridlayout.addWidget(self.lbl_Angle_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Angle_Wt,a,1)
        self.gridlayout.addWidget(self.cmbbox_Angle_material,a,2)
        self.gridlayout.addWidget(self.btn_add_mat_Angle_Wt,a,3)
        
        a+=1
        self.gridlayout.addItem(QSpacerItem(100,30),a,0)
          
        self.Set_all_TextBox_Width()         
        self.tb_description.setFixedWidth(120)
       
        
    def Set_all_TextBox_Width(self):
        # Get the QGridLayout widget
        #layout = self.findChild(QGridLayout)

        # Iterate over all of the widgets in the QGridLayout
        for i in range(self.gridlayout.rowCount()):
            for j in range(self.gridlayout.columnCount()):
                widget_item = self.gridlayout.itemAtPosition(i, j)
                if widget_item is not None:
                    widget = widget_item.widget()
                    # If the widget is a QLineEdit widget, set its width
                    if (isinstance(widget, QLineEdit) ):
                        widget.setFixedWidth(100)
                    if (isinstance(widget,QComboBox)):
                        pass   
                    elif(isinstance(widget,QPushButton)):                            
                        widget.setStyleSheet("background-color:lightgray;")

   
    def Add_material_to_BOM(self):
        _ProjectCOntroller=ProjectController()
        if(self.sender()==self.btn_add_mat_Pipe_Wt):           
            _ProjectCOntroller.add_update_item(item='Pipe Devit',item_name="Pipe Devit",wt=self.tb_Pipe_Wt.text(),material=self.cmbbox_Pipe_material.currentText())
        elif(self.sender()==self.btn_add_mat_Angle_Wt):           
            _ProjectCOntroller.add_update_item(item='Angle Devit',item_name="Angle Devit",wt=self.tb_Angle_Wt.text(),material=self.cmbbox_Angle_material.currentText())
        
        self.change_button_color_green()
    def Calculate_btn_clicked(self):
        
        from Controller.project_controller import Get_Pipe1_Data,Get_Elbow_Details
        try:
            self.A= int(self.tb_A.text())
            self.B= int(self.tb_B.text())
            self.C= int(self.tb_C.text())
            
            self.Pipe_Detail=Get_Pipe1_Data(self.A,self.C)
            self.Pipe_Size=self.Pipe_Detail.Pipe_Size
            
            self.NPS,self.SCHEDULE=[re.sub(r"[^\d]", "", a.strip()) for a in str.split(self.Pipe_Size, 'X')]
            self.Elbow_Detail=Get_Elbow_Details(self.NPS,self.SCHEDULE)
            self.Pipe_Wt=math.ceil((float(self.Elbow_Detail.WtPerMtr))*(self.A+self.B+self.C)*1.2/1000)            
            self.Angle_Wt=round(math.ceil((self.A/2)*math.sqrt(2)*1.1*float(self.Pipe_Detail.Ang_Wt))/1000,1)
            
            self.tb_Pipe_size.setText(self.Pipe_Size)
            self.tb_Pipe_Wt.setText(str(self.Pipe_Wt))
            self.tb_Angle_Wt.setText(str(self.Angle_Wt))
        except Exception as e:
            raise e
        # end try
        
        
        
     
        #self.reset_button_color_default(self.btn_add_SurfaceArea) #Reset the color of Add Material to BOM as Weight value got changed.
        
            
    def roundup_to_next100(self,num):
       return  math.ceil(num/100)*100
        
    def change_button_color_green(self):
        button = self.sender()
        button.setStyleSheet("background-color: green; color: white;")

    #This Function reset the color of "button" passed as an argument.
    def reset_button_color_default(self,button):
        #button = self.sender()
        button.setStyleSheet("")
        button.setStyleSheet("background-color:lightgrey")       
         
        
class ManHole_Devit(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
            
    def InitializeUI(self):
        self.set_ui_layout() 
                      
    def set_ui_layout(self):        
        self.grpbox=QGroupBox("ManHole Devit")
        self.grpbox.setFixedWidth(440)
        self.grpbox.setStyleSheet(set_styles.ip_grpbox1_style)        
        self.Vbox_layout=QVBoxLayout()
        self.Vbox_layout.addWidget(self.grpbox)
        self.setLayout(self.Vbox_layout)
        
        self.set_grpbox_UI()
        
        
    def set_grpbox_UI(self):
        
        #Gridlayout
        #Gridlayout
        self.gridlayout=QGridLayout()
        self.grpbox.setLayout(self.gridlayout)
        
        #Input
        self.lbl_description =QLabel("Description")
        self.lbl_description.setStyleSheet("font:bold")
        self.tb_description =QLineEdit("ManHole Devit")
        self.tb_description.setStyleSheet("font:bold")
        
        self.lbl_class=QLabel("Class")
        self.cmbbox_class=QComboBox()
        self.cmbbox_class.addItems(["150","300","600","900"])
        self.lbl_NPS=QLabel("NPS")
        self.cmbbox_NPS=QComboBox()
        self.cmbbox_NPS.addItems(["400","450","500","600"])
        self.lbl_No_of_Manhole=QLabel("No. of ManHoles")       
        self.tb_No_of_Manhole=QLineEdit("3")
        
        
        self.lbl_pipe1_size=QLabel("PIPE 1 SIZE")
        self.tb_pipe1_size=QLineEdit("---NB X SCH --")
        self.lbl_pipe2_size=QLabel("PIPE 2 SIZE")
        self.tb_pipe2_size=QLineEdit("80")
       
        
        self.lbl_Pipe1_Wt=QLabel("Pipe 1 Weight.")       
        self.tb_Pipe1_Wt=QLineEdit("XXX")
        self.cmbbox_Pipe1_material =QComboBox()
        self.cmbbox_Pipe1_material.addItems(var.master_mat_list)
        self.btn_add_mat_Pipe1_Wt=QPushButton("Add to BOM")
        self.btn_add_mat_Pipe1_Wt.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_Pipe2_Wt=QLabel("Pipe Weight.")       
        self.tb_Pipe2_Wt=QLineEdit("XXX")
        self.cmbbox_Pipe2_material =QComboBox()
        self.cmbbox_Pipe2_material.addItems(var.master_mat_list)
        self.btn_add_mat_Pipe2_Wt=QPushButton("Add to BOM")
        self.btn_add_mat_Pipe2_Wt.clicked.connect(self.Add_material_to_BOM)
        
        
        disabled_tb_list=[self.tb_pipe1_size,self.tb_pipe2_size,self.tb_Pipe1_Wt,self.tb_Pipe2_Wt]
        for tb in disabled_tb_list:
            tb.setEnabled(False)
            
        material_cmbbox_list=[self.cmbbox_Pipe1_material,self.cmbbox_Pipe2_material]
        for cmbbox in material_cmbbox_list:
            cmbbox.setStyleSheet("background-color:lightgreen;font:bold")
        
       
        
        self.btn_calculate_wt=QPushButton("Calculate")
        self.btn_calculate_wt.clicked.connect(self.Calculate_btn_clicked)
        
          
        a=0
        self.gridlayout.addWidget(self.lbl_description,a,0)
        self.gridlayout.addWidget(self.tb_description,a,1)
        
        a+=1 
        self.gridlayout.addWidget(self.lbl_class,a,0)
        self.gridlayout.addWidget(self.cmbbox_class,a,1)        
        self.gridlayout.addWidget(self.lbl_NPS,a,2)
        self.gridlayout.addWidget(self.cmbbox_NPS,a,3) 
        
        a+=1
        self.gridlayout.addItem(QSpacerItem(100,30),a,0)
        
        a+=1
        self.gridlayout.addWidget(self.btn_calculate_wt,a,1,Qt.AlignmentFlag.AlignHCenter)
        
        a+=1
        self.gridlayout.addItem(QSpacerItem(100,30),a,0)
        
        self.gridlayout.addWidget(self.lbl_pipe1_size,a,0)
        self.gridlayout.addWidget(self.tb_pipe1_size,a,1)       
        self.gridlayout.addWidget(self.lbl_pipe2_size,a,2)
        self.gridlayout.addWidget(self.tb_pipe2_size,a,3)
        
        a+=1
        self.gridlayout.addWidget(self.lbl_Pipe1_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Pipe1_Wt,a,1)
        self.gridlayout.addWidget(self.cmbbox_Pipe1_material,a,2)
        self.gridlayout.addWidget(self.btn_add_mat_Pipe1_Wt,a,3)
        
        a+=1
        self.gridlayout.addWidget(self.lbl_Pipe2_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Pipe2_Wt,a,1)
        self.gridlayout.addWidget(self.cmbbox_Pipe2_material,a,2)
        self.gridlayout.addWidget(self.btn_add_mat_Pipe2_Wt,a,3)
        
       
        a+=1
        self.gridlayout.addItem(QSpacerItem(100,30),a,0)
        
        a+=1
        self.gridlayout.addWidget(self.lbl_Pipe1_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Pipe1_Wt,a,1)
        self.gridlayout.addWidget(self.cmbbox_Pipe1_material,a,2)
        self.gridlayout.addWidget(self.btn_add_mat_Pipe1_Wt,a,3)
        
        a+=1
        self.gridlayout.addWidget(self.lbl_Pipe2_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Pipe2_Wt,a,1)
        self.gridlayout.addWidget(self.cmbbox_Pipe2_material,a,2)
        self.gridlayout.addWidget(self.btn_add_mat_Pipe2_Wt,a,3)
        
          
        self.Set_all_TextBox_Width()         
        self.tb_description.setFixedWidth(120)
       
        
    def Set_all_TextBox_Width(self):
        # Get the QGridLayout widget
        #layout = self.findChild(QGridLayout)

        # Iterate over all of the widgets in the QGridLayout
        for i in range(self.gridlayout.rowCount()):
            for j in range(self.gridlayout.columnCount()):
                widget_item = self.gridlayout.itemAtPosition(i, j)
                if widget_item is not None:
                    widget = widget_item.widget()
                    # If the widget is a QLineEdit widget, set its width
                    if (isinstance(widget, QLineEdit) ):
                        widget.setFixedWidth(100)
                    if (isinstance(widget,QComboBox)):
                        pass   
                    elif(isinstance(widget,QPushButton)):                            
                        widget.setStyleSheet("background-color:lightgray;")

   
    def Add_material_to_BOM(self):
        _ProjectCOntroller=ProjectController()
        if(self.sender()==self.btn_add_mat_Pipe1_Wt):           
            _ProjectCOntroller.add_update_item(item='Pipe1 Devit Manhole',item_name="Pipe1 Devit Manhole",wt=self.tb_Pipe1_Wt.text(),material=self.cmbbox_Pipe1_material.currentText())
        elif(self.sender()==self.btn_add_mat_Pipe2_Wt):           
            _ProjectCOntroller.add_update_item(item='Pipe2 Devit Manhole',item_name="Pipe2 Devit Manhole",wt=self.tb_Pipe2_Wt.text(),material=self.cmbbox_Pipe2_material.currentText())
        self.change_button_color_green()
        
    def Calculate_btn_clicked(self):
        
        from Controller.project_controller import Get_Pipe2_Data,Get_Elbow_Details
        try:
            self.No_of_Manhole=int(self.tb_No_of_Manhole.text())
            self.Classs= int(self.cmbbox_class.currentText())
            self.NPS= int(self.cmbbox_NPS.currentText())
            
            
            self.Pipe_Detail=Get_Pipe2_Data(self.Classs,self.NPS)
            self.Pipe1_Size=self.Pipe_Detail.Pipe
            self.elbow1_NPS,self.elbow1_SCHEDULE=[int(re.sub(r"[^\d]", "", a.strip())) for a in str.split(self.Pipe1_Size, 'X')]           
            self.Elbow1_Detail=Get_Elbow_Details(self.elbow1_NPS,self.elbow1_SCHEDULE)         
            self.Pipe1_Wt=round(math.ceil(float(self.Elbow1_Detail.WtPerMtr)*(200+50)*1.2/1000)*2*self.No_of_Manhole,1) 
            
            self.Pipe2_Size=int(self.Pipe_Detail.B)
            self.elbow2_NPS=self.Pipe2_Size
            self.elbow2_SCHEDULE=self.elbow1_SCHEDULE
            self.Elbow2_Detail=Get_Elbow_Details(self.elbow2_NPS,self.elbow2_SCHEDULE) 
            self.Pipe2_Wt=round(math.ceil(float(self.Elbow2_Detail.WtPerMtr)*(1500)*1.2/1000)*1.8*self.No_of_Manhole,1)
            
            self.tb_pipe1_size.setText(self.Pipe1_Size)
            self.tb_Pipe1_Wt.setText(str(self.Pipe1_Wt))
            self.tb_Pipe2_Wt.setText(str(self.Pipe2_Wt))
        except Exception as e:
            raise e
        # end try
        
        
        
     
        #self.reset_button_color_default(self.btn_add_SurfaceArea) #Reset the color of Add Material to BOM as Weight value got changed.
        
            
    def roundup_to_next100(self,num):
       return  math.ceil(num/100)*100
        
    def change_button_color_green(self):
        button = self.sender()
        button.setStyleSheet("background-color: green; color: white;")

    #This Function reset the color of "button" passed as an argument.
    def reset_button_color_default(self,button):
        #button = self.sender()
        button.setStyleSheet("")
        button.setStyleSheet("background-color:lightgrey")       
         
                
        
        
        
        
        

class set_styles:    
    op_vbox_style="""
                QVBoxLayout {
                    font: bold;
                    font-size:14px;
                    padding: 5px;
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
                    padding: 5px;
                    border: 1px solid silver;
                    border-radius: 6px;
                    background-color:#ccffcc
                                        
                }
                          
                """


