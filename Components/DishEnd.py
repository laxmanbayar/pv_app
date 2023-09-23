import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QWidget, \
    QTabWidget, QGroupBox, QPushButton, QHBoxLayout, QScrollArea, QGridLayout,QSpacerItem,QSizePolicy,QMessageBox,QSlider
from PyQt6.QtCore import Qt
#from Variables.var import Variables
from PyQt6.QtGui import *
from Calculation.abs_path import absolute_path
from Variables import var
import sys
import re
import math
from DataBase.DB_config import DB_config_class
from Controller.project_controller import add_or_update_material,add_or_update_surface_area
from Controller.project_controller import ProjectController




class Tab1_DEnd(QWidget):
    dentype=0
    def __init__(self):
        super().__init__()
        
        self.InitializeUI()

    def InitializeUI(self):
        self.setUp_DEnd_tab_layout()
       
       
    def setUp_DEnd_tab_layout(self):
        
        #UI for Top DIsh END   
        self.Top_DishEnd_selction=DEnd_selction("Top")
        #self.Top_DishEnd_var_selction.setFixedHeight(150)
        
        #UI for Bottom DIsh END
        self.Bottom_DishEnd_selction=DEnd_selction("Bottom")
        #self.Bottom_DishEnd_var_selction.setFixedHeight(150)
        
              
       
        self.VBox_all_grp_box_layout = QVBoxLayout()
       
        #Load Default DISHEND SELECTION(Both BALNK TYPE)
        self.SetUp_default_DEND_on_form_load()
        
        # add one container widget and set its Lsyout as "Vbox_all_grp_box_layout"
        self.container_widget = QWidget()
        self.container_widget.setLayout(self.VBox_all_grp_box_layout)

        # Create new Scroll area and set it as resizable
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Set the container widget as the widget for the scroll area
        self.scroll_area.setWidget(self.container_widget)

        # Add the scroll area to the main layout
        main_v_box = QVBoxLayout(self)
        main_v_box.addWidget(self.scroll_area)
        self.setLayout(main_v_box)
     
        #As per Dend type=Blank or crown petal ,Adjust the UI on if selcetion combobox is changed
        self.Top_DishEnd_selction.cmbbox_DEnd_var_sel.currentIndexChanged.connect(self.SetUI_for_Top_DEND_variant)
        self.Bottom_DishEnd_selction.cmbbox_DEnd_var_sel.currentIndexChanged.connect(self.SetUI_for_Bottom_DEND_variant)
        
        self.Top_DishEnd_selction.cmbbox_d_end_shape_sel.currentIndexChanged.connect(self.set_Shape_for_Top_DEND)
        self.Bottom_DishEnd_selction.cmbbox_d_end_shape_sel.currentIndexChanged.connect(self.set_Shape_for_Bottom_DEND)    
        


    def SetUp_default_DEND_on_form_load(self):
        #On form load this function will add both top and bototm Dish end as "BLANK" type as default.
        self.VBox_all_grp_box_layout.addWidget(self.Top_DishEnd_selction)
        self.Top_Dish_End=DEND_blk_type("Top")
        self.VBox_all_grp_box_layout.addWidget(self.Top_Dish_End)
        
        self.VBox_all_grp_box_layout.addWidget(self.Bottom_DishEnd_selction)
        self.Bottom_Dish_End=DEND_blk_type("Bottom")     
        self.VBox_all_grp_box_layout.addWidget(self.Bottom_Dish_End)
        
        # #As default DEND type on form load is 'BLANK' type for both top and bottom Dish End.
        # dend_shape= self.Top_DishEnd_var_selction.cmbbox_d_end_shape_type.currentText()
        # #pass on the DEND shape to the BLANK type as per combobox selection   
        # self.setShape_for_DEND(location='TOP',shape=dend_shape)     
      
    
    #This Function Either Set Variant Type(BLANK type or Crown Type Top DIsh ENd) as depending upon user selected shape 
    def SetUI_for_Top_DEND_variant(self):
        #This Function Either Set BLANK type or Crown Type Top DIsh ENd as depending upon user selected shape 
        top_dend_variant=self.Top_DishEnd_selction.cmbbox_DEnd_var_sel.currentText() #Blank or Crown_Petal
        
        if(str.upper(top_dend_variant)=='BLANK'):            
            self.Top_Dish_End=DEND_blk_type("Top")                      
        else:
            self.Top_Dish_End=DEND_crwn_petal_type("Top")
            
        #Remove the Top end Dish and i.e. groupbox at location(1) and replace it with new widget(Dishend-BLANL or Crown/petal) as per user selection  
        self.VBox_all_grp_box_layout.removeWidget(self.VBox_all_grp_box_layout.itemAt(1).widget())
        self.VBox_all_grp_box_layout.insertWidget(1,self.Top_Dish_End)
        self.set_Shape_for_Top_DEND()   
        #dend_shape= self.Top_DishEnd_var_selction.cmbbox_d_end_shape_type.currentText()
        #pass on the DEND shape to the BLANK or Crown-Petal class as per combobox selection
        #self.setShape_for_DEND(location='TOP',shape=dend_shape)
        #self.Top_DishEnd_var_selction.cmbbox_d_end_shape_type.currentIndexChanged.connect(self.set_Shape_for_Top_DEND(location='TOP',shape=dend_shape))   
             
  
    def SetUI_for_Bottom_DEND_variant(self):
        
        bottom_dend_variant=self.Bottom_DishEnd_selction.cmbbox_DEnd_var_sel.currentText() #Blank or Crown_Petal
             
        if(str.upper(bottom_dend_variant)=='BLANK'):            
            self.Bottom_Dish_End=DEND_blk_type("Bottom")            
        else:
            self.Bottom_Dish_End=DEND_crwn_petal_type("Bottom")
           
        #Remove the Bottom end Dish and i.e. groupbox at location(3) and replace it with new widget(Dishend-BLANL or Crown/petal) as per user selection      
        self.VBox_all_grp_box_layout.removeWidget(self.VBox_all_grp_box_layout.itemAt(3).widget())
        self.VBox_all_grp_box_layout.insertWidget(3,self.Bottom_Dish_End)
        self.set_Shape_for_Bottom_DEND()
        #dend_shape= self.Bottom_DishEnd_var_selction.cmbbox_d_end_shape_type.currentText()    
        #self.set_Shape_for_Top_DEND(location='BOTTOM',shape=dend_shape)
        #self.Bottom_DishEnd_var_selction.cmbbox_d_end_shape_type.currentIndexChanged.connect(self.set_Shape_for_Top_DEND(location='BOTTOM',shape=dend_shape))    
        
  
    def set_Shape_for_Top_DEND(self):
        self.Top_Dish_End.D_End_shape= self.Top_DishEnd_selction.cmbbox_d_end_shape_sel.currentText()
       
        
    def set_Shape_for_Bottom_DEND(self):
        self.Bottom_Dish_End.D_End_shape= self.Bottom_DishEnd_selction.cmbbox_d_end_shape_sel.currentText()    

class DEnd_selction(QWidget):#DISH END SELECTION GROUPBOX UI
    def __init__(self,location):
        super().__init__()
        self.location=location
        self.title=location+ " Dish End" #location=Top or Bottom
        self.InitializeUI() 
        
    def InitializeUI(self):
        self.setUp_UI_dish_end_selection() 
        
    
    #UI For BLANK/CRN_PETAL type and Ellip/Tori Selection       
    def setUp_UI_dish_end_selection(self):
        
        #Dish End Variant Selection :-BLANK TYPE or CROWN & PETAL TYPE
        self.lbl_d_end_var_sel = QLabel("Type of Dish End")
        self.lbl_d_end_var_sel.setStyleSheet("background-color: lightgreen; font-weight: bold;")
        self.cmbbox_DEnd_var_sel=QComboBox()
        type_list=['Blank','Crown and Petal']
        self.cmbbox_DEnd_var_sel.addItems(type_list)
        #self.cmbbox_DEnd_var_sel.currentIndexChanged.connect(self.SetUI_asper_DEND)
        self.cmbbox_DEnd_var_sel.setStyleSheet("background-color: lightgrey; font-weight: bold;")
        
        
         #Dish End Shape Selection :-'Ellipsoidal'/'Tori Spherical'
        self.lbl_DEnd_type =QLabel("Select Shape")
        self.lbl_DEnd_type.setStyleSheet("background-color: lightgreen; font-weight: bold;")
        self.cmbbox_d_end_shape_sel=QComboBox()
        self.DEnd_shape_list=['----','Ellipsoidal','Tori Spherical']
        self.cmbbox_d_end_shape_sel.addItems(self.DEnd_shape_list)
        self.cmbbox_d_end_shape_sel.setStyleSheet("background-color: lightgrey; font-weight: bold;")
        
        
        self.dishEnd_sel_gridlayout=QGridLayout()
        
        self.dishEnd_sel_gridlayout.addWidget(self.lbl_d_end_var_sel,0,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.dishEnd_sel_gridlayout.addWidget(self.cmbbox_DEnd_var_sel,0,1,alignment=Qt.AlignmentFlag.AlignLeft)
        self.dishEnd_sel_gridlayout.addWidget(self.lbl_DEnd_type,1,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.dishEnd_sel_gridlayout.addWidget(self.cmbbox_d_end_shape_sel,1,1,alignment=Qt.AlignmentFlag.AlignLeft)
        self.grpbbox_dishend_var_sel=QGroupBox(self.title)
        self.grpbbox_dishend_var_sel.setLayout(self.dishEnd_sel_gridlayout)
        self.Vbox_dishend_var_sel=QVBoxLayout()
        self.Vbox_dishend_var_sel.addWidget(self.grpbbox_dishend_var_sel)
        
        self.setLayout(self.Vbox_dishend_var_sel)
        if (self.location=="Top"):
            self.setStyleSheet(common_functionality.DishEnd_style_1)
        else:
            self.setStyleSheet(common_functionality.DishEnd_style_2)    
      
    
class DEND_blk_type(QWidget): #Variant=BLANK TYPE
    def __init__(self,location):
        super().__init__()
        self.D_End_shape:str="" #Tori/ellip/sherical
        self.D_End_location=location
        self.Item_Name="dish_end_" + self.D_End_location
        self.InitializeUI()
        
    def InitializeUI(self):
        self.setUp_UI_DEND_Blk_type()
    
    def setUp_UI_DEND_Blk_type(self):
        self.setUP_UI_Blk_dia_Calc()
        self.SetUP_UI_Plt_Sizing_Calc()
        self.setup_Main_layout()
        self.set_defaults()
        
    def setUP_UI_Blk_dia_Calc(self):
         #BLANK Dia Calc
        self.lbl_blktype_ID=QLabel("ID")
        self.tb_blktype_ID = QLineEdit("0.00")
        self.lbl_blktype_thk=QLabel("Thk")
        self.tb_blktype_thk = QLineEdit("0.00")
        self.lbl_blktype_stface_len=QLabel("Straigh Face")
        self.tb_blktype_stface_len = QLineEdit("0.00")
        self.lbl_blktype_Material =QLabel("Material")
        self.cmbbox_blktype_DEnd_Material=QComboBox()
        self.Material_list=var.master_mat_list
        self.cmbbox_blktype_DEnd_Material.addItems(self.Material_list)
        self.lbl_blktype_mat_density=QLabel("Density")
        self.tb_blktype_mat_density = QLineEdit("7.85")
        self.lbl_blktype_ICR=QLabel("ICR")
        self.tb_blktype_ICR = QLineEdit("0.00")
        self.tb_blktype_ICR.setEnabled(False) 
        self.lbl_blktype_IKR=QLabel("IKR")
        self.tb_blktype_IKR = QLineEdit("0.00")
        self.tb_blktype_IKR.setEnabled(False) 
        self.lbl_blktype_BLKDIA=QLabel("BLANK DIA")
        self.tb_blktype_BLKDIA = QLineEdit("0.00")
        self.tb_blktype_BLKDIA.setEnabled(False)
        self.button_calc_blkdia = QPushButton("Calculate BLANK DIA")
        self.button_calc_blkdia.setFixedSize(150, 30)
        self.button_calc_blkdia.setStyleSheet("QPushButton{font-weight: bold}")
        self.button_calc_blkdia.clicked.connect(self.calc_Blkdia)
        
        
        #Putting items on layout1 
        #BLANK Dia Calc Widgets 
        self.gridlayout_blktype=QGridLayout()        
        self.gridlayout_blktype.addWidget(self.lbl_blktype_ID,0,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_blktype.addWidget(self.tb_blktype_ID,0,1)
        self.gridlayout_blktype.addWidget(self.lbl_blktype_thk,0,2,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_blktype.addWidget(self.tb_blktype_thk,0,3)
        self.gridlayout_blktype.addWidget(self.lbl_blktype_stface_len,1,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_blktype.addWidget(self.tb_blktype_stface_len,1,1)
        self.gridlayout_blktype.addWidget(self.lbl_blktype_Material,1,2,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_blktype.addWidget(self.cmbbox_blktype_DEnd_Material,1,3)
        self.gridlayout_blktype.addWidget(self.lbl_blktype_ICR,2,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_blktype.addWidget(self.tb_blktype_ICR,2,1)
        self.gridlayout_blktype.addWidget(self.lbl_blktype_IKR,2,2,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_blktype.addWidget(self.tb_blktype_IKR,2,3)
        self.gridlayout_blktype.addWidget(self.lbl_blktype_BLKDIA,3,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_blktype.addWidget(self.tb_blktype_BLKDIA,3,1)
        self.gridlayout_blktype.addWidget(self.lbl_blktype_mat_density,3,2,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_blktype.addWidget(self.tb_blktype_mat_density,3,3)        
        self.gridlayout_blktype.addWidget(self.button_calc_blkdia,4,2)
        
             #Main GroupBox for BLANK DIA Calc
        self.main_grpbox_blktype = QGroupBox("BLANK Calc")
        #self.main_grpbox_blktype.setStyleSheet(common_functionality.DishEnd_style_1)
        self.main_grpbox_blktype.setLayout(self.gridlayout_blktype)
       
        
    def SetUP_UI_Plt_Sizing_Calc(self):
        
         #Plate Sizing Calc
        self.No_of_plates=1
        self.No_of_Segments=1
        self.Large_segment_width=None
        self.Small_segment_width=None
            
        self.lbl_No_of_Plates_required_for_blank=QLabel(f"<b>No of Plates required for Blank Cutting</b>")
        self.rb_single_plate=QRadioButton("1")             
        self.rb_two_plate=QRadioButton("2")
        self.rb_single_plate.setStyleSheet(common_functionality.rb_stylesheet)
        self.rb_two_plate.setStyleSheet(common_functionality.rb_stylesheet)
        self.rb_single_plate.clicked.connect(self.radio_button_changed)
        self.rb_two_plate.clicked.connect(self.radio_button_changed)
        
        #Segment      
        self.lbl_large_segment_ratio=QLabel(f"Large Segment Ratio (in %): <b>{str('XXX')}</b>")        
        # Create a slider
        self.slider_segment_ratio = QSlider(self)
        self.slider_segment_ratio.setStyleSheet(common_functionality.slider_style)              
        self.slider_segment_ratio.setOrientation(Qt.Orientation.Horizontal)  # Set the orientation to Horizontal
        self.slider_segment_ratio.setMinimum(50)
        self.slider_segment_ratio.setMaximum(100)
        self.slider_segment_ratio.setTickInterval(1)    
        self.slider_segment_ratio.valueChanged.connect(self.sliderValueChanged)
        self.lbl_large_segment_width=QLabel(f"Large Segment width: <b>{str('XXX')}</b>") 
        self.lbl_small_segment_width=QLabel(f"Small Segment width: <b>{str('XXX')}</b>") 
        
        #Avilable Raw Mat Plate COmbobox(For Large Section and Small Section)
        self.lbl_avl_raw_mat_plt1_width=QLabel("Selcet Available Plate Width(Larger-Section)")
        self.cmbbox_avl_raw_mat_plt1_width=QComboBox()
        self.cmbbox_avl_raw_mat_plt1_width.setFixedSize(100, 20)
        self.avl_plate_width=var.avl_plate_width_for_DEND
        self.avl_plate_width.insert(0,'0')#Insert '0" in begining of the
        self.cmbbox_avl_raw_mat_plt1_width.addItems(self.avl_plate_width)
        self.lbl_avl_raw_mat_plt2_width=QLabel("Selcet Available Plate Width(Smaller-Section)")
        self.cmbbox_avl_raw_mat_plt2_width=QComboBox()
        self.cmbbox_avl_raw_mat_plt2_width.setFixedSize(100, 20)        
        self.cmbbox_avl_raw_mat_plt2_width.addItems(self.avl_plate_width)
        
        #Optimum Calculated Plate Len for Largeand Small Section
        self.lbl_optimum_plt1_len=QLabel("Optimum Plate1 Length")
        self.tb_optimum_plt1_len = QLineEdit("0.00")
        self.tb_optimum_plt1_len.setEnabled(False) 
        self.lbl_optimum_plt2_len=QLabel("Optimum Plate2 Length")
        self.tb_optimum_plt2_len = QLineEdit("0.00")
        self.tb_optimum_plt2_len.setEnabled(False) 
        self.button_calc_opt_plt_len = QPushButton("Optimize Plate length")
        
        #Button-Calculate Optimum Length
        self.button_calc_opt_plt_len.setFixedSize(150, 30)
        self.button_calc_opt_plt_len.setStyleSheet("QPushButton{font-weight: bold;}")
        self.button_calc_opt_plt_len.clicked.connect(self.btn_clicked_calc_optimum_plt_size)
        
        #Output
        self.lbl_blktype_Wt=QLabel("Weight")
        self.tb_blktype_Wt = QLineEdit("0.00")
        self.tb_blktype_Wt.setEnabled(False)
        self.lbl_blktype_Surface_area=QLabel("Surface Area")
        self.tb_blktype_Surface_area=QLineEdit("Surface Area")
        self.tb_blktype_Surface_area.setEnabled(False)
        self.lbl_blktype_Raw_mat_plt1_size=QLabel("Raw_material Plate Size(LXW)")
        self.tb_blktype_Raw_mat_plt1_size=QLineEdit("00")
        self.tb_blktype_Raw_mat_plt1_size.setEnabled(False)
        self.lbl_blktype_Raw_mat_plt2_size=QLabel("Raw_material Plate Size(LXW)")
        self.tb_blktype_Raw_mat_plt2_size=QLineEdit("00")
        self.tb_blktype_Raw_mat_plt2_size.setEnabled(False)
        self.btn_add_to_BOM = QPushButton("ADD to BOM") 
        self.btn_add_to_BOM.setEnabled(False)
        self.btn_add_to_BOM.setFixedSize(150, 30)
        self.btn_add_to_BOM.setStyleSheet("QPushButton{font-weight: bold;}")  
        self.btn_add_to_BOM.clicked.connect(self.Add_to_BOM)  
        
      
        #Putting items on layout2 
        #Plate Sizing GroupBox2
        self.grpbox_plt_selc_blktype=QGroupBox("Plate Sizing")
        #self.grpbox_plt_selc_blktype.setStyleSheet(common_functionality.DishEnd_style_1)
        self.gridlayout_plt_selc_blktype=QGridLayout()
        
        self.Hbox_no_of_plates=QHBoxLayout()        
        self.Hbox_no_of_plates.addWidget(self.lbl_No_of_Plates_required_for_blank)
        self.Hbox_no_of_plates.addWidget(self.rb_single_plate)
        self.Hbox_no_of_plates.addWidget(self.rb_two_plate)
      
        self.gridlayout_plt_selc_blktype.addLayout(self.Hbox_no_of_plates,0,2,alignment=Qt.AlignmentFlag.AlignHCenter)
        self.gridlayout_plt_selc_blktype.addWidget(self.lbl_large_segment_ratio,1,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_plt_selc_blktype.addWidget(self.slider_segment_ratio,1,1)
        self.gridlayout_plt_selc_blktype.addWidget(self.lbl_large_segment_width,1,2)
        self.gridlayout_plt_selc_blktype.addWidget(self.lbl_small_segment_width,1,3)        
        self.gridlayout_plt_selc_blktype.addWidget(self.lbl_avl_raw_mat_plt1_width,2,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_plt_selc_blktype.addWidget(self.cmbbox_avl_raw_mat_plt1_width,2,1)
        self.gridlayout_plt_selc_blktype.addWidget(self.lbl_avl_raw_mat_plt2_width,2,2,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_plt_selc_blktype.addWidget(self.cmbbox_avl_raw_mat_plt2_width,2,3)
        self.gridlayout_plt_selc_blktype.addWidget(self.lbl_optimum_plt1_len,3,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_plt_selc_blktype.addWidget(self.tb_optimum_plt1_len,3,1)
        self.gridlayout_plt_selc_blktype.addWidget(self.lbl_optimum_plt2_len,3,2,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_plt_selc_blktype.addWidget(self.tb_optimum_plt2_len,3,3)
        self.gridlayout_plt_selc_blktype.addWidget(self.button_calc_opt_plt_len,4,2)
        
        #Output adding to Layout        
        self.gridlayout_plt_selc_blktype.addWidget(QLabel(text="Output",styleSheet='font:bold'),5,0)
        self.gridlayout_plt_selc_blktype.addWidget(self.lbl_blktype_Wt,6,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_plt_selc_blktype.addWidget(self.tb_blktype_Wt,6,1)
        self.gridlayout_plt_selc_blktype.addWidget(self.lbl_blktype_Surface_area,6,2,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_plt_selc_blktype.addWidget(self.tb_blktype_Surface_area,6,3)
        self.gridlayout_plt_selc_blktype.addWidget(self.lbl_blktype_Raw_mat_plt1_size,7,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_plt_selc_blktype.addWidget(self.tb_blktype_Raw_mat_plt1_size,7,1)
        self.gridlayout_plt_selc_blktype.addWidget(self.lbl_blktype_Raw_mat_plt2_size,7,2,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_plt_selc_blktype.addWidget(self.tb_blktype_Raw_mat_plt2_size,7,3)
        self.gridlayout_plt_selc_blktype.addWidget(self.btn_add_to_BOM,8,2)
        
        self.grpbox_plt_selc_blktype.setLayout(self.gridlayout_plt_selc_blktype)
        
    
    def setup_Main_layout(self):
        self.Vbox_main_blktype=QVBoxLayout()
        self.Vbox_main_blktype.addWidget(self.main_grpbox_blktype)
        self.Vbox_main_blktype.addWidget(self.grpbox_plt_selc_blktype)
        self.setLayout(self.Vbox_main_blktype)
        
        if (self.D_End_location=="Top"):
            self.setStyleSheet(common_functionality.DishEnd_style_1)
        else:    
            self.setStyleSheet(common_functionality.DishEnd_style_2)
     
    def set_defaults(self):
        self.grpbox_plt_selc_blktype.setVisible(False)#Bydefault Groupbox is disabled
        self.cmbbox_avl_raw_mat_plt2_width.setEnabled(False)
        self.button_calc_opt_plt_len.setEnabled(False)       
        self.rb_single_plate.setChecked(True)#Deafult "No of plates==1" 
            
    
    def calc_Blkdia(self):
        #BLKDIA Calculation
        blktype_IKR,blktype_ICR=0,0        
        if(bool(re.match('[a-zA-Z\s]+$', self.D_End_shape))):#D_End_shape selection string has only Alphabets not "-----"
            if(str.upper(self.D_End_shape)=='TORI SPHERICAL'):
                blktype_IKR =float(self.tb_blktype_ID.text())*0.15
                blktype_ICR=float(self.tb_blktype_ID.text())*0.8
            elif (str.upper(self.D_End_shape)=='ELLIPSOIDAL'):
                blktype_IKR =float(self.tb_blktype_ID.text())*0.1727 
                blktype_ICR=float(self.tb_blktype_ID.text())*0.9045
            
            blktype_BLKDIA=(float(self.tb_blktype_ID.text())+2*float(self.tb_blktype_thk.text()))+((float(self.tb_blktype_ID.text())+2*float(self.tb_blktype_thk.text()))/24)+2/3*blktype_IKR+2*float(self.tb_blktype_stface_len.text())+float(self.tb_blktype_thk.text())
            blktype_BLKDIA=round(blktype_BLKDIA)
            self.tb_blktype_IKR.setText(str(blktype_IKR))
            self.tb_blktype_IKR.setEnabled(False)  
            self.tb_blktype_ICR.setText(str(blktype_ICR)) 
            self.tb_blktype_ICR.setEnabled(False) 
            self.tb_blktype_BLKDIA.setText(str(blktype_BLKDIA) )
            self.tb_blktype_BLKDIA.setEnabled(False) 
            
            self.calc_defaults()
            
                
        else:
            common_functionality.Show_MessageBox(self,"Pls Select Suitable Dish End type")
            
    
    #Based on BLANK DIA ,set No_of_segment and No_of_raw_mat_plate and call appropriate Function to Set UI.     
    def calc_defaults(self):
        self.reset_widgets()
        blk_dia= float(self.tb_blktype_BLKDIA.text())
        if(blk_dia<=2500):
                self.No_of_Segments=1 #Cut entire Blank drom Single Plate
                self.No_of_plates=self.get_set_No_of_raw_mat_plates()
                self.slider_segment_ratio.setValue(100)
                self.sliderValueChanged()
                self.blk_dia_with_Single_Segment()                
        elif(blk_dia>2500):
                self.No_of_Segments=2 #Divide Blank into two Segments and cut as per user selection
                self.No_of_plates=self.get_set_No_of_raw_mat_plates()
                self.slider_segment_ratio.setValue(67)
                self.sliderValueChanged()
                self.rb_single_plate.setEnabled(True)
                self.rb_two_plate.setEnabled(True)
                self.blk_dia_with_two_Segment()  
    
    #Reset ALl the output If user Recalculates BALNK DIA              
    def reset_widgets(self):
        self.tb_optimum_plt1_len.setText("0")
        self.tb_optimum_plt2_len.setText("0")
        self.tb_blktype_Wt.setText("0")
        self.tb_blktype_Surface_area.setText("0")
        self.tb_blktype_Raw_mat_plt1_size.setText("0")
        self.tb_blktype_Raw_mat_plt2_size.setText("0")
        self.btn_add_to_BOM.setEnabled(False)
        
        
    #This Function is called when Button "Calc Optimum Size" is pressed
    #Based on No of Segments and No of Row mat Call the Function which Calculates WHich Raw Raw Mat plates can Accomodate the BLK Segments    
    def btn_clicked_calc_optimum_plt_size(self):
        No_of_raw_mat_plates=self.get_set_No_of_raw_mat_plates()
        if (self.No_of_Segments==1):           
            self.Calc_for_single_Segment()
        elif(self.No_of_Segments==2 and No_of_raw_mat_plates==1):
            self.Calc_for_two_Segment_one_plate()
        elif(self.No_of_Segments==2 and No_of_raw_mat_plates==2):
            self.Calc_for_two_Segment_two_plates()
        self.reset_button_color_default(self.btn_add_to_BOM) #Reset Color of the Add to BOM to default.
             
    #SetUI for SIngle Segment
    def blk_dia_with_Single_Segment(self):        
        self.setUI_for_single_Segment()      
     
     #SetUI for Two Segments   
    def blk_dia_with_two_Segment(self):
        No_of_raw_mat_plates=self.get_set_No_of_raw_mat_plates()
        if(No_of_raw_mat_plates==1):
            self.setUI_for_two_Segment_one_plate()          
        elif(No_of_raw_mat_plates==2):
            self.setUI_for_two_Segment_two_plates()
         
     #This Function returns No of Raw mat Plates Selection based on user selection of Radio button
     #also sets the value of No_of_plates variables        
    def get_set_No_of_raw_mat_plates(self):
        if(self.rb_single_plate.isChecked()):
            self.No_of_plates=1
            return self.No_of_plates
        elif(self.rb_two_plate.isChecked()):
            self.No_of_plates=2
            return self.No_of_plates
      
    def setUI_for_single_Segment(self):     
        blk_dia=float(self.tb_blktype_BLKDIA.text())
        self.rb_single_plate.setEnabled(False)#Make No of Plate selection Disabled
        self.rb_two_plate.setEnabled(False)#Make No of Plate selection Disabled
        self.grpbox_plt_selc_blktype.setVisible(True)#Enable Plate sizing Groubox
        self.button_calc_opt_plt_len.setEnabled(True)#Enable Calc opt len button        
        self.slider_segment_ratio.setEnabled(False)#Disable slider,as its not reqired
        self.rb_single_plate.setChecked(True)#Check No of plates==1 
        self.cmbbox_avl_raw_mat_plt2_width.setCurrentIndex(0)#"#set Smaller section plate selectin==0
        self.cmbbox_avl_raw_mat_plt2_width.setEnabled(False) #Disable Smaller section plate selectin 
        self.cmbbox_avl_raw_mat_plt1_width.setCurrentIndex(0)#set large section plate selectin==0
        self.cmbbox_avl_raw_mat_plt1_width.setEnabled(False) #Disable large section plate selectin 
       
         
    def setUI_for_two_Segment_one_plate(self):
        self.Hbox_no_of_plates.setEnabled(True)#Make No of Plate selection ENable
        self.grpbox_plt_selc_blktype.setVisible(True)#Enable Plate sizing Groubox
        self.button_calc_opt_plt_len.setEnabled(True)#Enable Calc opt len button        
        self.slider_segment_ratio.setEnabled(True)
        self.rb_single_plate.setChecked(True)#Check No of plates==1 
        self.cmbbox_avl_raw_mat_plt2_width.setCurrentIndex(0)#set Smaller section plate selectin==0
        self.cmbbox_avl_raw_mat_plt2_width.setEnabled(False) #Disable Smaller section plate selectin 
        self.cmbbox_avl_raw_mat_plt1_width.setCurrentIndex(0)#set large section plate selectin==0
        self.cmbbox_avl_raw_mat_plt1_width.setEnabled(False) #Disable large section plate selectin
  
                  
    def setUI_for_two_Segment_two_plates(self):
        self.Hbox_no_of_plates.setEnabled(True)#Make No of Plate selection ENable
        self.grpbox_plt_selc_blktype.setVisible(True)#Enable Plate sizing Groubox
        self.button_calc_opt_plt_len.setEnabled(True)#Enable Calc opt len button        
        self.slider_segment_ratio.setEnabled(True)
        self.rb_two_plate.setChecked(True)#Check No of plates==1 
        self.cmbbox_avl_raw_mat_plt2_width.setCurrentIndex(0)#set Smaller section plate selectin==0
        self.cmbbox_avl_raw_mat_plt2_width.setEnabled(False) #Disable Smaller section plate selectin 
        self.cmbbox_avl_raw_mat_plt1_width.setCurrentIndex(0)#set large section plate selectin==0
        self.cmbbox_avl_raw_mat_plt1_width.setEnabled(False) #Disable large section plate selectin
   
     #Function is executed when No_of_segment==1   
    def Calc_for_single_Segment(self):
        slider_value=self.slider_segment_ratio.value()
        suitable_raw_mat_plt_size,req_plt_len=self.Calc_suitable_raw_mat_plate_width_and_length(slider_value,No_of_Segments=1,No_of_Plates=1)
        index = self.cmbbox_avl_raw_mat_plt1_width.findText(str(suitable_raw_mat_plt_size))                 
        self.cmbbox_avl_raw_mat_plt1_width.setCurrentIndex(index)#Set suitable size as currentText of cmbbox1
        self.tb_optimum_plt1_len.setText(str(req_plt_len))
        self.tb_optimum_plt2_len.setText("0")
        result=self.check_raw_mat_len_contraint()
        if(result):
            self.set_Output_Value()
            self.btn_add_to_BOM.setEnabled(True)            
     
      #Function is executed when No_of_segment==2 and No_of_row_mat_plates==1                      
    def Calc_for_two_Segment_one_plate(self):
        slider_value=self.slider_segment_ratio.value()
        suitable_raw_mat_plt_size,req_plt_len=self.Calc_suitable_raw_mat_plate_width_and_length(slider_value,No_of_Segments=2,No_of_Plates=1)
        index = self.cmbbox_avl_raw_mat_plt1_width.findText(str(suitable_raw_mat_plt_size))             
        self.cmbbox_avl_raw_mat_plt1_width.setCurrentIndex(index)#Set suitable size as currentText of cmbbox1
        self.tb_optimum_plt1_len.setText(str(req_plt_len))
        self.tb_optimum_plt2_len.setText("0")
        result=self.check_raw_mat_len_contraint()
        if(result):
            self.set_Output_Value()
            self.btn_add_to_BOM.setEnabled(True) 
                        
    #Function is executed when No_of_segment==2 and No_of_row_mat_plates==2   
    def Calc_for_two_Segment_two_plates(self): 
        slider_value=self.slider_segment_ratio.value()       
        suitable_raw_mat_large_plt_size,suitable_raw_mat_small_plt_size,req_large_plt_len,req_small_plt_len=self.Calc_suitable_raw_mat_plate_width_and_length(slider_value,No_of_Segments=2,No_of_Plates=2)
        index1 = self.cmbbox_avl_raw_mat_plt1_width.findText(str(suitable_raw_mat_large_plt_size)) 
        index2 = self.cmbbox_avl_raw_mat_plt2_width.findText(str(suitable_raw_mat_small_plt_size))  
        self.cmbbox_avl_raw_mat_plt1_width.setCurrentIndex(index1)#Set suitable size as currentText of cmbbox1    
        self.cmbbox_avl_raw_mat_plt2_width.setCurrentIndex(index2)#Set suitable size as currentText of cmbbox1 
        self.tb_optimum_plt1_len.setText(str(req_large_plt_len)) 
        self.tb_optimum_plt2_len.setText(str(req_small_plt_len))
        result=self.check_raw_mat_len_contraint()
        if(result):
            self.set_Output_Value()
            self.btn_add_to_BOM.setEnabled(True)     
    
    
    #This Function Calculates the Raw Mat Plate width which can accomodate Segment/Segments and Also Raw mat Optimium len 
    #Raw Mat Width,Length
    def Calc_suitable_raw_mat_plate_width_and_length(self,slider_value,No_of_Segments,No_of_Plates):
        #blank_dia=float(self.tb_blktype_BLKDIA.text())
        blank_dia=float(self.tb_blktype_BLKDIA.text())
        plt_side_boundary_margin=0 #mm
        
        if(No_of_Segments==1 and No_of_Plates==1):
            req_plt_len=blank_dia+2*plt_side_boundary_margin
            avl_raw_mat_plate_width=self.get_Avl_raw_mat_plt_size(req_plt_len)#Get plate which has width justlarger than required width
            return avl_raw_mat_plate_width,req_plt_len
        
        elif(No_of_Segments==2 and No_of_Plates==2):#For this ,we need both Large section plate and small section ,separate plates
            slider_value=slider_value
            large_segment_width,small_segment_width=self.Large_segment_width,self.Small_segment_width#self.Calc_segment_width(slider_value)
            
            avl_raw_mat_large_plate_width=self.get_Avl_raw_mat_plt_size(large_segment_width)#Get plate which has width just wider than required width
            avl_raw_mat_small_plate_width=self.get_Avl_raw_mat_plt_size(small_segment_width)#Get plate which has width just wider than required width
            #Calculate Plate Len of these two segments
            #For Larger Segment
            req_large_plt_len=blank_dia+2*plt_side_boundary_margin
            #For smaller segment
            h1=large_segment_width-blank_dia/2
            l2=math.sqrt((blank_dia/2)**2-h1**2)
            Ls=2*l2+2*plt_side_boundary_margin            
            req_small_plt_len=round(Ls,2)
            
            return avl_raw_mat_large_plate_width,avl_raw_mat_small_plate_width,req_large_plt_len,req_small_plt_len
        
        elif(No_of_Segments==2 and No_of_Plates==1):#For this ,we need both Large section plate and small section ,cut from same raw mat plate
            slider_value=slider_value
            large_segment_width,small_segment_width=self.Large_segment_width,self.Small_segment_width#self.Calc_segment_width(slider_value)            
            #Temp Calc
            #Replace with your calc
            avl_raw_mat_plate_width=self.get_Avl_raw_mat_plt_size(large_segment_width)#Get avl plate width can just accomodate large section width
            blk_dia=float(self.tb_blktype_BLKDIA.text())
            
            #m1
            bottom_margin_of_large_section= 0
            #m2
            top_margin_of_large_section= avl_raw_mat_plate_width-large_segment_width
            #m3
            bottom_margin_of_small_section=0
            #g
            gap_between_two_section=50
            #Thetha(in radian)
            thetha=math.asin((avl_raw_mat_plate_width-top_margin_of_large_section-bottom_margin_of_small_section)/(blk_dia+gap_between_two_section))
            #m4==m5
            plt_side_boundary_margin=0
            #h1
            large_segment_flt_face_dist_frm_cntr=avl_raw_mat_plate_width-bottom_margin_of_small_section-top_margin_of_large_section-blk_dia/2
            req_plt_len=round(2*plt_side_boundary_margin+blank_dia/2+(blk_dia+gap_between_two_section)*math.cos(thetha)+math.sqrt((blk_dia/2)**2-large_segment_flt_face_dist_frm_cntr**2),2)
                        
            #end
            
            return avl_raw_mat_plate_width,req_plt_len
         
    
    def get_Avl_raw_mat_plt_size(self,req_plt_len):
        for index,plt_width in enumerate(self.avl_plate_width):
            if(float(plt_width)>=req_plt_len):
                return int(self.avl_plate_width[index])
            
     #As per Slider Value update Label Value         
    def sliderValueChanged(self):
        slider_value = self.slider_segment_ratio.value()       
        self.lbl_large_segment_ratio.setText(f"Large Segment Ratio (in %) : <b>{str(slider_value)}</b>")
        self.Large_segment_width,self.Small_segment_width=self.Calc_segment_width(slider_value)#Recalcuate Segment Width
        self.lbl_large_segment_width.setText(f"Large Segment width(mm): <b>{self.Large_segment_width}</b>") 
        self.lbl_small_segment_width.setText(f"Small Segment width(mm): <b>{self.Small_segment_width}</b>") 
        
        #print(f'Slider Value: {slider_value}')
     
    #As per Slider value calculate new segment width      
    def Calc_segment_width(self,segment_ratio):
        blk_dia=float(self.tb_blktype_BLKDIA.text())        
        small_segment_width=round(blk_dia*(100-segment_ratio)/100)
        large_segment_width=round(blk_dia-small_segment_width,2)
        
        if small_segment_width==0 :
            self.No_of_Segments=1
        else:
            self.No_of_Segments=2    
        return large_segment_width,small_segment_width
                
    def radio_button_changed(self):
        if(self.rb_single_plate.isChecked()):
            self.cmbbox_avl_raw_mat_plt2_width.setCurrentIndex(0)
            self.tb_optimum_plt2_len.setText("0")   
    
    #Check IF Optimum Length is a valid length or not
    def check_raw_mat_len_contraint(self):
        optimum_plt1_len=float(self.tb_optimum_plt1_len.text())
        optimum_plt2_len=float(self.tb_optimum_plt2_len.text())
        plt_thk=float(self.tb_blktype_thk.text())
        if(plt_thk>=70):
            if(optimum_plt1_len>6300 or optimum_plt2_len>6300):
                common_functionality.Show_MessageBox(self,f"For Plate Thk {plt_thk} mm Plate Length Cant be More than 6300")
                self.set_optimum_len_tb_color_red()
            else:
                 self.set_optimum_len_tb_color_green()
                 return True    
        elif(plt_thk>56 and plt_thk<=70):
            if(optimum_plt1_len>8000 or optimum_plt2_len>8000):
                common_functionality.Show_MessageBox(self,f"For Plate Thk {plt_thk} mm Plate Length Cant be More than 8000")
                self.set_optimum_len_tb_color_red()
            else:
                 self.set_optimum_len_tb_color_green()
                 return True      
        elif(plt_thk>36 and plt_thk<=56):
            if(optimum_plt1_len>10000 or optimum_plt2_len>10000):
                common_functionality.Show_MessageBox(self,f"For Plate Thk {plt_thk} mm Plate Length Cant be More than 10000")                
                self.set_optimum_len_tb_color_red() 
            else:
                 self.set_optimum_len_tb_color_green()
                 return True                     
        elif(plt_thk<=36):
            if(optimum_plt1_len>13000 or optimum_plt2_len>13000):
                common_functionality.Show_MessageBox(self,f"For Plate Thk {plt_thk} mm Plate Length Cant be More than 13000")                
                self.set_optimum_len_tb_color_red()
            else:
                 self.set_optimum_len_tb_color_green()
                 return True          
     
     
     #Calculate & Set Output Values(weight,Surface AREA)
    def set_Output_Value(self):
        blk_wt=round(math.pi/4 * (float(self.tb_blktype_BLKDIA.text()))**2  * float(self.tb_blktype_thk.text())  * float(self.tb_blktype_mat_density.text()) * 0.000001,2)        
        self.tb_blktype_Wt.setText(str(blk_wt))
        
        surface_are= round(math.pi/4 * (float(self.tb_blktype_BLKDIA.text()))**2 * 0.000001,2)
        self.tb_blktype_Surface_area.setText(str(surface_are))
        
        self.tb_blktype_Raw_mat_plt1_size.setText(f"{self.tb_optimum_plt1_len.text()} X {self.cmbbox_avl_raw_mat_plt1_width.currentText()}")
        self.tb_blktype_Raw_mat_plt2_size.setText(f"{self.tb_optimum_plt2_len.text()} X {self.cmbbox_avl_raw_mat_plt2_width.currentText()}")
    
    def Add_to_BOM(self):
       
        item_name= self.Item_Name       
        try:
           #If it exists Value gets updated ,otherwise new Key and value is inserted.
            var.Estimation_Schema['Wt']=self.tb_blktype_Wt.text()
            var.Estimation_Schema['Material']=self.cmbbox_blktype_DEnd_Material.currentText()
            var.Estimation_Dict[item_name]=var.Estimation_Schema
            self.change_button_color_green(self.btn_add_to_BOM)                          
            print(var.Estimation_Dict)
              #Insert/Update Database
            _ProjectController=ProjectController()     
            _ProjectController.add_or_update_material(item='dish end',item_name=item_name,wt=self.tb_blktype_Wt.text(),material=self.cmbbox_blktype_DEnd_Material.currentText())
            _ProjectController.add_or_update_surface_area(item='dish end',item_name=item_name,surface_area=self.tb_blktype_Surface_area.text())   
        except Exception as e:
            raise e
        # end try
          
                        
    def set_optimum_len_tb_color_red(self):
        self.tb_optimum_plt1_len.setStyleSheet('background-color:red')
        self.tb_optimum_plt2_len.setStyleSheet('background-color:red')
                    
    def set_optimum_len_tb_color_green(self):
        self.tb_optimum_plt1_len.setStyleSheet('background-color:lightgreen')
        self.tb_optimum_plt2_len.setStyleSheet('background-color:lightgreen')
                    
    def change_button_color_green(self,button):
        button.setStyleSheet("background-color: green; color: white;") 
        
    def reset_button_color_default(self,button):
        #button = self.sender()
        button.setStyleSheet("")      
        
                                  
class DEND_crwn_petal_type(QWidget):#Variant=CROWN & PETAL TYPE
    def __init__(self,location):
        super().__init__()
        self.D_End_shape:str="" #tori/ellip/spherical
        self.D_End_location=location
        self.Item_Name="dish_end_" + self.D_End_location
        self.InitializeUI() 
        
    def InitializeUI(self):
        self.setUp_Ip_grpbox_UI()
        self.setUp_UI_grpbox_refrence_images()
        self.setUp_UI_grpbox_add_BOM()
        self.setUp_UI_layout()
    
    def setUp_Ip_grpbox_UI(self):
        self.Material_list=var.master_mat_list
        self.lbl_Material =QLabel("Material")
        self.cmbbox_shell_DEnd_Material=QComboBox()
        self.cmbbox_shell_DEnd_Material.addItems(self.Material_list)
        self.lbl_ID = QLabel("ID")
        self.tb_ID = QLineEdit("")
        self.tb_ID.setPlaceholderText("INSIDE DIA OF DISHED END(mm)")
        self.lbl_ICR = QLabel("ICR")
        self.tb_ICR = QLineEdit("")
        self.tb_ICR.setPlaceholderText("INSIDE KNUCKLE RADIUS(mm)")
        self.lbl_IKR = QLabel("IKR")
        self.tb_IKR = QLineEdit("")
        self.tb_IKR.setPlaceholderText("INSIDE KNUCKLE RADIUS (mm)")
        self.lbl_SF = QLabel("SF")
        self.tb_SF = QLineEdit("")
        self.tb_SF.setPlaceholderText("STRAIGHT FLANGE OF DISHED END(mm)")
        self.lbl_t = QLabel("T(thk)")
        self.tb_t = QLineEdit("")
        self.tb_t.setPlaceholderText("THICKNESS OF PETAL(mm)")
        self.lbl_N = QLabel("N (NUMBER OF PETALS)")
        self.tb_N = QLineEdit("")
        self.tb_N.setPlaceholderText("NUMBER OF PETALS")
        self.lbl_CRNDIA_d = QLabel("d (CROWN DIAMETER)")
        self.tb_CRNDIA_d = QLineEdit("")
        self.tb_CRNDIA_d.setPlaceholderText("CROWN DIAMETER(mm)")
        self.lbl_SL = QLabel("SL")
        self.tb_SL = QLineEdit("")
        self.tb_SL.setPlaceholderText("STRAIGHT LENGTH IN THE DEV.PETAL(mm)")
        self.lbl_RATIO = QLabel("Ratio")
        self.tb_RATIO = QLineEdit("")
        self.tb_RATIO.setPlaceholderText("RATIO OF STRAIGHT LENGTH TO TOTAL LENGTH")
        self.lbl_Allwnc=QLabel("ALLOWANCES")
        self.tb_Allwnc=QLineEdit("Mat. Allowances")
        self.tb_Allwnc.setPlaceholderText("Material Allowances")

        self.petel_calculate_button = QPushButton("Run Petal Calculation.")
        self.petel_calculate_button.setMaximumSize(200, 80)
        self.petel_calculate_button.clicked.connect(self.petel_calc_button_pressed)

        


        # add label and textboxes to VBoxLayout
        self.vbox_gb1_layout = QVBoxLayout()
        #self.vbox_gb1_layout.addLayout(self.rb_h_box)
        self.vbox_gb1_layout.addWidget(self.lbl_Material)
        self.vbox_gb1_layout.addWidget(self.cmbbox_shell_DEnd_Material)
        self.vbox_gb1_layout.addWidget(self.lbl_ID)
        self.vbox_gb1_layout.addWidget(self.tb_ID)
        self.vbox_gb1_layout.addWidget(self.lbl_ICR)
        self.vbox_gb1_layout.addWidget(self.tb_ICR)
        self.vbox_gb1_layout.addWidget(self.lbl_IKR)
        self.vbox_gb1_layout.addWidget(self.tb_IKR)
        self.vbox_gb1_layout.addWidget(self.lbl_SF)
        self.vbox_gb1_layout.addWidget(self.tb_SF)
        self.vbox_gb1_layout.addWidget(self.lbl_t)
        self.vbox_gb1_layout.addWidget(self.tb_t)
        self.vbox_gb1_layout.addWidget(self.lbl_N)
        self.vbox_gb1_layout.addWidget(self.tb_N)
        self.vbox_gb1_layout.addWidget(self.lbl_CRNDIA_d)
        self.vbox_gb1_layout.addWidget(self.tb_CRNDIA_d)
        self.vbox_gb1_layout.addWidget(self.lbl_SL)
        self.vbox_gb1_layout.addWidget(self.tb_SL)
        self.vbox_gb1_layout.addWidget(self.lbl_RATIO)
        self.vbox_gb1_layout.addWidget(self.tb_RATIO)
        self.vbox_gb1_layout.addWidget(self.lbl_Allwnc)
        self.vbox_gb1_layout.addWidget(self.tb_Allwnc)
       
        self.vbox_gb1_layout.addWidget(self.petel_calculate_button, 0, Qt.AlignmentFlag.AlignHCenter)

        # Create GroupBox and set its layout to existing VBoxLayout
        self.grp_box1 = QGroupBox("Input")
        self.grp_box1.setLayout(self.vbox_gb1_layout)   
        
        # Default Input Values for testing
        self.Set_Default_Input_For_Dish_end_calc() 
    
    def setUp_UI_grpbox_refrence_images(self):
        # Add images to the second group box
        img1_path = absolute_path("Resources\Images\Dish_end1.jpg")
        img2_path = absolute_path("Resources\Images\Dish_end2.jpg")
        image1 = QPixmap(img1_path)
        img_size=300
        image1_resized = self.resize_image(image1, img_size, img_size)
        image2 = QPixmap(img2_path)
        image2_resized = self.resize_image(image2, img_size, img_size)
        label_image1 = QLabel()
        label_image1.setPixmap(image1_resized)
        label_image2 = QLabel()
        label_image2.setPixmap(image2_resized)
        self.Vbox_gb2_layout = QVBoxLayout()

        self.Vbox_gb2_layout.addWidget(label_image1)
        self.Vbox_gb2_layout.addWidget(label_image2)
        self.grp_box2 = QGroupBox("Refrence")
        self.grp_box2.setLayout(self.Vbox_gb2_layout)
    
    def setUp_UI_grpbox_add_BOM(self):
        self.Vbox_layout = QVBoxLayout()
      
        
        #Petal Dimensions
        #Horz Layout to Petal Dimension
        self.H_Box1_gb3_DEND=QHBoxLayout()
        self.lbl_A_with_allwnc=QLabel("A with Allwnc")
        self.tb_A_with_allwnc=QLineEdit("XX")
        self.tb_A_with_allwnc.setEnabled(False)
        self.lbl_B_with_allwnc=QLabel("B with Allwnc")
        self.tb_B_with_allwnc=QLineEdit("XX")
        self.tb_B_with_allwnc.setEnabled(False)
        self.lbl_SL_with_allwnc=QLabel("SL with Allwnc")
        self.tb_SL_with_allwnc=QLineEdit("XX")
        self.tb_SL_with_allwnc.setEnabled(False)
        self.lbl_TL_with_allwnc=QLabel("TL with Allwnc")
        self.tb_TL_with_allwnc=QLineEdit("XX")
        self.tb_TL_with_allwnc.setEnabled(False)
        self.H_Box1_gb3_DEND.addWidget(self.lbl_A_with_allwnc)
        self.H_Box1_gb3_DEND.addWidget(self.tb_A_with_allwnc)
        self.H_Box1_gb3_DEND.addWidget(self.lbl_B_with_allwnc)
        self.H_Box1_gb3_DEND.addWidget(self.tb_B_with_allwnc)
        self.H_Box1_gb3_DEND.addWidget(self.lbl_SL_with_allwnc)
        self.H_Box1_gb3_DEND.addWidget(self.tb_SL_with_allwnc)       
        self.H_Box1_gb3_DEND.addWidget(self.lbl_TL_with_allwnc)
        self.H_Box1_gb3_DEND.addWidget(self.tb_TL_with_allwnc)

        
         #Horz Layout to dispaly weight & No of Petals
        self.H_Box2_gb3_DEND=QHBoxLayout()
        self.tb_No_of_petel=QLineEdit("XX")
        self.tb_No_of_petel.setEnabled(False)
        self.H_Box2_gb3_DEND.addWidget(QLabel("No of Petels"))
        self.H_Box2_gb3_DEND.addWidget(self.tb_No_of_petel)
        self.H_Box2_gb3_DEND.addWidget(QLabel("Wt per Petal"))
        self.tb_wt_per_petel=QLineEdit("XXXX")
        self.tb_wt_per_petel.setEnabled(False)
        self.H_Box2_gb3_DEND.addWidget(self.tb_wt_per_petel)
        self.H_Box2_gb3_DEND.addWidget(QLabel("Material"))
        self.tb_D_end_material=QLineEdit("XXXX")
        self.H_Box2_gb3_DEND.addWidget(self.tb_D_end_material)
        self.tb_D_end_material.setEnabled(False)
        self.H_Box2_gb3_DEND.addWidget(QLabel("Surface Area"))
        self.tb_D_end_Surface_Area=QLineEdit("XXXX")
        self.H_Box2_gb3_DEND.addWidget(self.tb_D_end_Surface_Area)
        self.tb_D_end_Surface_Area.setEnabled(False)
        
        #Avilable Raw Mat Plate COmbobox(
        self.H_Box3_gb3_DEND=QHBoxLayout()
        self.lbl_avl_raw_mat_plt_width=QLabel("Selcet Available Plate Width(>=TL)")
        self.cmbbox_avl_raw_mat_plt_width=QComboBox()
        self.cmbbox_avl_raw_mat_plt_width.setFixedSize(100, 20)
        self.avl_plate_width=var.avl_plate_width_for_DEND
        self.avl_plate_width.insert(0,'0')#Insert '0" in begining of the
        self.cmbbox_avl_raw_mat_plt_width.addItems(self.avl_plate_width)
        
        #Button to calculate Raw mat plate length
        self.btn_calc_raw_mat_plt_length = QPushButton("Calc Plt Len")
        self.btn_calc_raw_mat_plt_length.setFixedWidth(150)
        self.btn_calc_raw_mat_plt_length.clicked.connect(self.btn_calc_raw_mat_plt_len_clicked)
        
        #text box to dispaly min length required
        self.lbl_min_raw_mat_plt_req_len=QLabel(f"Plate Legth Required to cut all Petels")
        self.tb_min_raw_mat_plt_req_len=QLineEdit("00")
        self.tb_min_raw_mat_plt_req_len.setEnabled(False)
        
        
        self.H_Box3_gb3_DEND.addWidget(self.lbl_avl_raw_mat_plt_width)
        self.H_Box3_gb3_DEND.addWidget(self.cmbbox_avl_raw_mat_plt_width)
        self.H_Box3_gb3_DEND.addWidget(self.btn_calc_raw_mat_plt_length)
        self.H_Box3_gb3_DEND.addWidget(self.lbl_min_raw_mat_plt_req_len)
        self.H_Box3_gb3_DEND.addWidget(self.tb_min_raw_mat_plt_req_len)
        
        

        self.btn_add_material = QPushButton("Add Material to BOM")
        self.btn_add_material.clicked.connect(self.add_material)
        #self.H_Box1_gb3_DEND.addWidget(self.btn_add_material)




        #self.dish_end_calc_btn = QPushButton("Save to file")
       
        
        self.Vbox_layout.addLayout(self.H_Box1_gb3_DEND)
        self.Vbox_layout.addLayout(self.H_Box2_gb3_DEND)
        self.Vbox_layout.addLayout(self.H_Box3_gb3_DEND)
       
        self.Vbox_layout.addWidget(self.btn_add_material,0,Qt.AlignmentFlag.AlignHCenter)

        self.grp_box3 = QGroupBox("Petal Dimensions & BOM selection")
        self.grp_box3.setLayout(self.Vbox_layout)
 
    def setUp_UI_layout(self):
        self.Hboxlayout_gb1_gb2=QHBoxLayout()
        self.Hboxlayout_gb1_gb2.addWidget(self.grp_box1)
        self.Hboxlayout_gb1_gb2.addWidget(self.grp_box2)
        self.Vbox_layout_gb1_gb2_gb3=QVBoxLayout()
        self.Vbox_layout_gb1_gb2_gb3.addLayout(self.Hboxlayout_gb1_gb2)
        self.Vbox_layout_gb1_gb2_gb3.addWidget(self.grp_box3)        
        self.setLayout(self.Vbox_layout_gb1_gb2_gb3)
        #self.setStyleSheet('background-color:#e5fff2;font:bold')
        
        if (self.D_End_location=="Top"):
            self.setStyleSheet(common_functionality.DishEnd_style_1)
        else:    
            self.setStyleSheet(common_functionality.DishEnd_style_2)
        #self.setStyleSheet(common_functionality.DishEnd_style_2)
       
        
      
    def Set_D_end_type(self):
        # if self.rb1.isChecked():
        #     #print("rb1_selecetd")
        #     self.dentype=1

        # elif self.rb2.isChecked():
        #     #print("rb2_selected")
        #     self.dentype = 2
        print(self.D_End_shape)
        if(str.upper(self.D_End_shape)=='TORI SPHERICAL'):
            self.dentype=1
        elif (str.upper(self.D_End_shape)=='ELLIPSOIDAL'):
            self.dentype=2    
        
    
    def Set_Default_Input_For_Dish_end_calc(self):
        self.Set_D_end_type()
        self.tb_ID.setText("9300")
        self.tb_ICR.setText("8370")
        self.tb_IKR.setText("1581")
        self.tb_SF.setText("50")
        self.tb_t.setText("40")
        self.tb_N.setText("24")
        self.tb_CRNDIA_d.setText("2500")
        self.tb_SL.setText("0")
        self.tb_RATIO.setText("0.25")
        self.tb_Allwnc.setText("40")   
    
    def petel_calc_button_pressed(self):
        self.Set_D_end_type()
        if(bool(re.match('[a-zA-Z\s]+$', self.D_End_shape))):#D_End_shape string has only Alphabets not "-----"   
            #print("button working")
            from Calculation.DEnd_Petal_Calc import DishEndCalc
            self.input_dict = {
                "Material":self.cmbbox_shell_DEnd_Material.currentText(),
                "dentype": self.dentype,
                "ID": float(self.tb_ID.text()),
                "ICR": float(self.tb_ICR.text()),
                "IKR": float(self.tb_IKR.text()),
                "SF": float(self.tb_SF.text()),
                "TK": float(self.tb_t.text()),
                "N": float(self.tb_N.text()),
                "CRNDIA_d": float(self.tb_CRNDIA_d.text()),
                "SL": float(self.tb_SL.text()),
                "RATIO": float(self.tb_RATIO.text()),
                "Allwnc": float(self.tb_Allwnc.text()),
            }
            calc = DishEndCalc(input_dict=self.input_dict)
            self.PETEL_OP_PARMS_WITH_ALLWNC=calc.Toripetal()#Main DEnd Calculation
            print(self.PETEL_OP_PARMS_WITH_ALLWNC)
            
            self.update_grp_box3() #Update DEnd BOM groupbox values

            #Change the Add material color back to default 
            self.reset_button_color_default(self.btn_add_material)
        else:
            message_box = QMessageBox(self)
            message_box.setIcon(QMessageBox.Icon.Information)
            message_box.setText("Pls Select Suitable Dish End type")
            message_box.setWindowTitle("Information")
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            message_box.exec()   
    
    def add_material(self):
        print("add meterial button working")
        try:
            #If it exists Value gets updated ,otherwise new Key and value is inserted.
            item_name=self.Item_Name
            var.Estimation_Schema['item']="dish end"
            var.Estimation_Schema['Wt']=self.tb_wt_per_petel.text()
            var.Estimation_Schema['Material']=self.tb_D_end_material.text()
            var.Estimation_Dict[item_name]=var.Estimation_Schema
            print(var.Estimation_Dict)
            
            #Insert/Update Database   
            add_or_update_material(item='dish end',item_name=item_name,wt=self.tb_wt_per_petel.text(),material=self.tb_D_end_material.text())
            add_or_update_surface_area(item='dish end',item_name=item_name,surface_area=self.tb_D_end_Surface_Area.text())
        except Exception as e:
            raise e    
        
        #button= self.sender()
        self.change_button_color_green()

    def update_grp_box3(self):
        
       self.tb_A_with_allwnc.setText(str(self.PETEL_OP_PARMS_WITH_ALLWNC['A']))
       self.tb_B_with_allwnc.setText(str(self.PETEL_OP_PARMS_WITH_ALLWNC['B']))
       self.tb_SL_with_allwnc.setText(str(self.PETEL_OP_PARMS_WITH_ALLWNC['SL']))
       self.tb_TL_with_allwnc.setText(str(self.PETEL_OP_PARMS_WITH_ALLWNC['TL'])) 
       self.tb_No_of_petel.setText(str(self.PETEL_OP_PARMS_WITH_ALLWNC['N']))   
       self.tb_wt_per_petel.setText(str(self.PETEL_OP_PARMS_WITH_ALLWNC['PETELWT']))
       self.tb_D_end_material.setText(str(self.PETEL_OP_PARMS_WITH_ALLWNC['MATERIAL']))
       self.tb_D_end_Surface_Area.setText(str(self.PETEL_OP_PARMS_WITH_ALLWNC['PETELAREA']))
    
    def btn_calc_raw_mat_plt_len_clicked(self):
        min_plt_width_req_for_Petal=float(self.tb_TL_with_allwnc.text())
        #set the combobox to minimum available plt width which can accomodate a Petal
        self.cmbbox_avl_raw_mat_plt_width.setCurrentText(self.get_Avl_raw_mat_plt_size(min_plt_width_req_for_Petal))
        min_plt_width_avl_for_Petal=int(self.cmbbox_avl_raw_mat_plt_width.currentText())
        
        #Calculate Min Lenght reqired of the plate
        min_plt_len_req_to_cut_all_Petels=self.Calculate_min_raw_mat_plt_len()
        self.tb_min_raw_mat_plt_req_len.setText(str(min_plt_len_req_to_cut_all_Petels))
        
        #Validate Plate Length is Feasible???
        result = self.check_raw_mat_len_contraint()
        
        

    def get_Avl_raw_mat_plt_size(self,min_plt_width_req_for_Petal):
        for index,plt_width in enumerate(self.avl_plate_width):
            if(float(plt_width)>=min_plt_width_req_for_Petal):
                return (self.avl_plate_width[index])
        
    def Calculate_min_raw_mat_plt_len(self):
        N=float(self.tb_No_of_petel.text())
        A= float(self.tb_A_with_allwnc.text())
        B=float(self.tb_B_with_allwnc.text())
        TL=float(self.tb_TL_with_allwnc.text())
        SL=float(self.tb_SL_with_allwnc.text())
        #margin
        m=50
        
        h1=TL-SL
        b0=(A-B)/2
        thetha= math.atan(b0/h1)
        b1=(SL+m/math.sin(thetha))*math.tan(thetha)
        Overlap_len=A-b0-B-b1        
        min_len_req=round(N*A-(N-1)*Overlap_len,2)
        return min_len_req
        
    def check_raw_mat_len_contraint(self):
        raw_mat_plt_thk=float(self.tb_t.text())   
        raw_mat_plt_len=float(self.tb_min_raw_mat_plt_req_len.text())
        if(raw_mat_plt_thk>=70):
            if(raw_mat_plt_len>6300):
                common_functionality.Show_MessageBox(self,f"For Plate Thk {raw_mat_plt_thk} mm Plate Length Cant be More than 6300")
                self.set_tb_min_raw_mat_plt_req_len_color_red()
            else:
                 self.set_tb_min_raw_mat_plt_req_len_color_green()
                 return True    
        elif(raw_mat_plt_thk>56 and raw_mat_plt_thk<=70):
            if(raw_mat_plt_len>8000 ):
                common_functionality.Show_MessageBox(self,f"For Plate Thk {raw_mat_plt_thk} mm Plate Length Cant be More than 8000")
                self.set_tb_min_raw_mat_plt_req_len_color_red()
            else:
                 self.set_tb_min_raw_mat_plt_req_len_color_green()
                 return True      
        elif(raw_mat_plt_thk>36 and raw_mat_plt_thk<=56):
            if(raw_mat_plt_len>10000 ):
                common_functionality.Show_MessageBox(self,f"For Plate Thk {raw_mat_plt_thk} mm Plate Length Cant be More than 10000")                
                self.set_tb_min_raw_mat_plt_req_len_color_red() 
            else:
                 self.set_tb_min_raw_mat_plt_req_len_color_green()
                 return True                     
        elif(raw_mat_plt_thk<=36):
            if(raw_mat_plt_len>13000 ):
                common_functionality.Show_MessageBox(self,f"For Plate Thk {raw_mat_plt_thk} mm Plate Length Cant be More than 13000")                
                self.set_tb_min_raw_mat_plt_req_len_color_red()
            else:
                 self.set_tb_min_raw_mat_plt_req_len_color_green()
                 return True          
     
         
   
    #This function changes the coor of sender button to green
    def change_button_color_green(self):
        button = self.sender()
        button.setStyleSheet("background-color: green; color: white;")

    #This Function reset the color of "button" passed as an argument.
    def reset_button_color_default(self,button):
        #button = self.sender()
        button.setStyleSheet("") 
        
    def set_tb_min_raw_mat_plt_req_len_color_red(self):
        self.tb_min_raw_mat_plt_req_len.setStyleSheet('background-color:red')
        self.tb_min_raw_mat_plt_req_len.setStyleSheet('background-color:red')
                    
    def set_tb_min_raw_mat_plt_req_len_color_green(self):
        self.tb_min_raw_mat_plt_req_len.setStyleSheet('background-color:lightgreen')
        self.tb_min_raw_mat_plt_req_len.setStyleSheet('background-color:lightgreen')       
     
    def resize_image(self,image: QPixmap, width: int, height: int) -> QPixmap:
        return image.scaled(width, height, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
 
class common_functionality():    
    DishEnd_style_1=\
    """
        QGroupBox {
            font: bold;
            font-size:14px;
            padding: 15px;
            border: 1px solid silver;
            border-radius: 6px;
            background-color: #e6e6ff
                                
        }
                    
        """ 
    DishEnd_style_2=\
    """
    QGroupBox {
            font: bold;
            font-size:14px;
            padding: 15px;
            border: 1px solid silver;
            border-radius: 6px;
            background-color:  #e5ffff
                                
        }
    """    
        
    # Change the color of the slider using a stylesheet
    slider_style="""
    QSlider::groove:horizontal {
    background: red;
    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */
    left: 4px; right: 4px;
    }

    QSlider::handle:horizontal {
        height: 10px;
        background: green;
        margin: 0 -4px; /* expand outside the groove */
    }

    QSlider::add-page:horizontal {
        background: white;
    }

    QSlider::sub-page:horizontal {
        background: pink;
    }
    
    """
    
    rb_stylesheet = """
            QRadioButton {
                font-weight: bold; /* Make the text bold */
            }
            QRadioButton::indicator {
                width: 15px; /* Adjust the indicator size as needed */
                height: 15px; /* Adjust the indicator size as needed */
            }
            QRadioButton::indicator::unchecked {
                font-weight: bold; /* Make the text bold */
            }
        """
        
        

          
    def Show_MessageBox(sender,msg:str):
        message_box = QMessageBox(sender)
        message_box.setIcon(QMessageBox.Icon.Information)
        message_box.setText(msg)
        message_box.setWindowTitle("Information")
        message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        message_box.exec()   
                 
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dend = Tab1_DEnd()
#     dend.show()