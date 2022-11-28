FROM python:3.9-slim
ARG buildenv
ENV PYTHONDONTWRITEBYTECODE 1

COPY . .

RUN pip install -r requirements.txt && \
    if [ "$buildenv" = "local" ]; then pip install -r requirements_local.txt; fi

CMD ["./run.sh"]