from graphviz import Digraph

def graph_full(vars):
    generated_edges = set() # สร้าง set เพื่อเก็บเส้น
    ps = Digraph('full', node_attr={'penwidth': '0', 'style': 'underline'})

    for x in vars: # ลูปผ่านทุกๆ โหนดที่อยู่ใน vars
        nodes = x.split() # แยกคำใน x โดยใช้ช่่องว่างเป็นตัวแยก
        a = len(nodes) - 1 # นับคำใน node 
        if a == 1: # เช็คว่ามีแค่ 2 Nodes 
            edge = (nodes[0], nodes[1]) # คู่ของโหนดที่เชื่อม
            if edge not in generated_edges: # ตรวจสอบว่าเชื่อมไปแล้วยัง
                ps.edge(nodes[0], nodes[1]) # สร้างเส้นเชื่อมตามคู่ที่กำหนด
                generated_edges.add(edge) # เพิ่มคู่ที่เชื่อมแล้วเข้า set()
        else: 
            for i in range(len(nodes)): # loop ใน list node กรณี 
                if i != a: # check ว่า node ปัจุบันไท่ได้อยู่ที่สุดท้าย
                    edge = (nodes[i], nodes[i + 1]) # คู่ของโหนดที่เชื่อม
                    if edge not in generated_edges: # ตรวจสอบว่าเชื่อมไปแล้วยัง
                        ps.edge(nodes[i], nodes[i + 1]) # สร้างเส้นเชื่อมตามคู่ที่กำหนด
                        generated_edges.add(edge) # เพิ่มคู่ที่เชื่อมแล้วเข้า set()
                else:
                    edge = (nodes[i], nodes[0])
                    if edge not in generated_edges:
                        ps.edge(nodes[i], nodes[0])
                        generated_edges.add(edge)
        for node in nodes:
            if node in ['Ri+', 'Ai-', 'Ri-', 'Ai+']:
                ps.node(node, label='<<u>' + node + '</u>>')
    return ps


def graph_half(vars):
    generated_edges = set()
    ps = Digraph('full', node_attr={'penwidth': '0', 'style': 'underline'})

    # Create edges
    for x in vars:
        nodes = x.split()
        a = len(nodes) - 1
        if a == 1:
            edge = (nodes[0], nodes[1])
            if edge not in generated_edges:
                ps.edge(nodes[0], nodes[1])
                generated_edges.add(edge)
        else:
            for i in range(len(nodes)):
                if i != a:
                    edge = (nodes[i], nodes[i + 1])
                    if edge not in generated_edges:
                        ps.edge(nodes[i], nodes[i + 1])
                        generated_edges.add(edge)
                else:
                    edge = (nodes[i], nodes[0])
                    if edge not in generated_edges:
                        ps.edge(nodes[i], nodes[0])
                        generated_edges.add(edge)

    return ps


def graph_chu133(vars):
    generated_edges = set()
    ps = Digraph('full', node_attr={'penwidth': '0', 'style': 'underline'})

    # Create edges
    for x in vars:
        nodes = x.split()
        a = len(nodes) - 1
        if a == 1:
            edge = (nodes[0], nodes[1])
            if edge not in generated_edges:
                ps.edge(nodes[0], nodes[1])
                generated_edges.add(edge)
        else:
            for i in range(len(nodes)):
                if i != a:
                    edge = (nodes[i], nodes[i + 1])
                    if edge not in generated_edges:
                        ps.edge(nodes[i], nodes[i + 1])
                        generated_edges.add(edge)
                else:
                    edge = (nodes[i], nodes[0])
                    if edge not in generated_edges:
                        ps.edge(nodes[i], nodes[0])
                        generated_edges.add(edge)
        for node in nodes:
            if node in ['La+', 'Za+', 'La-', 'Da+', 'Za-', 'Da-']:
                ps.node(node, label='<<u>' + node + '</u>>')
    return ps


def graph_vbe5b(vars):
    generated_edges = set()
    ps = Digraph('full', node_attr={'penwidth': '0', 'style': 'underline'})

    # Create edges
    for x in vars: # ลูปผ่านทุกๆ โหนดที่อยู่ใน vars
        nodes = x.split() # แยกคำใน x โดยใช้ช่่องว่างเป็นตัวแยก
        a = len(nodes) - 1 # นับคำใน node 
        if a == 1: # เช็คว่ามีแค่ 2 Nodes 
            edge = (nodes[0], nodes[1]) # คู่ของโหนดที่เชื่อม
            if edge not in generated_edges: # ตรวจสอบว่าเชื่อมไปแล้วยัง
                ps.edge(nodes[0], nodes[1]) # สร้างเส้นเชื่อมตามคู่ที่กำหนด
                generated_edges.add(edge) # เพิ่มคู่ที่เชื่อมแล้วเข้า set()
        else: 
            for i in range(len(nodes)): # loop ใน list node กรณี 
                if i != a: # check ว่า node ปัจุบันไท่ได้อยู่ที่สุดท้าย
                    edge = (nodes[i], nodes[i + 1]) 
                    if edge not in generated_edges:
                        ps.edge(nodes[i], nodes[i + 1])
                        generated_edges.add(edge)
                else:
                    edge = (nodes[i], nodes[0])
                    if edge not in generated_edges:
                        ps.edge(nodes[i], nodes[0])
                        generated_edges.add(edge)
        for node in nodes:
            if node in ['La+', 'Za+', 'La-', 'Da+', 'Za-', 'Da-']:
                ps.node(node, label='<<u>' + node + '</u>>')
    return ps

