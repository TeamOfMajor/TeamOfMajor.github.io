---

layout: single

title: Monitoring With AWS & On-premise (Influxdb, Telegraf, CloudWatch, Grafana) # 제목은 명확하고 간결하게 쓰기
excerpt: "아이언맨" # 작성자 닉네임(마블)
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
#  - Networking # 네트워킹
#  - DevOps # 데브옵스 환경 & 문화 안내
#  - IaC # 소스 코드를 통한 인프라 구성
  - OpenSource # 오픈 소스
#  - POC # 기술 검증 & 개념 검증
#  - BMT # 성능테스트
tags: 
  - Monitoring # 핵심 주요 단어
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

이 글을 작성하는 이유는? 이 글을 보는 독자가 얻을 수 있는 내용은?

# Monitoring With AWS & On-premise
> 지난 몇 년간 많은 Monitoring Tool을 사용해 오면서 그중 가장 간결하고, 빠르게 적용 할 수 있는 Monitoring Tool([Influxdb](https://www.influxdata.com/), [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/), [CloudWatch](https://aws.amazon.com/ko/cloudwatch/), [Grafana](https://grafana.com/))을 소개하고 **AWS**와 **On-premise**의 통합 모니터링 사이트 구축 방법을 공유하기 위해서 작성하였습니다.

[MIT License](https://www.olis.or.kr/license/Detailselect.do?lId=1006&mapCode=010006)

## Monitoring Tool
1. Influxdb
    - Go 언어로 작성되어 외부 의존성이 없습니다.
    - 다양한 API, HTTP(S)를 제공한다.
    - 시계열 데이터베이스로 시간 순서에 따라 저장하고 조회하는 기능으로 인해 실시간 비교가 필요한 모니터링에 적합합니다.
2. Telegraf
    - Go 언어로 작성되어 외부 의존성이 없습니다. (Influxdb와 동일한 업체에서 개발)
    - 다양한 매트릭을 수집하여 데이터베이스로 보내는 에이전트입니다.
    - 다양한 메트릭을 수집하기 위해 수많은 In-Out Put 플러그인을 제공합니다.
3. CloudWatch
    - AWS에서 운영되고 있는 서비스를 모니터링을 할 수 있게 해주는 서비스입니다.
    - 별도의 CloudWatch Agent를 다운받아서 On-premise에서 운영이 가능합니다.
    - 별도 다운받아 사용 할 수 있듯 커스텀 매트릭 설정이 가능합니다.
4. Grafana
    - 수집된 매트릭에 대한 자료를 한눈에 볼 수 있도록 시각화를 지원합니다.
    - 수많은 대시보드 템플릿 및 데이터 소스(Influxdb, CloudWatch, ETC.)를 지원합니다.

## Monitoring Flowchart
{% mermaid %}
graph LR
    AWS --> CloudWatch
    On-premise --> Telegraf.
    Telegraf. --> Influxdb.
    CloudWatch -->|AccessKey| Influxdb.
    Influxdb. --> Grafana.
{% endmermaid %}

## Monitoring Installation