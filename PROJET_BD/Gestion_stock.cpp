#include "Gestion_stock.h"
using namespace std;

Gestion_stock::Gestion_stock()
{
	conn = mysql_init(NULL);
}

Gestion_stock::~Gestion_stock()
{
	
}

void Gestion_stock::InsererUtilisateur(MYSQL* conn)
{
    string nomU, courrielU, mdp, admin, nomSys;

    cout << "Entrez les informations de l'utilisateur : " << endl;
    cout << "Nom : ";
    cin.ignore();
    getline(cin, nomU);

    cout << "Courriel : ";
    getline(cin, courrielU);

    cout << "Mot de passe : ";
    getline(cin, mdp);

    cout << "Admin  : ";
    getline(cin, admin);

    cout << "Nom du systeme : ";
    getline(cin, nomSys);

    stringstream insertSS;
    insertSS << "INSERT INTO utilisateur (nomU, courrielU, mdp, admin, nomSys) VALUES ('"<< nomU << "', '" << courrielU << "', '" << mdp << "', '" << admin << "', '" << nomSys << "')";

    string insert = insertSS.str();

    if (mysql_query(conn, insert.c_str())) {
        cout << "Erreur lors de l'insertion de l'utilisateur : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'utilisateur '" << nomU << "' a ete insere avec succes !" << endl;
}



void Gestion_stock::InsererRole(MYSQL* conn)
{
    string admin, type;

    cout << "Entrez les informations du role : " << endl;
    cout << "Admin : ";
    cin.ignore();
    getline(cin, admin);

    cout << "Type : ";
    getline(cin, type);

    stringstream insertSS;
    insertSS << "INSERT INTO role (admin, type) VALUES ('";
    insertSS << admin << "', '" << type << "')";

    string insert = insertSS.str();

    if (mysql_query(conn, insert.c_str())) {
        cout << "Erreur lors de l'insertion du role : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Le role avec le nom d'admin '" << admin << "' a ete insere avec succes !" << endl;
}


void Gestion_stock::InsererHistorique(MYSQL* conn)
{
    string dateHStr;
    int qte;

    cout << "Entrez les informations pour l'historique : " << endl;
    cout << "Date (AAAA-MM-JJ) : ";
    cin.ignore();
    getline(cin, dateHStr);

    cout << "Quantite : ";
    cin >> qte;

    // Vérifier si la date existe déjà dans la table
    stringstream checkSS;
    checkSS << "SELECT dateH FROM historique WHERE dateH = '" << dateHStr << "'";

    string check = checkSS.str();

    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification de l'historique : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) > 0) {
        cout << "L'historique pour la date " << dateHStr << " existe deja dans la table 'historique'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Insérer les données dans la table historique
    stringstream insertSS;
    insertSS << "INSERT INTO historique (dateH, qte) VALUES ('" << dateHStr << "', " << qte << ")";

    string insert = insertSS.str();

    if (mysql_query(conn, insert.c_str())) {
        cout << "Erreur lors de l'insertion de l'historique : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'historique pour la date " << dateHStr << " a ete insere avec succes !" << endl;
}


void Gestion_stock::InsererAlerte(MYSQL* conn)
{
    string seuilAl, dateAlStr;
    int qte;

    cout << "Entrez les informations de l'alerte : " << endl;
    cout << "Seuil d'alerte : ";
    cin.ignore();
    getline(cin, seuilAl);

    cout << "Date de l'alerte (AAAA-MM-JJ) : ";
    cin >> dateAlStr;

    cout << "Quantite : ";
    cin >> qte;

    // Convertir la date en format MySQL
    stringstream ssDate;
    ssDate << "'" << dateAlStr << "'";
    string dateAl = ssDate.str();

    // Construire la requête d'insertion
    stringstream insertSS;
    insertSS << "INSERT INTO alerte (seuilAl, dateAl, qte) VALUES ('";
    insertSS << seuilAl << "', " << dateAl << ", " << qte << ")";

    string insert = insertSS.str();

    // Exécuter la requête d'insertion
    if (mysql_query(conn, insert.c_str())) {
        cout << "Erreur lors de l'insertion de l'alerte : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'alerte avec le seuil '" << seuilAl << "' a ete inseree avec succes !" << endl;
}


void Gestion_stock::InsererParametre(MYSQL* conn)
{
    string seuilCom;
    float taux;

    cout << "Entrez les informations du parametre : " << endl;
    cout << "Seuil de commande : ";
    cin.ignore();
    getline(cin, seuilCom);

    cout << "Taux : ";
    cin >> taux;

    stringstream insertSS;
    insertSS << "INSERT INTO parametre_stock (seuilCom, taux) VALUES ('";
    insertSS << seuilCom << "', " << taux << ")";

    string insert = insertSS.str();

    if (mysql_query(conn, insert.c_str())) {
        cout << "Erreur lors de l'insertion du parametre : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Le parametre avec le seuil de commande '" << seuilCom << "' a ete insere avec succes !" << endl;
}


void Gestion_stock::SupprimerUtilisateur(MYSQL* conn)
{
    string nomU;

    cout << "Entrez le nom de l'utilisateur a supprimer : ";
    cin.ignore();
    getline(cin, nomU);

    stringstream deleteSS;
    deleteSS << "DELETE FROM utilisateur WHERE nomU = '";
    deleteSS << nomU << "'";

    string deletes = deleteSS.str();

    if (mysql_query(conn, deletes.c_str())) {
        cout << "Erreur lors de la suppression de l'utilisateur : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'utilisateur '" << nomU << "' a ete supprime avec succes !" << endl;
}


void Gestion_stock::SupprimerRole(MYSQL* conn)
{
    string admin;

    cout << "Entrez le nom d'admin du role a supprimer : ";
    cin.ignore();
    getline(cin, admin);

    stringstream deleteSS;
    deleteSS << "DELETE FROM role WHERE admin = '";
    deleteSS << admin << "'";

    string deletes = deleteSS.str();

    if (mysql_query(conn, deletes.c_str())) {
        cout << "Erreur lors de la suppression du role : " << mysql_error(conn) << endl;
        return;
    }

    if (mysql_affected_rows(conn) == 0) {
        cout << "Le role avec le nom d'admin '" << admin << "' n'existe pas dans la table 'role'." << endl;
    } else {
        cout << "Le role avec le nom d'admin '" << admin << "' a ete supprime avec succes !" << endl;
    }
}


void Gestion_stock::SupprimerHistorique(MYSQL* conn)
{
    string dateHStr;

    cout << "Entrez la date de l'historique a supprimer (AAAA-MM-JJ) : ";
    cin.ignore();
    getline(cin, dateHStr);

    // Vérifier si l'historique existe dans la table
    stringstream checkSS;
    checkSS << "SELECT dateH FROM historique WHERE dateH = '" << dateHStr << "'";

    string check = checkSS.str();

    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification de l'historique : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "L'historique pour la date " << dateHStr << " n'existe pas dans la table 'historique'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Supprimer l'entrée de l'historique
    stringstream deleteSS;
    deleteSS << "DELETE FROM historique WHERE dateH = '" << dateHStr << "'";

    string deletes = deleteSS.str();

    if (mysql_query(conn, deletes.c_str())) {
        cout << "Erreur lors de la suppression de l'historique : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'historique pour la date " << dateHStr << " a ete supprime avec succes !" << endl;
}


void Gestion_stock::SupprimerAlerte(MYSQL* conn)
{
    string seuilAl;

    cout << "Entrez le seuil d'alerte de l'alerte a supprimer : ";
    cin.ignore();
    getline(cin, seuilAl);

    // Construire la requête de suppression
    stringstream deleteSS;
    deleteSS << "DELETE FROM alerte WHERE seuilAl = '" << seuilAl << "'";

    string deletes = deleteSS.str();

    // Exécuter la requête de suppression
    if (mysql_query(conn, deletes.c_str())) {
        cout << "Erreur lors de la suppression de l'alerte : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'alerte avec le seuil '" << seuilAl << "' a ete supprime avec succes !" << endl;
}


void Gestion_stock::SupprimerParametre(MYSQL* conn)
{
    string seuilCom;

    cout << "Entrez le seuil de commande du parametre a supprimer : ";
    cin.ignore();
    getline(cin, seuilCom);

    stringstream deleteSS;
    deleteSS << "DELETE FROM parametre_stock WHERE seuilCom = '" << seuilCom << "'";

    string deletes = deleteSS.str();

    if (mysql_query(conn, deletes.c_str())) {
        cout << "Erreur lors de la suppression du parametre : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Le parametre avec le seuil de commande '" << seuilCom << "' a ete supprime avec succes !" << endl;
}


void Gestion_stock::ModifierUtilisateur(MYSQL* conn)
{
    string nomU;
    cout << "Entrez le nom de l'utilisateur a modifier : ";
    cin.ignore();
    getline(cin, nomU);

    // Vérifier si l'utilisateur existe
    string check = "SELECT nomU FROM utilisateur WHERE nomU = '" + nomU + "'";
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification de l'utilisateur : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "L'utilisateur '" << nomU << "' n'existe pas dans la table 'utilisateur'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    int choix;
    do {
        system("cls");
        cout << "Choisissez l'attribut a modifier pour l'utilisateur '" << nomU << "' :" << endl;
        cout << "1. Courriel" << endl;
        cout << "2. Mot de passe" << endl;
        cout << "3. Quitter" << endl;

        cout << "Votre choix : ";
        cin >> choix;

        cin.ignore(); // Ignorer le caractère de nouvelle ligne

        // Variables pour stocker les nouvelles valeurs
        string nouvelleValeur;

        switch (choix) {
            case 1:
                cout << "Nouveau courriel : ";
                getline(cin, nouvelleValeur);
                break;
            case 2:
                cout << "Nouveau mot de passe : ";
                getline(cin, nouvelleValeur);
                break;
            case 3:
                cout << "Sortie du programme." << endl;
                return;
            default:
                cout << "Choix invalide. Veuillez réessayer." << endl;
                break;
        }

        if (choix >= 1 && choix <= 4) {
            stringstream updateSS;
            updateSS << "UPDATE utilisateur SET ";
            switch (choix) {
                case 1:
                    updateSS << "courrielU = '" << nouvelleValeur << "'";
                    break;
                case 2:
                    updateSS << "mdp = '" << nouvelleValeur << "'";
                    break;
                default:
                    return;
            }
            updateSS << " WHERE nomU = '" << nomU << "'";

            string update = updateSS.str();

            if (mysql_query(conn, update.c_str())) {
                cout << "Erreur lors de la modification de l'utilisateur : " << mysql_error(conn) << endl;
                return;
            }
			
			cout << "L'Utilisateur avec le code " << nomU << " a ete modifie avec succes !" << endl;
            getchar();
            getch();
        }
    } while (choix != 3);
}


void Gestion_stock::ModifierRole(MYSQL* conn)
{
    string admin;

    cout << "Entrez le nom d'admin du role a modifier : ";
    cin.ignore();
    getline(cin, admin);

    // Vérifier si le rôle existe
    stringstream checkSS;
    checkSS << "SELECT admin FROM role WHERE admin = '";
    checkSS << admin << "'";

    string check = checkSS.str();

    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la verification du role : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "Le role avec le nom d'admin '" << admin << "' n'existe pas dans la table 'role'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    string type;

    cout << "Entrez le nouveau type de role (UTILISATEUR , ADMINISTRATEUR) : ";
    getline(cin, type);

    stringstream updateSS;
    updateSS << "UPDATE role SET type = '";
    updateSS << type << "' WHERE admin = '";
    updateSS << admin << "'";

    string update = updateSS.str();

    if (mysql_query(conn, update.c_str())) {
        cout << "Erreur lors de la modification du role : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Le rôle avec le nom d'admin '" << admin << "' a ete modifie avec succes !" << endl;
}

void Gestion_stock::ModifierHistorique(MYSQL* conn)
{
    string dateHStr;

    cout << "Entrez la date de l'historique a modifier (AAAA-MM-JJ) : ";
    cin.ignore();
    getline(cin, dateHStr);

    // Vérifier si l'historique existe dans la table
    stringstream checkSS;
    checkSS << "SELECT dateH FROM historique WHERE dateH = '" << dateHStr << "'";

    string check = checkSS.str();

    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification de l'historique : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "L'historique pour la date " << dateHStr << " n'existe pas dans la table 'historique'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Demander la nouvelle quantité
    int nouvelleQte;
    cout << "Entrez la nouvelle quantite : ";
    cin >> nouvelleQte;

    // Mettre à jour l'entrée de l'historique
    stringstream updateSS;
    updateSS << "UPDATE historique SET qte = " << nouvelleQte << " WHERE dateH = '" << dateHStr << "'";

    string update = updateSS.str();

    if (mysql_query(conn, update.c_str())) {
        cout << "Erreur lors de la modification de l'historique : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'historique pour la date " << dateHStr << " a ete modifie avec succes !" << endl;
}


void Gestion_stock::ModifierAlerte(MYSQL* conn)
{
    string seuilAl;

    cout << "Entrez le seuil d'alerte de l'alerte a modifier : ";
    cin.ignore();
    getline(cin, seuilAl);

    // Vérifier si l'alerte existe
    stringstream checkSS;
    checkSS << "SELECT seuilAl FROM alerte WHERE seuilAl = '" << seuilAl << "'";

    string check = checkSS.str();

    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la verification de l'alerte : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "L'alerte avec le seuil '" << seuilAl << "' n'existe pas dans la table 'alerte'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Variables pour les nouvelles valeurs de l'alerte
    string newSeuilAl;
    string newDateAl;
    int newQte;

    int choix;
    do {
        system("cls");
        // Afficher le menu des attributs à modifier
        cout << "Choisissez l'attribut a modifier : " << endl;
        cout << "1. Date d'alerte" << endl;
        cout << "2. Quantite" << endl;
        cout << "3. Quitter" << endl;

        cout << "Votre choix : ";
        cin >> choix;

        // Exécuter l'opération sélectionnée
        switch (choix) {
            case 1:
                cin.ignore();
                cout << "Nouvelle date d'alerte (AAAA-MM-JJ) : ";
                getline(cin, newDateAl);
                break;
            case 2:
                cout << "Nouvelle quantite : ";
                cin >> newQte;
                break;
            case 3:
                cout << "Sortie du programme." << endl;
                return;
            default:
                cout << "Choix invalide. Veuillez réessayer." << endl;
                break;
        }

        // Construire la requête de mise à jour
        stringstream updateSS;
        updateSS << "UPDATE alerte SET ";
        switch (choix) {
            case 1:
                updateSS << "dateAl = '" << newDateAl << "'";
                break;
            case 2:
                updateSS << "qte = " << newQte;
                break;
            default:
                return;
        }
        updateSS << " WHERE seuilAl = '" << seuilAl << "'";

        string update = updateSS.str();

        // Exécuter la requête de mise à jour
        if (mysql_query(conn, update.c_str())) {
            cout << "Erreur lors de la modification de l'alerte : " << mysql_error(conn) << endl;
            return;
        }

        cout << "L'alerte avec le seuil '" << seuilAl << "' a ete modifie avec succes !" << endl;
        getch();
        getchar();
    } while (choix != 3);
}



void Gestion_stock::ModifierParametre(MYSQL* conn)
{
    string seuilCom;
    float taux;

    cout << "Entrez le seuil de commande du parametre a modifier : ";
    cin.ignore();
    getline(cin, seuilCom);

    // Vérifier si le paramètre existe
    stringstream checkSS;
    checkSS << "SELECT seuilCom FROM parametre_stock WHERE seuilCom = '" << seuilCom << "'";

    string check = checkSS.str();

    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification du parametre : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "Le parametre avec le seuil de commande '" << seuilCom << "' n'existe pas dans la table 'parametre_stock'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    cout << "Entrez les nouvelles informations du parametre : " << endl;


    cout << "Nouveau taux : ";
    cin >> taux;

    stringstream updateSS;
    updateSS << "UPDATE parametre_stock SET taux = " << taux << " WHERE seuilCom = '" << seuilCom << "'";

    string update = updateSS.str();

    if (mysql_query(conn, update.c_str())) {
        cout << "Erreur lors de la modification du parametre : " << mysql_error(conn) << endl;
        return;
    }

    cout << "Le parametre avec le seuil de commande '" << seuilCom << "' a ete modifie avec succes !" << endl;
}


void Gestion_stock::ListerUtilisateur(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM utilisateur";

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


void Gestion_stock::ListerRole(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM role";

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

void Gestion_stock::ListerHistorique(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM historique";

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


void Gestion_stock::ListerAlerte(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM alerte";

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


void Gestion_stock::ListerParametre(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    const char* query = "SELECT * FROM parametre_stock";

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

