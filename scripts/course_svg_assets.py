# -*- coding: utf-8 -*-
"""
Helper com ilustrações vetoriais (SVGs) exclusivas para cada slide do curso de investimentos.
Estilo moderno, fintech, clean, com gradientes e elementos visuais de alto impacto.
"""

def get_svg_slide_1():
    return '''<svg viewBox="0 0 500 400" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="cov-glow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#10b981" stop-opacity="0.35" />
          <stop offset="100%" stop-color="#10b981" stop-opacity="0" />
        </radialGradient>
        <linearGradient id="cov-gold" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#f59e0b" />
          <stop offset="50%" stop-color="#10b981" />
          <stop offset="100%" stop-color="#06b6d4" />
        </linearGradient>
      </defs>
      <circle cx="250" cy="200" r="160" fill="url(#cov-glow)" />
      <circle cx="250" cy="200" r="140" fill="none" stroke="#10b981" stroke-width="1.5" stroke-dasharray="8 6" opacity="0.4" class="anim-rotate" />
      <circle cx="250" cy="200" r="110" fill="none" stroke="#f59e0b" stroke-width="1" stroke-dasharray="4 8" opacity="0.5" />
      <!-- Cofre / Escudo de Liberdade Financeira -->
      <g transform="translate(250, 200)">
        <polygon points="0,-85 70,-45 70,45 0,85 -70,45 -70,-45" fill="rgba(15,23,42,0.9)" stroke="url(#cov-gold)" stroke-width="3" />
        <!-- Moeda de Ouro Central com Símbolo de Crescimento -->
        <circle cx="0" cy="0" r="42" fill="#0f172a" stroke="#f59e0b" stroke-width="2.5" />
        <path d="M-18,12 L-4,-4 L8,8 L20,-14" fill="none" stroke="#10b981" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
        <polyline points="12,-14 20,-14 20,-6" fill="none" stroke="#10b981" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
        <!-- Cifrão Estilizado -->
        <text x="0" y="26" fill="#f59e0b" font-size="14" font-weight="900" text-anchor="middle" font-family="sans-serif">R$</text>
      </g>
      <!-- Barras de Crescimento em Degraus -->
      <g transform="translate(250, 315)">
        <rect x="-80" y="-12" width="160" height="24" rx="12" fill="rgba(15,23,42,0.85)" stroke="#10b981" stroke-width="1.5" />
        <text x="0" y="4" fill="#34d399" font-size="10.5" font-weight="800" text-anchor="middle" letter-spacing="1">GESTÃO &amp; INVESTIMENTOS 2026</text>
      </g>
    </svg>'''

def get_svg_generic(badge_text, icon_type="chart"):
    if icon_type == "scale":
        inner = '''<line x1="180" y1="170" x2="320" y2="170" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
                   <polygon points="250,140 240,170 260,170" fill="#06b6d4"/>
                   <line x1="250" y1="170" x2="250" y2="250" stroke="#64748b" stroke-width="4"/>
                   <line x1="210" y1="250" x2="290" y2="250" stroke="#64748b" stroke-width="4"/>
                   <circle cx="180" cy="205" r="26" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
                   <text x="180" y="210" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">Passivos</text>
                   <circle cx="320" cy="185" r="28" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
                   <text x="320" y="190" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Ativos</text>'''
    elif icon_type == "buffett":
        inner = '''<circle cx="250" cy="200" r="75" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6 4"/>
                   <circle cx="250" cy="200" r="50" fill="#0f172a" stroke="#10b981" stroke-width="3"/>
                   <text x="250" y="195" fill="#f59e0b" font-size="28" font-weight="900" text-anchor="middle">1º</text>
                   <text x="250" y="215" fill="#94a3b8" font-size="10" font-weight="700" text-anchor="middle">PRESERVAR</text>
                   <path d="M190,260 Q250,220 310,130" fill="none" stroke="#34d399" stroke-width="4" stroke-linecap="round"/>
                   <circle cx="310" cy="130" r="6" fill="#10b981"/>'''
    elif icon_type == "compound":
        inner = '''<path d="M150,270 L190,265 L230,250 L270,225 L310,180 L350,110" fill="none" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>
                   <path d="M150,270 L350,270" stroke="#334155" stroke-width="2"/>
                   <circle cx="350" cy="110" r="8" fill="#f59e0b"/>
                   <text x="350" y="95" fill="#f59e0b" font-size="12" font-weight="800" text-anchor="middle">R$ Exponencial</text>
                   <text x="250" y="290" fill="#64748b" font-size="11" font-weight="600" text-anchor="middle">Tempo &amp; Paciência (Anos)</text>'''
    elif icon_type == "jars":
        inner = '''<g transform="translate(170, 200)">
                     <rect x="-24" y="-35" width="48" height="70" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
                     <text x="0" y="5" fill="#06b6d4" font-size="11" font-weight="800" text-anchor="middle">50%</text>
                     <text x="0" y="52" fill="#94a3b8" font-size="9" font-weight="700" text-anchor="middle">Básico</text>
                   </g>
                   <g transform="translate(250, 195)">
                     <rect x="-24" y="-40" width="48" height="80" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
                     <text x="0" y="5" fill="#f59e0b" font-size="11" font-weight="800" text-anchor="middle">30%</text>
                     <text x="0" y="58" fill="#94a3b8" font-size="9" font-weight="700" text-anchor="middle">Reserva</text>
                   </g>
                   <g transform="translate(330, 190)">
                     <rect x="-24" y="-45" width="48" height="90" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2.5"/>
                     <text x="0" y="5" fill="#10b981" font-size="11" font-weight="800" text-anchor="middle">20%</text>
                     <text x="0" y="63" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">Liberdade</text>
                   </g>'''
    elif icon_type == "audit":
        inner = '''<circle cx="230" cy="190" r="50" fill="none" stroke="#06b6d4" stroke-width="4"/>
                   <line x1="265" y1="225" x2="310" y2="270" stroke="#06b6d4" stroke-width="8" stroke-linecap="round"/>
                   <circle cx="230" cy="190" r="38" fill="#0f172a"/>
                   <text x="230" y="185" fill="#ef4444" font-size="14" font-weight="900" text-anchor="middle">RALO</text>
                   <text x="230" y="202" fill="#f87171" font-size="9" font-weight="700" text-anchor="middle">-R$ 380/mês</text>'''
    elif icon_type == "quiz":
        inner = '''<polygon points="250,110 320,150 320,240 250,280 180,240 180,150" fill="#0f172a" stroke="#f59e0b" stroke-width="3" />
                   <text x="250" y="205" fill="#f59e0b" font-size="44" font-weight="900" text-anchor="middle">?</text>
                   <circle cx="250" cy="200" r="65" fill="none" stroke="#10b981" stroke-width="1.5" stroke-dasharray="6 4"/>'''
    elif icon_type == "budget":
        inner = '''<circle cx="250" cy="200" r="70" fill="none" stroke="#06b6d4" stroke-width="16" stroke-dasharray="220 220"/>
                   <circle cx="250" cy="200" r="70" fill="none" stroke="#f59e0b" stroke-width="16" stroke-dasharray="130 310" stroke-dashoffset="-220"/>
                   <circle cx="250" cy="200" r="70" fill="none" stroke="#10b981" stroke-width="16" stroke-dasharray="90 350" stroke-dashoffset="-350"/>
                   <text x="250" y="195" fill="#f8fafc" font-size="16" font-weight="900" text-anchor="middle">50/30/20</text>
                   <text x="250" y="215" fill="#94a3b8" font-size="10" font-weight="700" text-anchor="middle">EQUILÍBRIO</text>'''
    elif icon_type == "trash":
        inner = '''<rect x="210" y="170" width="80" height="90" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2.5"/>
                   <line x1="200" y1="160" x2="300" y2="160" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
                   <path d="M235,160 V150 H265 V160" fill="none" stroke="#ef4444" stroke-width="2.5"/>
                   <line x1="235" y1="185" x2="235" y2="235" stroke="#f87171" stroke-width="2" stroke-linecap="round"/>
                   <line x1="250" y1="185" x2="250" y2="235" stroke="#f87171" stroke-width="2" stroke-linecap="round"/>
                   <line x1="265" y1="185" x2="265" y2="235" stroke="#f87171" stroke-width="2" stroke-linecap="round"/>
                   <text x="250" y="285" fill="#10b981" font-size="12" font-weight="800" text-anchor="middle">+R$ 450 Economizados</text>'''
    elif icon_type == "card":
        inner = '''<rect x="180" y="150" width="140" height="90" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="2.5"/>
                   <rect x="180" y="170" width="140" height="18" fill="#06b6d4" opacity="0.8"/>
                   <rect x="200" y="205" width="25" height="18" rx="3" fill="#f59e0b"/>
                   <circle cx="290" cy="215" r="10" fill="#ef4444" opacity="0.8"/>
                   <circle cx="280" cy="215" r="10" fill="#f59e0b" opacity="0.8"/>
                   <text x="250" y="270" fill="#10b981" font-size="11" font-weight="800" text-anchor="middle">Milhas &amp; Cashback • Sem Juros</text>'''
    elif icon_type == "snowball":
        inner = '''<circle cx="190" cy="235" r="16" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
                   <circle cx="240" cy="215" r="26" fill="#0f172a" stroke="#f59e0b" stroke-width="2.5"/>
                   <circle cx="310" cy="180" r="40" fill="#0f172a" stroke="#10b981" stroke-width="3"/>
                   <path d="M170,255 L350,140" stroke="#334155" stroke-width="2" stroke-dasharray="4 4"/>
                   <text x="310" y="185" fill="#34d399" font-size="14" font-weight="900" text-anchor="middle">ZERO</text>
                   <text x="310" y="200" fill="#94a3b8" font-size="8" font-weight="700" text-anchor="middle">DÍVIDAS</text>'''
    elif icon_type == "emergency":
        inner = '''<path d="M250,130 L320,165 V235 C320,285 250,315 250,315 C250,315 180,285 180,235 V165 Z" fill="#0f172a" stroke="#10b981" stroke-width="3"/>
                   <rect x="225" y="200" width="50" height="40" rx="6" fill="#10b981"/>
                   <path d="M235,200 V185 C235,178 241,172 250,172 C259,172 265,178 265,185 V200" fill="none" stroke="#34d399" stroke-width="3"/>
                   <circle cx="250" cy="220" r="4" fill="#0f172a"/>
                   <text x="250" y="260" fill="#34d399" font-size="9.5" font-weight="800" text-anchor="middle">6 MESES SALVOS</text>'''
    elif icon_type == "fixed_income":
        inner = '''<rect x="180" y="140" width="140" height="110" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2.5"/>
                   <path d="M200,210 L230,190 L265,198 L300,165" fill="none" stroke="#10b981" stroke-width="3.5" stroke-linecap="round"/>
                   <circle cx="300" cy="165" r="5" fill="#f59e0b"/>
                   <text x="250" y="235" fill="#f8fafc" font-size="11" font-weight="800" text-anchor="middle">100% CDI / IPCA+</text>
                   <line x1="180" y1="165" x2="320" y2="165" stroke="#334155" stroke-width="1"/>'''
    elif icon_type == "treasury":
        inner = '''<polygon points="250,130 330,180 330,260 170,260 170,180" fill="#0f172a" stroke="#06b6d4" stroke-width="2.5"/>
                   <line x1="200" y1="200" x2="200" y2="250" stroke="#06b6d4" stroke-width="3"/>
                   <line x1="233" y1="200" x2="233" y2="250" stroke="#06b6d4" stroke-width="3"/>
                   <line x1="266" y1="200" x2="266" y2="250" stroke="#06b6d4" stroke-width="3"/>
                   <line x1="300" y1="200" x2="300" y2="250" stroke="#06b6d4" stroke-width="3"/>
                   <text x="250" y="170" fill="#f59e0b" font-size="11" font-weight="900" text-anchor="middle">TESOURO NACIONAL</text>'''
    elif icon_type == "fgc":
        inner = '''<path d="M190,190 Q250,130 310,190" fill="none" stroke="#10b981" stroke-width="6" stroke-linecap="round"/>
                   <line x1="250" y1="160" x2="250" y2="250" stroke="#10b981" stroke-width="4"/>
                   <circle cx="250" cy="265" r="6" fill="#f59e0b"/>
                   <rect x="200" y="210" width="100" height="26" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
                   <text x="250" y="227" fill="#f59e0b" font-size="10" font-weight="900" text-anchor="middle">FGC: R$ 250.000</text>'''
    elif icon_type == "ladder":
        inner = '''<rect x="160" y="220" width="35" height="40" rx="4" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
                   <text x="177" y="245" fill="#06b6d4" font-size="10" font-weight="800" text-anchor="middle">1 Ano</text>
                   <rect x="205" y="200" width="35" height="60" rx="4" fill="#0f172a" stroke="#3b82f6" stroke-width="2"/>
                   <text x="222" y="235" fill="#3b82f6" font-size="10" font-weight="800" text-anchor="middle">2 Anos</text>
                   <rect x="250" y="180" width="35" height="80" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
                   <text x="267" y="225" fill="#f59e0b" font-size="10" font-weight="800" text-anchor="middle">3 Anos</text>
                   <rect x="295" y="150" width="35" height="110" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
                   <text x="312" y="210" fill="#10b981" font-size="10" font-weight="800" text-anchor="middle">5 Anos</text>'''
    elif icon_type == "stocks":
        inner = '''<path d="M160,260 L200,230 L240,250 L280,180 L310,210 L350,140" fill="none" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>
                   <circle cx="350" cy="140" r="7" fill="#10b981"/>
                   <g transform="translate(180, 160)">
                     <rect x="0" y="0" width="18" height="35" fill="#10b981" opacity="0.4"/>
                     <line x1="9" y1="-8" x2="9" y2="43" stroke="#10b981" stroke-width="1.5"/>
                   </g>
                   <g transform="translate(230, 180)">
                     <rect x="0" y="0" width="18" height="40" fill="#ef4444" opacity="0.4"/>
                     <line x1="9" y1="-6" x2="9" y2="46" stroke="#ef4444" stroke-width="1.5"/>
                   </g>
                   <g transform="translate(290, 150)">
                     <rect x="0" y="0" width="18" height="50" fill="#10b981" opacity="0.4"/>
                     <line x1="9" y1="-10" x2="9" y2="58" stroke="#10b981" stroke-width="1.5"/>
                   </g>
                   <text x="250" y="285" fill="#94a3b8" font-size="11" font-weight="700" text-anchor="middle">Sócio de Grandes Negócios</text>'''
    elif icon_type == "fiis":
        inner = '''<rect x="180" y="140" width="55" height="120" rx="4" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
                   <line x1="195" y1="160" x2="220" y2="160" stroke="#06b6d4" stroke-width="2"/>
                   <line x1="195" y1="180" x2="220" y2="180" stroke="#06b6d4" stroke-width="2"/>
                   <line x1="195" y1="200" x2="220" y2="200" stroke="#06b6d4" stroke-width="2"/>
                   <rect x="250" y="170" width="75" height="90" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
                   <polygon points="250,170 287,145 325,170" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
                   <text x="250" y="285" fill="#f59e0b" font-size="11" font-weight="900" text-anchor="middle">Aluguel Isento Todo Mês</text>'''
    elif icon_type == "dividends":
        inner = '''<path d="M250,260 V180 M250,210 Q210,190 190,160 M250,190 Q290,170 310,140" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
                   <circle cx="190" cy="155" r="14" fill="#0f172a" stroke="#10b981" stroke-width="2.5"/>
                   <text x="190" y="160" fill="#34d399" font-size="10" font-weight="900" text-anchor="middle">R$</text>
                   <circle cx="310" cy="135" r="16" fill="#0f172a" stroke="#10b981" stroke-width="2.5"/>
                   <text x="310" y="140" fill="#34d399" font-size="11" font-weight="900" text-anchor="middle">R$</text>
                   <circle cx="250" cy="165" r="18" fill="#0f172a" stroke="#f59e0b" stroke-width="2.5"/>
                   <text x="250" y="171" fill="#f59e0b" font-size="13" font-weight="900" text-anchor="middle">R$</text>
                   <text x="250" y="285" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">Efeito Bola de Neve Reinvestido</text>'''
    elif icon_type == "besst":
        inner = '''<polygon points="250,135 320,185 295,260 205,260 180,185" fill="#0f172a" stroke="#06b6d4" stroke-width="2.5"/>
                   <circle cx="250" cy="135" r="15" fill="#0f172a" stroke="#10b981" stroke-width="2"/><text x="250" y="139" fill="#10b981" font-size="9" font-weight="900" text-anchor="middle">B</text>
                   <circle cx="320" cy="185" r="15" fill="#0f172a" stroke="#10b981" stroke-width="2"/><text x="320" y="189" fill="#10b981" font-size="9" font-weight="900" text-anchor="middle">E</text>
                   <circle cx="295" cy="260" r="15" fill="#0f172a" stroke="#10b981" stroke-width="2"/><text x="295" y="264" fill="#10b981" font-size="9" font-weight="900" text-anchor="middle">S</text>
                   <circle cx="205" cy="260" r="15" fill="#0f172a" stroke="#10b981" stroke-width="2"/><text x="205" y="264" fill="#10b981" font-size="9" font-weight="900" text-anchor="middle">S</text>
                   <circle cx="180" cy="185" r="15" fill="#0f172a" stroke="#10b981" stroke-width="2"/><text x="180" y="189" fill="#10b981" font-size="9" font-weight="900" text-anchor="middle">T</text>
                   <text x="250" y="205" fill="#f8fafc" font-size="12" font-weight="900" text-anchor="middle">BESST</text>'''
    elif icon_type == "psychology":
        inner = '''<circle cx="200" cy="200" r="42" fill="#0f172a" stroke="#ef4444" stroke-width="2.5"/>
                   <text x="200" y="195" fill="#f87171" font-size="11" font-weight="800" text-anchor="middle">PÂNICO</text>
                   <text x="200" y="210" fill="#94a3b8" font-size="9" font-weight="600" text-anchor="middle">Vende na Baixa</text>
                   <circle cx="300" cy="200" r="42" fill="#0f172a" stroke="#10b981" stroke-width="2.5"/>
                   <text x="300" y="195" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">CALMA</text>
                   <text x="300" y="210" fill="#94a3b8" font-size="9" font-weight="600" text-anchor="middle">Compra Desconto</text>
                   <path d="M230,170 Q250,150 270,170" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>'''
    elif icon_type == "bitcoin":
        inner = '''<circle cx="250" cy="200" r="60" fill="#0f172a" stroke="#f59e0b" stroke-width="4"/>
                   <text x="250" y="218" fill="#f59e0b" font-size="52" font-weight="900" text-anchor="middle" font-family="serif">₿</text>
                   <circle cx="250" cy="200" r="75" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="6 6" opacity="0.6"/>
                   <text x="250" y="295" fill="#34d399" font-size="11" font-weight="900" text-anchor="middle">21 MILHÕES • ESCASSEZ ABSOLUTA</text>'''
    elif icon_type == "crypto_pyramid":
        inner = '''<polygon points="250,140 310,240 190,240" fill="#0f172a" stroke="#ef4444" stroke-width="3"/>
                   <line x1="210" y1="210" x2="290" y2="210" stroke="#ef4444" stroke-width="2"/>
                   <line x1="230" y1="175" x2="270" y2="175" stroke="#ef4444" stroke-width="2"/>
                   <text x="250" y="200" fill="#f87171" font-size="11" font-weight="900" text-anchor="middle">GOLPE</text>
                   <text x="250" y="228" fill="#f87171" font-size="9" font-weight="700" text-anchor="middle">"3% ao dia"</text>
                   <text x="250" y="275" fill="#ef4444" font-size="11" font-weight="800" text-anchor="middle">Cuidado com Promessas Fáceis</text>'''
    elif icon_type == "coldwallet":
        inner = '''<rect x="220" y="140" width="60" height="110" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="2.5"/>
                   <rect x="230" y="155" width="40" height="25" rx="3" fill="#06b6d4" opacity="0.3"/>
                   <circle cx="250" cy="210" r="8" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
                   <text x="250" y="275" fill="#10b981" font-size="11" font-weight="800" text-anchor="middle">Not Your Keys, Not Your Coins</text>'''
    elif icon_type == "dca":
        inner = '''<rect x="170" y="230" width="30" height="30" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
                   <rect x="210" y="205" width="30" height="55" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
                   <rect x="250" y="180" width="30" height="80" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
                   <rect x="290" y="155" width="30" height="105" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
                   <text x="250" y="285" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">Aportes Semanais • Sem Estresse</text>'''
    elif icon_type == "allocation":
        inner = '''<line x1="180" y1="200" x2="320" y2="200" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
                   <circle cx="180" cy="200" r="30" fill="#0f172a" stroke="#10b981" stroke-width="3"/>
                   <text x="180" y="204" fill="#34d399" font-size="12" font-weight="900" text-anchor="middle">95%</text>
                   <text x="180" y="245" fill="#94a3b8" font-size="9" font-weight="700" text-anchor="middle">Conservador</text>
                   <circle cx="320" cy="200" r="16" fill="#0f172a" stroke="#f59e0b" stroke-width="2.5"/>
                   <text x="320" y="204" fill="#f59e0b" font-size="10" font-weight="900" text-anchor="middle">5%</text>
                   <text x="320" y="235" fill="#94a3b8" font-size="9" font-weight="700" text-anchor="middle">Cripto</text>'''
    elif icon_type == "allweather":
        inner = '''<circle cx="250" cy="200" r="70" fill="none" stroke="#06b6d4" stroke-width="2.5"/>
                   <line x1="250" y1="130" x2="250" y2="270" stroke="#334155" stroke-width="2"/>
                   <line x1="180" y1="200" x2="320" y2="200" stroke="#334155" stroke-width="2"/>
                   <text x="215" y="165" fill="#10b981" font-size="9.5" font-weight="800" text-anchor="middle">Crescimento</text>
                   <text x="285" y="165" fill="#f59e0b" font-size="9.5" font-weight="800" text-anchor="middle">Inflação</text>
                   <text x="215" y="240" fill="#3b82f6" font-size="9.5" font-weight="800" text-anchor="middle">Deflação</text>
                   <text x="285" y="240" fill="#ef4444" font-size="9.5" font-weight="800" text-anchor="middle">Recessão</text>
                   <circle cx="250" cy="200" r="16" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
                   <text x="250" y="204" fill="#f59e0b" font-size="8.5" font-weight="900" text-anchor="middle">DALIO</text>'''
    elif icon_type == "globe":
        inner = '''<circle cx="250" cy="200" r="65" fill="#0f172a" stroke="#3b82f6" stroke-width="3"/>
                   <ellipse cx="250" cy="200" rx="30" ry="65" fill="none" stroke="#3b82f6" stroke-width="1.5"/>
                   <line x1="185" y1="200" x2="315" y2="200" stroke="#3b82f6" stroke-width="1.5"/>
                   <circle cx="290" cy="170" r="16" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
                   <text x="290" y="174" fill="#34d399" font-size="11" font-weight="900" text-anchor="middle">US$</text>
                   <text x="250" y="285" fill="#94a3b8" font-size="10.5" font-weight="700" text-anchor="middle">S&amp;P 500 • ETFs Globais</text>'''
    elif icon_type == "freedom":
        inner = '''<path d="M190,240 A65,65 0 0,1 310,240" fill="none" stroke="#10b981" stroke-width="10" stroke-linecap="round"/>
                   <line x1="250" y1="240" x2="280" y2="190" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
                   <circle cx="250" cy="240" r="8" fill="#f59e0b"/>
                   <text x="250" y="165" fill="#34d399" font-size="20" font-weight="900" text-anchor="middle">4% REGRA</text>
                   <text x="250" y="265" fill="#94a3b8" font-size="10" font-weight="700" text-anchor="middle">Viver de Renda Perpétua</text>'''
    elif icon_type == "rebalance":
        inner = '''<circle cx="250" cy="200" r="60" fill="none" stroke="#06b6d4" stroke-width="2" stroke-dasharray="6 4"/>
                   <path d="M220,160 L280,160 L270,150 M280,160 L270,170" stroke="#10b981" stroke-width="2.5" stroke-linecap="round"/>
                   <path d="M280,240 L220,240 L230,230 M220,240 L230,250" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>
                   <text x="250" y="195" fill="#f8fafc" font-size="12" font-weight="800" text-anchor="middle">15 MINUTOS</text>
                   <text x="250" y="210" fill="#94a3b8" font-size="9" font-weight="600" text-anchor="middle">A Cada 6 Meses</text>'''
    elif icon_type == "commandments":
        inner = '''<rect x="210" y="140" width="80" height="110" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2.5"/>
                   <text x="250" y="170" fill="#f59e0b" font-size="11" font-weight="900" text-anchor="middle">I. Aporte</text>
                   <text x="250" y="190" fill="#34d399" font-size="11" font-weight="900" text-anchor="middle">II. Paciência</text>
                   <text x="250" y="210" fill="#06b6d4" font-size="11" font-weight="900" text-anchor="middle">III. Diversifique</text>
                   <text x="250" y="230" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">IV. Tempo</text>
                   <text x="250" y="275" fill="#f59e0b" font-size="11" font-weight="800" text-anchor="middle">Os 5 Mandamentos</text>'''
    else:
        inner = '''<circle cx="250" cy="200" r="60" fill="#0f172a" stroke="#10b981" stroke-width="3"/>
                   <path d="M220,200 L240,220 L280,180" fill="none" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>'''

    return f'''<svg viewBox="0 0 500 400" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="glow-{icon_type}" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#10b981" stop-opacity="0.2" />
          <stop offset="100%" stop-color="#10b981" stop-opacity="0" />
        </radialGradient>
      </defs>
      <circle cx="250" cy="200" r="150" fill="url(#glow-{icon_type})" />
      {inner}
      <!-- Faixa de Destaque -->
      <g transform="translate(250, 335)">
        <rect x="-110" y="-12" width="220" height="24" rx="12" fill="rgba(15,23,42,0.85)" stroke="#10b981" stroke-width="1.2" />
        <text x="0" y="4" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle" letter-spacing="1">{badge_text}</text>
      </g>
    </svg>'''
