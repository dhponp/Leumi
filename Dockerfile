FROM alpine:3.14

RUN apk add --no-cache python3 py3-pip

WORKDIR /home

COPY HiLeumi.py ./

ENV exparam hi 

CMD ["sh", "-c", "python3 HiLeumi.py ${exparam}"]