FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install selenium
RUN pip install Selenium-Screenshot
RUN pip install webdriver-manager

COPY . .

CMD [ "python", "./app.py" ]