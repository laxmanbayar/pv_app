
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QLayout, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout,QWidget, \
    QTabWidget,QGroupBox,QTableWidget,QTableWidgetItem,QGridLayout,QScrollArea,QSpacerItem
from Variables import var
from PyQt6.QtCore import Qt,QRect
import math
from Controller.project_controller import ProjectController,Get_Shell_ODs_from_Saddle_Data,Get_Saddle_Data,Get_Saddle_Dim_Data,Get_Vessel_Data

class Tab_WireMesh_Demister(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
        
    def InitializeUI(self):
       
        
        self.Vbox_layout=QVBoxLayout()
        type_A= Type_A()
        type_B=Type_B()
        
        self.Vbox_layout.addWidget(type_A)
        self.Vbox_layout.addWidget(type_B)
        
       
       
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
        
        
        
class Type_A(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
            
    def InitializeUI(self):
        self.set_ui_layout() 
                      
    def set_ui_layout(self):
        self.grpbox=QGroupBox("Type A")
        self.grpbox.setFixedWidth(850)
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
        self.tb_description =QLineEdit("Type-A Wiremesh Demister ")
        self.tb_description.setStyleSheet("font:bold")
        
        self.lbl_shell_ID =QLabel("Shell ID")
        self.tb_shell_ID =QLineEdit("1000")
        self.lb_material =QLabel("Material")
        self.cmbbox_material = QComboBox()
        self.cmbbox_material.addItems(["CS","SS"]) 
        self.lbl_corrosion_allwnc=QLabel("Corrosion allwnc")
        self.tb_corrosion_allwnc =QLineEdit("6")
        
        
        self.lbl_No_of_Beam=QLabel("No. of Beam")
        self.tb_No_of_Beam =QLineEdit("00")
        self.lbl_total_Beam_len=QLabel("Total Beam Length")
        self.tb_total_Beam_len =QLineEdit("00")
        self.lbl_Web_ht=QLabel("Web Height")
        self.tb_Web_ht =QLineEdit("00")
        self.lbl_Web_wdth=QLabel("Web Width")
        self.tb_Web_wdth =QLineEdit("150")
        
        self.lbl_thk=QLabel("Thkiness")
        self.tb_thk =QLineEdit("18")
        self.lbl_Ring_ht=QLabel("Ring Height")
        self.tb_Ring_ht =QLineEdit("50")
        self.lbl_Ring_thk=QLabel("Ring Thk")
        self.tb_Ring_thk =QLineEdit("18")
        
        self.btn_calculate_wt=QPushButton("Calculate")
        self.btn_calculate_wt.clicked.connect(self.Calculate_btn_clicked)
        
               
        self.lbl_Beam_Wt=QLabel("Beam Weight")
        self.tb_Beam_Wt = QLineEdit("XX") 
        self.tb_Beam_Wt.setEnabled(False)         
        self.lbl_Beam_material=QLabel("Beam Material")
        self.cmbbox_Beam_material=QComboBox()
        self.cmbbox_Beam_material.addItems(var.master_mat_list)
        self.btn_add_mat_Beam=QPushButton("Add to BOM")
        self.btn_add_mat_Beam.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_Ring_and_Stiffner_Wt=QLabel("Ring & Stiffner Weight")
        self.tb_Ring_and_Stiffner_Wt = QLineEdit("XX") 
        self.tb_Ring_and_Stiffner_Wt.setEnabled(False)         
        self.lbl_Ring_and_Stiffner_material=QLabel("Ring & Stiffner Material")
        self.cmbbox_Ring_and_Stiffner_material=QComboBox()
        self.cmbbox_Ring_and_Stiffner_material.addItems(var.master_mat_list)
        self.btn_add_mat_Ring_and_Stiffner=QPushButton("Add to BOM")
        self.btn_add_mat_Ring_and_Stiffner.clicked.connect(self.Add_material_to_BOM)
        
               
        #Layout
        
        
        a=2
        self.gridlayout.addWidget(self.lbl_description,a,2)
        self.gridlayout.addWidget(self.tb_description,a,3)
        
        a=a+2
        self.gridlayout.addWidget(self.lbl_shell_ID,a,0)
        self.gridlayout.addWidget(self.tb_shell_ID,a,1)
        self.gridlayout.addWidget(self.lb_material,a,2)
        self.gridlayout.addWidget(self.cmbbox_material,a,3)
        self.gridlayout.addWidget(self.lbl_corrosion_allwnc,a,4)
        self.gridlayout.addWidget(self.tb_corrosion_allwnc,a,5)
        
        a=a+1
        self.gridlayout.addWidget(self.lbl_No_of_Beam,a,0)
        self.gridlayout.addWidget(self.tb_No_of_Beam,a,1)       
        self.gridlayout.addWidget(self.lbl_total_Beam_len,a,2)
        self.gridlayout.addWidget(self.tb_total_Beam_len,a,3)
        self.gridlayout.addWidget(self.lbl_Web_ht,a,4)
        self.gridlayout.addWidget(self.tb_Web_ht,a,5)
        self.gridlayout.addWidget(self.lbl_Web_wdth,a,6)
        self.gridlayout.addWidget(self.tb_Web_wdth,a,7)
        
        a=a+1
        self.gridlayout.addWidget(self.lbl_thk,a,0)
        self.gridlayout.addWidget(self.tb_thk,a,1)
        self.gridlayout.addWidget(self.lbl_Ring_ht,a,2)
        self.gridlayout.addWidget(self.tb_Ring_ht,a,3)
        self.gridlayout.addWidget(self.lbl_Ring_thk,a,4)
        self.gridlayout.addWidget(self.tb_Ring_thk,a,5)
        
        a=a+1
        self.gridlayout.addItem(QSpacerItem(100,30),a,0)
        a=a+1
        self.gridlayout.addWidget(self.btn_calculate_wt,a,2,Qt.AlignmentFlag.AlignHCenter)

        #Output Layout 
        a=a+1           
        self.gridlayout.addWidget(QLabel("Output"),a,0) 
           
        a=a+1       
        self.gridlayout.addWidget(self.lbl_Beam_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Beam_Wt,a,1)
        self.gridlayout.addWidget(self.lbl_Beam_material,a,2)
        self.gridlayout.addWidget(self.cmbbox_Beam_material,a,3)
        self.gridlayout.addWidget(self.btn_add_mat_Beam,a,4)
        
        a=a+1       
        self.gridlayout.addWidget(self.lbl_Ring_and_Stiffner_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Ring_and_Stiffner_Wt,a,1)
        self.gridlayout.addWidget(self.lbl_Ring_and_Stiffner_material,a,2)
        self.gridlayout.addWidget(self.cmbbox_Ring_and_Stiffner_material,a,3)
        self.gridlayout.addWidget(self.btn_add_mat_Ring_and_Stiffner,a,4)
        
        
       
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
        if(self.sender()==self.btn_add_mat_Beam):           
            _ProjectCOntroller.add_update_item(item='Beam WireMesh-Demist',item_name="Beam WireMesh-Demist",wt=self.tb_Beam_Wt.text(),material=self.cmbbox_Beam_material.currentText())
        elif(self.sender()==self.btn_add_mat_Ring_and_Stiffner):           
            _ProjectCOntroller.add_update_item(item='Ring & Stiffner WireMesh-Demist',item_name="Ring & Stiffner WireMesh-Demist",wt=self.tb_Ring_and_Stiffner_Wt.text(),material=self.cmbbox_Ring_and_Stiffner_material.currentText())
        self.change_button_color_green()
        
    def Calculate_btn_clicked(self):
        
        # Database Table Missing
        # Read from Database ...below parameters
        # No. of Beams,Total Beam Length (L),
        # Height of Web (H),Thickness (T), Ring Thickness
        
        self.Beam_Wt=(float(self.tb_total_Beam_len.text()))*\
                    (float(self.tb_Web_ht.text()) + 2*float(self.tb_Web_wdth.text()))* \
                    (float(self.tb_thk.text()))*0.00000789 \
                    if (self.cmbbox_material.currentText()=='CS')  \
                    else  (float(self.tb_total_Beam_len.text()))*\
                    (float(self.tb_Web_ht.text()) + 2*float(self.tb_Web_wdth.text()))* \
                    (float(self.tb_thk.text()))*0.00000789
        self.Beam_Wt=round(self.Beam_Wt,1)
        self.tb_Beam_Wt.setText(str(self.Beam_Wt))
        
        self.Rib_and_Stiffner_Wt=math.pi*(float(self.tb_shell_ID.text()))*(float(self.tb_Ring_ht.text()))*(float(self.tb_Ring_thk.text()))*0.00000786   
        self.Rib_and_Stiffner_Wt=round(self.Rib_and_Stiffner_Wt,1)         
        self.tb_Ring_and_Stiffner_Wt.setText(str(self.Rib_and_Stiffner_Wt))                
       
     
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

class Type_B(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
            
    def InitializeUI(self):
        self.set_ui_layout() 
                      
    def set_ui_layout(self):
        self.grpbox=QGroupBox("Type B")
        self.grpbox.setFixedWidth(850)
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
        self.tb_description =QLineEdit("Type-A Wiremesh Demister ")
        self.tb_description.setStyleSheet("font:bold")
        
        self.lbl_shell_ID =QLabel("Shell ID")
        self.tb_shell_ID =QLineEdit("1000")
        self.lb_material =QLabel("Material")
        self.cmbbox_material = QComboBox()
        self.cmbbox_material.addItems(["SS","CS"]) 
        self.lbl_corrosion_allwnc=QLabel("Corrosion allwnc")
        self.tb_corrosion_allwnc =QLineEdit("1.5")
        
        
        self.lbl_No_of_Beam=QLabel("No. of Beam")
        self.tb_No_of_Beam =QLineEdit("00")
        self.lbl_total_Beam_len=QLabel("Total Beam Length")
        self.tb_total_Beam_len =QLineEdit("00")
        self.lbl_Web_ht=QLabel("Web Height")
        self.tb_Web_ht =QLineEdit("00")
        self.lbl_Web_wdth=QLabel("Web Width")
        self.tb_Web_wdth =QLineEdit("150")
        
        self.lbl_thk=QLabel("Thkiness")
        self.tb_thk =QLineEdit("9")
        self.lbl_removeable_through=QLabel("Removable Through")
        self.cmbbox_removeable_through=QComboBox()
        self.cmbbox_removeable_through.addItems(["Bottom","Top"])
        
        self.lbl_Ring_ht=QLabel("Ring/Demister Height")
        self.tb_Ring_ht =QLineEdit("50")
        self.lbl_Ring_thk=QLabel("Ring Thk")
        self.tb_Ring_thk =QLineEdit("6")
        
        self.lbl_Flat_ring_ID=QLabel("Flat Ring ID")
        self.tb_Flat_ring_ID =QLineEdit("XX")
        self.tb_Flat_ring_ID.setEnabled(False)
        self.lbl_Flat_ring_OD=QLabel("Flat Ring OD")
        self.tb_Flat_ring_OD =QLineEdit(self.tb_shell_ID.text())
        self.tb_Flat_ring_OD.setEnabled(False)
        self.lbl_Flat_ring_No_of_joints=QLabel("Flat Ring No. of Joints")
        self.tb_Flat_ring_No_of_joints =QLineEdit("7")
        self.lbl_Flat_ring_plt_width=QLabel("Flat Ring Plt Width")
        self.tb_Flat_ring_plt_width =QLineEdit("XX")
        self.tb_Flat_ring_plt_width.setEnabled(False)
        self.lbl_Flat_ring_plt_length=QLabel("Flat Ring Plt Length")
        self.tb_Flat_ring_plt_length =QLineEdit("XX")
        self.tb_Flat_ring_plt_length.setEnabled(False)
        
        self.btn_calculate=QPushButton("Calculate")
        self.btn_calculate.clicked.connect(self.Calculate_btn_clicked)
        
               
        self.lbl_Beam_Wt=QLabel("Beam Weight")
        self.tb_Beam_Wt = QLineEdit("XX") 
        self.tb_Beam_Wt.setEnabled(False)         
        self.lbl_Beam_material=QLabel("Beam Material")
        self.cmbbox_Beam_material=QComboBox()
        self.cmbbox_Beam_material.addItems(var.master_mat_list)
        self.btn_add_mat_Beam=QPushButton("Add to BOM")
        self.btn_add_mat_Beam.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_Ring_and_Stiffner_Wt=QLabel("Ring & Stiffner Weight")
        self.tb_Ring_and_Stiffner_Wt = QLineEdit("XX") 
        self.tb_Ring_and_Stiffner_Wt.setEnabled(False)         
        self.lbl_Ring_and_Stiffner_material=QLabel("Ring & Stiffner Material")
        self.cmbbox_Ring_and_Stiffner_material=QComboBox()
        self.cmbbox_Ring_and_Stiffner_material.addItems(var.master_mat_list)
        self.btn_add_mat_Ring_and_Stiffner=QPushButton("Add to BOM")
        self.btn_add_mat_Ring_and_Stiffner.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_Flat_ring_Wt=QLabel("Flat Ring Weight")
        self.tb_Flat_ring_Wt = QLineEdit("XX") 
        self.tb_Flat_ring_Wt.setEnabled(False)         
        self.lbl_Flat_ring_material=QLabel("Flat Ring Material")
        self.cmbbox_Flat_ring_material=QComboBox()
        self.cmbbox_Flat_ring_material.addItems(var.master_mat_list)
        self.btn_add_mat_Flat_ring=QPushButton("Add to BOM")
        self.btn_add_mat_Flat_ring.clicked.connect(self.Add_material_to_BOM)
        
               
        #Layout
        
        
        a=2
        self.gridlayout.addWidget(self.lbl_description,a,2)
        self.gridlayout.addWidget(self.tb_description,a,3)
        
        a=a+2
        self.gridlayout.addWidget(self.lbl_shell_ID,a,0)
        self.gridlayout.addWidget(self.tb_shell_ID,a,1)
        self.gridlayout.addWidget(self.lb_material,a,2)
        self.gridlayout.addWidget(self.cmbbox_material,a,3)
        self.gridlayout.addWidget(self.lbl_corrosion_allwnc,a,4)
        self.gridlayout.addWidget(self.tb_corrosion_allwnc,a,5)
        
        a=a+1
        self.gridlayout.addWidget(self.lbl_No_of_Beam,a,0)
        self.gridlayout.addWidget(self.tb_No_of_Beam,a,1)       
        self.gridlayout.addWidget(self.lbl_total_Beam_len,a,2)
        self.gridlayout.addWidget(self.tb_total_Beam_len,a,3)
        self.gridlayout.addWidget(self.lbl_Web_ht,a,4)
        self.gridlayout.addWidget(self.tb_Web_ht,a,5)
        self.gridlayout.addWidget(self.lbl_Web_wdth,a,6)
        self.gridlayout.addWidget(self.tb_Web_wdth,a,7)
        
        a=a+1
        self.gridlayout.addWidget(self.lbl_thk,a,0)
        self.gridlayout.addWidget(self.tb_thk,a,1)
        self.gridlayout.addWidget(self.lbl_removeable_through,a,2)
        self.gridlayout.addWidget(self.cmbbox_removeable_through,a,3)
        self.gridlayout.addWidget(self.lbl_Ring_ht,a,4)
        self.gridlayout.addWidget(self.tb_Ring_ht,a,5)
        self.gridlayout.addWidget(self.lbl_Ring_thk,a,6)
        self.gridlayout.addWidget(self.tb_Ring_thk,a,7)
        
        a=a+1
        self.gridlayout.addWidget(self.lbl_Flat_ring_OD,a,0)
        self.gridlayout.addWidget(self.tb_Flat_ring_OD,a,1)
        self.gridlayout.addWidget(self.lbl_Flat_ring_ID,a,2)
        self.gridlayout.addWidget(self.tb_Flat_ring_ID,a,3)
        self.gridlayout.addWidget(self.lbl_Flat_ring_No_of_joints,a,4)
        self.gridlayout.addWidget(self.tb_Flat_ring_No_of_joints,a,5)
        self.gridlayout.addWidget(self.lbl_Flat_ring_plt_width,a,6)
        self.gridlayout.addWidget(self.tb_Flat_ring_plt_width,a,7)
        
        a=a+1
        self.gridlayout.addWidget(self.lbl_Flat_ring_plt_length,a,0)
        self.gridlayout.addWidget(self.tb_Flat_ring_plt_length,a,1)
        
        a=a+1
        self.gridlayout.addItem(QSpacerItem(100,30),a,0)
        a=a+1
        self.gridlayout.addWidget(self.btn_calculate,a,2,Qt.AlignmentFlag.AlignHCenter)

        #Output Layout 
        a=a+1           
        self.gridlayout.addWidget(QLabel("Output"),a,0) 
           
        a=a+1       
        self.gridlayout.addWidget(self.lbl_Beam_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Beam_Wt,a,1)
        self.gridlayout.addWidget(self.lbl_Beam_material,a,2)
        self.gridlayout.addWidget(self.cmbbox_Beam_material,a,3)
        self.gridlayout.addWidget(self.btn_add_mat_Beam,a,4)
        
        a=a+1       
        self.gridlayout.addWidget(self.lbl_Ring_and_Stiffner_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Ring_and_Stiffner_Wt,a,1)
        self.gridlayout.addWidget(self.lbl_Ring_and_Stiffner_material,a,2)
        self.gridlayout.addWidget(self.cmbbox_Ring_and_Stiffner_material,a,3)
        self.gridlayout.addWidget(self.btn_add_mat_Ring_and_Stiffner,a,4)
        
        a=a+1       
        self.gridlayout.addWidget(self.lbl_Flat_ring_Wt,a,0)
        self.gridlayout.addWidget(self.tb_Flat_ring_Wt,a,1)
        self.gridlayout.addWidget(self.lbl_Flat_ring_material,a,2)
        self.gridlayout.addWidget(self.cmbbox_Flat_ring_material,a,3)
        self.gridlayout.addWidget(self.btn_add_mat_Flat_ring,a,4)
        
        
       
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
        if(self.sender()==self.btn_add_mat_Beam):           
            _ProjectCOntroller.add_update_item(item='Beam WireMesh-Demist',item_name="Beam WireMesh-Demist",wt=self.tb_Beam_Wt.text(),material=self.cmbbox_Beam_material.currentText())
        elif(self.sender()==self.btn_add_mat_Ring_and_Stiffner):           
            _ProjectCOntroller.add_update_item(item='Ring & Stiffner WireMesh-Demist',item_name="Ring & Stiffner WireMesh-Demist",wt=self.tb_Ring_and_Stiffner_Wt.text(),material=self.cmbbox_Ring_and_Stiffner_material.currentText())
        self.change_button_color_green()
    def Calculate_btn_clicked(self):
        
        
        # Database Table Missing
        # Read from Database ...below parameters
        # No. of Beams,Total Beam Length (L),
        # Height of Web (H),Thickness (T), Ring Thickness


        self.tb_Flat_ring_OD.setText(self.tb_shell_ID.text())
        self.Flat_ring_ID=(float(self.tb_shell_ID.text())-2*50) if(self.cmbbox_removeable_through=="Top")\
                            else(float(self.tb_shell_ID.text())-2*(100+float(self.tb_Ring_thk.text())))
        self.tb_Flat_ring_ID.setText(str(round(self.Flat_ring_ID,2)))
        
        
        self.Flat_ring_plt_width=self.BasePlt_Size_Wd(int(self.tb_Flat_ring_No_of_joints.text()),float(self.tb_Flat_ring_OD.text())) 
        self.tb_Flat_ring_plt_width.setText(str(self.Flat_ring_plt_width)) 
        
        self.Flat_ring_length=self.BasePlt_Size_Lg(int(self.tb_Flat_ring_No_of_joints.text()),float(self.tb_Flat_ring_OD.text()),self.Flat_ring_ID)                  
        self.tb_Flat_ring_plt_length.setText(str(self.Flat_ring_length))
        
        
        self.Beam_Wt=(float(self.tb_total_Beam_len.text()))*\
                    (float(self.tb_Web_ht.text()) + 2*float(self.tb_Web_wdth.text()))* \
                    (float(self.tb_thk.text()))*0.00000789 \
                    if (self.cmbbox_material.currentText()=='CS')  \
                    else  (float(self.tb_total_Beam_len.text()))*\
                    (float(self.tb_Web_ht.text()) + 2*float(self.tb_Web_wdth.text()))* \
                    (float(self.tb_thk.text()))*0.00000789
        self.Beam_Wt=round(self.Beam_Wt,1)
        self.tb_Beam_Wt.setText(str(self.Beam_Wt))
        
        self.Rib_and_Stiffner_Wt=math.pi*(float(self.tb_shell_ID.text()))*(float(self.tb_Ring_ht.text()))*(float(self.tb_Ring_thk.text()))*0.00000786   
        self.Rib_and_Stiffner_Wt=round(self.Rib_and_Stiffner_Wt,1)         
        self.tb_Ring_and_Stiffner_Wt.setText(str(self.Rib_and_Stiffner_Wt))  
        
        
        self.Flat_ring_Wt=(float(self.tb_thk.text()))*(float(self.tb_Flat_ring_plt_width.text()))*(float(self.tb_Flat_ring_plt_length.text()))*0.00000786   
        self.Flat_ring_Wt=round(self.Flat_ring_Wt,1)         
        self.tb_Flat_ring_Wt.setText(str(self.Flat_ring_Wt))  
                     
       
     
        #self.reset_button_color_default(self.btn_add_SurfaceArea) #Reset the color of Add Material to BOM as Weight value got changed.
        
    @staticmethod
    def BasePlt_Size_Lg(n, OD, ID):
        # 'This Function is used to calculate the Length of plate required of the base plate development
        # ' n = no. of Joints required, OD = Base Ring OD, ID = Base RIng ID
        T = 360 / (2 * n)
        Pi = math.pi
        R1 = (OD / 2) + 9
        R2 = (ID / 2) - 9
        x = R2 * math.cos(T * Pi / 180)
        y = R2 * math.sin(T * Pi / 180)
        Lg = (R1 - x) + (n - 1) * (math.sqrt(R1 ** 2 - y ** 2) - x)
        return  round(Lg, 0)
        
    @staticmethod
    def BasePlt_Size_Wd(n, OD):
        # 'This Function is used to calculate the width required for the base plate development
        # ' n = no. of Joints required, OD = Base Ring OD   
        T = 360 / (2 * n)
        Pi = math.pi
        R1 = (OD / 2) + 5
        Wd = 2 * R1 * math.sin(T * Pi / 180)
        return round(Wd, 0)  
    
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


