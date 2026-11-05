# -*- coding: utf-8 -*-
import re

html_path = r"C:\invest\index.html"
js_path = r"C:\invest\js\presentation.js"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

# 1. Checa contagem de slides
slides = re.findall(r'<section class="slide[^"]*" id="slide-(\d+)" data-index="(\d+)">', html)
print(f"Total de slides encontrados em index.html: {len(slides)}")
assert len(slides) == 38, f"Esperado 38 slides, encontrado {len(slides)}"

# 2. Checa contagem de quizzes
quizzes = re.findall(r'<div class="quiz-container" data-quiz-id="(\d+)">', html)
print(f"Total de quizzes encontrados: {len(quizzes)}")
assert len(quizzes) == 6, f"Esperado 6 quizzes, encontrado {len(quizzes)}"

# 3. Checa alternativas e botões de confirmação para cada quiz
for q in quizzes:
    assert f'data-quiz-id="{q}"' in html
    assert f'id="quiz-feedback-{q}"' in html
    # Verifica se há pelo menos uma alternativa correta
    block = html.split(f'data-quiz-id="{q}"')[1].split('</div>\n          </div>\n        </div>')[0]
    assert 'data-correct="true"' in block, f"Quiz {q} não tem alternativa correta!"
    assert 'data-correct="false"' in block, f"Quiz {q} não tem alternativa incorreta!"

# 4. Checa IDs vitais do DOM usados em presentation.js
vital_ids = [
    "top-progress-bar",
    "access-status-container",
    "btn-header-unlock",
    "access-badge-dot",
    "access-badge-text",
    "badge-action-label",
    "btn-modules",
    "btn-theme",
    "btn-overview",
    "btn-help",
    "btn-fullscreen",
    "modules-drawer",
    "close-drawer-btn",
    "drawer-progress-percent",
    "drawer-progress-bar",
    "drawer-modules-container",
    "btn-prev",
    "btn-next",
    "dock-dots-container",
    "overview-modal",
    "overview-grid",
    "close-overview-btn",
    "help-modal",
    "close-help-btn",
    "card-zoom-modal",
    "card-zoom-container",
    "card-zoom-close-btn",
    "card-zoom-content",
    "paywall-modal",
    "close-paywall-btn",
    "btn-paywall-kiwify",
    "btn-paywall-hotmart",
    "btn-paywall-enter-key",
    "unlock-modal",
    "close-unlock-btn",
    "form-unlock-key",
    "input-unlock-key",
    "btn-submit-unlock",
    "unlock-status-msg",
    "student-id-modal",
    "student-id-form",
    "input-reg-name",
    "input-reg-cpf",
    "student-id-error-msg",
    "course-toast",
    "official-certificate",
    "cert-bar-student-name",
    "cert-bar-student-cpf",
    "cert-edition-status",
    "cert-edition-pill",
    "btn-print-certificate",
    "cert-second-copy-badge",
    "cert-second-copy-watermark",
    "cert-display-name",
    "cert-display-cpf",
    "cert-date-display",
    "cert-auth-code",
    "cert-second-copy-note",
    "cert-orig-date"
]

missing = [i for i in vital_ids if f'id="{i}"' not in html]
if missing:
    print(f"ATENÇÃO: IDs faltantes em index.html: {missing}")
    assert False
else:
    print(f"Todos os {len(vital_ids)} IDs essenciais foram verificados com 100% de sucesso!")

print("VERIFICAÇÃO COMPLETA: O curso está 100% íntegro e pronto para produção!")
