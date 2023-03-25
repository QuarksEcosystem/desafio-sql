 
SELECT
    CONCAT(YEAR(CONVERT(DATE, [Data da Venda], 103)), '-Q', 
    DATEPART(QUARTER, CONVERT(DATE, [Data da Venda], 103))) AS Trimestre,
    SUM(CAST(REPLACE(REPLACE(REPLACE([Valor], '.', ''), ',', '.'), 'R$', '') AS MONEY)) AS Total_Vendas
INTO 
    tabela_trimestral_vendas
FROM 
    Desafio.dbo.dadosdesafio
GROUP BY 
    CONCAT(YEAR(CONVERT(DATE, [Data da Venda], 103)), '-Q', 
    DATEPART(QUARTER, CONVERT(DATE, [Data da Venda], 103)))
ORDER BY 
    Trimestre;