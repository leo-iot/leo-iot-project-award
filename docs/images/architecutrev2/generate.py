from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
from diagrams.programming.framework import Angular

with Diagram(show=False, direction='LR'):
    with Cluster("LEO-IOT-Server"):
        leo_backend = Custom("Backend", "quarkus-logo.jpg")

        leo_frontend = Angular("Frontend")




        graphana = Custom("Graphana", "grafana_logo.png")
        leo_frontend <<  graphana
        leo_frontend >>  leo_backend
        timescale = Custom("Database", "timescale_logo.png")
        leo_backend >> timescale


    with Cluster("Value-Sim"):
        leo_sim = Custom("Value Simulator", "quarkus-logo.jpg")
        postgres = Custom("Database", "postgres_logo.png")
        leo_sim >> postgres

    with Cluster("Mqtt-Server"):
        mosquitto = Custom("Mqtt-Broker", "mosquitto_logo.png")

    with Cluster("5AHIF"):
        leobox1 = Custom("LeoBox", "leobox.png")

    with Cluster("4BHITM"):
        leobox2 = Custom("LeoBox", "leobox.png")

    leobox1 >>  mosquitto
    leobox2 >>  mosquitto

    mosquitto >>  leo_frontend
    mosquitto >>  leo_backend

    leo_sim >>  mosquitto

    graphana << timescale


