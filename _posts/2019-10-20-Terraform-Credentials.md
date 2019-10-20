---

layout: single

title: Terraform-Credentials # 제목은 명확하고 간결하게 쓰기
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
#  - App # 어플리케이션
#  - DevOps # 데브옵스 환경 & 문화 안내
#  - IaC # 소스 코드를 통한 인프라 구성
  - OpenSource # 오픈 소스
#  - POC # 기술 검증 & 개념 검증
#  - BMT # 성능테스트
tags: 
  - Terraform # 핵심 주요 단어
  - AWS Credentials
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
# Terraform Credentials
> Terraform 을 사용하기 위해서는 Cloud Platform 별로 Access Key가 필요합니다.
**AWS** 를 예로들면 Access Key 및 Secert Key 가 필요하며, 해당 Key는 노출이 되어서는 안됩니다.
노출될 경우 악의적인 사람들로 인하여 무분별하게 리소스를 생성하여 엄청난 비용이 추가 될 수 있습니다.
아래 내용은 **Terraform** 사용 시 코드에 Access Key 및 Secert Key 를 직접 쓰지 않고 파일 형태로 사용하는 내용 입니다.

## 사전조건
- Windows OS 환경에서 진행
- AWS CLI 설치 필요
    - OS 별 각각 AWS CLI 설치 방법이 다르며 링크 참조하여 설치 진행
    - https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-chap-install.html


## Credentials 등록
- 명령 프롬프트에서 아래와 같이 실행
```bash
C:\Users\user>aws configure
```
- Key 및 Region 등록
```bash
AWS Access Key ID [None]: AAAAAAAAAAAAAAA
AWS Secret Access Key [None]: AAAAAAAAAAAAAA
Default region name [ap-northeast-2]: ap-northeast-2 
Default output format [None]: 꼭 필요한 사항은 아니니 default 로 넘어가도 무방
```

## Credentials 확인
- 입력이 완료되었다면 아래 경로에 파일이 생성
- %UserProfile%\.aws\credentials (default)
![Dashboard3](/assets/images/Creden/1.png)

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

## Monitoring Setup
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