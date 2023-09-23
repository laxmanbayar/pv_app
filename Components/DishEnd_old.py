from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QComboBox, QRadioButton, QPushButton, QVBoxLayout, QWidget, \
    QTabWidget, QGroupBox, QPushButton, QHBoxLayout, QScrollArea, QGridLayout,QSpacerItem,QSizePolicy
from PyQt6.QtCore import Qt
#from Variables.var import Variables
from PyQt6.QtGui import *
from Calculation.abs_path import absolute_path
from Variables import var
import sys
from DataBase.DB_config import DB_config_class
from Controller.project import add_or_update_material,add_or_update_surface_area




class Tab1_DEnd(QWidget):
    dentype=0
    def __init__(self):
        super().__init__()
        
        self.InitializeUI()

    def InitializeUI(self):
        # Label and Input for  Petel Calculation for dish End#

        
        self.setUp_UI_dish_end_variant_selection()
        self.setUp_UI_blank_type_DEND()
        self.setUp_UI_Dend_crn_petal_ip()
        self.setUp_UI_refrence_images()
        self.setUp_UI_add_BOM()
        
       
        self.VBox_all_grp_box_layout = QVBoxLayout()
        self.VBox_all_grp_box_layout.addLayout(self.dishEnd_sel_gridlayout)
        self.VBox_all_grp_box_layout.addWidget(self.grpbox_blktype)
        
        
        self.H_box_gb1_gb2_layout = QHBoxLayout()
        self.H_box_gb1_gb2_layout.addWidget(self.grp_box1)
        self.H_box_gb1_gb2_layout.addWidget(self.grp_box2)

       
       
        self.VBox_all_grp_box_layout.addLayout(self.H_box_gb1_gb2_layout)
        self.VBox_all_grp_box_layout.addWidget(self.grp_box3)

       


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
        self.SetUI_asper_DEND() #As per Dend type=Blank or crown petal ,Adjust the UI
        #self.setLayout(self.VBox_all_grp_box_layout)

    def setUp_UI_dish_end_variant_selection(self):
        self.lbl_d_end_var_sel = QLabel("Type of Dish End")
        self.lbl_d_end_var_sel.setStyleSheet("background-color: lightgreen; font-weight: bold;")
        self.cmbbox_DEnd_var_sel=QComboBox()
        type_list=['Blank','Crown and Petal']
        self.cmbbox_DEnd_var_sel.addItems(type_list)
        self.cmbbox_DEnd_var_sel.currentIndexChanged.connect(self.SetUI_asper_DEND)
        self.cmbbox_DEnd_var_sel.setStyleSheet("background-color: lightgreen; font-weight: bold;")
        
        self.lbl_DEnd_type =QLabel("Select Shape")
        self.lbl_DEnd_type.setStyleSheet("background-color: lightgreen; font-weight: bold;")
        self.cmbbox_d_end_shape_type=QComboBox()
        self.DEnd_shape_list=['Ellipsoidal','Tori Spherical']
        self.cmbbox_d_end_shape_type.addItems(self.DEnd_shape_list)
        self.cmbbox_d_end_shape_type.setStyleSheet("background-color: lightgreen; font-weight: bold;")
        
        self.dishEnd_sel_gridlayout=QGridLayout()
        
        self.dishEnd_sel_gridlayout.addWidget(self.lbl_d_end_var_sel,0,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.dishEnd_sel_gridlayout.addWidget(self.cmbbox_DEnd_var_sel,0,1,alignment=Qt.AlignmentFlag.AlignLeft)
        self.dishEnd_sel_gridlayout.addWidget(self.lbl_DEnd_type,1,0,alignment=Qt.AlignmentFlag.AlignRight)
        self.dishEnd_sel_gridlayout.addWidget(self.cmbbox_d_end_shape_type,1,1,alignment=Qt.AlignmentFlag.AlignLeft)
        
       
    def setUp_UI_blank_type_DEND(self):
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
        self.button_calc_blkdia.setMaximumSize(200, 50)
        self.button_calc_blkdia.clicked.connect(self.calc_Blkdia)
        # self.lbl_blktype_Wt=QLabel("Weight")
        # self.tb_blktype_Wt = QLineEdit("0.00")
        
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
        self.grpbox_blktype = QGroupBox("Input")
        self.grpbox_blktype.setLayout(self.gridlayout_blktype)
        #self.gridlayout_blktype.addWidget(self.lbl_blktype_BLKDIA)
       
    def setUp_UI_Dend_crn_petal_ip(self):
        # Create two QRadioButton objects to arrange in the group box
        # self.lbl_d_end_type = QLabel("Select Type")
        # self.rb1 = QRadioButton("Tori")
        # self.rb2 = QRadioButton("Ellip")
        # # If Radio button is toggled
        # self.rb1.toggled.connect(self.Set_D_end_type)
        # self.rb2.toggled.connect(self.Set_D_end_type)
        # self.rb1.setChecked(True)  # Set radio button1 selection default
        # self.rb_h_box = QHBoxLayout()
        # self.rb_h_box.addWidget(self.lbl_d_end_type)
        # self.rb_h_box.addWidget(self.rb1)
        # self.rb_h_box.addWidget(self.rb2)
        # self.rb_h_box.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #Material List
        self.Material_list=var.master_mat_list
        # Shell_DEnd_mat_list=['SA516Gr.60','SA516Gr.60(N)','SA516GR.60(NACE)','SA516Gr.60(NACE+HIC)','SA516Gr.60(NACE)+CLAD','SA516Gr.70',
        #         'SA105','SA105(NACE)','SA105(CLAD)','SA106Gr.B','SA106Gr.B(NACE)','SA106Gr.B(CLAD)','SA234Gr.WPB',
        #         'SA234Gr.WPB+CLAD','SA240TP304L','IS2062Gr.B']
        # Inner_plate_mat_list=['SA516Gr.60','SA516Gr.60(N)','SA516GR.60(NACE)','SA516Gr.60(NACE+HIC)','SA516Gr.60(NACE)+CLAD','SA516Gr.70',
        #               'SA105','SA105(NACE)','SA105(CLAD)','SA106Gr.B','SA106Gr.B(NACE)','SA106Gr.B(CLAD)','SA234Gr.WPB',
        #               'SA234Gr.WPB+CLAD','SA240TP304L','IS2062Gr.B']


        # Create label and textboxes
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

        # Default Input Values for testing
        self.Set_Default_Input_For_Dish_end_calc()


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

   

    def setUp_UI_refrence_images(self):
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

    def setUp_UI_add_BOM(self):
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

    def calc_Blkdia(self):
        #print("blkdia pressed")
        blktype_IKR,blktype_ICR=0,0
        if(str.upper(self.cmbbox_d_end_shape_type.currentText())=='TORI SPHERICAL'):
            blktype_IKR =float(self.tb_blktype_ID.text())*0.15
            blktype_ICR=float(self.tb_blktype_ID.text())*0.8
        elif (str.upper(self.cmbbox_d_end_shape_type.currentText())=='ELLIPSOIDAL'):
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
    
    def SetUI_asper_DEND(self):
          
        if(str.upper(self.cmbbox_DEnd_var_sel.currentText())=='BLANK'):
            self.grpbox_blktype.setVisible(True)
            self.grp_box1.setVisible(False)
            self.grp_box2.setVisible(False)
            self.grp_box3.setVisible(False)
            #Reduce the size of the container holding mainV box as we cant control the size of layout
            #we can only control size of widgets.
            self.container_widget.setFixedHeight(400)
            
        else:
            self.grpbox_blktype.setVisible(False)
            self.grp_box1.setVisible(True)
            self.grp_box2.setVisible(True) 
            self.grp_box3.setVisible(True) 
            #Reset the size of the container
            self.container_widget.setFixedHeight(800)
    
    def Set_D_end_type(self):
        # if self.rb1.isChecked():
        #     #print("rb1_selecetd")
        #     self.dentype=1

        # elif self.rb2.isChecked():
        #     #print("rb2_selected")
        #     self.dentype = 2
        if(str.upper(self.cmbbox_d_end_shape_type.currentText())=='TORI SPHERICAL'):
            self.dentype=1
        elif (str.upper(self.cmbbox_d_end_shape_type.currentText())=='ELLIPSOIDAL'):
            self.dentype=2    
        
    def petel_calc_button_pressed(self):
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
        calc.Toripetal()#Main DEnd Calculation
        
        self.update_grp_box3() #Update DEnd BOM groupbox values

        #Change the Add material color back to default 
        self.reset_button_color_default(self.btn_add_material)

    def update_grp_box3(self):
       self.tb_No_of_petel.setText(str(var.DEND_Crn_Petal_type_Params_incld_allwnc['N']))   
       self.tb_wt_per_petel.setText(str(var.DEND_Crn_Petal_type_Params_incld_allwnc['PETLWT1']))
       self.tb_D_end_material.setText(str(var.DEND_Crn_Petal_type_Params_incld_allwnc['PETEL_MATERIAL']))
       self.tb_D_end_Surface_Area.setText(var.DEND_Crn_Petal_type_Params_incld_allwnc['SURFACE_AREA'])


    def Set_Default_Input_For_Dish_end_calc(self):
        self.dentype=1
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


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dend = DEnd()
#     dend.show()