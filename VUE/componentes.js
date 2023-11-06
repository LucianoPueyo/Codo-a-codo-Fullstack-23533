const { createApp } = Vue;

const header = {
    template: `
    <header>
        <h1>Componentes VUE</h1>
        <p>Año {{año}}</p>
        <nav>
            <ul>
                <li v-for="link in links">
                    {{ link }}
                </li>
            </ul>
        </nav>
    </header>`,
    data(){
        return {
            año: 2023,
            links: ["Link 1", "Link 2", "Link 3"]
        }
    }
};

const main = {
    template: `
    <main>
        <h2>Codo a codo {{año}}</h2>
        <section>
            <article v-for="articulo in articulos">
                {{articulo}}
            </article>
        </section>
    </main>
    `,
    data(){
        return{
            año: 2023,
            articulos: ["Articulo1", "Articulo2"]
        }
    }
};

createApp({
    components: {
        "v-header": header,
        "v-main": main
    },

    data() {
        return {
            mensaje: "Hola Mundo Vue",
            curso: "Codo a codo",
            descripcion: "Esta es una descripcion mas detallada del curso de Codo a Codo",
            footer_content: "<p>2023 - todos los derechos reservados <span>Codo a Codo</span></p>",
            inscripciones_abiertas: true,
            cursos: ["Fullstack Python", "UX/UI", "Testing/QA"]
        }
    }
}).mount('#app')