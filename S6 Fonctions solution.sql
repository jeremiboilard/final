/*
1. Écrire une fonction qui prend en paramètre le prix à l'unité, la quantité et le rabais et qui retourne le montant total
   Utiliser cette fonction dans une requête qui affiche le montant total des ventes de chaque produit pour chaque année
*/
GO
CREATE OR ALTER FUNCTION GetMontantTotal(@Prix money, @Qte smallint, @Rabais real)
RETURNS money
AS
BEGIN
    RETURN (@Qte * @Prix)*(1-@Rabais);
END;
GO

SELECT DATEPART(year,OrderDate) as 'Année', ProductID, FORMAT(SUM(dbo.GetMontantTotal(UnitPrice, Quantity, Discount)), 'C', 'fr-CA') AS 'Total'
FROM Orders INNER JOIN [Order Details] ON Orders.OrderID = [Order Details].OrderID
GROUP BY DATEPART(year,OrderDate), ProductID
ORDER BY Année

/*
 2. Écrire une fonction qui prend en paramètre un numéro de téléphone au format '8195555555' et qui le retourne au format
    '(819) 555-5555'. Démontrer l'utilisation de la fonction à l'aide d'une requête de type SELECT FonctionTel('8195555555');
*/
GO
CREATE OR ALTER FUNCTION GetTelFormat(@Tel varchar(10))
RETURNS varchar(14)
AS

BEGIN
    RETURN CONCAT('(', substring(@Tel, 1, 3), ') ', substring(@Tel, 4, 3), '-', substring(@Tel, 7, 4));
END;
GO

-- Appel
SELECT dbo.GetTelFormat('8195555555')


/*
3. Écrire une fonction qui prend en paramètre un pays et qui retourne tous les Clients de ce pays. (Le type de retour sera table)
   Démontrer l'utilisation de la fonction.
*/
GO
CREATE OR ALTER FUNCTION GetClients(@Pays nvarchar(15))
RETURNS @clients TABLE (	
	CustomerID nchar(5) NOT NULL,
	CompanyName nvarchar(40) NOT NULL,
	ContactTitle nvarchar(30) NULL,
	Address nvarchar(60) NULL,
	City nvarchar(15) NULL,
	Region nvarchar(15) NULL,
	PostalCode nvarchar(10) NULL,
	Country nvarchar(15) NULL,
	Phone nvarchar(24) NULL,
	Fax nvarchar(24) NULL,
	ContactID int NULL)
AS
BEGIN;
    INSERT INTO @clients
    SELECT * FROM Customers WHERE Country LIKE @Pays
    RETURN;
END;
GO
SELECT * FROM GetClients('Canada');

/*
4. Écrire une fonction qui prend en paramètre un numéro de produit et qui retourne la valeur en stock (quantité en stock * unit price)
*/

GO
CREATE OR ALTER FUNCTION GetStock(@ProductID int)
RETURNS money
AS
BEGIN
    RETURN (SELECT UnitsInStock*UnitPrice FROM Products WHERE ProductID = @ProductID);
END;
GO

SELECT dbo.GetStock(1)

/*
5. Écrire une fonction qui prend 1 bit en paramètre. Si le paramètre est 1, retourner tous les produits discontinués, sinon retourner tous les
   produits que ne sont pas discontinués.
*/

GO
CREATE OR ALTER FUNCTION GetProducts(@Discontinued bit)
RETURNS @Products TABLE (
	ProductID int NOT NULL,
	ProductName nvarchar(40) NOT NULL,
	SupplierID int NULL,
	CategoryID int NULL,
	QuantityPerUnit nvarchar(20) NULL,
	UnitPrice money NULL,
	UnitsInStock smallint NULL,
	UnitsOnOrder smallint NULL,
	ReorderLevel smallint NULL,
	Discontinued bit NOT NULL
	)
AS
BEGIN
	INSERT INTO @Products
    SELECT * FROM Products WHERE Discontinued =  @Discontinued
    RETURN;
END;
GO

SELECT * FROM dbo.GetProducts(0);
SELECT * FROM dbo.GetProducts(1);