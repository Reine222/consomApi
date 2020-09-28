# consomApi
 consommation API
 
 # consommation graphql et api rest
 
  
    ############## API REST ##############
    <script>
     var ma_vue = new Vue({
       el: '#identifiant_id',
       data: { 
         resultats_chef: {'succes': false,'reponse':'' },
         resultats_plat_cat: [],
       },
       delimiters: ["${", "}"],
       mounted () {
         this.getchef()
         this.getplatcat()
       },
       methods: {
         getchef: function () {
           //axios.defaults.xsrfCookieName = 'csrftoken'
           //axios.defaults.xsrfHeaderName = 'X-CSRFToken'
           axios.get('http://127.0.0.1:8000/testimony/').then(response => {
             console.log(response)
             this.resultats_chef= response.data  
           })
           .catch((err) => {
             console.log(err)
             this.result['reponse'] = "Probleme de connexion , veuillez contactez l'administrateur"
             this.result['succes'] = false
           })
         },

         getplatcat: function () {
           //axios.defaults.xsrfCookieName = 'csrftoken'
           //axios.defaults.xsrfHeaderName = 'X-CSRFToken'
           axios.get('http://127.0.0.1:8000/categorie/').then(response => {
             console.log(response)
             this.resultats_plat_cat= response.data  
           })
           .catch((err) => {
             console.log(err)
             this.result['reponse'] = "Probleme de connexion , veuillez contactez l'administrateur"
             this.result['succes'] = false
           })
         }

       }
     })
    </script>
    
    ############## GRAPHQL ##############

    <script>
      var ma_vue2 = new Vue({
        el: '#graph_service',
        data: { 
          resultats_services: {},
          base_url: window.location.protocol + "//" + window.location.host + '/',
        },
        delimiters: ["${", "}"],
        mounted () {
          this.getservices()
        },
        methods: {
          getservices: function () {
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            axios({
              url : 'http://127.0.0.1:8000/graphql',
              methode : 'post',
              data : {
                query: `
                  query{
                    allServices{
                      edges{
                        node{
                          id
                          titre
                          icon
                          description
                          status
                        }
                      }
                    }
                  }
                `
              }
            }).then(response => {
              resultats = response.data.data;  
              console.log(resultats);
              //this.resultats_services = resultats.allServices;
            })
            .catch((err) => {
              console.log(err)
            })
          },
        }
      })
    </script>
 
 
# Django session
    https://www.geeksforgeeks.org/python-sessions-framework-using-django/?ref=rp


# Utilisation Echarts js
    import Chart from "chart.js";

    export function homeSetup(): void {
    ...

    initGraph();
    }

    ...

    function initGraph() {
    const ctx = document.getElementById("myChart");

    if (!ctx) {
        return;
    }

    const data = {
        datasets: [
        {
            backgroundColor: [
            "rgb(255, 99, 132)",
            "rgb(54, 162, 235)",
            "rgb(255, 206, 86)",
            ],
            borderColor: ["rgb(255, 255, 255)"],
            data: [10, 20, 30],
        },
        ],
        labels: ["Rouge", "Bleu", "Jaune"],
    };

    const graph = new Chart(ctx, {
        data,
        type: "polarArea",
    });
    }

    #########################   #################################

    % extends "base.html" %} {% block banner %}

    <h1>Hello Webpack !</h1>

    {% endblock %} {% block content %} {% lorem 5 %}

    <canvas id="myChart" width="400" height="400"></canvas>

    {% endblock %}


# grappelli django
    https://django-grappelli.readthedocs.io/en/latest/quickstart.html#installation

# Tuto sur la librairie Request
    https://www.pythonclassmates.org/category/tutoriels.html

# Le top 10 des erreurs des dev django
    https://www.toptal.com/django/django-top-10-mistakes

# admin personnalisé
    https://github.com/django-fluent/django-fluent-dashboard

    https://django-baton.readthedocs.io/en/latest/configuration.html
