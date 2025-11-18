def classifica_rischio(score: int):
    """
    Restituisce:
    - etichetta della classe di rischio
    - colore/emoji
    - stime di sopravvivenza a 1, 3 e 5 anni (da KM)
    """

    if score <= 0:
        risk_class = "Basso rischio"
        color = "🟢"
        # per ora: nessun decesso osservato nel gruppo a basso rischio
        surv_1y, surv_3y, surv_5y = 1.00, 1.00, 1.00

    elif 1 <= score <= 3:
        risk_class = "Rischio intermedio"
        color = "🟡"
        # valori indicativi, da aggiornare quando avrà le KM precise
        surv_1y, surv_3y, surv_5y = 1.00, 0.85, 0.75

    else:
        risk_class = "Alto rischio"
        color = "🔴"
        # valori allineati alle Kaplan–Meier del gruppo alto rischio
        surv_1y, surv_3y, surv_5y = 0.65, 0.45, 0.38

    return risk_class, color, surv_1y, surv_3y, surv_5y
