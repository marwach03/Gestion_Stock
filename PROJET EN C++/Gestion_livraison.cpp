#include "Gestion_livraison.h"

using namespace std;

Gestion_livraison::Gestion_livraison()
{
	conn = mysql_init(NULL);
}

Gestion_livraison::~Gestion_livraison()
{
	
}

/*void Gestion_livraison::InsereLivraison(MYSQL* conn)
{
	int numliv,numT;
	string dateliv;
	cout << "Entrez le numero de livraison : ";
    cin >> numliv;
    
    cin.ignore();
    
	cout << "Entrez la date de livraison : ";
    getline(cin,dateliv);
    
    cout << "Entrez le numero du transporteur : ";
    cin>>numT;
    cin.ignore();
    
    stringstream ss;
    ss << numliv;
    string numlivStr = ss.str();
    
    ss.str("");
    ss << numT;
    string numTStr = ss.str();
    
    string checkQuery = "SELECT numT FROM transporteur WHERE numT = " + numTStr;
    if (mysql_query(conn, checkQuery.c_str())) {
        cout << "Erreur lors de la vérification du transport : " << mysql_error(conn) << endl;
        return;
    }
    
    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "Le transport specifie n'existe pas dans la table 'Transport'." << endl;
        mysql_free_result(result);
        return;
    }
    
    mysql_free_result(result);
	stringstream queryll;
    queryll << "INSERT INTO livraison (numliv, dateliv, numT) VALUES ("<< numlivStr << ", " << dateliv << ", " << numT << ", " << ")";

	string query = queryll.str();
    if (mysql_query(conn, query.c_str())) {
        cout << "Erreur lors de l'insertion dans la table 'Livraison' : " << mysql_error(conn) << endl;
        return;
    }

    cout << "La livraison a ete insere avec succes !" << endl;
    
}*/

void Gestion_livraison::InsereLivraison(MYSQL* conn)
{
    int numLiv, numT;
    string dateLiv;
    
    cout << "Entrez le numéro de livraison : ";
    cin >> numLiv;
    
    cout << "Entrez la date de livraison (format YYYY-MM-DD) : ";
    cin >> dateLiv;
    
    cout << "Entrez le numéro du transporteur : ";
    cin >> numT;
    
    stringstream query;
    query << "INSERT INTO livraison (numLiv, dateLiv, numT) VALUES (" << numLiv << ", '" << dateLiv << "', " << numT << ")";

    if (mysql_query(conn, query.str().c_str())) {
        cout << "Erreur lors de l'insertion dans la table 'livraison' : " << mysql_error(conn) << endl;
        return;
    }

    cout << "La livraison a été insérée avec succès !" << endl;
}


void Gestion_livraison::InsereDetailliv(MYSQL* conn)
{
    int NDL;
    float coutU, prixU;
    
    cout << "Entrez le numero de livraison : ";
    cin >> NDL;
    
    cout << "Entrez le cout unitaire : ";
    cin >> coutU;
    
    cout << "Entrez le prix unitaire : ";
    cin >> prixU;

    stringstream query;
    query << "INSERT INTO detailLiv (NDL, coutU, prixU) VALUES (" << NDL << ", " << coutU << ", " << prixU << ")";

    if (mysql_query(conn, query.str().c_str())) {
        cout << "Erreur lors de l'insertion dans la table 'detailLiv' : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Les détails de livraison ont été insérés avec succès !" << endl;
}



void Gestion_livraison::InsereTransaction(MYSQL* conn)
{
    int numTrans;
    string produitSortant, produitEntrant, dateH, seuilCom;
    
    cout << "Entrez le numéro de transaction : ";
    cin >> numTrans;
    
    cin.ignore();
    
    cout << "Entrez le produit sortant : ";
    getline(cin, produitSortant);
    
    cout << "Entrez le produit entrant : ";
    getline(cin, produitEntrant);
    
    cout << "Entrez la date et l'heure (format YYYY-MM-DD) : ";
    getline(cin, dateH);
    
    cout << "Entrez le seuil de communication : ";
    getline(cin, seuilCom);
    
    stringstream query;
    query << "INSERT INTO transactions (numTrans, produit_sortant, produit_entrant, dateH, seuilCom) VALUES (" << numTrans << ", '" << produitSortant << "', '" << produitEntrant << "', '" << dateH << "', '" << seuilCom << "')";

    if (mysql_query(conn, query.str().c_str())) {
        cout << "Erreur lors de l'insertion dans la table 'transactions' : " << mysql_error(conn) << endl;
        return;
    }

    cout << "La transaction a été insérée avec succès !" << endl;
}




void Gestion_livraison::InsereExpedition(MYSQL* conn) {
    int numExp;
    string dateExp, statut;
    float ct;

    cout << "Entrez le numéro d'expédition : ";
    cin >> numExp;

    cin.ignore();

    cout << "Entrez la date d'expédition (format YYYY-MM-DD) : ";
    getline(cin, dateExp);

    cout << "Entrez le coût de l'expédition : ";
    cin >> ct;

    cin.ignore();

    cout << "Entrez le statut de l'expédition : ";
    getline(cin, statut);

    stringstream query;
    query << "INSERT INTO expedition (NumExp, dateExp, cout, statut) VALUES ("
          << numExp << ", '" << dateExp << "', " << ct << ", '" << statut << "')";

    if (mysql_query(conn, query.str().c_str())) {
        cout << "Erreur lors de l'insertion dans la table 'expedition' : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'expédition a été insérée avec succès !" << endl;
}


void Gestion_livraison::InsereTransporteur(MYSQL* conn)
{
    int numT;
    string nomT, adresseT, teleT, typeT;
    float fraixT;
    
    cout << "Entrez le numéro du transporteur : ";
    cin >> numT;
    
    cin.ignore();
    
    cout << "Entrez le nom du transporteur : ";
    getline(cin, nomT);
    
    cout << "Entrez l'adresse du transporteur : ";
    getline(cin, adresseT);
    
    cout << "Entrez le numéro de téléphone du transporteur : ";
    getline(cin, teleT);
    
    cout << "Entrez le frais du transporteur : ";
    cin >> fraixT;
    
    cin.ignore();
    
    cout << "Entrez le type du transporteur : ";
    getline(cin, typeT);
    
    stringstream query;
    query << "INSERT INTO transporteur (numT, nomT, adresseT, teleT, fraixT, typeT) VALUES (" << numT << ", '" << nomT << "', '" << adresseT << "', '" << teleT << "', " << fraixT << ", '" << typeT << "')";

    if (mysql_query(conn, query.str().c_str())) {
        cout << "Erreur lors de l'insertion dans la table 'transporteur' : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'expédition a été insérée avec succès !" << endl;
}


void Gestion_livraison::InsereClient(MYSQL* conn)
{
    int numCli;
    string nomCli, adresseCli, teleCli;
    
    cout << "Entrez le numéro du client : ";
    cin >> numCli;
    
    cin.ignore();
    
    cout << "Entrez le nom du client : ";
    getline(cin, nomCli);
    
    cout << "Entrez l'adresse du client : ";
    getline(cin, adresseCli);
    
    cout << "Entrez le numéro de téléphone du client : ";
    getline(cin, teleCli);
    
    stringstream query;
    query << "INSERT INTO client (numCli, nomCli, adresseCli, teleCli) VALUES (" << numCli << ", '" << nomCli << "', '" << adresseCli << "', '" << teleCli << "')";

    if (mysql_query(conn, query.str().c_str())) {
        cout << "Erreur lors de l'insertion dans la table 'client' : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Le client a été inséré avec succès !" << endl;
}

void Gestion_livraison::ModifierLivraison(MYSQL* conn)
{
    int numLiv;
    cout << "Entrez le numero de livraison a modifier : ";
    cin >> numLiv;

    // Vérifier si la livraison existe
    stringstream ssNumLiv;
    ssNumLiv << numLiv;
    string numLivStr = ssNumLiv.str();

    string checkQuery = "SELECT numLiv FROM livraison WHERE numLiv = " + numLivStr;
    if (mysql_query(conn, checkQuery.c_str())) {
        cout << "Erreur lors de la verification de la livraison : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "La livraison avec le numero " << numLiv << " n'existe pas dans la table 'livraison'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    int choix;
    do {
        system("cls");
        // Afficher le menu pour la sélection de l'attribut à modifier
        cout << "Choisissez l'attribut a modifier : " << endl;
        cout << "1. Date de livraison" << endl;
        cout << "2. Quitter" << endl;

        cout << "Votre choix : ";
        cin >> choix;

        // Exécuter l'opération sélectionnée
        switch (choix) {
            case 1: {
                string dateLiv;
                cout << "Nouvelle date de livraison (format: AAAA-MM-JJ) : ";
                cin.ignore();
                getline(cin, dateLiv);

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE livraison SET dateLiv = '" << dateLiv << "' WHERE numLiv = " << numLivStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification de la date de livraison : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "La date de livraison pour la livraison avec le numero " << numLiv << " a ete modifiee avec succes !" << endl;
                break;
            }
            case 2:
                cout << "Sortie du programme." << endl;
                return;
            default:
                cout << "Choix invalide. Veuillez réessayer." << endl;
                break;
        }

        getchar();
        getch();
    } while (choix != 2);
}

void Gestion_livraison::ModifierDetLiv(MYSQL* conn)
{
    int NDL;
    cout << "Entrez le numero de detail de livraison a modifier : ";
    cin >> NDL;

    // Vérifier si le détail de livraison existe
    stringstream ssNDL;
    ssNDL << NDL;
    string NDLStr = ssNDL.str();

    string checkQuery = "SELECT NDL FROM detailLiv WHERE NDL = " + NDLStr;
    if (mysql_query(conn, checkQuery.c_str())) {
        cout << "Erreur lors de la verification du detail de livraison : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "Le detail de livraison avec le numero " << NDL << " n'existe pas dans la table 'detailLiv'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    int choix;
    do {
        system("cls");
        // Afficher le menu pour la sélection de l'attribut à modifier
        cout << "Choisissez l'attribut a modifier : " << endl;
        cout << "1. Cout unitaire" << endl;
        cout << "2. Prix unitaire" << endl;
        cout << "3. Quitter" << endl;

        cout << "Votre choix : ";
        cin >> choix;

        // Exécuter l'opération sélectionnée
        switch (choix) {
            case 1: {
                float coutU;
                cout << "Nouveau cout unitaire : ";
                cin >> coutU;

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE detailLiv SET coutU = " << coutU << " WHERE NDL = " << NDLStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification du cout unitaire : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Le cout unitaire pour le detail avec le numero " << NDL << " a ete modifie avec succes !" << endl;
                break;
            }
            case 2: {
                float prixU;
                cout << "Nouveau prix unitaire : ";
                cin >> prixU;

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE detailLiv SET prixU = " << prixU << " WHERE NDL = " << NDLStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification du prix unitaire : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Le prix unitaire pour le detail avec le numero " << NDL << " a ete modifie avec succes !" << endl;
                break;
            }
            case 3:
                cout << "Sortie du programme." << endl;
                return;
            default:
                cout << "Choix invalide. Veuillez réessayer." << endl;
                break;
        }

        getchar();
        getch();
    } while (choix != 3);
}

void Gestion_livraison::ModifierTransaction(MYSQL* conn)
{
    int numTrans;
    cout << "Entrez le numero de la transaction a modifier : ";
    cin >> numTrans;

    // Vérifier si la transaction existe
    stringstream ssNumTrans;
    ssNumTrans << numTrans;
    string numTransStr = ssNumTrans.str();

    string checkQuery = "SELECT numTrans FROM transactions WHERE numTrans = " + numTransStr;
    if (mysql_query(conn, checkQuery.c_str())) {
        cout << "Erreur lors de la verification de la transaction : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "La transaction avec le numero " << numTrans << " n'existe pas dans la table 'transactions'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    int choix;
    do {
        system("cls");
        // Afficher le menu pour la sélection de l'attribut à modifier
        cout << "Choisissez l'attribut a modifier : " << endl;
        cout << "1. Produit sortant" << endl;
        cout << "2. Produit entrant" << endl;
        cout << "3. Quitter" << endl;

        cout << "Votre choix : ";
        cin >> choix;

        // Exécuter l'opération sélectionnée
        switch (choix) {
            case 1: {
                string produitSortant;
                cout << "Nouveau produit sortant : ";
                cin.ignore();
                getline(cin, produitSortant);

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE transactions SET produit_sortant = '" << produitSortant << "' WHERE numTrans = " << numTransStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification du produit sortant : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Le produit sortant pour la transaction avec le numero " << numTrans << " a ete modifie avec succes !" << endl;
                break;
            }
            case 2: {
                string produitEntrant;
                cout << "Nouveau produit entrant : ";
                cin.ignore();
                getline(cin, produitEntrant);

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE transactions SET produit_entrant = '" << produitEntrant << "' WHERE numTrans = " << numTransStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification du produit entrant : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Le produit entrant pour la transaction avec le numero " << numTrans << " a ete modifie avec succes !" << endl;
                break;
            }
            case 3:
                cout << "Sortie du programme." << endl;
                return;
            default:
                cout << "Choix invalide. Veuillez réessayer." << endl;
                break;
        }

        getchar();
        getch();
    } while (choix != 3);
}


void Gestion_livraison::ModifierTransporteur(MYSQL* conn)
{
    int numT;
    cout << "Entrez le numero du transporteur a modifier : ";
    cin >> numT;

    // Vérifier si le transporteur existe
    stringstream ssNumT;
    ssNumT << numT;
    string numTStr = ssNumT.str();

    string checkQuery = "SELECT numT FROM transporteur WHERE numT = " + numTStr;
    if (mysql_query(conn, checkQuery.c_str())) {
        cout << "Erreur lors de la verification du transporteur : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "Le transporteur avec le numero " << numT << " n'existe pas dans la table 'transporteur'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    int choix;
    do {
        system("cls");
        // Afficher le menu pour la sélection de l'attribut à modifier
        cout << "Choisissez l'attribut a modifier : " << endl;
        cout << "1. Nom du transporteur" << endl;
        cout << "2. Adresse du transporteur" << endl;
        cout << "3. Telephone du transporteur" << endl;
        cout << "4. Frais du transporteur" << endl;
        cout << "5. Type du transporteur" << endl;
        cout << "6. Quitter" << endl;

        cout << "Votre choix : ";
        cin >> choix;

        // Exécuter l'opération sélectionnée
        switch (choix) {
            case 1: {
                string nomT;
                cout << "Nouveau nom du transporteur : ";
                cin.ignore();
                getline(cin, nomT);

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE transporteur SET nomT = '" << nomT << "' WHERE numT = " << numTStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification du nom du transporteur : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Le nom du transporteur avec le numero " << numT << " a ete modifie avec succes !" << endl;
                break;
            }
            case 2: {
                string adresseT;
                cout << "Nouvelle adresse du transporteur : ";
                cin.ignore();
                getline(cin, adresseT);

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE transporteur SET adresseT = '" << adresseT << "' WHERE numT = " << numTStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification de l'adresse du transporteur : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "L'adresse du transporteur avec le numero " << numT << " a ete modifiee avec succes !" << endl;
                break;
            }
            case 3: {
                string teleT;
                cout << "Nouveau telephone du transporteur : ";
                cin.ignore();
                getline(cin, teleT);

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE transporteur SET teleT = '" << teleT << "' WHERE numT = " << numTStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification du telephone du transporteur : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Le telephone du transporteur avec le numero " << numT << " a ete modifie avec succes !" << endl;
                break;
            }
            case 4: {
                float fraisT;
                cout << "Nouveaux frais du transporteur : ";
                cin >> fraisT;

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE transporteur SET fraisT = " << fraisT << " WHERE numT = " << numTStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification des frais du transporteur : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Les frais du transporteur avec le numero " << numT << " ont ete modifies avec succes !" << endl;
                break;
            }
            case 5: {
                string typeT;
                cout << "Nouveau type du transporteur : ";
                cin.ignore();
                getline(cin, typeT);

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE transporteur SET typeT = '" << typeT << "' WHERE numT = " << numTStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification du type du transporteur : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Le type du transporteur avec le numero " << numT << " a ete modifie avec succes !" << endl;
                break;
            }
            case 6:
                cout << "Sortie du programme." << endl;
                return;
            default:
                cout << "Choix invalide. Veuillez réessayer." << endl;
                break;
        }

        getchar();
        getch();
    } while (choix != 6);
}

void Gestion_livraison::ModifierClient(MYSQL* conn)
{
    int numCli;
    cout << "Entrez le numero du client a modifier : ";
    cin >> numCli;

    // Vérifier si le client existe
    stringstream ssNumCli;
    ssNumCli << numCli;
    string numCliStr = ssNumCli.str();

    string checkQuery = "SELECT numCli FROM client WHERE numCli = " + numCliStr;
    if (mysql_query(conn, checkQuery.c_str())) {
        cout << "Erreur lors de la verification du client : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "Le client avec le numero " << numCli << " n'existe pas dans la table 'client'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    int choix;
    do {
        system("cls");
        // Afficher le menu pour la sélection de l'attribut à modifier
        cout << "Choisissez l'attribut a modifier : " << endl;
        cout << "1. Nom du client" << endl;
        cout << "2. Adresse du client" << endl;
        cout << "3. Telephone du client" << endl;
        cout << "4. Quitter" << endl;

        cout << "Votre choix : ";
        cin >> choix;

        // Exécuter l'opération sélectionnée
        switch (choix) {
            case 1: {
                string nomCli;
                cout << "Nouveau nom du client : ";
                cin.ignore();
                getline(cin, nomCli);

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE client SET nomCli = '" << nomCli << "' WHERE numCli = " << numCliStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification du nom du client : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Le nom du client avec le numero " << numCli << " a ete modifie avec succes !" << endl;
                break;
            }
            case 2: {
                string adresseCli;
                cout << "Nouvelle adresse du client : ";
                cin.ignore();
                getline(cin, adresseCli);

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE client SET adresseCli = '" << adresseCli << "' WHERE numCli = " << numCliStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification de l'adresse du client : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "L'adresse du client avec le numero " << numCli << " a ete modifiee avec succes !" << endl;
                break;
            }
            case 3: {
                string teleCli;
                cout << "Nouveau telephone du client : ";
                cin.ignore();
                getline(cin, teleCli);

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE client SET teleCli = '" << teleCli << "' WHERE numCli = " << numCliStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification du telephone du client : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Le telephone du client avec le numero " << numCli << " a ete modifie avec succes !" << endl;
                break;
            }
            case 4:
                cout << "Sortie du programme." << endl;
                return;
            default:
                cout << "Choix invalide. Veuillez réessayer." << endl;
                break;
        }

        getchar();
        getch();
    } while (choix != 4);
}

void Gestion_livraison::SupprimerLivraison(MYSQL* conn)
{
    int numLiv;
    cout << "Entrez le numéro de la livraison à supprimer : ";
    cin >> numLiv;

    // Vérifier si la livraison existe
    stringstream ssNumLiv;
    ssNumLiv << numLiv;
    string numLivStr = ssNumLiv.str();

    string checkQuery = "SELECT numLiv FROM livraison WHERE numLiv = " + numLivStr;
    if (mysql_query(conn, checkQuery.c_str())) {
        cout << "Erreur lors de la vérification de la livraison : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "La livraison avec le numéro " << numLiv << " n'existe pas dans la table 'livraison'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Construire la requête de suppression
    string deleteQuery = "DELETE FROM livraison WHERE numLiv = " + numLivStr;

    // Exécuter la requête de suppression
    if (mysql_query(conn, deleteQuery.c_str())) {
        cout << "Erreur lors de la suppression de la livraison : " << mysql_error(conn) << endl;
        return;
    }

    cout << "La livraison avec le numéro " << numLiv << " a été supprimée avec succès de la table 'livraison'." << endl;
}

void Gestion_livraison::SupprimerDetLiv(MYSQL* conn)
{
    int NDL;
    cout << "Entrez le numéro de détail de livraison à supprimer : ";
    cin >> NDL;

    // Vérifier si le détail de livraison existe
    stringstream ssNDL;
    ssNDL << NDL;
    string NDLStr = ssNDL.str();

    string checkQuery = "SELECT NDL FROM detailLiv WHERE NDL = " + NDLStr;
    if (mysql_query(conn, checkQuery.c_str())) {
        cout << "Erreur lors de la vérification du détail de livraison : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "Le détail de livraison avec le numéro " << NDL << " n'existe pas dans la table 'detailLiv'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Construire la requête de suppression
    string deleteQuery = "DELETE FROM detailLiv WHERE NDL = " + NDLStr;

    // Exécuter la requête de suppression
    if (mysql_query(conn, deleteQuery.c_str())) {
        cout << "Erreur lors de la suppression du détail de livraison : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Le détail de livraison avec le numéro " << NDL << " a été supprimé avec succès de la table 'detailLiv'." << endl;
}

void Gestion_livraison::SupprimerTransaction(MYSQL* conn)
{
    int numTrans;
    cout << "Entrez le numéro de la transaction à supprimer : ";
    cin >> numTrans;

    // Vérifier si la transaction existe
    stringstream ssNumTrans;
    ssNumTrans << numTrans;
    string numTransStr = ssNumTrans.str();

    string checkQuery = "SELECT numTrans FROM transactions WHERE numTrans = " + numTransStr;
    if (mysql_query(conn, checkQuery.c_str())) {
        cout << "Erreur lors de la vérification de la transaction : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "La transaction avec le numéro " << numTrans << " n'existe pas dans la table 'transactions'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Construire la requête de suppression
    string deleteQuery = "DELETE FROM transactions WHERE numTrans = " + numTransStr;

    // Exécuter la requête de suppression
    if (mysql_query(conn, deleteQuery.c_str())) {
        cout << "Erreur lors de la suppression de la transaction : " << mysql_error(conn) << endl;
        return;
    }

    cout << "La transaction avec le numéro " << numTrans << " a été supprimée avec succès de la table 'transactions'." << endl;
}

void Gestion_livraison::SupprimerExpedition(MYSQL* conn) {
    int numExp;

    cout << "Entrez le numéro d'expédition à supprimer : ";
    cin >> numExp;

    stringstream query;
    query << "DELETE FROM expedition WHERE NumExp = " << numExp;

    if (mysql_query(conn, query.str().c_str())) {
        cout << "Erreur lors de la suppression de l'expédition : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'expédition a été supprimée avec succès !" << endl;
}

void Gestion_livraison::SupprimerTransporteur(MYSQL* conn)
{
    int numT;
    cout << "Entrez le numéro du transporteur à supprimer : ";
    cin >> numT;

    // Vérifier si le transporteur existe
    stringstream ssNumT;
    ssNumT << numT;
    string numTStr = ssNumT.str();

    string checkQuery = "SELECT numT FROM transporteur WHERE numT = " + numTStr;
    if (mysql_query(conn, checkQuery.c_str())) {
        cout << "Erreur lors de la vérification du transporteur : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "Le transporteur avec le numéro " << numT << " n'existe pas dans la table 'transporteur'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Construire la requête de suppression
    string deleteQuery = "DELETE FROM transporteur WHERE numT = " + numTStr;

    // Exécuter la requête de suppression
    if (mysql_query(conn, deleteQuery.c_str())) {
        cout << "Erreur lors de la suppression du transporteur : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Le transporteur avec le numéro " << numT << " a été supprimé avec succès de la table 'transporteur'." << endl;
}

void Gestion_livraison::SupprimerClient(MYSQL* conn)
{
    int numCli;
    cout << "Entrez le numéro du client à supprimer : ";
    cin >> numCli;

    // Vérifier si le client existe
    stringstream ssNumCli;
    ssNumCli << numCli;
    string numCliStr = ssNumCli.str();

    string checkQuery = "SELECT numCli FROM client WHERE numCli = " + numCliStr;
    if (mysql_query(conn, checkQuery.c_str())) {
        cout << "Erreur lors de la vérification du client : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "Le client avec le numéro " << numCli << " n'existe pas dans la table 'client'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Construire la requête de suppression
    string deleteQuery = "DELETE FROM client WHERE numCli = " + numCliStr;

    // Exécuter la requête de suppression
    if (mysql_query(conn, deleteQuery.c_str())) {
        cout << "Erreur lors de la suppression du client : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Le client avec le numéro " << numCli << " a été supprimé avec succès de la table 'client'." << endl;
    
}


void Gestion_livraison::ModifierExpedition(MYSQL* conn) {
    int numExp;
    cout << "Entrez le numéro de l'expédition à modifier : ";
    cin >> numExp;

    // Vérifier si l'expédition existe
    stringstream ssNumExp;
    ssNumExp << numExp;
    string numExpStr = ssNumExp.str();

    string checkQuery = "SELECT NumExp FROM expedition WHERE NumExp = " + numExpStr;
    if (mysql_query(conn, checkQuery.c_str())) {
        cout << "Erreur lors de la vérification de l'expédition : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "L'expédition avec le numéro " << numExp << " n'existe pas dans la table 'expedition'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    int choix;
    do {
        system("cls");
        // Afficher le menu pour la sélection de l'attribut à modifier
        cout << "Choisissez l'attribut à modifier : " << endl;
        cout << "1. Date de l'expédition" << endl;
        cout << "2. Coût de l'expédition" << endl;
        cout << "3. Statut de l'expédition" << endl;
        cout << "4. Quitter" << endl;

        cout << "Votre choix : ";
        cin >> choix;

        // Exécuter l'opération sélectionnée
        switch (choix) {
            case 1: {
                string dateExp;
                cout << "Nouvelle date de l'expédition (format YYYY-MM-DD) : ";
                cin.ignore();
                getline(cin, dateExp);

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE expedition SET dateExp = '" << dateExp << "' WHERE NumExp = " << numExpStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification de la date de l'expédition : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "La date de l'expédition avec le numéro " << numExp << " a été modifiée avec succès !" << endl;
                break;
            }
            case 2: {
                float coutExp;
                cout << "Nouveau coût de l'expédition : ";
                cin >> coutExp;

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE expedition SET cout = " << coutExp << " WHERE NumExp = " << numExpStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification du coût de l'expédition : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Le coût de l'expédition avec le numéro " << numExp << " a été modifié avec succès !" << endl;
                break;
            }
            case 3: {
                string statutExp;
                cout << "Nouveau statut de l'expédition : ";
                cin.ignore();
                getline(cin, statutExp);

                // Construire la requête de mise à jour
                stringstream updateQuerySS;
                updateQuerySS << "UPDATE expedition SET statut = '" << statutExp << "' WHERE NumExp = " << numExpStr;

                string updateQuery = updateQuerySS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, updateQuery.c_str())) {
                    cout << "Erreur lors de la modification du statut de l'expédition : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Le statut de l'expédition avec le numéro " << numExp << " a été modifié avec succès !" << endl;
                break;
            }
            case 4:
                cout << "Sortie du programme." << endl;
                return;
            default:
                cout << "Choix invalide. Veuillez réessayer." << endl;
                break;
        }

        getchar();
        getch();
    } while (choix != 4);
}

void Gestion_livraison::ListerLivraison(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM livraison";

    if (mysql_query(conn, query)) {
        printf("Erreur lors de l'exécution de la requête : %s\n", mysql_error(conn));
        return;
    }

    result = mysql_store_result(conn);
    if (result == NULL) {
        printf("Erreur lors de la récupération des données : %s\n", mysql_error(conn));
        return;
    }

    int numFields = mysql_num_fields(result);

    while ((row = mysql_fetch_row(result))) {
        for (int i = 0; i < numFields; i++) {
            field = mysql_fetch_field_direct(result, i);
            printf("%s ", row[i]);
        }
        printf("\n");
    }

    mysql_free_result(result);
}


void Gestion_livraison::ListerDetailliv(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM detailLiv";

    if (mysql_query(conn, query)) {
        printf("Erreur lors de l'exécution de la requête : %s\n", mysql_error(conn));
        return;
    }

    result = mysql_store_result(conn);
    if (result == NULL) {
        printf("Erreur lors de la récupération des données : %s\n", mysql_error(conn));
        return;
    }

    int numFields = mysql_num_fields(result);

    while ((row = mysql_fetch_row(result))) {
        for (int i = 0; i < numFields; i++) {
            field = mysql_fetch_field_direct(result, i);
            printf("%s ", row[i]);
        }
        printf("\n");
    }

    mysql_free_result(result);
}


void Gestion_livraison::ListerTransaction(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM transactions";

    if (mysql_query(conn, query)) {
        printf("Erreur lors de l'exécution de la requête : %s\n", mysql_error(conn));
        return;
    }

    result = mysql_store_result(conn);
    if (result == NULL) {
        printf("Erreur lors de la récupération des données : %s\n", mysql_error(conn));
        return;
    }

    int numFields = mysql_num_fields(result);

    while ((row = mysql_fetch_row(result))) {
        for (int i = 0; i < numFields; i++) {
            field = mysql_fetch_field_direct(result, i);
            printf("%s ", row[i]);
        }
        printf("\n");
    }

    mysql_free_result(result);
}


void Gestion_livraison::ListerExpedition(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM expedition";

    if (mysql_query(conn, query)) {
        printf("Erreur lors de l'exécution de la requête : %s\n", mysql_error(conn));
        return;
    }

    result = mysql_store_result(conn);
    if (result == NULL) {
        printf("Erreur lors de la récupération des données : %s\n", mysql_error(conn));
        return;
    }

    int numFields = mysql_num_fields(result);

    while ((row = mysql_fetch_row(result))) {
        for (int i = 0; i < numFields; i++) {
            field = mysql_fetch_field_direct(result, i);
            printf("%s ", row[i]);
        }
        printf("\n");
    }

    mysql_free_result(result);
}


void Gestion_livraison::ListerTransporteur(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM transporteur";

    if (mysql_query(conn, query)) {
        printf("Erreur lors de l'exécution de la requête : %s\n", mysql_error(conn));
        return;
    }

    result = mysql_store_result(conn);
    if (result == NULL) {
        printf("Erreur lors de la récupération des données : %s\n", mysql_error(conn));
        return;
    }

    int numFields = mysql_num_fields(result);

    while ((row = mysql_fetch_row(result))) {
        for (int i = 0; i < numFields; i++) {
            field = mysql_fetch_field_direct(result, i);
            printf("%s ", row[i]);
        }
        printf("\n");
    }

    mysql_free_result(result);
}


void Gestion_livraison::ListerClient(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM client";

    if (mysql_query(conn, query)) {
        printf("Erreur lors de l'exécution de la requête : %s\n", mysql_error(conn));
        return;
    }

    result = mysql_store_result(conn);
    if (result == NULL) {
        printf("Erreur lors de la récupération des données : %s\n", mysql_error(conn));
        return;
    }

    int numFields = mysql_num_fields(result);

    while ((row = mysql_fetch_row(result))) {
        for (int i = 0; i < numFields; i++) {
            field = mysql_fetch_field_direct(result, i);
            printf("%s ", row[i]);
        }
        printf("\n");
    }

    mysql_free_result(result);
}






