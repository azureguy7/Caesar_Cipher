#Caesar Cipher

- 고전 암호 중에서 가장 간단하고 가장 널리 알려진 하나의 암호화 기법으로 단순 치환 암호
- Julius Caesar가 개인 서신에서 사용했다고 알려짐
- 카이사르 암호, 시저 암호, 시프트 암호, 시저의 코드, 서저 소프트라고도 불림.

## 시저 암호화 방법
- 말하고자 하는 알파벳의 고유 순서에서 일정한 간격으로 떨어진 순서의 알파벳을 암호로 표기해주는 방식
	- 일반문: abcdefghijklmnopqrstuvwxyz
	- 암호문: wxyzabcdefghijklmnopqrstuv
	i.e.
	- 일반문: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
	- 암호문: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD

## 시저 암호의 효과
- 시저 암호를 사용할 당시의 효과성은 알려져 있지 않음.
	- 다만, 시저의 적 대부분이 문맹이고, 외국어라고 오인했을 가능성이 있기 때문에 합리적인 수준에서 안전했을 거라 추정
	- 당시에는 단순 치환 암호를 푸는 기술에 대한 기록은 없음
	
## 시저 암호 해독
- 열심히 하면 되지 않겠습니까???
- 지속 보완하겠습니다!!!

## 유사 암호
1. Shift Cipher
    - 3칸이 아닌 임의로 지정한 n칸을 움직여서 암호화를 하는 방식
2. Monoalphabetic Cipher
    - 각 알파벳을 임의로 지정하여 key를 모른 상태에서 암호화 하는 방식

## 암호 파괴 방법
    - 잘 모르겠고, 아래 링크에 가셔서 열심히 연구하심 됩니다.
    [시저암호: 위키피디아](https://en.wikipedia.org/wiki/Caesar_cipher)
    1.단순 치환 암호라는 사실을 아는 경우.
        - 빈도 분석이 태턴 분석 등의 노가다(?) 접근이 필요합니다.
    2. Caesar 암호라는 사실은 알지만, Shift 값(몇 번째로 치환되었는지)을 모르는 경우,
		- 모든 경우의 shift 값을 대입해 보는 약간은 적은 노가다 방법 필요.

## 치명적 단점
	- 여러 번 암호화 하는 경우에, 자동으로 암호가 해독될 수 있음.
		i.e. shift A와 shift B의 두 암호화 = shift A+B 의 단일 암호화와 동일한 결과.
