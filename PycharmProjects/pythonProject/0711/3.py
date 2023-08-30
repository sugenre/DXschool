import sys
import MYPY #MYPY모듈이나 패키지를 import

sys.path.append("./") #현재 디렉토리에서 모듈이나 패키지를 검색하도록 설정
print(MYPY.MYPY)
MYPY.func("모듈 사용")