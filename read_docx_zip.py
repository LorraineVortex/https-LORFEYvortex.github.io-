import zipfile
import xml.etree.ElementTree as ET

# 打开DOCX文件（本质是ZIP文件）
with zipfile.ZipFile('文字文稿(8).docx', 'r') as docx_zip:
    # 读取document.xml文件
    with docx_zip.open('word/document.xml') as xml_file:
        # 解析XML
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # 定义命名空间
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        # 提取所有文本内容
        text_elements = root.findall('.//w:t', ns)
        text_content = '\n'.join([elem.text for elem in text_elements if elem.text])
        
        print(text_content)