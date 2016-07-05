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
  tbl.plezaliscastevilo <- tbl(conn, sql("SELECT nekoime.plezalisce, drzava, stevilo FROM nekoime JOIN plezalisca ON nekoime.plezalisce=plezalisca.plezalisce ORDER BY drzava, plezalisce"))
  tbl.drzave <- tbl(conn, "drzave")
  tbl.smeri <- tbl(conn, "smeri")
  tbl.drzavestevilo <-tbl(conn, sql("SELECT drzava, count(*) AS stevilo_plezalisc FROM plezalisca GROUP BY drzava ORDER BY stevilo_plezalisc DESC"))
  
  ############################
  
  output$plezaliscaPoDrzavah <- renderTable({
    
    t <- tbl.plezaliscastevilo %>% if(input$izberi_drzavo=="vse države") filter(input$stevilo_smeri[1]<= stevilo & stevilo <= input$stevilo_smeri[2]) else filter(drzava==input$izberi_drzavo & input$stevilo_smeri[1]<= stevilo & stevilo <= input$stevilo_smeri[2]) %>% data.frame()
    t
  })
  
  ##################
  output$drzavestevilo <- renderTable({drz <- tbl.drzavestevilo %>% filter(input$st_plezalisc[1] <= stevilo_plezalisc & stevilo_plezalisc<= input$st_plezalisc[2]) %>% data.frame()
                            drz})
  
  #######################
  
  output$plezaliscastevilo <- renderTable({ps <- tbl.plezaliscastevilo %>% data.frame()
  ps
    
    
  })
  
  
  
  
  
  })

