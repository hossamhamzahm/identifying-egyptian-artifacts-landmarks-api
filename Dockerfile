FROM pytorch/torchserve
WORKDIR /app
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY . .
RUN mkdir uploaded_imgs
RUN pip3 install -r requirements.txt
CMD ["flask", "run"]
EXPOSE 5000