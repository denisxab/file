


# Что это ?
Это встраемовая библиотека для работы с 
файлами формата 
- txt = [TxtFile](##TxtFile)
- csv = [CsvFile](##CsvFile)
- json = [JsonFile](##JsonFile)
- pick = [PickleFile](##PickleFile)
- SqlLite = [SqlLiteQrm](##SqlLiteQrm)



# Описание функционала библиотеки

## TxtFile
Сначала создаем экземпляр класса `TxtFile` а потом работаем с его методами
```python
txt_obj = TxtFile("test.txt")
```
---
- `readFileToResDict(*args: str, separator: str = '\n')-> Dict[str, str]` = Считывает файл и возвращает Dict
с ключами заданными в параметры `*args` разграничение происходит по параметру 
`separator`
> Пример
```python
txt_obj.writeFile("my name\nmy passwd\nmy token")
res = txt_obj.readFileToResDict("name", "passwd", "token")
assert res == {'name': 'my name', 'passwd': 'my passwd', 'token': 'my token'}
```
---
- `readFile(limit: int = 0, *, encoding: str = None)-> str` = Обычное чтение `.txt` файла.
Можно указать лимит по чтение строчек `limit`. И кодировку чтения `encoding` значения такие же как и 
стандартной функции `open()`
> Пример
```python
test_text = "123123\n3123133\n12312d1d12313"
txt_obj.writeFile(test_text)
assert txt_obj.readFile(limit=2) ==  "123123\n3123133\n"
```
---
- `searchFile(name_find:str) -> bool` = Поиск слова `name_find` в тексте
> Пример
```python
test_text = "Optional. If the number of \n bytes returned exceed the hint number, \n no more lines will be returned. Default value is  -1, which means all lines will be returned."
txt_obj.writeFile(test_text)
assert txt_obj.searchFile("more") ==  True
```
---
- `readBinaryFile()->bytes` = Чтение бинарного файла
> Пример
```python
test_str = '123'
txt_obj.writeBinaryFile(test_str.encode())
assert test_str.encode() ==  txt_obj.readBinaryFile()
```
---
- `writeFile(data:str)` = Запись в тактовом режиме
---
- `appendFile(data: str)` = Добавление в текстовом режиме
---
- `writeBinaryFile(data: Union[bytes, memoryview])` = Запись в бинарном режиме
---
- `appendBinaryFile(data: bytes)` = Добавление данных в бинарный файл
---



## CsvFile
Сначала создаем экземпляр класса `CsvFile` а потом работаем с его методами
```python
json_obj = CsvFile("test.csv")
```



- `readFile`

- `readFileAndFindDifferences`




## JsonFile
Сначала создаем экземпляр класса `JsonFile` а потом работаем с его методами
```python
json_obj = JsonFile("test.json")
```

---
- `readFile()` = Чтение данных из файла
---
- `writeFile(data: Union[List, Dict], *, indent=4, ensure_ascii: bool = False)` = Запись данных в файл, входные 
параметры такие же как у стандартной функции `open()`
---
- `appendFile(data: Union[List, Dict], *, ensure_ascii: bool = False)` = Добавить данные в файл
```python
# List
tempers: List = [1,2,3,4]

json_obj.writeFile(tempers)
json_obj.appendFile(tempers)

tempers += tempers
assert tempers == json_obj.readFile()

# Dict
tempers: Dict = {'1':11,'2':22,'3'::33}  # Все ключи должны быть типа str

json_obj.writeFile(tempers)
json_obj.appendFile(tempers)

tempers.update(tempers)
assert tempers ==  json_obj.readFile()
```
---

## PickleFile


## SqlLiteQrm










