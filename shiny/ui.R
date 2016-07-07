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
tabPanel( "države glede na število plezališč",
          sidebarLayout(
            sidebarPanel(
              selectInput("nacinprikaza",
                          label = "Izberi način prikaza:",
                          choices=list("histogram", "tortni diagram")
              )
              
              ),
            
            mainPanel(
              plotOutput("drzavetorta")
            ))),
##############################

tabPanel( "Poišči plezališče po meri",
          sidebarLayout(
            sidebarPanel(
              selectInput("ppdrzava", label="Izberi državo:",
                          choices = list("vse države", "Avstrija","Bosna in Hercegovina","Češka","Črna gora","Grčija","Hrvaška", "Juzna Afrika", "Maroko", "Nemčija", "Poljska", "Slovaška", "Slovenija","Španija", "Srbija", "Švedska", "Švica", "Tajska", "Turčija" ,"Združene države Amerike"),
                          selected = "vse države"),
              # #selectInput()
              #

              numericInput("mindolzina",
                          label="Izberi minimalno dolžino smeri",
                          value = 0,
                          min= 0,
                          max = 680
              ),
              numericInput("maxdolzina",
                           label="Izberi maksimalno dolžino smeri",
                           value = 680,
                           min= 0,
                           max = 680
              ),
              numericInput("maxtezavnost",
                           label="Izberi maksimalno težavnost smeri",
                           value = 6,
                           min= 1,
                           max = 9
              ),
              numericInput("mintezavnost",
                           label="Izberi minimalno težavnost smeri",
                           value = 1,
                           min= 1,
                           max = 9
              )
            #   sliderInput("ppdolžina",
            #               label="Izberi dolžino smeri",
            #               min= 0,
            #               max = 680,
            #               value=c(0, 680)
            #   ),
            # sliderInput("ppsmeri",
            #             label = "Izberi število smeri z določeno dolžino in težavnostjo",
            #             min= 1,
            #             max =706,
            #             value=c(1, 706)
           ),
             mainPanel( tableOutput("ppplezalisca")
               
             )))

  )))