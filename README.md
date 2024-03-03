# QA.GURU | Python | Автоматизация тестирования 10 поток
### Table of contents  
[]()
[Lesson 7: Working with files](https://school.qa.guru/pl/teach/control/lesson/view?id=314614372)

[Lesson 8: Python Basics. OOP](https://school.qa.guru/pl/teach/control/lesson/view?id=320830619)

[Lesson 9: Allure report](https://school.qa.guru/pl/teach/control/lesson/view?id=321205612)

[Lesson 10: Page object:](https://school.qa.guru/pl/teach/control/lesson/view?id=321374863)  
    [Lesson 10: Homework  mid-level-step-objects](https://github.com/svmyhome/demoqa10-e2e-tests/tree/lesson_10_mid-level-step-objects)  
    [Lesson 10: Homework high-level-step-objects](https://github.com/svmyhome/demoqa10-e2e-tests/tree/lesson_10_high-level-step-objects)  
    [Lesson 10: HomeWork application-manager](https://github.com/svmyhome/demoqa10-e2e-tests/tree/lesson_10_application-manager)  

[Lesson 11: Page object:](https://school.qa.guru/pl/teach/control/lesson/view?id=321671178)  

[Lesson 12: Jenkins First Task:](https://school.qa.guru/pl/teach/control/lesson/view?id=321892208)    

[Lesson 13: Jenkins run witn parameters:](https://school.qa.guru/pl/teach/control/lesson/view?id=322004438)    
### Hot keys pyCharm
Alt + shift + E в режиме дебага выполнить одну строку

### Зафризить форму
остановка JavaScripts or перейти в настройки хром три точки->More tools->Rendering->Emulate a focuse page
setTimeout(()=> { debugger; }, 2000);

### CSS

выбор одного из нескольких классов
[class~=react-datepicker__year-select] OR .react-datepicker__year-select

выбор нескольких классов
.react-datepicker__day--025.react-datepicker__day--weekend


### Python commands
python3 -m venv .venv - создает виртуальное окружение через коммандную строку source .venv/bin/activate - активирует виртуальное окружение

### Work with files

### Allure report

The Allure report did not generate a report if run locally. But this script generates local allure reports with history trends.
https://github.com/aleksandr-kotlyar/local-allure-history-trends-bash

Дополнительная библиотека 
bash allure_generate.sh tests/allure-results/

allure open allure

### Pydantic
берет данные из .env если файла нет не ругается, а берет из самого pydentic определенного в project.py
как запускать из строки  
base_url='https://google.com/' timeout='10.0' pytest tests  
driver_name=firefox pytest tests  
env -S 'driver_name=firefox' pytest tests  
context=stage pytest tests  

### Jenkins

Execute shell
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install
pytest .
```
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install
pytest ${TEST_FOLDER} --browser_version=${BROWSER_VERSION}
```

pytest tests/ --browser_version=99
