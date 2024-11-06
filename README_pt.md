
---

### README português

# Projeto de Monitoramento IoT

## Resumo


O Projeto de Monitoramento IoT foi idealizado para proporcionar um sistema robusto de monitoramento ambiental em tempo real, utilizando tecnologias de sensores e integração com plataformas de nuvem. O sistema é composto por um dispositivo ESP32, que coleta dados de temperatura e umidade por meio de um sensor DHT11 e dados de luminosidade através de um fotoresistor. Os dados são transmitidos via Wi-Fi para o sistema FIWARE, que os processa e armazena no MongoDB, localizado em uma instância de máquina virtual na plataforma Azure, configurada via Docker.

O ESP32, antes de enviar os dados ao banco de dados, utiliza um algoritmo para calcular a média das leituras feitas ao longo de um minuto, otimizando o uso de armazenamento e garantindo uma melhor qualidade dos dados. Além disso, a aplicação oferece uma interface interativa acessível de qualquer local com conexão à internet, permitindo o monitoramento contínuo do ambiente monitorado.

Este projeto ainda conta com um simulador virtual, desenvolvido através da plataforma Wokwi, que emula o comportamento do dispositivo ESP32 e seus sensores. O link para o simulador está disponível em: Wokwi IoT Project. Além disso, um script Python (api-sth.py) simula um servidor local simples para visualizar os dados em tempo real diretamente no navegador.

Com um foco em precisão e eficiência, o projeto visa ser uma solução escalável para monitoramento de dados ambientais em diversos contextos, como áreas de estudo, ambientes controlados e sistemas de gestão inteligente de recursos.

Este documento fornece uma visão geral completa da arquitetura, funcionalidades e tecnologias do sistema, sendo um guia valioso para desenvolvedores e pesquisadores interessados em sistemas de monitoramento IoT.

## Introdução

A Internet das Coisas (IoT) tem se consolidado como uma das tecnologias mais inovadoras e promissoras nos últimos anos, facilitando a coleta, análise e visualização de dados em tempo real. No contexto ambiental, esse tipo de solução oferece uma maneira eficiente de monitorar condições como temperatura, umidade e luminosidade, sendo fundamental para a automação e otimização de processos em vários setores.

Este projeto foi desenvolvido com o objetivo de fornecer uma plataforma de monitoramento inteligente que permita a coleta de dados ambientais com alto nível de precisão, a visualização desses dados em tempo real, e a geração de alertas baseados em condições críticas. A integração com tecnologias como FIWARE e MongoDB permite que a solução seja escalável e altamente eficiente, além de garantir que os dados sejam armazenados de forma segura e acessível.

## Objetivos

Aquisição de Dados: Implantar um sistema sem interrupções para coleta de dados dos sensores IoT, garantindo a precisão das medições.
Visualização de Dados: Desenvolver uma interface de visualização intuitiva, permitindo aos usuários acessarem e monitorarem os dados em tempo real.
Sistema de Alertas: Implementar um sistema de notificação para alertar os usuários sobre condições anormais ou críticas, com base nos limites pré-estabelecidos.
Eficiência no Armazenamento: Desenvolver um mecanismo para otimização de armazenamento de dados, utilizando a média de leituras ao longo de um intervalo de tempo.

## Funcionalidades

1. **Dashboard em Tempo Real**
O dashboard exibe dados atualizados em tempo real de sensores de temperatura, umidade e luminosidade.
Os dados são apresentados de forma interativa através de gráficos dinâmicos, possibilitando fácil interpretação e análise.
2. **Sistema de Alerta**
A aplicação monitora os dados coletados e emite alertas caso valores fora dos limites esperados sejam detectados.
Um sistema de alerta visual é ativado no dashboard e o ESP32 pode acionar um indicador luminoso externo para alertar sobre condições anormais.
3. **Armazenamento de Dados**
Utiliza MongoDB para o armazenamento de dados históricos, permitindo que os usuários consultem informações passadas e analisem tendências ao longo do tempo.
O armazenamento é otimizado, enviando dados para o banco apenas após o cálculo da média das leituras, o que reduz o volume de dados e melhora a performance.
4. **Integração com API RESTful**
A aplicação se comunica com a plataforma FIWARE, que garante a integração entre os dispositivos IoT e o servidor backend, facilitando a troca de dados e a comunicação eficiente.

## Tecnologias Utilizadas

**ASP.NET Core 6.0**: Framework de desenvolvimento multiplataforma que permite criar aplicações robustas, rápidas e escaláveis, sendo utilizado tanto para o backend quanto para a construção do dashboard.

**MongoDB**: Banco de dados NoSQL que armazena os dados dos sensores, possibilitando a análise e visualização eficientes dos dados ao longo do tempo.
Máquina Virtual Azure: Infraestrutura em nuvem que hospeda o MongoDB, garantindo escalabilidade e alta disponibilidade do sistema.

**ESP32**: Microcontrolador com conectividade Wi-Fi e Bluetooth, utilizado para coletar dados dos sensores e enviar as informações para a plataforma FIWARE.

**Sensor DHT11**: Sensor digital de temperatura e umidade, utilizado para medir condições ambientais com alta precisão.

**Fotoresistor (LDR)**: Componente eletrônico utilizado para medir a intensidade luminosa no ambiente.


## Visão Geral da Arquitetura

A arquitetura do sistema é projetada para ser escalável e modular. A seguir, detalhamos os principais componentes do sistema:

**Frontend**: Desenvolvido utilizando ASP.NET Core MVC, a interface gráfica interativa permite que os usuários monitorem os dados em tempo real, visualizem gráficos e recebam alertas.

**Backend**: Responsável por toda a lógica de negócios, incluindo a coleta de dados dos sensores, o processamento dos dados e o gerenciamento de alertas. A comunicação com a API Fiware permite que o sistema seja eficiente na troca de informações com os dispositivos IoT.

**Banco de Dados**: O MongoDB armazena os dados coletados, permitindo consultas e relatórios detalhados sobre os parâmetros monitorados ao longo do tempo.


## Instalação e Configuração
Para rodar o projeto localmente, é necessário se atentar para algumas orientações:

    
+ Para abrir a implementação com ASP NET CORE 6.0 localmente é necessário que tenha instalado em sua máquina o Visual Studio (recomendado a versão 22);

+ As orientações para criar uma VM com o mongoDB alocado por uma imagem em docker estão no repositório do professor Doutor [Fabio Cabrini](https://github.com/fabiocabrini/fiware).

+ Caso queira utilizar o servidor de teste em python para servir um servidor local com a amostragem dos dados brutos pode utilizar o arquivo "api-sth.py" no VS Code e instalando suas dependências. Não se esqueça de antes intalar o python em [Click Aqui](https://www.python.org/downloads/). o servidor estará disponivel em "localhost:8050".

+ Para acessar o site do FIWARE [Click Aqui](https://www.fiware.org/).

+ Para conhecer um pouco mais sobre o ESP32 [Click Aqui](https://www.espressif.com/en/products/socs/esp32).


#### Outras configurações caso necessário:

Clone o Repositório:

bash
Copiar código
git clone <repository-url>
cd <repository-directory>
Instale as Dependências:

Para o backend (ASP.NET Core):

bash
Copiar código
dotnet restore
dotnet build
Para rodar o MongoDB localmente, você pode utilizar o Docker:

bash
Copiar código
docker run -d -p 27017:27017 --name mongo mongo
Configuração do MongoDB:

Altere o arquivo de configuração de conexão no projeto para apontar para o seu MongoDB.
Rodando o Servidor:

Execute o projeto no Visual Studio ou via linha de comando:
bash
Copiar código
dotnet run
Acesse o Dashboard:

Acesse o dashboard através do navegador, utilizando o endereço http://localhost:5000.