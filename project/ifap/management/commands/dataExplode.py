from django.core.management.base import BaseCommand
# utiliser la commande   ./manage.py dataExplode   pour lancer ce script
class Command(BaseCommand):
    def handle(self, **options):
        from ifap.models import Classe, Ordre, Famille, Animal
        import pandas as pd
        data = pd.read_csv("/home/freshloic/Documents/UA/TDGenieLogiciel/project/ifap/management/commands/taxo.csv").to_dict(orient="row")
        # print(data)

        Classe.objects.all().delete()

        for item in data:
            # print(item['FAMILLE'])
            classe = Classe.objects.get_or_create(nom=item['CLASSE'])[0]
            ordre = Ordre.objects.get_or_create(nom=item['ORDRE'], classe=classe)[0]
            famille = Famille.objects.get_or_create(nom=item['FAMILLE'], ordre=ordre)[0]
            Animal.objects.get_or_create(nomVernaculaire=item['NOM COMMUN (vernaculaire) de l\'espèce'], nomScientifique=item['NOM SCIENTIFIQUE de l\'espèce'], famille=famille)
