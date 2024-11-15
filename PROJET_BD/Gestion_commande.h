#ifndef GESTION_COMMANDE_H
#define GESTION_COMMANDE_H
#include <iostream>
#include <mysql.h>
#include <string>
#include <sstream>
#include <conio.h>

class Gestion_commande
{
	public:
		Gestion_commande();
		~Gestion_commande();
		void InsereCommande(MYSQL* conn);
		void InsereDetailCom(MYSQL* conn);
		void InsereFournisseur(MYSQL* conn);
		
		void SupprimerCommande(MYSQL* conn);
		void SupprimerDetailCom(MYSQL* conn);
		void SupprimerFournisseur(MYSQL* conn);
		
		void ModifierCommande(MYSQL* conn);
		void ModifierDetailCom(MYSQL* conn);
		void ModifierFournisseur(MYSQL* conn);
		
		void ListerCommande(MYSQL* conn);
		void ListerDetailCom(MYSQL* conn);
		void ListerFournisseur(MYSQL* conn);
	private:
		MYSQL *conn;
};

#endif
