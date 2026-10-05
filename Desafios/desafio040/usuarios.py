class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Aluno:
    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie

class JSON:
    def exportar(self, dados):
        from json import dumps
        
        lista = []
        for item in dados:
            lista.append(item.__dict__)
        txt = dumps(lista, ensure_ascii=False, indent=2)
        return f'Exportando dados de {txt} para JSON'

class XML:
    def exportar(self, dados):
        import xml.etree.ElementTree as ET
        nome = dados[0].__class__.__name__.lower()
        pai = ET.Element('dados')
        for item in dados:
            filho = ET.SubElement(pai, nome)
            for chave, valor in item.__dict__.items():
                neto = ET.SubElement(filho, chave)
                neto.text = str(valor)
        ET.indent(pai, space='\t', level=0)
        txt = ET.tostring(pai, encoding='unicode', xml_declaration=True)
        return txt

def exportar_dados(formato, dados):
    print(f'{formato.exportar(dados)}')