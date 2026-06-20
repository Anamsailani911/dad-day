import html

import streamlit as st


st.set_page_config(
    page_title="For Abbu ❤️",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&family=DM+Sans:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,600;0,700;1,500&display=swap');

:root {
    --night: #030712;
    --navy: #07152e;
    --card: #0c1d3b;
    --blue: #2684ff;
    --electric: #65b5ff;
    --ice: #ddebff;
    --white: #f8fbff;
    --muted: #9fb4d3;
    --line: rgba(103, 174, 255, .22);
}

html, body, [data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at 12% 12%, rgba(25, 99, 210, .24), transparent 31rem),
        radial-gradient(circle at 90% 82%, rgba(0, 153, 255, .14), transparent 27rem),
        linear-gradient(145deg, var(--night), #061127 70%, #02050c) !important;
    color: var(--white);
}
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"] { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
.block-container {
    max-width: 1080px;
    padding-top: 2rem !important;
    padding-bottom: 4rem !important;
}
* { box-sizing: border-box; }
p, button, label, [data-testid="stCaptionContainer"] {
    font-family: "DM Sans", sans-serif !important;
}

.topbar {
    display: flex;
    justify-content: space-between;
    color: var(--muted);
    font: 600 10px "DM Sans", sans-serif;
    letter-spacing: .2em;
    text-transform: uppercase;
    margin-bottom: 11px;
}
.track {
    height: 3px;
    background: rgba(255,255,255,.08);
    border-radius: 99px;
    overflow: hidden;
    margin-bottom: 30px;
}
.fill {
    height: 100%;
    background: linear-gradient(90deg, var(--blue), #8ccbff);
    border-radius: 99px;
    box-shadow: 0 0 18px rgba(38,132,255,.7);
}
.scene {
    min-height: 570px;
    position: relative;
    overflow: hidden;
    border: 1px solid var(--line);
    border-radius: 28px;
    padding: clamp(34px, 6vw, 72px);
    background: linear-gradient(145deg, rgba(12,29,59,.88), rgba(3,10,24,.92));
    box-shadow: 0 30px 90px rgba(0,0,0,.45), inset 0 1px rgba(255,255,255,.05);
}
.scene::before {
    content: "";
    position: absolute;
    width: 380px;
    height: 380px;
    right: -180px;
    top: -190px;
    border-radius: 50%;
    border: 1px solid rgba(91,164,255,.16);
    box-shadow: 0 0 0 45px rgba(91,164,255,.025), 0 0 0 95px rgba(91,164,255,.018);
}
.eyebrow {
    color: var(--electric);
    font: 600 11px "DM Sans", sans-serif;
    text-transform: uppercase;
    letter-spacing: .24em;
    margin-bottom: 20px;
}
.hero {
    max-width: 880px;
    margin: 0;
    color: var(--white);
    font: 700 clamp(54px, 10vw, 108px)/.92 "Playfair Display", serif;
    letter-spacing: -.045em;
}
.hero .blue {
    background: linear-gradient(90deg, #4c9dff, #b8ddff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.headline {
    color: var(--white);
    font: 700 clamp(38px, 6vw, 68px)/1.02 "Playfair Display", serif;
    letter-spacing: -.03em;
    max-width: 840px;
    margin: 0 0 23px;
}
.intro {
    max-width: 750px;
    color: var(--ice);
    font: 300 clamp(17px, 2vw, 21px)/1.75 "DM Sans", sans-serif;
    margin-top: 28px;
}
.intro strong { color: white; font-weight: 600; }
.small {
    color: var(--muted);
    font: 400 12px "DM Sans", sans-serif;
    margin-top: 22px;
}
.heart-orbit {
    position: absolute;
    right: 8%;
    bottom: 10%;
    font-size: clamp(70px, 10vw, 120px);
    filter: drop-shadow(0 0 32px rgba(38,132,255,.46));
    animation: float 3s ease-in-out infinite;
}
@keyframes float { 0%,100%{transform:translateY(0) rotate(3deg)} 50%{transform:translateY(-12px) rotate(-3deg)} }

.quote {
    border-left: 3px solid var(--blue);
    padding: 6px 0 6px 24px;
    margin: 25px 0;
    color: #d9e9ff;
    font: 500 clamp(19px, 2.6vw, 27px)/1.55 "Playfair Display", serif;
    font-style: italic;
    max-width: 820px;
}
.chapter-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    margin-top: 30px;
}
.chapter-card {
    min-height: 150px;
    border: 1px solid var(--line);
    border-radius: 19px;
    padding: 24px;
    background: linear-gradient(145deg, rgba(22,53,101,.7), rgba(7,20,44,.75));
    transition: .22s ease;
}
.chapter-card:hover {
    border-color: rgba(101,181,255,.55);
    transform: translateY(-3px);
    box-shadow: 0 15px 32px rgba(0,0,0,.24);
}
.number {
    color: var(--electric);
    font: 600 10px "DM Sans", sans-serif;
    letter-spacing: .18em;
}
.chapter-card h3 {
    color: white;
    font: 600 25px "Playfair Display", serif;
    margin: 13px 0 8px;
}
.chapter-card p {
    color: var(--muted);
    font: 400 13px/1.55 "DM Sans", sans-serif;
    margin: 0;
}
.tap-hint {
    color: var(--electric);
    font: 500 11px "DM Sans", sans-serif;
    margin-top: 15px;
}

div[data-testid="stDialog"] > div {
    background: linear-gradient(150deg, #0c1d3b, #030814) !important;
    border: 1px solid rgba(101,181,255,.32) !important;
    border-radius: 24px !important;
    color: white !important;
    box-shadow: 0 30px 100px rgba(0,0,0,.7) !important;
}
div[data-testid="stDialog"] h1,
div[data-testid="stDialog"] h2,
div[data-testid="stDialog"] h3 { color: white !important; }
.modal-title {
    color: white;
    font: 700 clamp(29px, 5vw, 44px)/1.1 "Playfair Display", serif;
    margin: 0 0 22px;
}
.modal-copy {
    color: #d7e7fc;
    font: 400 16px/1.8 "DM Sans", sans-serif;
}
.modal-copy p { margin: 0 0 18px; }
.modal-copy strong { color: white; }
.modal-punch {
    padding: 16px 19px;
    border-radius: 13px;
    background: rgba(38,132,255,.12);
    border: 1px solid rgba(101,181,255,.24);
    color: white;
    margin: 18px 0;
    font-weight: 500;
}

.letter-preview {
    display: flex;
    align-items: center;
    gap: 19px;
    min-height: 128px;
    padding: 23px;
    border: 1px solid var(--line);
    border-radius: 17px;
    background: rgba(5,16,36,.62);
    margin-top: 12px;
}
.envelope { font-size: 39px; }
.letter-preview h3 {
    color: white;
    font: 600 22px "Playfair Display", serif;
    margin: 0 0 5px;
}
.letter-preview p { color: var(--muted); font-size: 12px; margin: 0; }
.closing {
    max-width: 760px;
    margin: 0 auto;
    text-align: center;
    padding-top: 22px;
}
.closing-heart {
    font-size: 73px;
    filter: drop-shadow(0 0 24px rgba(38,132,255,.55));
    animation: pulse 1.8s infinite ease-in-out;
}
@keyframes pulse { 0%,100%{transform:scale(1)} 50%{transform:scale(1.1)} }
.closing-title {
    color: white;
    font: 700 clamp(48px, 8vw, 83px)/1 "Playfair Display", serif;
    margin: 19px 0 23px;
}
.closing-copy {
    color: var(--ice);
    font: 400 18px/1.75 "DM Sans", sans-serif;
}
.signoff {
    color: var(--electric);
    font: 600 18px/1.6 "Playfair Display", serif;
    margin-top: 28px;
}

.stButton > button {
    width: 100%;
    min-height: 50px;
    border: 1px solid rgba(101,181,255,.55) !important;
    border-radius: 999px !important;
    color: white !important;
    background: linear-gradient(90deg, #1263d6, #258cff) !important;
    font-weight: 600 !important;
    box-shadow: 0 8px 25px rgba(18,99,214,.22);
    transition: .2s ease !important;
}
.stButton > button:hover {
    transform: translateY(-2px);
    border-color: #a8d4ff !important;
    box-shadow: 0 13px 32px rgba(18,99,214,.38);
}
.card-button .stButton > button {
    background: rgba(18,99,214,.12) !important;
    box-shadow: none;
}
.nav { height: 18px; }

@media(max-width: 720px) {
    .block-container { padding: 1rem 1rem 3rem !important; }
    .scene { padding: 34px 24px; min-height: 620px; border-radius: 21px; }
    .chapter-grid { grid-template-columns: 1fr; }
    .heart-orbit { opacity: .23; right: 3%; }
    .topbar { letter-spacing: .1em; }
}

/* Light, theme-independent redesign */
:root {
    --night: #eef6ff;
    --navy: #102b4e;
    --card: #ffffff;
    --blue: #246fca;
    --electric: #1768ba;
    --ice: #365875;
    --white: #102b4e;
    --muted: #617b95;
    --line: rgba(42, 105, 171, .18);
}
html, body, [data-testid="stAppViewContainer"] {
    color-scheme: light !important;
    background:
        radial-gradient(circle at 8% 8%, rgba(102, 174, 238, .22), transparent 27rem),
        radial-gradient(circle at 92% 82%, rgba(151, 204, 247, .24), transparent 29rem),
        linear-gradient(145deg, #f8fbff, #e8f3ff 64%, #fdfbf5) !important;
    color: var(--navy) !important;
}
.track { background: rgba(29, 82, 133, .11); }
.fill {
    background: linear-gradient(90deg, #1c67b3, #66afea);
    box-shadow: 0 0 14px rgba(36,111,202,.28);
}
.scene {
    border-color: rgba(65, 126, 184, .2);
    background:
        linear-gradient(145deg, rgba(255,255,255,.93), rgba(239,247,255,.91));
    box-shadow: 0 28px 75px rgba(42, 88, 132, .14), inset 0 1px rgba(255,255,255,.9);
}
.scene::before {
    border-color: rgba(50, 121, 189, .13);
    box-shadow: 0 0 0 45px rgba(91,164,255,.035), 0 0 0 95px rgba(91,164,255,.025);
}
.eyebrow, .number, .tap-hint, .signoff { color: #1768ba; }
.hero, .headline, .closing-title { color: #102b4e; }
.hero .blue {
    background: linear-gradient(90deg, #1768ba, #58a5e2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.intro { color: #365875; }
.intro strong { color: #102b4e; }
.quote {
    color: #193c61;
    background: rgba(212, 234, 253, .45);
    border-radius: 0 14px 14px 0;
    padding: 18px 23px;
}
.chapter-card {
    border-color: rgba(42,105,171,.18);
    background: linear-gradient(145deg, rgba(255,255,255,.98), rgba(227,241,254,.78));
    box-shadow: 0 9px 28px rgba(50, 102, 150, .08);
}
.chapter-card:hover {
    border-color: rgba(36,111,202,.42);
    box-shadow: 0 15px 32px rgba(44, 97, 146, .14);
}
.chapter-card h3 { color: #102b4e; }
.chapter-card p { color: #617b95; }
.heart-orbit {
    filter: drop-shadow(0 12px 22px rgba(36,111,202,.22));
}
.closing-copy { color: #365875; }

/* Full-page letter */
.letter-page {
    padding: clamp(22px, 4vw, 48px);
    background:
        radial-gradient(circle at 10% 5%, rgba(255, 170, 194, .26), transparent 22rem),
        radial-gradient(circle at 92% 95%, rgba(255, 118, 151, .16), transparent 24rem),
        linear-gradient(145deg, #fff8fb, #f4f8ff);
}
.letter-sheet {
    position: relative;
    max-width: 800px;
    margin: 0 auto;
    padding: clamp(38px, 7vw, 78px);
    border: 1px solid rgba(208, 102, 139, .22);
    border-radius: 9px;
    background:
        linear-gradient(rgba(255,252,252,.97), rgba(255,248,249,.97)),
        repeating-linear-gradient(0deg, transparent, transparent 31px, rgba(213,110,145,.07) 32px);
    box-shadow: 0 28px 70px rgba(123, 53, 84, .18);
    color: #49323b;
}
.letter-sheet::before {
    content: "";
    position: absolute;
    top: 18px;
    left: 18px;
    right: 18px;
    bottom: 18px;
    border: 1px solid rgba(203, 86, 128, .12);
    pointer-events: none;
}
.letter-sheet::after {
    content: "♡";
    position: absolute;
    right: 30px;
    top: 22px;
    color: #e96a96;
    font: 700 38px "Caveat", cursive;
    transform: rotate(9deg);
}
.letter-kicker {
    color: #c44b78;
    font: 700 12px "Caveat", cursive;
    text-align: right;
    letter-spacing: .08em;
    margin-bottom: 38px;
}
.letter-sheet .modal-copy {
    color: #49323b;
    font: 500 clamp(18px, 2.2vw, 21px)/1.92 "Playfair Display", serif;
}
.letter-sheet .modal-copy p { margin: 0 0 21px; }
.letter-sheet .modal-copy strong { color: #7c2949; }
.letter-dear {
    color: #9f315b;
    font: 700 clamp(38px, 6vw, 58px)/1 "Caveat", cursive !important;
    margin-bottom: 31px !important;
}
.letter-emphasis {
    color: #8e284e;
    font-size: 1.08em;
    font-style: italic;
    padding-left: 18px;
    border-left: 3px solid #ee8eae;
}
.letter-final {
    color: #ae345f;
    font: 700 clamp(29px, 4vw, 42px)/1.2 "Caveat", cursive !important;
    margin-top: 30px !important;
}
.letter-sheet .modal-punch {
    padding: 5px 0 5px 19px;
    border: 0;
    border-left: 3px solid #438dce;
    border-radius: 0;
    background: transparent;
    color: #163b60;
    font-weight: 600;
}
.letter-ending {
    margin-top: 42px;
    color: #102b4e;
    font: 500 clamp(18px, 2.3vw, 22px)/1.85 "Playfair Display", serif;
}
.letter-signature {
    margin-top: 34px;
    color: #aa315d;
    font: 700 clamp(22px, 3vw, 29px)/1.45 "Caveat", cursive;
}
.heart-note {
    position: relative;
    margin: 24px 0 28px;
    text-align: center;
}
.heart-note summary {
    display: inline-flex;
    width: 48px;
    height: 48px;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    background: linear-gradient(145deg, #ff769d, #d93467);
    color: white;
    font-size: 23px;
    cursor: pointer;
    list-style: none;
    box-shadow: 0 9px 22px rgba(199, 47, 95, .26);
    transition: transform .2s ease;
    animation: heartBeat 2.2s ease-in-out infinite;
}
.heart-note summary::-webkit-details-marker { display: none; }
.heart-note summary:hover { transform: scale(1.1) rotate(-5deg); }
.heart-note[open] summary { animation: none; transform: scale(.9); }
.heart-note div {
    max-width: 520px;
    margin: 14px auto 0;
    padding: 17px 21px;
    border: 1px solid rgba(215, 61, 109, .19);
    border-radius: 18px 18px 18px 5px;
    background: #fff0f5;
    color: #8e3152;
    font: 700 22px/1.35 "Caveat", cursive;
    box-shadow: 0 13px 30px rgba(135, 56, 84, .12);
}
.heart-hint {
    display: block;
    color: #bd6c87;
    font: 600 15px "Caveat", cursive;
    margin-top: 5px;
}
@keyframes heartBeat {
    0%, 100% { transform: scale(1); }
    12% { transform: scale(1.1); }
    24% { transform: scale(1); }
}
div[data-testid="stDialog"] > div {
    background: linear-gradient(150deg, #f9fcff, #e7f2ff) !important;
    border-color: rgba(35,106,176,.25) !important;
    color: #102b4e !important;
    box-shadow: 0 30px 90px rgba(29,71,111,.28) !important;
}
div[data-testid="stDialog"] h1,
div[data-testid="stDialog"] h2,
div[data-testid="stDialog"] h3,
.modal-title { color: #102b4e !important; }
.modal-copy { color: #294966; }
.modal-copy strong { color: #102b4e; }
.modal-punch {
    background: rgba(61,139,207,.1);
    border-color: rgba(44,117,183,.19);
    color: #153e65;
}
</style>
""",
    unsafe_allow_html=True,
)


PAGES = ["For Abbu", "Why this exists", "What you taught me", "A letter to you"]

OPENING = [
    (
        "Why a website?",
        """
        <p>I don't think words will ever be enough to tell you how much I love you, but I thought I'd try anyway.</p>
        <p>And what better way to celebrate Father's Day than by making you a website?</p>
        <div class="modal-punch">After all, this is probably the first time my engineering degree has been put to meaningful use. Consider this proof that your investment wasn't a complete waste.</div>
        """,
    ),
    (
        "Through every phase",
        """
        <p>Jokes aside, there isn't a single day that goes by where I don't realize how lucky I am to have you as my father.</p>
        <p>Through every phase of my life, every achievement, every mistake, every dramatic episode that I somehow found myself in, you've always been there.</p>
        <p>Sometimes loudly, sometimes quietly, sometimes with advice I didn't ask for, and sometimes just by standing beside me when I needed someone most.</p>
        """,
    ),
    (
        "The real reason",
        """
        <p>This little website is just my way of saying thank you.</p>
        <p>Not just for being my father.</p>
        <div class="modal-punch">But for being my Abbu. ❤️</div>
        """,
    ),
]

LESSONS = [
    (
        "You always stood by us",
        "No matter what happened, I never had to wonder if you were on my side. Whether I was right, wrong, confused, emotional, stubborn, or completely impossible to deal with, you stood there anyway.",
    ),
    (
        "You taught me to dream without limits",
        "You never placed a ceiling on my ambitions. You never told me that something was too big, too unrealistic, or impossible. Instead, you encouraged me to try, to learn, to fail, and to get back up again.",
    ),
    (
        'You redefined a "traditional father"',
        """
        <p>A lot of fathers provide for their children. You did that and so much more. You tried to understand us—our emotions, our fears, our struggles, and our perspectives.</p>
        <p>Now, are you perfect at it?</p>
        <div class="modal-punch">Absolutely not. Sometimes I genuinely think explaining my emotions to you requires a PowerPoint presentation, charts, graphs, and supporting documentation.</div>
        <p>But you try. And that effort means more than you know.</p>
        """,
    ),
    (
        "You carry everything",
        "You somehow manage to keep everything balanced, everything moving, and everything running smoothly. There is so much that happens behind the scenes that we'll probably never fully understand, but because of you, our lives have always felt secure, stable, and filled with love. And for all of that, I will always be grateful.",
    ),
]

LETTER_CHAPTERS = [
    (
        "From the very beginning",
        """
        <p>Dear Abbu,</p>
        <p>Happy Father's Day.</p>
        <p>I honestly don't know where to begin because there are some people in life who become so deeply woven into your existence that imagining life without them feels impossible. You're one of those people for me.</p>
        <p>From the very beginning, you've been there. From the moment you first saw me in the hospital, from the tiny baby who somehow managed to do a salam to you, to the grown-up version of me writing this letter today, you've been present through every chapter of my life.</p>
        <p>You've watched me take my first steps. You've watched me make good decisions. You've watched me make terrible decisions. You've watched me become the person I am today.</p>
        <div class="modal-punch">And through all of it, you've loved me anyway.</div>
        """,
    ),
    (
        "For believing in me",
        """
        <p>Thank you for giving me a life filled with opportunities.</p>
        <p>Thank you for never putting a full stop to my dreams. Thank you for encouraging me when I doubted myself. Thank you for believing in me when I didn't believe in myself.</p>
        <p>Thank you for standing beside me during some of the hardest moments of my life, especially when things hurt more than I knew how to explain.</p>
        <p>There were times when I didn't have the words to tell you what I was feeling. There were times when I was overwhelmed, emotional, stubborn, angry, frustrated, or completely lost.</p>
        <p>And while you may not always have understood everything going on in my head, you never stopped trying.</p>
        <div class="modal-punch">Even when I was a complete teenage disaster. Especially then.</div>
        """,
    ),
    (
        "The stubbornness problem",
        """
        <p>I know I haven't always made it easy. I've argued with you. I've disagreed with you. I've tested your patience more times than either of us can count.</p>
        <p>But I think part of the reason we argue so much is because we're incredibly similar.</p>
        <p><strong>We are both stubborn. We are both passionate.</strong></p>
        <div class="modal-punch">MAINLY BECAUSE: We both think we're right and, unfortunately for everyone around us, great minds really do think alike.</div>
        <p>Underneath every disagreement has always been love. A lot of love.</p>
        <p>The kind of love that doesn't disappear after an argument. The kind that survives slammed doors, eye rolls, dramatic speeches, and every “you just don't understand” moment I've ever had.</p>
        <p><strong>The kind of love that stays.</strong></p>
        """,
    ),
    (
        "The things I now see",
        """
        <p>Thank you for loving me unconditionally. Thank you for making sacrifices I'll probably never fully understand. Thank you for carrying burdens so I could focus on being a child.</p>
        <p>Thank you for working hard so our lives could be easier. Thank you for every lesson, every conversation, every piece of advice, every act of support, and every moment where you chose us over yourself.</p>
        <p>As I've grown older, I've started to realize something.</p>
        <p>The older I get, the more I understand how much you've done for us. The things that once seemed effortless now look extraordinary. The things I once took for granted now feel priceless.</p>
        <p>And while I don't say it enough, I want you to know that I see it.</p>
        <div class="modal-punch">I see you.<br>I see your efforts.<br>I see your sacrifices.<br>I see your love.</div>
        <p>And I appreciate every single bit of it.</p>
        """,
    ),
    (
        "What I hope you know",
        """
        <p>If there's one thing I hope you've always known, it's this:</p>
        <p>No matter how much I argue with you, annoy you, stress you out, or pretend I know better, I have always loved you more than words can explain.</p>
        <p>You have been my protector, my supporter, my safety net, and one of the greatest blessings in my life.</p>
        <p><strong>I am SO proud to be your daughter.</strong></p>
        <p>And I hope, more than anything, that I've made you proud too. I know that's extremely optimistic for someone who hasn't plucked shit in life, but someday I wish I make you proud.</p>
        """,
    ),
]

FULL_LETTER = """
<p class="letter-dear">Dear Abbu,</p>

<p>Happy Father's Day.</p>

<p>I honestly don't know where to begin, because there are some people who become so deeply woven into your life that imagining it without them feels impossible.</p>

<p>You're one of those people for me.</p>

<p>From the very beginning, you've been there—from the moment you first saw me in the hospital, when the tiny baby version of me somehow managed to do a salam to you, to the grown-up version of me writing this letter today.</p>

<p>You've watched me take my first steps.<br>
You've watched me make good decisions.<br>
You've watched me make terrible decisions.<br>
You've watched me become the person I am today.</p>

<p class="letter-emphasis">And through all of it, you've loved me anyway.</p>

<details class="heart-note">
<summary>♥</summary>
<span class="heart-hint">tap the heart, Abbu</span>
<div>Yes, even through every dramatic phase. That deserves an award honestly.</div>
</details>

<p>Thank you for giving me a life filled with opportunities. Thank you for never putting a full stop to my dreams. Thank you for encouraging me when I doubted myself, and for believing in me when I didn't believe in myself.</p>

<p>Thank you for standing beside me during some of the hardest moments of my life—especially when things hurt more than I knew how to explain.</p>

<p>There were times when I didn't have the words to tell you what I was feeling. Times when I was overwhelmed, emotional, stubborn, angry, frustrated, or completely lost.</p>

<p>And while you may not always have understood everything going on in my head, you never stopped trying.</p>

<p class="letter-emphasis">Even when I was a complete teenage disaster.<br>Especially then.</p>

<p>I know I haven't always made it easy. I've argued with you. I've disagreed with you. I've tested your patience more times than either of us can count.</p>

<p>But I think part of the reason we argue so much is because we're incredibly similar.</p>

<p><strong>We are both stubborn.<br>We are both passionate.<br>We both think we're right.</strong></p>

<p>And, unfortunately for everyone around us, great minds really do think alike.</p>

<p>Underneath every disagreement has always been love. A lot of love.</p>

<p>The kind of love that doesn't disappear after an argument. The kind that survives slammed doors, eye rolls, dramatic speeches, and every “you just don't understand” moment I've ever had.</p>

<p class="letter-emphasis">The kind of love that stays.</p>

<details class="heart-note">
<summary>♥</summary>
<span class="heart-hint">another little note</span>
<div>We may both be stubborn, but unfortunately for you, I inherited it from somewhere.</div>
</details>

<p>Thank you for loving me unconditionally. Thank you for making sacrifices I'll probably never fully understand. Thank you for carrying burdens so I could focus on being a child. Thank you for working hard so our lives could be easier.</p>

<p>Thank you for every lesson, every conversation, every piece of advice, every act of support, and every moment when you chose us over yourself.</p>

<p>As I've grown older, I've started to realize something:</p>

<p>The things that once seemed effortless now look extraordinary. The things I once took for granted now feel priceless.</p>

<p>And while I don't say it enough, I want you to know that I see it.</p>

<p class="letter-emphasis">I see you.<br>
I see your efforts.<br>
I see your sacrifices.<br>
I see your love.</p>

<details class="heart-note">
<summary>♥</summary>
<span class="heart-hint">one more</span>
<div>I may not say these things out loud enough, but I have always noticed more than you think.</div>
</details>

<p>And I appreciate every single bit of it.</p>

<p>If there's one thing I hope you've always known, it's this:</p>

<p>No matter how much I argue with you, annoy you, stress you out, or pretend I know better, I have always loved you more than words can explain.</p>

<p>You have been my protector, my supporter, my safety net, and one of the greatest blessings in my life.</p>

<p class="letter-emphasis">I am so proud to be your daughter.</p>

<p>And I hope, more than anything, that one day I make you just as proud. I may still be figuring my life out—and yes, that is extremely optimistic coming from someone who feels like she hasn't accomplished much yet—but someday, I will give you every reason to say, “That's my daughter.”</p>

<p>Happy Father's Day, Abbu.</p>

<p>Thank you for being the reason so much of my world feels safe.</p>

<p class="letter-final">I love you endlessly.</p>

<details class="heart-note">
<summary>♥</summary>
<span class="heart-hint">the last heart</span>
<div>Always. Even when I am arguing with you five minutes after you read this.</div>
</details>
"""


def clean(text):
    return html.escape(text)


@st.dialog("A piece of my heart", width="large")
def show_popup(title, body):
    st.markdown(
        f'<div class="modal-title">{clean(title)}</div><div class="modal-copy">{body}</div>',
        unsafe_allow_html=True,
    )


if "page" not in st.session_state:
    st.session_state.page = 0
if "celebrated" not in st.session_state:
    st.session_state.celebrated = False

page = min(st.session_state.page, len(PAGES) - 1)
st.session_state.page = page
progress = ((page + 1) / len(PAGES)) * 100

st.markdown(
    f"""
<div class="topbar"><span>Made by Anam · For Abbu</span><span>{page + 1} / {len(PAGES)} · {PAGES[page]}</span></div>
<div class="track"><div class="fill" style="width:{progress}%"></div></div>
""",
    unsafe_allow_html=True,
)

if page == 0:
    st.markdown(
        """
<section class="scene">
    <div class="eyebrow">A Father's Day story</div>
    <h1 class="hero">For my <span class="blue">Abbu.</span></h1>
    <p class="intro"><strong>Happy Father's Day, Abbu.</strong><br><br>
    I don't think words will ever be enough, but I thought I'd try anyway.</p>
    <div class="small">There are five little chapters. Take your time with them.</div>
    <div class="heart-orbit">💙</div>
</section>
""",
        unsafe_allow_html=True,
    )

elif page == 1:
    st.markdown(
        """
<section class="scene">
    <div class="eyebrow">Chapter one · Why this exists</div>
    <h1 class="headline">This is probably the first meaningful use of my engineering degree.</h1>
    <div class="quote">“Consider this proof that your investment wasn't a complete waste.”</div>
    <p class="intro">There is a serious reason too. Open each card to read the whole story.</p>
""",
        unsafe_allow_html=True,
    )
    st.markdown('<div class="chapter-grid">', unsafe_allow_html=True)
    cols = st.columns(3)
    for index, (title, body) in enumerate(OPENING):
        with cols[index]:
            st.markdown(
                f"""<div class="chapter-card"><div class="number">0{index + 1}</div>
                <h3>{clean(title)}</h3><p>A small piece of the reason behind this website.</p>
                <div class="tap-hint">OPEN THIS NOTE ↗</div></div>""",
                unsafe_allow_html=True,
            )
            if st.button("Read", key=f"opening_{index}"):
                show_popup(title, body)
    st.markdown("</div></section>", unsafe_allow_html=True)

elif page == 2:
    st.markdown(
        """
<section class="scene">
    <div class="eyebrow">Chapter two · Lessons & qualities</div>
    <h1 class="headline">Things I admire about you.</h1>
    <p class="intro">Four flashcards. Four reasons. Tap each one to turn it over.</p>
""",
        unsafe_allow_html=True,
    )
    cols = st.columns(2)
    for index, (title, body) in enumerate(LESSONS):
        with cols[index % 2]:
            st.markdown(
                f"""<div class="chapter-card"><div class="number">❤️ 0{index + 1}</div>
                <h3>{clean(title)}</h3><p>There is more behind this one.</p>
                <div class="tap-hint">FLIP THE CARD ↗</div></div>""",
                unsafe_allow_html=True,
            )
            if st.button("Open flashcard", key=f"lesson_{index}"):
                wrapped = body if "<p>" in body else f"<p>{clean(body)}</p>"
                show_popup(title, wrapped)
    st.markdown("</section>", unsafe_allow_html=True)

elif page == 3:
    st.markdown(
        f"""
<section class="scene letter-page">
    <div class="letter-sheet">
        <div class="letter-kicker">written with entirely too many feelings ♡</div>
        <div class="modal-copy">{FULL_LETTER}</div>
        <div class="letter-signature">
            Always and forever,<br><br>
            Your not-so-favourite but more emotionally available daughter,<br>
            Anam ❤️
        </div>
    </div>
</section>
""",
        unsafe_allow_html=True,
    )

st.markdown('<div class="nav"></div>', unsafe_allow_html=True)
back, _, forward = st.columns([1.2, 3, 1.7])
with back:
    if page > 0 and st.button("← Previous chapter"):
        st.session_state.page -= 1
        st.rerun()
with forward:
    if page < len(PAGES) - 1:
        labels = [
            "Start the story →",
            "What you taught me →",
            "Open my letter →",
        ]
        if st.button(labels[page]):
            st.session_state.page += 1
            st.rerun()
    elif st.button("Read it all again ↻"):
        st.session_state.page = 0
        st.session_state.celebrated = False
        st.rerun()
