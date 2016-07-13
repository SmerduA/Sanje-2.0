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
    t <- tbl.plezaliscastevilo
    if(input$izberi_drzavo != "vse države") {
      t <- t %>% filter(drzava==input$izberi_drzavo)
    }
    t <- t %>% filter(input$stevilo_smeri[1] <= stevilo,
                      stevilo <= input$stevilo_smeri[2]) %>% data.frame()
    validate(need(nrow(t) > 0, "Nobeno plezališče ne ustreza pogojem!"))
    Encoding(t$drzava) <- "UTF-8"
    Encoding(t$plezalisce) <- "UTF-8"
    colnames(t) <-c("Plezališče", "Država", "Število smeri")
    t
  })
  
  ##################
  output$drzavestevilo <- renderTable({drz <- tbl.drzavestevilo %>% filter(input$st_plezalisc[1] <= stevilo_plezalisc & stevilo_plezalisc<= input$st_plezalisc[2]) %>% data.frame()
    validate(need(nrow(drz) > 0, "Nobena država ne ustreza pogojem!"))      
    Encoding(drz$drzava) <-"UTF-8"  
    colnames(drz) <- c("Država","Število plezališč")
        drz})
  
  #######################
  
  output$drzavetorta <- renderPlot({ps <- tbl.drzavestevilo %>% data.frame()
  if(input$nacinprikaza == "histogram") hist(ps$stevilo_plezalisc, main= "Drzave po številu plezališč", xlab="število plezališč", ylab="število držav", breaks = 20)
  else
  pie(ps$stevilo_plezalisc, main="Drzave po številu plezališč")
    
    
  })
  
  ######################
  
  output$ppplezalisca <- renderTable({
    
    stavek <- paste("SELECT plezalisca.plezalisce, plezalisca.drzava, count(*) AS stevilo_smeri FROM smeri JOIN plezalisca ON smeri.plezalisce = plezalisca.plezalisce 
                    WHERE tezavnost <= text(", toString(input$maxtezavnost),") AND tezavnost>= text(", toString(input$mintezavnost), ") AND dolzina <= ", toString(input$maxdolzina), "AND dolzina >=", toString(input$mindolzina),
                    "GROUP BY plezalisca.plezalisce ORDER BY stevilo_smeri DESC", sep=" ")
    tbl.pomeri <- tbl(conn, sql(stavek))
    pomeri <- tbl.pomeri
    if(input$ppdrzava != "vse države") {
      pomeri <- pomeri %>% filter(drzava == input$ppdrzava)
    }
    
    pomeri <- pomeri %>% data.frame
    validate(need(nrow(pomeri) > 0, "Nobeno plezališče ne ustreza pogojem!"))
    Encoding(pomeri$plezalisce) <-"UTF-8"
    Encoding(pomeri$drzava) <- "UTF-8"
    colnames(pomeri) <- c("Plezališče","Država", "Število smeri, ki ustrezajo pogojem")
    pomeri
    
  })
  
  ######################################
  
  output$grafi <- renderPlot({
    tbl.smeridrzave <- tbl(conn, sql("SELECT ime, dolzina, tezavnost, plezalisca.drzava FROM smeri NATURAL JOIN plezalisca WHERE tezavnost NOT IN ('?', 'P', 'A', 'I', 'V') "))
    if(input$ddrzava != "vse države"){
      tbl.smeridrzave <-tbl.smeridrzave %>% filter(drzava == input$ddrzava)
    }
    smeridrzave <- tbl.smeridrzave %>% data.frame()
    
#    h1 <- hist(smeridrzave$dolzina, main="Histogram dolžin",breaks = 100)
#    h2 <- hist(smeridrzave$dolzina,main="Histogram težavnosti", breaks = 100)
    if(input$ddoltez == "dolžina smeri") {
      h <-hist(smeridrzave$dolzina, main="Histogram dolžin",xlab= "dolžina smeri", ylab="število",breaks = 100)
    }
    
    if(input$ddoltez == "težavnost smeri") {
    h <-hist(as.numeric(smeridrzave$tezavnost),main="Histogram težavnosti", xlab= "težavnost smeri", ylab="število", breaks = 100)
      }
    
    
    h  
  })
  
  
  
  })

