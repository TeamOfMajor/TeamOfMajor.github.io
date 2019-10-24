---

layout: single

title: Terraform Credentials # 제목은 명확하고 간결하게 쓰기
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
toc: true
comments: true

# Emoji 단축키 (https://gist.github.com/rxaviers/7360908)
# Maerdown 설명-1 https://gist.github.com/ihoneymon/652be052a0727ad59601
# Maerdown 설명-2 https://heropy.blog/2017/09/30/markdown/

# -- 블로그 글위에 색상 추가
xcerpt: "This post should display a **header with a solid background color**, if the theme #supports it."
header:
  #overlay_color: "#333"
  overlay_image: /assets/images/hannah-rodrigo-mf_3yZnC6ug-unsplash.jpg

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
> Terraform 경우 provider.tf 에서 인증처리를 하고 있으며, 인증을 받기 위해서는 Key 가 필요합니다. 
**AWS** 를 예로들면 Access Key 및 Secret Key 가 필요하며, 해당 Key는 노출이 되어서는 안됩니다.
노출될 경우 악의적인 사람들로 인하여 무분별하게 리소스를 생성하여 엄청난 비용이 추가 될 수 있습니다.
아래 내용은 **Terraform** 사용 시 코드에 Access Key 및 Secert Key 를 직접 쓰지 않고 파일 형태로 사용하는 내용 입니다.

## 사전조건
- Windows OS 환경에서 진행
- AWS CLI 설치 필요
    - OS 별 각각 AWS CLI 설치 방법이 다르며 링크 참조하여 설치 진행
    - [AWS CLI Install 참조 링크](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-chap-install.html)


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
- %UserProfile%\.aws\credentials (default 경로)
![Creden1](/assets/images/Creden/1.png)

- Config 파일은 Region 및 format 정보 저장
- Credentials 파일은 Access Key 및 Secret Key 정보 저장
![Creden2](/assets/images/Creden/2.png)


## Terraform Credentials 사용
- provider.tf 파일에 인증정보 입력
- profile 경우 입력을 하지 않으면 default로 저장되며 입맛에 맞게 변경하여 사용
```bash
provider "aws" {
	shared_credentials_file = "\Users\myunghoon.kim\.aws\Credentials"
	region = "ap-northeast-2"
	profile = "mhcred"
```
- provider.tf 파일 사용 예
![Creden3](/assets/images/Creden/3.png)
