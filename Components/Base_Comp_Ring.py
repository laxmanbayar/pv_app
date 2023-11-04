import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout,QWidget, \
    QTabWidget,QGroupBox,QTableWidget,QTableWidgetItem,QGridLayout,QScrollArea
from Variables import var
from PyQt6.QtCore import Qt
import math
import Controller.project_controller as DBController
from Controller.project_controller import ProjectController,Get_Elbow_Details,Get_WL_FLG_detail

class Tab_Base_Comp_Ring(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
    def InitializeUI(self):
        H_box_layout= QHBoxLayout() 
        base_comp_ring_gusset=Base_Comp_Ring_Gusset(Number=1)             
        H_box_layout.addWidget(base_comp_ring_gusset)
         
        V_box_layout=QVBoxLayout()
        V_box_layout.addLayout(H_box_layout)
        Bottom_DEnd_Nozzle=Nozzle_DEnd()  
        V_box_layout.addWidget(Bottom_DEnd_Nozzle) 
        
        # add one container widget and set its Lsyout as "V_box_layout"
        self.container_widget = QWidget()
        self.container_widget.setLayout(V_box_layout)
        #self.container_widget.setFixedHeight(400)

        # Create new Scroll area and set it as resizable
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        # Set the container widget as the widget for the scroll area
        self.scroll_area.setWidget(self.container_widget)  
        
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.scroll_area)
        #main_v_box.addLayout(self.V_box_layout)

        self.setLayout(main_v_box)     


class Base_Comp_Ring_Gusset(QWidget):

    def __init__(self,Number):
        super().__init__()
        self.Number=Number
        self.InitializeUI()
      

    def InitializeUI(self):

        self.set_styles()
        #Create a input GroupBox1       
        self.grpbox1 = QGroupBox("Input(Base Ring , Comp Ring , Gusset , Washer)",self)
        #self.grpbox1.setFixedWidth(400)
        self.grpbox1.setStyleSheet(self.ip_grpbox1_style)              
        
        
        #Create Groupbox2 for Intermediat op
        self.grpbox2 = QGroupBox("Intermediate Op",self)
        #self.grpbox2.setFixedWidth(100)
        self.grpbox2.setStyleSheet(self.ip_grpbox2_style)       
        self.grpbox2.setDisabled(True)
        
        ##Hbox for ip and intermediiate op
        self.HBox_layout_ip =QHBoxLayout()         
        self.HBox_layout_ip.addWidget(self.grpbox1)
        self.HBox_layout_ip.addWidget(self.grpbox2)
        
        #Create Groupbox1 for op
        self.grpbox1_op= QGroupBox("Base Plt-Comp Plt-Washer-Gusset",self)
        #self.grpbox2_op.setFixedHeight(100)         
        self.grpbox1_op.setStyleSheet(self.op_grpbox_style)  
        
        
        #Create Groupbox2 for op
        self.grpbox2_op=QGroupBox("Template",self)        
        self.grpbox2_op.setStyleSheet(self.op_grpbox_style)               
       
        
        ##Hbox for O/p 
        self.HBox_layout_op=QHBoxLayout()       
        self.HBox_layout_op.addWidget(self.grpbox1_op)
        self.HBox_layout_op.addWidget(self.grpbox2_op,alignment=Qt.AlignmentFlag.AlignTop)   
        
        self.SetUp_ip_GrpBox()#GropBox1
        self.SetUp_intermediate_op_GrpBox()#GropBox2
        self.SetUp_op_GrpBox1()#Groupbox3
        self.SetUp_op_GrpBox2()#Groupbox4
        
        
        self.Vbox_main_layout=QVBoxLayout()
        self.Vbox_main_layout.addLayout(self.HBox_layout_ip)
        self.Vbox_main_layout.addLayout(self.HBox_layout_op)
        
        self.setLayout(self.Vbox_main_layout)


    def set_styles(self):
        self.op_grpbox_style="""
                QGroupBox {
                    font: bold;
                    font-size:14px;
                    padding: 15px;
                    border: 1px solid silver;
                    border-radius: 6px;
                    margin-top: 5px;
                    background-color:lightgrey                     

                }
             
              
                """   
        self.ip_grpbox1_style="""
                QGroupBox {
                    font: bold;
                    font-size:14px;
                    padding: 15px;
                    border: 1px solid silver;
                    border-radius: 6px;
                    background-color:#ccffcc
                                        
                }
                          
                """
        self.ip_grpbox2_style="""
                QGroupBox {
                    font: bold;
                    font-size:14px;
                    padding: 15px;
                    border: 1px solid silver;
                    border-radius: 6px;
                    background-color:lightgrey
                                        
                }
                          
                """ 

        self.ip_textbox_style="""
        background-color:lightgreen
        """    

    def  SetUp_ip_GrpBox(self):  

        #Read Material list from Variables
        self.material_list = var.master_mat_list


       #Input
        self.lbl_material =QLabel("Material")
        self.cmb_box_material = QComboBox()
        self.cmb_box_material.addItems(self.material_list)
        #self.cmb_box_material.currentIndexChanged.connect(self.update_material)
        
        self.lbl_density =QLabel("Density")
        self.tb_density =QLineEdit("7.85")

        self.lbl_skirt_type =QLabel("Type of Skirt")
        self.cmb_box_skirt_type = QComboBox()
        list_skirt_type=["Cone","Shell"]
        self.cmb_box_skirt_type.addItems(list_skirt_type)
        self.cmb_box_skirt_type.currentIndexChanged.connect(self.update_skirt_type)
       
        self.lbl_cone_angle =QLabel("Cone Angle")
        self.tb_cone_angle =QLineEdit("0")

        self.lbl_bolt_size =QLabel("Bolt Size")
        self.tb_bolt_size =QLineEdit("32")
        
        self.lbl_bolt_count =QLabel("No. of Bolts")
        self.tb_bolt_count =QLineEdit("8")

        self.lbl_BCD =QLabel("BCD")
        self.tb_BCD =QLineEdit("1150")


        #Base Plt and gusset
        self.lbl_No_of_joints_Base_plt=QLabel("No. of Joints Base Plt")
        self.tb_No_of_joints_Base_plt=QLineEdit("4")  
        self.lbl_thk_Base_plt=QLabel("Base Plt Thk")
        self.tb_thk_Base_plt=QLineEdit("45")
        
        self.lbl_gusset_thk =QLabel("Gusset Thk")
        self.tb_gusset_thk =QLineEdit("18")
  
        #Comp Plt nd washer
        self.lbl_Compression=QLabel("Compression")
        self.tb_Compression =QLineEdit("Ring")
        self.lbl_No_of_joints_Comp_plt=QLabel("No. of Joints Comp Plt")       
        self.tb_No_of_joints_Comp_plt=QLineEdit("4")  
        self.lbl_thk_Comp_plt=QLabel("Comp Plt Thk")     
        self.tb_thk_Comp_plt=QLineEdit("40")
        
        self.lbl_washer_Thk=QLabel("Washer Thk")
        self.tb_washer_Thk =QLineEdit("20")
        self.lbl_washer_material=QLabel("Washer Material")
        self.cmb_box_washer_material =QComboBox()
        self.cmb_box_washer_material.addItems(self.material_list)
        
        self.lbl_template_Thk=QLabel("Template Thk")
        self.tb_template_Thk =QLineEdit("10")
        
        
        
        #self.tb_thk_Comp_plt.setStyleSheet(self.ip_textbox_style)




        #Create VBox Input
        self.Input_Gridlayout =QGridLayout()
       
        self.Input_Gridlayout.addWidget(self.lbl_material,0,0)
        self.Input_Gridlayout.addWidget(self.cmb_box_material,0,1)
        self.Input_Gridlayout.addWidget(self.lbl_density,0,2)
        self.Input_Gridlayout.addWidget(self.tb_density,0,3)
        self.Input_Gridlayout.addWidget(self.lbl_skirt_type,1,0)
        self.Input_Gridlayout.addWidget(self.cmb_box_skirt_type,1,1)
        self.Input_Gridlayout.addWidget(self.lbl_cone_angle,1,2)
        self.Input_Gridlayout.addWidget(self.tb_cone_angle,1,3)
        self.Input_Gridlayout.addWidget(self.lbl_bolt_size,2,0)
        self.Input_Gridlayout.addWidget(self.tb_bolt_size,2,1)
        self.Input_Gridlayout.addWidget(self.lbl_bolt_count,2,2)
        self.Input_Gridlayout.addWidget(self.tb_bolt_count,2,3)
        self.Input_Gridlayout.addWidget(self.lbl_BCD,3,0)
        self.Input_Gridlayout.addWidget(self.tb_BCD,3,1)
       
     
        self.Input_Gridlayout.addWidget(self.lbl_No_of_joints_Base_plt,4,0)#
        self.Input_Gridlayout.addWidget(self.tb_No_of_joints_Base_plt,4,1)
        self.Input_Gridlayout.addWidget(self.lbl_thk_Base_plt,4,2)#
        self.Input_Gridlayout.addWidget(self.tb_thk_Base_plt,4,3)
        self.Input_Gridlayout.addWidget(self.lbl_gusset_thk,5,0)
        self.Input_Gridlayout.addWidget(self.tb_gusset_thk,5,1)
        
        self.Input_Gridlayout.addWidget(self.lbl_Compression,6,0)#
        self.Input_Gridlayout.addWidget(self.tb_Compression,6,1)
        self.Input_Gridlayout.addWidget(self.lbl_No_of_joints_Comp_plt,6,2)#
        self.Input_Gridlayout.addWidget(self.tb_No_of_joints_Comp_plt,6,3)        
        self.Input_Gridlayout.addWidget(self.lbl_thk_Comp_plt,7,0)#
        self.Input_Gridlayout.addWidget(self.tb_thk_Comp_plt,7,1)
        self.Input_Gridlayout.addWidget(self.lbl_washer_Thk,8,0)
        self.Input_Gridlayout.addWidget(self.tb_washer_Thk,8,1)
        self.Input_Gridlayout.addWidget(self.lbl_washer_material,8,2)
        self.Input_Gridlayout.addWidget(self.cmb_box_washer_material,8,3)
        self.Input_Gridlayout.addWidget(self.lbl_template_Thk,9,0)
        self.Input_Gridlayout.addWidget(self.tb_template_Thk,9,1)
        
       
        
       
        self.btn_calc_op=QPushButton("Calculate Output")
        self.btn_calc_op.clicked.connect(self.Calculate_Outputs)
        self.Input_Gridlayout.addWidget(self.btn_calc_op,11,1,Qt.AlignmentFlag.AlignHCenter)

        #input grpbox1 layout to VBox_layout1
        #self.grpbox1 = QGroupBox("Input(Base Ring , Comp Ring , Gusset , Washer)",self)
        self.grpbox1.setStyleSheet(self.ip_grpbox1_style)
        self.grpbox1.setLayout(self.Input_Gridlayout)
    

    def  SetUp_intermediate_op_GrpBox(self):
         #create a Vbox_layout2         
        self.VBox_layout2=QVBoxLayout()
       
        self.lbl_No_of_gusset_plt =QLabel("No. of Gusset Plt")
        self.tb_No_of_gusset_plt =QLineEdit("XX")

        self.lbl_gusset_ht =QLabel("Gusset Ht.")
        self.tb_gusset_ht =QLineEdit("XX")

        self.lbl_gusset_wd_at_top =QLabel("Gusset Width @Top")
        self.tb_gusset_wd_at_top =QLineEdit("XX")

        self.lbl_gusset_wd_at_btm =QLabel("Gusset Width @Bottom")
        self.tb_gusset_wd_at_btm =QLineEdit("XX")

        self.lbl_comp_ring_ID =QLabel("Comp. Ring ID")
        self.tb_comp_ring_ID =QLineEdit("XX")

        self.lbl_comp_ring_OD =QLabel("Comp. Ring OD")
        self.tb_comp_ring_OD =QLineEdit("XX")

        self.lbl_base_ring_ID =QLabel("Base Ring ID")
        self.tb_base_ring_ID =QLineEdit("XX")

        self.lbl_base_ring_OD =QLabel("Base Ring OD")
        self.tb_base_ring_OD =QLineEdit("XX")

        self.lbl_washer_dia =QLabel("Washer Dia")
        self.tb_washer_dia =QLineEdit("XX")


        self.VBox_layout2.addWidget(self.lbl_No_of_gusset_plt)
        self.VBox_layout2.addWidget(self.tb_No_of_gusset_plt)
        self.VBox_layout2.addWidget(self.lbl_gusset_ht)
        self.VBox_layout2.addWidget(self.tb_gusset_ht)
        self.VBox_layout2.addWidget(self.lbl_gusset_wd_at_top)
        self.VBox_layout2.addWidget(self.tb_gusset_wd_at_top)
        self.VBox_layout2.addWidget(self.lbl_gusset_wd_at_btm)
        self.VBox_layout2.addWidget(self.tb_gusset_wd_at_btm)
        self.VBox_layout2.addWidget(self.lbl_comp_ring_ID)
        self.VBox_layout2.addWidget(self.tb_comp_ring_ID)
        self.VBox_layout2.addWidget(self.lbl_comp_ring_OD)
        self.VBox_layout2.addWidget(self.tb_comp_ring_OD)
        self.VBox_layout2.addWidget(self.lbl_base_ring_ID)
        self.VBox_layout2.addWidget(self.tb_base_ring_ID)
        self.VBox_layout2.addWidget(self.lbl_base_ring_OD)
        self.VBox_layout2.addWidget(self.tb_base_ring_OD)
        self.VBox_layout2.addWidget(self.lbl_washer_dia)
        self.VBox_layout2.addWidget(self.tb_washer_dia)

        #Set Groupbox2 layout to Vbox_layout2 
        self.grpbox2.setLayout(self.VBox_layout2)
       
              
        
    def SetUp_op_GrpBox1(self):#Base Ring and Gusset
       
        #Base Ring and Gusset
        self.lbl_wdth_Base_plt=QLabel("Base Plt Width")
        self.tb_wdth_Base_plt=QLineEdit("XXX")
        self.tb_wdth_Base_plt.setDisabled(True)
        self.lbl_len_Base_plt=QLabel("Base Plt Length")
        self.tb_len_Base_plt=QLineEdit("XX")
        self.tb_len_Base_plt.setDisabled(True)
        

        self.lbl_wt_Base_plt=QLabel("Base Plt Weight")
        self.tb_wt_Base_plt=QLineEdit("XXXX")
        self.tb_wt_Base_plt.setDisabled(True)
        self.btn_add_wt_Base_plt=QPushButton("Add")       
        self.lbl_wt_BOM_Base_plt=QLabel("Base Plt Weight BOM")
        self.tb_wt_BOM_Base_plt=QLineEdit("XXXX")
        self.tb_wt_BOM_Base_plt.setDisabled(True)
        self.btn_add_wt_BOM_Base_plt=QPushButton("Add")

        self.lbl_wt_gusset=QLabel("Gusset Weight")
        self.tb_wt_gusset=QLineEdit("XXX")
        self.tb_wt_gusset.setDisabled(True)
        self.btn_add_wt_gusset=QPushButton("Add")
        
        
        
        #Comp Ring ad Washer
        self.lbl_wdth_Comp_plt=QLabel("Comp Plt Width")
        self.tb_wdth_Comp_plt=QLineEdit("4")
        self.tb_wdth_Comp_plt.setDisabled(True)
        self.lbl_len_Comp_plt=QLabel("Comp Plt Length")
        self.tb_len_Comp_plt=QLineEdit("4")
        self.tb_len_Comp_plt.setDisabled(True)
        

        self.lbl_wt_Comp_plt=QLabel("Comp Plt Weight")
        self.tb_wt_Comp_plt=QLineEdit("XXXX")
        self.tb_wt_Comp_plt.setDisabled(True)
        self.btn_add_wt_Comp_plt=QPushButton("Add")
        self.lbl_wt_BOM_Comp_plt=QLabel("Comp Plt Weight BOM")
        self.tb_wt_BOM_Comp_plt=QLineEdit("XXXX")
        self.tb_wt_BOM_Comp_plt.setDisabled(True)
        self.btn_add_wt_BOM_Comp_plt=QPushButton("Add")

        self.lbl_wt_washer=QLabel("Washer Weight")
        self.tb_wt_washer=QLineEdit("4")
        self.tb_wt_washer.setDisabled(True)
        self.btn_add_wt_washer=QPushButton("Add")
        
        #Base comp ring Syrface area
        self.lbl_base_comp_ring_surface_area=QLabel("Base Comp Ring Surface Area")
        self.tb_base_comp_ring_surface_area=QLineEdit("XXX")
        self.tb_base_comp_ring_surface_area.setDisabled(True)
        self.btn_add_base_comp_ring_surface_area=QPushButton("Add")
        
      
        

        grid_layout1=QGridLayout()
        #Base Ring      
        grid_layout1.addWidget(self.lbl_wdth_Base_plt,0,0)
        grid_layout1.addWidget(self.tb_wdth_Base_plt,0,1)
        grid_layout1.addWidget(self.lbl_len_Base_plt,1,0)
        grid_layout1.addWidget(self.tb_len_Base_plt,1,1)
        grid_layout1.addWidget(self.lbl_wt_Base_plt,2,0)
        grid_layout1.addWidget(self.tb_wt_Base_plt,2,1)
        grid_layout1.addWidget(self.btn_add_wt_Base_plt,2,2)
        grid_layout1.addWidget(self.lbl_wt_BOM_Base_plt,3,0)
        grid_layout1.addWidget(self.tb_wt_BOM_Base_plt,3,1)
        grid_layout1.addWidget(self.btn_add_wt_BOM_Base_plt,3,2)
        grid_layout1.addWidget(self.lbl_wt_gusset,4,0)
        grid_layout1.addWidget(self.tb_wt_gusset,4,1)
        grid_layout1.addWidget(self.btn_add_wt_gusset,4,2)
        
        #Surface Area
        grid_layout1.addWidget(self.lbl_base_comp_ring_surface_area,5,0)
        grid_layout1.addWidget(self.tb_base_comp_ring_surface_area,5,1)
        grid_layout1.addWidget(self.btn_add_base_comp_ring_surface_area,5,2)
        
        
        #Comp Ring
        grid_layout1.addWidget(self.lbl_wdth_Comp_plt,0,3)
        grid_layout1.addWidget(self.tb_wdth_Comp_plt,0,4)
        grid_layout1.addWidget(self.lbl_len_Comp_plt,1,3)
        grid_layout1.addWidget(self.tb_len_Comp_plt,1,4)
        grid_layout1.addWidget(self.lbl_wt_Comp_plt,2,3)
        grid_layout1.addWidget(self.tb_wt_Comp_plt,2,4)
        grid_layout1.addWidget(self.btn_add_wt_Comp_plt,2,5)
        grid_layout1.addWidget(self.lbl_wt_BOM_Comp_plt,3,3)
        grid_layout1.addWidget(self.tb_wt_BOM_Comp_plt,3,4)
        grid_layout1.addWidget(self.btn_add_wt_BOM_Comp_plt,3,5)
        grid_layout1.addWidget(self.lbl_wt_washer,4,3)
        grid_layout1.addWidget(self.tb_wt_washer,4,4)
        grid_layout1.addWidget(self.btn_add_wt_washer,4,5)
        
        self.grpbox1_op.setLayout(grid_layout1)
        
    def SetUp_op_GrpBox2(self):
        
         #Template(ring+template)
        self.lbl_ring_and_ring_template_wt=QLabel("Ring+Ring Template Wt")
        self.tb_ring_and_ring_template_wt=QLineEdit("XXX")
        self.tb_ring_and_ring_template_wt.setDisabled(True)
        self.btn_ring_and_ring_template_wt=QPushButton("Add")
        
        #Template(box+template)
        self.lbl_box_and_ring_template_wt=QLabel("Box+Ring Template Wt")
        self.tb_box_and_ring_template_wt=QLineEdit("XXX")
        self.tb_box_and_ring_template_wt.setDisabled(True)
        self.btn_box_and_ring_template_wt=QPushButton("Add")
        
      

        grid_layout2=QGridLayout()           
        grid_layout2.addWidget(self.lbl_ring_and_ring_template_wt,0,0)
        grid_layout2.addWidget(self.tb_ring_and_ring_template_wt,0,1)
        grid_layout2.addWidget(self.btn_ring_and_ring_template_wt,0,2) 
        grid_layout2.addWidget(self.lbl_box_and_ring_template_wt,1,0)
        grid_layout2.addWidget(self.tb_box_and_ring_template_wt,1,1)
        grid_layout2.addWidget(self.btn_box_and_ring_template_wt,1,2) 
        self.grpbox2_op.setLayout(grid_layout2)
         


    def Calculate_Outputs(self):
        
        #Intermediate Outputs
        bolt_count=int(self.tb_bolt_count.text())
        No_of_gusset_plt=2*bolt_count 
        self.tb_No_of_gusset_plt.setText(str(No_of_gusset_plt))
        bolt_size= int(self.tb_bolt_size.text())
        gusset_detail=DBController.Get_gusset_detail(bolt_size)
        gusset_ht=float(gusset_detail.H)
        self.tb_gusset_ht.setText(str(gusset_ht))
        gusset_wd_at_top=float(gusset_detail.A)+float(gusset_detail.B)
        gusset_wd_at_btm=float(gusset_detail.L)-float(gusset_detail.K)
        self.tb_gusset_wd_at_top.setText(str(gusset_wd_at_top))
        self.tb_gusset_wd_at_btm.setText(str(gusset_wd_at_btm))
        BCD=float(self.tb_BCD.text())
        self.tb_comp_ring_ID.setText(str(BCD-2*float(gusset_detail.A)))
        self.tb_comp_ring_OD.setText(str(BCD+2*float(gusset_detail.B)))
        self.tb_base_ring_ID.setText(str(BCD-2*(float(gusset_detail.A)+float(gusset_detail.K))))
        self.tb_base_ring_OD.setText(str(float(self.tb_base_ring_ID.text())+2*float(gusset_detail.L)))
        self.tb_washer_dia.setText(str(float(gusset_detail.F)))
        
        
       #---------#
       #Outputs
       #----------#
       
       #Base Plt
        n_base_ring=int(self.tb_No_of_joints_Base_plt.text())
        OD_base_ring=float(self.tb_base_ring_OD.text())
        ID_base_ring=float(self.tb_base_ring_ID.text())
        wdth_of_base_plt = self.BasePlt_Size_Wd(n_base_ring,OD_base_ring)
        len_of_base_plt = self.BasePlt_Size_Lg(n_base_ring,OD_base_ring,ID_base_ring)
        density=float(self.tb_density.text())*0.000001
        thk_base_plt=float(self.tb_thk_Base_plt.text())
        wt_base_ring = round(wdth_of_base_plt*len_of_base_plt*thk_base_plt*density,1)
        wt_BOM_base_ring= round(math.pi/4*(OD_base_ring**2-ID_base_ring**2)*thk_base_plt*density,1)
        
        #Gusets
        thk_gusset=float(self.tb_gusset_thk.text())       
        wt_gusset=round(No_of_gusset_plt*gusset_ht*gusset_wd_at_top*thk_gusset*density)
        
        #Comp Ring
        n_comp_ring=int(self.tb_No_of_joints_Comp_plt.text())
        No_of_bolts=int(self.tb_bolt_count.text())
        OD_comp_ring=float(self.tb_comp_ring_OD.text())
        ID_comp_ring=float(self.tb_comp_ring_ID.text())
        thk_comp_plt=float(self.tb_thk_Comp_plt.text())
        is_ring=self.tb_Compression.text().lower()=='ring'       
        wdth_of_comp_plt= self.BasePlt_Size_Wd(n_comp_ring,OD_comp_ring) if(is_ring) else (ID_comp_ring)
        len_of_comp_plt=self.BasePlt_Size_Lg(n_comp_ring,OD_comp_ring,ID_comp_ring) if(is_ring) else (OD_comp_ring) 
        wt_comp_ring =  round(wdth_of_comp_plt*len_of_comp_plt*thk_comp_plt*density,1) if(is_ring) else round(wdth_of_comp_plt*len_of_comp_plt*thk_comp_plt*density*No_of_bolts,1)
        wt_BOM_comp_ring = round(math.pi/4*(OD_comp_ring**2-ID_comp_ring**2)*thk_comp_plt*density,1) if(is_ring) else round(wdth_of_comp_plt*len_of_comp_plt*thk_comp_plt*density*No_of_bolts,1) 
        
        #Washer
        OD_washer=float(self.tb_washer_dia.text())
        thk_washer=float(self.tb_washer_Thk.text())
        ID_washer=float(OD_washer-bolt_size)
        wt_washer=round(math.pi/4*(OD_washer**2-ID_washer**2)*thk_washer*No_of_bolts*density,1)
        
        
        #Surface Area
        surface_area_base_ring=math.pi/4*((OD_base_ring/1000)**2-(ID_base_ring/1000)**2)+math.pi*OD_base_ring*thk_base_plt/1000/1000*2
        surface_area_comp_ring=math.pi/4*((OD_comp_ring/1000)**2-(ID_comp_ring/1000)**2)+math.pi*OD_comp_ring*thk_comp_plt/1000/1000*2
        surface_area_gusset=gusset_ht*gusset_wd_at_top/1000/1000*No_of_gusset_plt*2
        surface_arae_base_comp_ring=round(surface_area_base_ring+surface_area_comp_ring+surface_area_gusset,1)
        
        #Template
        Wt_ring_and_ring_template=round(float(self.tb_template_Thk.text())*wt_base_ring/thk_base_plt*2,1)
        Wt_box_and_ring_template=round(Wt_ring_and_ring_template*3/2*1.2,1)
        
        #Update OP groupboxes
        self.tb_wdth_Base_plt.setText(str(wdth_of_base_plt))
        self.tb_len_Base_plt.setText(str(len_of_base_plt))
        self.tb_wt_Base_plt.setText(str(wt_base_ring))
        self.tb_wt_BOM_Base_plt.setText(str(wt_BOM_base_ring))
        self.tb_wt_gusset.setText(str(wt_gusset))
        self.tb_wdth_Comp_plt.setText(str(wdth_of_comp_plt))
        self.tb_len_Comp_plt.setText(str(len_of_comp_plt))
        self.tb_wt_Comp_plt.setText(str(wt_comp_ring))
        self.tb_wt_BOM_Comp_plt.setText(str(wt_BOM_comp_ring))
        self.tb_wt_washer.setText(str(wt_washer))
        self.tb_base_comp_ring_surface_area.setText(str(surface_arae_base_comp_ring))
        
        #Upxate Templaet OP groupbox
        self.tb_ring_and_ring_template_wt.setText(str(Wt_ring_and_ring_template))
        self.tb_box_and_ring_template_wt.setText(str(Wt_box_and_ring_template))
        
        #Define Button functionality
        self.btn_add_wt_Base_plt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
                                                                           {'item':'Base Ring',
                                                                            'item_name':'Base Ring'+str(self.Number),
                                                                            'wt':str(wt_base_ring),
                                                                            'material':self.cmb_box_material.currentText()
                                                                            }))
        
        self.btn_add_wt_BOM_Base_plt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
                                                            {'item':'Base Ring',
                                                            'item_name':'Base Ring BOM'+str(self.Number),
                                                            'wt':str(wt_BOM_base_ring),
                                                            'material':self.cmb_box_material.currentText()
                                                            }))

        self.btn_add_wt_Comp_plt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
                                                            {'item':'Comp Ring',
                                                            'item_name':'Comp Ring'+str(self.Number),
                                                            'wt':str(wt_comp_ring),
                                                            'material':self.cmb_box_material.currentText()
                                                            }))
        
        self.btn_add_wt_BOM_Comp_plt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
                                                            {'item':'Comp Ring',
                                                            'item_name':'Comp Ring BOM'+str(self.Number),
                                                            'wt':str(wt_BOM_comp_ring),
                                                            'material':self.cmb_box_material.currentText()
                                                            }))
        
        self.btn_add_wt_gusset.clicked.connect(lambda:self.Add_wt_to_BOM(data=
                                                            {'item':'Gusset',
                                                            'item_name':'Gusset'+str(self.Number),
                                                            'wt':str(wt_gusset),
                                                            'material':self.cmb_box_material.currentText()
                                                            }))
        
        self.btn_add_wt_washer.clicked.connect(lambda:self.Add_wt_to_BOM(data=
                                                            {'item':'Washer',
                                                            'item_name':'Washer'+str(self.Number),
                                                            'wt':str(wt_washer),
                                                            'material':self.cmb_box_material.currentText()
                                                            }))
        
        self.btn_add_base_comp_ring_surface_area.clicked.connect(lambda:self.Add_SurfaceArea_to_BOM(data=
                                                            {'item':'Gusset',
                                                            'item_name':'Gusset'+str(self.Number),
                                                            'surface_area':str(surface_arae_base_comp_ring)                                                            
                                                            }))
        self.btn_ring_and_ring_template_wt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
                                                            {'item':'Ring+Ring_Template',
                                                            'item_name':'Ring+Ring_Template'+str(self.Number),
                                                            'wt':str(Wt_ring_and_ring_template),
                                                             'material':self.cmb_box_material.currentText()                                                           
                                                            }))
        
        self.btn_box_and_ring_template_wt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
                                                            {'item':'Box+Ring_Template',
                                                            'item_name':'Box+Ring_Template'+str(self.Number),
                                                            'wt':str(Wt_box_and_ring_template),
                                                             'material':self.cmb_box_material.currentText()                                                           
                                                            }))

        
        #self.change_button_color_green()#Change color of the Calc button
        self.reset_button_color_default()#Reset the color of Add  to BOM as Weight value got changed.
            
    def update_material(self) :
        #This will update the Material in the Shell OPutput Groupbox
        #self.tb_shell_op_Material.setText(str(self.cmb_box_material.currentText()))
        #print(i)
        pass
    def update_skirt_type(self):
        #print(self.cmb_box_skirt_type.currentText())

        #Hide Cone_angle label and text if skirt_type not eq to 'shell'
        if(str.lower(self.cmb_box_skirt_type.currentText())=='cone'):
            self.lbl_cone_angle.setHidden(False)
            self.tb_cone_angle.setHidden(False)
        else:
            self.lbl_cone_angle.setHidden(True)
            self.tb_cone_angle.setHidden(True)

    def Add_wt_to_BOM(self,data):
        print("Add Shell Material to BOM Pressed")
        _projectcontroller=ProjectController()
        _projectcontroller.add_update_item(item=data['item'],item_name=data['item_name'],wt=data['wt'],material=data['material'])
        print(data)
        self.change_button_color_green()
        
    def Add_SurfaceArea_to_BOM(self,data):
         _projectcontroller=ProjectController()
         _projectcontroller.add_update_surface_area(item=data['item'],item_name=data['item_name'],surface_area=data['surface_area'])
         self.change_button_color_green()

    # @staticmethod
    # def calculate_allwnce_on_dia(ID, T):
    #     OD = ID + 2 * T
            
    #     if T > 100:
    #         Allow = 300
    #     elif 50 < T <= 100:
    #         Allow = 2 * T
    #     elif (30 < T < 50) and (OD / T) <= 24:
    #         Allow = 2 * T
    #     elif (T <= 30) and (OD / T) <= 15:
    #         Allow = 1 * T
    #     else:
    #         Allow = 0
    #     print(ID,OD,T,Allow)    
    #     return Allow
   
    @staticmethod
    def BasePlt_Size_Wd(n, OD):  
        #'This Function is used to calculate the width required for the base plate development
        #' n = no. of Joints required, OD = Base Ring OD

        T = 360 / (2 * n)
        Pi = 22 / 7
        R1 = (OD / 2) + 5
        Wd = 2 * R1 * math.sin(T * Pi / 180)
        return round(Wd)
    
    @staticmethod
    def BasePlt_Size_Lg(n, OD, ID):     
    # 'This Function is used to calculate the Length of plate required of the base plate development
    # ' n = no. of Joints required, OD = Base Ring OD, ID = Base RIng ID

        T = 360 / (2 * n)
        Pi = 22 / 7
        R1 = (OD / 2) + 9
        R2 = (ID / 2) - 9
        x = R2 * math.cos(T * Pi / 180)
        y = R2 * math.sin(T * Pi / 180)
        Lg = (R1 - x) + (n - 1) * (math.sqrt(R1 ** 2 - y ** 2) - x)
        return round(Lg)
        
   
    #This function changes the coor of sender button to green
    def change_button_color_green(self):
        button = self.sender()
        button.setStyleSheet("background-color: green; color: white;")

    #This Function reset the color of "button" passed as an argument.
    def reset_button_color_default(self):
        #button = self.sender()
        for button in self.grpbox1_op.findChildren(QPushButton):
            button.setStyleSheet("")  # Reset the color      

class Nozzle_DEnd(QWidget):  
    def __init__(self) -> None:
        super().__init__()
        self.InitializeUI()
        
    def InitializeUI(self):
        self.grpbox_Nozzle=QGroupBox("Nozzle on Bottom D'ENd")
        self.grpbox_Nozzle.setFixedWidth(800)
        self.grpbox_Nozzle.setStyleSheet(Custom_Style.op_grpbox_style)        
        self.SetUI_Nozzle()      
        
        self.Vbox_layout_Nozzle=QVBoxLayout()
        self.Vbox_layout_Nozzle.addWidget(self.grpbox_Nozzle)
        self.setLayout(self.Vbox_layout_Nozzle)
        
    def SetUI_Nozzle(self):
              
        self.lbl_nozzle_class=QLabel("Class")
        self.lbl_nozzle_class.setStyleSheet("background-color:#ccffcc")
        self.cmbbox_nozzle_class=QComboBox() 
        self.cmbbox_nozzle_class.setStyleSheet("background-color:#ccffcc")
        self.cmbbox_nozzle_class.addItems([str(item) for item in  var.Nozzle_class])
        
        self.lbl_nozzle_NPS=QLabel("NPS")
        self.lbl_nozzle_NPS.setStyleSheet("background-color:#ccffcc")
        self.cmbbox_nozzle_NPS=QComboBox()
        self.cmbbox_nozzle_NPS.setStyleSheet("background-color:#ccffcc") 
        self.cmbbox_nozzle_NPS.addItems([str(item) for item in  var.NPS_list])
        
        self.lbl_nozzle_schedule=QLabel("Schedule")
        self.lbl_nozzle_schedule.setStyleSheet("background-color:#ccffcc")        
        self.cmbbox_nozzle_schedule=QComboBox()
        self.cmbbox_nozzle_schedule.setStyleSheet("background-color:#ccffcc") 
        self.cmbbox_nozzle_schedule.addItems([str(item) for item in  var.Schedule_list])
        
        self.lbl_90LR_Elbow_wt=QLabel("Wt of 90LR Elbow")
        self.tb_90LR_Elbow_wt=QLineEdit("XX")
        self.tb_90LR_Elbow_wt.setEnabled(False)        
        self.lbl_90LR_Elbow_material=QLabel("Material")
        self.lbl_90LR_Elbow_material.setStyleSheet("background-color:#ccffcc") 
        self.cmbbox_90LR_Elbow_material=QComboBox()
        self.cmbbox_90LR_Elbow_material.setStyleSheet("background-color:#ccffcc") 
        self.cmbbox_90LR_Elbow_material.addItems(var.master_mat_list)
        self.btn_90LR_Elbow_wt=QPushButton("Add to BOM")
        self.btn_90LR_Elbow_wt.setFixedWidth(120)   
             
        self.lbl_len_of_projection=QLabel("Proj. len from nozzle cntr")
        self.lbl_len_of_projection.setStyleSheet("background-color:#ccffcc")
        self.tb_len_of_projection=QLineEdit("730")
        self.tb_len_of_projection.setStyleSheet("background-color:#ccffcc")
        self.lbl_pipe_thk=QLabel("Pipe Thk")
        self.tb_pipe_thk=QLineEdit("XX")
        self.tb_pipe_thk.setEnabled(False)
        
        self.lbl_sleeve_pad_wt=QLabel("Wt of Sleeve Pad")
        self.tb_sleeve_pad_wt=QLineEdit("XX")
        self.tb_sleeve_pad_wt.setEnabled(False)
        self.lbl_sleeve_pad_material=QLabel("Material")
        self.lbl_sleeve_pad_material.setStyleSheet("background-color:#ccffcc")
        self.cmbbox_sleeve_pad_material=QComboBox()
        self.cmbbox_sleeve_pad_material.setStyleSheet("background-color:#ccffcc") 
        self.cmbbox_sleeve_pad_material.addItems(var.master_mat_list)
        self.btn_sleeve_pad_wt=QPushButton("Add to BOM")
        self.btn_sleeve_pad_wt.setFixedWidth(120)  
        
        self.lbl_horz_pipe_wt=QLabel("Wt of Horz Pipe(B'DEnd)")
        self.tb_horz_pipe_wt=QLineEdit("XX")
        self.tb_horz_pipe_wt.setEnabled(False)
        self.lbl_horz_pipe_material=QLabel("Material")
        self.lbl_horz_pipe_material.setStyleSheet("background-color:#ccffcc")
        self.cmbbox_horz_pipe_material=QComboBox() 
        self.cmbbox_horz_pipe_material.setStyleSheet("background-color:#ccffcc")
        self.cmbbox_horz_pipe_material.addItems(var.master_mat_list)
        self.btn_horz_pipe_wt=QPushButton("Add to BOM")
        self.btn_horz_pipe_wt.setFixedWidth(120) 
        
        self.lbl_pipe_open_pad_wt=QLabel("Wt of Pipe OPen Pad")
        self.tb_pipe_open_pad_wt=QLineEdit("XX")
        self.tb_pipe_open_pad_wt.setEnabled(False)
        self.lbl_pipe_open_pad_material=QLabel("Material")
        self.lbl_pipe_open_pad_material.setStyleSheet("background-color:#ccffcc")
        self.cmbbox_pipe_open_pad_material=QComboBox()
        self.cmbbox_pipe_open_pad_material.setStyleSheet("background-color:#ccffcc") 
        self.cmbbox_pipe_open_pad_material.addItems(var.master_mat_list)
        self.btn_pipe_open_pad_wt=QPushButton("Add to BOM")
        self.btn_pipe_open_pad_wt.setFixedWidth(120)
        
        self.lbl_pipe_OD=QLabel("Pipe OD")
        self.tb_pipe_OD=QLineEdit("XX")
        self.tb_pipe_OD.setEnabled(False)
        self.lbl_Flange_OD=QLabel("Flange OD")
        self.tb_Flange_OD=QLineEdit("XX")
        self.tb_Flange_OD.setEnabled(False) 
        self.lbl_pipe_pad_Lg1=QLabel("Pipe Pad Lg1")
        self.tb_pipe_pad_Lg1=QLineEdit("XX")
        self.tb_pipe_pad_Lg1.setEnabled(False)
        self.lbl_pipe_pad_Lg2=QLabel("Pipe Pad Lg2")
        self.tb_pipe_pad_Lg2=QLineEdit("XX")
        self.tb_pipe_pad_Lg2.setEnabled(False)
        
        self.btn_calc_Nozzle_op=QPushButton("Calculate Wt")
        self.btn_calc_Nozzle_op.setFixedWidth(120)
        self.btn_calc_Nozzle_op.clicked.connect(self.Calc_Nozzle_op)
               

        gridlayout_Nozzle=QGridLayout()
        gridlayout_Nozzle.addWidget(self.lbl_nozzle_class,1,0)
        gridlayout_Nozzle.addWidget(self.cmbbox_nozzle_class,1,1)        
        gridlayout_Nozzle.addWidget(self.lbl_nozzle_NPS,1,2)
        gridlayout_Nozzle.addWidget(self.cmbbox_nozzle_NPS,1,3)
        gridlayout_Nozzle.addWidget(self.lbl_nozzle_schedule,2,0)
        gridlayout_Nozzle.addWidget(self.cmbbox_nozzle_schedule,2,1)
        gridlayout_Nozzle.addWidget(self.lbl_90LR_Elbow_material,2,2)       
        gridlayout_Nozzle.addWidget(self.cmbbox_90LR_Elbow_material,2,3) 
        gridlayout_Nozzle.addWidget(self.btn_calc_Nozzle_op,3,2)
        gridlayout_Nozzle.addWidget(self.lbl_90LR_Elbow_wt,4,0)
        gridlayout_Nozzle.addWidget(self.tb_90LR_Elbow_wt,4,1)        
        gridlayout_Nozzle.addWidget(self.btn_90LR_Elbow_wt,4,2)
        
        gridlayout_Nozzle.addWidget(self.lbl_len_of_projection,6,0)
        gridlayout_Nozzle.addWidget(self.tb_len_of_projection,6,1)
        gridlayout_Nozzle.addWidget(self.lbl_pipe_thk,6,2)
        gridlayout_Nozzle.addWidget(self.tb_pipe_thk,6,3)
        
        gridlayout_Nozzle.addWidget(self.lbl_Flange_OD,7,0)
        gridlayout_Nozzle.addWidget(self.tb_Flange_OD,7,1)
        gridlayout_Nozzle.addWidget(self.lbl_pipe_OD,7,2)
        gridlayout_Nozzle.addWidget(self.tb_pipe_OD,7,3)        
       
        gridlayout_Nozzle.addWidget(self.lbl_pipe_pad_Lg1,8,0)
        gridlayout_Nozzle.addWidget(self.tb_pipe_pad_Lg1,8,1)
        gridlayout_Nozzle.addWidget(self.lbl_pipe_pad_Lg2,8,2)
        gridlayout_Nozzle.addWidget(self.tb_pipe_pad_Lg2,8,3)
        
        gridlayout_Nozzle.addWidget(self.lbl_sleeve_pad_wt,9,0)
        gridlayout_Nozzle.addWidget(self.tb_sleeve_pad_wt,9,1)
        gridlayout_Nozzle.addWidget(self.cmbbox_sleeve_pad_material,9,2)
        gridlayout_Nozzle.addWidget(self.btn_sleeve_pad_wt,9,3)
        
        gridlayout_Nozzle.addWidget(self.lbl_horz_pipe_wt,10,0)
        gridlayout_Nozzle.addWidget(self.tb_horz_pipe_wt,10,1)
        gridlayout_Nozzle.addWidget(self.cmbbox_horz_pipe_material,10,2)
        gridlayout_Nozzle.addWidget(self.btn_horz_pipe_wt,10,3)
        
        gridlayout_Nozzle.addWidget(self.lbl_pipe_open_pad_wt,11,0)
        gridlayout_Nozzle.addWidget(self.tb_pipe_open_pad_wt,11,1)
        gridlayout_Nozzle.addWidget(self.cmbbox_pipe_open_pad_material,11,2)
        gridlayout_Nozzle.addWidget(self.btn_pipe_open_pad_wt,11,3)
         
       
       
        
        self.grpbox_Nozzle.setLayout(gridlayout_Nozzle)
        
    def Calc_Nozzle_op(self):
       
        elbow_detail=Get_Elbow_Details(nps=self.cmbbox_nozzle_NPS.currentText(),schedule=self.cmbbox_nozzle_schedule.currentText())
        self.elbow_90LR_elbow_Wt=float(elbow_detail.Wt)
        self.tb_90LR_Elbow_wt.setText(str(self.elbow_90LR_elbow_Wt))
        
        self.pipe_thk=float(elbow_detail.THK)
        self.tb_pipe_thk.setText(str(self.pipe_thk))
        
        WN_FLG_detail=Get_WL_FLG_detail(nps=self.cmbbox_nozzle_NPS.currentText(),classs=self.cmbbox_nozzle_class.currentText())
        
        self.sleev_pad_wt=round(var.Skirt_thk*2*(float(WN_FLG_detail.flg_od)+20)*2*(float(WN_FLG_detail.flg_od)+20)*0.00000785,1)        
        self.tb_sleeve_pad_wt.setText(str(self.sleev_pad_wt))
        
        self.proj_len=float(self.tb_len_of_projection.text())
        self.tb_len_of_projection.setText(str(self.proj_len))
        
        self.Bot_DEnd_horz_pipe_wt=round((float(elbow_detail.WtPerMtr)*(self.proj_len-float(elbow_detail.Ht))-(float(WN_FLG_detail.flg_ht_wn_incld_rf)+20))/1000,1)
        self.tb_horz_pipe_wt.setText(str(self.Bot_DEnd_horz_pipe_wt))
        
        self.pipe_OD=round(float(elbow_detail.NOZL_OD),1)
        self.tb_pipe_OD.setText(str(self.pipe_OD))
        
        self.flg_od=math.ceil(float(WN_FLG_detail.flg_od)+2*self.pipe_thk)
        self.tb_Flange_OD.setText(str(self.flg_od))
        
        self.pipe_pad_Lg1=math.ceil(self.flg_od+2*min(14,var.Skirt_thk+2)+2*(self.flg_od/2))
        self.pipe_pad_Lg2=math.ceil(self.OPad_Lg(var.Skirt_ID,var.Skirt_thk,self.flg_od,(self.flg_od/2),min(14,var.Skirt_thk),self.pipe_thk,0))
        self.tb_pipe_pad_Lg1.setText(str(self.pipe_pad_Lg1))
        self.tb_pipe_pad_Lg2.setText(str(self.pipe_pad_Lg2))
        
        self.pipe_open_pad_wt=round(self.pipe_pad_Lg1*self.pipe_pad_Lg2*14*0.00000785,1)
        self.tb_pipe_open_pad_wt.setText(str(self.pipe_open_pad_wt))
        
        #Define Button functionality
        self.btn_90LR_Elbow_wt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
                                                                           {'item':'Bottom DEnd Nozzle Elbow',
                                                                            'item_name':'Bottom DEnd Nozzle Elbow',
                                                                            'wt':str(self.elbow_90LR_elbow_Wt),
                                                                            'material':self.cmbbox_90LR_Elbow_material.currentText()
                                                                            }))
        self.btn_sleeve_pad_wt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
                                                                           {'item':'Bottom DEnd Nozzle Sleeve Pad',
                                                                            'item_name':'Bottom DEnd Nozzle Sleeve Pad',
                                                                            'wt':str(self.sleev_pad_wt),
                                                                            'material':self.cmbbox_sleeve_pad_material.currentText()
                                                                            }))
        self.btn_horz_pipe_wt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
                                                                           {'item':'Bottom DEnd Horz Pipe',
                                                                            'item_name':'Bottom DEnd Horz Pipe',
                                                                            'wt':str(self.Bot_DEnd_horz_pipe_wt),
                                                                            'material':self.cmbbox_horz_pipe_material.currentText()
                                                                            }))
        self.btn_pipe_open_pad_wt.clicked.connect(lambda:self.Add_wt_to_BOM(data=
                                                                           {'item':'Bottom DEnd Pipe Opening Pad',
                                                                            'item_name':'Bottom DEnd Pipe Opening Pad',
                                                                            'wt':str(self.pipe_open_pad_wt),
                                                                            'material':self.cmbbox_pipe_open_pad_material.currentText()
                                                                            }))
        
        self.reset_button_color_default()#Reset the color of Add  to BOM as Weight value got changed.
        
    def Add_wt_to_BOM(self,data):        
        _projectcontroller=ProjectController()
        _projectcontroller.add_update_item(item=data['item'],item_name=data['item_name'],wt=data['wt'],material=data['material'])
        print(data)
        self.change_button_color_green()        
        
    @staticmethod   
    def OPad_Lg(ID, Thk, NOD, PadWd, PadThk, NozlThk, OffDist):
    #  'This Function is used to cal. Pad Lg1. of OffSetNozl.
    # ' a stands for angle

        ShellOR = ID / 2 + Thk
        AE = ShellOR + PadThk
        DE = OffDist - (NOD / 2)
        x = math.sqrt(AE ** 2 - DE ** 2)
        a1 = math.atan(DE / x)
        GF = OffDist + (NOD / 2)
        AF = (ID / 2) + Thk
        y = math.sqrt(AF ** 2 - GF ** 2)
        a2 = math.atan(GF / y)
        a = a2 - a1
        PADMR = ShellOR + (PadThk / 2)
        OPad_Lg = a * PADMR + 2 * PadWd   
        return OPad_Lg 

    #This function changes the coor of sender button to green
    def change_button_color_green(self):
            button = self.sender()
            button.setStyleSheet("background-color: green; color: white;")

    #This Function reset the color of "button" passed as an argument.
    def reset_button_color_default(self):
            #button = self.sender()
            for button in self.grpbox_Nozzle.findChildren(QPushButton):
                button.setStyleSheet("")  # Reset the color      




class Custom_Style:
    op_grpbox_style="""
                QGroupBox {
                    font: bold;
                    font-size:14px;
                    padding: 15px;
                    border: 1px solid silver;
                    border-radius: 6px;
                    margin-top: 5px;
                    background-color:lightgrey                     

        } """  