---
title:  Terraform With Windows 설치 # 주제
excerpt: "블랙위도우." # 닉네임(마블)
search: true
categories: 
  - Cloud   # 대분류
  - OpenSource     # 소분류
tags: 
  - Terraform # 핵심 주요 단어
toc: true
comments: true

last_modified_at: 2019-10-03T00:03:00+09:00
#last_modified_at: {{ page.last_modified_at | date: '%Y:%B:%A:%d:%S:%R' }}



## -- 블로그 글위에 이미지 추가
#header:
#  image: https://cdn.pixabay.com/photo/2019/06/27/06/49/plane-4301615_1280.png

## -- 블로그 글위에 색상 추가
#xcerpt: "This post should display a **header with a solid background color**, if the theme #supports it."
#header:
#  overlay_color: "#333"

# -- 블로그 글위에 배경 추가 및 링크 추가
xcerpt: "This post should [...]"
header:
  overlay_image: /assets/images/hannah-rodrigo-mf_3yZnC6ug-unsplash.jpg
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Download"
      url: "https://www.terraform.io/downloads.html"

---



## Terraform With Windows 설치

**Windows 에서 Terraform을 사용할 수 있는 방법입니다**


### Terraform 이란?
- hashicorp에서 오픈소스로 개발중인 인프라스트럭처 관리 도구 입니다
- 코드로써 IaC(Infrstructure as Code)를 지향하고 있는 도구 입니다
- GUI 및 Web Console 을 사용하지 않는 대신 코드로써 인프라를 관리할 수 있는 도구 입니다
- Cloud에 최적화 된 코드이며 AWS, Azure, GCP 등 모두 사용이 가능합니다
- Terraform 기능 및 설명에 대해서는 다음 주제에서 자세히 다룰 예정입니다

---

### 소개
- 아래 환경은 Windows 10 으로 진행 하였습니다
- Linux 및 Mac에서 설치는 따로 다루도록 하겠습니다
- 설치 방법은 간단하며 환경 변수를 지정하여 바로 실행이 가능합니다

---

### 설치방법

1. 로컬 디렉토리 생성
- C:\terraform 디렉토리 생성  


2. terraform.exe 다운로드  
- 상단 Download 링크를 통하여 Terraform.exe 다운로드  
<!-- ![screenshot](/assets/images/terraforminstall/1.png "width:200px;height:100px")  -->
<img src="/assets/images/terraforminstall/1.png" width="80%">  


3. 환경변수 등록   
- 내컴퓨터 > 고급시스템 속성 > 고급 > 환경변수  
<!-- ![screenshot](/assets/images/terraforminstall/2.png "width:250px;height:100px") -->
<img src="/assets/images/terraforminstall/2.png" width="75%">  

4. 환경변수 등록  
- 시스템 변수 > Path 편집  
<!-- ![screenshot](/assets/images/terraforminstall/3.png "width:300px;height:100px")   -->
<img src="/assets/images/terraforminstall/3.png" width="75%">  

5. Terraform 환경변수 등록  
- 새로만들기 > 설치경로 입력 "C:\terraform"  
<!-- ![screenshot](/assets/images/terraforminstall/4.png "width:250px;height:100px")   -->
<img src="/assets/images/terraforminstall/4.png" width="75%">  

6. 명령 프롬프트 실행하여 Terraform 실행  
- 테라폼에 대한 명령어를 확인 할 수 있습니다  
<!-- ![screenshot](/assets/images/terraforminstall/5.png "width:250px;height:100px")   -->
<img src="/assets/images/terraforminstall/5.png" width="75%">  

7. Terraform 초기화 진행  
- 테라폼 본체에 프로바이더들이 포함되어 있었지만 0.10 버전 부터
프로바이더가 플러그인으로 분리 되었습니다  
- 이에 따라 테라폼 프로젝트를 별도로 초기화할 필요가 있습니다  
- 테라폼은 테라폼 프로젝트를 초기화할 때 프로바이더 설정을 보고 필요한 플러그인을 설치 합니다  
- 여기까지 성공했다면 테라폼 사용준비가 완료된 상태입니다  
- "8"번 부터는 번외이니 참고만 하면 됩니다    
<!-- ![screenshot](/assets/images/terraforminstall/6.png "width:250px;height:100px")   -->
<img src="/assets/images/terraforminstall/6.png" width="75%">  

8. 환경변수 잡지 않고 사용할 때  
- 명령 프롬프트 관리자 권한 실행  
- set PATH=%PATH%;C:\terraform  
<!-- ![screenshot](/assets/images/terraforminstall/7.png "width:300px;height:100px")   -->
<img src="/assets/images/terraforminstall/7.png" width="75%">  

9. terraform 사용가능 여부 확인 
- terraform 명령어 실행 시 아래와 같이 나와야 합니다  
<!-- ![screenshot](/assets/images/terraforminstall/8.png "width:250px;height:100px")   -->
<img src="/assets/images/terraforminstall/8.png" width="75%">  

---
- <u>Terraform TIP</u>

```markdown
Terraform은 해당 디렉토리에 모든 .tf 파일을 읽음
**terraform plan**로 올바르게 코드가 작성되었는지 시뮬레이션 가능
- 미리 구성을 테스트 해 볼 수 있습니다.
- 실수로 인프라를 변경하지 않도록 확인이 가능
**terraform apply**로 적용
```