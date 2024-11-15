#include "Gestion_produit.h"


Gestion_produit::Gestion_produit()
{
	conn = mysql_init(NULL);
}

Gestion_produit::~Gestion_produit()
{
	//rien
}

void Gestion_produit::InsereArticle(MYSQL* conn)
{
    int codeA;
    cout << "Entrez le code de l'article : ";
    cin >> codeA;

    string nomA, descriptionA, nomF, nomCat;
    float coutA, prixV;
    int qteA, numEmp;

    cin.ignore();  // Ignorer le caractère de nouvelle ligne restant après la saisie précédente

    cout << "Nom de l'article : ";
    getline(cin, nomA);

    cout << "Description de l'article : ";
    getline(cin, descriptionA);

    cout << "Cout de l'article : ";
    cin >> coutA;

    cout << "Prix de vente de l'article : ";
    cin >> prixV;

    cout << "Quantite de l'article : ";
    cin >> qteA;

    cout << "Numero d'emplacement de l'article (1,9,12): ";
    cin >> numEmp;

    cin.ignore();  // Ignore the newline character after reading numEmp

    cout << "Nom Fournisseur (AMINE , RYM , MOHAMMED): ";
    getline(cin, nomF);

    cout << "Nom categorie (A,B,C): ";
    getline(cin, nomCat);

    stringstream ss;
    ss << codeA;
    string codeAStr = ss.str();

    ss.str("");
    ss << coutA;
    string coutAStr = ss.str();

    ss.str("");
    ss << prixV;
    string prixVStr = ss.str();

    ss.str("");
    ss << qteA;
    string qteAStr = ss.str();

    ss.str("");
    ss << numEmp;
    string numEmpStr = ss.str();


    // Check if the numEmp exists in the emplacement table
    string check = "SELECT numEmp FROM emplacement WHERE numEmp = " + numEmpStr;
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification de l'emplacement : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "L'emplacement specifie n'existe pas dans la table 'emplacement'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    string insert = "INSERT INTO article (codeA, nomA, descriptionA, coutA, qteA, prixV, nomF, nomCat, numEmp) VALUES (" + codeAStr + ", '" + nomA + "', '" + descriptionA + "', " + coutAStr + ", " + qteAStr + ", " + prixVStr + ", '" + nomF + "', '" + nomCat + "', " + numEmpStr + ")";

    if (mysql_query(conn, insert.c_str())) {
        cout << "Erreur lors de l'insertion dans la table 'article' : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'article a ete insere avec succes !" << endl;
}

void Gestion_produit::InsereCategorie(MYSQL* conn)
{
    string nomCat, descriptionCat;

    cin.ignore();
    cout << "Entrez le nom de la categorie : ";
    getline(cin, nomCat);

    cout << "Description de la categorie : ";
    getline(cin, descriptionCat);

    string insert = "INSERT INTO categorie (nomCat, descriptionCat) VALUES ('" + nomCat + "', '" + descriptionCat + "')";

    if (mysql_query(conn, insert.c_str())) {
        cout << "Erreur lors de l'insertion dans la table 'categorie' : " << mysql_error(conn) << endl;
        return;
    }
    

    cout << "La categorie a ete inseree avec succes !" << endl;
}

void Gestion_produit::InsereEmplacement(MYSQL* conn)
{
    int numEmp;
    string nomEmp, descriptionEmp;
    float capaciteEmp;

    cout << "Entrez le numero de l'emplacement : ";
    cin >> numEmp;

    cin.ignore();
    cout << "Entrez le nom de l'emplacement : ";
    getline(cin, nomEmp);

    cout << "Description de l'emplacement : ";
    getline(cin, descriptionEmp);

    cout << "Entrez la capacite de l'emplacement : ";
    cin >> capaciteEmp;

    cin.ignore();

    stringstream ss;
    ss << numEmp;
    string numEmpStr = ss.str();

    ss.str("");
    ss << capaciteEmp;
    string capaciteEmpStr = ss.str();

    // Check if the numEmp already exists in the emplacement table
    string check = "SELECT numEmp FROM emplacement WHERE numEmp = " + numEmpStr;
    if (mysql_query(conn, check.c_str())) 
	{
        cout << "Erreur lors de la verification de l'emplacement : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) > 0)
	{
        cout << "L'emplacement avec le numero specifie existe deja dans la table 'emplacement'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // SQL query to insert data into the "emplacement" table
    string insert = "INSERT INTO emplacement (numEmp, nomEmp, descriptionEmp, capaciteEmp) VALUES (" +numEmpStr + ", '" + nomEmp + "', '" + descriptionEmp + "', " +capaciteEmpStr + ")";

    if (mysql_query(conn, insert.c_str())) {
        cout << "Erreur lors de l'insertion dans la table 'emplacement' : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'emplacement a ete inseree avec succes ! !" << endl;
}


		
void Gestion_produit::SupprimerArticle(MYSQL* conn)
{
    int codeA;
    cout << "Entrez le code de l'article a supprimer : ";
    cin >> codeA;

    // Check if the article exists
    stringstream ss;
    ss << codeA;
    string codeAStr = ss.str();

    string check = "SELECT codeA FROM article WHERE codeA = " + codeAStr;
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification de l'article : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "L'article avec le code " << codeA << " n'existe pas dans la table 'article'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Delete the article
    string deletes = "DELETE FROM article WHERE codeA = " + codeAStr;
    if (mysql_query(conn, deletes.c_str())) {
        cout << "Erreur lors de la suppression de l'article : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'article avec le code " << codeA << " a ete supprime avec succes !" << endl;
}



void Gestion_produit::SupprimerCategorie(MYSQL* conn)
{
    string nomCat;
    cout << "Entrez le nom de la categorie a supprimer : ";
    cin.ignore();
    getline(cin, nomCat);

    // Check if the categorie exists
    string check = "SELECT nomCat FROM categorie WHERE nomCat = '" + nomCat + "'";
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification de la categorie : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "La categorie '" << nomCat << "' n'existe pas dans la table 'categorie'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Delete the categorie
    string deletes = "DELETE FROM categorie WHERE nomCat = '" + nomCat + "'";
    if (mysql_query(conn, deletes.c_str())) {
        cout << "Erreur lors de la suppression de la categorie : " << mysql_error(conn) << endl;
        return;
    }

    cout << "La categorie '" << nomCat << "' a ete supprimee avec succes !" << endl;
}



void Gestion_produit::SupprimerEmplacement(MYSQL* conn)
{
    int numEmp;
    cout << "Entrez le numero d'emplacement a supprimer : ";
    cin >> numEmp;

    // Check if the emplacement exists
    stringstream ss;
    ss << numEmp;
    string numEmpStr = ss.str();

    string check = "SELECT numEmp FROM emplacement WHERE numEmp = " + numEmpStr;
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification de l'emplacement : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "L'emplacement avec le numero " << numEmp << " n'existe pas dans la table 'emplacement'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    // Delete the emplacement
    string deletes = "DELETE FROM emplacement WHERE numEmp = " + numEmpStr;
    if (mysql_query(conn, deletes.c_str())) {
        cout << "Erreur lors de la suppression de l'emplacement : " << mysql_error(conn) << endl;
        return;
    }

    cout << "L'emplacement avec le numero " << numEmp << " a ete supprime avec succes !" << endl;
}

	
void Gestion_produit::ModifierArticle(MYSQL* conn)
{
    int codeA;
    cout << "Entrez le code de l'article a modifier : ";
    cin >> codeA;

    // Check if the article exists
    stringstream ssCode;
    ssCode << codeA;
    string codeAStr = ssCode.str();

    string check = "SELECT codeA FROM article WHERE codeA = " + codeAStr;
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification de l'article : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "L'article avec le code " << codeA << " n'existe pas dans la table 'article'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    string nomA, descriptionA;
    float coutA, prixV;
    int qteA;

    cin.ignore();  // Ignore the newline character

    int choix;
    do {
        system("cls");
        // Display menu for attribute selection
        cout << "Choisissez l'attribut a modifier : " << endl;
        cout << "1. Nom de l'article" << endl;
        cout << "2. Description de l'article" << endl;
        cout << "3. Cout de l'article" << endl;
        cout << "4. Prix de vente de l'article" << endl;
        cout << "5. Quantite de l'article" << endl;
        cout << "6. Quitter" << endl;

        cout << "Votre choix : ";
        cin >> choix;

        // Execute the selected operation
        switch (choix) {
            case 1:
                cin.ignore();  // Ignore the newline character
                cout << "Nouveau nom de l'article : ";
                getline(cin, nomA);
                break;
            case 2:
                cin.ignore();  // Ignore the newline character
                cout << "Nouvelle description de l'article : ";
                getline(cin, descriptionA);
                break;
            case 3:
                cout << "Nouveau cout de l'article : ";
                cin >> coutA;
                break;
            case 4:
                cout << "Nouveau prix de vente de l'article : ";
                cin >> prixV;
                break;
            case 5:
                cout << "Nouvelle quantite de l'article : ";
                cin >> qteA;
                break;
            case 6:
                cout << "Sortie du programme." << endl;
                return;
            default:
                cout << "Choix invalide. Veuillez reessayer." << endl;
                break;
        }

        // Update the selected attribute
        stringstream updateSS;
        switch (choix) {
            case 1:
                updateSS << nomA;
                break;
            case 2:
                updateSS << descriptionA;
                break;
            case 3:
                updateSS << coutA;
                break;
            case 4:
                updateSS << prixV;
                break;
            case 5:
                updateSS << qteA;
                break;
            default:
                return;
        }

        // Construct the update query
        stringstream updateS;
        updateS << "UPDATE article SET ";
        switch (choix) {
            case 1:
                updateS << "nomA = '" << updateSS.str() << "'";
                break;
            case 2:
                updateS << "descriptionA = '" << updateSS.str() << "'";
                break;
            case 3:
                updateS << "coutA = " << updateSS.str();
                break;
            case 4:
                updateS << "prixV = " << updateSS.str();
                break;
            case 5:
                updateS << "qteA = " << updateSS.str();
                break;
            default:
                return;
        }
        updateS << " WHERE codeA = " << codeAStr;

        string update = updateS.str();

        // Execute the update query
        if (mysql_query(conn, update.c_str())) {
            cout << "Erreur lors de la modification de l'article : " << mysql_error(conn) << endl;
            return;
        }

        cout << "L'article avec le code " << codeA << " a ete modifie avec succes !" << endl;
		getchar();
		getch();
    } while (choix != 6);
}

void Gestion_produit::ModifierCategorie(MYSQL* conn)
{
    string nomCat;
    cout << "Entrez le nom de la categorie a modifier : ";
    cin.ignore(); // Ignore the newline character
    getline(cin, nomCat);

    // Check if the category exists
    string check = "SELECT nomCat FROM categorie WHERE nomCat = '" + nomCat + "'";
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la verification de la categorie : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "La categorie avec le nom '" << nomCat << "' n'existe pas dans la table 'categorie'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    string descriptionCat;
    cout << "Nouvelle description de la categorie : ";
    getline(cin, descriptionCat);

    // Construct the update query
    string update = "UPDATE categorie SET descriptionCat = '" + descriptionCat + "' WHERE nomCat = '" + nomCat + "'";

    // Execute the update query
    if (mysql_query(conn, update.c_str())) {
        cout << "Erreur lors de la modification de la catégorie : " << mysql_error(conn) << endl;
        return;
    }

    cout << "La catégorie avec le nom '" << nomCat << "' a ete modifiee avec succes !" << endl;
}



void Gestion_produit::ModifierEmplacement(MYSQL* conn)
{
    int numEmp;
    cout << "Entrez le numéro de l'emplacement à modifier : ";
    cin >> numEmp;

    // Vérifier si l'emplacement existe
    stringstream ssNumEmp;
    ssNumEmp << numEmp;
    string numEmpStr = ssNumEmp.str();

    string check = "SELECT numEmp FROM emplacement WHERE numEmp = " + numEmpStr;
    if (mysql_query(conn, check.c_str())) {
        cout << "Erreur lors de la vérification de l'emplacement : " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (mysql_num_rows(result) == 0) {
        cout << "L'emplacement avec le numéro " << numEmp << " n'existe pas dans la table 'emplacement'." << endl;
        mysql_free_result(result);
        return;
    }
    mysql_free_result(result);

    string nomEmp, descriptionEmp;
    float capaciteEmp;

    cin.ignore();  // Ignorer le caractère de nouvelle ligne

    int choix;
    do {
        system("cls");
        // Afficher le menu de sélection des attributs
        cout << "Choisissez l'attribut a modifier : " << endl;
        cout << "1. Nom de l'emplacement" << endl;
        cout << "2. Description de l'emplacement" << endl;
        cout << "3. Capacite de l'emplacement" << endl;
        cout << "4. Quitter" << endl;

        cout << "Votre choix : ";
        cin >> choix;

        // Exécuter l'opération sélectionnée
        switch (choix) {
            case 1:
                cin.ignore();  // Ignorer le caractère de nouvelle ligne
                cout << "Nouveau nom de l'emplacement : ";
                getline(cin, nomEmp);
                break;
            case 2:
                cin.ignore();  // Ignorer le caractère de nouvelle ligne
                cout << "Nouvelle description de l'emplacement : ";
                getline(cin, descriptionEmp);
                break;
            case 3:
                cout << "Nouvelle capacite de l'emplacement : ";
                cin >> capaciteEmp;
                break;
            case 4:
                cout << "Sortie du programme." << endl;
                return;
            default:
                cout << "Choix invalide. Veuillez réessayer." << endl;
                break;
        }

        // Construire la requête de mise à jour
        stringstream updateSS;
        switch (choix) {
            case 1:
                updateSS << nomEmp;
                break;
            case 2:
                updateSS << descriptionEmp;
                break;
            case 3:
                updateSS << capaciteEmp;
                break;
            default:
                return;
        }

        // Construire la requête de mise à jour
        stringstream updateS;
        updateS << "UPDATE emplacement SET ";
        switch (choix) {
            case 1:
                updateS << "nomEmp = '" << updateSS.str() << "'";
                break;
            case 2:
                updateS << "descriptionEmp = '" << updateSS.str() << "'";
                break;
            case 3:
                updateS << "capaciteEmp = " << updateSS.str();
                break;
            default:
                return;
        }
        updateS << " WHERE numEmp = " << numEmpStr;

        string update = updateS.str();

        // Exécuter la requête de mise à jour
        if (mysql_query(conn, update.c_str())) {
            cout << "Erreur lors de la modification de l'emplacement : " << mysql_error(conn) << endl;
            return;
        }

        cout << "L'emplacement avec le numéro " << numEmp << " a ete modifie avec succes !" << endl;
		getchar();
		getch();
    } while (choix != 4);
}




void Gestion_produit::ListerArticle(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;
    
    string query = "SELECT * FROM article";

    if (mysql_query(conn, query.c_str())) {
        std::cout << "Erreur lors de l'exécution de la requête : " << mysql_error(conn) << endl;
        return;
    }

    result = mysql_store_result(conn);
    if (result == NULL) {
        cout << "Erreur lors de la récupération des données : " << mysql_error(conn) << endl;
        return;
    }

    int numFields = mysql_num_fields(result);

    while ((row = mysql_fetch_row(result))) {
        for (int i = 0; i < numFields; i++) {
            field = mysql_fetch_field_direct(result, i);
            cout << row[i] << " ";
        }
        cout << endl;
    }

    mysql_free_result(result);
}



void Gestion_produit::ListerCategorie(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    std::string query = "SELECT * FROM categorie";

    if (mysql_query(conn, query.c_str())) {
        std::cout << "Erreur lors de l'exécution de la requête : " << mysql_error(conn) << std::endl;
        return;
    }

    result = mysql_store_result(conn);
    if (result == NULL) {
        std::cout << "Erreur lors de la récupération des données : " << mysql_error(conn) << std::endl;
        return;
    }

    int numFields = mysql_num_fields(result);

    while ((row = mysql_fetch_row(result))) {
        for (int i = 0; i < numFields; i++) {
            field = mysql_fetch_field_direct(result, i);
            std::cout << row[i] << " ";
        }
        std::cout << std::endl;
    }

    mysql_free_result(result);
}





void Gestion_produit::ListerEmplacement(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;
    MYSQL_FIELD* field;

    std::string query = "SELECT * FROM emplacement";

    if (mysql_query(conn, query.c_str())) {
        std::cout << "Erreur lors de l'exécution de la requête : " << mysql_error(conn) << std::endl;
        return;
    }

    result = mysql_store_result(conn);
    if (result == NULL) {
        std::cout << "Erreur lors de la récupération des données : " << mysql_error(conn) << std::endl;
        return;
    }

    int numFields = mysql_num_fields(result);

    while ((row = mysql_fetch_row(result))) {
        for (int i = 0; i < numFields; i++) {
            field = mysql_fetch_field_direct(result, i);
            std::cout << row[i] << " ";
        }
        std::cout << std::endl;
    }

    mysql_free_result(result);
}

