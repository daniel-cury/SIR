import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# ── 1. Dados do projeto ─────────────────────────────────────────────────────────
tarefas = [
    ("Recherches, entretiens, organisation du groupe",
     dt.date(2025, 5, 20), dt.date(2025, 5, 30)),
    ("Étude de faisabilité",
     dt.date(2025, 5, 31), dt.date(2025, 6, 6)),
    ("Étude d'une UX propre",
     dt.date(2025, 6, 7), dt.date(2025, 6, 12)),
    ("MVP et rapport",
     dt.date(2025, 6, 13), dt.date(2025, 6, 28)),
]

# ── 2. Pré‑processamento ────────────────────────────────────────────────────────
# Converte datas para valores numéricos (matplotlib trabalha melhor assim)
start_nums = [mdates.date2num(t[1]) for t in tarefas]
duracoes   = [(t[2] - t[1]).days for t in tarefas]
labels     = [t[0] for t in tarefas]

# Para exibir da primeira para a última (topo → base)
y_pos = list(reversed(range(len(tarefas))))  # [3, 2, 1, 0]

# ── 3. Plot ─────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 4))

# Desenha cada barra
for y, start, dur in zip(y_pos, start_nums, duracoes):
    ax.barh(
        y=y,
        width=dur,
        left=start,
        height=0.6,
        align="center",
        edgecolor="black",
        alpha=0.8,
    )

# ── 4. Ajustes de eixos ─────────────────────────────────────────────────────────
ax.set_yticks(y_pos)
ax.set_yticklabels(reversed(labels), fontsize=9)

# Formata eixo X como datas legíveis
ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))

# Títulos e grades
ax.set_title("Planning du projet (Gantt)", fontsize=12, pad=12)
ax.grid(axis="x", linestyle="--", alpha=0.5)
fig.autofmt_xdate()

plt.tight_layout()
plt.show()
