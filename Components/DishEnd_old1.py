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
from DataBase.DB_config import DB_config_class
from Controller.project import add_or_update_material,add_or_update_surface_area




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
        self.Top_Dish_End=DEND_blk_type()
        self.VBox_all_grp_box_layout.addWidget(self.Top_Dish_End)
        
        self.VBox_all_grp_box_layout.addWidget(self.Bottom_DishEnd_selction)
        self.Bottom_Dish_End=DEND_blk_type()     
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
            self.Top_Dish_End=DEND_blk_type()                      
        else:
            self.Top_Dish_End=DEND_crwn_petal_type()
            
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
            self.Bottom_Dish_End=DEND_blk_type()            
        else:
            self.Bottom_Dish_End=DEND_crwn_petal_type()
           
        #Remove the Bottom end Dish and i.e. groupbox at location(3) and replace it with new widget(Dishend-BLANL or Crown/petal) as per user selection      
        self.VBox_all_grp_box_layout.removeWidget(self.VBox_all_grp_box_layout.itemAt(3).widget())
        self.VBox_all_grp_box_layout.insertWidget(3,self.Bottom_Dish_End)
        self.set_Shape_for_Bottom_DEND()
        #dend_shape= self.Bottom_DishEnd_var_selction.cmbbox_d_end_shape_type.currentText()    
        #self.set_Shape_for_Top_DEND(location='BOTTOM',shape=dend_shape)
        #self.Bottom_DishEnd_var_selction.cmbbox_d_end_shape_type.currentIndexChanged.connect(self.set_Shape_for_Top_DEND(location='BOTTOM',shape=dend_shape))    
        
  
    def set_Shape_for_Top_DEND(self):
        self.Top_Dish_End.D_End_shape= self.Top_DishEnd_selction.cmbbox_d_end_shape_sel.currentText()
        # dend_loaction=location
        # dend_shape=shape
        # if(str.upper(dend_loaction)=='TOP'):
        #     self.Top_Dish_End.D_End_shape=dend_shape # Pass DEnd shape(tori,ellipsoidal,hemi) to Top Dish ENd
        # elif(str.upper(dend_loaction)=='BOTTOM'):
        #     self.Bottom_Dish_End.D_End_shape=dend_shape # Pass DEnd shape(tori,ellipsoidal,hemi) to Bottom Dish ENd
        
    def set_Shape_for_Bottom_DEND(self):
        self.Bottom_Dish_End.D_End_shape= self.Bottom_DishEnd_selction.cmbbox_d_end_shape_sel.currentText()    

class DEnd_selction(QWidget):#DISH END SELECTION GROUPBOX UI
    def __init__(self,location):
        super().__init__()
        self.location=location+ " Dish End" # location=Top or Bottom
        self.InitializeUI() 
        
    def InitializeUI(self):
        self.setUp_UI_dish_end_selection() 
        
           
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
        self.grpbbox_dishend_var_sel=QGroupBox(self.location)
        self.grpbbox_dishend_var_sel.setLayout(self.dishEnd_sel_gridlayout)
        self.Vbox_dishend_var_sel=QVBoxLayout()
        self.Vbox_dishend_var_sel.addWidget(self.grpbbox_dishend_var_sel)
        
        self.setLayout(self.Vbox_dishend_var_sel)
        self.setStyleSheet(common_functionality.grpbox_style)
      
    
class DEND_blk_type(QWidget): #Variant=BLANK TYPE
    def __init__(self):
        super().__init__()
        self.D_End_shape:str="" #Tori/ellip/sherical
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
        self.main_grpbox_blktype.setStyleSheet(common_functionality.grpbox_style)
        self.main_grpbox_blktype.setLayout(self.gridlayout_blktype)
       
        
    def SetUP_UI_Plt_Sizing_Calc(self):
        
         #Plate Sizing Calc
        self.No_of_plates=0    
        self.lbl_No_of_Plates_required_for_blank=QLabel(f"<b>No of Plates required for Blank Cutting</b>")
        self.rb_single_plate=QRadioButton("1")             
        self.rb_two_plate=QRadioButton("2")
        self.rb_single_plate.setStyleSheet(common_functionality.rb_stylesheet)
        self.rb_two_plate.setStyleSheet(common_functionality.rb_stylesheet)
        self.rb_single_plate.clicked.connect(self.plate_sizing_for_single_plate)
        self.rb_two_plate.clicked.connect(self.plate_sizing_for_two_plate)
        
        #default_slider_value=67
        #large_segment_width,small_segment_width=self.Calc_segment_width(default_slider_value)        
        self.lbl_large_segment_ratio=QLabel(f"Large Segment Ratio (in %): <b>{str('XXX')}</b>")
        
        
        # Create a slider
        self.slider_segment_ratio = QSlider(self)
        self.slider_segment_ratio.setStyleSheet(common_functionality.slider_style)
        # Change the background color of the slider        
        self.slider_segment_ratio.setOrientation(Qt.Orientation.Horizontal)  # Set the orientation to Horizontal
        self.slider_segment_ratio.setMinimum(50)
        self.slider_segment_ratio.setMaximum(100)
        #self.slider_segment_ratio.setValue(default_slider_value)#default value       
        #self.slider_segment_ratio.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_segment_ratio.setTickInterval(1)               
        self.slider_segment_ratio.valueChanged.connect(self.sliderValueChanged)
        self.lbl_large_segment_width=QLabel(f"Large Segment width: <b>{str('XXX')}</b>") 
        self.lbl_small_segment_width=QLabel(f"Small Segment width: <b>{str('XXX')}</b>") 
        
        self.lbl_avl_raw_mat_plt1_width=QLabel("Selcet Available Plate Width(Larger-Section)")
        self.cmbbox_avl_raw_mat_plt1_width=QComboBox()
        self.cmbbox_avl_raw_mat_plt1_width.setFixedSize(100, 20)
        self.avl_plate_width=list(map(str,[x for x in range(2500,13500,500)]))
        self.avl_plate_width.insert(0,'0')#Insert '0" in begining of the
        self.cmbbox_avl_raw_mat_plt1_width.addItems(self.avl_plate_width)
        self.lbl_avl_raw_mat_plt2_width=QLabel("Selcet Available Plate Width(Smaller-Section)")
        self.cmbbox_avl_raw_mat_plt2_width=QComboBox()
        self.cmbbox_avl_raw_mat_plt2_width.setFixedSize(100, 20)
        
        self.cmbbox_avl_raw_mat_plt2_width.addItems(self.avl_plate_width)
        
        self.lbl_optimum_plt_len=QLabel("Optimum Plate Length")
        self.tb_optimum_plt_len = QLineEdit("0.00")
        self.tb_optimum_plt_len.setEnabled(False) 
        self.button_calc_opt_plt_len = QPushButton("Optimize Plate length")
        
        self.button_calc_opt_plt_len.setFixedSize(150, 30)
        self.button_calc_opt_plt_len.setStyleSheet("QPushButton{font-weight: bold;}")
        self.button_calc_opt_plt_len.clicked.connect(self.calc_opt_plt_len)
        # self.lbl_blktype_Wt=QLabel("Weight")
        # self.tb_blktype_Wt = QLineEdit("0.00")  
        
      
        #Putting items on layout2 
        #Plate Sizing GroupBox2
        self.grpbox_plt_selc_blktype=QGroupBox("Plate Sizing")
        self.grpbox_plt_selc_blktype.setStyleSheet(common_functionality.grpbox_style)
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
        self.gridlayout_plt_selc_blktype.addWidget(self.lbl_optimum_plt_len,3,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.gridlayout_plt_selc_blktype.addWidget(self.tb_optimum_plt_len,3,1)
        self.gridlayout_plt_selc_blktype.addWidget(self.button_calc_opt_plt_len,3,2)
       
        self.grpbox_plt_selc_blktype.setLayout(self.gridlayout_plt_selc_blktype)
        
    
    def setup_Main_layout(self):
        self.Vbox_main_blktype=QVBoxLayout()
        self.Vbox_main_blktype.addWidget(self.main_grpbox_blktype)
        self.Vbox_main_blktype.addWidget(self.grpbox_plt_selc_blktype)
        self.setLayout(self.Vbox_main_blktype)
     
    def set_defaults(self):
        self.grpbox_plt_selc_blktype.setVisible(False)#Bydefault Groupbox is disabled
        self.cmbbox_avl_raw_mat_plt2_width.setEnabled(False)
        self.button_calc_opt_plt_len.setEnabled(False)       
        #self.rb_single_plate.setChecked(True)#Deafult "No of plates==1"     
    
    def calc_Blkdia(self):
        #print("blkdia pressed")
        blktype_IKR,blktype_ICR=0,0
        #self.cmbbox_d_end_shape_type.currentText()
        #print(self.D_End_shape)
        if(bool(re.match('[a-zA-Z\s]+$', self.D_End_shape))):#D_End_shape selection string has only Alphabets not "-----"
            if(str.upper(self.D_End_shape)=='TORI SPHERICAL'):
                blktype_IKR =float(self.tb_blktype_ID.text())*0.15
                blktype_ICR=float(self.tb_blktype_ID.text())*0.8
            elif (str.upper(self.D_End_shape)=='ELLIPSOIDAL'):
                blktype_IKR =float(self.tb_blktype_ID.text())*0.1727 
                blktype_ICR=float(self.tb_blktype_ID.text())*0.9045
            
            blktype_BLKDIA=(float(self.tb_blktype_ID.text())+2*float(self.tb_blktype_thk.text()))+((float(self.tb_blktype_ID.text())+2*float(self.tb_blktype_thk.text()))/24)+2/3*blktype_IKR+2*float(self.tb_blktype_stface_len.text())+float(self.tb_blktype_thk.text())
            blktype_BLKDIA=round(blktype_BLKDIA, 2)
            self.tb_blktype_IKR.setText(str(blktype_IKR))
            self.tb_blktype_IKR.setEnabled(False)  
            self.tb_blktype_ICR.setText(str(blktype_ICR)) 
            self.tb_blktype_ICR.setEnabled(False) 
            self.tb_blktype_BLKDIA.setText(str(blktype_BLKDIA) )
            self.tb_blktype_BLKDIA.setEnabled(False) 
            
            #Based on BLKDIA ,Set Visibality of Plate Sizing GroupBox
            self.setUI_visible_for_plate_sizing()
            
            
       
                
        else:
            common_functionality.Show_MessageBox(self,"Pls Select Suitable Dish End type")
            
    
    def setUI_visible_for_plate_sizing(self):
        self.grpbox_plt_selc_blktype.setVisible(True)
        blk_dia=float(self.tb_blktype_BLKDIA.text())
        
        # if(blk_dia<=2500):
        # if(self.rb_single_plate.isChecked()):
        #     self.No_of_plates=1
        # else:
        #     self.No_of_plates=2
               
        
        
        if (blk_dia<=2500 ):
            self.No_of_plates=1
            self.SetUI_for_single_plate()
            self.UpdateUI_for_Single_plate()
            
        if(blk_dia>=2500):
            self.No_of_plates=2
            self.SetUI_for_two_plate()
            self.UpdateUI_for_two_plates()
            
                
           
    def SetUI_for_single_plate(self):        
        #self.rb_single_plate.setChecked(True)#Check Radiobutton1
        blk_dia=float(self.tb_blktype_BLKDIA.text())
        self.Hbox_no_of_plates.setEnabled(False)#Make No of Plate selection Disabled
        self.grpbox_plt_selc_blktype.setVisible(True)#Enable Plate sizing Groubox(we will enable only selected widget from it)
        self.button_calc_opt_plt_len.setEnabled(True)#Enable Calc opt len button
        #blk_dia<=2500mm or No_of_plate==1 ,only need one section that is larger section === entire blank==100%
        self.slider_segment_ratio.setEnabled(False)#Disable slider,as its not reqired            
        
        
    def UpdateUI_for_Single_plate(self):
        self.slider_segment_ratio.setValue(100)#Only Larger section is required no smaller section 
        #self.rb_single_plate.setChecked(True)#Check No of plates==1   
        #self.sliderValueChanged()#Update segment width Label as per 100%-large and 0%-small section value
        self.cmbbox_avl_raw_mat_plt2_width.setCurrentText="0"#set Smaller section plate selectin==0
        self.cmbbox_avl_raw_mat_plt2_width.setEnabled(False) #Disable Smaller section plate selectin
        suitable_raw_mat_plt_size=self.get_suitable_raw_mat_plate_width(100)
        self.cmbbox_avl_raw_mat_plt1_width.setCurrentText(str(suitable_raw_mat_plt_size))#Set suitable size as currentText of cmbbox1
    
    def SetUI_for_two_plate(self):
        self.Hbox_no_of_plates.setEnabled(True)#Make No of Plate selection ENable
        self.grpbox_plt_selc_blktype.setVisible(True)#Enable Plate sizing Groubox
        self.button_calc_opt_plt_len.setEnabled(True)#Enable Calc opt len button        
        self.slider_segment_ratio.setEnabled(True)
                  
    def UpdateUI_for_two_plates(self,slider_value=67):
        blk_dia=float(self.tb_blktype_BLKDIA.text())
        #self.rb_two_plate.setChecked(True)#Check No of plates==2  
        self.slider_segment_ratio.setValue(slider_value)#If not specified slider_value=67
        #self.sliderValueChanged()#Update segment width Label as per slider value
              
        self.cmbbox_avl_raw_mat_plt2_width.setEnabled(True)
        suitable_raw_mat_large_plt_size,suitable_raw_mat_small_plt_size=self.get_suitable_raw_mat_plate_width(slider_value)
        self.cmbbox_avl_raw_mat_plt1_width.setCurrentText(suitable_raw_mat_large_plt_size)#Set suitable size as currentText of cmbbox1    
        self.cmbbox_avl_raw_mat_plt2_width.setCurrentText(suitable_raw_mat_small_plt_size)#Set suitable size as currentText of cmbbox1    
   
    def plate_sizing_for_single_plate(self):
        self.UpdateUI_for_Single_plate()
        
    def plate_sizing_for_two_plate(self):
        self.UpdateUI_for_two_plates(self,self.slider_segment_ratio.value())   
            
    def get_suitable_raw_mat_plate_width(self,slider_value):
        #blank_dia=float(self.tb_blktype_BLKDIA.text())
        blank_dia=float(self.tb_blktype_BLKDIA.text())
        plt_boundary_margin=0 #mm
        if(blank_dia<=2500 or self.No_of_plates==1):#For Both Casees,Only Large section plate is required,no small section
            req_plt_len=blank_dia+2*plt_boundary_margin
            avl_raw_mat_plate_width=self.get_Avl_raw_mat_plt_size(req_plt_len)#Get plate which has width justlarger than required width
            return avl_raw_mat_plate_width
        elif(blank_dia>2500 and self.No_of_plates==2):#For this ,we need both Large section plate and small section ,separate plates
            large_segment_width,small_segment_width=self.Calc_segment_width(slider_value)
            req_large_plt_len=large_segment_width+2*plt_boundary_margin
            req_small_plt_len=small_segment_width+2*plt_boundary_margin
            avl_raw_mat_large_plate_width=self.get_Avl_raw_mat_plt_size(large_segment_width)#Get plate which has width justlarger than required width
            avl_raw_mat_small_plate_width=self.get_Avl_raw_mat_plt_size(small_segment_width)#Get plate which has width justlarger than required width
            return avl_raw_mat_large_plate_width,avl_raw_mat_small_plate_width
            #self.cmbbox_avl_raw_mat_plt1_width.setCurrentText(avl_raw_mat_plate_width)  
              
    def calc_opt_plt_len(self):
        blank_dia=float(self.tb_blktype_BLKDIA.text())
        selc_large_section_plt_width=float(self.cmbbox_avl_raw_mat_plt1_width.currentText())
        selc_small_section_plt_width=float(self.cmbbox_avl_raw_mat_plt2_width.currentText())
        plt_boundary_margin=0 #mm
        req_plt_len=0
        
        #selc_plt_wd_excl_margin=selc_plt_width-2*plt_boundary_margin#(Top margin and bottom margin)
        if(blank_dia<=2500):#Only Large section plate is required,no small section
            req_plt_len=blank_dia+2*plt_boundary_margin
            avl_raw_mat_plate_width=self.get_Avl_raw_mat_plt_size(req_plt_len)#Get plate which has width justlarger than required width
            self.cmbbox_avl_raw_mat_plt1_width.setCurrentText(avl_raw_mat_plate_width)
            
            
        elif(blank_dia>2500):
            pass            
            #Case 1-two different plate
            
            #Check if ,plt width is sufficient enough to accomodate BLANK(either full or in section)
            #Means Plate width exclusding margin should be wider enough to atleast half segment
            #If it cant then plate is not wider enough and no solution exist,select wider plate
            
            # if(selc_plt_wd_excl_margin>=blank_dia/2):

            #     #Check if ,plt width is sufficient enough to accomodate entire BLANK
            #     if(selc_plt_wd_excl_margin>=blank_dia):
            #         req_plt_len=blank_dia+2*plt_boundary_margin
            #         print(f"Required Plate Len = {req_plt_len}")
                    
            #     #Check if ,plt width is sufficient enough to hold two sections    
            #     if(selc_plt_wd_excl_margin>=blank_dia/2):
            #         larger_section_width=round(2/3*blank_dia)
            #         smaller_section_width=round(blank_dia-larger_section_width,2)
                    
                    
                    #print(f"Required Plate Len = {larger_section_width},{smaller_section_width}")
                
            # else:
            #     common_functionality.Show_MessageBox(self,"plate width not sufficiant to accomodate BLANK,select Higher size plate")
            #     print("plate width not sufficiant to accomodate BLANK,select Higher size plate")        
            
        #Case 1-Putting Larger section and adjacent tangent(with some gap) small section
        
        #Check if selcted width can accomodate 02 half i.e. identical section.
    def get_Avl_raw_mat_plt_size(self,req_plt_len):
        for plt_width in self.avl_plate_width:
            if(float(plt_width)>=req_plt_len):
                return plt_width
            
              
    def sliderValueChanged(self):
        slider_value = self.slider_segment_ratio.value()       
        self.lbl_large_segment_ratio.setText(f"Large Segment Ratio (in %) : <b>{str(slider_value)}</b>")
        large_segment_width,small_segment_width=self.Calc_segment_width(slider_value)#Recalcuate Segment Width
        self.lbl_large_segment_width.setText(f"Large Segment width(mm): <b>{large_segment_width}</b>") 
        self.lbl_small_segment_width.setText(f"Small Segment width(mm): <b>{small_segment_width}</b>") 
        
        #print(f'Slider Value: {slider_value}')
          
    def Calc_segment_width(self,segment_ratio):
        blk_dia=float(self.tb_blktype_BLKDIA.text())        
        small_segment_width=round(blk_dia*(100-segment_ratio)/100,2)
        large_segment_width=round(blk_dia-small_segment_width,2)
        return large_segment_width,small_segment_width
                
     
             
class DEND_crwn_petal_type(QWidget):#Variant=CROWN & PETAL TYPE
    def __init__(self):
        super().__init__()
        self.D_End_shape:str="" #tori/ellip/spherical
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
        img_size=500
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
      
        #Horz Layout to dispaly weight & No of Petals
        self.H_Box_gb3_DEND=QHBoxLayout()
        
        self.tb_No_of_petel=QLineEdit("XX")
        self.tb_No_of_petel.setEnabled(False)
        self.H_Box_gb3_DEND.addWidget(QLabel("No of Petels"))
        self.H_Box_gb3_DEND.addWidget(self.tb_No_of_petel)
        self.H_Box_gb3_DEND.addWidget(QLabel("Wt per Petal"))
        self.tb_wt_per_petel=QLineEdit("XXXX")
        self.tb_wt_per_petel.setEnabled(False)
        self.H_Box_gb3_DEND.addWidget(self.tb_wt_per_petel)
        self.H_Box_gb3_DEND.addWidget(QLabel("Material"))
        self.tb_D_end_material=QLineEdit("XXXX")
        self.H_Box_gb3_DEND.addWidget(self.tb_D_end_material)
        self.tb_D_end_material.setEnabled(False)
        self.H_Box_gb3_DEND.addWidget(QLabel("Surface Area"))
        self.tb_D_end_Surface_Area=QLineEdit("XXXX")
        self.H_Box_gb3_DEND.addWidget(self.tb_D_end_Surface_Area)
        self.tb_D_end_Surface_Area.setEnabled(False)

        self.btn_add_material = QPushButton("Add Material to BOM")
        self.btn_add_material.clicked.connect(self.add_material)
        self.H_Box_gb3_DEND.addWidget(self.btn_add_material)




        self.dish_end_calc_btn = QPushButton("Save to file")
       
        
       
        self.Vbox_layout.addLayout(self.H_Box_gb3_DEND)
        #self.Vbox_layout.addWidget(self.btn_add_material)
        self.Vbox_layout.addWidget(self.dish_end_calc_btn)

        self.grp_box3 = QGroupBox("Logic For Petal BOM Material Selection")
        self.grp_box3.setLayout(self.Vbox_layout)
 
    def setUp_UI_layout(self):
        self.Hboxlayout_gb1_gb2=QHBoxLayout()
        self.Hboxlayout_gb1_gb2.addWidget(self.grp_box1)
        self.Hboxlayout_gb1_gb2.addWidget(self.grp_box2)
        self.Vbox_layout_gb1_gb2_gb3=QVBoxLayout()
        self.Vbox_layout_gb1_gb2_gb3.addLayout(self.Hboxlayout_gb1_gb2)
        self.Vbox_layout_gb1_gb2_gb3.addWidget(self.grp_box3)
        self.setLayout(self.Vbox_layout_gb1_gb2_gb3)
        
      
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
        self.tb_Allwnc.setText("100")   
    
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
            self.PETEL_OP_PARMS_WITH_ALLWNC= calc.Toripetal()#Main DEnd Calculation
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
            add_or_update_material(item='dish end',item_name='dish end pv1',wt=self.tb_wt_per_petel.text(),material=self.tb_D_end_material.text())
            add_or_update_surface_area(item='dish end',item_name='dish end pv1',wt=self.tb_wt_per_petel.text(),surface_area=self.tb_D_end_Surface_Area.text())
        except:
            pass    
        
        #button= self.sender()
        self.change_button_color_green()

    def update_grp_box3(self):
       self.tb_No_of_petel.setText(str(var.DEND_Crn_Petal_type_Params_incld_allwnc['N']))   
       self.tb_wt_per_petel.setText(str(var.DEND_Crn_Petal_type_Params_incld_allwnc['PETLWT1']))
       self.tb_D_end_material.setText(str(var.DEND_Crn_Petal_type_Params_incld_allwnc['PETEL_MATERIAL']))
       self.tb_D_end_Surface_Area.setText(var.DEND_Crn_Petal_type_Params_incld_allwnc['SURFACE_AREA'])
    

    def add_material(self):
        print("add meterial button working")
        try:
            add_or_update_material(item='dish end',item_name='dish end pv1',wt=self.tb_wt_per_petel.text(),material=self.tb_D_end_material.text())
            add_or_update_surface_area(item='dish end',item_name='dish end pv1',wt=self.tb_wt_per_petel.text(),surface_area=self.tb_D_end_Surface_Area.text())
        except:
            pass    
        
        #button= self.sender()
        self.change_button_color_green()

    #This function changes the coor of sender button to green
    def change_button_color_green(self):
        button = self.sender()
        button.setStyleSheet("background-color: green; color: white;")

    #This Function reset the color of "button" passed as an argument.
    def reset_button_color_default(self,button):
        #button = self.sender()
        button.setStyleSheet("")    
     
    def resize_image(self,image: QPixmap, width: int, height: int) -> QPixmap:
        return image.scaled(width, height, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
 
class common_functionality():    
    grpbox_style=\
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