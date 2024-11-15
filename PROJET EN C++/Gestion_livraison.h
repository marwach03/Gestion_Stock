#ifndef GESTION_LIVRAISON_H
#define GESTION_LIVRAISON_H

#include <iostream>
#include <mysql.h>
#include <string>
#include <sstream>
#include <conio.h>

class Gestion_livraison
{
	public:
		Gestion_livraison();
		~Gestion_livraison();
		
		void InsereLivraison(MYSQL* conn);
		void InsereDetailliv(MYSQL* conn);
		void InsereTransaction(MYSQL* conn);
		void InsereExpedition(MYSQL* conn);
		void InsereTransporteur(MYSQL* conn);
		void InsereClient(MYSQL* conn);
		
		void SupprimerLivraison(MYSQL* conn);
		void SupprimerDetLiv(MYSQL* conn);
		void SupprimerTransaction(MYSQL* conn);
		void SupprimerExpedition(MYSQL* conn);
		void SupprimerTransporteur(MYSQL* conn);
		void SupprimerClient(MYSQL* conn);
		
		void ModifierLivraison(MYSQL* conn);
		void ModifierDetLiv(MYSQL* conn);
		void ModifierTransaction(MYSQL* conn);
		void ModifierExpedition(MYSQL* conn);
		void ModifierTransporteur(MYSQL* conn);
		void ModifierClient(MYSQL* conn);
		
		void ListerLivraison(MYSQL* conn);
		void ListerDetailliv(MYSQL* conn);
		void ListerTransaction(MYSQL* conn);
		void ListerExpedition(MYSQL* conn);
		void ListerTransporteur(MYSQL* conn);
		void ListerClient(MYSQL* conn);
		
	private:
		MYSQL *conn;
};

#endif
