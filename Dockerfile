FROM pytorch/torchserve
USER root
RUN apt update && apt install libpq-dev -y
# RUN useradd -ms /bin/bash flask_user
# USER flask_user
WORKDIR /app
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY . .
RUN mkdir uploaded_imgs
RUN pip3 install -r requirements.txt
CMD ["flask", "run", "--cert=cert/fullchain.pem", "--key=cert/privkey.pem"]
EXPOSE 5000
