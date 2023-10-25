import math
from Variables import var
import os
import datetime


class DishEndCalc:
    A = 0

    def __init__(self,input_dict):
        #self.var = Variables()
        print(input_dict)
        self.Material =input_dict['Material']
        self.ICNT = 0
        self.IDA = 3000
        self.ID = input_dict["ID"]
        self.ICRA = 0
        self.IKRA = 0
        self.ICR = input_dict["ICR"]
        self.IKR = input_dict["IKR"]
        self.SF = input_dict["SF"]
        self.TKA = 0
        self.TK = input_dict["TK"]
        self.CRNDIAA = 0
        self.CRNDIA = input_dict["CRNDIA_d"]
        self.STLEN1 = input_dict["SL"]
        self.RATIO = input_dict["RATIO"]
        self.THETA = 0
        self.WONO = var.project_id
        self.dendtyp = 0
        self.N = input_dict["N"]
        self.NA = 0
        self.allwnc = input_dict["Allwnc"]
        self.A11 = 0
        self.B11 = 0
        self.ALP1 = 0
        self.D11 = 0
        self.ALP4 = 0
        self.ALEN = 0
        self.BETA = 0
        self.SWIDTH = 0
        self.ADDL = 0
        self.B77 = 0
        self.BWIDTH = 0
        self.STLEN2 = 0
        self.SLLEN = 0
        self.XSML = 0
        self.GAMA = 0
        self.MCR = 0
        self.BLKDIA = 0
        self.BLKDIA1 = 0
        self.BLKWT = 0
        self.BLKWT1 = 0
        self.Y = 0
        self.AXX = 0
        self.DXX = 0
        self.BXX = 0
        self.ANGLE1 = 0
        self.ADDL1 = 0
        self.OFFSET = 0
        self.XBETA = 0
        self.AREA1 = 0
        self.AREA2 = 0
        self.PETLAREA = 0
        self.PETLWT = 0
        self.OMEGA = 0
        self.ALLS = 0
        self.ALCR = 0
        self.STLEN = 0
        self.SWID = 0
        self.BWID = 0
        self.ALEN2 = 0
        self.PETLAREA1 = 0
        self.PETLWT1 = 0

    # @staticmethod
    def Toripetal(self):

        self.IDA = 3000

        self.ICNT = 0

        if self.ID == 0:
            self.ID = self.IDA

        if self.dendtyp == 1:
            self.ICRA = self.ID * 0.8
            self.IKRA = self.ID * 0.15
        else:
            self.ICRA = self.ID * 0.9045085
            self.IKRA = self.ID * 0.1727457

        if self.ICR == 0:
            self.ICR = self.ICRA

        if self.IKR == 0:
            self.IKR = self.IKRA

        if self.SF == 0:
            self.SF = 50

        self.TKA = 10

        if self.TK == 0:
            self.TK = self.TKA

        if self.ID <= 1000:
            self.NA = 3
        elif self.ID <= 2000:
            self.NA = 4
        elif self.ID <= 3000:
            self.NA = 6
        elif self.ID <= 4000:
            self.NA = 8
        elif self.ID <= 5000:
            self.NA = 10
        elif self.ID <= 6000:
            self.NA = 12

        if self.N == 0:
            self.N = self.NA

        self.CRNDIAA = 0.5 * self.ID

        if self.CRNDIA == 0:
            self.CRNDIA = self.CRNDIAA

        if self.STLEN1 <= 0 and self.RATIO <= 0:
            self.RATIO = 0.25

        if self.allwnc == 0:
            self.allwnc = 100

        filecontent = ""
        filecontent += str(datetime.datetime.now()) + "\n"
        filecontent += "DEVELOPMENT OF TORISPHERICAL DISHED END PETALS\n"
        filecontent += "WORKORDER No:-\t" + str(self.WONO) + "\n"

        filecontent += "----------------------------------------------------------------------------------------------------\n"
        filecontent += "\t\t\t\tINPUTS\n"
        filecontent += "----------------------------------------------------------------------------------------------------\n"
        filecontent += "INSIDE DIA OF TORISPHERICAL DISHED END, ID (mm)\t\t\t=\t" + str(self.ID) + "\n"
        filecontent += "INSIDE CROWN RADIUS, ICR (mm)\t\t\t\t\t=\t" + str(self.ICR) + "\n"
        filecontent += "INSIDE KNUCKLE RADIUS, IKR (mm)\t\t\t\t\t=\t" + str(self.IKR) + "\n"
        filecontent += "STRAIGHT FLANGE OF DISHED END, SF (mm)\t\t\t\t=\t" + str(self.SF) + "\n"

        filecontent += "THICKNESS OF PETAL, t (mm)\t\t\t\t\t=\t" + str(self.TK) + "\n"
        filecontent += "NUMBER OF PETALS, N\t\t\t\t\t\t=\t" + str(self.N) + "\n"
        filecontent += "CROWN DIAMETER, d (mm)\t\t\t\t\t\t=\t" + str(self.CRNDIA) + "\n"
        filecontent += "STRAIGHT LENGTH IN THE DEVELOPED PETAL, SL (mm)\t\t\t=\t" + str(self.STLEN1) + "\n"
        filecontent += "RATIO OF STRAIGHT LENGTH TO TOTAL LENGTH, RATIO\t\t\t=\t" + str(self.RATIO) + "\n"

        self.ID = self.ID + self.TK
        self.IKR = self.IKR + self.TK / 2
        self.ICR = self.ICR + self.TK / 2
        self.THETA = math.pi / self.N
        self.A11 = self.CRNDIA / 2.0
        self.B11 = self.A11 * self.THETA
        self.ALP1 = math.asin(self.A11 / self.ICR)
        self.D11 = self.A11 / math.cos(self.ALP1)
        self.ALP4 = math.asin((self.ID / 2 - self.IKR) / (self.ICR - self.IKR))
        self.ALEN = self.SF + (math.pi / 2 - self.ALP4) * self.IKR + (self.ALP4 - self.ALP1) * self.ICR
        self.BETA = 2 * math.asin(self.B11 / (2 * self.D11))
        self.SWIDTH = self.B11 * 2
        self.ADDL = (1 - math.cos(self.BETA)) * self.D11
        self.ALEN = self.ALEN + self.ADDL
        self.B77 = self.ID * (self.THETA / 2)
        self.BWIDTH = 2 * self.B77

        if self.STLEN1 <= 0.01:
            self.STLEN1 = self.RATIO * self.ALEN

        self.STLEN2 = 0.3 * self.ALEN + 1
        self.SLLEN = self.ALEN - self.STLEN1
        self.XSML = self.SWIDTH / 2
        self.GAMA = self.ALP1

        self.MCR = self.ICR
        self.BLKDIA = 2 * self.ALP1 * self.MCR
        self.BLKDIA1 = self.BLKDIA + self.allwnc

        self.BLKWT = math.pi / 4 * self.BLKDIA * self.BLKDIA * self.TK * 7.85 * 10 ** -6
        self.BLKWT1 = math.pi / 4 * self.BLKDIA1 * self.BLKDIA1 * self.TK * 7.85 * 10 ** -6

        filecontent += "\n\n"
        filecontent += "----------------------------------------------------------------------------------------------------\n"
        filecontent += "\t\t\t\tOUTPUT\n"
        filecontent += "----------------------------------------------------------------------------------------------------\n"

        filecontent += "BLANK DIAMETER OF CROWN (mm)/Wt.OF CROWN WITHOUT ALLOWANCES(Kg)\t\t=\t" + str(
            round(self.BLKDIA, 2)) + "/" + str(round(self.BLKWT, 2)) + "\n"
        filecontent += "BLANK DIAMETER OF CROWN (mm)/Wt.OF CROWN WITH " + str(
            self.allwnc) + " mm ALLOWANCES(Kg)\t=\t" + str(round(self.BLKDIA1, 2)) + "/" + str(
            round(self.BLKWT1, 2)) + "\n"
        # filecontent += "BLANK DIAMTER OF CROWN INCL. 60 MM ALLOW.(mm)\t\t\t=\t" + str(round(self.BLKDIA1, 2)) + "\n"

        # filecontent += "WEIGHT OF FINISHED BLANK (KG)\t\t\t\t\t=\t" + str(round(self.BLKWT, 2)) + "\n"
        # filecontent += "WEIGHT OF BLANK WITH ALLOWANCE (KG)\t\t\t\t=\t" + str(round(self.BLKWT1, 2)) + "\n"
        filecontent += "CALCULATED SIZE OF SMALLER SIDE(MIN), b (mm)\t\t\t\t=\t" + str(round(self.SWIDTH, 2)) + "\n"
        # filecontent += "----------------------------------------------------------------------------------------------------\n"
        # write close

        i = 1
        while i <= 5000:
            i += 1
            self.Y = self.ADDL + (self.GAMA - self.ALP1) * self.ICR

            if self.GAMA > self.ALP4:
                self.Y = self.ADDL + (self.ALP4 - self.ALP1) * self.ICR + (self.GAMA - self.ALP4) * self.IKR

            self.AXX = self.ID / 2 - (1 - math.cos(math.pi / 2 - self.GAMA)) * self.IKR

            if self.GAMA < self.ALP4:
                self.AXX = self.ICR * math.sin(self.GAMA)

            self.DXX = self.AXX / math.cos(self.GAMA)
            self.BXX = self.AXX * self.THETA
            self.ANGLE1 = 2 * math.asin(self.BXX / (2 * self.DXX))
            self.ADDL1 = self.DXX * (1 - math.cos(self.ANGLE1))

            self.Y = self.Y - self.ADDL1
            if self.Y <= self.SLLEN:
                self.OFFSET = self.DXX * math.sin(self.ANGLE1)
                self.XBETA = self.B77 - (self.B77 - self.XSML) * (self.SLLEN - self.Y) / self.SLLEN
                while self.XBETA < self.OFFSET:
                    self.XSML += 1
                    self.XBETA = self.B77 - (self.B77 - self.XSML) * (self.SLLEN - self.Y) / self.SLLEN
                self.GAMA = self.GAMA + 0.01
                i = 5001

        self.SWIDTH = 2 * self.XSML

        filecontent += "\n\n"
        filecontent += "DIMENSION OF THE PETAL WITHOUT ALLOWANCES\n"
        filecontent += "\n"
        filecontent += "WIDTH ON LARGER SIDE, A (mm)\t\t\t\t\t=\t" + str(round(self.BWIDTH, 2)) + "\n"
        filecontent += "WIDTH ON SMALLER SIDE, B (mm)\t\t\t\t\t=\t" + str(round(self.SWIDTH, 2)) + "\n"
        filecontent += "TOTAL LENGTH, L (mm)\t\t\t\t\t\t=\t" + str(round(self.ALEN, 2)) + "\n"
        filecontent += "LENGTH OF STRAIGHT PORTION, C (mm)\t\t\t\t=\t" + str(round(self.STLEN1, 2)) + "\n"

        self.AREA1 = self.BWIDTH * self.STLEN1
        self.AREA2 = (self.ALEN - self.STLEN1) * 0.5 * (self.BWIDTH + self.SWIDTH)
        self.PETLAREA = self.AREA1 + self.AREA2
        self.PETLWT = self.TK * self.PETLAREA * 7.85 * 10 ** -6

        filecontent += "WEIGHT OF FINISHED PETAL (KG)\t\t\t\t\t=\t" + str(round(self.PETLWT, 2)) + "\n"
        filecontent += "----------------------------------------------------------------------------------------------------\n"

        self.OMEGA = math.atan((self.B77 - self.XSML) / self.SLLEN)

        if self.TK > 20:
            self.ALLS = self.TK
        else:
            self.ALLS = 20

        self.ALCR = self.allwnc #40  ##Original lisp code its 30,
        self.BWID = self.BWIDTH + (2 * self.ALLS) # A-1
        self.SWID = (self.SWIDTH + (2 * self.ALLS / math.cos(self.OMEGA))) - (2 * self.ALCR * math.tan(self.OMEGA)) #B-2
        self.ALEN2 = self.ALEN + (self.ALCR * 2) #L-3
        self.STLEN = self.STLEN1 + self.ALCR + (self.ALLS * math.tan(self.OMEGA / 2)) #C-4

        filecontent += "\n\n"
        filecontent += "DIMENSION OF THE PETAL INCLUDING ALLOWANCES FOR PETAL EXCEPT CLOSING PETAL\n"
        filecontent += "\n"
        filecontent += "WIDTH ON LARGER SIDE, A (mm)\t\t\t\t\t=\t" + str(round(self.BWID, 2)) + "\n"
        filecontent += "WIDTH ON SMALLER SIDE, B (mm)\t\t\t\t\t=\t" + str(round(self.SWID, 2)) + "\n"
        filecontent += "TOTAL LENGTH, L (mm)\t\t\t\t\t\t=\t" + str(round(self.ALEN2, 2)) + "\n"
        filecontent += "LENGTH OF STRAIGHT PORTION, C (mm)\t\t\t\t=\t" + str(round(self.STLEN, 2)) + "\n"

        self.AREA1 = self.BWID * self.STLEN
        self.AREA2 = (self.ALEN2 - self.STLEN) * 0.5 * (self.BWID + self.SWID)
        self.PETLAREA1 = self.AREA1 + self.AREA2
        self.PETLWT1 = self.TK * self.PETLAREA1 * 7.85 * 10 ** -6

        # var.DEND_Crn_Petal_type_Params_incld_allwnc["N"]=str(self.N)#Save No. of Petels to Variables
        # var.DEND_Crn_Petal_type_Params_incld_allwnc['PETLWT1']=str(round(self.PETLWT1)) #Save wt to Variables
        # var.DEND_Crn_Petal_type_Params_incld_allwnc["PETEL_MATERIAL"]=str(self.Material)#Save Material to Variables
        # #var.DEND_Params["BLKDIA1"]=str(round(self.BLKDIA1,2))#Save Blank Dia with allwnc  to Variables
        # var.DEND_Crn_Petal_type_Params_incld_allwnc["SURFACE_AREA"]=str(round(math.pi/4*(self.BLKDIA1/1000)**2,2))#Save Surface Area to Variables
        #print(self.BLKDIA1,float(var.DEND_Crn_Petal_type_Params_incld_allwnc["SURFACE_AREA"]))
        
        #Save output to Var.py
        var.CRN_AND_PETEL_OP_PARMS_WITH_ALLWNC={
            "N":self.N,
            "A":round(self.BWID, 2),
            "B":round(self.SWID, 2),
            "TL":round(self.ALEN2, 2),
            "SL":round(self.STLEN, 2),
            "PETELAREA":round(self.PETLAREA1/1000000,2),
            "PETELWT":round(self.PETLWT1),
            "MATERIAL":self.Material
        }

        filecontent += "WEIGHT OF PETAL WITH ALLOWANCE (KG)\t\t\t\t=\t" + str(round(self.PETLWT1, 2)) + "\n"
        filecontent += "----------------------------------------------------------------------------------------------------\n"


        K = 20
        # self.ALCR = 35
        self.BWID = self.BWIDTH + K + (2 * self.ALLS)  # A -1
        self.SWID = (self.SWIDTH + K + (2 * self.ALLS / math.cos(self.OMEGA))) - (
                2 * self.ALCR * math.tan(self.OMEGA))  # B -2
        self.ALEN2 = self.ALEN + (self.ALCR * 2)  # L-3
        self.STLEN = self.STLEN1 + self.ALCR + (self.ALLS * math.tan(self.OMEGA / 2))  # C-4
        
      
        
        

        filecontent += "\n\n"
        filecontent += "DIMENSION OF THE PETAL INCLUDING ALLOWANCES FOR CLOSING PETAL\n"
        filecontent += "\n"
        filecontent += "WIDTH ON LARGER SIDE, A (mm)\t\t\t\t\t=\t" + str(round(self.BWID, 2)) + "\n"
        filecontent += "WIDTH ON SMALLER SIDE, B (mm)\t\t\t\t\t=\t" + str(round(self.SWID, 2)) + "\n"
        filecontent += "TOTAL LENGTH, L (mm)\t\t\t\t\t\t=\t" + str(round(self.ALEN2, 2)) + "\n"
        filecontent += "LENGTH OF STRAIGHT PORTION, C (mm)\t\t\t\t=\t" + str(round(self.STLEN, 2)) + "\n"

        self.AREA1 = self.BWID * self.STLEN
        self.AREA2 = (self.ALEN2 - self.STLEN) * 0.5 * (self.BWID + self.SWID)
        self.PETLAREA1 = self.AREA1 + self.AREA2
        self.PETLWT1 = self.TK * self.PETLAREA1 * 7.85 * 10 ** -6

        filecontent += "WEIGHT OF PETAL WITH ALLOWANCE (KG)\t\t\t\t=\t" + str(round(self.PETLWT1, 2)) + "\n"
        filecontent += "----------------------------------------------------------------------------------------------------\n"
        filecontent += "\t\t\t\tPROGRAM END\n"
        filecontent += "----------------------------------------------------------------------------------------------------\n"

        self.write_to_file(file_content=filecontent)
        
        return var.CRN_AND_PETEL_OP_PARMS_WITH_ALLWNC

    def write_to_file(self, file_content):
        from Calculation.abs_path import absolute_path
        path = "Output" + "\\" + str(var.project_id)
        project_folder = absolute_path(path)
        if not os.path.exists(project_folder):
            os.makedirs(project_folder, exist_ok=True)

        op_file_name = " ".join(("DishEnd_Output_", var.project_id, ".txt"))
        dish_end_op_file_path = os.path.join(project_folder, op_file_name)
        print(dish_end_op_file_path)

        with open(dish_end_op_file_path, "w") as f:
            f.write(file_content)
            f.close()
    