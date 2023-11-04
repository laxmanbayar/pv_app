
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout,QWidget, \
    QTabWidget,QGroupBox,QTableWidget,QTableWidgetItem
from Variables import var
from PyQt6.QtCore import Qt,QTimer
import math
#from Controller.project_controller import read_estimation_table,read_surface_area_table
from Controller.project_controller import ProjectController


class Tab4_BOM(QWidget):
    def __init__(self):
        super().__init__()        
        self.InitializeUI()
        
    def InitializeUI(self):
        self.V_box_layout= QVBoxLayout()
        self.btn_refresh_data=QPushButton("Refresh Data")
        self.btn_refresh_data.setFixedSize(120,30)
        self.btn_refresh_data.setStyleSheet("background-color:lightgrey")
        self.btn_refresh_data.clicked.connect(self.Refresh_Data)
        self.V_box_layout.addWidget(self.btn_refresh_data,1,Qt.AlignmentFlag.AlignRight)
        self.Refresh_Data() 
        
        
        
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.Refresh_Data)
        # self.timer.start(10000)  # Update every 2 seconds       
       
        self.V_box_main_layout=QVBoxLayout()       
        self.V_box_main_layout.addLayout(self.V_box_layout)
       

        self.setLayout(self.V_box_main_layout)
        
    def Refresh_Data(self):
        try:
            self.V_box_layout.removeWidget(self.Estimation)
            self.V_box_layout.removeWidget(self.SurfaceArea)
        except Exception as e:
            pass     
        self.Estimation=Estimation_Detail()
        self.SurfaceArea=SurfaceArea_Detail()
        self.V_box_layout.addWidget(self.Estimation)
        self.V_box_layout.addWidget(self.SurfaceArea)
        

class Estimation_Detail(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()

    def InitializeUI(self):      
        self.estimation_table:QTableWidget=self.setUp_estimation_table()
        
        self.Vbox_layout_estimation=QVBoxLayout()
        self.Vbox_layout_estimation.addWidget(self.estimation_table)
        self.grpbox_estimation = QGroupBox("Estimation Data")
        self.grpbox_estimation.setStyleSheet(customStyles.estimation_grpbox_style)
        self.grpbox_estimation.setLayout(self.Vbox_layout_estimation)
        
        self.Vbox_main_layout_estimation=QVBoxLayout()
        self.Vbox_main_layout_estimation.addWidget(self.grpbox_estimation)
        self.setLayout(self.Vbox_main_layout_estimation)    
    
        
    # def set_Estimation_table_layout(self):
        
    #     self.estimation_table:QTableWidget=self.setUp_estimation_table()
    #     #self.setUp_estimation_table()     
        
    #     self.Vbox_layout_estimation=QVBoxLayout()
    #     self.Vbox_layout_estimation.addWidget(self.estimation_table)
    #     self.grpbox_estimation = QGroupBox("Estimation Data")
    #     self.grpbox_estimation.setStyleSheet(customStyles.estimation_grpbox_style)
    #     self.grpbox_estimation.setLayout(self.Vbox_layout_estimation)
        
    #     self.Vbox_main_layout_estimation=QVBoxLayout()
    #     self.Vbox_main_layout_estimation.addWidget(self.grpbox_estimation)
    #     self.setLayout(self.Vbox_main_layout_estimation)    
        
        
    
    def setUp_estimation_table(self):
        _ProjectController=ProjectController() 
        data,column_names=_ProjectController.read_estimation_table()
        column_names.pop(0) #Remove SNo. Column
        row_count,col_count=len(data),len(column_names)
                 
        table =QTableWidget(row_count,col_count)
        table_header_list=column_names#['Item','Item Description','Wt(in kg)','Material']
        
        table.setHorizontalHeaderLabels(table_header_list)#[header for header in table_header_list])
        #table.setLineWidth(2)
        font = table.horizontalHeader().font()
        font.setBold(True)
        table.horizontalHeader().setFont(font)
        for row_num, row in enumerate(data):
            for col_num, col_name in enumerate(column_names):
                # print(getattr(row, col_name))
                # if(col_num==0):#First Column(SNo.)
                #     item = QTableWidgetItem(str(col_num+1)) 
                # else:
                #     item = QTableWidgetItem(str(getattr(row, col_name)))
                item = QTableWidgetItem(str(getattr(row, col_name)))    
                table.setItem(row_num, col_num, item)
                table.setColumnWidth(col_num,200)
                
        #self.estimation_table=table
        return table   
        
        
class SurfaceArea_Detail(QWidget):
    def __init__(self):
        super().__init__()
        self.InitializeUI()

    def InitializeUI(self):
        self.surface_area_table:QTableWidget=self.setUp_surface_area_table()
        self.Vbox_layout_surface_area=QVBoxLayout()
        self.Vbox_layout_surface_area.addWidget(self.surface_area_table)
        self.grpbox_surface_area = QGroupBox("Surface Area Data")
        self.grpbox_surface_area.setStyleSheet(customStyles.surface_area_grpbox_style)
        self.grpbox_surface_area.setLayout(self.Vbox_layout_surface_area)
       
        
        self.Vbox_main_layout_surface_area=QVBoxLayout()
        self.Vbox_main_layout_surface_area.addWidget(self.grpbox_surface_area)
        self.setLayout(self.Vbox_main_layout_surface_area)    
        
    
    def setUp_surface_area_table(self):
        _ProjectController=ProjectController()        
        data,column_names=_ProjectController.read_surface_area_table()
        column_names.pop(0) #Remove SNo. Column
        row_count,col_count=len(data),len(column_names)
                 
        table =QTableWidget(row_count,col_count)
         # Set the size policy to Expanding and horizontal stretch factor to 1
     
        table_header_list=column_names#['Item','Item Description',''Surface Area']
        
        table.setHorizontalHeaderLabels(table_header_list)#[header for header in table_header_list])
        #table.setLineWidth(2)
        font = table.horizontalHeader().font()
        font.setBold(True)
        table.horizontalHeader().setFont(font)
        for row_num, row in enumerate(data):
            for col_num, col_name in enumerate(column_names):
                # print(getattr(row, col_name))
                # if(col_num==0):#First Column(SNo.)
                #     item = QTableWidgetItem(str(col_num+1)) 
                # else:
                #     item = QTableWidgetItem(str(getattr(row, col_name)))
                item = QTableWidgetItem(str(getattr(row, col_name)))    
                table.setItem(row_num, col_num, item)
                table.setColumnWidth(col_num,200)
                
        return table   
        
        
         


class customStyles:
    estimation_grpbox_style="""
                QGroupBox {
                    font: bold;
                    font-size:14px;
                    padding: 15px;
                    border: 1px solid silver;
                    border-radius: 6px;
                    margin-top: 5px;
                    background-color:#ccf5ff                    

                }
                """
    surface_area_grpbox_style="""
                QGroupBox {
                    font: bold;
                    font-size:14px;
                    padding: 15px;
                    border: 1px solid silver;
                    border-radius: 6px;
                    margin-top: 5px;
                    background-color:#ccf5ff                     

                }
                """            