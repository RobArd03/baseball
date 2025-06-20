from database.DB_connect import DBConnect
from model.teams import Team


class DAO():

    @staticmethod
    def getAllNodes(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT *
                    FROM teams t
                    WHERE t.year = %s
                    """
        cursor.execute(query,(year, ))

        for row in cursor:
            result.append(Team(**row))


        cursor.close()
        conn.close()
        return result

    @staticmethod
    def setPesi(year, idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT t.ID, SUM(s.salary) as peso
                    FROM teams t, salaries s
                    WHERE t.year = s.year 
                    AND t.year = %s
                    AND t.ID = s.teamID
                    GROUP BY t.ID
                """
        cursor.execute(query, (year,))

        for row in cursor:
            idMap[ row[ 'ID' ] ].setPeso( row[ 'peso' ] )

        cursor.close()
        conn.close()

