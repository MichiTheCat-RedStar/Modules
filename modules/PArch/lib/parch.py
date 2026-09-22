# 	parch // ☭
# MichiTheCat-RedStar (c) 2026

from zlib import compress
from pathlib import Path
from sys import argv


def PArch(path:str, is_object:bool=False) -> str:
	'Создать из файла python-код'
	
	# Теги шаблона:
	#  <|CONTENT|> - байт-контент
	#  <|NAME|> - имя файла (с расширением)
	blueprint = '''# MichiTheCat-RedStar (c) 2026\n# <|NAME|>\n
from zlib import decompress\n
with open(\'<|NAME|>\', \'wb\') as f: f.write(decompress(<|CONTENT|>))'''
	
	p = Path(path)
	
	if not p.exists():
		raise FileNotFoundError('Нет такого файла!')
	elif not p.is_file(): #NOTE: Изначально было is_dir, но вспомнил, что
		raise IsADirectoryError('Указан не файл!') # есть не только папки
	
	content = Path(p).read_bytes()
	compressed = compress(content, level=9)
	
	name = p.name
	
	result = blueprint.replace('<|NAME|>', name).replace('<|CONTENT|>', str(compressed))
	
	if is_object:
		with open(f'{name}.py', 'w', encoding='utf-8') as f: f.write(result)
		return 'Успешно!'
	else:
		return result


#TEST
if __name__ == '__main__':
	if not argv[1:]:
		PArch(input('Укажите путь: '), True)
	else:
		with open('a.py', 'w', encoding='utf-8') as f: f.write(PArch(argv[1]))


#TODO: Не стоит переживать, будут правки
