import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Chemins relatifs au dépôt (données dans le sous-module data/Experiment_Data)
ROOT = os.path.dirname(os.path.abspath(__file__))
REELS = os.path.join(ROOT, "data", "Experiment_Data", "SIR_Experiment", "Reels")
OUT = os.path.join(ROOT, "resultados")
os.makedirs(OUT, exist_ok=True)

# Prend le CSV en local
df = pd.read_csv(os.path.join(REELS, "2_5_6pro_LTE_YTshorts_stat_64sps.csv"))
# print("colunas no arquico csv")
# print(df.columns.tolist())
# with open(os.path.join(REELS, "1_5_6pro_3G_insta_stat_64sps.csv"), encoding="utf-8") as f:
#     for i in range(15):
#         print(f.readline().strip())


# #0. Organisation des colonnes
# # fait une division de la colonne avec les valeurs qui nous interessent
# colunas_embutidas = ['V_BAT', 'I_BAT', 'P_BAT', 'V_BB', 'I_BB', 'P_BB', 'V_PA', 'I_PA', 'P_PA']
# df[colunas_embutidas] = df["V_BAT,I_BAT,P_BAT,V_BB,I_BB,P_BB,V_PA,I_PA,P_PA"].str.split(",", expand=True).astype(float)


# # 1. Recalcule la puissance pour vérifier la consistance des données
# df["P_BAT_calc"] = df["V_BAT"] * df["I_BAT"]
# df["P_PA_calc"] = df["V_PA"] * df["I_PA"]

# # 2. Calcul de l'erreur percentuel relactif entre puissance moyenne et calculée
# df["P_BAT_error_pct"] = (df["P_BAT_calc"] - df["P_BAT"]) / df["P_BAT"] * 100
# df["P_PA_error_pct"] = (df["P_PA_calc"] - df["P_PA"]) / df["P_PA"] * 100

# # 3. Stats des variables
# desc_stats = df[["V_BAT", "I_BAT", "P_BAT", "V_PA", "I_PA", "P_PA"]].describe()
# print("Estatísticas descritivas:\n", desc_stats)

# # 4. Erreur moyenne entre puissance réele et calculée
# bat_error_mean = df["P_BAT_error_pct"].mean()
# pa_error_mean = df["P_PA_error_pct"].mean()
# print(f"\nErro médio P_BAT: {bat_error_mean:.3f}%")
# print(f"Erro médio P_PA: {pa_error_mean:.3f}%")

# # 5. [Energie totale
# # On pose 64 samples par seconde
# sampling_rate = 64
# delta_t = 1 / sampling_rate  # segundos por amostra

# # Energia total em Joules = somatório de P (W) * tempo (s)
# total_energy_joules = (df["P_BAT"] * delta_t).sum()
# print(f"\nEnergia total consumida: {total_energy_joules:.2f} Joules")

# # Converter para Wh
# total_energy_wh = total_energy_joules / 3600
# print(f"Energia total consumida: {total_energy_wh:.4f} Wh")

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configurações gerais
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

arquivos = {
    #Insta
    os.path.join(REELS, "1_5_6pro_3G_insta_stat_64sps.csv"): "insta_3G_stat_1",
    os.path.join(REELS, "2_5_6pro_3G_insta_stat_64sps.csv"): "insta_3G_stat_2",
    os.path.join(REELS, "1_5_6pro_LTE_insta_stat_64sps.csv"): "insta_LTE_stat_1",
    os.path.join(REELS, "2_5_6pro_LTE_insta_stat_64sps.csv"): "insta_LTE_stat_2",
    # os.path.join(REELS, "1_5_6pro_LTE_insta_Dyna_T1_Prefecture_INSA_64sps.csv"): "insta_LTE_dyna_1",
    # os.path.join(REELS, "2_5_6pro_LTE_insta_Dyna_T1_Prefecture_INSA_64sps.csv"): "insta_LTE_dyna_2",
    # os.path.join(REELS, "3_5_6pro_LTE_insta_Dyna_T1_Prefecture_INSA_64sps.csv"): "insta_LTE_dyna_3",

    #Tiktok
    os.path.join(REELS, "1_5_6pro_3G_tiktok_stat_64sps.csv"): "tiktok_3G_stat_1",
    os.path.join(REELS, "2_5_6pro_3G_tiktok_stat_64sps.csv"): "tiktok_3G_stat_2",
    os.path.join(REELS, "3_5_6pro_3G_tiktok_stat_64sps.csv"): "tiktok_3G_stat_3",
    os.path.join(REELS, "2_5_6pro_LTE_tiktok_stat_64sps.csv"): "tiktok_LTE_stat_2",
    # os.path.join(REELS, "1_5_6pro_LTE_tiktok_Dyna_T1_Belcombe_Auditorium_64sps.csv"): "tiktok_LTE_dyna_1",
    # os.path.join(REELS, "1_5_6pro_LTE_tiktok_Dyna_T1_Doua_Auditorium_64sps.csv"): "tiktok_LTE_dyna_2",
    # os.path.join(REELS, "2_5_6pro_LTE_tiktok_Dyna_T1_INSA_Prefecture_64sps.csv"): "tiktok_LTE_dyna_3",
    # os.path.join(REELS, "2_5_6pro_LTE_tiktok_Dyna_T1_INSA_Prefecture_64sps.csv"): "tiktok_LTE_dyna_4",

    #YT
    os.path.join(REELS, "1_5_6pro_3G_YTshorts_stat_64sps.csv"): "yt_3G_stat_1",
    os.path.join(REELS, "2_5_6pro_3G_YTshorts_stat_64sps.csv"): "yt_3G_stat_2",
    os.path.join(REELS, "1_5_6pro_LTE_YTshorts_stat_64sps.csv"): "yt_LTE_stat_1"


}

df_all = []
energia_total = {}

for arquivo, rotulo in arquivos.items():
    if not os.path.exists(arquivo):
        print(f"[AVISO] Arquivo não encontrado: {arquivo}")
        continue

    df = pd.read_csv(arquivo)

    # Corrigido: dentro do loop
    coluna_concatenada = "V_BAT,I_BAT,P_BAT,V_BB,I_BB,P_BB,V_PA,I_PA,P_PA"
    if coluna_concatenada in df.columns:
        colunas_embutidas = ['V_BAT', 'I_BAT', 'P_BAT', 'V_BB', 'I_BB', 'P_BB', 'V_PA', 'I_PA', 'P_PA']
        df[colunas_embutidas] = df[coluna_concatenada].str.split(",", expand=True).astype(float)

        df["sessao"] = rotulo
        df_all.append(df)

        if "P_BAT" in df.columns:
            # Énergie par minute (Wh/min) : les sessions n'ont pas toutes la même durée
            energia_total[rotulo] = df["P_BAT"].mean() * 60 / 3600
        print(f"[OK] Dados processados: {rotulo}")
    else:
        print(f"[ERRO] Coluna concatenada não encontrada em {rotulo}")

if not df_all:
    print("Nenhum dado foi carregado. Verifique os arquivos.")
    exit()

df_total = pd.concat(df_all, ignore_index=True)

# # Boxplots
# for coluna in ["P_BAT", "P_PA", "I_BAT", "I_PA"]:
#     if coluna in df_total.columns:
#         print(f"Plotando boxplot: {coluna}")
#         plt.figure()
#         sns.boxplot(data=df_total, x="sessao", y=coluna)
#         plt.title(f"Boxplot de {coluna}")
#         plt.xticks(rotation=45)
#         plt.tight_layout()
#         plt.savefig(os.path.join(OUT, f"boxplot_{coluna}.png"))
#         plt.show()
#         plt.close()

# Barras: energia total
print("Plotando gráfico de energia total...")
plt.figure()
sns.barplot(x=list(energia_total.keys()), y=list(energia_total.values()))
plt.title("Énergie consommée par minute, par session (Wh/min)")
plt.ylabel("Wh/min")
plt.xlabel("Session")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUT, f"energia_total.png"))
plt.show()
plt.close()


# Série temporal opcional
plot_temporal = False
sessao_especifica = "3G_stat_1"

if plot_temporal:
    df_plot = df_total[df_total["sessao"] == sessao_especifica]
    if not df_plot.empty:
        print(f"Plotando série temporal: {sessao_especifica}")
        plt.figure()
        plt.plot(df_plot.index / 64, df_plot["P_BAT"], label="P_BAT (W)")
        plt.plot(df_plot.index / 64, df_plot["P_PA"], label="P_PA (W)")
        plt.title(f"Evolução Temporal - {sessao_especifica}")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Potência (W)")
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(OUT, f"serie_temporal_{sessao_especifica}.png"))
        plt.show()
        plt.close()


energia_total = []

for path, rotulo in arquivos.items():
    if not os.path.exists(path):
        print(f"Aviso: {path} não encontrado.")
        continue

    df = pd.read_csv(path)

    if "V_BAT,I_BAT,P_BAT,V_BB,I_BB,P_BB,V_PA,I_PA,P_PA" in df.columns:
        colunas = ['V_BAT', 'I_BAT', 'P_BAT', 'V_BB', 'I_BB', 'P_BB', 'V_PA', 'I_PA', 'P_PA']
        df[colunas] = df["V_BAT,I_BAT,P_BAT,V_BB,I_BB,P_BB,V_PA,I_PA,P_PA"].str.split(",", expand=True).astype(float)

    # Extrair informações
    app = rotulo.split("_")[0]
    modo = "dyna" if "dyna" in rotulo else "stat"
    rede = "3G" if "_3G_" in rotulo else ("LTE" if "_LTE_" in rotulo else "desconhecido")

    df["sessao"] = rotulo
    df["app"] = app
    df["modo"] = modo
    df["rede"] = rede

    # Énergie par minute (Wh/min), normalisée par la durée de la session
    energia_Wh = df["P_BAT"].mean() * 60 / 3600
    energia_total.append({
        "sessao": rotulo,
        "app": app,
        "modo": modo,
        "rede": rede,
        "energia_Wh": energia_Wh
    })

    df_all.append(df)

df_total = pd.concat(df_all, ignore_index=True)
df_energia = pd.DataFrame(energia_total)

plt.figure(figsize=(12, 6))
sns.barplot(data=df_energia, x="app", y="energia_Wh", hue="rede", errorbar=None)
plt.title("Énergie consommée par minute — 3G vs LTE")
plt.ylabel("Énergie (Wh/min)")
plt.xlabel("Application")
plt.tight_layout()
plt.savefig(os.path.join(OUT, f"comparacao_rede_apps.png"))
plt.show()

g = sns.catplot(
    data=df_energia, x="app", y="energia_Wh", hue="rede",
    col="modo", kind="bar", height=5, aspect=1
)
g.fig.subplots_adjust(top=0.85)
g.fig.suptitle("Énergie par minute — application, mobilité et réseau")
g.set_axis_labels("Application", "Énergie (Wh/min)")
g.set_titles("{col_name}")
plt.savefig(os.path.join(OUT, f"comparacao_rede_modo_app.png"))
plt.show()


sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Caminhos completos do seu dicionário original (inclua todos, sem simplificação!)
arquivos = {
    # Insta - stat
    os.path.join(REELS, "1_5_6pro_LTE_insta_stat_64sps.csv"): "insta_LTE_stat_1",
    os.path.join(REELS, "2_5_6pro_LTE_insta_stat_64sps.csv"): "insta_LTE_stat_2",
    # Insta - dyna
    os.path.join(REELS, "1_5_6pro_LTE_insta_Dyna_T1_Prefecture_INSA_64sps.csv"): "insta_LTE_dyna_1",
    os.path.join(REELS, "2_5_6pro_LTE_insta_Dyna_T1_Prefecture_INSA_64sps.csv"): "insta_LTE_dyna_2",
    os.path.join(REELS, "3_5_6pro_LTE_insta_Dyna_T1_Prefecture_INSA_64sps.csv"): "insta_LTE_dyna_3",
    # Tiktok - stat
    os.path.join(REELS, "2_5_6pro_LTE_tiktok_stat_64sps.csv"): "tiktok_LTE_stat_2",
    # Tiktok - dyna
    os.path.join(REELS, "1_5_6pro_LTE_tiktok_Dyna_T1_Belcombe_Auditorium_64sps.csv"): "tiktok_LTE_dyna_1",
    os.path.join(REELS, "1_5_6pro_LTE_tiktok_Dyna_T1_Doua_Auditorium_64sps.csv"): "tiktok_LTE_dyna_2",
    os.path.join(REELS, "2_5_6pro_LTE_tiktok_Dyna_T1_INSA_Prefecture_64sps.csv"): "tiktok_LTE_dyna_3",
    os.path.join(REELS, "3_5_6pro_LTE_tiktok_Dyna_T1_INSA_Prefecture_64sps.csv"): "tiktok_LTE_dyna_4",
}

energia_total = []

for caminho, rotulo in arquivos.items():
    if not os.path.exists(caminho):
        print(f"[ERRO] Arquivo não encontrado: {caminho}")
        continue

    df = pd.read_csv(caminho)

    # Se dados vierem todos em uma string, extrair colunas
    if "V_BAT,I_BAT,P_BAT,V_BB,I_BB,P_BB,V_PA,I_PA,P_PA" in df.columns:
        colunas = ['V_BAT', 'I_BAT', 'P_BAT', 'V_BB', 'I_BB', 'P_BB', 'V_PA', 'I_PA', 'P_PA']
        df[colunas] = df["V_BAT,I_BAT,P_BAT,V_BB,I_BB,P_BB,V_PA,I_PA,P_PA"].str.split(",", expand=True).astype(float)

    # Extrair metadados do nome
    app, rede, modo = rotulo.split("_")[0:3]

    # Énergie par minute (Wh/min), normalisée par la durée de la session
    energia = df["P_BAT"].mean() * 60 / 3600

    energia_total.append({
        "app": app,
        "rede": rede,
        "modo": modo,
        "sessao": rotulo,
        "energia_Wh": energia
    })

    print(f"[OK] Dados processados: {rotulo}")

df_energia = pd.DataFrame(energia_total)

# Filtrar apenas apps com ambos modos presentes
apps_validos = df_energia.groupby("app")["modo"].nunique()
apps_com_stat_dyna = apps_validos[apps_validos >= 2].index.tolist()
df_filtrado = df_energia[df_energia["app"].isin(apps_com_stat_dyna)]

# Gráfico: comparação entre modo estático e dinâmico
g = sns.catplot(
    data=df_filtrado,
    x="app", y="energia_Wh", hue="modo",
    col="rede", kind="bar", height=5, aspect=1.2, errorbar=None
)
g.fig.subplots_adjust(top=0.8)
g.fig.suptitle("Énergie par minute — statique vs dynamique (LTE)")
g.set_axis_labels("Application", "Énergie (Wh/min)")
g.set_titles("Rede: {col_name}")
plt.savefig(os.path.join(OUT, f"comparacao_stat_dyna_LTE.png"))
plt.show()
