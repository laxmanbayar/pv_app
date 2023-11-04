
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QLayout, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout,QWidget, \
    QTabWidget,QGroupBox,QTableWidget,QTableWidgetItem,QGridLayout,QScrollArea
from Variables import var
from PyQt6.QtCore import Qt,QRect
import math
from Controller.project_controller import ProjectController

class Tab_Shell(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
        
    def InitializeUI(self):
        
        #Variable to hold all shell() class instances 
        self.shell_instances=[]
        
        #Gridlayout for shell count label and combobox
        self.gridlayout=QGridLayout()     
        self.lbl_No_of_shell=QLabel("No. of Shell")
        self.lbl_No_of_shell.setStyleSheet("font: bold; font-size: 16px;")
       
        self.cmbbox_No_of_shell=QComboBox()
        self.cmbbox_No_of_shell.setStyleSheet("font: bold; font-size: 16px;")    
        self.cmbbox_No_of_shell.addItems(([str(x) for x in range(1,20,1)]))       
        self.cmbbox_No_of_shell.currentIndexChanged.connect(self.Set_No_of_Shell)        
        
        self.gridlayout.addWidget(self.lbl_No_of_shell,0,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout.addWidget(self.cmbbox_No_of_shell,0,1,alignment=Qt.AlignmentFlag.AlignLeft)
   

        #V_box_layout holds gridpayout and all the shells widget(hbox_shells)
        self.V_box_layout=QVBoxLayout()
        self.V_box_layout.addLayout(self.gridlayout)
        
        #hbox_shell_layout holds all the shell widgets (based on combobox value)
        self.hbox_shells_layout=QHBoxLayout()       
        self.V_box_layout.addLayout(self.hbox_shells_layout)
      
        # add one container widget and set its Lsyout as "V_box_layout"
        self.container_widget = QWidget()
        self.container_widget.setLayout(self.V_box_layout)

        # Create new Scroll area and set it as resizable
        self.scroll_area = QScrollArea()
        # self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        # self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setWidgetResizable(True)
       

        # Set the container widget as the widget for the scroll area
        self.scroll_area.setWidget(self.container_widget)
       

        # Add the scroll area to the main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.scroll_area)

        self.setLayout(main_v_box)
        self.cmbbox_No_of_shell.setCurrentIndex(2)

    def Set_No_of_Shell(self):
        
        for i in reversed(range(self.hbox_shells_layout.count())):
            widget = self.hbox_shells_layout.itemAt(i).widget()
            if widget is not None:
                widget.close()
       
        no_of_shells=int(self.cmbbox_No_of_shell.currentText())
        for _ in range(0,no_of_shells):
            shell=Shell()
            self.shell_instances.append(shell)         
            self.hbox_shells_layout.addWidget(shell)
        
        
        
class Shell(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
            
    def InitializeUI(self):
        self.set_ui_layout() 
                      
    def set_ui_layout(self):
        self.grpbox=QGroupBox("Shell")
        self.grpbox.setStyleSheet(set_styles.ip_grpbox1_style)
        self.grpbox_Vbox_layout_shell=QVBoxLayout()
        self.grpbox.setLayout(self.grpbox_Vbox_layout_shell)
        self.Vbox_main_shell=QVBoxLayout()
        self.Vbox_main_shell.addWidget(self.grpbox)
        self.setLayout(self.Vbox_main_shell)
        
        self.set_grpbox_UI()
        
    def set_grpbox_UI(self):
        
        #Input
        self.lbl_shell_desc =QLabel("Description")
        self.tb_shell_desc =QLineEdit("Shell xxxx")
        self.material_list = var.master_mat_list
        self.lbl_shell_material =QLabel("Material")
        self.cmb_box_shell_material = QComboBox()
        self.cmb_box_shell_material.addItems(self.material_list)
        #self.cmb_box_shell_material.currentIndexChanged.connect(self.update_material)#This will update the Material in the Shell OPutput Groupbox
        self.lbl_shell_density =QLabel("Density")
        self.tb_shell_density =QLineEdit("7.85")
        self.lbl_shell_ht=QLabel("Height")
        self.tb_shell_ht =QLineEdit("3200")
        self.lbl_shell_ID=QLabel("ID")
        self.tb_shell_ID =QLineEdit("1000")
        self.lbl_shell_allwnc_dia =QLabel("Allowances on Dia")
        self.tb_shell_allwnc_dia =QLineEdit("XXX")
        self.tb_shell_allwnc_dia.setEnabled(False)#Diabled as its calculated based on ID & thk
        self.lbl_shell_allwnc_ht =QLabel("Allowances on Height")
        self.tb_shell_allwnc_ht =QLineEdit("00")
        self.lbl_shell_thk=QLabel("Thk")
        self.tb_shell_thk =QLineEdit("50")
        self.lbl_shell_No_of_Seams_alng_len=QLabel("No.of Seam along Length")
        self.tb_shell_No_of_Seams_alng_len =QLineEdit("3")
        #self.lbl_shell_No_of_Seams_alng_wd=QLabel("No.of Seam along Width")
        #self.tb_shell_No_of_Seams_alng_lwd =QLineEdit("3")
        self.btn_calculate_shell_wt=QPushButton("Calculate")
        self.btn_calculate_shell_wt.clicked.connect(self.Calculate_btn_clicked)
        
        #Calc Raw mat plt width and Count
        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_shell_desc)
        self.grpbox_Vbox_layout_shell.addWidget(self.tb_shell_desc)
        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_shell_material)
        self.grpbox_Vbox_layout_shell.addWidget(self.cmb_box_shell_material)
        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_shell_density)
        self.grpbox_Vbox_layout_shell.addWidget(self.tb_shell_density)
        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_shell_ht)
        self.grpbox_Vbox_layout_shell.addWidget(self.tb_shell_ht)
        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_shell_ID)
        self.grpbox_Vbox_layout_shell.addWidget(self.tb_shell_ID)
        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_shell_allwnc_ht)
        self.grpbox_Vbox_layout_shell.addWidget(self.tb_shell_allwnc_ht)
        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_shell_allwnc_dia)
        self.grpbox_Vbox_layout_shell.addWidget(self.tb_shell_allwnc_dia)

        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_shell_thk)
        self.grpbox_Vbox_layout_shell.addWidget(self.tb_shell_thk)
        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_shell_No_of_Seams_alng_len)
        self.grpbox_Vbox_layout_shell.addWidget(self.tb_shell_No_of_Seams_alng_len)
        #self.grpbox_Vbox_layout_shell.addWidget(self.lbl_shell_No_of_Seams_alng_wd)
        #self.grpbox_Vbox_layout_shell.addWidget(self.tb_shell_No_of_Seams_alng_lwd)
        self.grpbox_Vbox_layout_shell.addWidget(self.btn_calculate_shell_wt,0,Qt.AlignmentFlag.AlignHCenter)
        
        #Calc Raw mat plt width and Count
        self.lbl_shell_op =QLabel("Output")
        self.lbl_shell_op.setStyleSheet("font:bold;font-size:16px")
        self.lbl_Shell_wt =QLabel(" Shell Wt")
        self.tb_Shell_wt =QLineEdit("XXXXXX")
        self.tb_Shell_wt.setDisabled(True)
        self.lbl_shell_plt_size =QLabel("Raw Mat Plt size(Qty along ht x raw plt height x Qty along length x raw plt length per seam)")
        self.lbl_shell_plt_size.setWordWrap(True)
        self.tb_shell_plt_size =QLineEdit("XXXXXX")
        self.tb_shell_plt_size.setEnabled(False)
        self.lbl_Shell_plt_offcut_size =QLabel("Offcut Size")
        self.tb_Shell_plt_offcut_size =QLineEdit("XXXXXX")
        self.tb_Shell_plt_offcut_size.setDisabled(True)
        self.lbl_Shell_plt_surface_area =QLabel("Surface Area(m2)")
        self.tb_Shell_plt_surface_area =QLineEdit("XXXXXX")
        self.tb_Shell_plt_surface_area.setEnabled(False)
        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_shell_op)       
        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_Shell_wt)
        self.grpbox_Vbox_layout_shell.addWidget(self.tb_Shell_wt)
        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_shell_plt_size)
        self.grpbox_Vbox_layout_shell.addWidget(self.tb_shell_plt_size)
        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_Shell_plt_surface_area)
        self.grpbox_Vbox_layout_shell.addWidget(self.tb_Shell_plt_surface_area)
        self.grpbox_Vbox_layout_shell.addWidget(self.lbl_Shell_plt_offcut_size)
        self.grpbox_Vbox_layout_shell.addWidget(self.tb_Shell_plt_offcut_size)

        
        
        #Add Materia to BOM Buton
        self.btn_add_shell_mat_to_BOM=QPushButton("Add to BOM")
        self.btn_add_shell_mat_to_BOM.clicked.connect(self.Add_Shell_mat_to_BOM)
        self.grpbox_Vbox_layout_shell.addWidget(self.btn_add_shell_mat_to_BOM,0,Qt.AlignmentFlag.AlignHCenter)       
        
   


    def Add_Shell_mat_to_BOM(self):
        _ProjectCOntroller=ProjectController()
        _ProjectCOntroller.add_update_item(item='Shell',item_name=self.tb_shell_desc.text(),wt=self.tb_Shell_wt.text(),material=self.cmb_box_shell_material.currentText())
        _ProjectCOntroller.add_update_surface_area(item='Shell',item_name=self.tb_shell_desc.text(),surface_area=self.tb_Shell_plt_surface_area.text())
        print("Add Shell Material to BOM Pressed")
        self.change_button_color_green()

    @staticmethod
    def calculate_allwnce_on_dia(ID, T):
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
       # print(ID,OD,T,Allow)    
        return Allow
    
    # def Calculate_Shell_wt(self,raw_plt_width):
        
        ID=float(self.tb_shell_ID.text())#ID
        t=float(self.tb_shell_thk.text())#thk
        rho=float(self.tb_shell_density.text())#density
        E=float(self.tb_shell_allwnc_ht.text())#Length Allwnc
        h_incld_allwmc=float(self.tb_shell_ht.text())+E #Height
        no_of_seams_alng_len=float(self.tb_shell_No_of_Seams_alng_len.text())
       
        
        #allwnc_on_dia (a)  
        a=self.calculate_allwnce_on_dia(ID,t)
        self.tb_shell_allwnc_dia.setText(str(a))
        
        
        #Case-1 Raw mat plate wd = 2500mm
        raw_mat_plt_width=2500        
        Qty_alng_ht=int(math.ceil(h_incld_allwmc/raw_mat_plt_width))   
 
        
        #Raw mat each plt length along seam       
        Lg_per_seam_alng_len=self.roundup_to_nex100(math.pi*(ID+t)+a)/(no_of_seams_alng_len+1) #Length per seam
       
        
        shell_wt =round((no_of_seams_alng_len+1)*Lg_per_seam_alng_len*h_incld_allwmc*t*rho*0.000001,2)
        self.tb_Shell_wt.setText(str(shell_wt))
        self.tb_shell_plt_size.setText(f"{Qty_alng_ht} x {raw_mat_plt_width}mm x  {no_of_seams_alng_len+1} x {Lg_per_seam_alng_len}mm")
        
        #offcut size
        offcut_height=raw_mat_plt_width * Qty_alng_ht-h_incld_allwmc
        offcut_len=Lg_per_seam_alng_len*(no_of_seams_alng_len+1)
        self.tb_Shell_plt_offcut_size.setText(f"{offcut_height} x {offcut_len}")
        
        self.btn_calculate_shell_wt.setFocus()#Remove focus from Combox otherwise accidently can be changed by user
        self.reset_button_color_default(self.btn_add_shell_mat_to_BOM)#Reset the color of Add Material to BOM as Weight value got changed.    
    
    def Calculate_btn_clicked(self):
        #This Function calculates Shell wt & update it into Shell Op groupbox
        
        ID=float(self.tb_shell_ID.text())#ID
        t=float(self.tb_shell_thk.text())#thk
        rho=float(self.tb_shell_density.text())#density
        E=float(self.tb_shell_allwnc_ht.text())#Length Allwnc
        h_incld_allwmc=float(self.tb_shell_ht.text())+E #Height
        no_of_seams_alng_len=float(self.tb_shell_No_of_Seams_alng_len.text())
       
        a=self.calculate_allwnce_on_dia(ID,t) #allwnc_on_dia (a)
        self.tb_shell_allwnc_dia.setText(str(a))
        
        
        raw_mat_plt_choice=[2500,2000]
        offcut_area=[0.0]*len(raw_mat_plt_choice)
        Qty_alng_ht=[0.0]*len(raw_mat_plt_choice)
        Lg_per_seam_alng_len=[0.0]*len(raw_mat_plt_choice)
        shell_wt=[0.0]*len(raw_mat_plt_choice)
        offcut_height=[0.0]*len(raw_mat_plt_choice)
        offcut_len=[0.0]*len(raw_mat_plt_choice)
        offcut_area=[0.0]*len(raw_mat_plt_choice)
        surface_area=[0.0]*len(raw_mat_plt_choice)
        
        
        for index,raw_mat_plt_width in enumerate(raw_mat_plt_choice):
            #Qty along Height            
            Qty_alng_ht[index]=int(math.ceil(h_incld_allwmc/raw_mat_plt_width))  
            #Raw mat each plt length along seam       
            Lg_per_seam_alng_len[index]=self.roundup_to_next100(math.pi*(ID+t)+a)/(no_of_seams_alng_len+1) #Length per seam
            shell_wt[index] =round((no_of_seams_alng_len+1)*Lg_per_seam_alng_len[index]*h_incld_allwmc*t*rho*0.000001,2)
           
           #Surface ARea
            surface_area[index]=round((shell_wt[index]/rho/t),2)
            
            #offcut size
            offcut_height[index]=raw_mat_plt_width * Qty_alng_ht[index]-h_incld_allwmc
            offcut_len[index]=Lg_per_seam_alng_len[index]*(no_of_seams_alng_len+1)            
            offcut_area[index]=offcut_height[index]*offcut_len[index]
            
        
        #Check which raw mat plate gives minium offcut area ,and use that plate values to populate output
        min_offcut_area_index=offcut_area.index(min(offcut_area))    
        self.tb_Shell_wt.setText(str(shell_wt[min_offcut_area_index])) 
        self.tb_Shell_plt_surface_area.setText(str(surface_area[min_offcut_area_index]))        
        self.tb_shell_plt_size.setText(f"{Qty_alng_ht[min_offcut_area_index]} x {raw_mat_plt_choice[min_offcut_area_index]}mm x  {no_of_seams_alng_len+1} x {Lg_per_seam_alng_len[min_offcut_area_index]}mm")
        self.tb_Shell_plt_offcut_size.setText(f"{offcut_height[min_offcut_area_index]} x {offcut_len[min_offcut_area_index]}")
        print(self.tb_Shell_wt.text(),self.tb_Shell_plt_surface_area.text())
        
        self.btn_calculate_shell_wt.setFocus()#Remove focus from Combox otherwise accidently can be changed by user
        self.reset_button_color_default(self.btn_add_shell_mat_to_BOM)#Reset the color of Add Material to BOM as Weight value got changed.
        
            
    def roundup_to_next100(self,num):
       return  math.ceil(num/100)*100
        
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


# class Shellll(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.InitializeUI()

#     def InitializeUI(self):

#         self.SetUp_Shell_ip_GrpBox()
#         self.SetUp_Shell_op_GrpBox()
#         self.VBox_layout_Shell =QVBoxLayout()
            
#         self.VBox_layout_Shell.addWidget(self.grpbox1)
#         self.VBox_layout_Shell.addWidget(self.grpbox2)
#         #self.GrpBox_shell=QGroupBox("Shell",self)
#         #self.GrpBox_shell.setLayout(self.VBox_layout_Shell)
#         self.setLayout(self.VBox_layout_Shell)
#        #self.setFixedWidth(200)
        
#         # container_widget = QWidget()
#         # container_widget.setLayout(self.VBox_layout_Shell)
        

#     def  SetUp_Shell_ip_GrpBox(self):  

#         #Read Material list from Variables
#         self.material_list = var.master_mat_list

#         #Add groupbox and set its layout to SHell VBox Input
#         self.grpbox1 = QGroupBox("Shell Input")
#         #self.grpbox1.setStyleSheet(style_1)
#         #self.grpbox1.setFixedWidth(300)
#         self.VBox_layout1 =QVBoxLayout()
#         self.grpbox1.setLayout(self.VBox_layout1)

#        #Shell Input
#         self.lbl_shell_material =QLabel("Material")
#         self.cmb_box_shell_material = QComboBox()
#         self.cmb_box_shell_material.addItems(self.material_list)
#         self.cmb_box_shell_material.currentIndexChanged.connect(self.update_material)#This will update the Material in the Shell OPutput Groupbox
#         self.lbl_shell_density =QLabel("Density")
#         self.tb_shell_density =QLineEdit("7.85")
#         self.lbl_shell_length =QLabel("Length")
#         self.tb_shell_length =QLineEdit("3200")
#         self.lbl_shell_allwnc_lg =QLabel("Allowances on Lg")
#         self.tb_shell_allwnc_lg =QLineEdit("20")
#         self.lbl_shell_thk =QLabel("Thickness")
#         self.tb_shell_thk =QLineEdit("14")
#         self.lbl_shell_ID=QLabel("ID")
#         self.tb_shell_ID =QLineEdit("1000")
#         self.lbl_shell_allwnc_dia =QLabel("Allowances on Dia")
#         self.tb_shell_allwnc_dia =QLineEdit("XXX")
#         self.tb_shell_allwnc_dia.setEnabled(False)#Diabled as its calculated based on ID & thk
#         self.lbl_shell_coarse_no =QLabel("Shell Coarse No.")
#         self.tb_shell_coarse_no =QLineEdit("1")
#         self.VBox_layout1.addWidget(self.lbl_shell_material)
#         self.VBox_layout1.addWidget(self.cmb_box_shell_material)
#         self.VBox_layout1.addWidget(self.lbl_shell_density)
#         self.VBox_layout1.addWidget(self.tb_shell_density)
#         self.VBox_layout1.addWidget(self.lbl_shell_allwnc_lg)
#         self.VBox_layout1.addWidget(self.tb_shell_allwnc_lg)
#         self.VBox_layout1.addWidget(self.lbl_shell_thk)
#         self.VBox_layout1.addWidget(self.tb_shell_thk)
#         self.VBox_layout1.addWidget(self.lbl_shell_ID)
#         self.VBox_layout1.addWidget(self.tb_shell_ID)
#         self.VBox_layout1.addWidget(self.lbl_shell_allwnc_dia)
#         self.VBox_layout1.addWidget(self.tb_shell_allwnc_dia)
#         self.VBox_layout1.addWidget(self.lbl_shell_coarse_no)
#         self.VBox_layout1.addWidget(self.tb_shell_coarse_no)
#         self.btn_calc_shell_wt=QPushButton("Calculate Wt")
#         self.btn_calc_shell_wt.clicked.connect(self.Calculate_Shell_wt)
#         self.VBox_layout1.addWidget(self.btn_calc_shell_wt,0,Qt.AlignmentFlag.AlignHCenter)

#     def  SetUp_Shell_op_GrpBox(self):
#          #Add groupbox and set its layout to SHell VBox Input
#         self.grpbox2 = QGroupBox("Shell Output")
#         #self.grpbox2.setStyleSheet(style_1)
#         #self.grpbox2.setFixedWidth(300)
#         #self.grpbox2.setDisabled(True)
#         self.HBox_layout2=QHBoxLayout()
#         self.grpbox2.setLayout(self.HBox_layout2)
        

#         self.lbl_shell_op_Material =QLabel("Material")
#         self.tb_shell_op_Material =QLineEdit(str(self.cmb_box_shell_material.currentText()))
#         self.tb_shell_op_Material.setDisabled(True)
#         self.lbl_Shell_wt =QLabel(" Shell Wt")
#         self.tb_Shell_wt =QLineEdit("XXXXXX")
#         self.tb_Shell_wt.setDisabled(True)
#         self.HBox_layout2.addWidget(self.lbl_shell_op_Material)
#         self.HBox_layout2.addWidget(self.tb_shell_op_Material)
#         self.HBox_layout2.addWidget(self.lbl_Shell_wt)
#         self.HBox_layout2.addWidget(self.tb_Shell_wt)
#         #Add Materia to BOM Buton
#         self.btn_add_shell_mat_to_BOM=QPushButton("Add to BOM")
#         self.btn_add_shell_mat_to_BOM.clicked.connect(self.Add_Shell_mat_to_BOM)
#         self.HBox_layout2.addWidget(self.btn_add_shell_mat_to_BOM,0,Qt.AlignmentFlag.AlignHCenter)
        

#     def Calculate_Shell_wt(self):
#         #This Function calculates Shell wt & update it into Shell Op groupbox
#         #allwnc_on_dia (a)   
        
#         Lg=float(self.tb_shell_length.text()) #Length
#         E=float(self.tb_shell_allwnc_lg.text())#Length Allwnc
#         ID=float(self.tb_shell_ID.text())#ID
#         t=float(self.tb_shell_thk.text())
#         rho=float(self.tb_shell_density.text())

#         a=self.calculate_allwnce_on_dia(ID,t)
#         self.tb_shell_allwnc_dia.setText(str(a))
        
#         TL=Lg+E
#         shell_wt =round(math.pi*(ID+a)*t*TL*rho*0.000001,2)
#         self.tb_Shell_wt.setText(str(shell_wt))
#         #print(shell_wt)
#         self.btn_calc_shell_wt.setFocus()#Remove focus from Combox otherwise accidently can be changed by user
#         self.reset_button_color_default(self.btn_add_shell_mat_to_BOM)#Reset the color of Add Material to BOM as Weight value got changed.
        
        
#     def update_material(self) :
#         #This will update the Material in the Shell OPutput Groupbox
#         self.tb_shell_op_Material.setText(str(self.cmb_box_shell_material.currentText()))
#         #print(i)


#     def Add_Shell_mat_to_BOM(self):
#         print("Add Shell Material to BOM Pressed")
#         self.change_button_color_green()

#     def calculate_allwnce_on_dia(_,ID, T):
#         OD = ID + 2 * T
            
#         if T > 100:
#             Allow = 300
#         elif 50 < T <= 100:
#             Allow = 2 * T
#         elif (30 < T < 50) and (OD / T) <= 24:
#             Allow = 2 * T
#         elif (T <= 30) and (OD / T) <= 15:
#             Allow = 1 * T
#         else:
#             Allow = 0
#         print(ID,OD,T,Allow)    
#         return Allow
#     #This function changes the coor of sender button to green
#     def change_button_color_green(self):
#         button = self.sender()
#         button.setStyleSheet("background-color: green; color: white;")

#     #This Function reset the color of "button" passed as an argument.
#     def reset_button_color_default(self,button):
#         #button = self.sender()
#         button.setStyleSheet("")       


# class custom_style:
#     grpbox_style="""
#             QGroupBox QLineEdit {
#             width:100px
#             }
#             """   
#     gridlayout_shell_count_style="""
#     {
#         background-color:lightgreen
#     }
#     """

# # class Insert_Plate(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.InitializeUI()

# #     def InitializeUI(self):

# #         self.SetUp_Insrt_plt_ip_GrpBox()
# #         self.SetUp_Insrt_plt_op_GrpBox()
# #         self.VBox_layout_Insrt_plt =QVBoxLayout()
# #         self.VBox_layout_Insrt_plt.addWidget(self.grpbox1)
# #         self.VBox_layout_Insrt_plt.addWidget(self.grpbox2)
# #         self.setLayout(self.VBox_layout_Insrt_plt)

# #     def  SetUp_Insrt_plt_ip_GrpBox(self):  

# #         #Read Material list from Variables
# #         self.material_list = var.master_mat_list

# #         #Add groupbox and set its layout to Insert Plate VBox Input
# #         self.grpbox1 = QGroupBox("Insert Plate Input",self)
# #         self.VBox_layout1 =QVBoxLayout()
# #         self.grpbox1.setLayout(self.VBox_layout1)

# #        #Insert Plate
# #         self.lbl_Insrt_plt_material =QLabel("Material")
# #         self.cmb_box_Insrt_plt_material = QComboBox()
# #         self.cmb_box_Insrt_plt_material.addItems(self.material_list)
# #         self.cmb_box_Insrt_plt_material.currentIndexChanged.connect(self.update_material)#This will update the Material in the Insrt_plt OPutput Groupbox
# #         self.lbl_Insrt_plt_density =QLabel("Density")
# #         self.tb_Insrt_plt_density =QLineEdit("7.85")
# #         self.lbl_Insrt_plt_length =QLabel("Density")
# #         self.tb_Insrt_plt_length =QLineEdit("1000")
# #         self.lbl_Insrt_plt_allwnc_lg =QLabel("Allowances on Lg")
# #         self.tb_Insrt_plt_allwnc_lg =QLineEdit("10")
# #         self.lbl_Insrt_plt_thk =QLabel("Thickness")
# #         self.tb_Insrt_plt_thk =QLineEdit("10")
# #         self.lbl_Insrt_plt_ID=QLabel("ID")
# #         self.tb_Insrt_plt_ID =QLineEdit("1000")
# #         self.lbl_Insrt_plt_allwnc_dia =QLabel("Allowances on Dia")
# #         self.tb_Insrt_plt_allwnc_dia =QLineEdit("XXX")
# #         self.tb_Insrt_plt_allwnc_dia.setEnabled(False)#Diabled as its calculated based on ID & thk
# #         #self.lbl_Insrt_plt_coarse_no =QLabel("Insrt_plt Coarse No.")
# #         #self.tb_Insrt_plt_coarse_no =QLineEdit("1")
# #         self.VBox_layout1.addWidget(self.lbl_Insrt_plt_material)
# #         self.VBox_layout1.addWidget(self.cmb_box_Insrt_plt_material)
# #         self.VBox_layout1.addWidget(self.lbl_Insrt_plt_density)
# #         self.VBox_layout1.addWidget(self.tb_Insrt_plt_density)
# #         self.VBox_layout1.addWidget(self.lbl_Insrt_plt_allwnc_lg)
# #         self.VBox_layout1.addWidget(self.tb_Insrt_plt_allwnc_lg)
# #         self.VBox_layout1.addWidget(self.lbl_Insrt_plt_thk)
# #         self.VBox_layout1.addWidget(self.tb_Insrt_plt_thk)
# #         self.VBox_layout1.addWidget(self.lbl_Insrt_plt_ID)
# #         self.VBox_layout1.addWidget(self.tb_Insrt_plt_ID)
# #         self.VBox_layout1.addWidget(self.lbl_Insrt_plt_allwnc_dia)
# #         self.VBox_layout1.addWidget(self.tb_Insrt_plt_allwnc_dia)
# #         #self.VBox_layout1.addWidget(self.lbl_Insrt_plt_coarse_no)
# #         #self.VBox_layout1.addWidget(self.tb_Insrt_plt_coarse_no)
# #         self.btn_calc_Insrt_plt_wt=QPushButton("Calculate Wt")
# #         self.btn_calc_Insrt_plt_wt.clicked.connect(self.Calculate_Insrt_plt_wt)
# #         self.VBox_layout1.addWidget(self.btn_calc_Insrt_plt_wt,0,Qt.AlignmentFlag.AlignHCenter)

# #     def  SetUp_Insrt_plt_op_GrpBox(self):
# #          #Add groupbox and set its layout to Insrt_plt VBox Input
# #         self.grpbox2 = QGroupBox("Insert Plate Output",self)
# #         #self.grpbox2.setDisabled(True)
# #         self.HBox_layout2=QHBoxLayout()
# #         self.grpbox2.setLayout(self.HBox_layout2)
        

# #         self.lbl_Insrt_plt_op_Material =QLabel("Material")
# #         self.tb_Insrt_plt_op_Material =QLineEdit(str(self.cmb_box_Insrt_plt_material.currentText()))
# #         self.tb_Insrt_plt_op_Material.setDisabled(True)
# #         self.lbl_Insrt_plt_wt =QLabel("Insert Plate Wt")
# #         self.tb_Insrt_plt_wt =QLineEdit("XXXXXX")
# #         self.tb_Insrt_plt_wt.setDisabled(True)
# #         self.HBox_layout2.addWidget(self.lbl_Insrt_plt_op_Material)
# #         self.HBox_layout2.addWidget(self.tb_Insrt_plt_op_Material)
# #         self.HBox_layout2.addWidget(self.lbl_Insrt_plt_wt)
# #         self.HBox_layout2.addWidget(self.tb_Insrt_plt_wt)
# #         #Add Materia to BOM Buton
# #         self.btn_add_Insrt_plt_mat_to_BOM=QPushButton("Add to BOM")
# #         self.btn_add_Insrt_plt_mat_to_BOM.clicked.connect(self.Add_Insrt_plt_mat_to_BOM)
# #         self.HBox_layout2.addWidget(self.btn_add_Insrt_plt_mat_to_BOM,0,Qt.AlignmentFlag.AlignHCenter)
        

# #     def Calculate_Insrt_plt_wt(self):
# #         #This Function calculates Insrt_plt wt & update it into Insrt_plt Op groupbox

# #         Lg=float(self.tb_Insrt_plt_length.text()) #Length
# #         E=float(self.tb_Insrt_plt_allwnc_lg.text())#Length Allwnc
# #         ID=float(self.tb_Insrt_plt_ID.text())#ID
        
# #         t=float(self.tb_Insrt_plt_thk.text())
# #         rho=float(self.tb_Insrt_plt_density.text())

# #         a=self.calculate_allwnce_on_dia(ID,t)#ALlwnc on ID
# #         self.tb_Insrt_plt_allwnc_dia.setText(str(a))
    
# #         TL=Lg+E
# #         Insrt_plt_wt =round(math.pi*(ID+a)*t*TL*rho*0.000001,2)
# #         self.tb_Insrt_plt_wt.setText(str(Insrt_plt_wt))
# #         #print(Insrt_plt_wt)
# #         self.btn_calc_Insrt_plt_wt.setFocus()#Remove focus from Combox otherwise accidently can be changed by user
# #         self.reset_button_color_default(self.btn_add_Insrt_plt_mat_to_BOM)#Reset the color of Add Material to BOM as Weight value got changed.
        
        
# #     def update_material(self) :
# #         #This will update the Material in the Insrt_plt OPutput Groupbox
# #         self.tb_Insrt_plt_op_Material.setText(str(self.cmb_box_Insrt_plt_material.currentText()))
# #         #print(i)


# #     def Add_Insrt_plt_mat_to_BOM(self):
# #         print("Add Insrt_plt Material to BOM Pressed")
# #         self.change_button_color_green()

# #     def calculate_allwnce_on_dia(_,ID, T):
# #         OD = ID + 2 * T
            
# #         if T > 100:
# #             Allow = 300
# #         elif 50 < T <= 100:
# #             Allow = 2 * T
# #         elif (30 < T < 50) and (OD / T) <= 24:
# #             Allow = 2 * T
# #         elif (T <= 30) and (OD / T) <= 15:
# #             Allow = 1 * T
# #         else:
# #             Allow = 0
# #         print(ID,OD,T,Allow)        
# #         return Allow

# #         #This function changes the coor of sender button to green
# #     def change_button_color_green(self):
# #         button = self.sender()
# #         button.setStyleSheet("background-color: green; color: white;")

# #     #This Function reset the color of "button" passed as an argument.
# #     def reset_button_color_default(self,button):
# #         #button = self.sender()
# #         button.setStyleSheet("")         

# # class Misc(QWidget):
#     def __init__(self):
#         super().__init__() 
#         self.InitializeUI()

#     def InitializeUI(self):
#         layout = QVBoxLayout()
#         table1=self.create_table1()
#         layout.addWidget(table1)
#         table2=self.create_table2()
#         layout.addWidget(table2)
#         table3=self.create_table3()
#         layout.addWidget(table3)
        
#         self.setLayout(layout)
       
                

    

#     def create_table1(self):#FOundation Template
#         table =QTableWidget(1,9)
#         table_header_list=['Plate Desc.','Thk','Width','Length','Qty.','Material','Wt.', ' ',' ']
        
#         table.setHorizontalHeaderLabels([header for header in table_header_list])
#         #table.setLineWidth(2)
#         font = table.horizontalHeader().font()
#         font.setBold(True)
#         table.horizontalHeader().setFont(font)

#         # Populate the table with data
#         #for row in range(3):
#         #row=0
#         for col in range(9):
#                 item = QTableWidgetItem("000000")
#                 table.setItem(0, col, item)
#                 table.setColumnWidth(col,80)

#                 if col==5:#Material Combobox
#                     mat_list=var.master_mat_list
#                     combobox=QComboBox()
#                     combobox.addItems(mat_list)
#                     table.setCellWidget(0,col,combobox)
#                     #table.setColumnWidth(6,150)#set Width of combobox cell is 150px

#                 if col==6: #Wt cell  
#                     #item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled & ~Qt.ItemFlag.ItemIsEditable) #Make it Non editable by user
#                     self.disable_wt_cell(table,col)##Diable Wt Column Make it Non editable by user

#                 if col == 7:#Calc Wt Button
#                     button = QPushButton("Calc. Wt")
#                     button.clicked.connect(lambda:self.btn1_wt_calc(table))#lammbda function is anonymous function ,we use lambda as we can pass argment with connect event 
#                     table.setCellWidget(0, col, button)

#                 if col == 8:#Add to BOM Button╛
#                     button = QPushButton("Add to BOM")
#                     button.clicked.connect(lambda:self.btn_Add_to_BOM(table))#lammbda function is anonymous function ,we use lambda as we can pass argment with connect event 
#                     table.setCellWidget(0, col, button)


#         table.setItem(0,0,QTableWidgetItem("Foundation Template"))
#         table.setItem(0,4,QTableWidgetItem("1"))
#         self.set_table_size(table)
       
#         return table
        
#     def create_table2(self):#Internal PIpe
#         table =QTableWidget(1,9)
#         table_header_list=['Plate Desc.','NPS','Schedule','Length','Qty.','Material','Wt.', ' ',' ']
        
#         table.setHorizontalHeaderLabels([header for header in table_header_list])
#         #table.setLineWidth(2)
#         font = table.horizontalHeader().font()
#         font.setBold(True)
#         table.horizontalHeader().setFont(font)

#         # Populate the table with data
#         #for row in range(3):
#         #row=0
#         for col in range(9):
#                 item = QTableWidgetItem("000000")
#                 table.setItem(0, col, item)
#                 table.setColumnWidth(col,80)

#                 if col==1:#NPS Combobox
#                     NPS_list=[str(x) for x in var.NPS_list] #Read From Vars/DB
#                     combobox=QComboBox()
#                     combobox.addItems(NPS_list)
#                     table.setCellWidget(0,col,combobox)

#                 if col==2:#Schedule Combobox
#                     Schedule_list=[str(x) for x in var.Schedule_list] #Read From Vars/DB
#                     combobox=QComboBox()
#                     combobox.addItems(Schedule_list)
#                     table.setCellWidget(0,col,combobox)    

#                 if col==5:#Material Combobox
#                     mat_list=var.master_mat_list
#                     combobox=QComboBox()
#                     combobox.addItems(mat_list)
#                     table.setCellWidget(0,col,combobox)
#                     #table.setColumnWidth(6,150)#set Width of combobox cell is 150px

#                 if col==6: #Wt cell  
#                     #item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled & ~Qt.ItemFlag.ItemIsEditable) #Make it Non editable by user
#                     #table.item(0,col).setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled & ~Qt.ItemFlag.ItemIsEditable)
#                     self.disable_wt_cell(table,col)##Diable Wt Column Make it Non editable by user

#                 if col == 7:#Calc Wt Button
#                     button = QPushButton("Calc. Wt")
#                     button.clicked.connect(lambda:self.btn2_wt_calc(table))#lammbda function is anonymous function ,we use lambda as we can pass argment with connect event 
#                     table.setCellWidget(0, col, button)

#                 if col == 8:#Add to BOM Button
#                     button = QPushButton("Add to BOM")
#                     button.clicked.connect(lambda:self.btn_Add_to_BOM(table))#lammbda function is anonymous function ,we use lambda as we can pass argment with connect event 
#                     table.setCellWidget(0, col, button)

#         table.setItem(0,0,QTableWidgetItem("Internal Pipe"))
#         table.setItem(0,4,QTableWidgetItem("1"))
#         self.set_table_size(table)
#         return table
    
#     def create_table3(self):
#         table =QTableWidget(1,9)
#         table_header_list=['U Bolt.','OD','ID','Lg','Qty.','Material','Wt.', ' ',' ']
        
#         table.setHorizontalHeaderLabels([header for header in table_header_list])
#         #table.setLineWidth(2)
#         font = table.horizontalHeader().font()
#         font.setBold(True)
#         table.horizontalHeader().setFont(font)

#         # Populate the table with data
#         #for row in range(3):
#         #row=0
#         for col in range(9):
#                 item = QTableWidgetItem("000000")
#                 table.setItem(0, col, item)
#                 table.setColumnWidth(col,80)

#                 if col==5:#Material Combobox
#                     mat_list=var.master_mat_list
#                     combobox=QComboBox()
#                     combobox.addItems(mat_list)
#                     table.setCellWidget(0,col,combobox)
#                     #table.setColumnWidth(6,150)#set Width of combobox cell is 150px

#                 if col==6: #Wt cell  
#                     #item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled & ~Qt.ItemFlag.ItemIsEditable) #Make it Non editable by user
#                     self.disable_wt_cell(table,col)##Diable Wt Column Make it Non editable by user

#                 if col == 7:#Calc Wt Button
#                     button = QPushButton("Calc. Wt")
#                     button.clicked.connect(lambda:self.btn3_wt_calc(table))#lammbda function is anonymous function ,we use lambda as we can pass argment with connect event 
#                     table.setCellWidget(0, col, button)

#                 if col == 8:#Add to BOM Button╛
#                     button = QPushButton("Add to BOM")
#                     button.clicked.connect(lambda:self.btn_Add_to_BOM(table))#lammbda function is anonymous function ,we use lambda so we can pass argment with connect event 
#                     table.setCellWidget(0, col, button)

#         table.setItem(0,0,QTableWidgetItem("U Bolt"))
#         table.setItem(0,4,QTableWidgetItem("1"))
#         self.set_table_size(table)     
        
#         return table
    
#     def btn1_wt_calc(self,table:QTableWidget):
#         print("ADD BOM BUTTON from  TABLE 1 Clicked")
#         thk =float(table.item(0,1).text())
#         width=float(table.item(0,2).text())
#         len=float(table.item(0,3).text())
#         qty=float(table.item(0,4).text())
#         density=7.85*10**-6
#         wt=round(thk*width*len*qty*density,2)
#         wt_column=6
#         table.setItem(0,wt_column,QTableWidgetItem(str(wt))) # Overwrite the Wt cell widget with new cell Widget with new wt value
#         table.cellWidget(0,8).setStyleSheet("")#Reset Color of "Add to BOM " Button ,on every calculation rerun.
#         self.disable_wt_cell(table,wt_column)#Again disable Wt column as its we overwrite the previous CellWIdget on Wt column.
#         #table.resizeColumnsToContents()
      
        
#     def btn_Add_to_BOM(self,table:QTableWidget):
#         combobox:QComboBox = table.cellWidget(0,5)#row=0,col=5--->combobox
#         material=combobox.currentText()
#         wt=table.item(0,6).text()
#         print(wt,material)

#         #table.resizeColumnsToContents()
#         self.change_button_color_green()

    
#     def btn2_wt_calc(self,table:QTableWidget):
#         print("ADD BOM BUTTON from  TABLE 2 Clicked")
#         some_valu_from_db =10 #Some value from DB of NPS & SCHEDULE
        
#         len=float(table.item(0,3).text())
#         qty=float(table.item(0,4).text())
#         #density=7.85*10**-6
#         wt=round(some_valu_from_db*len*qty/1000,2)
#         wt_column=6
#         table.setItem(0,wt_column,QTableWidgetItem(str(wt)))
#         table.cellWidget(0,8).setStyleSheet("")#Reset Color of "Add to BOM " Button ,on every calculation rerun.
#         self.disable_wt_cell(table,wt_column)
#         #table.resizeColumnsToContents()

#     def btn3_wt_calc(self,table:QTableWidget):
#         print("ADD BOM BUTTON from  TABLE 3 Clicked")
#         OD =float(table.item(0,1).text())
#         ID=float(table.item(0,2).text())
#         Lg=float(table.item(0,3).text())
#         qty=float(table.item(0,4).text())
#         density=7.85*10**-6
#         wt=math.pi/4*(OD**2-ID**2)*Lg*qty*density
#         print(OD,ID,Lg,qty,wt)
#         wt=round(wt,2)
#         wt_column=6
#         table.setItem(0,wt_column,QTableWidgetItem(str(wt))) # Overwrite the Wt cell widget with new cell Widget with new wt value
#         table.cellWidget(0,8).setStyleSheet("")#Reset Color of "Add to BOM " Button ,on every calculation rerun.
#         self.disable_wt_cell(table,wt_column)#Again disable Wt column as its we overwrite the previous CellWIdget on Wt column. 
#         #table.resizeColumnsToContents()   

#     def disable_wt_cell(self,table:QTableWidget,col):
#         table.item(0,col).setFlags(table.item(0,col).flags() & ~Qt.ItemFlag.ItemIsEnabled & ~Qt.ItemFlag.ItemIsEditable)   

#     def change_button_color_green(self):
#         button = self.sender()
#         button.setStyleSheet("background-color: green; color: white;")

#     def set_table_size(self,table:QTableWidget):
        # width=[60,100,150]
        # table.setColumnWidth(0,width[2])
        # table.setColumnWidth(1,width[0])
        # table.setColumnWidth(2,width[0])
        # table.setColumnWidth(3,width[0])
        # table.setColumnWidth(4,width[0])
        # table.setColumnWidth(5,width[2])
        # table.setColumnWidth(6,width[0])
        # table.setColumnWidth(7,width[1])
        # table.setColumnWidth(8,width[1])