#ifndef GESTION_PRODUIT_H
#define GESTION_PRODUIT_H

#include <iostream>
#include <mysql.h>
#include <string>
#include <sstream>
#include <conio.h>

using namespace std;

class Gestion_produit
{
	public:
		Gestion_produit();
		~Gestion_produit();
		
		void InsereArticle(MYSQL* conn);
		void InsereCategorie(MYSQL* conn);
		void InsereEmplacement(MYSQL* conn);
		
		void SupprimerArticle(MYSQL* conn);
		void SupprimerCategorie(MYSQL* conn);
		void SupprimerEmplacement(MYSQL* conn);
		
		void ModifierArticle(MYSQL* conn);
		void ModifierCategorie(MYSQL* conn);
		void ModifierEmplacement(MYSQL* conn);
		
		void ListerArticle(MYSQL* conn);
		void ListerCategorie(MYSQL* conn);
		void ListerEmplacement(MYSQL* conn);
	private:
		MYSQL *conn;
		
};

#endif
