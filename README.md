# consomApi
 consommation API
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