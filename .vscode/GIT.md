깃 허브 사용시 주의 사항 기재

1. 프로젝트의 기여(contributions) 표시 되게 반영하기
    1) 깃 허브에 로그인후 우측상단의 원 아이콘 클릭
        your profile을 클릭해서 등록되어있는 이름과 메일주소를 확인
        
    2) github에 등록된 이름과 email주소와 local에 등록한 이름과 email을 확인한다.

        a. local에 등록된 내용 설정하기
        terminal에서 git config --list로 설정된 이름과 메일주소를 확인

        b. 아래와 같이 github의 메일주소와 이름을 설정
           git config user.email "내 이메일 주소"
           git config user.name "내 이름"
        
        c.설정된 이름과 메일주소를 확인
           git config --list
          
 
    3) github로 부터 프로젝트 다운로드 하기 
        Your repositories에서 작업하고자하는 프로젝트를 클릭
        Code를 눌러서 Clone으로 복사를한다.

        vscode의 경우 
            f1키로 명령창을 활성화 시킨후 
            git:clone을 입력하고, 위의 github에서 복사한 URL을 붙여넣어 준다.
    
    4) 작업을 마친후에는 프로젝트를 커밋(추가설명포함), 푸시를 진행하여 깃허브에 제대로 반영되었는지를 확인해준다.

    5) 중요한 contributions에도 표시되어 잔디가 심어지는지 확인할 것