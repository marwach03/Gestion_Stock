#ifndef GESTION_STOCK_H
#define GESTION_STOCK_H

#include <iostream>
#include <mysql.h>
#include <string>
#include <sstream>
#include <conio.h>

class Gestion_stock
{
	public:
		Gestion_stock();
		~Gestion_stock();
		
		void InsererUtilisateur(MYSQL *conn);
		void InsererRole(MYSQL *conn);
		void InsererHistorique(MYSQL *conn);
		void InsererAlerte(MYSQL *conn);
		void InsererParametre(MYSQL *conn);
		
		void SupprimerUtilisateur(MYSQL *conn);
		void SupprimerRole(MYSQL *conn);
		void SupprimerHistorique(MYSQL *conn);
		void SupprimerAlerte(MYSQL *conn);
		void SupprimerParametre(MYSQL *conn);
		
		void ModifierUtilisateur(MYSQL *conn);
		void ModifierRole(MYSQL *conn);
		void ModifierHistorique(MYSQL *conn);
		void ModifierAlerte(MYSQL *conn);
		void ModifierParametre(MYSQL *conn);
		
		void ListerUtilisateur(MYSQL *conn);
		void ListerRole(MYSQL *conn);
		void ListerHistorique(MYSQL *conn);
		void ListerAlerte(MYSQL *conn);
		void ListerParametre(MYSQL *conn);
	private:
		MYSQL *conn;
};

#endif
