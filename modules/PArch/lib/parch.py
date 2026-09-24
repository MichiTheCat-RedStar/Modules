# 	parch // ☭
# MichiTheCat-RedStar (c) 2026

from zlib import compress
from pathlib import Path
from sys import argv


def PArch(path:str) -> str:
	'Создать из файла python-код'
	
	# Теги шаблона:
	#  <|CONTENT|> - байт-контент
	#  <|NAME|>    - имя файла (с расширением)
	blueprint = '''# MichiTheCat-RedStar (c) 2026\n# <|NAME|>\n
from zlib import decompress\n
with open(\'<|NAME|>\', \'wb\') as f: f.write(decompress(<|CONTENT|>))'''
	
	p = Path(path)
	
	if not p.exists():
		raise FileNotFoundError('Нет такого файла!')
	elif not p.is_file():
		raise IsADirectoryError('Указан не файл!')
	
	content = Path(p).read_bytes()
	compressed = compress(content, level=9)
	
	name = p.name
	
	return blueprint.replace('<|NAME|>', name).replace('<|CONTENT|>', str(compressed))


#TEST
if __name__ == '__main__':
	if not argv[1:]:
		with open(f'{input("Укажите имя: ")}.py', 'w', encoding='utf-8') as f:
			f.write(PArch(input('Укажите путь: ').strip()))
	else:
		if Path(argv[1]).is_file():
			print(PArch(argv[1]))
		else:
			raise FileNotFoundError('Ошибка нахождения файла!')

