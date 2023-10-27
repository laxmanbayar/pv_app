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
        self.gridlayout.addWidget(self.lbl_No_of_skirt_sec,2,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout.addWidget(self.cmbbox_No_of_skirt_sec,2,1,alignment=Qt.AlignmentFlag.AlignLeft)
        
        self.groupbox_skirt_ip=QGroupBox("Skirt(Input)")
        self.groupbox_skirt_ip.setFixedHeight(150)
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
    
    #This Function sets the Gloval Variables so that other Class instances can use it
    def Set_global_varriables(self):
        global Skirt_ID,Skirt_thk
        Skirt_ID = float(self.tb_skirt_ID.text())
        Skirt_thk = float(self.tb_skirt_thk.text()) 
            
   
class Skirt_Section(QWidget):
    def __init__(self,Number):
        super().__init__()
        self.Number=Number
        self.InitiailizeUI()
        
    def InitiailizeUI(self):
        self.grpbox_skirt_sec=QGroupBox(f"Skirt Sec{self.Number}")
        self.gridlayout_skirt_sec=QGridLayout()
        self.gridlayout_skirt_sec.setVerticalSpacing(20)
        self.grpbox_skirt_sec.setLayout(self.gridlayout_skirt_sec)
        self.SetUp_Skirt_Sec_UI()
        
        self.Vbox_layout_skirt_sec=QVBoxLayout()
        self.Vbox_layout_skirt_sec.addWidget(self.grpbox_skirt_sec)
        self.setLayout(self.Vbox_layout_skirt_sec)
        
    def SetUp_Skirt_Sec_UI(self):
        
        #Input
        self.lbl_mat_density =QLabel("Density")
        self.tb_mat_density =QLineEdit("7.85")
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
        self.btn_add_to_BOM_skirt_sec_Wt=QPushButton("Add")
        self.btn_add_to_BOM_skirt_sec_Wt.clicked.connect(self.Add_to_BOM_Wt)
        self.lbl_skirt_sec_surfaceArea=QLabel("Skirt Section Surface Area")
        self.tb_skirt_sec_surfaceArea=QLineEdit("XX")
        self.tb_skirt_sec_surfaceArea.setEnabled(False)
        self.btn_add_to_BOM_skirt_sec_SurfaceArea=QPushButton("Add")
        self.btn_add_to_BOM_skirt_sec_SurfaceArea.clicked.connect(self.Add_to_BOM_SurfaceArea)
        
        #Input layout set
        self.gridlayout_skirt_sec.addWidget(self.lbl_mat_density,0,0)
        self.gridlayout_skirt_sec.addWidget(self.tb_mat_density,0,1)
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
        print(Skirt_ID,Skirt_thk)
        skirt_len=float(self.tb_skirt_sec_len.text())
        density=float(self.tb_mat_density.text())*0.000001 
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
    def Add_to_BOM_SurfaceArea(self):
        _ProjectConroller=ProjectController()        
        _ProjectConroller.add_update_surface_area(item="Skirt",
                                          item_name= f"Skirt_Sec{self.Number}",
                                          surface_area=self.tb_skirt_sec_surfaceArea.text())  
    
class Skirt_AO(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.InitializeUI()
        
    def InitializeUI(self):
        #Input GroupBox and Layout
        self.grpbox_sec_AO_ip=QGroupBox("Section Access Opening(AO) Input")
        self.gridlayout_sec_AO_ip=QGridLayout()
        self.grpbox_sec_AO_ip.setLayout(self.gridlayout_sec_AO_ip)
        
        #Output GroupBox and Layout
        self.grpbox_sec_AO_op=QGroupBox("Section Access Opening(AO) Output")
        self.gridlayout_sec_AO_op=QGridLayout()
        self.grpbox_sec_AO_op.setLayout(self.gridlayout_sec_AO_op)
        
        #main layout
        self.Vboxlayout_sec_AO =QVBoxLayout()
        self.Vboxlayout_sec_AO.addWidget(self.grpbox_sec_AO_ip)
        self.Vboxlayout_sec_AO.addWidget(self.grpbox_sec_AO_op) 
        
        self.setLayout(self.Vboxlayout_sec_AO)
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
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_Insulation_thk,0,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_Insulation_thk,0,1)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_FireProof_thk,0,2)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_FireProof_thk,0,3)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_AO_inside_dia,1,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_AO_inside_dia,1,1)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_len_of_AO,1,2)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_len_of_AO,1,3)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_No_of_AO,1,4)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_No_of_AO,1,5)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_pad_thk,2,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_pad_thk,2,1)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_AO_cvr_plt_thk,3,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_AO_cvr_plt_thk,3,1)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_No_of_AO_handles,3,2)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_No_of_AO_handles,3,3)       
        self.gridlayout_sec_AO_ip.addWidget(self.btn_calculate_sec_AO_op,4,2,alignment=Qt.AlignmentFlag.AlignCenter)
        
        #Intermediate OP        
        self.gridlayout_sec_AO_ip.addItem(QSpacerItem(30, 30),5, 0,alignment=Qt.AlignmentFlag.AlignCenter)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_thk_of_AO,6,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_thk_of_AO,6,1)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_pad_wdth,6,2)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_pad_wdth,6,3)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_pad_len,6,4)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_pad_len,6,5)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_in_out_projection,7,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_in_out_projection,7,1)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_AO_cvr_plt_dia,8,0)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_AO_cvr_plt_dia,8,1)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_AO_handle_size,8,2)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_AO_handle_size,8,3)
        self.gridlayout_sec_AO_ip.addWidget(self.lbl_AO_cvr_side_ring,8,4)
        self.gridlayout_sec_AO_ip.addWidget(self.tb_AO_cvr_side_ring,8,5)
        
                 
           
    def SetUp_Sec_AO_Op_UI(self):
        pass
    def Calc_btn_Sec_AO_op(self):
        #print(Skirt_ID,Skirt_thk)
        self.Skirt_thk=Skirt_thk
        self.AO_thk=min(14,self.Skirt_thk+2)        
        self.AO_inside_dia=float(self.tb_AO_inside_dia.text())
        self.pad_wdth= self.AO_inside_dia/2       
        self.In_out_projection=max(float(self.tb_Insulation_thk.text())+30, float(self.tb_FireProof_thk.text())+30, 50)        
        self.AO_cvr_plt_dia=float(self.tb_AO_inside_dia.text())+2*self.AO_thk+2*float(self.tb_AO_cvr_plt_thk.text())        
        self.pad_thk=float(self.tb_pad_thk.text())
        self.pad_len= self.IPad_Lg(Skirt_ID,self.AO_inside_dia,self.AO_thk,self.pad_thk,self.pad_wdth)
       
        #Update Textbox value
        self.tb_thk_of_AO.setText(str(self.AO_thk))
        self.tb_pad_wdth.setText(str(self.pad_wdth))
        self.tb_in_out_projection.setText(str(self.In_out_projection))
        self.tb_AO_cvr_plt_dia.setText(str(self.AO_cvr_plt_dia))
        self.tb_AO_handle_size.setText("Ø12" + " x " + "Lg " + str(round(150+2*80+(2*90*math.pi/180*6),0)))        
        self.tb_AO_cvr_side_ring.setText("3 Thk" + " x " + "25 Wd" + " x " + str(round(math.pi*(self.AO_inside_dia+2*self.AO_thk+2*3+2*1.5),0)) + " Lg")
        self.tb_pad_len.setText(str(self.pad_len))
    
    
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
   
    
    
# class Skirt(QWidget):

#     def __init__(self,Number):
#         super().__init__()
#         self.Number=Number
#         self.InitializeUI()
      

#     def InitializeUI(self):

#         self.set_styles()
#         self.SetUp_skirt_ip_GrpBox()#GropBox1
#         self.SetUp_intermediate_op_GrpBox()#GropBox2
#         self.HBox_layout_ip =QHBoxLayout()         
#         self.HBox_layout_ip.addWidget(self.grpbox1)
#         self.HBox_layout_ip.addWidget(self.grpbox2)

        
#         self.HBox_layout_op=QHBoxLayout()
#         self.SetUp_op_GrpBox1()#Groupbox3
#         self.HBox_layout_op.addWidget(self.grpbox1_op)     
        
#         self.Vbox_main_layout=QVBoxLayout()
#         self.Vbox_main_layout.addLayout(self.HBox_layout_ip)
#         self.Vbox_main_layout.addLayout(self.HBox_layout_op)
        
#         self.setLayout(self.Vbox_main_layout)


#     def set_styles(self):
#         self.op_grpbox_style="""
#                 QGroupBox {
#                     font: bold;
#                     font-size:14px;
#                     padding: 15px;
#                     border: 1px solid silver;
#                     border-radius: 6px;
#                     margin-top: 5px;
#                     background-color:lightgrey                     

#                 }
             
              
#                 """   
#         self.ip_grpbox1_style="""
#                 QGroupBox {
#                     font: bold;
#                     font-size:14px;
#                     padding: 15px;
#                     border: 1px solid silver;
#                     border-radius: 6px;
#                     background-color:#ccffcc
                                        
#                 }
                          
#                 """
#         self.ip_grpbox2_style="""
#                 QGroupBox {
#                     font: bold;
#                     font-size:14px;
#                     padding: 15px;
#                     border: 1px solid silver;
#                     border-radius: 6px;
#                     background-color:lightgrey
                                        
#                 }
                          
#                 """ 

#         self.ip_textbox_style="""
#         background-color:lightgreen
#         """    

#     def SetUp_skirt_ip_GrpBox(self):  

#         #Read Material list from Variables
#         self.material_list = var.master_mat_list


#        #Input
#         self.lbl_material =QLabel("Material")
#         self.cmb_box_material = QComboBox()
#         self.cmb_box_material.addItems(self.material_list)
      
#         self.lbl_density =QLabel("Density")
#         self.tb_density =QLineEdit("7.85")

#         self.lbl_skirt_ID =QLabel("Skirt ID")
#         self.tb_skirt_ =QLineEdit("1650")
        
#         self.lbl_skirt_thk =QLabel("Skirt Thk")
#         self.tb_skirt_thk =QLineEdit("12")

#         self.lbl_BCD =QLabel("BCD")
#         self.tb_BCD =QLineEdit("1150")


#         #Base Plt and gusset
#         self.lbl_No_of_joints_Base_plt=QLabel("No. of Joints Base Plt")
#         self.tb_No_of_joints_Base_plt=QLineEdit("4")  
#         self.lbl_thk_Base_plt=QLabel("Base Plt Thk")
#         self.tb_thk_Base_plt=QLineEdit("45")
        
#         self.lbl_gusset_thk =QLabel("Gusset Thk")
#         self.tb_gusset_thk =QLineEdit("18")
  
#         #Comp Plt nd washer
#         self.lbl_Compression=QLabel("Compression")
#         self.tb_Compression =QLineEdit("Ring")
#         self.lbl_No_of_joints_Comp_plt=QLabel("No. of Joints Comp Plt")       
#         self.tb_No_of_joints_Comp_plt=QLineEdit("4")  
#         self.lbl_thk_Comp_plt=QLabel("Comp Plt Thk")     
#         self.tb_thk_Comp_plt=QLineEdit("40")
        
#         self.lbl_washer_Thk=QLabel("Washer Thk")
#         self.tb_washer_Thk =QLineEdit("20")
#         self.lbl_washer_material=QLabel("Washer Material")
#         self.cmb_box_washer_material =QComboBox()
#         self.cmb_box_washer_material.addItems(self.material_list)
        
        
        
#         #self.tb_thk_Comp_plt.setStyleSheet(self.ip_textbox_style)




#         #Create VBox Input
#         self.Input_Gridlayout =QGridLayout()
       
#         self.Input_Gridlayout.addWidget(self.lbl_material,0,0)
#         self.Input_Gridlayout.addWidget(self.cmb_box_material,0,1)
#         self.Input_Gridlayout.addWidget(self.lbl_density,0,2)
#         self.Input_Gridlayout.addWidget(self.tb_density,0,3)
#         self.Input_Gridlayout.addWidget(self.lbl_skirt_type,1,0)
#         self.Input_Gridlayout.addWidget(self.cmb_box_skirt_type,1,1)
#         self.Input_Gridlayout.addWidget(self.lbl_cone_angle,1,2)
#         self.Input_Gridlayout.addWidget(self.tb_cone_angle,1,3)
#         self.Input_Gridlayout.addWidget(self.lbl_bolt_size,2,0)
#         self.Input_Gridlayout.addWidget(self.tb_bolt_size,2,1)
#         self.Input_Gridlayout.addWidget(self.lbl_bolt_count,2,2)
#         self.Input_Gridlayout.addWidget(self.tb_bolt_count,2,3)
#         self.Input_Gridlayout.addWidget(self.lbl_BCD,3,0)
#         self.Input_Gridlayout.addWidget(self.tb_BCD,3,1)
       
     
#         self.Input_Gridlayout.addWidget(self.lbl_No_of_joints_Base_plt,4,0)#
#         self.Input_Gridlayout.addWidget(self.tb_No_of_joints_Base_plt,4,1)
#         self.Input_Gridlayout.addWidget(self.lbl_thk_Base_plt,4,2)#
#         self.Input_Gridlayout.addWidget(self.tb_thk_Base_plt,4,3)
#         self.Input_Gridlayout.addWidget(self.lbl_gusset_thk,5,0)
#         self.Input_Gridlayout.addWidget(self.tb_gusset_thk,5,1)
        
#         self.Input_Gridlayout.addWidget(self.lbl_Compression,6,0)#
#         self.Input_Gridlayout.addWidget(self.tb_Compression,6,1)
#         self.Input_Gridlayout.addWidget(self.lbl_No_of_joints_Comp_plt,6,2)#
#         self.Input_Gridlayout.addWidget(self.tb_No_of_joints_Comp_plt,6,3)        
#         self.Input_Gridlayout.addWidget(self.lbl_thk_Comp_plt,7,0)#
#         self.Input_Gridlayout.addWidget(self.tb_thk_Comp_plt,7,1)
#         self.Input_Gridlayout.addWidget(self.lbl_washer_Thk,7,2)
#         self.Input_Gridlayout.addWidget(self.tb_washer_Thk,7,3)
#         self.Input_Gridlayout.addWidget(self.lbl_washer_material,7,2)
#         self.Input_Gridlayout.addWidgetself.cmb_box_washer_material,7,3
        
       
        
       
#         self.btn_calc_intrmd_op=QPushButton("Calculate Output")
#         self.btn_calc_intrmd_op.clicked.connect(self.Calculate_Outputs)
#         self.Input_Gridlayout.addWidget(self.btn_calc_intrmd_op,8,1,Qt.AlignmentFlag.AlignHCenter)

#         #Create a GroupBox1 and set its layout to VBox_layout1
#         self.grpbox1 = QGroupBox("Input(Base Ring , Comp Ring , Gusset , Washer)",self)
#         self.grpbox1.setStyleSheet(self.ip_grpbox1_style)
#         self.grpbox1.setLayout(self.Input_Gridlayout)
    
#     def Setup_skirt_section_UI(self):
#         self.cmbbox_No_of_skirt_sec=QComboBox()
#         self.cmbbox_No_of_skirt_sec.setStyleSheet("font: bold; font-size: 16px;")    
#         self.cmbbox_No_of_skirt_sec.addItems(([str(x) for x in range(1,5,1)]))    

#     def  SetUp_intermediate_op_GrpBox(self):
#          #create a Vbox_layout2         
#         self.VBox_layout2=QVBoxLayout()
       
#         self.lbl_No_of_gusset_plt =QLabel("No. of Gusset Plt")
#         self.tb_No_of_gusset_plt =QLineEdit("XX")

#         self.lbl_gusset_ht =QLabel("Gusset Ht.")
#         self.tb_gusset_ht =QLineEdit("XX")

#         self.lbl_gusset_wd_at_top =QLabel("Gusset Width @Top")
#         self.tb_gusset_wd_at_top =QLineEdit("XX")

#         self.lbl_gusset_wd_at_btm =QLabel("Gusset Width @Bottom")
#         self.tb_gusset_wd_at_btm =QLineEdit("XX")

#         self.lbl_comp_ring_ID =QLabel("Comp. Ring ID")
#         self.tb_comp_ring_ID =QLineEdit("XX")

#         self.lbl_comp_ring_OD =QLabel("Comp. Ring OD")
#         self.tb_comp_ring_OD =QLineEdit("XX")

#         self.lbl_base_ring_ID =QLabel("Base Ring ID")
#         self.tb_base_ring_ID =QLineEdit("XX")

#         self.lbl_base_ring_OD =QLabel("Base Ring OD")
#         self.tb_base_ring_OD =QLineEdit("XX")

#         self.lbl_washer_dia =QLabel("Washer Dia")
#         self.tb_washer_dia =QLineEdit("XX")


#         self.VBox_layout2.addWidget(self.lbl_No_of_gusset_plt)
#         self.VBox_layout2.addWidget(self.tb_No_of_gusset_plt)
#         self.VBox_layout2.addWidget(self.lbl_gusset_ht)
#         self.VBox_layout2.addWidget(self.tb_gusset_ht)
#         self.VBox_layout2.addWidget(self.lbl_gusset_wd_at_top)
#         self.VBox_layout2.addWidget(self.tb_gusset_wd_at_top)
#         self.VBox_layout2.addWidget(self.lbl_gusset_wd_at_btm)
#         self.VBox_layout2.addWidget(self.tb_gusset_wd_at_btm)
#         self.VBox_layout2.addWidget(self.lbl_comp_ring_ID)
#         self.VBox_layout2.addWidget(self.tb_comp_ring_ID)
#         self.VBox_layout2.addWidget(self.lbl_comp_ring_OD)
#         self.VBox_layout2.addWidget(self.tb_comp_ring_OD)
#         self.VBox_layout2.addWidget(self.lbl_base_ring_ID)
#         self.VBox_layout2.addWidget(self.tb_base_ring_ID)
#         self.VBox_layout2.addWidget(self.lbl_base_ring_OD)
#         self.VBox_layout2.addWidget(self.tb_base_ring_OD)
#         self.VBox_layout2.addWidget(self.lbl_washer_dia)
#         self.VBox_layout2.addWidget(self.tb_washer_dia)

#         #Create Groupbox2 and sets its layout to Vbox_layout2
#         self.grpbox2 = QGroupBox("Intermediate Op",self)
#         self.grpbox2.setStyleSheet(self.ip_grpbox2_style)
#         self.grpbox2.setLayout(self.VBox_layout2)
#         self.grpbox2.setDisabled(True)
              
        
#     def SetUp_op_GrpBox1(self):#Base Ring and Gusset
       
#         #Base Ring and Gusset
#         self.lbl_wdth_Base_plt=QLabel("Base Plt Width")
#         self.tb_wdth_Base_plt=QLineEdit("XXX")
#         self.tb_wdth_Base_plt.setDisabled(True)
#         self.lbl_len_Base_plt=QLabel("Base Plt Length")
#         self.tb_len_Base_plt=QLineEdit("XX")
#         self.tb_len_Base_plt.setDisabled(True)
        

#         self.lbl_wt_Base_plt=QLabel("Base Plt Weight")
#         self.tb_wt_Base_plt=QLineEdit("XXXX")
#         self.tb_wt_Base_plt.setDisabled(True)
#         self.btn_add_wt_Base_plt=QPushButton("Add")       
#         self.lbl_wt_BOM_Base_plt=QLabel("Base Plt Weight BOM")
#         self.tb_wt_BOM_Base_plt=QLineEdit("XXXX")
#         self.tb_wt_BOM_Base_plt.setDisabled(True)
#         self.btn_add_wt_BOM_Base_plt=QPushButton("Add")

#         self.lbl_wt_gusset=QLabel("Gusset Weight")
#         self.tb_wt_gusset=QLineEdit("XXX")
#         self.tb_wt_gusset.setDisabled(True)
#         self.btn_add_wt_gusset=QPushButton("Add")
        
        
        
#         #Comp Ring ad Washer
#         self.lbl_wdth_Comp_plt=QLabel("Comp Plt Width")
#         self.tb_wdth_Comp_plt=QLineEdit("4")
#         self.tb_wdth_Comp_plt.setDisabled(True)
#         self.lbl_len_Comp_plt=QLabel("Comp Plt Length")
#         self.tb_len_Comp_plt=QLineEdit("4")
#         self.tb_len_Comp_plt.setDisabled(True)
        

#         self.lbl_wt_Comp_plt=QLabel("Comp Plt Weight")
#         self.tb_wt_Comp_plt=QLineEdit("XXXX")
#         self.tb_wt_Comp_plt.setDisabled(True)
#         self.btn_add_wt_Comp_plt=QPushButton("Add")
#         self.lbl_wt_BOM_Comp_plt=QLabel("Comp Plt Weight BOM")
#         self.tb_wt_BOM_Comp_plt=QLineEdit("XXXX")
#         self.tb_wt_BOM_Comp_plt.setDisabled(True)
#         self.btn_add_wt_BOM_Comp_plt=QPushButton("Add")

#         self.lbl_wt_washer=QLabel("Washer Weight")
#         self.tb_wt_washer=QLineEdit("4")
#         self.tb_wt_washer.setDisabled(True)
#         self.btn_add_wt_washer=QPushButton("Add")
        
#         #Base comp ring Syrface area
#         self.lbl_base_comp_ring_surface_area=QLabel("Base Comp Ring Surface Area")
#         self.tb_base_comp_ring_surface_area=QLineEdit("XXX")
#         self.tb_base_comp_ring_surface_area.setDisabled(True)
#         self.btn_add_base_comp_ring_surface_area=QPushButton("Add")
        
        
        

#         grid_layout1=QGridLayout()
#         #Base Ring      
#         grid_layout1.addWidget(self.lbl_wdth_Base_plt,0,0)
#         grid_layout1.addWidget(self.tb_wdth_Base_plt,0,1)
#         grid_layout1.addWidget(self.lbl_len_Base_plt,1,0)
#         grid_layout1.addWidget(self.tb_len_Base_plt,1,1)
#         grid_layout1.addWidget(self.lbl_wt_Base_plt,2,0)
#         grid_layout1.addWidget(self.tb_wt_Base_plt,2,1)
#         grid_layout1.addWidget(self.btn_add_wt_Base_plt,2,2)
#         grid_layout1.addWidget(self.lbl_wt_BOM_Base_plt,3,0)
#         grid_layout1.addWidget(self.tb_wt_BOM_Base_plt,3,1)
#         grid_layout1.addWidget(self.btn_add_wt_BOM_Base_plt,3,2)
#         grid_layout1.addWidget(self.lbl_wt_gusset,4,0)
#         grid_layout1.addWidget(self.tb_wt_gusset,4,1)
#         grid_layout1.addWidget(self.btn_add_wt_gusset,4,2)
        
#         #Surface Area
#         grid_layout1.addWidget(self.lbl_base_comp_ring_surface_area,5,0)
#         grid_layout1.addWidget(self.tb_base_comp_ring_surface_area,5,1)
#         grid_layout1.addWidget(self.btn_add_base_comp_ring_surface_area,5,2)
        
        
#         #Comp Ring
#         grid_layout1.addWidget(self.lbl_wdth_Comp_plt,0,3)
#         grid_layout1.addWidget(self.tb_wdth_Comp_plt,0,4)
#         grid_layout1.addWidget(self.lbl_len_Comp_plt,1,3)
#         grid_layout1.addWidget(self.tb_len_Comp_plt,1,4)
#         grid_layout1.addWidget(self.lbl_wt_Comp_plt,2,3)
#         grid_layout1.addWidget(self.tb_wt_Comp_plt,2,4)
#         grid_layout1.addWidget(self.btn_add_wt_Comp_plt,2,5)
#         grid_layout1.addWidget(self.lbl_wt_BOM_Comp_plt,3,3)
#         grid_layout1.addWidget(self.tb_wt_BOM_Comp_plt,3,4)
#         grid_layout1.addWidget(self.btn_add_wt_BOM_Comp_plt,3,5)
#         grid_layout1.addWidget(self.lbl_wt_washer,4,3)
#         grid_layout1.addWidget(self.tb_wt_washer,4,4)
#         grid_layout1.addWidget(self.btn_add_wt_washer,4,5)
        
        
        
       

#         self.grpbox1_op= QGroupBox("Base Plt-Comp Plt-Washer-Gusset",self)
        
#         self.grpbox1_op.setStyleSheet(self.op_grpbox_style)  
#         self.grpbox1_op.setLayout(grid_layout1)
        
        


#     def Calculate_Outputs(self):
        
#         #Intermediate Outputs
#         bolt_count=int(self.tb_bolt_count.text())
#         No_of_gusset_plt=2*bolt_count 
#         self.tb_No_of_gusset_plt.setText(str(No_of_gusset_plt))
#         bolt_size= int(self.tb_bolt_size.text())
#         gusset_detail=DBController.Get_gusset_detail(bolt_size)
#         gusset_ht=float(gusset_detail.H)
#         self.tb_gusset_ht.setText(str(gusset_ht))
#         gusset_wd_at_top=float(gusset_detail.A)+float(gusset_detail.B)
#         gusset_wd_at_btm=float(gusset_detail.L)-float(gusset_detail.K)
#         self.tb_gusset_wd_at_top.setText(str(gusset_wd_at_top))
#         self.tb_gusset_wd_at_btm.setText(str(gusset_wd_at_btm))
#         BCD=float(self.tb_BCD.text())
#         self.tb_comp_ring_ID.setText(str(BCD-2*float(gusset_detail.A)))
#         self.tb_comp_ring_OD.setText(str(BCD+2*float(gusset_detail.B)))
#         self.tb_base_ring_ID.setText(str(BCD-2*(float(gusset_detail.A)+float(gusset_detail.K))))
#         self.tb_base_ring_OD.setText(str(float(self.tb_base_ring_ID.text())+2*float(gusset_detail.L)))
#         self.tb_washer_dia.setText(str(float(gusset_detail.F)))
        
        
#        #---------#
#        #Outputs
#        #----------#
       
#        #Base Plt
#         n_base_ring=int(self.tb_No_of_joints_Base_plt.text())
#         OD_base_ring=float(self.tb_base_ring_OD.text())
#         ID_base_ring=float(self.tb_base_ring_ID.text())
#         wdth_of_base_plt = self.BasePlt_Size_Wd(n_base_ring,OD_base_ring)
#         len_of_base_plt = self.BasePlt_Size_Lg(n_base_ring,OD_base_ring,ID_base_ring)
#         density=float(self.tb_density.text())*0.000001
#         thk_base_plt=float(self.tb_thk_Base_plt.text())
#         wt_base_ring = round(wdth_of_base_plt*len_of_base_plt*thk_base_plt*density,1)
#         wt_BOM_base_ring= round(math.pi/4*(OD_base_ring**2-ID_base_ring**2)*thk_base_plt*density,1)
        
#         #Gusets
#         thk_gusset=float(self.tb_gusset_thk.text())       
#         wt_gusset=round(No_of_gusset_plt*gusset_ht*gusset_wd_at_top*thk_gusset*density)
        
#         #Comp Ring
#         n_comp_ring=int(self.tb_No_of_joints_Comp_plt.text())
#         No_of_bolts=int(self.tb_bolt_count.text())
#         OD_comp_ring=float(self.tb_comp_ring_OD.text())
#         ID_comp_ring=float(self.tb_comp_ring_ID.text())
#         thk_comp_plt=float(self.tb_thk_Comp_plt.text())
#         is_ring=self.tb_Compression.text().lower()=='ring'       
#         wdth_of_comp_plt= self.BasePlt_Size_Wd(n_comp_ring,OD_comp_ring) if(is_ring) else (ID_comp_ring)
#         len_of_comp_plt=self.BasePlt_Size_Lg(n_comp_ring,OD_comp_ring,ID_comp_ring) if(is_ring) else (OD_comp_ring) 
#         wt_comp_ring =  round(wdth_of_comp_plt*len_of_comp_plt*thk_comp_plt*density,1) if(is_ring) else round(wdth_of_comp_plt*len_of_comp_plt*thk_comp_plt*density*No_of_bolts,1)
#         wt_BOM_comp_ring = round(math.pi/4*(OD_comp_ring**2-ID_comp_ring**2)*thk_comp_plt*density,1) if(is_ring) else round(wdth_of_comp_plt*len_of_comp_plt*thk_comp_plt*density*No_of_bolts,1) 
        
#         #Washer
#         OD_washer=float(self.tb_washer_dia.text())
#         thk_washer=float(self.tb_washer_Thk.text())
#         ID_washer=float(OD_washer-bolt_size)
#         wt_washer=round(math.pi/4*(OD_washer**2-ID_washer**2)*thk_washer*No_of_bolts*density,1)
        
        
#         #Surface Area
#         surface_area_base_ring=math.pi/4*((OD_base_ring/1000)**2-(ID_base_ring/1000)**2)+math.pi*OD_base_ring*thk_base_plt/1000/1000*2
#         surface_area_comp_ring=math.pi/4*((OD_comp_ring/1000)**2-(ID_comp_ring/1000)**2)+math.pi*OD_comp_ring*thk_comp_plt/1000/1000*2
#         surface_area_gusset=gusset_ht*gusset_wd_at_top/1000/1000*No_of_gusset_plt*2
#         surface_arae_base_comp_ring=round(surface_area_base_ring+surface_area_comp_ring+surface_area_gusset,1)
        
        
#         #Update OP groupboxes
#         self.tb_wdth_Base_plt.setText(str(wdth_of_base_plt))
#         self.tb_len_Base_plt.setText(str(len_of_base_plt))
#         self.tb_wt_Base_plt.setText(str(wt_base_ring))
#         self.tb_wt_BOM_Base_plt.setText(str(wt_BOM_base_ring))
#         self.tb_wt_gusset.setText(str(wt_gusset))
#         self.tb_wdth_Comp_plt.setText(str(wdth_of_comp_plt))
#         self.tb_len_Comp_plt.setText(str(len_of_comp_plt))
#         self.tb_wt_Comp_plt.setText(str(wt_comp_ring))
#         self.tb_wt_BOM_Comp_plt.setText(str(wt_BOM_comp_ring))
#         self.tb_wt_washer.setText(str(wt_washer))
#         self.tb_base_comp_ring_surface_area.setText(str(surface_arae_base_comp_ring))
        
#         #Define Button functionality
#         self.btn_add_wt_Base_plt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
#                                                                            {'item':'Base Ring',
#                                                                             'item_name':'Base Ring'+str(self.Number),
#                                                                             'wt':str(wt_base_ring),
#                                                                             'material':self.cmb_box_material.currentText()
#                                                                             }))
        
#         self.btn_add_wt_BOM_Base_plt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
#                                                             {'item':'Base Ring',
#                                                             'item_name':'Base Ring BOM'+str(self.Number),
#                                                             'wt':str(wt_BOM_base_ring),
#                                                             'material':self.cmb_box_material.currentText()
#                                                             }))

#         self.btn_add_wt_Comp_plt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
#                                                             {'item':'Comp Ring',
#                                                             'item_name':'Comp Ring'+str(self.Number),
#                                                             'wt':str(wt_comp_ring),
#                                                             'material':self.cmb_box_material.currentText()
#                                                             }))
        
#         self.btn_add_wt_BOM_Comp_plt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
#                                                             {'item':'Comp Ring',
#                                                             'item_name':'Comp Ring BOM'+str(self.Number),
#                                                             'wt':str(wt_BOM_comp_ring),
#                                                             'material':self.cmb_box_material.currentText()
#                                                             }))
        
#         self.btn_add_wt_gusset.clicked.connect(lambda:self.Add_wt_to_BOM(data=
#                                                             {'item':'Gusset',
#                                                             'item_name':'Gusset'+str(self.Number),
#                                                             'wt':str(wt_gusset),
#                                                             'material':self.cmb_box_material.currentText()
#                                                             }))
        
#         self.btn_add_wt_washer.clicked.connect(lambda:self.Add_wt_to_BOM(data=
#                                                             {'item':'Washer',
#                                                             'item_name':'Washer'+str(self.Number),
#                                                             'wt':str(wt_washer),
#                                                             'material':self.cmb_box_material.currentText()
#                                                             }))
        
#         self.btn_add_base_comp_ring_surface_area.clicked.connect(lambda:self.Add_SurfaceArea_to_BOM(data=
#                                                             {'item':'Gusset',
#                                                             'item_name':'Gusset'+str(self.Number),
#                                                             'surface_area':str(surface_arae_base_comp_ring)                                                            
#                                                             }))

        
#         #self.change_button_color_green()#Change color of the Calc button
#         self.reset_button_color_default()#Reset the color of Add  to BOM as Weight value got changed.
            
#     def update_material(self) :
#         #This will update the Material in the Shell OPutput Groupbox
#         #self.tb_shell_op_Material.setText(str(self.cmb_box_material.currentText()))
#         #print(i)
#         pass
#     def update_skirt_type(self):
#         #print(self.cmb_box_skirt_type.currentText())

#         #Hide Cone_angle label and text if skirt_type not eq to 'shell'
#         if(str.lower(self.cmb_box_skirt_type.currentText())=='cone'):
#             self.lbl_cone_angle.setHidden(False)
#             self.tb_cone_angle.setHidden(False)
#         else:
#             self.lbl_cone_angle.setHidden(True)
#             self.tb_cone_angle.setHidden(True)

#     def Add_wt_to_BOM(self,data):
#         print("Add Shell Material to BOM Pressed")
#         _projectcontroller=ProjectController()
#         _projectcontroller.add_update_item(item=data['item'],item_name=data['item_name'],wt=data['wt'],material=data['material'])
#         print(data)
#         self.change_button_color_green()
        
#     def Add_SurfaceArea_to_BOM(self,data):
#          _projectcontroller=ProjectController()
#          _projectcontroller.add_update_surface_area(item=data['item'],item_name=data['item_name'],surface_area=data['surface_area'])
#          self.change_button_color_green()

#     # @staticmethod
#     # def calculate_allwnce_on_dia(ID, T):
#     #     OD = ID + 2 * T
            
#     #     if T > 100:
#     #         Allow = 300
#     #     elif 50 < T <= 100:
#     #         Allow = 2 * T
#     #     elif (30 < T < 50) and (OD / T) <= 24:
#     #         Allow = 2 * T
#     #     elif (T <= 30) and (OD / T) <= 15:
#     #         Allow = 1 * T
#     #     else:
#     #         Allow = 0
#     #     print(ID,OD,T,Allow)    
#     #     return Allow
   
#     @staticmethod
#     def BasePlt_Size_Wd(n, OD):  
#         #'This Function is used to calculate the width required for the base plate development
#         #' n = no. of Joints required, OD = Base Ring OD

#         T = 360 / (2 * n)
#         Pi = 22 / 7
#         R1 = (OD / 2) + 5
#         Wd = 2 * R1 * math.sin(T * Pi / 180)
#         return round(Wd)
    
#     @staticmethod
#     def BasePlt_Size_Lg(n, OD, ID):     
#     # 'This Function is used to calculate the Length of plate required of the base plate development
#     # ' n = no. of Joints required, OD = Base Ring OD, ID = Base RIng ID

#         T = 360 / (2 * n)
#         Pi = 22 / 7
#         R1 = (OD / 2) + 9
#         R2 = (ID / 2) - 9
#         x = R2 * math.cos(T * Pi / 180)
#         y = R2 * math.sin(T * Pi / 180)
#         Lg = (R1 - x) + (n - 1) * (math.sqrt(R1 ** 2 - y ** 2) - x)
#         return round(Lg)
        
   
#     #This function changes the coor of sender button to green
#     def change_button_color_green(self):
#         button = self.sender()
#         button.setStyleSheet("background-color: green; color: white;")

#     #This Function reset the color of "button" passed as an argument.
#     def reset_button_color_default(self):
#         #button = self.sender()
#         for button in self.grpbox1_op.findChildren(QPushButton):
#             button.setStyleSheet("")  # Reset the color      

    