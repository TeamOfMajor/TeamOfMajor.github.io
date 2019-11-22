---

layout: single

title: rocketchat # 제목은 명확하고 간결하게 쓰기
excerpt: "블랙위도우" # 작성자 닉네임(마블)
search: true
categories: # 작성 글 형식 내용에서 맞게 아래 주석에서 최대 2개 선택
#  - Study # 새롭게 알게 된 내용
  - Tutorial # 프로그램 등의 설치 및 설정 방법
#  - Reviews # 책이나 세미나에 대한 후기
#  - Issue # 새로 등장한 기술을 공부하고 그 내용을 정리
#  - News # 새로 등장한 기술을 공부하고 그 내용을 정리
#  - Error # 겪은 오부류의 해결 방법
#  - Translation # 좋은 글을 보면 (허락하에) 번역
#  - Cloud # 클라우드 서비스
#  - Certificate # 자격증
#  - Networking # 네트워킹
  - App # 어플리케이션
#  - DevOps # 데브옵스 환경 & 문화 안내
#  - IaC # 소스 코드를 통한 인프라 구성
  - OpenSource # 오픈 소스
#  - POC # 기술 검증 & 개념 검증
#  - BMT # 성능테스트
tags: 
  - rocketchat # 핵심 주요 단어
toc: true
comments: true

# Emoji 단축키 (https://gist.github.com/rxaviers/7360908)
# Maerdown 설명-1 https://gist.github.com/ihoneymon/652be052a0727ad59601
# Maerdown 설명-2 https://heropy.blog/2017/09/30/markdown/

# -- 블로그 글위에 색상 추가
xcerpt: "This post should display a **header with a solid background color**, if the theme #supports it."
header:
  overlay_color: "#333"

## -- 블로그 글위에 이미지 추가
#header:
#  image: https://cdn.pixabay.com/photo/2019/06/27/06/49/plane-4301615_1280.png

## -- 블로그 글위에 색상 추가
#xcerpt: "This post should display a **header with a solid background color**, if the theme #supports it."
#header:
#  overlay_color: "#333"

## -- 블로그 글위에 배경 추가 및 링크 추가
#xcerpt: "This post should [...]"
#header:
#  overlay_image: /assets/images/unsplash-image-1.jpg
#  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
#  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
#  actions:
#    - label: "Download"
#      url: "https://github.com"

---
# Rocketchat
> 많이 사용하는 Slack 형태의 중-소규모 그룹을 위한 오픈소스 **메신저 서버/클라이언트 프로그램**입니다. 
실시간 채팅을 할 수 있고, 음성과 화상채팅도 가능합니다. 
다양한 서버 OS를 지원하고 있으며, Client 프로그램으로는 PC(Windows,macOS,Linux) 와 Mobile App(iOS,Android) 을 지원하고 있습니다.


## 장점
- Open Source 기반이라 무료로 사용이 가능
- Custom 개발을 통하여 기능 향상 가능
- Container 지원
- 계정연동 프로토콜 지원 LDAP , oAuth 등


## 구성환경
- Cloud: Azure (Azure AD 사용하기 위해 선택)
- OS: ubuntu 16.04
- Container: Docker
- SSL Certificate: 사용 (사용권장)
- DNS: Route 53
- WEB: nginx
- DB: mongo
- LDAP: Azure Active Directory Domain Service (Active Directory 상관없음)

## Architecture
<!-- ![rc_architecture](/assets/images/rc/1.png) -->
<img src="/assets/images/rc/1.png" width="70%" height="30%">  

## Rocket Chat Install 
1.[Docker](https://docs.docker.com/get-started/)

- hosts 추가
```bash
$ vi /etc/hosts
127.0.0.1    localhost.localdomain    localhost
127.0.0.1    azuretest.hooniworld.io  azuretest
```

- Docker-compose 다운로드 및 설치
```bash
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-Linux-x86_64" -o /usr/local/bin/docker-compose
$ chmod +x /usr/local/bin/docker-compose
$ sudo -i docker-compose --version
```

- 패키지 정보 업데이트 및 CA certificates 설치  
APT가 https로 동작할 수 있도록 설치
```bash
$ sudo apt-get update
$ sudo apt-get install apt-transport-https ca-certificates
```

- GPG key 추가
```bash
$ apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
$ vi /etc/apt/sources.list/docker.list (해당 파일이 없으면 생성)
deb https://apt.dockerproject.org/repo ubuntu-xenial main (내용 입력 후 저장)
```

- APT package index 업데이트
```bash
$ sudo apt-get update
```

- 오래된 저장소를 삭제
```bash
$ sudo apt-get purge lxc-docker
```

- 올바른 저장소에서 받은 지 검증
```bash
$ apt-cache policy docker-engine
```

- linux-image-extra 패키지를 설치
```bash
$ sudo apt-get install linux-image-extra-$(uname -r)
$ sudo apt-get update
```

- Docker engine 설치
```bash
$ sudo apt-get install docker-engine
```

- docker가 정상적으로 설치되었는지 확인
```bash
$ /etc/apt/sources.list.d# sudo docker run hello-world
sudo: unable to resolve host test-chat-imsi1
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
1b930d010525: Pull complete 
Digest: sha256:c3b4ada4687bbaa170745b3e4dd8ac3f194ca95b2d0518b417fb47e5879d9b5f
Status: Downloaded newer image for hello-world:latest
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

- Docker 서비스 시작 및 자동 시작 설정 
```bash
$ sudo service docker start
$ systemctl enable docker
```

2.nginx

- nginx 설치 
```bash
$ apt-get -y install nginx
$ service nginx start
$ systemctl enable nginx
$ ps -ef | grep nginx
root       3841      1  0 00:09 ?        00:00:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data   3844   3841  0 00:09 ?        00:00:00 nginx: worker process
```

- nginx 인증서 통합  
<u>※ 통합된 unified.pem 파일 편집기로 열어 PEM 내용간 구분되어 있는지 확인</u>
```bash
$ cat cert.pem > unified.pem 
$ cat chain.pem >> unified.pem 
또는
$ cat "서버인증서.pem" "체인인증서(모두).crt" "루트인증서.crt" > unified.pem
```

- nginx.conf (/etc/nginx/sites-available/default)  
```nginx
# HTTPS Server
    server {
        listen 443 ssl;
        server_name azuretest.hooniworld.io;
        error_log /var/log/nginx/rocketchat_error.log;
        ssl_certificate /etc/nginx/unified.pem;
        ssl_certificate_key /etc/nginx/certificate.key;
        #ssl_dhparam /etc/nginx/dhparams.pem;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';
        ssl_prefer_server_ciphers on;
        ssl_session_cache shared:SSL:20m;
        ssl_session_timeout 180m;

        location / {
            proxy_pass http://127.0.0.1:3000/;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forward-Proto http;
            proxy_set_header X-Nginx-Proxy true;
            proxy_redirect off;
        }
    }
# HTTP Server
    server {
        listen 80;
        server_name azuretest.hooniworld.io;
        return 301 https://$host$request_uri;
}
```

- nginx 설정 확인 및 재시작  
<u>※ restart 명령어는 프로세스를 재기동시키기 때문에 이미 들어온 요청들은 에러가 발생하지만 reload 명령어는 이미 들어온 요청들을 다 처리한 후에 새로운 프로세스를 생성하여 새로운 설정을 반영하게 됩니다</u>
```bash
$ nginx -t
$ nginx -s reload
```

3.RocketChat with mongoDB

- 디렉토리 생성
```bash
$ mkdir -p /var/www/rocket.chat/data/runtime/db
$ mkdir -p /var/www/rocket.chat/data/dump
```

- rocketchat yaml (/var/www/rocket.chat/docker-compose.yml)
```yaml
version: '2'
services:
  rocketchat:
    image: rocket.chat:latest
    command: bash -c 'for i in `seq 1 30`; do node main.js && s=$$? && break || s=$$?; echo "Tried $$i times. Waiting 5 secs..."; sleep 5; done; (exit $$s)'
    restart: unless-stopped
    volumes:
      - ./uploads:/app/uploads
    environment:
      - PORT=3000
      - ROOT_URL=http://azuretest.hooniworld.io
      - MONGO_URL=mongodb://mongo:27017/rocketchat
      - MONGO_OPLOG_URL=mongodb://mongo:27017/local
      - Accounts_UseDNSDomainCheck=ture
    depends_on:
      - mongo
    ports:
      - 3000:3000

  mongo:
    image: mongo:4.0
    restart: unless-stopped
    volumes:
     - ./data/db:/data/db
     - ./data/dump:/dump
    command: mongod --smallfiles --oplogSize 128 --replSet rs0 --storageEngine=mmapv1

  # this container's job is just run the command to initialize the replica set.
  # it will run the command and remove himself (it will not stay running)
  mongo-init-replica:
    image: mongo
    command: 'bash -c "for i in `seq 1 30`; do mongo mongo/rocketchat --eval \"rs.initiate({ _id: ''rs0'', members: [ { _id: 0, host: ''localhost:27017'' } ]})\" && s=$$? && break || s=$$?; echo \"Tried $$i times. Waiting 5 secs...\"; sleep 5; done; (exit $$s)"'
    depends_on:
      - mongo

  # hubot, the popular chatbot (add the bot user first and change the password before starting this image)
  hubot:
    image: rocketchat/hubot-rocketchat:latest
    restart: unless-stopped
    environment:
      - ROCKETCHAT_URL=52.141.37.59:3000
      - ROCKETCHAT_ROOM=GENERAL
      - ROCKETCHAT_USER=test
      - ROCKETCHAT_PASSWORD=testpassword
      - BOT_NAME=test
  # you can add more scripts as you'd like here, they need to be installable by npm
      - EXTERNAL_SCRIPTS=hubot-help,hubot-seen,hubot-links,hubot-diagnostics
    depends_on:
      - rocketchat
    volumes:
      - ./scripts:/home/hubot/scripts
  # this is used to expose the hubot port for notifications on the host on port 3001, e.g. for hubot-jenkins-notifier
    ports:
      - 3001:8080
```
  
## Conclusion
설치 명령어 10줄 정도와 설정 파일 내용을 한두 번 변경하면서 AWS & On-premise 모두를 모니터링할 수 있는 환경의 기초를 마련했습니다. 지금 보여드린 부분은 Grafana, Influxdb, Telegraf, CloudWatch 기능에 극히 일부분 및 모니터링 구성에서 보안 요구 사항이 전혀 반영되지 않은 설정이지만 위와 같이 최대한 간결하게라도 구성을 경험하는데 취지를 두고 작성하였습니다.:smiley:
<br>
<br>
다음 포스팅 내용은 아래의 내용들을 정리해서 포스팅 하겠습니다.
- CloudWatch Custom Metric
- Telegraf Plugins
- Granafa & Influxdb 최적화
