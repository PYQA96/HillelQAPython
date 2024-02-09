FROM python:3.11-bookworm

LABEL "Automation"="Python with my framework"

WORKDIR /HillelQAPython


RUN pip3 install -r requirements.txt

COPY . .

CMD pytest -v HillelQAPython/tests_for_api