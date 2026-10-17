FILE: shorts.md

```markdown
# 모아컵(MoaCup) 30초 쇼핑 쇼츠 기획안

* **기획 고지:** 본 문서는 실제 영상이나 음성(TTS)을 생성하지 않은 텍스트 기반 영상 기획안입니다.
* **발화 길이 안내:** 내레이션의 소리 내어 읽은 실제 발화 길이는 미측정 상태입니다.
* **콘텐츠 원칙:** 제공된 가상 상품 자료만을 바탕으로 작성되었으며, 확인되지 않은 성능(보온 시간, 누수 방지, 식기세척기 호환성, 의학적 효과 등)은 포함하지 않았습니다.

| 구간(초) | 화면 행동 (Visual Action) | 내레이션 (Narration) | 큰 한 줄 자막 (Big Subtitle) |
| :--- | :--- | :--- | :--- |
| **0~5** | 책상 위에서 크림 색상과 네이비 색상 모아컵 두 개를 나란히 비추며 깔끔한 외관을 클로즈업합니다. | 책상 위에서 매일 손이 가는 깔끔한 컵을 찾으셨나요? 크림과 네이비 두 가지 색상의 모아컵을 소개합니다. | 크림 & 네이비, 깔끔한 데스크 짝꿍 모아컵 |
| **5~10** | 한 손으로 모아컵을 가볍게 들어 올린 뒤, 450mL 계량컵의 물을 모아컵에 가득 따르는 장면을 보여줍니다. | 280그램의 무게에 용량은 450밀리리터로, 책상 위에 두고 마시기에 적당한 크기입니다. | 450mL 용량과 280g의 가벼운 무게 |
| **10~15** | 스테인리스 본체 내부와 폴리프로필렌 재질의 뚜껑을 분리하여 각각의 표면 질감을 상세히 보여줍니다. | 본체는 스테인리스, 뚜껑은 폴리프로필렌 소재로 제작되어 실용적인 구성을 갖추었습니다. | 스테인리스 본체 + 폴리프로필렌 뚜껑 |
| **15~20** | 싱크대에서 부드러운 수세미에 거품을 내어 컵을 닦으며 손목시계를 살짝 보는 코믹한 연출을 합니다. | 세척하실 때는 손 세척을 권장해 드립니다. 설거지하며 팔 운동도 겸한다고 생각하면 마음이 한결 편해집니다. | 관리는 부드러운 손 세척 권장! |
| **20~25** | 화면에 물음표 아이콘과 함께 '보온 시간·누수 방지·식기세척기·의학적 효과 미확인' 텍스트 카드를 명확히 띄웁니다. | 다만 식기세척기 사용 가능 여부나 보온 시간, 누수 방지, 의학적 효과는 확인된 자료가 없으니 참고해 주세요. | 보온·누수방지·식기세척기 여부는 확인 자료 없음 |
| **25~30** | 크림과 네이비 모아컵이 나란히 놓인 정면 샷과 함께 가격 텍스트(24,900원, 구매 링크 없음)를 띄우며 마무리합니다. | 모아컵의 가격은 24,900원입니다. 본 영상은 테스트용 기획 자료로 별도의 구매 링크는 제공되지 않습니다. | 가격 24,900원 (테스트용 가상 상품·구매 링크 없음) |

```

FILE: factcheck.csv

```csv
claim_id,claim,verdict,evidence
1,용량 450mL,SUPPORTED,공통 자료에 용량 450mL로 명시됨
2,24시간 보온,UNVERIFIED,공통 자료에 보온 시간은 확인 자료 없음으로 명시됨
3,식기세척기 사용 가능,UNVERIFIED,공통 자료에 손 세척 권장 및 식기세척기 사용 가능 여부는 확인 자료 없음으로 명시됨
4,본체 스테인리스,SUPPORTED,공통 자료에 본체 스테인리스로 명시됨
5,완벽한 누수 방지,UNVERIFIED,공통 자료에 누수 방지는 확인 자료 없음으로 명시됨
6,가격 24900원,SUPPORTED,공통 자료에 가격 24900원으로 명시됨

```

FILE: costs.csv

```csv
plan,runs,input_tokens,output_tokens,input_usd,output_usd,total_usd,total_krw
가형,1,10000,2000,0.02,0.02,0.04,56
가형,25,250000,50000,0.5,0.5,1,1400
가형,100,1000000,200000,2,2,4,5600
가형,500,5000000,1000000,10,10,20,28000
나형,1,10000,2000,0.04,0.04,0.08,112
나형,25,250000,50000,1,1,2,2800
나형,100,1000000,200000,4,4,8,11200
나형,500,5000000,1000000,20,20,40,56000

```

FILE: demo.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>모아컵 실습실 (MoaCup Lab)</title>
  <style>
    :root {
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --text-main: #0f172a;
      --text-sub: #475569;
      --border-color: #cbd5e1;
      --accent-color: #1e293b;
      --accent-focus: #2563eb;
      --warn-bg: #fffbeb;
      --warn-border: #f59e0b;
      --warn-text: #78350f;
      --badge-ok-bg: #dcfce7;
      --badge-ok-text: #14532d;
      --badge-unv-bg: #f1f5f9;
      --badge-unv-text: #334155;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Pretendard", "Malgun Gothic", sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.6;
      padding: 20px 16px 48px;
    }

    .container {
      max-width: 1360px;
      margin: 0 auto;
    }

    header {
      margin-bottom: 20px;
      padding-bottom: 16px;
      border-bottom: 2px solid var(--border-color);
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: baseline;
      gap: 12px;
    }

    h1 {
      font-size: 1.75rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--text-main);
    }

    .subtitle {
      font-size: 0.95rem;
      color: var(--text-sub);
      font-weight: 500;
    }

    .notice-banner {
      background-color: var(--warn-bg);
      border: 2px solid var(--warn-border);
      color: var(--warn-text);
      padding: 14px 18px;
      border-radius: var(--radius);
      margin-bottom: 24px;
      font-size: 0.92rem;
    }

    .notice-banner strong {
      display: block;
      font-size: 1rem;
      margin-bottom: 4px;
    }

    .grid-layout {
      display: grid;
      grid-template-columns: 1fr;
      gap: 24px;
    }

    @media (min-width: 960px) {
      .grid-layout {
        grid-template-columns: 1fr 1fr;
        align-items: start;
      }
    }

    .card {
      background-color: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 24px;
      box-shadow: var(--shadow);
    }

    .card-title {
      font-size: 1.25rem;
      font-weight: 700;
      margin-bottom: 16px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .tag-mock {
      font-size: 0.78rem;
      font-weight: 600;
      background-color: #e2e8f0;
      color: #1e293b;
      padding: 4px 10px;
      border-radius: 999px;
    }

    /* Canvas Section */
    .canvas-wrapper {
      position: relative;
      background: linear-gradient(180deg, #f1f5f9 0%, #e2e8f0 100%);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 16px;
      margin-bottom: 18px;
    }

    canvas {
      max-width: 100%;
      height: auto;
      display: block;
    }

    .canvas-caption {
      font-size: 0.82rem;
      color: var(--text-sub);
      margin-top: 8px;
      text-align: center;
      font-weight: 600;
    }

    .controls-group {
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin-bottom: 20px;
    }

    .control-row {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }

    .control-label {
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--text-main);
    }

    .btn-group {
      display: flex;
      gap: 8px;
    }

    button {
      font-family: inherit;
      font-size: 0.92rem;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: 8px;
      border: 2px solid var(--border-color);
      background-color: #ffffff;
      color: var(--text-main);
      cursor: pointer;
      transition: all 0.15s ease;
    }

    button:hover {
      border-color: #64748b;
      background-color: #f8fafc;
    }

    button:focus-visible,
    input:focus-visible,
    select:focus-visible {
      outline: 3px solid var(--accent-focus);
      outline-offset: 2px;
    }

    button[aria-pressed="true"] {
      background-color: var(--accent-color);
      color: #ffffff;
      border-color: var(--accent-color);
    }

    .swatch-dot {
      display: inline-block;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      margin-right: 6px;
      vertical-align: middle;
      border: 1px solid rgba(0, 0, 0, 0.25);
    }

    .slider-container {
      flex: 1;
      min-width: 180px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    input[type="range"] {
      flex: 1;
      height: 6px;
      accent-color: var(--accent-color);
      cursor: pointer;
    }

    .angle-readout {
      font-variant-numeric: tabular-nums;
      font-weight: 700;
      min-width: 48px;
      text-align: right;
      font-size: 0.9rem;
    }

    /* Specs & Factcheck */
    .spec-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
      margin-bottom: 18px;
    }

    .spec-item {
      background-color: #f8fafc;
      border: 1px solid var(--border-color);
      padding: 10px 12px;
      border-radius: 8px;
    }

    .spec-item dt {
      font-size: 0.78rem;
      color: var(--text-sub);
      font-weight: 600;
    }

    .spec-item dd {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-main);
      margin-top: 2px;
    }

    .unverified-box {
      background-color: #f8fafc;
      border-left: 4px solid #64748b;
      padding: 12px 14px;
      border-radius: 6px;
      font-size: 0.88rem;
      color: var(--text-sub);
    }

    .unverified-box strong {
      color: var(--text-main);
      display: block;
      margin-bottom: 4px;
    }

    /* Calculator Section */
    .calc-form {
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin-bottom: 20px;
    }

    .input-wrap {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .input-row {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    input[type="number"] {
      font-family: inherit;
      font-size: 1rem;
      font-weight: 600;
      padding: 8px 12px;
      border: 2px solid var(--border-color);
      border-radius: 8px;
      width: 140px;
      color: var(--text-main);
    }

    .preset-btns {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }

    .preset-btns button {
      padding: 6px 12px;
      font-size: 0.85rem;
    }

    .validation-msg {
      font-size: 0.85rem;
      color: #b91c1c;
      font-weight: 600;
      min-height: 1.2em;
    }

    .result-cards {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-bottom: 20px;
    }

    .res-box {
      background-color: #f8fafc;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 12px 14px;
    }

    .res-box.highlight {
      background-color: #eff6ff;
      border-color: #93c5fd;
    }

    .res-label {
      font-size: 0.8rem;
      color: var(--text-sub);
      font-weight: 600;
    }

    .res-value {
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--text-main);
      font-variant-numeric: tabular-nums;
      margin-top: 2px;
    }

    .table-container {
      overflow-x: auto;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      margin-top: 12px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.86rem;
      text-align: left;
    }

    th, td {
      padding: 10px 12px;
      border-bottom: 1px solid var(--border-color);
      font-variant-numeric: tabular-nums;
    }

    th {
      background-color: #f1f5f9;
      font-weight: 700;
      color: var(--text-main);
      white-space: nowrap;
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr.active-row {
      background-color: #fef9c3;
      font-weight: 700;
    }

    .badge {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 0.76rem;
      font-weight: 700;
    }

    .badge-supported {
      background-color: var(--badge-ok-bg);
      color: var(--badge-ok-text);
    }

    .badge-unverified {
      background-color: var(--badge-unv-bg);
      color: var(--badge-unv-text);
    }

    @media (max-width: 480px) {
      body {
        padding: 12px 10px 36px;
      }
      .card {
        padding: 16px;
      }
      .spec-grid,
      .result-cards {
        grid-template-columns: 1fr;
      }
      h1 {
        font-size: 1.45rem;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>모아컵 실습실 (MoaCup Lab)</h1>
      <span class="subtitle">한국어 AI 비교 칼럼 첨부용 독립 실행 데모</span>
    </header>

    <aside class="notice-banner" role="note" aria-label="가상 자료 및 미확인 성능 고지">
      <strong>[필수 고지] 테스트용 가상 상품 및 가상 단가 안내</strong>
      본 페이지의 '모아컵'과 'AI 업무 단가(가형/나형)'는 실제 상품이나 실제 AI 제공사 요금이 아닌 칼럼 실습용 가상 데이터입니다.
      또한 <strong>식기세척기 사용 가능 여부, 보온 시간, 누수 방지, 의학적 효과</strong>는 확인된 자료가 없으며 구매 링크도 존재하지 않습니다.
    </aside>

    <main class="grid-layout">
      <!-- 왼쪽 섹션: 모아컵 Canvas 시각화 및 제품 사양 -->
      <section class="card" aria-labelledby="visualizer-title">
        <div class="card-title">
          <h2 id="visualizer-title">1. 모아컵 3D 형태 시각화</h2>
          <span class="tag-mock">실제 제품 사진 아님 (Canvas 렌더링)</span>
        </div>

        <div class="canvas-wrapper">
          <canvas id="cupCanvas" width="340" height="320" aria-label="모아컵 3D 원통형 텀블러 시각화 캔버스"></canvas>
          <p class="canvas-caption">※ 위 그래픽은 코드로 직접 렌더링한 가상 도형이며 실제 제품 사진이 아닙니다.</p>
        </div>

        <div class="controls-group">
          <div class="control-row">
            <span class="control-label" id="color-label">색상 전환</span>
            <div class="btn-group" role="group" aria-labelledby="color-label">
              <button type="button" id="btnCream" aria-pressed="true" onclick="setCupColor('cream')">
                <span class="swatch-dot" style="background-color: #f5efe1;"></span>크림 (Cream)
              </button>
              <button type="button" id="btnNavy" aria-pressed="false" onclick="setCupColor('navy')">
                <span class="swatch-dot" style="background-color: #1e294b;"></span>네이비 (Navy)
              </button>
            </div>
          </div>

          <div class="control-row">
            <label class="control-label" for="rotationSlider">회전 각도 (키보드 좌우 화살표 조작 가능)</label>
            <div class="slider-container">
              <input type="range" id="rotationSlider" min="0" max="360" value="25" step="1" aria-valuemin="0" aria-valuemax="360" aria-valuenow="25">
              <span class="angle-readout" id="angleValue">25°</span>
            </div>
          </div>
        </div>

        <dl class="spec-grid">
          <div class="spec-item">
            <dt>상품명 / 가격</dt>
            <dd>모아컵 / 24,900원</dd>
          </div>
          <div class="spec-item">
            <dt>용량 / 무게</dt>
            <dd>450mL / 280g</dd>
          </div>
          <div class="spec-item">
            <dt>본체 / 뚜껑 재질</dt>
            <dd>스테인리스 / 폴리프로필렌</dd>
          </div>
          <div class="spec-item">
            <dt>세척 방법 / 구매 링크</dt>
            <dd>손 세척 권장 / 링크 없음</dd>
          </div>
        </dl>

        <div class="unverified-box">
          <strong>확인되지 않은 성능 (근거 자료 없음)</strong>
          식기세척기 사용 가능 여부 · 보온 유지 시간 · 완벽한 누수 방지 여부 · 의학적 효과는 제공된 자료에서 확인되지 않았습니다.
        </div>

        <h3 style="font-size: 1rem; margin: 20px 0 8px; font-weight: 700;">주요 주장 6개 팩트체크 요약</h3>
        <div class="table-container">
          <table aria-label="모아컵 6개 주장 검증 표">
            <thead>
              <tr>
                <th>번호</th>
                <th>검증 주장</th>
                <th>판정 (Verdict)</th>
                <th>근거 요약</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>①</td>
                <td>용량 450mL</td>
                <td><span class="badge badge-supported">SUPPORTED</span></td>
                <td>공통 자료에 용량 450mL 명시</td>
              </tr>
              <tr>
                <td>②</td>
                <td>24시간 보온</td>
                <td><span class="badge badge-unverified">UNVERIFIED</span></td>
                <td>보온 시간 확인 자료 없음</td>
              </tr>
              <tr>
                <td>③</td>
                <td>식기세척기 사용 가능</td>
                <td><span class="badge badge-unverified">UNVERIFIED</span></td>
                <td>손 세척 권장, 식기세척기 확인 자료 없음</td>
              </tr>
              <tr>
                <td>④</td>
                <td>본체 스테인리스</td>
                <td><span class="badge badge-supported">SUPPORTED</span></td>
                <td>공통 자료에 본체 스테인리스 명시</td>
              </tr>
              <tr>
                <td>⑤</td>
                <td>완벽한 누수 방지</td>
                <td><span class="badge badge-unverified">UNVERIFIED</span></td>
                <td>누수 방지 확인 자료 없음</td>
              </tr>
              <tr>
                <td>⑥</td>
                <td>가격 24900원</td>
                <td><span class="badge badge-supported">SUPPORTED</span></td>
                <td>공통 자료에 가격 24900원 명시</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- 오른쪽 섹션: 가상 업무 비용 계산기 -->
      <section class="card" aria-labelledby="calc-title">
        <div class="card-title">
          <h2 id="calc-title">2. 가상 AI 업무 비용 계산기</h2>
          <span class="tag-mock">가상 단가 (실제 요금 아님)</span>
        </div>

        <p style="font-size: 0.88rem; color: var(--text-sub); margin-bottom: 16px;">
          1회 작업 기준: <strong>입력 10,000토큰 + 출력 2,000토큰</strong> | 가정 환율: <strong>$1 = 1,400원</strong> (세금·캐싱·도구 호출 제외)<br>
          가형 단가: 입력 $2 / 1M, 출력 $10 / 1M | 나형 단가: 입력 $4 / 1M, 출력 $20 / 1M
        </p>

        <div class="calc-form">
          <div class="control-row">
            <span class="control-label" id="plan-label">가상 요금제 선택</span>
            <div class="btn-group" role="group" aria-labelledby="plan-label">
              <button type="button" id="btnPlanA" aria-pressed="true" onclick="setPlan('A')">가형 ($2 / $10)</button>
              <button type="button" id="btnPlanB" aria-pressed="false" onclick="setPlan('B')">나형 ($4 / $20)</button>
            </div>
          </div>

          <div class="input-wrap">
            <label class="control-label" for="runsInput">작업 횟수 (1 ~ 100,000회 정수 입력)</label>
            <div class="input-row">
              <input type="number" id="runsInput" min="1" max="100000" step="1" value="25" aria-describedby="runsError">
              <div class="preset-btns" role="group" aria-label="작업 횟수 빠른 선택">
                <button type="button" onclick="setPresetRuns(1)">1회</button>
                <button type="button" onclick="setPresetRuns(25)">25회</button>
                <button type="button" onclick="setPresetRuns(100)">100회</button>
                <button type="button" onclick="setPresetRuns(500)">500회</button>
              </div>
            </div>
            <p id="runsError" class="validation-msg" role="alert" aria-live="polite"></p>
          </div>
        </div>

        <div class="result-cards" aria-live="polite">
          <div class="res-box">
            <div class="res-label">누적 입력 토큰</div>
            <div class="res-value" id="resInputTokens">250,000</div>
          </div>
          <div class="res-box">
            <div class="res-label">누적 출력 토큰</div>
            <div class="res-value" id="resOutputTokens">50,000</div>
          </div>
          <div class="res-box">
            <div class="res-label">입력 비용 + 출력 비용 (USD)</div>
            <div class="res-value" id="resSplitUsd">$0.50 + $0.50</div>
          </div>
          <div class="res-box highlight">
            <div class="res-label">총 비용 (USD / KRW)</div>
            <div class="res-value" id="resTotalCost">$1.00 / 1,400원</div>
          </div>
        </div>

        <h3 style="font-size: 1rem; margin: 16px 0 8px; font-weight: 700;">가형·나형 기준 횟수별 비교표 (1, 25, 100, 500회)</h3>
        <div class="table-container">
          <table aria-label="가형 및 나형 비용 계산 비교표">
            <thead>
              <tr>
                <th>구분</th>
                <th>횟수</th>
                <th>입력 토큰</th>
                <th>출력 토큰</th>
                <th>입력($)</th>
                <th>출력($)</th>
                <th>총액($)</th>
                <th>총액(원)</th>
              </tr>
            </thead>
            <tbody id="costTableBody">
              <!-- 자바스크립트로 렌더링 -->
            </tbody>
          </table>
        </div>
      </section>
    </main>
  </div>

  <script>
    // --- 상태 관리 ---
    const state = {
      color: 'cream',
      angle: 25,
      plan: 'A',
      runs: 25
    };

    const PLANS = {
      A: { name: '가형', inRate: 2, outRate: 10 },
      B: { name: '나형', inRate: 4, outRate: 20 }
    };

    const TOKENS_PER_RUN = { input: 10000, output: 2000 };
    const EXCHANGE_RATE = 1400;
    const PRESET_RUNS = [1, 25, 100, 500];

    // --- 캔버스 모아컵 3D풍 렌더링 ---
    const canvas = document.getElementById('cupCanvas');
    const ctx = canvas.getContext('2d');

    function drawMoaCup() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      const cx = canvas.width / 2;
      const topY = 74;
      const bottomY = 262;
      const topRx = 68;
      const topRy = 18;
      const botRx = 54;
      const botRy = 15;

      const rad = (state.angle * Math.PI) / 180;

      // 색상 팔레트 설정
      const palette = state.color === 'cream'
        ? {
            bodyLeft: '#fdfbf7',
            bodyMid: '#f3ebd9',
            bodyRight: '#d6cbb5',
            labelColor: '#334155',
            badgeBg: 'rgba(30, 41, 59, 0.08)'
          }
        : {
            bodyLeft: '#314475',
            bodyMid: '#1e294b',
            bodyRight: '#0f172a',
            labelColor: '#f8fafc',
            badgeBg: 'rgba(255, 255, 255, 0.12)'
          };

      // 1. 바닥 그림자
      ctx.save();
      ctx.beginPath();
      ctx.ellipse(cx, bottomY + 12, botRx + 14, botRy + 6, 0, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(15, 23, 42, 0.16)';
      ctx.fill();
      ctx.restore();

      // 2. 스테인리스 하단 베이스 링 (본체 스테인리스 표현)
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(cx - botRx, bottomY - 12);
      ctx.lineTo(cx - botRx, bottomY);
      ctx.ellipse(cx, bottomY, botRx, botRy, 0, Math.PI, 0, true);
      ctx.lineTo(cx + botRx, bottomY - 12);
      ctx.closePath();
      const steelGrad = ctx.createLinearGradient(cx - botRx, 0, cx + botRx, 0);
      steelGrad.addColorStop(0, '#94a3b8');
      steelGrad.addColorStop(0.35, '#e2e8f0');
      steelGrad.addColorStop(0.7, '#64748b');
      steelGrad.addColorStop(1, '#cbd5e1');
      ctx.fillStyle = steelGrad;
      ctx.fill();
      ctx.strokeStyle = '#475569';
      ctx.lineWidth = 1;
      ctx.stroke();
      ctx.restore();

      // 3. 컵 본체 (원통형 그라데이션)
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(cx - topRx, topY);
      ctx.lineTo(cx - botRx, bottomY - 10);
      ctx.ellipse(cx, bottomY - 10, botRx, botRy, 0, Math.PI, 0, true);
      ctx.lineTo(cx + topRx, topY);
      ctx.closePath();

      const bodyGrad = ctx.createLinearGradient(cx - topRx, 0, cx + topRx, 0);
      bodyGrad.addColorStop(0, palette.bodyLeft);
      bodyGrad.addColorStop(0.45, palette.bodyMid);
      bodyGrad.addColorStop(0.9, palette.bodyRight);
      bodyGrad.addColorStop(1, palette.bodyMid);
      ctx.fillStyle = bodyGrad;
      ctx.fill();
      ctx.strokeStyle = 'rgba(15, 23, 42, 0.25)';
      ctx.lineWidth = 1.2;
      ctx.stroke();

      // 본체 클리핑 후 회전 연동 그래픽(전면 로고 및 눈금) 렌더링
      ctx.clip();

      const offsetX = Math.sin(rad) * 52;
      const frontVisibility = Math.cos(rad);

      // 회전 시 입체감을 주는 세로 하이라이트 선
      const highlightX = cx + Math.sin(rad * 2) * 18 - 22;
      ctx.fillStyle = 'rgba(255, 255, 255, 0.16)';
      ctx.fillRect(highlightX, topY, 14, bottomY - topY);

      // 전면 로고 (앞면을 향할 때 표시)
      if (frontVisibility > -0.2) {
        ctx.save();
        ctx.globalAlpha = Math.max(0.15, (frontVisibility + 0.2) / 1.2);
        ctx.translate(cx + offsetX, (topY + bottomY) / 2 - 6);
        ctx.scale(Math.max(0.25, Math.abs(frontVisibility)), 1);

        ctx.fillStyle = palette.badgeBg;
        ctx.beginPath();
        ctx.roundRect(-42, -26, 84, 52, 8);
        ctx.fill();

        ctx.fillStyle = palette.labelColor;
        ctx.font = '800 15px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('MOACUP', 0, -4);
        ctx.font = '600 11px sans-serif';
        ctx.fillText('450mL · 280g', 0, 14);
        ctx.restore();
      }

      // 후면 스테인리스 안내 각인 (뒷면을 향할 때 표시)
      if (frontVisibility < 0.2) {
        ctx.save();
        ctx.globalAlpha = Math.max(0.15, (-frontVisibility + 0.2) / 1.2);
        ctx.translate(cx - offsetX, (topY + bottomY) / 2);
        ctx.fillStyle = palette.labelColor;
        ctx.font = '600 11px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('BODY: STAINLESS', 0, -4);
        ctx.fillText('LID: PP (손 세척 권장)', 0, 12);
        ctx.restore();
      }

      ctx.restore();

      // 4. 스테인리스 상단 림 (Rim)
      ctx.save();
      ctx.beginPath();
      ctx.ellipse(cx, topY, topRx, topRy, 0, 0, Math.PI * 2);
      ctx.fillStyle = steelGrad;
      ctx.fill();
      ctx.strokeStyle = '#64748b';
      ctx.lineWidth = 1;
      ctx.stroke();
      ctx.restore();

      // 5. 폴리프로필렌(PP) 뚜껑
      const lidHeight = 16;
      const lidRx = topRx + 2;
      const lidRy = topRy + 1;

      ctx.save();
      ctx.beginPath();
      ctx.moveTo(cx - lidRx, topY - 2);
      ctx.lineTo(cx - lidRx, topY - lidHeight);
      ctx.ellipse(cx, topY - lidHeight, lidRx, lidRy, 0, Math.PI, 0, false);
      ctx.lineTo(cx + lidRx, topY - 2);
      ctx.ellipse(cx, topY - 2, lidRx, lidRy, 0, 0, Math.PI, false);
      ctx.closePath();

      const lidGrad = ctx.createLinearGradient(cx - lidRx, 0, cx + lidRx, 0);
      lidGrad.addColorStop(0, '#e2e8f0');
      lidGrad.addColorStop(0.5, '#f8fafc');
      lidGrad.addColorStop(1, '#cbd5e1');
      ctx.fillStyle = lidGrad;
      ctx.fill();
      ctx.strokeStyle = '#64748b';
      ctx.lineWidth = 1.2;
      ctx.stroke();

      // 뚜껑 윗면
      ctx.beginPath();
      ctx.ellipse(cx, topY - lidHeight, lidRx, lidRy, 0, 0, Math.PI * 2);
      ctx.fillStyle = '#f1f5f9';
      ctx.fill();
      ctx.strokeStyle = '#94a3b8';
      ctx.stroke();

      // 뚜껑 음용구 포인트 (회전 각도에 따라 위치 이동)
      const sipX = cx + Math.cos(rad) * (lidRx * 0.55);
      const sipY = (topY - lidHeight) + Math.sin(rad) * (lidRy * 0.55);
      ctx.beginPath();
      ctx.ellipse(sipX, sipY, 10, 5, rad, 0, Math.PI * 2);
      ctx.fillStyle = '#475569';
      ctx.fill();
      ctx.restore();

      // 6. 캔버스 내부 워터마크 및 사양 안내
      ctx.save();
      ctx.fillStyle = '#334155';
      ctx.font = '700 12px sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('모아컵 가상 3D 모델 (제품 사진 아님)', 12, 22);
      ctx.font = '600 11px sans-serif';
      ctx.fillStyle = '#475569';
      ctx.fillText(`현재 색상: ${state.color === 'cream' ? '크림' : '네이비'} | 회전: ${state.angle}°`, 12, 308);
      ctx.restore();
    }

    function setCupColor(color) {
      state.color = color;
      document.getElementById('btnCream').setAttribute('aria-pressed', color === 'cream' ? 'true' : 'false');
      document.getElementById('btnNavy').setAttribute('aria-pressed', color === 'navy' ? 'true' : 'false');
      drawMoaCup();
    }

    document.getElementById('rotationSlider').addEventListener('input', function (e) {
      const val = Number(e.target.value);
      state.angle = val;
      e.target.setAttribute('aria-valuenow', String(val));
      document.getElementById('angleValue').textContent = val + '°';
      drawMoaCup();
    });

    // --- 가상 비용 계산기 로직 ---
    function calculateMetrics(planKey, runs) {
      const plan = PLANS[planKey];
      const inputTokens = runs * TOKENS_PER_RUN.input;
      const outputTokens = runs * TOKENS_PER_RUN.output;

      // 부동소수점 오차 방지를 위한 정밀 계산
      const inputUsd = (inputTokens / 1000000) * plan.inRate;
      const outputUsd = (outputTokens / 1000000) * plan.outRate;
      const totalUsd = inputUsd + outputUsd;
      const totalKrw = Math.round(totalUsd * EXCHANGE_RATE);

      return {
        planName: plan.name,
        runs,
        inputTokens,
        outputTokens,
        inputUsd,
        outputUsd,
        totalUsd,
        totalKrw
      };
    }

    function formatUsd(num) {
      return Number.isInteger(num) ? num.toString() : num.toFixed(2).replace(/\.?0+$/, '');
    }

    function updateCalculatorUI() {
      const inputEl = document.getElementById('runsInput');
      const errorEl = document.getElementById('runsError');
      const rawVal = inputEl.value.trim();
      const parsed = Number(rawVal);

      if (rawVal === '' || !Number.isInteger(parsed) || parsed < 1 || parsed > 100000) {
        errorEl.textContent = '오류: 작업 횟수는 1 이상 100,000 이하의 정수로 입력해 주세요.';
        return;
      }

      errorEl.textContent = '';
      state.runs = parsed;

      const m = calculateMetrics(state.plan, state.runs);

      document.getElementById('resInputTokens').textContent = m.inputTokens.toLocaleString('ko-KR') + ' 토큰';
      document.getElementById('resOutputTokens').textContent = m.outputTokens.toLocaleString('ko-KR') + ' 토큰';
      document.getElementById('resSplitUsd').textContent = `$${ m.inputUsd.toFixed(2) } + $${ m.outputUsd.toFixed(2) }`;
      document.getElementById('resTotalCost').textContent = `$${ m.totalUsd.toFixed(2) } / ${ m.totalKrw.toLocaleString('ko-KR') }원`;

      renderComparisonTable();
    }

    function renderComparisonTable() {
      const tbody = document.getElementById('costTableBody');
      tbody.innerHTML = '';

      ['A', 'B'].forEach(planKey => {
        PRESET_RUNS.forEach(r => {
          const m = calculateMetrics(planKey, r);
          const tr = document.createElement('tr');
          if (state.plan === planKey && state.runs === r) {
            tr.className = 'active-row';
          }
          tr.innerHTML = `
            <td>${m.planName}</td>
            <td>${m.runs}회</td>
            <td>${m.inputTokens.toLocaleString('ko-KR')}</td>
            <td>${m.outputTokens.toLocaleString('ko-KR')}</td>
            <td>$${formatUsd(m.inputUsd)}</td>
            <td>$${formatUsd(m.outputUsd)}</td>
            <td>$${formatUsd(m.totalUsd)}</td>
            <td>${m.totalKrw.toLocaleString('ko-KR')}원</td>
          `;
          tbody.appendChild(tr);
        });
      });
    }

    function setPlan(planKey) {
      state.plan = planKey;
      document.getElementById('btnPlanA').setAttribute('aria-pressed', planKey === 'A' ? 'true' : 'false');
      document.getElementById('btnPlanB').setAttribute('aria-pressed', planKey === 'B' ? 'true' : 'false');
      updateCalculatorUI();
    }

    function setPresetRuns(runsVal) {
      const inputEl = document.getElementById('runsInput');
      inputEl.value = String(runsVal);
      updateCalculatorUI();
    }

    document.getElementById('runsInput').addEventListener('input', updateCalculatorUI);

    // 초기 실행
    drawMoaCup();
    updateCalculatorUI();
  </script>
</body>
</html>

```

**생성된 파일명:** `shorts.md`, `factcheck.csv`, `costs.csv`, `demo.html`

**제한점:** 테스트용 가상 데이터만 사용했으며, `shorts.md`의 실제 내레이션 발화 시간은 측정하지 않았고, 식기세척기 호환·보온 시간·누수 방지·의학적 효과는 확인 자료가 없어 단정하지 않았으며, `demo.html`의 컵 시각화는 실제 제품 사진이 아닌 코드 기반 2D Canvas 그래픽입니다.