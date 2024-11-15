#include "Statistiques.h"
#include <cstdlib>
using namespace std;

Statistiques::Statistiques()
{
	conn = mysql_init(NULL);
}

Statistiques::~Statistiques()
{
	
}


//1
void Statistiques::GetSalesStats(MYSQL* conn) 
{
    if (mysql_query(conn, "SELECT COUNT(*) AS ventes, SUM(qteCom) AS quantite_vendue FROM detalCom")) 
	{
        std::cout << "Erreur lors de l'exécution de la requête : " << mysql_error(conn) << std::endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);

    if (result) 
	{
        MYSQL_ROW row = mysql_fetch_row(result);

        if (row) 
		{
            int ventes = std::atoi(row[0]);
            int quantite_vendue = std::atoi(row[1]);

            std::cout << "Nombre de ventes : " << ventes << std::endl;
            std::cout << "Quantite vendue : " << quantite_vendue << std::endl;
        }

        mysql_free_result(result);
    }
}

//2

void Statistiques::Temps_moyen_de_rotation_des_stocks(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;

    if (mysql_query(conn, "SELECT AVG(DATEDIFF(c.dateCom, l.dateLiv)) AS temps_rotation_stocks "
                          "FROM commande c "
                          "INNER JOIN livraison l ON c.numLiv = l.numLiv "
                          "WHERE c.statut = 'Livré'")) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        return;
    }

    result = mysql_use_result(conn);
    if (result) {
        if ((row = mysql_fetch_row(result))) {
            int temps_rotation = row[0] ? atoi(row[0]) : 0;
            printf("Temps moyen de rotation des stocks : %d jours\n", temps_rotation);
        }
        mysql_free_result(result);
    }
}

//3
void Statistiques::GetRuptureStockTaux(MYSQL* conn)
{
    MYSQL_RES* result;
    MYSQL_ROW row;

    if (mysql_query(conn, "SELECT (COUNT(*) * 100) / (SELECT COUNT(*) FROM commande) AS taux_rupture_stock "
                          "FROM commande "
                          "WHERE statut = 'En attente'")) {
        std::cout << "Erreur lors de l'exécution de la requête : " << mysql_error(conn) << std::endl;
        return;
    }

    result = mysql_use_result(conn);
    if (result) {
        if ((row = mysql_fetch_row(result))) {
            double tauxRuptureStock = atof(row[0]);
            std::cout << "Taux de rupture de stock : " << tauxRuptureStock << "%" << std::endl;
        }
        mysql_free_result(result);
    }
}

//4
void Statistiques::GetCoutMoyenArticleVendu(MYSQL* conn)
{
    MYSQL_RES* result;
    MYSQL_ROW row;

    if (mysql_query(conn, "SELECT (SELECT SUM(coutU) AS cout_total_comm FROM detalcom) / (SELECT SUM(qtecom) AS quantite_vendue_comm FROM detalcom) AS cout_moyen_par_article;")) {
        std::cout << "Erreur lors de l'exécution de la requête : " << mysql_error(conn) << std::endl;
        return;
    }

    result = mysql_use_result(conn);
    if (result) {
        if ((row = mysql_fetch_row(result))) {
            double coutMoyen = atof(row[0]);
            std::cout << "Cout moyen des articles vendus : " << coutMoyen << std::endl;
        }
        mysql_free_result(result);
    }
}


//5

void Statistiques::GetAverageStockLevel(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;

    if (mysql_query(conn, "SELECT AVG(qteA) AS niveau_stock_moyen FROM article")) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        return;
    }

    result = mysql_use_result(conn);
    if (result) {
        if ((row = mysql_fetch_row(result))) {
            double niveauStockMoyen = atof(row[0]);
            printf("Niveau de stock moyen : %.2f\n", niveauStockMoyen);
        }
        mysql_free_result(result);
    }
}


//6
void Statistiques::GetStockRotationRate(MYSQL *conn) {
    MYSQL_RES *result;
    MYSQL_ROW row;

    // Calcul du nombre total de commandes
    if (mysql_query(conn, "SELECT COUNT(*) AS total_commandes FROM commande")) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        return;
    }

    result = mysql_use_result(conn);
    if (result) {
        if ((row = mysql_fetch_row(result))) {
            int totalCommandes = std::atoi(row[0]);

            printf("Nombre total de commandes : %d\n", totalCommandes);
        }
        mysql_free_result(result);
    }
}



//7
void Statistiques::GetAverageStockCost(MYSQL* conn) 
{
    if (mysql_query(conn, "SELECT AVG(coutA * qteA) AS cout_moyen_stocks FROM article")) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        return;
    }

    MYSQL_RES* result = mysql_use_result(conn);
    if (result) {
        MYSQL_ROW row;
        if ((row = mysql_fetch_row(result))) {
            int coutMoyenStocks = std::atoi(row[0]);

            printf("Coût moyen des stocks : %d\n", coutMoyenStocks);
        }
        mysql_free_result(result);
    }
}


//8
void Statistiques::GetOrderSatisfactionRate(MYSQL* conn) {
    MYSQL_RES* result;
    MYSQL_ROW row;

    if (mysql_query(conn, "SELECT (COUNT(CASE WHEN statut = 'Satisfait' THEN 1 END) / COUNT(*)) * 100 AS taux_satisfaction "
                          "FROM commande")) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        return;
    }

    result = mysql_use_result(conn);
    if (result) {
        if ((row = mysql_fetch_row(result))) {
            int taux_satisfaction = std::atoi(row[0]); // Utiliser std::atoi pour convertir en entier
            printf("Taux de satisfaction des commandes : %d%%\n", taux_satisfaction);
        }
        mysql_free_result(result);
    }
}


//9
void Statistiques::GetDelayedOrdersCount(MYSQL* conn) {
    MYSQL_RES *result;
    MYSQL_ROW row;

    if (mysql_query(conn, "SELECT COUNT(*) AS commandes_en_retard "
                          "FROM commande c "
                          "JOIN livraison l ON c.numliv= l.numliv "
                          "WHERE l.dateLiv > c.datecom")) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        return;
    }

    result = mysql_use_result(conn);
    if (result) {
        if ((row = mysql_fetch_row(result))) {
            printf("Nombre de commandes en retard : %s\n", row[0]);
        }
        mysql_free_result(result);
    }
}

void Statistiques::GetCostOfStockOut(MYSQL* conn) 
{
    MYSQL_RES* result;
    MYSQL_ROW row;

    if (mysql_query(conn, "SELECT SUM(ventes_perdues) + SUM(couts_production_supplementaires) /100 AS cout_rupture_stock "
                          "FROM ( "
                          "    SELECT (qteA * prixV) AS ventes_perdues, (coutA * qteA) AS couts_production_supplementaires "
                          "    FROM article "
                          "    WHERE qteA = 100 "
                          ") AS ruptures_stock")) {
        fprintf(stderr, "%s\n", mysql_error(conn));
        return;
    }

    result = mysql_use_result(conn);
    if (result) {
        if ((row = mysql_fetch_row(result))) {
            double coutRuptureStock = std::atof(row[0]);
            std::cout << "Coût de la rupture de stock : " << coutRuptureStock << std::endl;
        }
        mysql_free_result(result);
    }
}




