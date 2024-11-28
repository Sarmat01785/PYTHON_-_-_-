## Импорт модулей и специальная конструкция 


```python
if __name__ == '__main__'
```

Импортирование модулей в Python позволяет использовать функциональность, предоставленную другими модулями. Это могут быть стандартные библиотеки Python, сторонние пакеты или ваши собственные модули.

### Команда `dir()`
Команда `dir()` используется для получения списка всех атрибутов объекта или имен, доступных в текущем локальном пространстве имен.


```python
x = 7
print(dir())  # Выведет список имен, определенных в текущем пространстве имен
```

    ['In', 'Out', '_', '_1', '_2', '_3', '_4', '_5', '_6', '_7', '__', '___', '__builtin__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__pandas', '__session__', '__spec__', '_dh', '_i', '_i1', '_i2', '_i3', '_i4', '_i5', '_i6', '_i7', '_i8', '_ih', '_ii', '_iii', '_oh', 'dataframe_columns', 'dataframe_hash', 'dtypes_str', 'exit', 'get_dataframes', 'get_ipython', 'getpass', 'hashlib', 'import_pandas_safely', 'is_data_frame', 'json', 'open', 'quit', 'x']
    

### Команда `help()`
Команда `help()` предоставляет справочную информацию по модулям, ключевым словам, атрибутам или любым другим объектам.


```python
print(help('modules'))  # Выведет список доступных модулей
```

    
    Please wait a moment while I gather a list of all available modules...
    
    

    C:\Users\Sarmat\anaconda3\Lib\pkgutil.py:92: DeprecationWarning: `torch.distributed._shard.checkpoint` will be deprecated, use `torch.distributed.checkpoint` instead
      __import__(info.name)
    C:\Users\Sarmat\anaconda3\Lib\pkgutil.py:92: DeprecationWarning: `torch.distributed._sharded_tensor` will be deprecated, use `torch.distributed._shard.sharded_tensor` instead
      __import__(info.name)
    C:\Users\Sarmat\anaconda3\Lib\pkgutil.py:92: DeprecationWarning: `torch.distributed._sharding_spec` will be deprecated, use `torch.distributed._shard.sharding_spec` instead
      __import__(info.name)
    C:\Users\Сармат\AppData\Roaming\Python\Python311\site-packages\torch\distributed\algorithms\_optimizer_overlap\optimizer_overlap.py:12: DeprecationWarning: `TorchScript` support for functional optimizers is deprecated and will be removed in a future PyTorch release. Consider using the `torch.compile` optimizer instead.
      from torch.distributed.optim import as_functional_optim
    W1128 11:13:44.094000 7760 AppData\Roaming\Python\Python311\site-packages\torch\distributed\elastic\multiprocessing\redirects.py:29] NOTE: Redirects are currently not supported in Windows or MacOs.
    C:\Users\Sarmat\anaconda3\Lib\site-packages\_yaml\__init__.py:18: DeprecationWarning: The _yaml extension module is now located at yaml._yaml and its location is subject to change.  To use the LibYAML-based parser and emitter, import from `yaml`: `from yaml import CLoader as Loader, CDumper as Dumper`.
      warnings.warn(
    C:\Users\Sarmat\anaconda3\Lib\site-packages\clyent\__init__.py:5: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
      import imp
    C:\Users\Sarmat\anaconda3\Lib\site-packages\conda_token\repo_config.py:14: PendingDeprecationWarning: conda.cli.python_api is pending deprecation and will be removed in 24.9. Use `conda.testing.conda_cli` instead.
      from conda.cli.python_api import Commands, run_command
    WARNING: AstropyDeprecationWarning: The private astropy._erfa module has been made into its own package, pyerfa, which is a dependency of astropy and can be imported directly using "import erfa" [astropy._erfa]
    

### Модуль `sys`
Модуль `sys` содержит различные системные функции и атрибуты, такие как пути поиска модулей, аргументы командной строки и многое другое.


```python
import sys

print(sys.path)  # Выведет список путей, где Python ищет модули при их импорте
```

    ['C:\\Users\\Сармат', 'C:\\Users\\Sarmat\\anaconda3\\python311.zip', 'C:\\Users\\Sarmat\\anaconda3\\DLLs', 'C:\\Users\\Sarmat\\anaconda3\\Lib', 'C:\\Users\\Sarmat\\anaconda3', '', 'C:\\Users\\Сармат\\AppData\\Roaming\\Python\\Python311\\site-packages', 'C:\\Users\\Sarmat\\anaconda3\\Lib\\site-packages', 'C:\\Users\\Sarmat\\anaconda3\\Lib\\site-packages\\win32', 'C:\\Users\\Sarmat\\anaconda3\\Lib\\site-packages\\win32\\lib', 'C:\\Users\\Sarmat\\anaconda3\\Lib\\site-packages\\Pythonwin']
    


```python
# Конструкция if __name__ == '__main__'
Эта специальная конструкция используется для определения, выполняется ли модуль как основной скрипт или он был импортирован в другой модуль.
```


```python
if __name__ == '__main__':
    # Этот блок кода будет выполнен только тогда, когда файл запущен непосредственно,
    # а не импортирован в качестве модуля.
    print('Файл запущен напрямую, а не импортирован.')
```

    Файл запущен напрямую, а не импортирован.
    

### Применение конструкции if __name__ == '__main__'
Когда вы импортируете данный скрипт в другой модуль, код в блоке if __name__ == '__main__' не будет выполнен. Эта конструкция полезна для написания тестов или инициализации программы, которая должна выполниться только при непосредственном запуске модуля.

### Примеры использования

#### Пример 1: Простое тестирование модуля

Предположим, у вас есть функция, которую вы хотите протестировать перед интеграцией в проект. Вы можете поместить тестовый код в блок if __name__ == '__main__'.


```python
def add(a, b):
    """Функция для сложения двух чисел."""
    return a + b

if __name__ == '__main__':
    result = add(2, 3)
    print(result)  # Выведет 5
```

    5
    

#### Пример 2: Запуск основного приложения

Вы можете использовать конструкцию if __name__ == '__main__', чтобы определить точку входа в ваше приложение.


```python
def main():
    print("Приложение запущено.")

if __name__ == '__main__':
    main()
```

    Приложение запущено.
    

### Заключение

Конструкция if __name__ == '__main__' — мощный инструмент для организации кода в Python. Она помогает разделить логику исполнения и тестирования, обеспечивая чистоту и удобство разработки.
