
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout,QWidget, \
    QTabWidget,QGroupBox,QTableWidget,QTableWidgetItem,QGridLayout
from Variables import var
from PyQt6.QtCore import Qt
import math
from Controller.project_controller import ProjectController,Get_Elbow_Details

class Tab_Nozzle(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()
    def InitializeUI(self):
        #Nozzle count
        self.Nozzle_Instances=[]
        self.lbl_No_of_Nozzles=QLabel("No. of Nozzles")
        self.cmbbox_No_of_Nozzles=QComboBox()  
        self.cmbbox_No_of_Nozzles.addItems([str(i) for i in range(1,5)])
        self.cmbbox_No_of_Nozzles.currentIndexChanged.connect(self.Set_UI_as_per_Nozzle_Count)  
       
       #Nozzle count grpbox
        grpbox_nozzle_count=QGroupBox()
        grpbox_nozzle_count.setFixedSize(200,70)
        gridlayout_nozzle_count=QGridLayout()       
        gridlayout_nozzle_count.addWidget(self.lbl_No_of_Nozzles,0,0)
        gridlayout_nozzle_count.addWidget(self.cmbbox_No_of_Nozzles,1,0)
        grpbox_nozzle_count.setLayout(gridlayout_nozzle_count)
         
        V_box_main_layout=QVBoxLayout() 
        V_box_main_layout.addWidget(grpbox_nozzle_count,0,Qt.AlignmentFlag.AlignHCenter)
        
         # All the Nozzle UI goes into Vbox_Nozzle
        self.Vbox_nozzle=QVBoxLayout()
        V_box_main_layout.addLayout(self.Vbox_nozzle)
         
        
        
        
        self.setLayout(V_box_main_layout)
        self.cmbbox_No_of_Nozzles.setCurrentIndex(1)      
        
    def Set_UI_as_per_Nozzle_Count(self):
        #Clear everything from Vbox_nozzle_selction
        for i in reversed(range(self.Vbox_nozzle.count())):
            widget = self.Vbox_nozzle.itemAt(i).widget()
            if widget is not None:
                widget.close()
                
        self.No_of_Nozzles= int(self.cmbbox_No_of_Nozzles.currentText())
        for i in range(0,self.No_of_Nozzles):
            nozzle=Nozzle(i+1)
            self.Nozzle_Instances.clear()
            self.Nozzle_Instances.append(nozzle)
            self.Vbox_nozzle.addWidget(nozzle)
        
     

class Nozzle(QWidget):
    def __init__(self,Number:int):
        super().__init__() 
        self.Number=Number
        self.InitializeUI()

    def InitializeUI(self):
        self.grpbox=QGroupBox(f"Nozzle {self.Number}")
        self.gridlayout=QGridLayout()
        self.grpbox.setLayout(self.gridlayout)
        self.SetUI_for_Nozzles()
        vbox_main_layout=QVBoxLayout()
        vbox_main_layout.addWidget(self.grpbox)
        self.setLayout(vbox_main_layout)
        
    def SetUI_for_Nozzles(self):    
        
        self.lbl_Nozzle_On=QLabel("Nozzel On")
        self.cmbbox_Nozzle_On=QComboBox()
        self.cmbbox_Nozzle_On.setFixedWidth(100) 
        self.cmbbox_Nozzle_On.addItems(["SHELL","DEND"])
        
        
        self.lbl_Nozzle_type=QLabel("Nozzel Type")
        self.cmbbox_Nozzle_type=QComboBox()
        self.cmbbox_Nozzle_type.setFixedWidth(100)
        self.cmbbox_Nozzle_type.addItems(["FROM PIPE","FRPM  PLATE"])
        
        
        a=0
        alignment=Qt.AlignmentFlag.AlignLeft
        self.gridlayout.addWidget(self.lbl_Nozzle_On,0,0,alignment)
        self.gridlayout.addWidget(self.cmbbox_Nozzle_On,1,0,alignment)
        self.gridlayout.addWidget(self.lbl_Nozzle_type,2,0,alignment)
        self.gridlayout.addWidget(self.cmbbox_Nozzle_type,3,0,alignment)
        
        self.Set_UI_for_selected_Nozzle()
        
    def Set_UI_for_selected_Nozzle(self):
        self.Nozzle_ON=self.cmbbox_Nozzle_On.currentText()
        self.Nozzle_TYPE=self.cmbbox_Nozzle_type.currentText()
        if(self.Nozzle_ON=='SHELL' and self.Nozzle_TYPE=='From PIPE'):
            nozzle_selcted=Nozzle_Shell('FROM PIPE')
        elif(self.Nozzle_ON=='SHELL' and self.Nozzle_TYPE=='From PLATE'):
            nozzle_selcted=Nozzle_Shell('FROM PLATE') 
        elif(self.Nozzle_ON=='DEND' and self.Nozzle_TYPE=='From PIPE'):
            nozzle_selcted=Nozzle_DEnd('FROM PIPE')
        elif(self.Nozzle_ON=='SHELL' and self.Nozzle_TYPE=='From PLATE'):
            nozzle_selcted=Nozzle_Shell('FROM PLATE')           
           
 
class Nozzle_Shell(QWidget):
    def __init__(self,Nozzle_TYPE:str):
        super().__init__() 
        self.Nozzle_TYPE=Nozzle_TYPE
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
      
class Nozzle_DEnd(QWidget):
    pass        
        
        
        


# class Nozzle_Selection(QWidget):
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
#         item=table.item(0,0).text()
#         item_name=table.item(0,0).text()
#         combobox:QComboBox = table.cellWidget(0,5)#row=0,col=5--->combobox
#         material=combobox.currentText()
#         wt=table.item(0,6).text()
#         _projectcontroller=ProjectController()
#         _projectcontroller.add_update_item(item=item,item_name=item_name,wt=wt,material=material)
#         print(wt,material)

#         #table.resizeColumnsToContents()
#         self.change_button_color_green()

    
#     def btn2_wt_calc(self,table:QTableWidget):
#         print("ADD BOM BUTTON from  TABLE 2 Clicked")
#         NPS=table.cellWidget(0,1).currentText()
#         SCHEDULE=table.cellWidget(0,2).currentText()
        
#         wt_per_meter=float(self.get_elbow_wt_from_db(NPS,SCHEDULE))
#         #some_valu_from_db =10 #Some value from DB of NPS & SCHEDULE
        
#         len=float(table.item(0,3).text())
#         qty=float(table.item(0,4).text())
#         #density=7.85*10**-6
#         wt=round(wt_per_meter*len*qty/1000,2)
#         wt_column=6
#         table.setItem(0,wt_column,QTableWidgetItem(str(wt)))
#         table.cellWidget(0,8).setStyleSheet("")#Reset Color of "Add to BOM " Button ,on every calculation rerun.
#         self.disable_wt_cell(table,wt_column)
#         #table.resizeColumnsToContents()

#     def get_elbow_wt_from_db(self,NPS,SCHEDULE):
#         elbow_wt_per_meter=float(Get_Elbow_Details(NPS,SCHEDULE).WtPerMtr)
#         return elbow_wt_per_meter
    
    
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