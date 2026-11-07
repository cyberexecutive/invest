# -*- coding: utf-8 -*-
"""
Compilador mestre de index.html para o curso 'Como investir e gerenciar o seu dinheiro'.
Gera todas as seções, cabeçalhos, slides interativos, quizzes e certificado oficial.
"""
import os
import sys

from course_slides_data import SLIDES_DATA
from course_svg_assets import get_svg_slide_1, get_svg_generic

def generate_slide_html(slide):
    snum = slide["slide_num"]
    stype = slide["type"]
    active_cls = " active" if snum == 1 else ""

    if stype == "cover":
        cards_html = ""
        for c in slide["cards"]:
            cards_html += f'''
            <div class="info-card">
              <div class="card-header-line">
                <div class="card-icon {c['icon']}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
                <div class="card-title">{c['title']}</div>
              </div>
              <p class="card-desc">{c['desc']}</p>
            </div>'''

        svg_art = get_svg_slide_1()

        return f'''    <!-- ==========================================
         SLIDE {snum:02d}: {slide['category']}
         ========================================== -->
    <section class="slide{active_cls}" id="slide-{snum}" data-index="{snum}">
      <div class="slide-body">
        <div class="content-col">
          <div class="slide-header-block">
            <div class="slide-category">
              <span></span> {slide['category']}
            </div>
            <h1 class="slide-title">
              {slide['title']}
            </h1>
            <p class="slide-subtitle">
              {slide['subtitle']}
            </p>
          </div>

          <div class="cards-grid-3">
            {cards_html}
          </div>

          <div class="alert-callout tip">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
            <span>{slide['tip']}</span>
          </div>

          <!-- Observação de Tela Cheia para Melhor Leitura -->
          <div class="fullscreen-notice-banner">
            <div class="fs-banner-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
            </div>
            <div class="fs-banner-text">
              <strong>Visualização Otimizada:</strong> Abra o treinamento em <strong>Tela Cheia</strong> para a melhor experiência visual e leitura dos slides. Pressione <strong>F</strong> ou clique ao lado.
            </div>
            <button class="action-pill fs-action-btn" id="btn-fs-prompt" onclick="window.PresentationApp.toggleFullscreen()">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
              <span id="btn-fs-prompt-text">Abrir em Tela Cheia (F)</span>
            </button>
          </div>

          <div style="margin-top: clamp(8px, 1.4vh, 16px); display: flex; gap: 12px; align-items: center;">
            <button class="action-pill primary" id="btn-start-course" onclick="window.PresentationApp.startCourse()">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              Iniciar Treinamento
            </button>
            <button class="action-pill" onclick="window.PresentationApp.toggleModulesDrawer()">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
              Ver Grade de Aulas
            </button>
          </div>
        </div>

        <div class="visual-col">
          <div class="visual-container">
            <div class="svg-illustration">
              {svg_art}
            </div>
          </div>
        </div>
      </div>
    </section>'''

    elif stype == "lesson":
        cards_html = ""
        for c in slide["cards"]:
            cards_html += f'''
            <div class="info-card">
              <div class="card-header-line">
                <div class="card-icon {c['icon']}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
                <div class="card-title">{c['title']}</div>
              </div>
              <p class="card-desc">{c['desc']}</p>
            </div>'''

        svg_art = get_svg_generic(slide.get("svg_badge", f"AULA {snum:02d}"), slide.get("svg_icon", "chart"))

        return f'''    <!-- ==========================================
         SLIDE {snum:02d}: {slide['title']}
         ========================================== -->
    <section class="slide{active_cls}" id="slide-{snum}" data-index="{snum}">
      <div class="slide-body">
        <div class="content-col">
          <div class="slide-header-block">
            <div class="slide-category">
              <span></span> {slide['category']}
            </div>
            <h2 class="slide-title">
              {slide['title']}
            </h2>
            <p class="slide-subtitle">
              {slide['subtitle']}
            </p>
          </div>

          <div class="cards-grid-3">
            {cards_html}
          </div>

          <div class="alert-callout tip">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
            <span>{slide['tip']}</span>
          </div>
        </div>

        <div class="visual-col">
          <div class="visual-container">
            <div class="svg-illustration">
              {svg_art}
            </div>
          </div>
        </div>
      </div>
    </section>'''

    elif stype == "quiz":
        qid = slide["quiz_id"]
        opts_html = ""
        for idx, opt in enumerate(slide["options"]):
            correct_str = "true" if opt["correct"] else "false"
            opts_html += f'''
              <button class="quiz-opt-btn" data-opt-idx="{idx}" data-correct="{correct_str}">
                <div class="quiz-opt-letter">{opt['letter']}</div>
                <div class="quiz-opt-desc">{opt['desc']}</div>
                <div class="quiz-opt-zoom-btn" role="button" tabindex="0" title="Ampliar esta alternativa (sem escolher)" aria-label="Ampliar alternativa">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                </div>
              </button>'''

        svg_art = get_svg_generic(slide.get("svg_badge", f"DESAFIO {qid:02d}"), "quiz")

        return f'''    <!-- ==========================================
         SLIDE {snum:02d}: {slide['title']}
         ========================================== -->
    <section class="slide{active_cls}" id="slide-{snum}" data-index="{snum}">
      <div class="slide-body">
        <div class="content-col">
          <div class="slide-header-block">
            <div class="slide-category">
              <span></span> {slide['category']}
            </div>
            <h2 class="slide-title">
              {slide['title']}
            </h2>
            <p class="slide-subtitle">
              {slide['subtitle']}
            </p>
          </div>

          <div class="quiz-container" data-quiz-id="{qid}">
            <div class="quiz-scenario-box">
              <div class="quiz-badge-tag">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                Cenário da Vida Real
              </div>
              <p class="quiz-scenario-text">
                "{slide['scenario']}"
              </p>
            </div>

            <div class="quiz-options-list">
              {opts_html}
            </div>

            <!-- Barra de Confirmação e Cancelamento -->
            <div class="quiz-confirm-bar">
              <button class="action-pill primary btn-confirm-quiz" title="Confirmar sua resposta escolhida">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                Confirmar Resposta
              </button>
              <button class="action-pill btn-cancel-quiz" title="Cancelar escolha">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
                Cancelar
              </button>
            </div>

            <div class="quiz-feedback-box" id="quiz-feedback-{qid}" title="Clique para ampliar esta explicação em tela cheia">
              <div class="quiz-feedback-header">
                <span class="quiz-feedback-title"></span>
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span class="quiz-score-badge">+10 Pontos</span>
                  <span class="quiz-feedback-zoom-hint" title="Ampliar em tela cheia" onclick="event.stopPropagation(); window.PresentationApp.openQuizFeedbackZoom({qid})">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                  </span>
                </div>
              </div>
              <div class="quiz-feedback-text">
                {slide['feedback_text']}
              </div>
              <div class="quiz-feedback-actions">
                <button class="action-pill primary" onclick="window.PresentationApp.nextSlide()">
                  Próxima Aula →
                </button>
                <button class="action-pill" onclick="window.PresentationApp.retryQuiz({qid})">
                  Refazer Questão
                </button>
                <button class="action-pill btn-zoom-feedback" onclick="window.PresentationApp.openQuizFeedbackZoom({qid})" title="Ampliar resposta em tela cheia">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                  Ampliar em Tela Cheia
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="visual-col">
          <div class="visual-container">
            <div class="svg-illustration">
              {svg_art}
            </div>
          </div>
        </div>
      </div>
    </section>'''

    elif stype == "certificate":
        return f'''    <!-- ==========================================
         SLIDE 38: CERTIFICAÇÃO EXECUTIVA OFICIAL
         ========================================== -->
    <section class="slide{active_cls}" id="slide-38" data-index="38">
      <div class="cert-slide-content">
        <!-- Barra com Dados Oficiais do Aluno Registrado -->
        <div class="cert-registered-bar">
          <div class="cert-student-profile-badge">
            <div class="cert-profile-avatar">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            </div>
            <div class="cert-profile-info">
              <span class="cert-profile-label">Titular do Certificado Oficial:</span>
              <div class="cert-profile-data">
                <strong class="cert-profile-name" id="cert-bar-student-name">Investidor(a) Estratégico(a)</strong>
                <span class="cert-profile-dot">•</span>
                <span class="cert-profile-cpf" id="cert-bar-student-cpf">CPF: 000.000.000-00</span>
              </div>
            </div>
          </div>

          <div class="cert-status-actions">
            <div class="cert-edition-status" id="cert-edition-status">
              <span class="cert-edition-pill" id="cert-edition-pill">1ª VIA ORIGINAL</span>
            </div>
            <button class="action-pill primary btn-print-cert" id="btn-print-certificate" onclick="window.PresentationApp.printCertificate()">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
              <span id="btn-print-label">Imprimir / Salvar em PDF</span>
            </button>
          </div>
        </div>

        <!-- O Certificado Formal de Gestão Financeira & Investimentos -->
        <div class="certificate-card" id="official-certificate">
          <!-- Elementos Tecnológicos de Canto -->
          <div class="cert-corner-bracket cert-corner-tl" aria-hidden="true"></div>
          <div class="cert-corner-bracket cert-corner-tr" aria-hidden="true"></div>
          <div class="cert-corner-bracket cert-corner-bl" aria-hidden="true"></div>
          <div class="cert-corner-bracket cert-corner-br" aria-hidden="true"></div>

          <!-- Selo e Marca d'Água de 2ª Via -->
          <div class="cert-second-copy-badge" id="cert-second-copy-badge" style="display: none;">
            ★ SEGUNDA VIA OFICIAL ★
          </div>
          <div class="cert-second-copy-watermark" id="cert-second-copy-watermark" style="display: none;">
            2ª VIA OFICIAL
          </div>

          <!-- Marca D'água Tecnológica de Fundo -->
          <div class="cert-tech-watermark" aria-hidden="true">
            <svg viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="250" cy="250" r="220" stroke="currentColor" stroke-width="1.5" stroke-dasharray="6 6" />
              <circle cx="250" cy="250" r="180" stroke="currentColor" stroke-width="1" />
              <circle cx="250" cy="250" r="140" stroke="currentColor" stroke-width="2" stroke-dasharray="12 4" />
              <path d="M250 30 V110 M250 390 V470 M30 250 H110 M390 250 H470" stroke="currentColor" stroke-width="2" />
              <path d="M95 95 L150 150 M350 350 L405 405 M405 95 L350 150 M150 350 L95 405" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 4" />
              <!-- Cifrão / Moeda de Ouro no Centro -->
              <circle cx="250" cy="250" r="45" stroke="currentColor" stroke-width="2.5" fill="none" />
              <path d="M235 260 L245 235 L255 245 L265 225" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </div>

          <div class="cert-header">
            <!-- Brasão Oficial Centralizado no Topo -->
            <div class="cert-crest-wrap">
              <img src="imagens/logo-cyber-executive.png?v=4.7" alt="Brasão Oficial Cyber Executive" class="cert-top-crest" width="64" height="64" decoding="async" />
            </div>

            <div class="cert-badge-ribbon">
              ★ FORMAÇÃO EXECUTIVA OFICIAL ★
            </div>

            <h1 class="cert-title">Formação Executiva em Gestão Financeira &amp; Investimentos Estratégicos</h1>
            <p class="cert-sub">EDUCAÇÃO FINANCEIRA • RENDA FIXA • AÇÕES &amp; FIIS • CRIPTOATIVOS • ALOCAÇÃO GLOBAL</p>
          </div>

          <div class="cert-body">
            <p class="cert-certifies">Certificamos com distinção e reconhecimento profissional que</p>
            <div class="cert-student-name-display" id="cert-display-name">Investidor(a) Estratégico(a)</div>
            <div class="cert-student-cpf-display" id="cert-display-cpf">CPF: 000.000.000-00</div>
            <p class="cert-statement">
              concluiu com êxito o treinamento prático e executivo <strong>Como Investir e Gerenciar o Seu Dinheiro</strong>,
              demonstrando proficiência comprovada em Planejamento Orçamentário Estratégico, Eliminação de Dívidas e Formação de Reserva de Emergência,
              Rentabilização em Renda Fixa Inteligente (Tesouro Direto, CDBs, LCIs/LCAs), Seleção e Acumulação de Ações de Valor e Fundos Imobiliários (FIIs),
              Custódia Segura e Estratégias em Criptoativos/Bitcoin, e Construção de Carteira Blindada com Alocação Global e Rebalanceamento Periódico.
            </p>

            <!-- Metadados de Carga Horária, Data e Aproveitamento -->
            <div class="cert-meta-grid">
              <div class="cert-meta-card">
                <div class="cert-meta-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                </div>
                <div class="cert-meta-text">
                  <span class="cert-meta-label">Carga Horária</span>
                  <span class="cert-meta-val">6 Horas • Executivo</span>
                </div>
              </div>

              <div class="cert-meta-card">
                <div class="cert-meta-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                </div>
                <div class="cert-meta-text">
                  <span class="cert-meta-label">Data de Conclusão</span>
                  <span class="cert-meta-val" id="cert-date-display">04 de Novembro de 2026</span>
                </div>
              </div>

              <div class="cert-meta-card">
                <div class="cert-meta-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>
                </div>
                <div class="cert-meta-text">
                  <span class="cert-meta-label">Aproveitamento</span>
                  <span class="cert-meta-val">100% • Aprovado</span>
                </div>
              </div>
            </div>
          </div>

          <div class="cert-footer-row">
            <!-- Assinatura Centralizada da Direção / CEO -->
            <div class="cert-signature-box central">
              <div class="cert-signature-space" title="Assinatura Digital Oficial">
                <img src="imagens/assinatura-ceo.png" alt="Assinatura Claudinei Gonçalves de Lima" class="cert-signature-img" />
              </div>
              <div class="cert-signature-line"></div>
              <div class="cert-signature-name">Claudinei Gonçalves de Lima</div>
              <div class="cert-signature-role">CEO - Strategic Financial Planning &amp; Corporate Management</div>
              <div class="cert-code-tag" id="cert-auth-code">INV-2026-8942-BR</div>
              <div class="cert-second-copy-note" id="cert-second-copy-note" style="display: none;">
                1ª Emissão Original em <span id="cert-orig-date">--</span> • Via registrada pelo titular acadêmico.
              </div>
            </div>
          </div>
        </div>

        <div class="cert-actions-bar">
          <button class="action-pill" onclick="window.PresentationApp.goToSlide(1)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
            Voltar ao Início
          </button>
          <button class="action-pill" onclick="window.PresentationApp.restartCourse()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="1 4 1 10 7 10"/><polyline points="23 20 23 14 17 14"/><path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"/></svg>
            Reiniciar Treinamento
          </button>
        </div>
      </div>
    </section>'''

def compile_index_html():
    slides_body = ""
    for s in SLIDES_DATA:
        slides_body += generate_slide_html(s) + "\n\n"

    full_html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Como Investir e Gerenciar o Seu Dinheiro | Formação Prática 2026</title>
  <meta name="description" content="Como Investir e Gerenciar o Seu Dinheiro. Formação interativa e prática: mentalidade financeira, eliminação de dívidas, renda fixa inteligente, ações de dividendos, fundos imobiliários, criptoativos e alocação global blindada.">
  <meta name="keywords" content="como investir e gerenciar dinheiro, educação financeira, renda fixa, tesouro direto, ações dividendos, fundos imobiliários fiis, bitcoin criptoativos, orçamento pessoal">
  <meta name="author" content="Claudinei Gonçalves de Lima | Cyber Executive">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#090d16">

  <!-- Favicon e Ícones Oficiais -->
  <link rel="icon" type="image/svg+xml" href="imagens/logo-cyber-executive.svg?v=4.7">
  <link rel="icon" type="image/png" sizes="32x32" href="imagens/favicon-32x32.png?v=4.7">
  <link rel="icon" type="image/png" sizes="16x16" href="imagens/favicon-16x16.png?v=4.7">
  <link rel="shortcut icon" href="favicon.ico?v=4.7">
  <link rel="apple-touch-icon" sizes="180x180" href="imagens/apple-touch-icon.png?v=4.7">

  <!-- Canonical URL -->
  <link rel="canonical" href="https://cyberexecutive.github.io/invest/">

  <!-- Open Graph -->
  <meta property="og:site_name" content="Invest Pro 2026">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://cyberexecutive.github.io/invest/">
  <meta property="og:title" content="Como Investir e Gerenciar o Seu Dinheiro">
  <meta property="og:description" content="Formação 100% interativa: 6 módulos estratégicos, 6 desafios práticos com tomada de decisão da vida real e Certificado Oficial com validação criptográfica.">
  <meta property="og:image" content="https://cyberexecutive.github.io/invest/imagens/anuncio-hotmart-1x1.jpg">
  <meta property="og:image:alt" content="Como Investir e Gerenciar o Seu Dinheiro - Formação 2026">
  <meta property="og:locale" content="pt_BR">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Como Investir e Gerenciar o Seu Dinheiro | Formação 2026">
  <meta name="twitter:description" content="Aprenda a investir do zero ao avançado, dominar seu orçamento, lucrar com ações e se proteger com alocação global.">
  <meta name="twitter:image" content="https://cyberexecutive.github.io/invest/imagens/anuncio-hotmart-1x1.jpg">

  <link rel="stylesheet" href="css/styles.css?v=5.0">
  
</head>
<body>

  <!-- Barra de Progresso Linear Superior -->
  <div id="top-progress-bar"></div>

  <!-- Cabeçalho Fixo Superior -->
  <header class="top-header">
    <div class="brand-badge">
      <img src="imagens/logo-cyber-executive.png?v=4.7" alt="Cyber Executive Logo" class="brand-badge-logo" />
      <span>INVEST • COMO INVESTIR E GERENCIAR O SEU DINHEIRO</span>
    </div>

    <div class="header-actions">
      <!-- Badge de Acesso / Botão de Desbloqueio do Aluno -->
      <div id="access-status-container">
        <button class="header-pill-badge" id="btn-header-unlock" title="Status de Acesso do Treinamento">
          <span class="badge-dot" id="access-badge-dot"></span>
          <span id="access-badge-text">⚡ Demonstração Gratuita</span>
          <span class="badge-action" id="badge-action-label">• 🔑 Já sou Aluno</span>
        </button>
      </div>

      <!-- Botão Página de Vendas (Landing Page) -->
      <a href="landing.html" class="header-btn" title="Página de Apresentação e Vendas (Landing Page)" style="text-decoration: none;">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/>
          <line x1="3" y1="6" x2="21" y2="6"/>
          <path d="M16 10a4 4 0 0 1-8 0"/>
        </svg>
      </a>

      <!-- Botão Trilha de Módulos (Menu Lateral) -->
      <button class="header-btn" id="btn-modules" title="Trilha de Módulos (M)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>

      <!-- Botão Modo Claro/Escuro -->
      <button class="header-btn" id="btn-theme" title="Alternar Modo Escuro / Claro (T)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="5"/>
          <line x1="12" y1="1" x2="12" y2="3"/>
          <line x1="12" y1="21" x2="12" y2="23"/>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
          <line x1="1" y1="12" x2="3" y2="12"/>
          <line x1="21" y1="12" x2="23" y2="12"/>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
        </svg>
      </button>

      <!-- Botão Visão Geral de Todos os Slides -->
      <button class="header-btn" id="btn-overview" title="Grade de Slides (G)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="3" y="3" width="7" height="7"/>
          <rect x="14" y="3" width="7" height="7"/>
          <rect x="14" y="14" width="7" height="7"/>
          <rect x="3" y="14" width="7" height="7"/>
        </svg>
      </button>

      <!-- Botão Ajuda / Atalhos -->
      <button class="header-btn" id="btn-help" title="Atalhos do Teclado (?)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"/>
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
          <line x1="12" y1="17" x2="12.01" y2="17"/>
        </svg>
      </button>

      <!-- Botão Tela Cheia -->
      <button class="header-btn" id="btn-fullscreen" title="Modo Tela Cheia (F)">
        <svg id="fs-icon-enter" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/>
        </svg>
        <svg id="fs-icon-exit" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:none;">
          <path d="M8 3v3a2 2 0 0 1-2 2H3m18 0h-3a2 2 0 0 1-2-2V3m0 18v-3a2 2 0 0 1 2-2h3M3 16h3a2 2 0 0 1 2 2v3"/>
        </svg>
      </button>
    </div>
  </header>

  <!-- Drawer Lateral: Trilha dos 6 Módulos -->
  <aside class="modules-drawer" id="modules-drawer">
    <div class="drawer-overlay" id="drawer-overlay"></div>
    <div class="drawer-panel">
      <div class="drawer-header">
        <div>
          <h3 style="display: flex; align-items: center; gap: 8px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.5"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
            Trilha do Curso
          </h3>
          <p>6 Módulos • 6 Desafios Práticos • Certificado Oficial</p>
        </div>
        <button class="drawer-close-btn" id="close-drawer-btn" title="Fechar Menu (Esc)">✕</button>
      </div>

      <div class="drawer-progress-box">
        <div class="drawer-progress-labels">
          <span>Progresso do Aluno</span>
          <span id="drawer-progress-percent">0%</span>
        </div>
        <div class="drawer-progress-track">
          <div class="drawer-progress-bar" id="drawer-progress-bar"></div>
        </div>
      </div>

      <div class="drawer-modules-list" id="drawer-modules-container">
        <!-- Preenchido dinamicamente pelo JS com status de conclusão e notas -->
      </div>
    </div>
  </aside>

  <!-- Viewport Principal de Apresentação dos Slides -->
  <main id="presentation-viewport">

{slides_body}

  </main>

  <!-- Barra de Controles Flutuante Inferior (Dock) -->
  <footer class="bottom-dock">
    <div class="dock-controls">
      <button class="dock-btn" id="btn-prev" title="Slide Anterior (←)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 18 9 12 15 6"/>
        </svg>
      </button>

      <div class="dock-counter">
        <span class="current-num">01</span> / <span class="total-num">38</span>
      </div>

      <button class="dock-btn" id="btn-next" title="Próximo Slide (→)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"/>
        </svg>
      </button>
    </div>

    <div class="dock-divider"></div>

    <div class="dock-dots" id="dock-dots-container">
      <!-- Gerado dinamicamente pelo JS -->
    </div>
  </footer>

  <!-- Modal de Visão Geral (Overview Grid) -->
  <div class="modal-overlay" id="overview-modal">
    <div class="overview-content">
      <div class="overview-header">
        <h3>Índice e Grade de Slides do Curso (38 Slides)</h3>
        <button class="close-modal-btn" id="close-overview-btn" title="Fechar (Esc)">✕</button>
      </div>
      <div class="overview-grid" id="overview-grid">
        <!-- Preenchido dinamicamente pelo JS -->
      </div>
    </div>
  </div>

  <!-- Modal de Ajuda e Atalhos -->
  <div class="modal-overlay" id="help-modal">
    <div class="overview-content" style="max-width: 650px;">
      <div class="overview-header">
        <h3>Atalhos e Dicas de Navegação</h3>
        <button class="close-modal-btn" id="close-help-btn" title="Fechar (Esc)">✕</button>
      </div>

      <div class="shortcuts-grid">
        <div class="shortcut-row">
          <span>Próxima Aula / Slide</span>
          <div>
            <span class="shortcut-key">→</span>
            <span class="shortcut-key">Espaço</span>
            <span class="shortcut-key">PgDn</span>
          </div>
        </div>

        <div class="shortcut-row">
          <span>Aula Anterior</span>
          <div>
            <span class="shortcut-key">←</span>
            <span class="shortcut-key">Backspace</span>
            <span class="shortcut-key">PgUp</span>
          </div>
        </div>

        <div class="shortcut-row">
          <span>Trilha de Módulos (Menu)</span>
          <span class="shortcut-key">M</span>
        </div>

        <div class="shortcut-row">
          <span>Tela Cheia</span>
          <span class="shortcut-key">F</span>
        </div>

        <div class="shortcut-row">
          <span>Grade de Miniaturas</span>
          <span class="shortcut-key">G</span> ou <span class="shortcut-key">O</span>
        </div>

        <div class="shortcut-row">
          <span>Alternar Modo Claro/Escuro</span>
          <span class="shortcut-key">T</span>
        </div>

        <div class="shortcut-row">
          <span>Fechar Modais / Zoom</span>
          <span class="shortcut-key">Esc</span>
        </div>
      </div>

      <div class="alert-callout tip">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
        <span>Você pode clicar em qualquer card, caixa de cenário ou ilustração para <strong>ampliar</strong> em tela cheia com facilidade!</span>
      </div>
    </div>
  </div>

  <!-- Modal de Card Ampliado (Zoom Modal) -->
  <div class="card-modal-overlay" id="card-zoom-modal" aria-hidden="true">
    <div class="card-modal-container" id="card-zoom-container">
      <button class="card-modal-close" id="card-zoom-close-btn" title="Fechar (Esc ou clique fora)" aria-label="Fechar card ampliado">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
      <div class="card-modal-content" id="card-zoom-content">
        <!-- Conteúdo do card ampliado inserido dinamicamente via JS -->
      </div>
    </div>
  </div>

  <!-- Modal de Paywall / Trava de Demonstração -->
  <div class="modal-overlay" id="paywall-modal" aria-hidden="true">
    <div class="overview-content paywall-card-container">
      <button class="close-modal-btn" id="close-paywall-btn" title="Fechar (Esc)">✕</button>
      
      <div class="paywall-header">
        <div class="paywall-badge">
          🔒 CONTEÚDO EXCLUSIVO PARA ALUNOS
        </div>
        <h2 class="paywall-title">Você Concluiu a <span class="highlight-cyan">Demonstração Gratuita</span>!</h2>
        <p class="paywall-subtitle">
          Parabéns por completar as aulas do <strong>Módulo 01 (Mentalidade Financeira &amp; O Jogo do Dinheiro)</strong>. Para continuar sua formação prática e desbloquear todos os <strong>6 Módulos Completos (38 Slides)</strong> e o <strong>Certificado Oficial Executivo</strong>, garanta seu acesso com desconto especial de lançamento.
        </p>
      </div>

      <div class="paywall-benefits-list">
        <div class="paywall-benefit-item">
          <div class="paywall-benefit-icon">📈</div>
          <div>
            <strong>6 Módulos Completos sem Restrições (38 Aulas Práticas)</strong>
            <span>Orçamento 50/30/20, Faxina de Dívidas, Tesouro Direto, CDB/LCI/LCA, Ações, FIIs, Bitcoin e Portfólio Global</span>
          </div>
        </div>
        <div class="paywall-benefit-item">
          <div class="paywall-benefit-icon">🎯</div>
          <div>
            <strong>6 Desafios Práticos da Vida Real com Tomada de Decisão</strong>
            <span>Simulações bem-humoradas com pontuação individual e feedback estratégico imediato</span>
          </div>
        </div>
        <div class="paywall-benefit-item">
          <div class="paywall-benefit-icon">📜</div>
          <div>
            <strong>Certificado Oficial Executivo (6 Horas)</strong>
            <span>Personalizado com seu nome, CPF, código criptográfico INV-2026 e assinatura executiva</span>
          </div>
        </div>
      </div>

      <div class="paywall-action-box">
        <div class="paywall-price-info">
          <span class="paywall-price-label">Acesso Vitalício por apenas:</span>
          <div class="paywall-price-value">R$ 47<small>,00</small> <span class="paywall-price-sub">(ou 5x de R$ 10,25)</span></div>
        </div>
        <div class="paywall-dual-buttons">
          <a href="https://pay.kiwify.com.br/SVqQtZZ" class="paywall-cta-btn paywall-btn-kiwify" id="btn-paywall-kiwify" target="_blank" rel="noopener" style="border-radius: 9999px !important;">
            PAGAR VIA KIWIFY
          </a>
          <a href="https://pay.hotmart.com/T108385988V" class="paywall-cta-btn paywall-btn-hotmart" id="btn-paywall-hotmart" target="_blank" rel="noopener" style="border-radius: 9999px !important;">
            PAGAR VIA HOTMART
          </a>
        </div>
      </div>

      <div class="paywall-footer-hint">
        <span>Já adquiriu o treinamento?</span>
        <button type="button" class="paywall-unlock-link" id="btn-paywall-enter-key">Inserir Chave de Acesso do Aluno</button>
      </div>
    </div>
  </div>

  <!-- Modal para Inserir Chave de Acesso -->
  <div class="modal-overlay" id="unlock-modal" aria-hidden="true">
    <div class="overview-content unlock-card-container">
      <button class="close-modal-btn" id="close-unlock-btn" title="Fechar (Esc)">✕</button>
      
      <div class="unlock-icon-circle">🔑</div>
      <h3 class="unlock-title">Ativação de Acesso do Aluno</h3>
      <p class="unlock-desc">Digite sua chave de aluno ou a chave master de gestão do treinamento:</p>
      
      <form id="form-unlock-key" onsubmit="return false;" class="unlock-form">
        <div class="unlock-input-wrap">
          <input type="text" id="input-unlock-key" class="unlock-input" placeholder="Ex: INVEST-PRO-2026 ou GESTOR" autocomplete="off" spellcheck="false" autocapitalize="characters" />
          <button type="submit" class="action-pill primary" id="btn-submit-unlock">Ativar Acesso</button>
        </div>
        <div class="unlock-status-msg" id="unlock-status-msg"></div>
      </form>

      <p class="unlock-support-note">
        Dúvidas com o seu acesso? Verifique o e-mail cadastrado na compra ou fale com nosso suporte executivo.
      </p>
    </div>
  </div>

  <!-- Modal de Identificação Obrigatória do Aluno -->
  <div class="modal-overlay" id="student-id-modal" aria-hidden="true">
    <div class="overview-content student-id-card">
      <div class="student-id-header">
        <div class="student-id-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        </div>
        <h3 class="student-id-title">Identificação Oficial do Aluno</h3>
        <p class="student-id-subtitle">
          Informe seu <strong>Nome Completo</strong> e <strong>CPF</strong> para personalização automática do seu Certificado Executivo Oficial.
        </p>
      </div>

      <form id="student-id-form" onsubmit="event.preventDefault(); window.PresentationApp.submitStudentRegistration();" class="student-id-form">
        <div class="student-id-field">
          <label for="input-reg-name">Nome Completo do Aluno *</label>
          <input type="text" id="input-reg-name" class="student-id-input" placeholder="Ex: Carlos Eduardo de Oliveira" required autocomplete="name" />
          <span class="field-hint">Nome que constará oficialmente no seu Certificado de Conclusão.</span>
        </div>

        <div class="student-id-field">
          <label for="input-reg-cpf">CPF do Aluno *</label>
          <input type="text" id="input-reg-cpf" class="student-id-input" placeholder="000.000.000-00" maxlength="14" required autocomplete="off" />
          <span class="field-hint">Registro oficial para autenticidade e validação antifraude.</span>
        </div>

        <div class="student-id-error-msg" id="student-id-error-msg"></div>

        <div class="student-id-actions">
          <button type="submit" class="action-pill primary btn-confirm-reg">
            Salvar Dados e Iniciar Treinamento →
          </button>
        </div>
      </form>
    </div>
  </div>

  <!-- Toast Flutuante de Notificação -->
  <div id="course-toast" class="course-toast" aria-live="polite"></div>

  
  <script src="js/presentation.js?v=5.0"></script>
</body>
</html>'''

    output_path = r"C:\invest\index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Sucesso! Gerado index.html com {len(SLIDES_DATA)} slides em {output_path}")

if __name__ == "__main__":
    compile_index_html()
