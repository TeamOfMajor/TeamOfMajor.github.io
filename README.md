# teamofmajor.github.io

## **깔끔한 commit history 관리를 위해 `Squash Merge`를 사용해 주세요.**

## 글쓰기 방법

#### 1. 로컬에 [Jekyll](https://jekyllrb.com/docs/)를 설치 하는 경우
글 수정 후 확인은 로컬에 설치된 Jekyll을 이용해서 바로 확인 할 수 있습니다.
  - 이 [Repository](https://github.com/teamofmajor/teamofmajor.github.io)를 바로 clone 해서 사용.
  - `feature/<id>-*` 브랜치 생성 후 작업 -> PR 생성 -> `Squash Merge`
  - PR 생성

#### 2. Jekyll을 설치 하지 않고 하는 경우
Jekyll을 로컬에 설치 하지 않은 경우 github의 `master branch에 push`해야 합니다. 이 경우 `작성 중인 글이 사이트에 노출` 되고 `commit history 가 지저분`해지는 문제가 있으므로 아래 방법으로 진행 하시길 추천 드립니다.

**예시는...`moon-tae-kwon` ID로 `feature/taekwon-readme` 브랜치로 작업한 예시입니다.**

  - 이 [Repository](https://github.com/teamofmajor/teamofmajor.github.io)를 본인의 계정으로 `fork` 합니다.
  - `fork 한 본인 계정의 Repository`의 `Settings`에서 `Repository name`을 수정합니다.
    - `moon-tae-kwon.github.io`로 변경.
    - 변경 하고 잠시 후 (1~2분?) `https://moon-tae-kwon.github.io`로 접속하면 사이트가 열립니다.
  - Fork 받은 본인의 Repository를 clone 합니다.

    ```
    $ git clone git@github.com:moon-tae-kwon/moon-tae-kwon.github.io.git
    ```
  
  - `feature/taekwon-readme` 브랜치 생성, checkout, push

    ```
    $ git branch feature/taekwon-readme
    $ git checkout feature/taekwon-readme
    $ git push -u origin feature/taekwon-readme
    ```

  - 이제 clone 받은 소스의 `_posts` 디렉토리에 post를 생성 합니다.
    - 파일명은 `YYYY-MM-DD-<post-name>.md`로 합니다.
    - 본분을 html로 작성할 경우 `.html`도 사용 할 수 있습니다.

  - 수정 한 글을 사이트에서 확인 하려면 master branch에 push 합니다.
    - 원본 [Repository](https://github.com/teamofmajor/teamofmajor.github.io)로의 PR을 만들기 위해 수정은 생성한 `feature/taekwon-readme` branch에서 진행 하고 수정사항 확인을 위해 master branch에 merge 합니다. 

  ```
  $ git add .
  $ git commit -m 'readme 작성중'
  $ git push
  $ git checkout master
  $ git merge feature/taekwon-readme
  $ git push
  $ git checkout feature/taekwon-readme
  ```

  - master branch에 변경사항이 push 되면 1~2분 이내에 수정사항이 반영 되었다고 메일이 옵니다.
  - post가 완성되면 원본 [Repository](https://github.com/teamofmajor/teamofmajor.github.io)로 PR을 생성합니다. (자신의 계정 PR 탭에서 진행)
    - PR(Pull Request)를 생성할때 from / to는 아래와 같이 설정 합니다.
        - base repository: teamofmajor/teamofmajor.github.io
            - base: master
        - head repository: moon-tae-kwon/moon-tae-kwon.github.io
            - compare: feature/taekwon-readme

  - **PR 생성 후 Merge 시에는 `Squash and merge`를 선택해서 Merge 합니다.**


## 글 작성 팁

#### 1. `subtitle` 설정 하기
  - subtitle를 설정하지 않으면 글 목록에 본문의 앞 몇글자를 잘라서 보여 주게 됩니다.
  - subtitle를 사용하면 글 목록에 노출 되기 원하는 문구를 별도로 지정 가능합니다.

#### 2. 상단 배너 이미지 넣기
  - `https://unsplash.com`에서 적절히 고릅니다. (저작권 고민안하고 써도 되는 이미지 사이트 입니다.)
  - 다운받은 후 `/assets/images/`에 넣고 `background`에 경로를 적습니다.
  - (선택) Download시 나오는 `Photo by *** on Unsplash` 문구를 Post 상단에 넣습니다.
    - 예시 입니다. href의 링크는 적절히 수정해서 사용합니다.
    
    ```html
    <div class="photo-copyright">
    Photo by <a href="https://unsplash.com/@zhenhu2424?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Zhen Hu</a> on <a href="https://unsplash.com/search/photos/lock?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
    </div>
    ```

#### 3. [mermaid.js](https://mermaidjs.github.io/#/) 사용하기
  * Text를 이용해 다이어그램을 그릴 수 있습니다. 
  * Flowchart / Sequence diagrams을 그릴 수 있습니다.
  * 아래 예시 처럼 `<div class="mermaid">`를 본문에 사용하시면 됩니다.

```
{% mermaid %}
graph LR
    A --> B
    B --> C
    C --> D
    D -->|AccessKey| C
    D --> A
{% endmermaid %}
```

#### 4. 글 주제 팁
1. 프레임워크나 라이브러리에서 새롭게 알게 된 사용방법
2. 프로그램 등의 설치 및 설정 방법
3. 좋은 글을 보면 (허락하에) 번역
4. 새로 등장한 기술을 공부하고 그 내용을 정리
5. 겪은 오부류의 해결 방법
6. 책이나 세미나에 대한 후기

#### 5. 글 내용 팁
1. 이 글에서 다루는 문제는 무엇인가요?
2. 이 글을 작성하는 이유는? 이 글을 보는 독자가 얻을 수 있는 내용은?
3. 문제에 대한 해결 방안
4. 해결 후, 남은 이슈는 있나요?
5. 또 어떤 것을 고민해보면 좋을까요?
6. 참고 자료(Reference)

#### 6. 글 작성 팁
1. 초안을 수정없이 작성한다.
2. 초안 작성 이후에 이글을 통해서 설명하려고 하는 부분이 설명 되었는지 확인한다.
3. 리뷰어가 검토하게 될 내용을 생각하고 수정한다.
4. 독자의 입장에서 검토하고, 전문 지식이 없어도 쉽게 이해 할수 있도록 신경 쓴다.

#### 7. 리뷰 지침
1. 오타는 없는가?
2. 글 전개 방식은 자연스러운가?
3. 가독성(글 & 이미지)