# 🛒 DODODADA - 포인트 기반 쇼핑 서비스

![DODODADA](https://img.shields.io/badge/DODODADA-v1.0-black)
![Django](https://img.shields.io/badge/Django-5.0-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)

## ✨ 서비스 소개

**DODODADA**는 포인트를 충전하고 다양한 상품을 구매할 수 있는 온라인 쇼핑 플랫폼입니다. 사용자 친화적인 인터페이스와 안전한 포인트 시스템을 통해 편리한 쇼핑 경험을 제공합니다.

### 💰 포인트 기반 시스템

실제 화폐 대신 포인트를 사용하여 안전하고 편리하게 상품을 구매할 수 있습니다. 다양한 금액으로 포인트를 충전하고 원하는 상품을 구매하세요!

## 🌟 주요 기능

### 👤 사용자 관리
- **회원가입/로그인**: 개인 정보 보호와 맞춤형 서비스를 위한 계정 관리
- **마이페이지**: 개인 정보 확인 및 수정, 포인트 확인
- **회원탈퇴**: 필요시 계정 삭제 가능

### 💸 포인트 시스템
- **포인트 충전**: 다양한 금액(1,000~50,000) 선택 가능
- **포인트 사용**: 상품 구매시 자동 차감
- **잔액 확인**: 실시간 포인트 잔액 확인

### 🛍️ 상품 구매
- **카테고리별 검색**: 다양한 카테고리로 상품 필터링
- **가격별 정렬**: 가격 높은순/낮은순 정렬 기능
- **상품 상세 정보**: 이미지, 설명, 가격, 재고 확인
- **재고 관리**: 실시간 재고 확인 및 품절 상품 표시

### 📋 주문 관리
- **주문 내역**: 구매한 상품 목록 확인
- **결제 정보**: 상품명, 카테고리, 가격, 구매 일시 확인

### 👨‍💼 관리자 기능
- **상품 관리**: 상품 등록, 수정, 삭제
- **카테고리 관리**: 카테고리 추가 및 관리
- **사용자 관리**: 회원 정보 관리
- **주문 내역 관리**: 모든 주문 내역 확인

## 🚀 시작하기

### 필수 요구사항
- Python 3.8 이상
- Django 5.0 이상
- Pillow (이미지 처리)

### 설치 방법

```bash
# 저장소 복제
git clone https://github.com/yourusername/dododada.git
cd dododada

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 필요한 패키지 설치
pip install -r requirements.txt

# 프로젝트 루트 경로에서 secrets.json 파일 생성
{
    "SECRET": "django-insecure...~~~~~",
}
=> 다음 정보 저장

# 프로젝트 루트 경로의 manage.py 파일 클릭 및 환경을 local로 변경
def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

=> 위와 같이 config.settings.production을 config.settings.local로 변경
=> (주의) 깃허브에 배포시에는 꼭 config.settings.production으로 변경후 올리기

# 데이터베이스 마이그레이션
python manage.py migrate

# 초기 데이터 로드
python manage.py loaddata dododada/fixtures/categories.json

# 서버 실행
python manage.py runserver --settings=config.settings.local

# 접속
http://127.0.0.1:8000/

```

## 📸 서비스 화면

- 메인 페이지: 서비스 소개 및 시작점
- 포인트 충전: 다양한 금액 옵션으로 포인트 충전
- 상품 목록: 카테고리별, 가격별 상품 검색 및 정렬
- 상품 상세: 상품 정보 확인 및 구매
- 결제 내역: 구매한 상품 내역 및 결제 정보

## 📝 개발 정보

- 프레임워크: Django
- 프론트엔드: HTML, CSS, JavaScript, Bootstrap 5
- 데이터베이스: SQLite (개발)
- 이미지 처리: Pillow

## 🔒 보안 정보

- 사용자 인증: Django 기본 인증 시스템
- 비밀번호 암호화: PBKDF2 알고리즘
- CSRF 보호: Django 기본 CSRF 보호

## 📜 라이센스

이 프로젝트는 dododada서비스 라이센스 하에 배포됩니다.

---

🏡 [DODODADA 홈페이지](https://dododada.example.com)
📧 문의: contact@dododada.example.com
