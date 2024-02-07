FROM python:3.11-bookworm

LABEL "Automation"="Python with my framework"

WORKDIR /HillelQAPython

COPY . .

RUN pip3 install -r requirements.txt
RUN pip install -e .


CMD pytest -v HillelQAPython/tests_for_api/*