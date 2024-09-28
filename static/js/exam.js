
const { createApp, ref } = Vue

//const template = ``;

createApp({
    // template,
    setup() {
        const saikat = ref('Hello vue!');
        const activeTab = ref(0);
        const activeQuestion = ref(0);
        const answeredQuestions = ref([]);
        const questionAudio = ref(null);

        const tabChange = (index)=>{
            activeTab.value = index;
            console.log(index);
        }

        return {
            saikat, activeTab, tabChange
      }
    }
})
.component("", {
    
})
.mount('#app')