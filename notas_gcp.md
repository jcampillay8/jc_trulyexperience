# Creando el dataframe
df = pd.DataFrame({
    "Opción": ["VPC Endpoints", "Cloud NAT", "Shared VPC", "Private Google Access"],
    "Enfoque": ["Conexión segura a servicios de Google", "Traducción de direcciones IP para VMs", "Compartir una VPC entre proyectos", "Acceso privado a APIs y servicios públicos de Google"],
    "Recomendaciones": ["Utilizar para servicios sensibles", "Utilizar para VMs con IPs públicas", "Utilizar para centralizar la gestión de redes", "Utilizar para VMs sin IP pública que necesiten acceder a recursos públicos de Google"],
    "Mejor para": ["Aplicaciones que requieren alta seguridad y confiabilidad", "VMs que necesitan acceder a internet", "Organizaciones con múltiples proyectos", "VMs que necesitan acceder a BigQuery, Cloud Storage y otros servicios públicos sin tener una IP pública"],
    "Categoría": ["Servicio", "Servicio", "Función", "Función"]
})

# Mostrando el dataframe
print(df.to_string())



# Creando el dataframe
df = pd.DataFrame({
    "Opción": ["App Engine Standard Environment", "App Engine Flexible Environment", "Google Kubernetes Engine (GKE)", "Cloud Run for Anthos"],
    "Enfoque": ["Entorno preconfigurado, sin servidores", "Entorno personalizable con contenedores", "Orquestación de contenedores a nivel empresarial", "Ejecución de contenedores en entornos híbridos y multicloud"],
    "Ventajas": ["Fácil de usar, escalabilidad automática, precios sin servidor", "Mayor control de recursos, libertad de elección de runtime", "Alta disponibilidad, escalabilidad horizontal, seguridad", "Ejecución en clusters privados, híbridos o multicloud"],
    "Desventajas": ["Menor control, disponibilidad limitada de lenguajes y runtimes", "Mayor complejidad de gestión, requiere conocimientos de Docker", "Costo mayor, requiere gestión de clusters", "Limitaciones de despliegue, dependencia de infraestructura externa"],
    "Mejor para": ["Aplicaciones sin estado, desarrollos rápidos, microservicios", "Aplicaciones complejas, necesidad de runtimes específicos", "Grandes cargas de trabajo, alta disponibilidad crítica", "Ejecución de aplicaciones en entornos diversos"],
    "Categoría": ["PaaS", "PaaS", "Managed Kubernetes", "Serverless Kubernetes"]
})

# Mostrando el dataframe
print(df.to_string())

# Creando el dataframe
df = pd.DataFrame({
    "Opción": ["Pay-as-you-go", "SLOs", "Incident Contracts", "SLA"],
    "Enfoque": ["Modelo de pago por uso", "Objetivos de nivel de servicio", "Contratos de incidentes", "Acuerdos de nivel de servicio"],
    "Recomendaciones": ["Utilizar para cargas de trabajo variables", "Establecer para servicios críticos", "Utilizar para servicios sensibles al tiempo", "Utilizar para relaciones con proveedores"],
    "Mejor para": ["Pruebas, desarrollos, uso esporádico", "Monitoreo de rendimiento", "Respuesta rápida a incidentes", "Garantías de servicio"],
    "Categoría": ["Modelo de pago", "Medición de rendimiento", "Respuesta a incidentes", "Contrato formal"]
})

# Mostrando el dataframe
print(df.to_string())


# Creando el dataframe
df = pd.DataFrame({
    "Opción": ["Anthos", "Google Kubernetes Engine (GKE)", "App Engine", "Cloud Functions"],
    "Enfoque": ["Plataforma de gestión de aplicaciones multicloud", "Orquestación de contenedores a nivel empresarial", "Plataforma de desarrollo y alojamiento sin servidor", "Ejecución de código sin estado en eventos"],
    "Recomendaciones": ["Utilizar para centralizar la gestión de aplicaciones en múltiples nubes", "Utilizar para ejecutar aplicaciones a gran escala con alta disponibilidad", "Utilizar para desarrollar y escalar aplicaciones web sin servidores", "Utilizar para ejecutar código sin estado en respuesta a eventos"],
    "Mejor para": ["Organizaciones con entornos multicloud", "Desarrolladores que necesitan un entorno escalable y seguro", "Desarrollos rápidos, microservicios", "Procesamiento de eventos, tareas de corta duración"],
    "Categoría": ["Plataforma de gestión", "Orquestación de contenedores", "Plataforma sin servidor", "Plataforma sin servidor"]
})

# Mostrando el dataframe
print(df.to_string())


# Creando el dataframe
df = pd.DataFrame({
    "Opción": ["Firebase", "Cloud Functions", "App Engine", "Plantillas de Instancias"],
    "Enfoque": ["Plataforma de desarrollo móvil y web sin servidor", "Ejecución de código sin estado en eventos", "Plataforma de desarrollo y alojamiento sin servidor", "Automatización de la creación de VMs"],
    "Recomendaciones": ["Utilizar para desarrollar aplicaciones móviles y web escalables", "Utilizar para ejecutar código en respuesta a eventos sin necesidad de servidores", "Utilizar para desarrollar y escalar aplicaciones web sin servidores", "Utilizar para crear VMs con configuraciones predefinidas"],
    "Mejor para": ["Desarrolladores móviles y web", "Procesamiento de eventos, tareas de corta duración", "Desarrollos rápidos, microservicios", "Agilidad y eficiencia en la creación de VMs"],
    "Categoría": ["Plataforma sin servidor", "Plataforma sin servidor", "Plataforma sin servidor", "Herramienta de automatización"]
})

# Mostrando el dataframe
print(df.to_string())


# Creando el dataframe
df = pd.DataFrame({
    "Opción": ["Google App Engine", "Compute Engine", "Cloud Functions", "Google Kubernetes Engine (GKE)"],
    "Enfoque": ["Plataforma de desarrollo y alojamiento sin servidor", "Máquinas virtuales escalables", "Ejecución de código sin estado en eventos", "Orquestación de contenedores a nivel empresarial"],
    "Recomendaciones": ["Utilizar para desarrollar y escalar aplicaciones web sin servidores", "Utilizar para ejecutar aplicaciones con necesidades específicas de recursos", "Utilizar para ejecutar código en respuesta a eventos sin necesidad de servidores", "Utilizar para ejecutar aplicaciones a gran escala con alta disponibilidad"],
    "Mejor para": ["Desarrollos rápidos, microservicios", "Aplicaciones con alto rendimiento o necesidades específicas", "Procesamiento de eventos, tareas de corta duración", "Desarrolladores que necesitan un entorno escalable y seguro"],
    "Categoría": ["Plataforma sin servidor", "Infraestructura como servicio", "Plataforma sin servidor", "Orquestación de contenedores"]
})

# Mostrando el dataframe
print(df.to_string())



# REVISAR (304, 188, 139, 261)


Organiztions are building applications on Gogole cloud. The application manges critiacl customer data and needs to prevent dat breaches and non--compliance. How should you respond?

To prevent application data breaches and non compliance uste the Security Command Center to imopelemnent a mechanism to asses misconfigurations and vulnerabilities security command center is asecurity andrisk mangaeement platform for Google cloud.. It identifies misconfiguraiton and complinace violations that compromise the seciurtiy of your Google cloud assets and provides acctionable recommenddtios 


Organiztions want to perform analytics on Googlee cloud on hundreds of gigabytes of data every day, while maintaining compute workloasds in their on-premises envirfonment. How do you configure your netweork to accompolish this?

In this scenario, you need to work with onñ-prjeises workloads to perform analysis on Google cloud that generates dundres od gigabytes of data each day. Fast, secure network connections are required to coordineate data processing between platforms. Tnhere foe, Google cloud reuquirews you to set up da dedicated interconnect between the two dat centers to estabils h a fast aand reliable connection . Dedicates inteconcect is a swerice that providesleased line conncecitons and is ideal for secure high-speed adata movements

The organiztion migrates applications from iuts on-premises environment to Google Cloud to respond quickly to business demands. In doing so, you want ot dinamically adjust the application according to user needs. What are the benerfits of storing data in GoogCloud?



# Conncect

- VPC
- Cloud DNS
- Cloud VPN
- Cloud Router
- Dedicated Interconnect
- Partner Interconnect

# Secure

- Cloud Armor
- Firewall
- Packet
- Cloud IAP
- Cloud NAT

# Scale

- Cloud Load Balancer
- Cloud CDN

# Optimize

- Premium Tier
- Standar Tier
- Network Intelligence Center 

# Modernize

- GKE Network (+O On-Prem)(In Anthos)
- Traffic Director (In Anthos)

  



Google Cloud Platform Icons

# Compute

- Compute Engine
- App Engine
- Container Engine
- Container Registry
- Cloud Functions

# Identity & Security

- Cloud IAM
- Cloud Resource Manager
- Cloud Security Scanner
- Cloud Platform Security

# Networking

- Cloud Virtual Network
- Cloud Load Balancing
- Cloud CDN
- Cloud Interconnect
- Cloud DNS

# Big Data

- BigQuery
- Cloud Dataflow
- Cloud Dataproc
- Cloud Datalab
- Cloud Pub/Sub
- Genomics

# Storage and Databases

- Cloud Storage
- Cloud Bigtable
- Cloud Datastore
- Cloud SQL
- Persistent Disk


# Machine Learning

- Cloud Machine Learning
- Vision API
- Speech API
- Natural Language API
- Translation API
- Jobs API

# Management Tools

- Stackdriver
- Monitoring
- Logging
- Error Reporting
- Trace
- Debugger
- Deployment Manager
- Cloud Console
- Cloud Endpoints
- Cloud Shell
- Cloud Mobile App
- Billing App
- Cloud APIs

# Developer Tools

- Cloud SDK
- Deployment Manager
- Cloud Source Repositories
- Cloud Tools for Android Studio
- Cloud Tools for IntelliJ
- Cloud Tools for PowerShell
- Cloud Tools for Visual Studio
- Google Plug-in for Eclipse
- Cloud Test Lab

