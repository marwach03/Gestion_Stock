#include <iostream>
#include <mysql.h>
#include <string>
#include <sstream>
#include <conio.h>
#include "Gestion_produit.h"
#include "Gestion_commande.h"
#include "Gestion_stock.h"
#include "Gestion_livraison.h"
#include "Statistiques.h"

Gestion_produit p;
Gestion_commande c;
Gestion_stock s;
Gestion_livraison l;
Statistiques st;

using namespace std;


int main()
{
	MYSQL *conn;
    const char *username = "root";
    const char *password = "";
    const char *host = "localhost";
    int port = 3306;
    const char *database = "stock";

    // Créer la structure de la connexion
    conn = mysql_init(NULL);
    cout << "STOCK!" << endl;

    // Établir la connexion à la base de données
    if (!mysql_real_connect(conn, host, username, password, database, port, NULL, 0)) {
        cout << "Erreur de connexion à MySQL: " << mysql_error(conn) << endl;
        return 1;
    }
	int choix;
	
	
	do{
		system("cls");
		cout<<"--------GESTIONS--------"<<endl;
		cout<<" 1. GETION DE PRODUITS \n 2. GESTION DE COMMANDES \n 3. GESTION DE LIVRAISONS \n 4. GESTION STOCK\n 5. STATISTIQUES \n 6. QUITTER \n"<<endl;
		cout<<"VEUILEEZ SAISIR VOTRE CHOIX : ";
		cin>>choix;
		switch(choix)
		{
			int choixP;
			case 1:
				do{
					system("cls");
					cout<<"--------TABLES--------"<<endl;
					cout<<"1. ARTICLE \n 2. CATEGORIE \n 3. EMPLACEMENT\n 4. QUITTER \n"<<endl;
					cout<<"VEUILEEZ SAISIR LA TABLE : ";
					cin>>choixP;
					int choixT;
					switch(choixP)
					{
						case 1:
							
							do{
								system("cls");
								cout<<"1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										p.InsereArticle(conn);
									break;
									case 2:
										p.ModifierArticle(conn);
									break;
									case 3:
										p.SupprimerArticle(conn);
									break;
									
									case 4:
										p.ListerArticle(conn);
									break;
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);
						break;
						
						case 2:
							
							do{
								system("cls");
								cout<<"1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										p.InsereCategorie(conn);
									break;
									case 2:
										p.ModifierCategorie(conn);
									break;
									case 3:
										p.SupprimerCategorie(conn);
									break;
									
									case 4:
										p.ListerCategorie(conn);
									break;
									
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);
						break;
						
						case 3:
							
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										p.InsereEmplacement(conn);
									break;
									case 2:
										p.ModifierEmplacement(conn);
									break;
									case 3:
										p.SupprimerEmplacement(conn);
									break;
									
									case 4:
										p.ListerEmplacement(conn);
									break;
									
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);			
						break;
						
						case 4:
							cout<<"FIN DE PROGRAMME TABLES"<<endl;			
						break;
					}
					getchar();
					getch();
				}while(choixP!=4);
			break;
			
			case 2:
				do{
					system("cls");
					cout<<"--------TABLES--------"<<endl;
					cout<<"1. COMMANDE \n 2. DETAIL COMMANDE \n 3. FOURNISSEUR\n 4. QUITTER \n"<<endl;
					cout<<"VEUILEEZ SAISIR LA TABLE : ";
					cin>>choixP;
					int choixT;
					switch(choixP)
					{
						case 1:
							
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										c.InsereCommande(conn);
									break;
									case 2:
										c.ModifierCommande(conn);
									break;
									case 3:
										c.SupprimerCommande(conn);
									break;
									
									case 4:
										c.ListerCommande(conn);
									break;
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);
						break;
						
						case 2:
						
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										c.InsereDetailCom(conn);
									break;
									case 2:
										c.ModifierDetailCom(conn);
									break;
									case 3:
										c.SupprimerDetailCom(conn);
									break;
									
									case 4:
										c.ListerDetailCom(conn);
									break;
									
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);
						break;
						
						case 3:
							
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										c.InsereFournisseur(conn);
									break;
									case 2:
										c.ModifierFournisseur(conn);
									break;
									case 3:
										c.SupprimerFournisseur(conn);
									break;
									
									case 4:
										c.ListerFournisseur(conn);
									break;
									
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);			
						break;
						
						case 4:
							cout<<"FIN DE PROGRAMME TABLES"<<endl;			
						break;
					}
					getchar();
					getch();
				}while(choixP!=4);
			break;
			
			case 3:
				do{
					system("cls");
					cout<<"--------TABLES--------"<<endl;
					cout<<"1. LIVRAISON \n 2. DETAL LIVRAISON \n 3. TRANSACTION \n 4. EXPEDITION \n 5. TRANSPORTEUR \n 6. CLIENT \n 7.QUITTER \n"<<endl;
					cout<<"VEUILEEZ SAISIR LA TABLE : ";
					cin>>choixP;
					int choixT;
					switch(choixP)
					{
						case 1:
							
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										l.InsereLivraison(conn);
									break;
									case 2:
										l.ModifierLivraison(conn);
									break;
									case 3:
										l.SupprimerLivraison(conn);
									break;
									
									case 4:
										l.ListerLivraison(conn);
									break;
					
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);
						break;
						
						case 2:
							
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										l.InsereDetailliv(conn);
									break;
									case 2:
										l.ModifierDetLiv(conn);
									break;
									case 3:
										l.SupprimerDetLiv(conn);
									break;
									case 4:
										l.ListerDetailliv(conn);
									break;
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);
						break;
						
						case 3:
							
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										l.InsereTransaction(conn);
									break;
									case 2:
										l.ModifierTransaction(conn);
									break;
									case 3:
										l.SupprimerTransaction(conn);
									break;
									case 4:
										l.ListerTransaction(conn);
									break;
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);			
						break;
						
						case 4:
							
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										l.InsereExpedition(conn);
									break;
									case 2:
										l.ModifierExpedition(conn);
									break;
									case 3:
										l.SupprimerExpedition(conn);
									break;
									case 4:
										l.ListerExpedition(conn);
									break;
									 	
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);
						break;
						
						case 5:
							
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										l.InsereTransporteur(conn);
									break;
									case 2:
										l.ModifierTransporteur(conn);
									break;
									case 3:
										l.SupprimerTransporteur(conn);
									break;
									case 4:
										l.ListerTransporteur(conn);
									break;
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);
						break;
						
						case 6:
							
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										l.InsereClient(conn);
									break;
									case 2:
										l.ModifierClient(conn);
									break;
									case 3:
										l.SupprimerClient(conn);
									break;
									
									case 4:
										l.ListerClient(conn);
									break;
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);
						break;
						
						case 7:
							cout<<"FIN DE PROGRAMME TABLES"<<endl;			
						break;
					}
					getchar();
					getch();
				}while(choixP!=7);
			break;
			
			case 4:
				do{
					system("cls");
					cout<<"--------TABLES--------"<<endl;
					cout<<"1. UTILISATEUR \n 2. ROLE \n 3. HISTORIQUE\n 4. ALERTE \n 5. PARAMETRE \n 6. QUITTER \n"<<endl;
					cout<<"VEUILEEZ SAISIR LA TABLE : ";
					cin>>choixP;
					int choixT;
					switch(choixP)
					{
						case 1:
							
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										s.InsererUtilisateur(conn);
									break;
									case 2:
										s.ModifierUtilisateur(conn);
									break;
									case 3:
										s.SupprimerUtilisateur(conn);
									break;
									
									case 4:
										s.ListerUtilisateur(conn);
									break;
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);
						break;
						
						case 2:
							
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										s.InsererRole(conn);
									break;
									case 2:
										s.ModifierRole(conn);
									break;
									case 3:
										s.SupprimerRole(conn);
									break;
									case 4:
										s.ListerRole(conn);
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);
						break;
						
						case 3:
							
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										s.InsererHistorique(conn);
									break;
									case 2:
										s.ModifierHistorique(conn);
									break;
									case 3:
										s.SupprimerHistorique(conn);
									break;
									case 4:
										s.ListerHistorique(conn);
									break;
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);			
						break;
						
						case 4:
						
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										s.InsererAlerte(conn);
									break;
									case 2:
										s.ModifierAlerte(conn);
									break;
									case 3:
										s.SupprimerAlerte(conn);
									break;
									case 4:
										s.ListerAlerte(conn);
									break;
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
								getchar();
								getch();
							}while(choixT!=5);			
						break;
						
						case 5:
							
							do{
								system("cls");
								cout<<" 1. INSERER \n 2. MODIFIER \n 3. SUPPRIMER \n 4. LISTER \n 5. QUITTER\n"<<endl;
								cout<<"VEUILEEZ SAISIR L'OPERATION : ";
								cin>>choixT;
								switch(choixT)
								{
									case 1:
										s.InsererParametre(conn);
									break;
									case 2:
										s.ModifierParametre(conn);
									break;
									case 3:
										s.SupprimerParametre(conn);
									break;
									case 4:
										s.ListerParametre(conn);
									break;
									case 5:
										cout<<"FIN DE L'OPERARTIONS"<<endl;
									break;
								}
							}while(choixT!=5);			
						break;
						
						case 6:
							cout<<"FIN DE PROGRAMME TABLES"<<endl;			
						break;
					}
					getchar();
					getch();
				}while(choixP!=6);
			break;
			
			case 5:
				do{
					system("cls");
					cout<<"--------Statistiques--------"<<endl;
					cout<<"1. TAUX DE VENTES \n 2. Temps Rotation \n 3. TEMPS REPTURE \n 4.Cout Moyenne \n 5. NIVEAU MOYENNE DU STOCK \n 6.Taux de rotation des stocks\n 7. cout_moyen_stocks \n 8. Taux de satisfaction des commandes \n 9. Nombre de commandes en retard \n 10. Coût de la rupture de stock \n 11. QUITTER \n"<<endl;
					cout<<"VEUILEEZ SAISIR LA TABLE : ";
					cin>>choixP;
					switch(choixP)
					{
						case 1:
							st.GetSalesStats(conn);
						break;
						
						case 2:
							st.Temps_moyen_de_rotation_des_stocks(conn);
						break;
						
						case 3:
							st.GetRuptureStockTaux(conn);
						break;
						
						case 4:
							st.GetCoutMoyenArticleVendu(conn);
						break;
						
						case 5:
							st.GetAverageStockLevel(conn);
						break;
						
						case 6:
							st.GetStockRotationRate(conn);
						break;
						
						case 7:
							st.GetAverageStockCost(conn);
						break;
						
						case 8:
							st.GetOrderSatisfactionRate(conn);
						break;
						
						case 9:
							st.GetDelayedOrdersCount(conn);
						break;
						
						case 10:
							st.GetCostOfStockOut(conn);	
						break;
						
						case 11:
							cout<<"FIN DE PROGRAMME TABLES"<<endl;
						break;
						
					}
					getchar();
					getch();
				}while(choixP!=11);
			break;
			
			case 6:
				cout<<"FIN PROGRAMME!"<<endl;
			break;
			default:
				break;
		}
		getchar();
		getch();
	}while(choix!=6);
	mysql_close(conn);

    return 0;
}
