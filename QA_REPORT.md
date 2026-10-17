# 예제 검증 보고서

## 객관 검증
- 기준 경로: `.`
- 시작 시점 파일 스냅샷만 검증. 없는 모델은 기다리거나 재확인하지 않음.
- 원본 수정 없음. 독립 headless Chromium / 임시 context / 오프라인 / 외부 요청 차단.
- argon: 객관 PASS 19, FAIL 1; 원본 해시 일치=True. 상세 `argon\qa_results.json`
  - 실패: horizontal_overflow — {"observed": {"inner": 390, "scroll": 600, "body": 600}}
  - 스크린샷: `argon\qa_desktop1440x1000.png`
  - 스크린샷: `argon\qa_mobile390x844.png`
- sol: 객관 PASS 20, FAIL 0; 원본 해시 일치=True. 상세 `sol\qa_results.json`
  - 스크린샷: `sol\qa_desktop1440x1000.png`
  - 스크린샷: `sol\qa_mobile390x844.png`
- opus: 객관 PASS 20, FAIL 0; 원본 해시 일치=True. 상세 `opus\qa_results.json`
  - 스크린샷: `opus\qa_desktop1440x1000.png`
  - 스크린샷: `opus\qa_mobile390x844.png`

## 주관 평가 / 한계
- 세련됨·생활형 유머·내레이션 자연스러움은 주관 항목이며 자동 통과 판정하지 않음.
- 쇼츠 6구간 및 미확인 성능 문구는 검출/인용한다. 임의의 자연어 전체 사실성을 정규식으로 증명할 수는 없다.
- 실제 TTS/영상 생성·발화 시간 측정·실제 제품 성능 검증은 수행하지 않음. 모델 성능 순위로 일반화하지 않음.

## 재실행
- `python qa_examples.py` (실행 시 완성된 argon/sol/opus만 즉시 검증)
- 설치/외부 통신/개인 프로필 연결 없음.
