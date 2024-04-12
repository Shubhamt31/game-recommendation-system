FROM python:3.12

ENV APP_HOME=/app
ENV APP_USER=runner

RUN groupadd -r $APP_USER && \
    useradd -r -g $APP_USER -d /home/$APP_USER -s /bin/bash -c "Docker image user" $APP_USER

RUN mkdir -p /home/$APP_USER && chown -R $APP_USER:$APP_USER /home/$APP_USER

WORKDIR $APP_HOME

RUN pip install --upgrade pip
RUN chown -R $APP_USER:$APP_USER $APP_HOME

USER $APP_USER

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="${PATH}:/app/.local/bin:/home/${APP_USER}/.local/bin"

COPY . .
EXPOSE 8000