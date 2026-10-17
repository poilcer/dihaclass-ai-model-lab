FILE: shorts.md
```markdown
# 모아컵 30초 쇼핑 쇼츠 기획안

> **기획 문서입니다.** 영상과 TTS는 실제로 만들지 않았습니다.
> 모아컵은 테스트용 **가상 상품**이고, 구매 링크는 없습니다.
> 소리 내어 읽었을 때의 실제 길이는 **측정하지 않았습니다.** 구간별 시간은 목표 배분입니다.

- 형식: 세로 9:16, 약 30초, 한국어 정중체
- 확인된 정보만 사용: 450mL, 280g, 24900원, 본체 스테인리스, 뚜껑 폴리프로필렌, 크림/네이비, 손 세척 권장
- 사용하지 않는 주장: 식기세척기 사용 가능 여부, 보온 시간, 누수 방지, 의학적 효과 (모두 확인 자료 없음)
- 생활형 유머: 20~25초 구간에 1회
- 구매를 재촉하는 표현은 넣지 않음 (한정 수량, 지금 바로 구매 등)

| 구간 | 화면 행동 | 내레이션 | 큰 한 줄 자막 |
|---|---|---|---|
| 0~5초 | 아침 책상 위의 크림색 모아컵을 천천히 클로즈업합니다. 화면 구석에 '가상 상품' 라벨을 표시합니다. | 책상 위에 컵 하나 두실 분들께 모아컵을 소개해 드릴게요. | 오늘의 컵, 모아컵 |
| 5~10초 | 컵 옆에 450mL 계량 눈금 그래픽과 280g 저울 아이콘을 차례로 띄웁니다. | 용량은 450mL이고, 무게는 280g입니다. | 450mL · 280g |
| 10~15초 | 본체와 뚜껑에 화살표 라벨을 붙이고, 뚜껑을 살짝 들어 올리는 동작을 보여 줍니다. | 본체는 스테인리스, 뚜껑은 폴리프로필렌으로 되어 있습니다. | 본체 스테인리스 · 뚜껑 PP |
| 15~20초 | 크림 컵이 회전하면서 네이비 컵으로 바뀌고, 두 컵을 나란히 둡니다. | 색상은 크림과 네이비, 두 가지 중에서 고르실 수 있어요. | 크림 또는 네이비 |
| 20~25초 | 싱크대에서 스펀지로 컵을 손 세척하는 장면을 보여 주고, 마지막에 사람이 살짝 웃습니다. | 세척은 손으로 하시길 권장드려요. 컵을 닦다 보면 밀린 생각까지 조금 정리되는 기분입니다. | 손 세척 권장 |
| 25~30초 | 가격 카드와 함께 작은 글씨로 '보온·누수·식기세척기 정보 미확인'을 표시하고 화면을 정지합니다. | 가격은 24,900원입니다. 보온과 누수 관련 정보는 아직 확인되지 않았으니 천천히 비교해 보세요. | 24,900원 · 일부 성능 미확인 |

## 제작 메모
- 의학적 효과, 보온 시간, 누수 방지, 식기세척기 관련 문구와 자막은 넣지 않습니다.
- 마지막 구간 내레이션은 5초를 넘길 수 있습니다. 실제 녹음 후 길이를 재고 문장을 다듬어야 합니다.
```

FILE: factcheck.csv
```csv
claim_id,claim,verdict,evidence
1,용량 450mL,SUPPORTED,"공통 자료에 용량 450mL로 명시됨"
2,24시간 보온,UNVERIFIED,"공통 자료에 보온 시간은 확인 자료 없음으로 표기됨"
3,식기세척기 사용 가능,UNVERIFIED,"공통 자료에는 손 세척 권장만 있고, 식기세척기 사용 가능 여부는 확인 자료 없음으로 표기됨"
4,본체 스테인리스,SUPPORTED,"공통 자료에 본체 스테인리스로 명시됨"
5,완벽한 누수 방지,UNVERIFIED,"공통 자료에 누수 방지는 확인 자료 없음으로 표기됨"
6,가격 24900원,SUPPORTED,"공통 자료에 가격 24900원으로 명시됨"
```

FILE: costs.csv
```csv
plan,runs,input_tokens,output_tokens,input_usd,output_usd,total_usd,total_krw
가형,1,10000,2000,0.02,0.02,0.04,56
가형,25,250000,50000,0.50,0.50,1.00,1400
가형,100,1000000,200000,2.00,2.00,4.00,5600
가형,500,5000000,1000000,10.00,10.00,20.00,28000
나형,1,10000,2000,0.04,0.04,0.08,112
나형,25,250000,50000,1.00,1.00,2.00,2800
나형,100,1000000,200000,4.00,4.00,8.00,11200
나형,500,5000000,1000000,20.00,20.00,40.00,56000
```

FILE: demo.html
```html
<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>모아컵 실습실</title>
<link rel="icon" href="data:,">
<style>
  :root{
    --bg:#F5F1E8;
    --surface:#FFFFFF;
    --surface-2:#FBF9F4;
    --ink:#1A2132;
    --muted:#4A5468;
    --line:#DCD4C3;
    --accent:#1F3A6E;
    --accent-ink:#FFFFFF;
    --accent-soft:#E6ECF7;
    --ok-bg:#E3F2E8;
    --ok-ink:#14532D;
    --warn-bg:#FFF3D1;
    --warn-ink:#5A3E00;
    --error:#B42318;
    --focus:#2563EB;
    --radius:18px;
    --shadow:0 1px 2px rgba(26,33,50,.06),0 8px 28px rgba(26,33,50,.08);
    --c-body:#EEE3CB;
    --c-lid:#D8C8A6;
    --c-steel:#B9C0C9;
  }
  *{box-sizing:border-box}
  html{-webkit-text-size-adjust:100%}
  body{
    margin:0;background:var(--bg);color:var(--ink);
    font-family:system-ui,-apple-system,"Apple SD Gothic Neo","Malgun Gothic","Noto Sans KR",sans-serif;
    line-height:1.6;font-size:16px;
  }
  .wrap{max-width:1200px;margin:0 auto;padding:24px 16px 48px}
  header.top{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:12px;margin-bottom:16px}
  .eyebrow{font-size:13px;font-weight:700;letter-spacing:.08em;color:var(--accent);margin:0 0 4px}
  h1{font-size:clamp(28px,5vw,44px);line-height:1.15;margin:0;letter-spacing:-.02em}
  h2{font-size:20px;margin:0 0 4px;letter-spacing:-.01em}
  .sub{color:var(--muted);margin:6px 0 0}
  .notice{
    background:var(--warn-bg);color:var(--warn-ink);border:1px solid #EBD38E;
    border-radius:12px;padding:12px 14px;font-size:14px;margin:0 0 20px
  }
  .notice strong{font-weight:800}
  .grid{display:grid;grid-template-columns:1fr;gap:20px}
  @media (min-width:900px){.grid{grid-template-columns:1.05fr 1fr}}
  .card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:20px}
  .card-head{margin-bottom:14px}
  .card-head p{margin:0;color:var(--muted);font-size:14px}

  /* 컵 시각화 */
  .stage{
    position:relative;height:340px;border-radius:14px;overflow:hidden;
    background:radial-gradient(120% 90% at 50% 20%,#FFFFFF 0%,#EFE9DC 70%,#E6DECD 100%);
    perspective:900px;outline:none;border:1px solid var(--line);
  }
  .stage:focus-visible{outline:3px solid var(--focus);outline-offset:3px}
  .floor-shadow{
    position:absolute;left:50%;top:50%;width:190px;height:34px;margin-left:-95px;margin-top:112px;
    background:radial-gradient(closest-side,rgba(20,26,40,.28),rgba(20,26,40,0));
  }
  .cup{position:absolute;left:50%;top:50%;width:0;height:0;transform-style:preserve-3d;transform:rotateX(-16deg) rotateY(0deg)}
  .pn{
    position:absolute;backface-visibility:hidden;-webkit-backface-visibility:hidden;
    --hi:0;--sh:0;
  }
  .pn.body{background:linear-gradient(rgba(255,255,255,var(--hi)),rgba(255,255,255,var(--hi))),linear-gradient(rgba(10,15,30,var(--sh)),rgba(10,15,30,var(--sh))),var(--c-body)}
  .pn.lid{background:linear-gradient(rgba(255,255,255,var(--hi)),rgba(255,255,255,var(--hi))),linear-gradient(rgba(10,15,30,var(--sh)),rgba(10,15,30,var(--sh))),var(--c-lid)}
  .pn.steel{background:linear-gradient(rgba(255,255,255,var(--hi)),rgba(255,255,255,var(--hi))),linear-gradient(rgba(10,15,30,var(--sh)),rgba(10,15,30,var(--sh))),var(--c-steel)}
  .disc{position:absolute;border-radius:50%}
  .disc.top{background:radial-gradient(circle at 40% 40%,rgba(255,255,255,.25),rgba(0,0,0,.06)),var(--c-lid)}
  .disc.top::after{
    content:"";position:absolute;left:50%;top:14%;width:34%;height:16%;transform:translateX(-50%);
    border-radius:40px;background:rgba(10,15,30,.35);
  }
  .disc.bottom{background:var(--c-steel)}
  .viz-tag{
    position:absolute;left:12px;top:12px;font-size:12px;font-weight:700;
    background:rgba(255,255,255,.92);color:var(--ink);border:1px solid var(--line);
    border-radius:999px;padding:4px 10px
  }
  .viz-color{position:absolute;right:12px;top:12px;font-size:12px;font-weight:700;background:var(--accent);color:var(--accent-ink);border-radius:999px;padding:4px 10px}

  .controls{display:grid;gap:14px;margin-top:16px}
  .row{display:flex;flex-wrap:wrap;align-items:center;gap:10px}
  .label{font-size:14px;font-weight:700}
  .seg{display:inline-flex;gap:8px;flex-wrap:wrap}
  button{font:inherit;cursor:pointer}
  .chip{
    display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:8px 14px;
    border-radius:999px;border:1.5px solid var(--line);background:var(--surface);color:var(--ink);font-weight:700;font-size:15px
  }
  .chip[aria-pressed="true"]{border-color:var(--accent);background:var(--accent-soft)}
  .swatch{width:18px;height:18px;border-radius:50%;border:1px solid rgba(0,0,0,.25)}
  .chip:focus-visible,.btn:focus-visible,input:focus-visible,.radio input:focus-visible+span{outline:3px solid var(--focus);outline-offset:2px}
  .btn{min-height:44px;padding:8px 14px;border-radius:10px;border:1.5px solid var(--accent);background:var(--surface);color:var(--accent);font-weight:700;font-size:15px}
  .btn.primary{background:var(--accent);color:var(--accent-ink)}
  .range-wrap{display:grid;grid-template-columns:1fr auto;align-items:center;gap:12px}
  input[type=range]{width:100%;accent-color:var(--accent);min-height:44px}
  .deg{font-variant-numeric:tabular-nums;font-weight:800;min-width:56px;text-align:right}
  .hint{font-size:13px;color:var(--muted);margin:0}

  /* 계산기 */
  fieldset{border:0;margin:0;padding:0}
  legend{font-size:14px;font-weight:700;margin-bottom:8px;padding:0}
  .radio-group{display:grid;grid-template-columns:1fr 1fr;gap:10px}
  .radio{position:relative;display:block}
  .radio input{position:absolute;opacity:0;width:1px;height:1px}
  .radio span{
    display:block;border:1.5px solid var(--line);border-radius:12px;padding:12px 14px;background:var(--surface-2);min-height:44px
  }
  .radio b{display:block;font-size:17px}
  .radio small{color:var(--muted);font-size:13px}
  .radio input:checked+span{border-color:var(--accent);background:var(--accent-soft);box-shadow:inset 0 0 0 1px var(--accent)}
  .field{display:grid;gap:6px;margin-top:16px}
  .field label{font-size:14px;font-weight:700}
  .input-row{display:flex;gap:8px;flex-wrap:wrap}
  input[type=text]{
    flex:1 1 140px;min-width:0;min-height:48px;font:inherit;font-size:18px;font-weight:700;
    padding:8px 12px;border-radius:10px;border:1.5px solid #9AA3B2;background:#fff;color:var(--ink);font-variant-numeric:tabular-nums
  }
  input[aria-invalid="true"]{border-color:var(--error);background:#FFF5F4}
  .err{color:var(--error);font-size:14px;font-weight:700;min-height:22px;margin:0}
  .quick{display:flex;flex-wrap:wrap;gap:8px}
  .quick .btn{min-width:64px}
  .results{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}
  .stat{background:var(--surface-2);border:1px solid var(--line);border-radius:12px;padding:10px 12px;min-width:0}
  .stat dt{font-size:13px;color:var(--muted);font-weight:700}
  .stat dd{margin:2px 0 0;font-size:18px;font-weight:800;font-variant-numeric:tabular-nums;overflow-wrap:anywhere}
  .stat.total{grid-column:1/-1;background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
  .stat.total dt{color:#D6DEEE}
  .stat.total dd{font-size:26px}
  .formula{font-size:13px;color:var(--muted);margin:10px 0 0}
  .compare{margin-top:16px;display:grid;gap:8px}
  .bar-row{display:grid;grid-template-columns:44px 1fr auto;align-items:center;gap:10px;font-size:14px}
  .bar{height:12px;border-radius:999px;background:#ECE6D8;overflow:hidden}
  .bar i{display:block;height:100%;width:0;background:var(--accent);border-radius:999px;transition:width .3s ease}
  .bar-row.alt .bar i{background:#8A6D3B}
  .bar-row b{font-variant-numeric:tabular-nums}

  /* 표 */
  .table-wrap{overflow-x:auto;margin-top:8px;border:1px solid var(--line);border-radius:12px}
  table{width:100%;border-collapse:collapse;font-size:14px;font-variant-numeric:tabular-nums;min-width:560px}
  th,td{padding:10px 12px;text-align:right;border-bottom:1px solid var(--line);white-space:nowrap}
  th:first-child,td:first-child{text-align:left}
  thead th{background:var(--surface-2);font-size:13px;color:var(--muted)}
  tbody tr:last-child td{border-bottom:0}

  /* 사양 */
  .specs{display:grid;grid-template-columns:1fr;gap:16px;margin-top:20px}
  @media (min-width:900px){.specs{grid-template-columns:1fr 1fr}}
  ul.list{list-style:none;margin:0;padding:0;display:grid;gap:8px}
  ul.list li{display:flex;justify-content:space-between;gap:12px;padding:10px 12px;border-radius:10px;background:var(--surface-2);border:1px solid var(--line)}
  .badge{font-size:12px;font-weight:800;border-radius:999px;padding:2px 10px;white-space:nowrap;align-self:center}
  .badge.ok{background:var(--ok-bg);color:var(--ok-ink)}
  .badge.no{background:var(--warn-bg);color:var(--warn-ink)}
  footer{margin-top:24px;font-size:13px;color:var(--muted)}
  .sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}

  @media (max-width:420px){
    .card{padding:16px}
    .stage{height:310px}
    .results{grid-template-columns:1fr}
    .stat.total dd{font-size:22px}
  }
  @media (prefers-reduced-motion:reduce){.bar i{transition:none}}
</style>
</head>
<body>
<div class="wrap">
  <header class="top">
    <div>
      <p class="eyebrow">AI 비교 칼럼 실습</p>
      <h1>모아컵 실습실</h1>
      <p class="sub">가상 상품 시각화와 가상 업무 단가 계산기</p>
    </div>
  </header>

  <p class="notice" role="note">
    <strong>고지:</strong> 모아컵은 테스트용 <strong>가상 상품</strong>입니다. 아래 단가 역시 <strong>가상 업무 단가</strong>이며 실제 AI 제공사 요금이 아닙니다.
    환율은 계산을 위해 1달러 = 1,400원으로 가정했고 세금·캐싱·도구 호출은 포함하지 않았습니다. 구매 링크는 없습니다.
  </p>
  <noscript><p class="notice">이 페이지의 회전, 색상 전환, 계산기 기능은 JavaScript가 켜져 있어야 작동합니다.</p></noscript>

  <main class="grid">
    <!-- 시각화 -->
    <section class="card" aria-labelledby="viz-title">
      <div class="card-head">
        <h2 id="viz-title">컵 시각화</h2>
        <p>CSS 3D로 직접 코딩한 형태이며 <strong>제품 사진이 아닙니다.</strong> 실제 비율이나 마감과 다를 수 있습니다.</p>
      </div>
      <div class="stage" id="stage" tabindex="0" role="img" aria-roledescription="회전 가능한 시각화"
           aria-label="모아컵 CSS 3D 시각화, 크림 색상, 0도 회전. 왼쪽·오른쪽 화살표 키로 회전합니다.">
        <span class="viz-tag" aria-hidden="true">코드로 그린 시각화 · 사진 아님</span>
        <span class="viz-color" id="vizColor" aria-hidden="true">크림</span>
        <div class="floor-shadow" aria-hidden="true"></div>
        <div class="cup" id="cup" aria-hidden="true"></div>
      </div>

      <div class="controls">
        <div class="row">
          <span class="label" id="colorLabel">색상</span>
          <div class="seg" role="group" aria-labelledby="colorLabel">
            <button type="button" class="chip" data-color="cream" aria-pressed="true"><span class="swatch" style="background:#EEE3CB"></span>크림</button>
            <button type="button" class="chip" data-color="navy" aria-pressed="false"><span class="swatch" style="background:#22355F"></span>네이비</button>
          </div>
        </div>
        <div>
          <label class="label" for="rot">회전 각도</label>
          <div class="range-wrap">
            <input type="range" id="rot" min="0" max="359" step="1" value="0" aria-valuetext="0도">
            <output class="deg" id="rotOut" for="rot">0°</output>
          </div>
        </div>
        <div class="row">
          <button type="button" class="btn" id="autoBtn" aria-pressed="false">자동 회전 켜기</button>
          <p class="hint">시각화 영역을 선택한 뒤 ← → 키로 10도씩, Home 키로 정면으로 돌릴 수 있습니다.</p>
        </div>
      </div>
    </section>

    <!-- 계산기 -->
    <section class="card" aria-labelledby="calc-title">
      <div class="card-head">
        <h2 id="calc-title">가상 비용 계산기</h2>
        <p>한 작업 = 입력 10,000토큰 + 출력 2,000토큰 · 1달러 = 1,400원 가정</p>
      </div>
      <form id="calcForm" novalidate>
        <fieldset>
          <legend>단가 선택</legend>
          <div class="radio-group">
            <label class="radio">
              <input type="radio" name="plan" value="ga" checked>
              <span><b>가형</b><small>입력 $2 · 출력 $10 / 100만 토큰</small></span>
            </label>
            <label class="radio">
              <input type="radio" name="plan" value="na">
              <span><b>나형</b><small>입력 $4 · 출력 $20 / 100만 토큰</small></span>
            </label>
          </div>
        </fieldset>

        <div class="field">
          <label for="runs">작업 수 (1 ~ 1,000,000회, 정수)</label>
          <div class="input-row">
            <input type="text" id="runs" inputmode="numeric" autocomplete="off" value="25" aria-describedby="runsErr runsHint">
          </div>
          <p class="hint" id="runsHint">숫자만 입력하세요. 쉼표나 소수점은 사용할 수 없습니다.</p>
          <p class="err" id="runsErr" role="alert" aria-live="assertive"></p>
          <div class="quick" role="group" aria-label="작업 수 빠른 선택">
            <button type="button" class="btn" data-runs="1">1회</button>
            <button type="button" class="btn" data-runs="25">25회</button>
            <button type="button" class="btn" data-runs="100">100회</button>
            <button type="button" class="btn" data-runs="500">500회</button>
          </div>
        </div>
      </form>

      <dl class="results" aria-live="polite" id="results">
        <div class="stat"><dt>누적 입력 토큰</dt><dd id="rIt">—</dd></div>
        <div class="stat"><dt>누적 출력 토큰</dt><dd id="rOt">—</dd></div>
        <div class="stat"><dt>입력비 (USD)</dt><dd id="rIn">—</dd></div>
        <div class="stat"><dt>출력비 (USD)</dt><dd id="rOut">—</dd></div>
        <div class="stat"><dt>총액 (USD)</dt><dd id="rTot">—</dd></div>
        <div class="stat"><dt>환산 (KRW)</dt><dd id="rKrwSmall">—</dd></div>
        <div class="stat total"><dt id="totalLabel">가형 총액</dt><dd id="rKrw">—</dd></div>
      </dl>
      <p class="formula" id="formula"></p>

      <div class="compare" aria-label="같은 작업 수에서 두 단가 비교">
        <div class="bar-row"><span>가형</span><div class="bar" aria-hidden="true"><i id="barGa"></i></div><b id="cmpGa">—</b></div>
        <div class="bar-row alt"><span>나형</span><div class="bar" aria-hidden="true"><i id="barNa"></i></div><b id="cmpNa">—</b></div>
      </div>
    </section>
  </main>

  <section class="card" style="margin-top:20px" aria-labelledby="table-title">
    <h2 id="table-title">기준 작업 수별 가상 비용</h2>
    <p class="hint">costs.csv와 같은 계산 방식입니다.</p>
    <div class="table-wrap" tabindex="0" role="region" aria-labelledby="table-title">
      <table>
        <thead>
          <tr><th scope="col">단가</th><th scope="col">작업 수</th><th scope="col">입력 토큰</th><th scope="col">출력 토큰</th><th scope="col">입력비 $</th><th scope="col">출력비 $</th><th scope="col">총액 $</th><th scope="col">총액 원</th></tr>
        </thead>
        <tbody id="presetBody"></tbody>
      </table>
    </div>
  </section>

  <section class="specs" aria-label="모아컵 정보">
    <div class="card">
      <h2>자료로 확인된 정보</h2>
      <ul class="list" style="margin-top:10px">
        <li><span>용량</span><span>450mL <span class="badge ok">확인</span></span></li>
        <li><span>무게</span><span>280g <span class="badge ok">확인</span></span></li>
        <li><span>가격</span><span>24,900원 <span class="badge ok">확인</span></span></li>
        <li><span>소재</span><span>본체 스테인리스 · 뚜껑 폴리프로필렌 <span class="badge ok">확인</span></span></li>
        <li><span>색상</span><span>크림 / 네이비 <span class="badge ok">확인</span></span></li>
        <li><span>세척</span><span>손 세척 권장 <span class="badge ok">확인</span></span></li>
      </ul>
    </div>
    <div class="card">
      <h2>확인되지 않은 성능</h2>
      <p class="hint" style="margin-bottom:10px">아래 항목은 자료가 없어 확인되지 않았습니다. 사실이 아니라는 뜻이 아니라 근거가 없다는 뜻입니다.</p>
      <ul class="list">
        <li><span>식기세척기 사용 가능 여부</span><span class="badge no">미확인</span></li>
        <li><span>보온 시간</span><span class="badge no">미확인</span></li>
        <li><span>누수 방지</span><span class="badge no">미확인</span></li>
        <li><span>의학적 효과</span><span class="badge no">미확인</span></li>
      </ul>
    </div>
  </section>

  <footer>
    이 페이지는 외부 라이브러리, 폰트, 이미지, 네트워크 요청 없이 하나의 HTML 파일로 동작합니다. 모든 수치는 실습용 가상 자료입니다.
  </footer>
</div>

<script>
(function(){
  "use strict";

  /* ---------- 컵 시각화 ---------- */
  var N = 28;
  var cup = document.getElementById("cup");
  var stage = document.getElementById("stage");
  var rotInput = document.getElementById("rot");
  var rotOut = document.getElementById("rotOut");
  var vizColor = document.getElementById("vizColor");
  var panels = [];
  var rot = 0;
  var colorName = "크림";

  var COLORS = {
    cream: {name:"크림", body:"#EEE3CB", lid:"#D8C8A6"},
    navy:  {name:"네이비", body:"#22355F", lid:"#16223F"}
  };

  function ring(cls, r, top, h){
    var w = 2 * r * Math.tan(Math.PI / N) + 1;
    for (var i = 0; i < N; i++){
      var a = i * 360 / N;
      var el = document.createElement("div");
      el.className = "pn " + cls;
      el.style.width = w + "px";
      el.style.height = h + "px";
      el.style.left = (-w / 2) + "px";
      el.style.top = top + "px";
      el.style.transform = "rotateY(" + a + "deg) translateZ(" + r + "px)";
      el.dataset.a = a;
      cup.appendChild(el);
      panels.push(el);
    }
  }
  function disc(cls, r, y, rx){
    var el = document.createElement("div");
    el.className = "disc " + cls;
    el.style.width = (r * 2) + "px";
    el.style.height = (r * 2) + "px";
    el.style.left = (-r) + "px";
    el.style.top = (y - r) + "px";
    el.style.transform = "rotateX(" + rx + "deg)";
    cup.appendChild(el);
  }

  // 뚜껑(-107 ~ -73), 본체(-73 ~ 97), 하단 밴드(97 ~ 107)
  ring("lid", 74, -107, 35);
  ring("body", 70, -73, 171);
  ring("steel", 70, 97, 10);
  disc("top", 74, -107, 90);
  disc("bottom", 70, 107, -90);

  function shade(){
    for (var i = 0; i < panels.length; i++){
      var p = panels[i];
      var t = (Number(p.dataset.a) + rot + 35) * Math.PI / 180;
      var l = Math.cos(t);
      p.style.setProperty("--hi", (Math.max(0, l) * 0.16).toFixed(3));
      p.style.setProperty("--sh", ((1 - l) / 2 * 0.42).toFixed(3));
    }
  }

  function setRot(v, fromInput){
    v = ((Math.round(v) % 360) + 360) % 360;
    rot = v;
    cup.style.transform = "rotateX(-16deg) rotateY(" + v + "deg)";
    rotOut.textContent = v + "°";
    if (!fromInput) rotInput.value = v;
    rotInput.setAttribute("aria-valuetext", v + "도");
    stage.setAttribute("aria-label", "모아컵 CSS 3D 시각화, " + colorName + " 색상, " + v + "도 회전. 왼쪽·오른쪽 화살표 키로 회전합니다.");
    shade();
  }

  rotInput.addEventListener("input", function(){ setRot(Number(rotInput.value), true); });

  stage.addEventListener("keydown", function(e){
    if (e.key === "ArrowRight" || e.key === "ArrowUp"){ setRot(rot + 10); e.preventDefault(); }
    else if (e.key === "ArrowLeft" || e.key === "ArrowDown"){ setRot(rot - 10); e.preventDefault(); }
    else if (e.key === "Home"){ setRot(0); e.preventDefault(); }
  });

  var chips = document.querySelectorAll(".chip[data-color]");
  function setColor(key){
    var c = COLORS[key];
    if (!c) return;
    colorName = c.name;
    cup.style.setProperty("--c-body", c.body);
    cup.style.setProperty("--c-lid", c.lid);
    vizColor.textContent = c.name;
    for (var i = 0; i < chips.length; i++){
      chips[i].setAttribute("aria-pressed", chips[i].dataset.color === key ? "true" : "false");
    }
    setRot(rot);
  }
  for (var ci = 0; ci < chips.length; ci++){
    chips[ci].addEventListener("click", function(){ setColor(this.dataset.color); });
  }

  // 자동 회전 (기본 꺼짐)
  var autoBtn = document.getElementById("autoBtn");
  var autoOn = false, rafId = null, last = 0;
  function tick(ts){
    if (!autoOn) return;
    if (!last) last = ts;
    var dt = ts - last;
    if (dt > 40){ setRot(rot + 1); last = ts; }
    rafId = requestAnimationFrame(tick);
  }
  autoBtn.addEventListener("click", function(){
    autoOn = !autoOn;
    autoBtn.setAttribute("aria-pressed", autoOn ? "true" : "false");
    autoBtn.textContent = autoOn ? "자동 회전 끄기" : "자동 회전 켜기";
    if (autoOn){ last = 0; rafId = requestAnimationFrame(tick); }
    else if (rafId){ cancelAnimationFrame(rafId); }
  });

  setColor("cream");

  /* ---------- 가상 비용 계산기 ---------- */
  var PLANS = {
    ga: {name:"가형", inRate:2, outRate:10},
    na: {name:"나형", inRate:4, outRate:20}
  };
  var IN_TOK = 10000, OUT_TOK = 2000, FX = 1400, MAX_RUNS = 1000000;

  // 정수 연산: 토큰 × (100만 토큰당 달러) = 마이크로달러
  function calc(planKey, runs){
    var p = PLANS[planKey];
    var it = IN_TOK * runs, ot = OUT_TOK * runs;
    var inMicro = it * p.inRate, outMicro = ot * p.outRate;
    return {
      it: it, ot: ot,
      inUsd: inMicro / 1e6,
      outUsd: outMicro / 1e6,
      totUsd: (inMicro + outMicro) / 1e6,
      krw: Math.round((inMicro + outMicro) * FX / 1e6)
    };
  }
  var nf = new Intl.NumberFormat("ko-KR");
  function usd(n){ return "$" + n.toLocaleString("en-US", {minimumFractionDigits:2, maximumFractionDigits:2}); }
  function won(n){ return nf.format(n) + "원"; }

  var runsInput = document.getElementById("runs");
  var runsErr = document.getElementById("runsErr");
  var out = {
    it: document.getElementById("rIt"), ot: document.getElementById("rOt"),
    inU: document.getElementById("rIn"), outU: document.getElementById("rOut"),
    tot: document.getElementById("rTot"), krwS: document.getElementById("rKrwSmall"),
    krw: document.getElementById("rKrw"), label: document.getElementById("totalLabel"),
    formula: document.getElementById("formula"),
    cmpGa: document.getElementById("cmpGa"), cmpNa: document.getElementById("cmpNa"),
    barGa: document.getElementById("barGa"), barNa: document.getElementById("barNa")
  };

  function currentPlan(){
    var r = document.querySelector('input[name="plan"]:checked');
    return r ? r.value : "ga";
  }

  function validate(str){
    str = String(str).trim();
    if (str === "") return {ok:false, msg:"작업 수를 입력하세요."};
    if (!/^\d+$/.test(str)) return {ok:false, msg:"숫자만 입력하세요. 쉼표, 소수점, 음수는 사용할 수 없습니다."};
    var n = Number(str);
    if (n < 1) return {ok:false, msg:"작업 수는 1회 이상이어야 합니다."};
    if (n > MAX_RUNS) return {ok:false, msg:"작업 수는 1,000,000회 이하로 입력하세요."};
    return {ok:true, value:n};
  }

  function clearResults(){
    ["it","ot","inU","outU","tot","krwS","krw","cmpGa","cmpNa"].forEach(function(k){ out[k].textContent = "—"; });
    out.formula.textContent = "";
    out.barGa.style.width = "0";
    out.barNa.style.width = "0";
  }

  function update(){
    var v = validate(runsInput.value);
    var planKey = currentPlan();
    out.label.textContent = PLANS[planKey].name + " 총액 (원)";
    if (!v.ok){
      runsInput.setAttribute("aria-invalid", "true");
      runsErr.textContent = v.msg;
      clearResults();
      return;
    }
    runsInput.setAttribute("aria-invalid", "false");
    runsErr.textContent = "";
    var n = v.value, r = calc(planKey, n);
    out.it.textContent = nf.format(r.it);
    out.ot.textContent = nf.format(r.ot);
    out.inU.textContent = usd(r.inUsd);
    out.outU.textContent = usd(r.outUsd);
    out.tot.textContent = usd(r.totUsd);
    out.krwS.textContent = won(r.krw);
    out.krw.textContent = won(r.krw);
    var p = PLANS[planKey];
    out.formula.textContent = "계산: 입력 " + nf.format(r.it) + "토큰 × $" + p.inRate + "/100만 + 출력 " +
      nf.format(r.ot) + "토큰 × $" + p.outRate + "/100만 = " + usd(r.totUsd) + " × 1,400원";

    var a = calc("ga", n), b = calc("na", n);
    var max = Math.max(a.krw, b.krw) || 1;
    out.cmpGa.textContent = won(a.krw);
    out.cmpNa.textContent = won(b.krw);
    out.barGa.style.width = (a.krw / max * 100) + "%";
    out.barNa.style.width = (b.krw / max * 100) + "%";
  }

  runsInput.addEventListener("input", update);
  document.getElementById("calcForm").addEventListener("submit", function(e){ e.preventDefault(); update(); });
  var radios = document.querySelectorAll('input[name="plan"]');
  for (var ri = 0; ri < radios.length; ri++) radios[ri].addEventListener("change", update);
  var quick = document.querySelectorAll("[data-runs]");
  for (var qi = 0; qi < quick.length; qi++){
    quick[qi].addEventListener("click", function(){ runsInput.value = this.dataset.runs; update(); });
  }

  // 기준 표
  var body = document.getElementById("presetBody");
  ["ga","na"].forEach(function(k){
    [1,25,100,500].forEach(function(n){
      var r = calc(k, n);
      var tr = document.createElement("tr");
      [PLANS[k].name, nf.format(n), nf.format(r.it), nf.format(r.ot),
       r.inUsd.toFixed(2), r.outUsd.toFixed(2), r.totUsd.toFixed(2), nf.format(r.krw)].forEach(function(t, i){
        var cell = document.createElement(i === 0 ? "th" : "td");
        if (i === 0) cell.scope = "row";
        cell.textContent = t;
        tr.appendChild(cell);
      });
      body.appendChild(tr);
    });
  });

  update();
})();
</script>
</body>
</html>
```

**파일:** shorts.md, factcheck.csv, costs.csv, demo.html

**제한점**
- 모든 상품 정보와 단가는 가상 자료입니다. 환율은 고정값으로 가정했습니다.
- 쇼츠는 기획안만 작성했습니다. 영상과 음성은 만들지 않았고, 낭독 길이도 측정하지 않았습니다.
- demo.html은 실제 브라우저와 기기(390px, 1440px)에서 렌더링 테스트를 하지 않았습니다. CSS 3D 표현은 브라우저마다 다르게 보일 수 있습니다.
- factcheck.csv의 UNVERIFIED는 거짓이라는 판정이 아니라 근거가 없다는 뜻입니다.