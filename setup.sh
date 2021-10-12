mkdir -p ~/.streamlit/

echo "\
[theme]
base='light'\n\
primaryColor='#1cb4c4'\n\
[server]\n\
maxUploadSize = 250\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml