from functools import partial

logs = ["INFO: Connexion", "ERROR: Crash", "INFO: Login", "STOP"]

def nettoyer_logs(prefixe, message):
    return f"{prefixe} | {message.upper()}"

log_systeme = partial(nettoyer_logs, "[SYSTEME]")
iter_logs = iter(logs)
flux = iter(lambda : next(iter_logs).upper(), "STOP")

print("--- TEST PARTIAL ---")
print(log_systeme("Erreur critique"))

print("--- TEST FLUX AVEC SENTINELLE ---")
for msg in flux:
    print(log_systeme(msg))