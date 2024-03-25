from schemdraw import logic , Drawing
import schemdraw
import schemdraw.elements as elm
from schemdraw.segments import *
from schemdraw import Drawing
from schemdraw import logic
from PyQt6.QtWidgets import QMessageBox

def circuit_half(text1):
        class C_element(elm.Element):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                if len(text1) < 2:
                    QMessageBox.warning(None, "Warning", "ข้อมูลไม่ถูกต้องในการสร้างกราฟและวงจร")
                else:
                    if len(text1[0].split()) <= 3:
                        QMessageBox.warning(None, "Warning", "ข้อมูลไม่ถูกต้องในการสร้างกราฟและวงจร")
                        return
                    elif len(text1[1].split()) <= 6:
                        QMessageBox.warning(None, "Warning", "ข้อมูลไม่ถูกต้องในการสร้างกราฟและวงจร")
                        return
                    else:
                        first_word_1 = text1[0].split()[2].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ -
                        third_word_1 = text1[0].split()[4].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ -
                        second_word_1 = text1[0].split()[3].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ -
                        sixth_word_2 = text1[1].split()[6].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ -

                # C 1
                self.segments.append(SegmentCircle([1.25, -0.65], 0.8, fill=None))
                self.segments.append(SegmentText([1.2, -0.76], "C", fontsize=35))
                self.segments.append(Segment([[1.25, 0.15], [1.25, 0.675]]))  # เส้นบน Input
                self.segments.append(SegmentText([-0.95, -2], first_word_1, fontsize=15)) # เอาตัวแรกมาแสดง input
                self.segments.append(SegmentText([-0.9, 0.7], second_word_1, fontsize=15)) # เอาตัวสามมาแสดง input
                self.segments.append(SegmentText([3.5, -0.72], third_word_1, fontsize=15)) # เอาตัวสามมาแสดง input
                self.segments.append(Segment([[1.25, -2], [1.25, -1.46]]))  # เส้นล่าง Input
                self.segments.append(Segment([[3, -0.7], [2.07, -0.7]]))  # เส้น Output
                self.segments.append(Segment([[-0.5, 0.7], [1.25, 0.7]]))  # เส้นบน Input ทางด้านซ้าย
                self.segments.append(Segment([[-0.5, -2], [1.25, -2]]))  # เส้นบน Input ทางด้านซ้าย

                # C 2
                self.segments.append(SegmentCircle([1.25, -5.15], 0.8, fill=None))
                self.segments.append(SegmentText([1.2, -5.26],"C",fontsize = 35))
                self.segments.append(Segment([[1.25, -4], [1.25,-3.825]])) #เส้นบน Input
                self.segments.append(Segment([[1.25, -6], [1.25,-6.52]])) #เส้นล่าง Input
                self.segments.append(Segment([[3, -5.2], [2,-5.2]])) #เล้น Output
                self.segments.append(Segment([[-0.5, -3.78], [1.25, -3.78]]))  # เส้นบน Input ทางด้านซ้าย
                self.segments.append(Segment([[-0.5, -6.55], [1.25, -6.55]]))  # เส้นบน Input ทางด้านซ้าย
                self.segments.append(SegmentText([-0.95, -3.78], first_word_1, fontsize=15)) # เอาตัวแรกมาแสดง input
                self.segments.append(SegmentText([-0.9, -6.5], sixth_word_2, fontsize=15)) # เอาตัวสามมาแสดง input
                self.segments.append(SegmentText([3.5, -5.175], second_word_1, fontsize=15)) # เอาตัวสามมาแสดง input
                self.segments.append(SegmentCircle([1.25, -4.18], 0.175)) #small circle

    # Create a drawing object
        d = Drawing()
        # Create an instance of your custom element
        c_element = C_element()
        # Add the element to the drawing
        d.add(c_element)
        # Save the drawing as an SVG file
        svg_file = 'circuithalf.svg'
        d.save(svg_file)
        # Read the content of the SVG file
        with open(svg_file, 'r') as f:
            svg_content = f.read()
        return svg_content

def circuit_full(text1):
        class C_element(elm.Element):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                if len(text1) < 1:
                    QMessageBox.warning(None, "Warning", "ข้อมูลไม่ถูกต้องในการสร้างกราฟและวงจร.")
                    return
                
                first_word_1 = text1[1].split()[4].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ -
                third_word_1 = text1[1].split()[2].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ -
                second_word_1 = text1[1].split()[3].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ -

                # C 1
                self.segments.append(SegmentCircle([1.25, -2.52], 0.8, fill=None))
                self.segments.append(SegmentText([1.2, -2.52],"C",fontsize = 35))
                self.segments.append(Segment([[1.25, -3.65], [1.25,-4]])) #เส้นล่าง Input
                self.segments.append(Segment([[1.25, -1.2], [1.25,-1.7]])) #เส้นบน Input
                self.segments.append(Segment([[3, -2.5], [2.07,-2.5]])) #เล้น Output
                self.segments.append(Segment([[-0.5, -1.2], [1.25, -1.2]]))  # เส้นบน Input ทางด้านซ้าย
                self.segments.append(Segment([[-0.5, -4], [1.25, -4]]))  # เส้นล่าง Input ทางด้านซ้าย
                self.segments.append(SegmentText([-0.95, -1.2], first_word_1, fontsize=15)) # เอาตัวแรกมาแสดง input
                self.segments.append(SegmentText([-0.9, -4], third_word_1, fontsize=15)) # เอาตัวสามมาแสดง input
                self.segments.append(SegmentText([3.5, -2.5], second_word_1, fontsize=15)) # เอาตัวสามมาแสดง input
                self.segments.append(SegmentCircle([1.25, -3.465], 0.175)) #small circle

        # Create a drawing object
        d = Drawing()
        first_word_1 = text1[0].split()[2].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ -
        second_word_1 = text1[0].split()[3].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ -
        third_word_1 = text1[0].split()[4].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ -
        # Add logic gates to the drawing
        gate4 = (a := logic.And(inputnots=[2]).label(first_word_1, 'in1').label(third_word_1, 'in2').label(second_word_1, 'out'))
        # Create an instance of your custom element
        c_element = C_element()
        # Add the element to the drawing
        d.add(c_element)
        # Get the dimensions of c_element
        c_element_dimensions = c_element.bbox
        # Define the position for gate4 relative to c_element
        gate4_x = c_element_dimensions[0] + 10
        gate4_y = c_element_dimensions[1] - 500
        # Add gate4 to the drawing at the specified position
        d.add(gate4).down().at([gate4_x, gate4_y])
        # Save the drawing as an SVG file
        svg_file = 'circuitfull.svg'
        d.save(svg_file)
        # Read the content of the SVG file
        with open(svg_file, 'r') as f:
            svg_content = f.read()
        return svg_content

def circuit_vbe5b(text1):
        class C_element(elm.Element):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                if len(text1) < 1:
                    QMessageBox.warning(None, "Warning", "ข้อมูลไม่ถูกต้องในการสร้างกราฟและวงจร.")
                    return
                
                first_word_1 = text1[0].split()[7].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Lr
                first_word_3 = text1[2].split()[2].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - La
                second_word_3 = text1[2].split()[6].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Zr

                # C 1
                self.segments.append(SegmentCircle([1.25, -0.9], 0.8, fill=None))
                self.segments.append(SegmentText([1.2, -0.9],"C",fontsize = 35))
                self.segments.append(Segment([[1.25, -2.2], [1.25,-1.755]])) #เส้นล่าง Input
                self.segments.append(Segment([[1.25, 0.4], [1.25,-0.1125]])) #เส้นบน Input
                self.segments.append(Segment([[3, -0.88], [2.07,-0.88]])) #เล้น Output
                self.segments.append(Segment([[-0.5, 0.4], [1.25, 0.4]]))  # เส้นบน Input ทางด้านซ้าย
                self.segments.append(Segment([[-0.5, -2.2], [1.25, -2.2]]))  # เส้นล่าง Input ทางด้านซ้าย
                self.segments.append(SegmentText([-0.95, 0.675], "Internal Wire 1", fontsize=15)) # เอาตัวแรกมาแสดง input
                self.segments.append(SegmentText([-0.9, -1.98], "Internal Wire 2", fontsize=15)) # เอาตัวสามมาแสดง input
                self.segments.append(SegmentText([3.5, -0.9], first_word_1, fontsize=15)) # เอาตัวสามมาแสดง input
                # C 2
                self.segments.append(SegmentCircle([8, -0.9], 0.8, fill=None))
                self.segments.append(SegmentText([8, -0.9],"C",fontsize = 35))
                self.segments.append(Segment([[8, 0.4], [8,-0.1125]])) #เส้นบน Input
                self.segments.append(Segment([[8, -2.2], [8,-1.755]])) #เส้นล่าง Input
                self.segments.append(Segment([[8.8, -0.88], [9.81,-0.88]])) #เล้น Output
                self.segments.append(Segment([[6, 0.4], [8, 0.4]]))  # เส้นบน Input ทางด้านซ้าย
                self.segments.append(Segment([[6, -2.2], [8, -2.2]]))  # เส้นบน Input ทางด้านซ้าย
                self.segments.append(SegmentText([5.5, 0.675], "Internal Wire 3", fontsize=15)) # เอาตัวแรกมาแสดง input
                self.segments.append(SegmentText([5.5, -2.16], first_word_3, fontsize=15)) # เอาตัวสามมาแสดง input
                self.segments.append(SegmentText([10.33, -0.9], second_word_3, fontsize=15)) # เอาตัวสามมาแสดง input

        # Create a drawing object
        d = Drawing()
        second_word_1 = text1[0].split()[6].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Za
        first_word_2 = text1[1].split()[7].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Da
        second_word_2 = text1[1].split()[6].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Dr
        first_word_3 = text1[2].split()[2].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - La
        second_word_3 = text1[2].split()[6].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Zr
        # กำหนดตำแหน่งและขนาดของ c_element
        c_element_x = 1
        c_element_y = 1
        # สร้าง c_element และกำหนดตำแหน่ง
        c_element = C_element().at([c_element_x, c_element_y])
        # gateOR
        # gateAND
        gateAND_x = c_element_x - 0.5
        gateAND_y = c_element_y + 2.2
        gateOR_x = c_element_x - 0.5
        gateOR_y = c_element_y + 4.2  # กำหนดตำแหน่ง Y ให้ gateAND ตรงกลางของ c_element
        gateOR1_x = gateOR_x + 6
        gateOR1_y = gateOR_y
        gateOR2_x = gateAND_x + 6
        gateOR2_y = gateAND_y 
        


        # สร้าง gate
        gateOR = (a := logic.Nor().label(first_word_2, 'in1').label(second_word_2, 'in2').label("Internal Wire 1", 'out')).at([gateOR_x, gateOR_y])
        gateOR1 = ( a := logic.Nor().label(second_word_1, 'in1').label(second_word_3, 'in2').label("Internal Wire 2", 'out')).at([gateOR1_x, gateOR1_y])
        gateAND1 = (a := logic.Nand().label(second_word_1, 'in1').label(first_word_2, 'in2').label("Internal Wire 3", 'out')).at([gateAND_x, gateAND_y])
        gateOR2 = ( a := logic.Nor().label(first_word_3, 'in1').label(second_word_3, 'in2').label(second_word_2, 'out')).at([gateOR2_x, gateOR2_y])
        # เพิ่ม c_element และ gate ลงใน drawing
        d.add(c_element)
        d.add(gateAND1)
        d.add(gateOR)
        d.add(gateOR1)
        d.add(gateOR2)
        # บันทึก drawing เป็นไฟล์ SVG
        svg_file = 'circuitvbe5b.svg'
        d.save(svg_file)
        # อ่านเนื้อหาของไฟล์ SVG
        with open(svg_file, 'r') as f:
            svg_content = f.read()
        # ส่งเนื้อหา SVG กลับ
        return svg_content

def circuit_chu133(text1):
        class C_element(elm.Element):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                if len(text1) < 1:
                    QMessageBox.warning(None, "Warning", "ข้อมูลไม่ถูกต้องในการสร้างกราฟและวงจร.")
                    return

                first_word_1 = text1[0].split()[2].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - La
                second_word_1 = text1[0].split()[3].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Dr
                first_word_2 = text1[1].split()[6].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Zr
                second_word_2 = text1[1].split()[8].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - X
                third_word_2 = text1[1].split()[7].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Za
                third_word_3 = text1[1].split()[5].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Da

                # C 1
                self.segments.append(SegmentCircle([1.25, -0.9], 0.8, fill=None))
                self.segments.append(SegmentText([1.2, -0.9],"C",fontsize = 35))
                self.segments.append(Segment([[1.25, -2.2], [1.25,-1.755]])) #เส้นล่าง Input
                self.segments.append(Segment([[1.25, 0.4], [1.25,-0.1125]])) #เส้นบน Input
                self.segments.append(Segment([[3, -0.88], [2.07,-0.88]])) #เล้น Output
                self.segments.append(Segment([[-0.5, 0.4], [1.25, 0.4]]))  # เส้นบน Input ทางด้านซ้าย
                self.segments.append(Segment([[-0.5, -2.2], [1.25, -2.2]]))  # เส้นล่าง Input ทางด้านซ้าย
                self.segments.append(SegmentText([-0.95, 0.675], first_word_1, fontsize=15)) # เอาตัวแรกมาแสดง input 1
                self.segments.append(SegmentText([-0.9, -1.98], first_word_2, fontsize=15)) # เอาตัวสามมาแสดง input 2
                self.segments.append(SegmentText([3.5, -0.9], second_word_1, fontsize=15)) # เอาตัวสามมาแสดง output
                # C 2
                self.segments.append(SegmentCircle([8, -0.9], 0.8, fill=None))
                self.segments.append(SegmentText([8, -0.9],"C",fontsize = 35))
                self.segments.append(Segment([[8, 0.4], [8,-0.1125]])) #เส้นบน Input
                self.segments.append(Segment([[8, -2.2], [8,-1.755]])) #เส้นล่าง Input
                self.segments.append(Segment([[8.8, -0.88], [9.81,-0.88]])) #เล้น Output
                self.segments.append(Segment([[6, 0.4], [8, 0.4]]))  # เส้นบน Input ทางด้านซ้าย
                self.segments.append(Segment([[6, -2.2], [8, -2.2]]))  # เส้นบน Input ทางด้านซ้าย
                self.segments.append(SegmentText([5.5, 0.675], third_word_2, fontsize=15)) # เอาตัวแรกมาแสดง input
                self.segments.append(SegmentText([5.5, -2.16], third_word_3, fontsize=15)) # เอาตัวสามมาแสดง input
                self.segments.append(SegmentText([10.33, -0.9], second_word_2, fontsize=15)) # เอาตัวสามมาแสดง input

        # Create a drawing object
        d = Drawing()
        second_word_1 = text1[0].split()[3].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Dr
        first_word_2 = text1[1].split()[6].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Zr
        second_word_2 = text1[1].split()[8].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - X
        third_word_3 = text1[1].split()[5].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Da
        first_word_3 = text1[2].split()[4].replace('+', '').replace('-', '')  # ลบเครื่องหมาย + และ - Lr
        
        # กำหนดตำแหน่งและขนาดของ c_element
        c_element_x = 1
        c_element_y = 1
        # สร้าง c_element และกำหนดตำแหน่ง
        c_element = C_element().at([c_element_x, c_element_y])
        # gateAND
        gateAND_x = c_element_x - 0.5
        gateAND_y = c_element_y + 2.2
        # gateOR
        gateOR_x = gateAND_x + 6
        gateOR_y = gateAND_y  # กำหนดตำแหน่ง Y ให้ gateAND ตรงกลางของ c_element
        # สร้าง gate
        gateOR = (a := logic.Nor().label(second_word_2, 'in1').label(second_word_1, 'in2').label(first_word_3, 'out')).at([gateOR_x, gateOR_y])
        gateAND1 = (a := logic.And(inputnots=[2]).label(third_word_3, 'in1').label(second_word_2, 'in2').label(first_word_2, 'out')).at([gateAND_x, gateAND_y])
        # เพิ่ม c_element และ gate ลงใน drawing
        d.add(c_element)
        d.add(gateAND1)
        d.add(gateOR)
        # บันทึก drawing เป็นไฟล์ SVG
        svg_file = 'circuitchu133.svg'
        d.save(svg_file)
        # อ่านเนื้อหาของไฟล์ SVG
        with open(svg_file, 'r') as f:
            svg_content = f.read()
        # ส่งเนื้อหา SVG กลับ
        return svg_content
