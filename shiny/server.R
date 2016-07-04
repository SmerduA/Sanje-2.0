library(shiny)
library(dplyr)
library(RPostgreSQL)
library(datasets)


source("../auth_public.R")

shinyServer(function(input, output) {
  # Vzpostavimo povezavo
  conn <- src_postgres(dbname = db, host = host,
                       user = user, password = password)
  tbl.plezalisca <- tbl(conn, "plezalisca")
  output$plezalisca <- renderTable({
    
    t <- tbl.plezalisca
    t
  })
  })