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
- OS: ubuntu 16.04
- Container: Docker
- SSL Certificate
- LDAP: Azure Active Directory Domain Service (Active Directory 상관없음)

## 사용하는 이유
<script src="https://unpkg.com/mermaid@8.0.0/dist/mermaid.min.js"></script>
<div class="mermaid">
graph LR
    AWS --> CloudWatch
    On-premise --> Telegraf.
    Telegraf. --> Influxdb.
    CloudWatch -->|AccessKey| Influxdb.
    Influxdb. --> Grafana.
</div>

## Objects
1.[Grafana Installing](https://grafana.com/docs/installation/debian/)

- apt-get 패키지 설정
```bash
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
curl https://packages.grafana.com/gpg.key | sudo apt-key add -
```
- Install
```bash
sudo apt-get update && sudo apt-get install grafana
```
- 설정
```bash
systemctl daemon-reload # 설정 반영
systemctl start grafana-server
systemctl status grafana-server
systemctl enable grafana-server.service # 부팅시 활성화
```
- 웹페이지
    - http://34.220.10.205:3000/login
    - ID, PW : admin/admin

2.[Influxdb Installing](https://docs.influxdata.com/influxdb/v1.7/introduction/installation/)
- apt-get 패키지 설정
```bash
curl https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/lsb-release
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
```
- Install
```bash
sudo apt-get update && sudo apt-get install influxdb
```
- 설정
```bash
systemctl start influxdb
systemctl status influxdb
systemctl enable influxdb
```

3.[Telegraf Installing](https://www.influxdata.com/get-influxdb/)
- Download ~~(모니터링 대상 서버의 패키지 관리를 위해 다운로드 형식으로 진행)~~ 
```bash
wget https://dl.influxdata.com/telegraf/releases/telegraf_1.12.2-1_amd64.deb
```
- Install
```bash
sudo dpkg -i telegraf_1.12.2-1_amd64.deb
```
- 설정
```bash
systemctl start telegraf
systemctl status telegraf
systemctl enable telegraf
```

4.[CloudWatch Setup](https://grafana.com/docs/features/datasources/cloudwatch/)
- Setup-Policy (AWS > IAM > Policies > Create policy > JSON)
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowReadingMetricsFromCloudWatch",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:DescribeAlarmsForMetric",
                "cloudwatch:ListMetrics",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:GetMetricData"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowReadingTagsInstancesRegionsFromEC2",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeTags",
                "ec2:DescribeInstances",
                "ec2:DescribeRegions"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowReadingResourcesForTags",
            "Effect" : "Allow",
            "Action" : "tag:GetResources",
            "Resource" : "*"
        }
    ]
}
```
- Setup-Access Key (AWS > IAM > User >)
    - Access Type: Programmatic access
    - Set permissions: Attach existing policies directly
    - Filter policies: 1번에서 생성한 Policy Name 등록
    - Create User: Download.csv (credentials.csv)

## Controller
**[Grafana Datasources Setup](https://grafana.com/docs/features/datasources/) & Monitoring Agent(Telegraf)**

> **Influxdb Config Setup** (/etc/influxdb/influxdb.conf)
```conf
[http]
  enabled = true # 활성화
  bind-address = ":8086" # 활성화
```
> Grafana 웹페이지 > datasources > Add data source
![influxdb](/assets/images/post/2019/datasources-influxdb.png)
HTTP (localhost = Public IP(34.220.10.205))
![influxdb2](/assets/images/post/2019/influxdb-http.png)
Database (기본 설정 사용 패스워드 미 설정)
![influxdb3](/assets/images/post/2019/influxdb-batabase.png)

> **CloudWatch Setup** (AWS AccessKey)
<br>
Grafana 웹페이지 > datasources > Add data source
![datasources](/assets/images/post/2019/cloudwatch-data.png)
AccessKey 등록
![datasources2](/assets/images/post/2019/cloudwatch-data-2.png)

> **Telegraf Setup** (/etc/telegraf/telegraf.conf)
<br>
```conf
[[outputs.influxdb]]
  urls = ["http://34.220.10.205:8086"] # 활성화
  database = "telegraf" #활성화
```
```bash
systemctl restart telegraf
systemctl status telegraf
```

## Monitoring Dashboard Setup
**[Grafana Dashboard](https://grafana.com/grafana/dashboards)**

- Telegraf Dashboard
Grafana 웹페이지 > Dashboards > Import
![Dashboard3](/assets/images/post/2019/cloudwatch-id-1.png)
- ID는 위의 Grafana Dashboard URL에서 마음에 드는 Dashboard 찾아서 입력<br>
(블로그에서 사용하는 [Dashboard 링크](https://grafana.com/grafana/dashboards/1375))
![Dashboard4](/assets/images/post/2019/Telegraf-id-1.png)
    - Name/Folder/Unique identifier (uid): 임의 지정
    - servermonitor: InfluxDB

- 커뮤니티 Dashboard를 적용하여 표현
![Dashboard5](/assets/images/post/2019/linux-Dashboard.png)

- AWS-CloudWatch Dashboard
Grafana 웹페이지 > Dashboards > New dashboard > Add Query
![Dashboard1](/assets/images/post/2019/cloud-ec2.png)
    - Query: CloudWatch
    - Region: 사용하는 리전 지정
    - Metric: 확인하고 싶은 매트릭 지정
    - Dimensions: InstanceId = 타겟-InstanceId

- 다양한 차트로 표현
![Dashboard1](/assets/images/post/2019/grafana-cloud2.png)

## Conclusion
설치 명령어 10줄 정도와 설정 파일 내용을 한두 번 변경하면서 AWS & On-premise 모두를 모니터링할 수 있는 환경의 기초를 마련했습니다. 지금 보여드린 부분은 Grafana, Influxdb, Telegraf, CloudWatch 기능에 극히 일부분 및 모니터링 구성에서 보안 요구 사항이 전혀 반영되지 않은 설정이지만 위와 같이 최대한 간결하게라도 구성을 경험하는데 취지를 두고 작성하였습니다.:smiley:
<br>
<br>
다음 포스팅 내용은 아래의 내용들을 정리해서 포스팅 하겠습니다.
- CloudWatch Custom Metric
- Telegraf Plugins
- Granafa & Influxdb 최적화
