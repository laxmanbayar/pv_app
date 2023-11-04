
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout,QWidget, \
    QTabWidget,QGroupBox,QTableWidget,QTableWidgetItem,QGridLayout
from Variables import var
from PyQt6.QtCore import Qt
import math
from Controller.project_controller import ProjectController,Get_Elbow_Details

class Tab_Misc(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
    def InitializeUI(self):
        #H_box_layout= QHBoxLayout() 
        #shell=Shell() 
        #insert_Plate=Insert_Plate()
        #H_box_layout.addWidget(shell)
        #H_box_layout.addWidget(insert_Plate)

        V_box_main_layout=QVBoxLayout()
        #V_box_main_layout.addLayout(H_box_layout)
        Misc_items = Misc()
        
        V_box_main_layout.addWidget(Misc_items)

        self.setLayout(V_box_main_layout)



# class Shell(QWidget):

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
        
#         # container_widget = QWidget()
#         # container_widget.setLayout(self.VBox_layout_Shell)
        

#     def  SetUp_Shell_ip_GrpBox(self):  

#         #Read Material list from Variables
#         self.material_list = var.master_mat_list

#         #Add groupbox and set its layout to SHell VBox Input
#         self.grpbox1 = QGroupBox("Shell Input",self)
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
#         self.grpbox2 = QGroupBox("Shell Output",self)
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


# class Insert_Plate(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.InitializeUI()

#     def InitializeUI(self):

#         self.SetUp_Insrt_plt_ip_GrpBox()
#         self.SetUp_Insrt_plt_op_GrpBox()
#         self.VBox_layout_Insrt_plt =QVBoxLayout()
#         self.VBox_layout_Insrt_plt.addWidget(self.grpbox1)
#         self.VBox_layout_Insrt_plt.addWidget(self.grpbox2)
#         self.setLayout(self.VBox_layout_Insrt_plt)

#     def  SetUp_Insrt_plt_ip_GrpBox(self):  

#         #Read Material list from Variables
#         self.material_list = var.master_mat_list

#         #Add groupbox and set its layout to Insert Plate VBox Input
#         self.grpbox1 = QGroupBox("Insert Plate Input",self)
#         self.gridlayout_Insert_Plt_input=QGridLayout()
#         self.grpbox1.setLayout(self.gridlayout_Insert_Plt_input)

#        #Insert Plate
#         self.lbl_Insrt_plt_material =QLabel("Material")
#         self.cmb_box_Insrt_plt_material = QComboBox()
#         self.cmb_box_Insrt_plt_material.addItems(self.material_list)
#         self.cmb_box_Insrt_plt_material.currentIndexChanged.connect(self.update_material)#This will update the Material in the Insrt_plt OPutput Groupbox
#         self.lbl_Insrt_plt_density =QLabel("Density")
#         self.tb_Insrt_plt_density =QLineEdit("7.85")
#         self.lbl_Insrt_plt_length =QLabel("Density")
#         self.tb_Insrt_plt_length =QLineEdit("1000")
#         self.lbl_Insrt_plt_allwnc_lg =QLabel("Allowances on Lg")
#         self.tb_Insrt_plt_allwnc_lg =QLineEdit("10")
#         self.lbl_Insrt_plt_thk =QLabel("Thickness")
#         self.tb_Insrt_plt_thk =QLineEdit("10")
#         self.lbl_Insrt_plt_ID=QLabel("ID")
#         self.tb_Insrt_plt_ID =QLineEdit("1000")
#         self.lbl_Insrt_plt_allwnc_dia =QLabel("Allowances on Dia")
#         self.tb_Insrt_plt_allwnc_dia =QLineEdit("XXX")
#         self.tb_Insrt_plt_allwnc_dia.setEnabled(False)#Diabled as its calculated based on ID & thk
      
        
       
#         self.gridlayout_Insert_Plt_input.addWidget(self.lbl_Insrt_plt_material,0,0)
#         self.gridlayout_Insert_Plt_input.addWidget(self.cmb_box_Insrt_plt_material,0,1)
#         self.gridlayout_Insert_Plt_input.addWidget(self.lbl_Insrt_plt_density,0,2)
#         self.gridlayout_Insert_Plt_input.addWidget(self.tb_Insrt_plt_density,0,3)
#         self.gridlayout_Insert_Plt_input.addWidget(self.lbl_Insrt_plt_allwnc_lg,1,0)
#         self.gridlayout_Insert_Plt_input.addWidget(self.tb_Insrt_plt_allwnc_lg,1,1)
#         self.gridlayout_Insert_Plt_input.addWidget(self.lbl_Insrt_plt_thk,1,2)
#         self.gridlayout_Insert_Plt_input.addWidget(self.tb_Insrt_plt_thk,1,3)
#         self.gridlayout_Insert_Plt_input.addWidget(self.lbl_Insrt_plt_ID,2,0)
#         self.gridlayout_Insert_Plt_input.addWidget(self.tb_Insrt_plt_ID,2,1)
#         self.gridlayout_Insert_Plt_input.addWidget(self.lbl_Insrt_plt_allwnc_dia,2,2)
#         self.gridlayout_Insert_Plt_input.addWidget(self.tb_Insrt_plt_allwnc_dia,2,3)
        
#         self.btn_calc_Insrt_plt_wt=QPushButton("Calculate Wt")
#         self.btn_calc_Insrt_plt_wt.clicked.connect(self.Calculate_Insrt_plt_wt_and_surface_area)
#         self.gridlayout_Insert_Plt_input.addWidget(self.btn_calc_Insrt_plt_wt,3,2,Qt.AlignmentFlag.AlignHCenter)
#         #self.gridlayout_Insert_Plt.addWidget(self.tb_Insrt_plt_allwnc_dia,2,3)
       

#     def  SetUp_Insrt_plt_op_GrpBox(self):
#          #Add groupbox and set its layout to Insrt_plt VBox Input
#         self.grpbox2 = QGroupBox("Insert Plate Output",self)
#         #self.grpbox2.setDisabled(True)
#         self.HBox_layout2=QHBoxLayout()
#         self.grpbox2.setLayout(self.HBox_layout2)
        

#         self.lbl_Insrt_plt_op_Material =QLabel("Material")
#         self.tb_Insrt_plt_op_Material =QLineEdit(str(self.cmb_box_Insrt_plt_material.currentText()))
#         self.tb_Insrt_plt_op_Material.setDisabled(True)
#         self.lbl_Insrt_plt_wt =QLabel("Wt")
#         self.tb_Insrt_plt_wt =QLineEdit("XXXXXX")
#         self.tb_Insrt_plt_wt.setDisabled(True)
#         self.lbl_Insrt_plt_surface_area =QLabel("Surface Area")
#         self.tb_Insrt_plt_surface_area =QLineEdit("XXXXXX")
#         self.tb_Insrt_plt_surface_area.setDisabled(True)
#         self.HBox_layout2.addWidget(self.lbl_Insrt_plt_op_Material)
#         self.HBox_layout2.addWidget(self.tb_Insrt_plt_op_Material)
#         self.HBox_layout2.addWidget(self.lbl_Insrt_plt_wt)
#         self.HBox_layout2.addWidget(self.tb_Insrt_plt_wt)
#         self.HBox_layout2.addWidget(self.lbl_Insrt_plt_surface_area)
#         self.HBox_layout2.addWidget(self.tb_Insrt_plt_surface_area)
#         #Add Materia to BOM Buton
#         self.btn_add_Insrt_plt_mat_to_BOM=QPushButton("Add to BOM")
#         self.btn_add_Insrt_plt_mat_to_BOM.clicked.connect(self.Add_Insrt_plt_mat_to_BOM)
#         self.HBox_layout2.addWidget(self.btn_add_Insrt_plt_mat_to_BOM,0,Qt.AlignmentFlag.AlignHCenter)
        

#     def Calculate_Insrt_plt_wt_and_surface_area(self):
#         #This Function calculates Insrt_plt wt & update it into Insrt_plt Op groupbox

#         Lg=float(self.tb_Insrt_plt_length.text()) #Length
#         E=float(self.tb_Insrt_plt_allwnc_lg.text())#Length Allwnc
#         ID=float(self.tb_Insrt_plt_ID.text())#ID
        
#         t=float(self.tb_Insrt_plt_thk.text())
#         rho=float(self.tb_Insrt_plt_density.text())

#         a=self.calculate_allwnce_on_dia(ID,t)#ALlwnc on ID
#         self.tb_Insrt_plt_allwnc_dia.setText(str(a))
    
#         TL=Lg+E
#         Insrt_plt_wt =round(math.pi*(ID+a)*t*TL*rho*0.000001,2)
#         self.tb_Insrt_plt_wt.setText(str(Insrt_plt_wt))
#         #print(Insrt_plt_wt)
#         self.btn_calc_Insrt_plt_wt.setFocus()#Remove focus from Combox otherwise accidently can be changed by user
#         self.reset_button_color_default(self.btn_add_Insrt_plt_mat_to_BOM)#Reset the color of Add Material to BOM as Weight value got changed.
        
        
#     def update_material(self) :
#         #This will update the Material in the Insrt_plt OPutput Groupbox
#         self.tb_Insrt_plt_op_Material.setText(str(self.cmb_box_Insrt_plt_material.currentText()))
#         #print(i)


#     def Add_Insrt_plt_mat_to_BOM(self):
#         print("Add Insrt_plt Material to BOM Pressed")
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

#         #This function changes the coor of sender button to green
#     def change_button_color_green(self):
#         button = self.sender()
#         button.setStyleSheet("background-color: green; color: white;")

#     #This Function reset the color of "button" passed as an argument.
#     def reset_button_color_default(self,button):
#         #button = self.sender()
#         button.setStyleSheet("")         

class Misc(QWidget):
    def __init__(self):
        super().__init__() 
        self.InitializeUI()

    def InitializeUI(self):
        layout = QVBoxLayout()
        table1=self.create_table1()
        layout.addWidget(table1)
        table2=self.create_table2()
        layout.addWidget(table2)
        table3=self.create_table3()
        layout.addWidget(table3)
        
        self.setLayout(layout)
       
                

    

    def create_table1(self):#FOundation Template
        table =QTableWidget(1,9)
        table_header_list=['Plate Desc.','Thk','Width','Length','Qty.','Material','Wt.', ' ',' ']
        
        table.setHorizontalHeaderLabels([header for header in table_header_list])
        #table.setLineWidth(2)
        font = table.horizontalHeader().font()
        font.setBold(True)
        table.horizontalHeader().setFont(font)

        # Populate the table with data
        #for row in range(3):
        #row=0
        for col in range(9):
                item = QTableWidgetItem("000000")
                table.setItem(0, col, item)
                table.setColumnWidth(col,80)

                if col==5:#Material Combobox
                    mat_list=var.master_mat_list
                    combobox=QComboBox()
                    combobox.addItems(mat_list)
                    table.setCellWidget(0,col,combobox)
                    #table.setColumnWidth(6,150)#set Width of combobox cell is 150px

                if col==6: #Wt cell  
                    #item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled & ~Qt.ItemFlag.ItemIsEditable) #Make it Non editable by user
                    self.disable_wt_cell(table,col)##Diable Wt Column Make it Non editable by user

                if col == 7:#Calc Wt Button
                    button = QPushButton("Calc. Wt")
                    button.clicked.connect(lambda:self.btn1_wt_calc(table))#lammbda function is anonymous function ,we use lambda as we can pass argment with connect event 
                    table.setCellWidget(0, col, button)

                if col == 8:#Add to BOM Button╛
                    button = QPushButton("Add to BOM")
                    button.clicked.connect(lambda:self.btn_Add_to_BOM(table))#lammbda function is anonymous function ,we use lambda as we can pass argment with connect event 
                    table.setCellWidget(0, col, button)


        table.setItem(0,0,QTableWidgetItem("Foundation Template"))
        table.setItem(0,4,QTableWidgetItem("1"))
        self.set_table_size(table)
       
        return table
        
    def create_table2(self):#Internal PIpe
        table =QTableWidget(1,9)
        table_header_list=['Plate Desc.','NPS','Schedule','Length','Qty.','Material','Wt.', ' ',' ']
        
        table.setHorizontalHeaderLabels([header for header in table_header_list])
        #table.setLineWidth(2)
        font = table.horizontalHeader().font()
        font.setBold(True)
        table.horizontalHeader().setFont(font)

        # Populate the table with data
        #for row in range(3):
        #row=0
        for col in range(9):
                item = QTableWidgetItem("000000")
                table.setItem(0, col, item)
                table.setColumnWidth(col,80)

                if col==1:#NPS Combobox
                    NPS_list=[str(x) for x in var.NPS_list] #Read From Vars/DB
                    combobox=QComboBox()
                    combobox.addItems(NPS_list)
                    table.setCellWidget(0,col,combobox)

                if col==2:#Schedule Combobox
                    Schedule_list=[str(x) for x in var.Schedule_list] #Read From Vars/DB
                    combobox=QComboBox()
                    combobox.addItems(Schedule_list)
                    table.setCellWidget(0,col,combobox)    

                if col==5:#Material Combobox
                    mat_list=var.master_mat_list
                    combobox=QComboBox()
                    combobox.addItems(mat_list)
                    table.setCellWidget(0,col,combobox)
                    #table.setColumnWidth(6,150)#set Width of combobox cell is 150px

                if col==6: #Wt cell  
                    #item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled & ~Qt.ItemFlag.ItemIsEditable) #Make it Non editable by user
                    #table.item(0,col).setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled & ~Qt.ItemFlag.ItemIsEditable)
                    self.disable_wt_cell(table,col)##Diable Wt Column Make it Non editable by user

                if col == 7:#Calc Wt Button
                    button = QPushButton("Calc. Wt")
                    button.clicked.connect(lambda:self.btn2_wt_calc(table))#lammbda function is anonymous function ,we use lambda as we can pass argment with connect event 
                    table.setCellWidget(0, col, button)

                if col == 8:#Add to BOM Button
                    button = QPushButton("Add to BOM")
                    button.clicked.connect(lambda:self.btn_Add_to_BOM(table))#lammbda function is anonymous function ,we use lambda as we can pass argment with connect event 
                    table.setCellWidget(0, col, button)

        table.setItem(0,0,QTableWidgetItem("Internal Pipe"))
        table.setItem(0,4,QTableWidgetItem("1"))
        self.set_table_size(table)
        return table
    
    def create_table3(self):
        table =QTableWidget(1,9)
        table_header_list=['U Bolt.','OD','ID','Lg','Qty.','Material','Wt.', ' ',' ']
        
        table.setHorizontalHeaderLabels([header for header in table_header_list])
        #table.setLineWidth(2)
        font = table.horizontalHeader().font()
        font.setBold(True)
        table.horizontalHeader().setFont(font)

        # Populate the table with data
        #for row in range(3):
        #row=0
        for col in range(9):
                item = QTableWidgetItem("000000")
                table.setItem(0, col, item)
                table.setColumnWidth(col,80)

                if col==5:#Material Combobox
                    mat_list=var.master_mat_list
                    combobox=QComboBox()
                    combobox.addItems(mat_list)
                    table.setCellWidget(0,col,combobox)
                    #table.setColumnWidth(6,150)#set Width of combobox cell is 150px

                if col==6: #Wt cell  
                    #item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled & ~Qt.ItemFlag.ItemIsEditable) #Make it Non editable by user
                    self.disable_wt_cell(table,col)##Diable Wt Column Make it Non editable by user

                if col == 7:#Calc Wt Button
                    button = QPushButton("Calc. Wt")
                    button.clicked.connect(lambda:self.btn3_wt_calc(table))#lammbda function is anonymous function ,we use lambda as we can pass argment with connect event 
                    table.setCellWidget(0, col, button)

                if col == 8:#Add to BOM Button╛
                    button = QPushButton("Add to BOM")
                    button.clicked.connect(lambda:self.btn_Add_to_BOM(table))#lammbda function is anonymous function ,we use lambda so we can pass argment with connect event 
                    table.setCellWidget(0, col, button)

        table.setItem(0,0,QTableWidgetItem("U Bolt"))
        table.setItem(0,4,QTableWidgetItem("1"))
        self.set_table_size(table)     
        
        return table
    
    def btn1_wt_calc(self,table:QTableWidget):
        print("ADD BOM BUTTON from  TABLE 1 Clicked")
        thk =float(table.item(0,1).text())
        width=float(table.item(0,2).text())
        len=float(table.item(0,3).text())
        qty=float(table.item(0,4).text())
        density=7.85*10**-6
        wt=round(thk*width*len*qty*density,2)
        wt_column=6
        table.setItem(0,wt_column,QTableWidgetItem(str(wt))) # Overwrite the Wt cell widget with new cell Widget with new wt value
        table.cellWidget(0,8).setStyleSheet("")#Reset Color of "Add to BOM " Button ,on every calculation rerun.
        self.disable_wt_cell(table,wt_column)#Again disable Wt column as its we overwrite the previous CellWIdget on Wt column.
        #table.resizeColumnsToContents()
      
        
    def btn_Add_to_BOM(self,table:QTableWidget):
        item=table.item(0,0).text()
        item_name=table.item(0,0).text()
        combobox:QComboBox = table.cellWidget(0,5)#row=0,col=5--->combobox
        material=combobox.currentText()
        wt=table.item(0,6).text()
        _projectcontroller=ProjectController()
        _projectcontroller.add_update_item(item=item,item_name=item_name,wt=wt,material=material)
        print(wt,material)

        #table.resizeColumnsToContents()
        self.change_button_color_green()

    
    def btn2_wt_calc(self,table:QTableWidget):
        print("ADD BOM BUTTON from  TABLE 2 Clicked")
        NPS=table.cellWidget(0,1).currentText()
        SCHEDULE=table.cellWidget(0,2).currentText()
        
        wt_per_meter=float(self.get_elbow_wt_from_db(NPS,SCHEDULE))
        #some_valu_from_db =10 #Some value from DB of NPS & SCHEDULE
        
        len=float(table.item(0,3).text())
        qty=float(table.item(0,4).text())
        #density=7.85*10**-6
        wt=round(wt_per_meter*len*qty/1000,2)
        wt_column=6
        table.setItem(0,wt_column,QTableWidgetItem(str(wt)))
        table.cellWidget(0,8).setStyleSheet("")#Reset Color of "Add to BOM " Button ,on every calculation rerun.
        self.disable_wt_cell(table,wt_column)
        #table.resizeColumnsToContents()

    def get_elbow_wt_from_db(self,NPS,SCHEDULE):
        elbow_wt_per_meter=float(Get_Elbow_Details(NPS,SCHEDULE).WtPerMtr)
        return elbow_wt_per_meter
    
    
    def btn3_wt_calc(self,table:QTableWidget):
        print("ADD BOM BUTTON from  TABLE 3 Clicked")
        OD =float(table.item(0,1).text())
        ID=float(table.item(0,2).text())
        Lg=float(table.item(0,3).text())
        qty=float(table.item(0,4).text())
        density=7.85*10**-6
        wt=math.pi/4*(OD**2-ID**2)*Lg*qty*density
        print(OD,ID,Lg,qty,wt)
        wt=round(wt,2)
        wt_column=6
        table.setItem(0,wt_column,QTableWidgetItem(str(wt))) # Overwrite the Wt cell widget with new cell Widget with new wt value
        table.cellWidget(0,8).setStyleSheet("")#Reset Color of "Add to BOM " Button ,on every calculation rerun.
        self.disable_wt_cell(table,wt_column)#Again disable Wt column as its we overwrite the previous CellWIdget on Wt column. 
        #table.resizeColumnsToContents()   

    def disable_wt_cell(self,table:QTableWidget,col):
        table.item(0,col).setFlags(table.item(0,col).flags() & ~Qt.ItemFlag.ItemIsEnabled & ~Qt.ItemFlag.ItemIsEditable)   

    def change_button_color_green(self):
        button = self.sender()
        button.setStyleSheet("background-color: green; color: white;")

    def set_table_size(self,table:QTableWidget):
        width=[60,100,150]
        table.setColumnWidth(0,width[2])
        table.setColumnWidth(1,width[0])
        table.setColumnWidth(2,width[0])
        table.setColumnWidth(3,width[0])
        table.setColumnWidth(4,width[0])
        table.setColumnWidth(5,width[2])
        table.setColumnWidth(6,width[0])
        table.setColumnWidth(7,width[1])
        table.setColumnWidth(8,width[1])