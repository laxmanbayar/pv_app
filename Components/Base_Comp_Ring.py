import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout,QWidget, \
    QTabWidget,QGroupBox,QTableWidget,QTableWidgetItem,QGridLayout
from Variables import var
from PyQt6.QtCore import Qt
import math

class Tab3_Base_Comp_Ring(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
    def InitializeUI(self):
        H_box_layout= QHBoxLayout() 
        base_comp_ring_gusset=Base_Comp_Ring_Gusset() 
        #comp_ring=Comp_Ring()
        H_box_layout.addWidget(base_comp_ring_gusset)
        #H_box_layout.addWidget(comp_ring)

        V_box_main_layout=QVBoxLayout()
        V_box_main_layout.addLayout(H_box_layout)
        #Misc_items = Misc()
        
        #V_box_main_layout.addWidget(Misc_items)

        self.setLayout(V_box_main_layout)

class Base_Comp_Ring_Gusset(QWidget):

    def __init__(self):
        super().__init__()
        self.InitializeUI()
      

    def InitializeUI(self):

        self.set_styles()
        self.SetUp_ip_GrpBox()#GropBox1
        self.SetUp_intermediate_op_GrpBox()#GropBox2
        self.HBox_layout_ip =QHBoxLayout()         
        self.HBox_layout_ip.addWidget(self.grpbox1)
        self.HBox_layout_ip.addWidget(self.grpbox2)

        
        self.HBox_layout_op=QHBoxLayout()
        self.SetUp_op_GrpBox1()#Groupbox3
        self.HBox_layout_op.addWidget(self.grpbox1_op)
        self.SetUp_op_GrpBox2()#Groupbox3
        self.HBox_layout_op.addWidget(self.grpbox2_op)
        
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
                    background-color:lightgreen
                                        
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

        self.lbl_BCD =QLabel("BCD")
        self.tb_BCD =QLineEdit("1150")

        self.lbl_gusset_thk =QLabel("Gusset Thk")
        self.tb_gusset_thk =QLineEdit("18")

        self.lbl_washer_Thk=QLabel("Washer Thk")
        self.tb_washer_Thk =QLineEdit("20")

        self.lbl_Compression=QLabel("Compression")
        self.tb_Compression =QLineEdit("Ring")



        #Create VBox Input
        self.VBox_layout1 =QVBoxLayout()
       
        self.VBox_layout1.addWidget(self.lbl_material)
        self.VBox_layout1.addWidget(self.cmb_box_material)
        self.VBox_layout1.addWidget(self.lbl_density)
        self.VBox_layout1.addWidget(self.tb_density)
        self.VBox_layout1.addWidget(self.lbl_skirt_type)
        self.VBox_layout1.addWidget(self.cmb_box_skirt_type)
        self.VBox_layout1.addWidget(self.lbl_cone_angle)
        self.VBox_layout1.addWidget(self.tb_cone_angle)
        self.VBox_layout1.addWidget(self.lbl_BCD)
        self.VBox_layout1.addWidget(self.tb_BCD)
        self.VBox_layout1.addWidget(self.lbl_gusset_thk)
        self.VBox_layout1.addWidget(self.tb_gusset_thk)
        self.VBox_layout1.addWidget(self.lbl_washer_Thk)
        self.VBox_layout1.addWidget(self.tb_washer_Thk)
        self.VBox_layout1.addWidget(self.lbl_Compression)#
        self.VBox_layout1.addWidget(self.tb_Compression)
       
        self.btn_calc_shell_wt=QPushButton("Calculate Inermediate Op")
        self.btn_calc_shell_wt.clicked.connect(self.Calculate_Intermediate_op)
        self.VBox_layout1.addWidget(self.btn_calc_shell_wt,0,Qt.AlignmentFlag.AlignHCenter)

        #Create a GroupBox1 and set its layout to VBox_layout1
        self.grpbox1 = QGroupBox("Input(Base Ring , Comp Ring , Gusset , Washer)",self)
        self.grpbox1.setStyleSheet(self.ip_grpbox1_style)
        self.grpbox1.setLayout(self.VBox_layout1)
    

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

        #Create Groupbox2 and sets its layout to Vbox_layout2
        self.grpbox2 = QGroupBox("Intermediate Op",self)
        self.grpbox2.setStyleSheet(self.ip_grpbox2_style)
        self.grpbox2.setLayout(self.VBox_layout2)
        self.grpbox2.setDisabled(True)
              
        
    def SetUp_op_GrpBox1(self):#Base Ring and Gusset
       
        self.lbl_No_of_joints_Base_plt=QLabel("No. of Joints")
        self.lbl_No_of_joints_Base_plt.setStyleSheet(self.ip_textbox_style)
        self.tb_No_of_joints_Base_plt=QLineEdit("4")
        self.tb_No_of_joints_Base_plt.setStyleSheet(self.ip_textbox_style)
        self.lbl_thk_Base_plt=QLabel("Base Plt Thk")
        self.lbl_thk_Base_plt.setStyleSheet(self.ip_textbox_style)
        self.tb_thk_Base_plt=QLineEdit("4")
        self.tb_thk_Base_plt.setStyleSheet(self.ip_textbox_style)
        
        self.lbl_wdth_Base_plt=QLabel("Base Plt Width")
        self.tb_wdth_Base_plt=QLineEdit("4")
        self.tb_wdth_Base_plt.setDisabled(True)
        self.lbl_len_Base_plt=QLabel("Base Plt Length")
        self.tb_len_Base_plt=QLineEdit("4")
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
        self.tb_wt_gusset=QLineEdit("4")
        self.tb_wt_gusset.setDisabled(True)
        self.btn_add_wt_gusset=QPushButton("Add")

        grid_layout1=QGridLayout()
        grid_layout1.addWidget(self.lbl_No_of_joints_Base_plt,0,0)
        grid_layout1.addWidget(self.tb_No_of_joints_Base_plt,0,1)
        grid_layout1.addWidget(self.lbl_thk_Base_plt,1,0)
        grid_layout1.addWidget(self.tb_thk_Base_plt,1,1)
        grid_layout1.addWidget(self.lbl_wdth_Base_plt,2,0)
        grid_layout1.addWidget(self.tb_wdth_Base_plt,2,1)
        grid_layout1.addWidget(self.lbl_len_Base_plt,3,0)
        grid_layout1.addWidget(self.tb_len_Base_plt,3,1)
        grid_layout1.addWidget(self.lbl_wt_Base_plt,4,0)
        grid_layout1.addWidget(self.tb_wt_Base_plt,4,1)
        grid_layout1.addWidget(self.btn_add_wt_Base_plt,4,2)
        grid_layout1.addWidget(self.lbl_wt_BOM_Base_plt,5,0)
        grid_layout1.addWidget(self.tb_wt_BOM_Base_plt,5,1)
        grid_layout1.addWidget(self.btn_add_wt_BOM_Base_plt,5,2)
        grid_layout1.addWidget(self.lbl_wt_gusset,6,0)
        grid_layout1.addWidget(self.tb_wt_gusset,6,1)
        grid_layout1.addWidget(self.btn_add_wt_gusset,6,2)
       

        self.grpbox1_op= QGroupBox("Base Plt and Gusset",self)
        
        self.grpbox1_op.setStyleSheet(self.op_grpbox_style)  
        self.grpbox1_op.setLayout(grid_layout1)

    def SetUp_op_GrpBox2(self):#Comp Ring & Washer
        self.lbl_No_of_joints_Comp_plt=QLabel("No. of Joints")
        self.lbl_No_of_joints_Comp_plt.setStyleSheet(self.ip_textbox_style)
        self.tb_No_of_joints_Comp_plt=QLineEdit("4")
        self.tb_No_of_joints_Comp_plt.setStyleSheet(self.ip_textbox_style)
        self.lbl_thk_Comp_plt=QLabel("Comp Plt Thk")
        self.lbl_thk_Comp_plt.setStyleSheet(self.ip_textbox_style)
        self.tb_thk_Comp_plt=QLineEdit("4")
        self.tb_thk_Comp_plt.setStyleSheet(self.ip_textbox_style)
        
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

        grid_layout1=QGridLayout()
        grid_layout1.addWidget(self.lbl_No_of_joints_Comp_plt,0,0)
        grid_layout1.addWidget(self.tb_No_of_joints_Comp_plt,0,1)
        grid_layout1.addWidget(self.lbl_thk_Comp_plt,1,0)
        grid_layout1.addWidget(self.tb_thk_Comp_plt,1,1)
        grid_layout1.addWidget(self.lbl_wdth_Comp_plt,2,0)
        grid_layout1.addWidget(self.tb_wdth_Comp_plt,2,1)
        grid_layout1.addWidget(self.lbl_len_Comp_plt,3,0)
        grid_layout1.addWidget(self.tb_len_Comp_plt,3,1)
        grid_layout1.addWidget(self.lbl_wt_Comp_plt,4,0)
        grid_layout1.addWidget(self.tb_wt_Comp_plt,4,1)
        grid_layout1.addWidget(self.btn_add_wt_Comp_plt,4,2)
        grid_layout1.addWidget(self.lbl_wt_BOM_Comp_plt,5,0)
        grid_layout1.addWidget(self.tb_wt_BOM_Comp_plt,5,1)
        grid_layout1.addWidget(self.btn_add_wt_BOM_Comp_plt,5,2)
        grid_layout1.addWidget(self.lbl_wt_washer,6,0)
        grid_layout1.addWidget(self.tb_wt_washer,6,1)
        grid_layout1.addWidget(self.btn_add_wt_washer,6,2)
       

        self.grpbox2_op= QGroupBox("Comp Plt and Washer",self)
       
        self.grpbox2_op.setStyleSheet(self.op_grpbox_style)  
        self.grpbox2_op.setLayout(grid_layout1)



    def Calculate_Intermediate_op(self):
        #This Function calculates Shell wt & update it into Shell Op groupbox
        #allwnc_on_dia (a)   
        
        Lg=float(self.tb_bolt_size.text()) #Length
        E=float(self.tb_BCD.text())#Length Allwnc
        ID=float(self.tb_washer_Thk.text())#ID
        t=float(self.tb_gusset_thk.text())
        rho=float(self.tb_density.text())

        a=self.calculate_allwnce_on_dia(ID,t)
        self.tb_shell_allwnc_dia.setText(str(a))
        
        TL=Lg+E
        shell_wt =round(math.pi*(ID+a)*t*TL*rho*0.000001,2)
        self.tb_Shell_wt.setText(str(shell_wt))
        #print(shell_wt)
        self.btn_calc_shell_wt.setFocus()#Remove focus from Combox otherwise accidently can be changed by user
        self.reset_button_color_default(self.btn_add_shell_mat_to_BOM)#Reset the color of Add Material to BOM as Weight value got changed.
        
        
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

    def Add_Shell_mat_to_BOM(self):
        print("Add Shell Material to BOM Pressed")
        self.change_button_color_green()

    def calculate_allwnce_on_dia(_,ID, T):
        OD = ID + 2 * T
            
        if T > 100:
            Allow = 300
        elif 50 < T <= 100:
            Allow = 2 * T
        elif (30 < T < 50) and (OD / T) <= 24:
            Allow = 2 * T
        elif (T <= 30) and (OD / T) <= 15:
            Allow = 1 * T
        else:
            Allow = 0
        print(ID,OD,T,Allow)    
        return Allow
    #This function changes the coor of sender button to green
    def change_button_color_green(self):
        button = self.sender()
        button.setStyleSheet("background-color: green; color: white;")

    #This Function reset the color of "button" passed as an argument.
    def reset_button_color_default(self,button):
        #button = self.sender()
        button.setStyleSheet("")       


