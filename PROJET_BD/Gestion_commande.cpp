#include "Gestion_commande.h"
using namespace std;
Gestion_commande::Gestion_commande()
{
	conn = mysql_init(NULL);
}

Gestion_commande::~Gestion_commande()
{
	
}


void Gestion_commande::InsereCommande(MYSQL* conn)
{
    int numCom, numLiv, numCli;
    string dateCom, statut, nomF;

    cout << "Entrez le numéro de la commande : ";
    cin >> numCom;

    // Vérifier si le numéro de commande existe déjà dans la table
    stringstream ssNumCom;
    ssNumCom << numCom;
    string numComStr = ssNumCom.str();

    string check = "SELECT numCom FROM commande WHERE numCom = " + numComStr;
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la verification du numero de commande : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) > 0) {
        cout << "Le numero de commande " << numCom << " existe deja dans la table 'commande'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    cin.ignore();  // Ignorer le caractère de nouvelle ligne

    cout << "Entrez la date de la commande (au format 'AAAA-MM-JJ') : ";
    getline(cin, dateCom);

    cout << "Entrez le statut de la commande : ";
    getline(cin, statut);

    cout << "Entrez le numéro de livraison : ";
    cin >> numLiv;

    cin.ignore();  // Ignorer le caractère de nouvelle ligne

    cout << "Entrez le nom du fournisseur : ";
    getline(cin, nomF);

    cout << "Entrez le numéro du client : ";
    cin >> numCli;

    // Construire la requête d'insertion
    stringstream insert;
    insert << "INSERT INTO commande (numCom, dateCom, statut, numLiv, nomF, numCli) VALUES (";
    insert << numCom << ", '" << dateCom << "', '" << statut << "', " << numLiv << ", '" << nomF << "', " << numCli << ")";

    string insertS = insert.str();

    // Exécuter la requête d'insertion
    if (mysql_query(conn, insertS.c_str())) {
        cout << "Erreur lors de l'insertion de la commande : " << mysql_error(conn) << endl;
        return;
    }

    cout << "La commande avec le numéro " << numCom << " a ete inseree avec succes dans la table 'commande'." << endl;
}


void Gestion_commande::InsereDetailCom(MYSQL* conn)
{
    int NDC;
    cout << "Entrez le numero de detail de commande : ";
    cin >> NDC;

    // Vérifier si le détail de commande existe déjà
    stringstream ssNDC;
    ssNDC << NDC;
    string NDCStr = ssNDC.str();

    string check = "SELECT NDC FROM detalCom WHERE NDC = " + NDCStr;
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification du détail de commande : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) > 0) {
        cout << "Le detail de commande avec le numero " << NDC << " existe deja dans la table 'detalCom'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    int qteCom;
    float coutU, prixU;

    cout << "Quantite de commande : ";
    cin >> qteCom;

    cout << "Cout unitaire : ";
    cin >> coutU;

    cout << "Prix unitaire : ";
    cin >> prixU;

    // Construire la requête d'insertion
    stringstream insertSS;
    insertSS << "INSERT INTO detalCom (NDC, qteCom, coutU, prixU) VALUES (";
    insertSS << NDCStr << ", " << qteCom << ", " << coutU << ", " << prixU << ")";

    string insert = insertSS.str();

    // Exécuter la requête d'insertion
    if (mysql_query(conn, insert.c_str())) {
        cout << "Erreur lors de l'insertion du detail de commande : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Le détail de commande avec le numero " << NDC << " a ete insere avec succes dans la table 'detalCom'." << endl;
}

void Gestion_commande::InsereFournisseur(MYSQL* conn)
{
    string nomF, adresseF, teleF, faxF, courrielF, contact;
    
    cin.ignore();  // Ignore the newline character
    
    cout << "Entrez le nom du fournisseur : ";
    getline(cin, nomF);
    
    cout << "Entrez l'adresse du fournisseur : ";
    getline(cin, adresseF);
    
    cout << "Entrez le numero de téléphone du fournisseur : ";
    getline(cin, teleF);
    
    cout << "Entrez le numero de fax du fournisseur : ";
    getline(cin, faxF);
    
    cout << "Entrez le courriel du fournisseur (au format nom@gmail.com ): ";
    getline(cin, courrielF);
    
    cout << "Entrez le nom du contact du fournisseur : ";
    getline(cin, contact);
    
    // Construire la requête d'insertion
    string insert = "INSERT INTO fournisseur (nomF, adresseF, teleF, faxF, courrielF, contact) VALUES ('" + nomF + "', '" + adresseF + "', '" + teleF + "', '" + faxF + "', '" + courrielF + "', '" + contact + "')";

    // Exécuter la requête d'insertion
    if (mysql_query(conn, insert.c_str())) {
        cout << "Erreur lors de l'insertion du fournisseur : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Le fournisseur " << nomF << " a ete insere avec succes !" << endl;
}

	
void Gestion_commande::SupprimerCommande(MYSQL* conn)
{
    int numCom;
    cout << "Entrez le numéro de la commande à supprimer : ";
    cin >> numCom;

    // Vérifier si la commande existe
    stringstream ssNumCom;
    ssNumCom << numCom;
    string numComStr = ssNumCom.str();

    string check = "SELECT numCom FROM commande WHERE numCom = " + numComStr;
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification de la commande : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "La commande avec le numero " << numCom << " n'existe pas dans la table 'commande'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Construire la requête de suppression
    string deletes = "DELETE FROM commande WHERE numCom = " + numComStr;

    // Exécuter la requête de suppression
    if (mysql_query(conn, deletes.c_str())) {
        cout << "Erreur lors de la suppression de la commande : " << mysql_error(conn) << endl;
        return;
    }

    cout << "La commande avec le numero " << numCom << " a été supprimée avec succès de la table 'commande'." << endl;
}

void Gestion_commande::SupprimerDetailCom(MYSQL* conn)
{
    int NDC;
    cout << "Entrez le numero de detail de commande a supprimer : ";
    cin >> NDC;

    // Vérifier si le détail de commande existe
    stringstream ssNDC;
    ssNDC << NDC;
    string NDCStr = ssNDC.str();

    string check = "SELECT NDC FROM detalCom WHERE NDC = " + NDCStr;
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la verification du detail de commande : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "Le detail de commande avec le numero " << NDC << " n'existe pas dans la table 'detalCom'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Construire la requête de suppression
    stringstream deleteSS;
    deleteSS << "DELETE FROM detalCom WHERE NDC = " << NDCStr;

    string deletes = deleteSS.str();

    // Exécuter la requête de suppression
    if (mysql_query(conn, deletes.c_str())) {
        cout << "Erreur lors de la suppression du detail de commande : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Le detail de commande avec le numero " << NDC << " a ete supprime avec succes de la table 'detalCom'." << endl;
}

void Gestion_commande::SupprimerFournisseur(MYSQL* conn)
{
    string nomF;
    
    cin.ignore();  // Ignore the newline character
    
    cout << "Entrez le nom du fournisseur a supprimer : ";
    getline(cin, nomF);
    
    // Vérifier si le fournisseur existe
    string check = "SELECT nomF FROM fournisseur WHERE nomF = '" + nomF + "'";
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification du fournisseur : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "Le fournisseur avec le nom '" << nomF << "' n'existe pas dans la table 'fournisseur'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);
    
    // Construire la requête de suppression
    string deletes = "DELETE FROM fournisseur WHERE nomF = '" + nomF + "'";
    
    // Exécuter la requête de suppression
    if (mysql_query(conn, deletes.c_str())) {
        cout << "Erreur lors de la suppression du fournisseur : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Le fournisseur " << nomF << " a ete supprime avec succes !" << endl;
}

		
void Gestion_commande::ModifierCommande(MYSQL* conn)
{
    int numCom;
    cout << "Entrez le numéro de la commande à modifier : ";
    cin >> numCom;

    // Vérifier si la commande existe
    stringstream ssNumCom;
    ssNumCom << numCom;
    string numComStr = ssNumCom.str();

    string check = "SELECT numCom FROM commande WHERE numCom = " + numComStr;
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification de la commande : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "La commande avec le numero " << numCom << " n'existe pas dans la table 'commande'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    int choix;
    string nouvelleValeur;

    cin.ignore();  // Ignorer le caractère de nouvelle ligne

    do {
    	system("cls");
        cout << "Choisissez l'attribut a modifier : " << endl;
        cout << "1. Date de la commande" << endl;
        cout << "2. Statut de la commande" << endl;
        cout << "3. Quitter" << endl;
        cout << "Votre choix : ";
        cin >> choix;

        cin.ignore();  // Ignorer le caractère de nouvelle ligne

        string attribut;
        switch (choix) {
            case 1:
                attribut = "dateCom";
                cout << "Nouvelle date de la commande (au format 'AAAA-MM-JJ') : ";
                getline(cin, nouvelleValeur);
                break;
            case 2:
                attribut = "statut";
                cout << "Nouveau statut de la commande (En cours , En attente , Livre) : ";
                getline(cin, nouvelleValeur);
                break;
            case 3:
                cout << "Sortie du programme." << endl;
                break;
            default:
                cout << "Choix invalide. Veuillez reessayer." << endl;
                break;
        }

        if (choix >= 1 && choix <= 2) {
            string update = "UPDATE commande SET " + attribut + " = '" + nouvelleValeur + "' WHERE numCom = " + numComStr;
            if (mysql_query(conn, update.c_str())) {
                cout << "Erreur lors de la modification de l'attribut : " << mysql_error(conn) << endl;
                return;
            }
            cout << "L'attribut a ete modifie avec succes !" << endl;
        }
		getch();
		getchar();
    } while (choix != 3);
}


void Gestion_commande::ModifierDetailCom(MYSQL* conn)
{
    int NDC;
    cout << "Entrez le numero de detail de commande a modifier : ";
    cin >> NDC;

    // Vérifier si le détail de commande existe
    stringstream ssNDC;
    ssNDC << NDC;
    string NDCStr = ssNDC.str();

    string check = "SELECT NDC FROM detalCom WHERE NDC = " + NDCStr;
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la verification du detail de commande : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "Le detail de commande avec le numéro " << NDC << " n'existe pas dans la table 'detalCom'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    int choix;
    do {
        system("cls");
        // Afficher le menu pour la sélection de l'attribut à modifier
        cout << "Choisissez l'attribut a modifier : " << endl;
        cout << "1. Quantite de commande" << endl;
        cout << "2. Cout unitaire" << endl;
        cout << "3. Prix unitaire" << endl;
        cout << "4. Quitter" << endl;

        cout << "Votre choix : ";
        cin >> choix;

        // Exécuter l'opération sélectionnée
        switch (choix) {
            case 1: {
                int qteCom;
                cout << "Nouvelle quantite de commande : ";
                cin >> qteCom;

                // Construire la requête de mise à jour
                stringstream updateSS;
                updateSS << "UPDATE detalCom SET qteCom = " << qteCom << " WHERE NDC = " << NDCStr;

                string update = updateSS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, update.c_str())) {
                    cout << "Erreur lors de la modification de la quantite de commande : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "La quantite de commande pour le detail avec le numero " << NDC << " a ete modifiee avec succes !" << endl;
                break;
            }
            case 2: {
                float coutU;
                cout << "Nouveau cout unitaire : ";
                cin >> coutU;

                // Construire la requête de mise à jour
                stringstream updateSS;
                updateSS << "UPDATE detalCom SET coutU = " << coutU << " WHERE NDC = " << NDCStr;

                string update = updateSS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, update.c_str())) {
                    cout << "Erreur lors de la modification du coût unitaire : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Le cout unitaire pour le detail avec le numero " << NDC << " a ete modifie avec succes !" << endl;
                break;
            }
            case 3: {
                float prixU;
                cout << "Nouveau prix unitaire : ";
                cin >> prixU;

                // Construire la requête de mise à jour
                stringstream updateSS;
                updateSS << "UPDATE detalCom SET prixU = " << prixU << " WHERE NDC = " << NDCStr;

                string update = updateSS.str();

                // Exécuter la requête de mise à jour
                if (mysql_query(conn, update.c_str())) {
                    cout << "Erreur lors de la modification du prix unitaire : " << mysql_error(conn) << endl;
                    return;
                }

                cout << "Le prix unitaire pour le detail avec le numéro " << NDC << " a ete modifie avec succes !" << endl;
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



void Gestion_commande::ModifierFournisseur(MYSQL* conn)
{
    string nomF;
    
    cin.ignore();  // Ignore the newline character
    
    cout << "Entrez le nom du fournisseur a modifier : ";
    getline(cin, nomF);
    
    // Vérifier si le fournisseur existe
    string check = "SELECT nomF FROM fournisseur WHERE nomF = '" + nomF + "'";
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification du fournisseur : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "Le fournisseur avec le nom '" << nomF << "' n'existe pas dans la table 'fournisseur'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);
    
    string adresseF, teleF, faxF, courrielF, contact;

    int choix;
    do {
        system("cls");
        // Afficher le menu de sélection de l'attribut à modifier
        cout << "Choisissez l'attribut a modifier : " << endl;
        cout << "1. Adresse du fournisseur" << endl;
        cout << "2. Telephone du fournisseur" << endl;
        cout << "3. Fax du fournisseur" << endl;
        cout << "4. Courriel du fournisseur" << endl;
        cout << "5. Contact du fournisseur" << endl;
        cout << "6. Quitter" << endl;

        cout << "Votre choix : ";
        cin >> choix;

        // Exécuter l'opération sélectionnée
        switch (choix) {
            case 1:
                cin.ignore();  // Ignorer le caractère de nouvelle ligne
                cout << "Nouvelle adresse du fournisseur : ";
                getline(cin, adresseF);
                break;
            case 2:
                cin.ignore();  // Ignorer le caractère de nouvelle ligne
                cout << "Nouveau telephone du fournisseur : ";
                getline(cin, teleF);
                break;
            case 3:
                cin.ignore();  // Ignorer le caractère de nouvelle ligne
                cout << "Nouveau fax du fournisseur : ";
                getline(cin, faxF);
                break;
            case 4:
                cin.ignore();  // Ignorer le caractère de nouvelle ligne
                cout << "Nouveau courriel du fournisseur : ";
                getline(cin, courrielF);
                break;
            case 5:
                cin.ignore();  // Ignorer le caractère de nouvelle ligne
                cout << "Nouveau contact du fournisseur : ";
                getline(cin, contact);
                break;
            case 6:
                cout << "Sortie du programme." << endl;
                return;
            default:
                cout << "Choix invalide. Veuillez réessayer." << endl;
                break;
        }

        // Construire la requête de mise à jour
        stringstream updateSS;
        updateSS << "UPDATE fournisseur SET ";
        switch (choix) {
            case 1:
                updateSS << "adresseF = '" << adresseF << "'";
                break;
            case 2:
                updateSS << "teleF = '" << teleF << "'";
                break;
            case 3:
                updateSS << "faxF = '" << faxF << "'";
                break;
            case 4:
                updateSS << "courrielF = '" << courrielF << "'";
                break;
            case 5:
                updateSS << "contact = '" << contact << "'";
                break;
            default:
                return;
        }
        updateSS << " WHERE nomF = '" << nomF << "'";

        string update = updateSS.str();

        // Exécuter la requête de mise à jour
        if (mysql_query(conn, update.c_str())) {
            cout << "Erreur lors de la modification du fournisseur : " << mysql_error(conn) << endl;
            return;
        }

        cout << "Le fournisseur avec le nom '" << nomF << "' a ete modifie avec succes !" << endl;
        getchar();
        getch();
    } while (choix != 6);
}


void Gestion_commande::ListerCommande(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM commande";

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

void Gestion_commande::ListerDetailCom(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM detalCom";

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
		
void Gestion_commande::ListerFournisseur(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM fournisseur";

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
