
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QLayout, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout,QWidget, \
    QTabWidget,QGroupBox,QTableWidget,QTableWidgetItem,QGridLayout,QScrollArea,QSpacerItem
from Variables import var
from PyQt6.QtCore import Qt,QRect
import math
from Controller.project_controller import ProjectController,Get_Shell_ODs_from_Saddle_Data,Get_Saddle_Data,Get_Saddle_Dim_Data,Get_Vessel_Data

class Tab_Fire_Insl(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
        
    def InitializeUI(self):
       
        
        self.Vbox_layout=QVBoxLayout()
        Insl_cold= Insl_Cold()
        Insl_hot=Insl_Hot(Insl_cold)
        Fire_proof=Fire_Proof()
        self.Vbox_layout.addWidget(Insl_cold)
        self.Vbox_layout.addWidget(Insl_hot)
        self.Vbox_layout.addWidget(Fire_proof)
       
       
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
        
        
        
class Insl_Cold(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
            
    def InitializeUI(self):
        self.set_ui_layout() 
                      
    def set_ui_layout(self):
        self.grpbox=QGroupBox("Insulation Cold")
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
        self.tb_description =QLineEdit("Insl Cold ")
        self.tb_description.setStyleSheet("font:bold")
        self.lbl_insl_thk =QLabel("Insl thk")
        self.tb_insl_thk =QLineEdit("50")
        self.lbl_shell_dia =QLabel("Shell Dia")
        self.tb_shell_dia = QLineEdit("2500") 
        self.lbl_shell_Ht=QLabel("Shell Ht")
        self.tb_shell_Ht =QLineEdit("9500")
        self.lbl_Dim_L=QLabel("Dimension 'L'")
        self.tb_Dim_L =QLineEdit("600")
        self.lbl_T_Cleat_thk=QLabel("T-Cleat Thk")
        self.tb_T_Cleat_thk =QLineEdit("8")
        self.lbl_Flat_plt_wd=QLabel("Flat Plt Width")
        self.tb_Flat_plt_wd =QLineEdit(f"{float(self.tb_insl_thk.text())-10}")
        self.lbl_Flat_plt_thk=QLabel("Flat Plt Thk")
        self.tb_Flat_plt_thk =QLineEdit("6")
        self.lbl_No_of_rings=QLabel("No. of Rings")
        self.tb_No_of_rings =QLineEdit("6")
        self.lbl_No_of_T_cleat=QLabel("No. of T-Cleats")
        self.tb_No_of_T_cleat =QLineEdit("50")
        self.lbl_bending_allwnc_per_ring=QLabel("Bending Allwnc per Ring")
        self.tb_bending_allwnc_per_ring =QLineEdit("500")
        
        self.btn_calculate_wt=QPushButton("Calculate")
        self.btn_calculate_wt.clicked.connect(self.Calculate_btn_clicked)
        
        self.lbl_T_cleat_Wt=QLabel("T-Cleat Weight")
        self.tb_T_cleat_Wt = QLineEdit("XX") 
        self.tb_T_cleat_Wt.setEnabled(False)         
        self.lbl_T_cleat_material=QLabel("T-Cleat Material")
        self.cmbbox_T_cleat_material=QComboBox()
        self.cmbbox_T_cleat_material.addItems(var.master_mat_list)
        self.btn_add_mat_T_Cleat=QPushButton("Add to BOM")
        self.btn_add_mat_T_Cleat.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_Flat_plt_Wt=QLabel("Flat Plate Weight")
        self.tb_Flat_plt_Wt = QLineEdit("XX") 
        self.tb_Flat_plt_Wt.setEnabled(False)         
        self.lbl_Flat_plt_material=QLabel("Flat Plate Material")
        self.cmbbox_Flat_plt_material=QComboBox()
        self.cmbbox_Flat_plt_material.addItems(var.master_mat_list)
        self.btn_add_mat_Flat_plt=QPushButton("Add to BOM")
        self.btn_add_mat_Flat_plt.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_fastners_detail=QLabel("Enter FastNers detail")
        self.tb_fastners_detail = QLineEdit("M6 x 30Lg")
        self.lbl_No_of_fastners=QLabel("No. of FastNers")
        self.tb_No_of_fastners = QLineEdit("XX")
        self.tb_No_of_fastners.setEnabled(False)
        self.lbl_fastners_material=QLabel("Fastners Material")
        self.tb_fastners_material=QLineEdit("CS-Fast")
        self.btn_add_mat_Fastners=QPushButton("Add to BOM")
        self.btn_add_mat_Fastners.clicked.connect(self.Add_material_to_BOM)
        
        
        self.lbl_sheet_detail=QLabel("Sheet detail")
        self.tb_sheet_detail = QLineEdit("Thk x L x W")
        self.tb_sheet_detail.setEnabled(False)
        self.lbl_sheet_material=QLabel("Sheet Material")
        self.tb_sheet_material=QLineEdit("Asbestos")
        self.btn_add_mat_Sheet=QPushButton("Add to BOM")
        self.btn_add_mat_Sheet.clicked.connect(self.Add_material_to_BOM)
               
      
        
       
        
        #Saddle Surface Area
        self.lbl_surfaceArea=QLabel("Surface Area")
        self.tb_insl_cold_surfaceArea =QLineEdit("XXx")
        self.tb_insl_cold_surfaceArea.setEnabled(False)
        
        #Add Material Buttin
        self.btn_add_SurfaceArea=QPushButton("Add to BOM")        
        self.btn_add_SurfaceArea.clicked.connect(self.Add_material_to_BOM)
        
        
        #Input Layout
        
        
        a=2
        self.gridlayout.addWidget(self.lbl_description,a,2)
        self.gridlayout.addWidget(self.tb_description,a,3)
        
        b=a+1
        self.gridlayout.addWidget(self.lbl_insl_thk,b,0)
        self.gridlayout.addWidget(self.tb_insl_thk,b,1)
        self.gridlayout.addWidget(self.lbl_shell_dia,b,2)
        self.gridlayout.addWidget(self.tb_shell_dia,b,3)
        self.gridlayout.addWidget(self.lbl_shell_Ht,b,4)
        self.gridlayout.addWidget(self.tb_shell_Ht,b,5)
        
        b1=b+1
        self.gridlayout.addWidget(self.lbl_Dim_L,b1,0)
        self.gridlayout.addWidget(self.tb_Dim_L,b1,1)
        
        c=b1+1
        self.gridlayout.addWidget(self.lbl_T_Cleat_thk,c,0)
        self.gridlayout.addWidget(self.tb_T_Cleat_thk,c,1)
        self.gridlayout.addWidget(self.lbl_Flat_plt_wd,c,2)
        self.gridlayout.addWidget(self.tb_Flat_plt_wd,c,3)
        self.gridlayout.addWidget(self.lbl_Flat_plt_thk,c,4)
        self.gridlayout.addWidget(self.tb_Flat_plt_thk,c,5)
        
        d=c+1
        self.gridlayout.addWidget(self.lbl_No_of_rings,d,0)
        self.gridlayout.addWidget(self.tb_No_of_rings,d,1)
        self.gridlayout.addWidget(self.lbl_No_of_T_cleat,d,2)
        self.gridlayout.addWidget(self.tb_No_of_T_cleat,d,3)
        self.gridlayout.addWidget(self.lbl_bending_allwnc_per_ring,d,4)
        self.gridlayout.addWidget(self.tb_bending_allwnc_per_ring,d,5)
        
        e=d+1 
        self.gridlayout.addItem(QSpacerItem(100,30),e,0)
        f=e+1
        self.gridlayout.addWidget(self.btn_calculate_wt,f,2,Qt.AlignmentFlag.AlignHCenter)

        #Output Layout 
        g=f+1           
        self.gridlayout.addWidget(QLabel("Output"),g,0) 
        h=g+1              
        self.gridlayout.addWidget(self.lbl_T_cleat_Wt,h,0)
        self.gridlayout.addWidget(self.tb_T_cleat_Wt,h,1)
        self.gridlayout.addWidget(self.lbl_T_cleat_material,h,2)
        self.gridlayout.addWidget(self.cmbbox_T_cleat_material,h,3)        
        self.gridlayout.addWidget(self.btn_add_mat_T_Cleat,h,4)
               
        h1=h+1       
        self.gridlayout.addWidget(self.lbl_Flat_plt_Wt,h1,0)
        self.gridlayout.addWidget(self.tb_Flat_plt_Wt,h1,1)
        self.gridlayout.addWidget(self.lbl_Flat_plt_material,h1,2)
        self.gridlayout.addWidget(self.cmbbox_Flat_plt_material,h1,3)
        self.gridlayout.addWidget(self.btn_add_mat_Flat_plt,h1,4)
        
        i=h1+1       
        self.gridlayout.addWidget(self.lbl_fastners_detail,i,0)
        self.gridlayout.addWidget(self.tb_fastners_detail,i,1)
        self.gridlayout.addWidget(self.lbl_No_of_fastners,i,2)
        self.gridlayout.addWidget(self.tb_No_of_fastners,i,3)
       
        
        i1=i+1
        self.gridlayout.addWidget(self.lbl_fastners_material,i1,0)
        self.gridlayout.addWidget(self.tb_fastners_material,i1,1)
        self.gridlayout.addWidget(self.btn_add_mat_Fastners,i1,4)
        
        j=i1+1
        self.gridlayout.addWidget(self.lbl_sheet_detail,j,0)
        self.gridlayout.addWidget(self.tb_sheet_detail,j,1)
        self.gridlayout.addWidget(self.lbl_sheet_material,j,2)
        self.gridlayout.addWidget(self.tb_sheet_material,j,3)
        self.gridlayout.addWidget(self.btn_add_mat_Sheet,j,4)
        
        
        
        #Surface Aere
        k=j+1
        self.gridlayout.addWidget(self.lbl_surfaceArea,k,2)
        self.gridlayout.addWidget(self.tb_insl_cold_surfaceArea,k,3)
        self.gridlayout.addWidget(self.btn_add_SurfaceArea,k,4) 
       
        self.Set_all_TextBox_Width()
        #self.btn_add_SurfaceArea.setFixedWidth(150)
        # self.btn_calculate_wt.setFixedSize(150,30) 
        self.tb_description.setFixedWidth(120)
        
        
    # def Set_button_functionality(self):
    #     T_cleat_data={'item':'T Cleat','item_name':'Insl Cold T Cleat','wt':self.tb_T_cleat_Wt.text(),'material':self.cmbbox_T_cleat_material.currentText()}        
    #     self.btn_add_mat_T_Cleat.clicked.connect(lambda:self.Add_material_to_BOM(T_cleat_data))
    #     Flat_plt_data={'item':'Flat Plate','item_name':'Insl Cold Flat Plate','wt':self.tb_Flat_plt_Wt.text(),'material':self.cmbbox_Flat_plt_material.currentText()}        
    #     self.btn_add_mat_Flat_plt.clicked.connect(lambda:self.Add_material_to_BOM(Flat_plt_data))
    #     Fastner_data={'item':'Fastner','item_name':self.tb_fastners_detail.text(),'wt':self.tb_No_of_fastners.text(),'material':self.tb_fastners_material.text()}        
    #     self.btn_add_mat_Fastners.clicked.connect(lambda:self.Add_material_to_BOM(Fastner_data))
    #     Sheet_data={'item':'Sheet','item_name':'Insl Cold Sheet','wt':self.tb_sheet_detail.text(),'material':self.tb_sheet_material.text()}        
    #     self.btn_add_mat_Sheet.clicked.connect(lambda:self.Add_material_to_BOM(Sheet_data))
        
    #     Insl_Cold_SurfaceArea_data={'item':'Insl Cold','item_name':'Insl Cold','surface_area':self.tb_insl_cold_surfaceArea.text()}        
    #     self.btn_add_mat_Sheet.clicked.connect(lambda:self.Add_material_to_BOM(Insl_Cold_SurfaceArea_data))
        
        
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
                    if (isinstance(widget, QLineEdit) or isinstance(widget,QComboBox)):
                        widget.setFixedWidth(130)
                    elif(isinstance(widget,QPushButton)):                            
                        widget.setStyleSheet("background-color:lightgray;")

   
    def Add_material_to_BOM(self):
        _ProjectCOntroller=ProjectController()
        if(self.sender()==self.btn_add_mat_T_Cleat):           
            _ProjectCOntroller.add_update_item(item='T-Cleat',item_name="T-Cleat for Insl Cold ",wt=self.tb_T_cleat_Wt.text(),material=self.cmbbox_T_cleat_material.currentText())
        elif(self.sender()==self.btn_add_mat_Flat_plt):           
            _ProjectCOntroller.add_update_item(item='Flat Plate',item_name="Flat Plate for Insl Cold",wt=self.tb_Flat_plt_Wt.text(),material=self.cmbbox_Flat_plt_material.currentText())
        
        elif(self.sender()==self.btn_add_mat_Fastners):           
            _ProjectCOntroller.add_update_item(item='Fastner',item_name=self.tb_fastners_detail.text(),wt=self.tb_No_of_fastners.text(),material=self.tb_fastners_material.text())
        
        elif(self.sender()==self.btn_add_mat_Sheet):           
            _ProjectCOntroller.add_update_item(item='Sheet',item_name="Sheet for Insl Cold",wt=self.tb_sheet_detail.text(),material=self.tb_sheet_material.text())
        elif(self.sender()==self.btn_add_SurfaceArea):
            _ProjectCOntroller.add_update_surface_area(item='Insl Cold',item_name="Insl Cold",surface_area=self.tb_insl_cold_surfaceArea.text())
        
        self.change_button_color_green()

    def Calculate_btn_clicked(self):
        self.Flt_plt_wd=float(self.tb_insl_thk.text())-10
        self.tb_Flat_plt_wd.setText(str(self.Flt_plt_wd))
        self.shell_Ht=float(self.tb_shell_Ht.text())
        self.Dim_L=float(self.tb_Dim_L.text())
        self.shell_dia=float(self.tb_shell_dia.text())
        self.No_of_rings=math.ceil((self.shell_Ht+self.Dim_L)/2500+1)
        self.tb_No_of_rings.setText(str(self.No_of_rings))
        self.ins_thk=float(self.tb_insl_thk.text())        
        self.No_of_T_Cleat=math.ceil(max(math.pi*(self.shell_dia+2*self.ins_thk)/1000*self.No_of_rings,3*self.No_of_rings))        
        self.tb_No_of_T_cleat.setText(str(self.No_of_T_Cleat))
        self.T_cleat_thk=float(self.tb_T_Cleat_thk.text())
        self.T_cleat_Wt=round(100*(self.ins_thk-10)*self.T_cleat_thk*0.00000785*self.No_of_T_Cleat*2,1)
        self.tb_T_cleat_Wt.setText(str(self.T_cleat_Wt))
        self.bending_allwnc=float(self.tb_bending_allwnc_per_ring.text())
        self.Flat_plt_thk=float(self.tb_Flat_plt_thk.text())
        self.Flat_plt_Wt= round((math.pi*(self.shell_dia+2*self.ins_thk)+self.bending_allwnc)*self.No_of_rings*0.00000785*self.Flat_plt_thk*(self.Flt_plt_wd+5)+(math.pi*(self.shell_dia+2*self.ins_thk)+self.bending_allwnc)*2*0.00000785*self.Flat_plt_thk*(self.Flt_plt_wd+5),1)   
        self.tb_Flat_plt_Wt.setText(str(self.Flat_plt_Wt))
        self.No_of_Fastners=2*math.ceil(max(3*self.No_of_rings,math.pi*(self.shell_dia+2*self.ins_thk)/1000*self.No_of_rings))
        self.tb_No_of_fastners.setText(f"{self.No_of_Fastners} No.")
        self.Insl_cold_surfaceArea=round((self.T_cleat_Wt+self.Flat_plt_Wt)*2/self.T_cleat_thk/7.85,1)
        self.tb_insl_cold_surfaceArea.setText(str(self.Insl_cold_surfaceArea))
        self.sheet_detail=f"3 Thk x {(100*self.No_of_T_Cleat/2)} x {(self.ins_thk-15)*self.No_of_T_Cleat/2}"
        self.tb_sheet_detail.setText(self.sheet_detail)
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

class Insl_Hot(QWidget):
    def __init__(self,insl_cold):
        super().__init__()
        self.Insl_cold=insl_cold
        self.InitializeUI()
            
    def InitializeUI(self):
        self.set_ui_layout() 
                      
    def set_ui_layout(self):
        self.grpbox=QGroupBox("Insulation Hot")
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
        self.tb_description =QLineEdit("Insl Hot ")
        self.tb_description.setStyleSheet("font:bold")
        self.lbl_insl_thk =QLabel("Insl thk")
        self.tb_insl_thk =QLineEdit(f"{self.Insl_cold.tb_insl_thk.text()}")
        self.tb_insl_thk.setEnabled(False)
        self.lbl_shell_dia =QLabel("Shell Dia")
        self.tb_shell_dia = QLineEdit(f"{self.Insl_cold.tb_shell_dia.text()}") 
        self.tb_shell_dia.setEnabled(False)
        self.lbl_shell_Length=QLabel("Shell Length")
        self.tb_shell_Length =QLineEdit("22000")
        self.lbl_Dim_L=QLabel("Dimension 'L'")
        self.tb_Dim_L =QLineEdit(f"{self.Insl_cold.tb_Dim_L.text()}")
        self.tb_Dim_L.setEnabled(False)
        self.lbl_T_Cleat_thk=QLabel("T-Cleat Thk")
        self.tb_T_Cleat_thk =QLineEdit(f"{self.Insl_cold.tb_T_Cleat_thk.text()}")
        self.tb_T_Cleat_thk.setEnabled(False)
        self.lbl_Angle_size=QLabel("Angle Size")
        self.tb_Angle_size =QLineEdit(f"{float(self.tb_insl_thk.text())-10}")
        self.lbl_Flat_plt_thk=QLabel("Flat Plt Thk")
        self.tb_Flat_plt_thk =QLineEdit("8")
        self.lbl_No_of_rings=QLabel("No. of Rings")
        self.tb_No_of_rings =QLineEdit("6")
        self.lbl_No_of_T_cleat=QLabel("No. of T-Cleats")
        self.tb_No_of_T_cleat =QLineEdit("50")
        self.lbl_bending_allwnc_per_ring=QLabel("Bending Allwnc per Ring")
        self.tb_bending_allwnc_per_ring =QLineEdit("500")
        
        self.btn_calculate_wt=QPushButton("Calculate")
        self.btn_calculate_wt.clicked.connect(self.Calculate_btn_clicked)
        
        self.lbl_T_cleat_Wt=QLabel("T-Cleat Weight")
        self.tb_T_cleat_Wt = QLineEdit("XX") 
        self.tb_T_cleat_Wt.setEnabled(False)         
        self.lbl_T_cleat_material=QLabel("T-Cleat Material")
        self.cmbbox_T_cleat_material=QComboBox()
        self.cmbbox_T_cleat_material.addItems(var.master_mat_list)
        self.btn_add_mat_T_Cleat=QPushButton("Add to BOM")
        self.btn_add_mat_T_Cleat.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_Angle_Wt=QLabel("Angle Weight")
        self.tb_Angle_Wt = QLineEdit("XX") 
        self.tb_Angle_Wt.setEnabled(False)         
        self.lbl_Angle_material=QLabel("Flat Plate Material")
        self.cmbbox_Angle_material=QComboBox()
        self.cmbbox_Angle_material.addItems(var.master_mat_list)
        self.btn_add_mat_Angle=QPushButton("Add to BOM")
        self.btn_add_mat_Angle.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_fastners1_detail=QLabel("Enter FastNers detail")
        self.tb_fastners1_detail = QLineEdit("M6 x 30Lg")
        self.lbl_No_of_fastners1=QLabel("No. of FastNers")
        self.tb_No_of_fastners1 = QLineEdit("XX")
        self.tb_No_of_fastners1.setEnabled(False)
        self.lbl_fastners1_material=QLabel("Fastners Material")
        self.tb_fastners1_material=QLineEdit("CS-Fast")
        self.btn_add_mat_Fastners1=QPushButton("Add to BOM")        
        self.btn_add_mat_Fastners1.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_fastners2_detail=QLabel("Enter FastNers detail")
        self.tb_fastners2_detail = QLineEdit("M6 x 40Lg")
        self.lbl_No_of_fastners2=QLabel("No. of FastNers")
        self.tb_No_of_fastners2 = QLineEdit("XX")
        self.tb_No_of_fastners2.setEnabled(False)
        self.lbl_fastners2_material=QLabel("Fastners Material")
        self.tb_fastners2_material=QLineEdit("CS-Fast")
        self.btn_add_mat_Fastners2=QPushButton("Add to BOM")
        self.btn_add_mat_Fastners2.clicked.connect(self.Add_material_to_BOM)
        
        
        self.lbl_sheet_detail=QLabel("Sheet detail")
        self.tb_sheet_detail = QLineEdit("Thk x L x W")
        self.tb_sheet_detail.setEnabled(False)
        self.lbl_sheet_material=QLabel("Sheet Material")
        self.tb_sheet_material=QLineEdit("Asbestos")
        self.btn_add_mat_Sheet=QPushButton("Add to BOM")
        self.btn_add_mat_Sheet.clicked.connect(self.Add_material_to_BOM)
        
        
        self.lbl_Washer1_detail=QLabel("Enter Washer1 detail")
        self.tb_Washer1_detail = QLineEdit("Washer 3 Thk x 20 OD ")
        self.lbl_No_of_Washer1=QLabel("No. of Washer1")
        self.tb_No_of_Washer1 = QLineEdit("XX")
        self.tb_No_of_Washer1.setEnabled(False)
        self.lbl_Washer1_material=QLabel("Washer1 Material")
        self.tb_Washer1_material=QLineEdit("Neoprene")
        self.btn_add_mat_Washer1=QPushButton("Add to BOM")
        self.btn_add_mat_Washer1.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_Washer2_detail=QLabel("Enter Washer2 detail")
        self.tb_Washer2_detail = QLineEdit("Washer 2 Thk x 20 OD ")
        self.lbl_No_of_Washer2=QLabel("No. of Washer2")
        self.tb_No_of_Washer2 = QLineEdit("XX")
        self.tb_No_of_Washer2.setEnabled(False)
        self.lbl_Washer2_material=QLabel("Washer2 Material")
        self.tb_Washer2_material=QLineEdit("Aluminium")
        self.btn_add_mat_Washer2=QPushButton("Add to BOM")
        self.btn_add_mat_Washer2.clicked.connect(self.Add_material_to_BOM)
        
        self.lbl_T_cleat_Wt_on_DEnd_and_misc=QLabel("T-Cleat Wt.on DEnd & Misc.")
        self.tb_T_cleat_Wt_on_DEnd_and_misc = QLineEdit("XX") 
        self.tb_T_cleat_Wt_on_DEnd_and_misc.setEnabled(False)         
        self.lbl_T_cleat_Wt_on_DEnd_and_misc_material=QLabel("Material")
        self.cmbbox_T_cleat_Wt_on_DEnd_and_misc_material=QComboBox()
        self.cmbbox_T_cleat_Wt_on_DEnd_and_misc_material.addItems(var.master_mat_list)
        self.btn_add_mat_T_cleat_Wt_on_DEnd_and_misc=QPushButton("Add to BOM")
        self.btn_add_mat_T_cleat_Wt_on_DEnd_and_misc.clicked.connect(self.Add_material_to_BOM)
               
      
        
        #Input Layout
        
        
        a=2
        self.gridlayout.addWidget(self.lbl_description,a,2)
        self.gridlayout.addWidget(self.tb_description,a,3)
        
        b=a+1
        self.gridlayout.addWidget(self.lbl_insl_thk,b,0)
        self.gridlayout.addWidget(self.tb_insl_thk,b,1)
        self.gridlayout.addWidget(self.lbl_shell_dia,b,2)
        self.gridlayout.addWidget(self.tb_shell_dia,b,3)
        self.gridlayout.addWidget(self.lbl_shell_Length,b,4)
        self.gridlayout.addWidget(self.tb_shell_Length,b,5)
        
        b1=b+1
        self.gridlayout.addWidget(self.lbl_Dim_L,b1,0)
        self.gridlayout.addWidget(self.tb_Dim_L,b1,1)
        
        c=b1+1
        self.gridlayout.addWidget(self.lbl_T_Cleat_thk,c,0)
        self.gridlayout.addWidget(self.tb_T_Cleat_thk,c,1)
        self.gridlayout.addWidget(self.lbl_Angle_size,c,2)
        self.gridlayout.addWidget(self.tb_Angle_size,c,3)
        self.gridlayout.addWidget(self.lbl_Flat_plt_thk,c,4)
        self.gridlayout.addWidget(self.tb_Flat_plt_thk,c,5)
        
        d=c+1
        self.gridlayout.addWidget(self.lbl_No_of_rings,d,0)
        self.gridlayout.addWidget(self.tb_No_of_rings,d,1)
        self.gridlayout.addWidget(self.lbl_No_of_T_cleat,d,2)
        self.gridlayout.addWidget(self.tb_No_of_T_cleat,d,3)
        self.gridlayout.addWidget(self.lbl_bending_allwnc_per_ring,d,4)
        self.gridlayout.addWidget(self.tb_bending_allwnc_per_ring,d,5)
        
        e=d+1 
        self.gridlayout.addItem(QSpacerItem(100,30),e,0)
        f=e+1
        self.gridlayout.addWidget(self.btn_calculate_wt,f,2,Qt.AlignmentFlag.AlignHCenter)

        #Output Layout 
        g=f+1           
        self.gridlayout.addWidget(QLabel("Output"),g,0) 
        h=g+1              
        self.gridlayout.addWidget(self.lbl_T_cleat_Wt,h,0)
        self.gridlayout.addWidget(self.tb_T_cleat_Wt,h,1)
        self.gridlayout.addWidget(self.lbl_T_cleat_material,h,2)
        self.gridlayout.addWidget(self.cmbbox_T_cleat_material,h,3)        
        self.gridlayout.addWidget(self.btn_add_mat_T_Cleat,h,4)
               
        h1=h+1       
        self.gridlayout.addWidget(self.lbl_Angle_Wt,h1,0)
        self.gridlayout.addWidget(self.tb_Angle_Wt,h1,1)
        self.gridlayout.addWidget(self.lbl_Angle_material,h1,2)
        self.gridlayout.addWidget(self.cmbbox_Angle_material,h1,3)
        self.gridlayout.addWidget(self.btn_add_mat_Angle,h1,4)
        
        i=h+2      
        self.gridlayout.addWidget(self.lbl_fastners1_detail,i,0)
        self.gridlayout.addWidget(self.tb_fastners1_detail,i,1)
        self.gridlayout.addWidget(self.lbl_No_of_fastners1,i,2)
        self.gridlayout.addWidget(self.tb_No_of_fastners1,i,3)
       
        
        i1=i+1
        self.gridlayout.addWidget(self.lbl_fastners1_material,i1,0)
        self.gridlayout.addWidget(self.tb_fastners1_material,i1,1)
        self.gridlayout.addWidget(self.btn_add_mat_Fastners1,i1,4)
        
        i2=i1+1       
        self.gridlayout.addWidget(self.lbl_fastners2_detail,i2,0)
        self.gridlayout.addWidget(self.tb_fastners2_detail,i2,1)
        self.gridlayout.addWidget(self.lbl_No_of_fastners2,i2,2)
        self.gridlayout.addWidget(self.tb_No_of_fastners2,i2,3)
       
        
        i3=i2+1
        self.gridlayout.addWidget(self.lbl_fastners2_material,i3,0)
        self.gridlayout.addWidget(self.tb_fastners2_material,i3,1)
        self.gridlayout.addWidget(self.btn_add_mat_Fastners2,i3,4)
        
        j=i3+1
        self.gridlayout.addWidget(self.lbl_sheet_detail,j,0)
        self.gridlayout.addWidget(self.tb_sheet_detail,j,1)
        self.gridlayout.addWidget(self.lbl_sheet_material,j,2)
        self.gridlayout.addWidget(self.tb_sheet_material,j,3)
        self.gridlayout.addWidget(self.btn_add_mat_Sheet,j,4)
        
        k=j+1       
        self.gridlayout.addWidget(self.lbl_Washer1_detail,k,0)
        self.gridlayout.addWidget(self.tb_Washer1_detail,k,1)
        self.gridlayout.addWidget(self.lbl_No_of_Washer1,k,2)
        self.gridlayout.addWidget(self.tb_No_of_Washer1,k,3)
       
        
        k1=k+1
        self.gridlayout.addWidget(self.lbl_Washer1_material,k1,0)
        self.gridlayout.addWidget(self.tb_Washer1_material,k1,1)
        self.gridlayout.addWidget(self.btn_add_mat_Washer1,k1,4)
        
        l=k+2       
        self.gridlayout.addWidget(self.lbl_Washer2_detail,l,0)
        self.gridlayout.addWidget(self.tb_Washer2_detail,l,1)
        self.gridlayout.addWidget(self.lbl_No_of_Washer2,l,2)
        self.gridlayout.addWidget(self.tb_No_of_Washer2,l,3)
       
        l1=l+1
        self.gridlayout.addWidget(self.lbl_Washer2_material,l1,0)
        self.gridlayout.addWidget(self.tb_Washer2_material,l1,1)
        self.gridlayout.addWidget(self.btn_add_mat_Washer2,l1,4)
        
        m=l+2      
        self.gridlayout.addWidget(self.lbl_T_cleat_Wt_on_DEnd_and_misc,m,0)
        self.gridlayout.addWidget(self.tb_T_cleat_Wt_on_DEnd_and_misc,m,1)
        self.gridlayout.addWidget(self.lbl_T_cleat_Wt_on_DEnd_and_misc_material,m,2)
        self.gridlayout.addWidget(self.cmbbox_T_cleat_Wt_on_DEnd_and_misc_material,m,3)
        self.gridlayout.addWidget(self.btn_add_mat_T_cleat_Wt_on_DEnd_and_misc,m,4)
        
        
       
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
                    if (isinstance(widget, QLineEdit) or isinstance(widget,QComboBox)):
                        widget.setFixedWidth(130)
                    elif(isinstance(widget,QPushButton)):                            
                        widget.setStyleSheet("background-color:lightgray;")

   
   
    def Add_material_to_BOM(self):
        _ProjectCOntroller=ProjectController()
        if(self.sender()==self.btn_add_mat_T_Cleat):           
            _ProjectCOntroller.add_update_item(item='T-Cleat',item_name="T-Cleat for Insl Hot ",wt=self.tb_T_cleat_Wt.text(),material=self.cmbbox_T_cleat_material.currentText())
        elif(self.sender()==self.btn_add_mat_Angle):           
            _ProjectCOntroller.add_update_item(item='Angle Plate',item_name="Angle Plate for Insl Hot",wt=self.tb_Angle_Wt.text(),material=self.cmbbox_Angle_material.currentText())
        
        elif(self.sender()==self.btn_add_mat_Fastners1):           
            _ProjectCOntroller.add_update_item(item='Fastner',item_name="fastner1 Insl hot: "+self.tb_fastners1_detail.text(),wt=self.tb_No_of_fastners1.text(),material=self.tb_fastners1_material.text())
        
        elif(self.sender()==self.btn_add_mat_Fastners2):           
            _ProjectCOntroller.add_update_item(item='Fastner',item_name="fastner2 Insl hot: "+self.tb_fastners2_detail.text(),wt=self.tb_No_of_fastners2.text(),material=self.tb_fastners2_material.text())
        
        elif(self.sender()==self.btn_add_mat_Sheet):           
            _ProjectCOntroller.add_update_item(item='Sheet',item_name="Sheet for Insl hot",wt=self.tb_sheet_detail.text(),material=self.tb_sheet_material.text())
        
        elif(self.sender()==self.btn_add_mat_Washer1):           
            _ProjectCOntroller.add_update_item(item='Washer',item_name="Washer1 Insl hot"+self.tb_Washer1_detail.text(),wt=self.tb_No_of_Washer1.text(),material=self.tb_Washer1_material.text())
        elif(self.sender()==self.btn_add_mat_Washer2):           
            _ProjectCOntroller.add_update_item(item='Washer',item_name="Washer2 Insl hot"+self.tb_Washer2_detail.text(),wt=self.tb_No_of_Washer2.text(),material=self.tb_Washer2_material.text())
        elif(self.sender()==self.btn_add_mat_T_cleat_Wt_on_DEnd_and_misc):           
            _ProjectCOntroller.add_update_item(item='T-Cleat Addl',item_name="T-Cleat Addl Wt on DEnd & Misc.",wt=self.tb_T_cleat_Wt_on_DEnd_and_misc.text(),material=self.cmbbox_T_cleat_Wt_on_DEnd_and_misc_material.currentText())
        
        
        self.change_button_color_green()

    def Calculate_btn_clicked(self):
        
        #Update Common value from Cold Insl Instance
        self.update_common_values_from_cold_insl()
        
        self.Angle_size=float(self.tb_insl_thk.text())-10
        self.tb_Angle_size.setText(str(self.Angle_size))
        self.shell_len=float(self.tb_shell_Length.text())
        self.Dim_L=float(self.tb_Dim_L.text())
        self.shell_dia=float(self.tb_shell_dia.text())
        self.No_of_rings=math.ceil((self.shell_len+self.Dim_L)/2500+1)
        self.tb_No_of_rings.setText(str(self.No_of_rings))
        self.ins_thk=float(self.tb_insl_thk.text())
               
        self.No_of_T_Cleat=math.ceil(max(math.pi*(self.shell_dia+2*self.ins_thk)/1000*self.No_of_rings,3*self.No_of_rings))        
        self.tb_No_of_T_cleat.setText(str(self.No_of_T_Cleat))
        self.T_cleat_thk=float(self.tb_T_Cleat_thk.text())
        self.T_cleat_Wt=round(100*(self.ins_thk-10)*self.T_cleat_thk*0.00000785*self.No_of_T_Cleat*2,1)
        self.tb_T_cleat_Wt.setText(str(self.T_cleat_Wt))
        self.bending_allwnc=float(self.tb_bending_allwnc_per_ring.text())
       
        self.Angle_size=float(self.tb_Angle_size.text())       
        self.Flat_plt_thk=float(self.tb_Flat_plt_thk.text())
        
        self.bending_allwnc_Insl_cold=float(self.Insl_cold.tb_bending_allwnc_per_ring.text())
        self.Flat_plt_wd_Insl_cold=float(self.Insl_cold.tb_Flat_plt_wd.text())
        self.Flat_plt_thk_Insl_cold=float(self.Insl_cold.tb_Flat_plt_thk.text())        
        self.ins_thk_Insl_cold=float(self.Insl_cold.tb_insl_thk.text())        
        self.Angle_Wt= round((math.pi*(self.shell_dia+2*self.ins_thk)+self.bending_allwnc)*self.No_of_rings*0.00000785*self.Flat_plt_thk*(self.Angle_size+5)+(math.pi*(self.shell_dia+2*self.ins_thk_Insl_cold)+self.bending_allwnc_Insl_cold)*2*0.00000785*self.Flat_plt_thk_Insl_cold*(self.Flat_plt_wd_Insl_cold+5),1)   
        self.tb_Angle_Wt.setText(str(self.Angle_Wt))
        
        #Fastner1
        count=0
        if(self.shell_dia>=40):
            count=2*math.ceil(max(3*self.No_of_rings , math.pi*(self.shell_dia+2*self.ins_thk)/1000*self.No_of_rings))                   
        else:
            count=2*math.ceil(max(3*self.No_of_rings/2 , math.pi*(self.shell_dia+2*self.ins_thk)/1000*self.No_of_rings/2))
        self.No_of_Fastners1=count
        self.tb_No_of_fastners1.setText(f"{self.No_of_Fastners1} No.")
        
        #Fastner2
        self.No_of_Fastners2=math.ceil(max(3*self.No_of_rings , math.pi*(self.shell_dia+2*self.ins_thk)/1000*self.No_of_rings))
        self.tb_No_of_fastners2.setText(f"{self.No_of_Fastners2} No.")
        
        #Sheet        
        self.sheet_detail=f"3 Thk x {(100*self.No_of_T_Cleat/2)} x {(self.ins_thk-15)*self.No_of_T_Cleat/2}" if (self.shell_dia>=40) else None
        if (self.sheet_detail is None) :
            #self.btn_add_mat_Sheet.setEnabled(False)
            self.tb_sheet_detail.setText("Not Required")
            self.tb_sheet_material.setText("Not Required")
        else:    
            self.tb_sheet_detail.setText(str(self.sheet_detail))
        
        #Washer1        
        self.No_of_Washer1=math.ceil(max(3*self.No_of_rings,math.pi*(self.shell_dia+2*self.ins_thk)/1000*self.No_of_rings))
        self.tb_No_of_Washer1.setText(str(self.No_of_Washer1)+"No.")
        #Washer2        
        self.No_of_Washer2=math.ceil(max(3*self.No_of_rings,math.pi*(self.shell_dia+2*self.ins_thk)/1000*self.No_of_rings))
        self.tb_No_of_Washer2.setText(str(self.No_of_Washer2)+"No.")  
        
        #Wt of Cleats on DEnd and Misc
        self.T_cleat_Wt_on_DEnd_and_misc=math.ceil(math.pi*(self.shell_dia-100)/600)*self.ins_thk*35*self.Flat_plt_thk*0.00000785+0.5+5 
        self.tb_T_cleat_Wt_on_DEnd_and_misc.setText(str(self.T_cleat_Wt_on_DEnd_and_misc))
        #self.reset_button_color_default(self.btn_add_SurfaceArea) #Reset the color of Add Material to BOM as Weight value got changed.
        
    def update_common_values_from_cold_insl(self):
        #self.tb_insl_thk.setText(self.Insl_cold.tb_insl_thk)
        self.tb_shell_dia.setText(self.Insl_cold.tb_shell_dia.text())
        self.tb_Dim_L.setText(self.Insl_cold.tb_Dim_L.text())
        #self.tb_T_Cleat_thk.setText(self.Insl_cold.tb_T_Cleat_thk)
    
            
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



class Fire_Proof(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
            
    def InitializeUI(self):
        self.set_ui_layout() 
                      
    def set_ui_layout(self):
        self.grpbox=QGroupBox("Fire Proofing")
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
        self.lbl_skirt_ht =QLabel("Skirt Height")
        self.tb_skirt_ht =QLineEdit("1650")
        self.lbl_skirt_OD =QLabel("Skirt OD")
        self.tb_skirt_OD = QLineEdit("1000") 
        self.lbl_Fastner_detail=QLabel("Fastner Detail")
        self.tb_Fastner_detail=QLineEdit("M12 Sq Nuts")
        self.lbl_No_of_Fastner=QLabel("No. of Fastners")
        self.tb_No_of_Fastner=QLineEdit("XX")
        self.tb_No_of_Fastner.setEnabled(False)
        self.lbl_Fastner_material=QLabel("Fastner Material")
        self.tb_Fastner_material=QLineEdit("CS-Fast")        
           
        
        #Calculate Button
        self.btn_calculate=QPushButton("Calculate")
        self.btn_calculate.clicked.connect(self.Calculate_btn_clicked)
      
        #Add Material Buttin
        self.btn_add_material=QPushButton("Add to BOM")
        #self.btn_add_material.setMaximumWidth(150)
        self.btn_add_material.clicked.connect(self.Add_material_to_BOM)
        
        
        #Input Layout
        
        a=2
        self.gridlayout.addWidget(self.lbl_skirt_ht,a,0)
        self.gridlayout.addWidget(self.tb_skirt_ht,a,1)
        self.gridlayout.addWidget(self.lbl_skirt_OD,a,2)
        self.gridlayout.addWidget(self.tb_skirt_OD,a,3)        
        self.gridlayout.addWidget(self.btn_calculate,a,4)
       
        
        b=a+1
        self.gridlayout.addWidget(self.lbl_Fastner_detail,b,0)
        self.gridlayout.addWidget(self.tb_Fastner_detail,b,1)
        self.gridlayout.addWidget(self.lbl_No_of_Fastner,b,2)
        self.gridlayout.addWidget(self.tb_No_of_Fastner,b,3)
        self.gridlayout.addWidget(self.lbl_Fastner_material,b,4)
        self.gridlayout.addWidget(self.tb_Fastner_material,b,5)  
        self.gridlayout.addWidget(self.btn_add_material,b,6)
       
        self.Set_all_TextBox_Width() 
        
 
        
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
                    if (isinstance(widget, QLineEdit) or isinstance(widget,QComboBox)):
                        widget.setFixedWidth(100)
                    elif(isinstance(widget,QPushButton)):                            
                        widget.setStyleSheet("background-color:lightgray;")    

   
    def Add_material_to_BOM(self):
        
        _ProjectCOntroller=ProjectController()
        _ProjectCOntroller.add_update_item(item='Fastner',item_name="Fastner Fire proof: "+self.tb_Fastner_detail.text(),wt=self.tb_No_of_Fastner.text(),material=self.tb_Fastner_material.text())
       
        self.change_button_color_green()

    def Calculate_btn_clicked(self):
        self.No_of_Fastner=math.ceil((math.pi*float(self.tb_skirt_OD.text())/450*float(self.tb_skirt_ht.text())/450))*2
        self.tb_No_of_Fastner.setText(str(self.No_of_Fastner))
        
        self.reset_button_color_default(self.btn_add_material) #Reset the color of Add Material to BOM if alculate button is reclicked
        
            
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


