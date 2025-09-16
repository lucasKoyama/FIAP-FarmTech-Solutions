# importar dados
dados <- read.csv("dados.csv", stringsAsFactors = FALSE)

# mostrar primeiras linhas
head(dados)

# médias
media_comprimento <- mean(dados$comprimento)
media_largura     <- mean(dados$largura)
media_area        <- mean(dados$area)
media_insumo      <- mean(dados$insumo)

# desvios padrão
desvio_comprimento <- sd(dados$comprimento)
desvio_largura     <- sd(dados$largura)
desvio_area        <- sd(dados$area)
desvio_insumo      <- sd(dados$insumo)

# imprimir resultados
cat("📊 Estatísticas básicas:\n")
cat("Média comprimento:", media_comprimento, "\n")
cat("Média largura:", media_largura, "\n")Q
cat("Média área:", media_area, "\n")
cat("Média insumo:", media_insumo, "\n\n")

cat("Desvio padrão comprimento:", desvio_comprimento, "\n")
cat("Desvio padrão largura:", desvio_largura, "\n")
cat("Desvio padrão área:", desvio_area, "\n")
cat("Desvio padrão insumo:", desvio_insumo, "\n")
