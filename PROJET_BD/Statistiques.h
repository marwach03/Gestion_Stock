#ifndef STATISTIQUES_H
#define STATISTIQUES_H

#include <iostream>
#include <mysql.h>
#include <string>
#include <sstream>
#include <conio.h>
using namespace std;

class Statistiques
{
	public:
		Statistiques();
		~Statistiques();
		void GetSalesStats(MYSQL* conn); 
		void Temps_moyen_de_rotation_des_stocks(MYSQL* conn); 
		void GetRuptureStockTaux(MYSQL* conn);
		void GetCoutMoyenArticleVendu(MYSQL* conn);
		void GetAverageStockLevel(MYSQL* conn);
		void GetStockRotationRate(MYSQL* conn);
		void GetAverageStockCost(MYSQL* conn);
		void GetOrderSatisfactionRate(MYSQL* conn);
		void GetDelayedOrdersCount(MYSQL* conn);
		void GetCostOfStockOut(MYSQL* conn);
	private:
		MYSQL *conn;
};

#endif
