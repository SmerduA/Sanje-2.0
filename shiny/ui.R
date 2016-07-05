library(shiny)

shinyUI(fluidPage(
  titlePanel("Plezališča"),
  
  tabsetPanel(
    
  #############################
    
  tabPanel( "Plezališča po državah",
    sidebarLayout(
    sidebarPanel(
      selectInput("izberi_drzavo",
                  label = "Izberi državo:",
                  choices = list("vse države", "Avstrija","Bosna in Hercegovina","Češka","Črna gora","Grčija","Hrvaška", "Juzna Afrika", "Maroko", "Nemčija", "Poljska", "Slovaška", "Slovenija","Španija", "Srbija", "Švedska", "Švica", "Tajska", "Turčija" ,"Združene države Amerike"),
                  selected="vse države"
    ),
    sliderInput("stevilo_smeri",
                label= "Število smeri v plezališču:",
                min= 1,
                max =706,
                value=c(1, 706)
      
    )
    ),
    
    mainPanel(
  tableOutput("plezaliscaPoDrzavah")
))),
##############################
tabPanel( "Države",
          sidebarLayout(
            sidebarPanel(
              sliderInput("st_plezalisc",
                          label = "Število plezališč:",
                          min = 1,
                          max = 103,
                          value = c(0,103)
              )),
            
            mainPanel(
              tableOutput("drzavestevilo")
            ))),

##############################
tabPanel( "neki",
          sidebarLayout(
            sidebarPanel(
              sliderInput("st_plezalisc",
                          label = "Število plezališč:",
                          min = 1,
                          max = 103,
                          value = c(0,103)
              )
              
              ),
            
            mainPanel(
              tableOutput("plezaliscastevilo")
            )))



  )))