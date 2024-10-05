
const { createApp, ref, onMounted, computed, onBeforeUpdate, useEffect } = Vue

//const template = ``;

// function questionObj(question, index, answer=null){
//     return {
//         index,
//         id,
//         question,
//         answer,
//     };
// };


createApp(
{
    delimiters: ['${', '}$'],
    // template,
    setup() {
        const examId = null;

        const activeTab = ref(0);
        const showList = ref(true);
        const total_audio = ref([]);
        const total_others = ref([]);

        const activeQuestion = ref({});
        const questionAudio = ref(null);
        const activeAudios = ref([]);
        const activeOthers = ref([]);

        const tabChange = (index)=>{
            if (screen.width <= 1280){   // change the value               
                if ( (index === activeTab.value) && (showList.value === true) ){
                    showList.value = false;
                }else{
                    showList.value = true;
                    activeTab.value = index;
                }
            }else{
                activeTab.value = index;
            }
        }


        const answer = (selection)=>{
            if (!activeQuestion.value.answer)
                activeQuestion.value.answer = selection;
            console.log("okaaaayyyyy.....");
            
        }


        onMounted(()=>{
            if (showList.value === true){
                console.log("same tab press");
                showList.value = false;
            }
            const data = JSON.parse(document.getElementById("data"));
            examId = data.id;

            data.questions.forEach( (val, ind) =>{
                // if val.type !== 'audio'
                if(val.type !== "audio"){
                    total_others.value = [ ...total_others.value, { index : ind+1, question: null, answer: null}];
                 // if val.type === 'audio'
                }else{
                    console.log(ind);
                    total_audio.value = [ ...total_audio.value, { index : ind+1, question: null, answer: null}];    
                }
            })

            activeAudios.value = total_audio.value;
            activeOthers.value = total_others.value;
            activeQuestion.value = total_others.value[0];
        });

        const preventReload = (e)=>{
          e?.preventDefault();
        };

        useEffect(()=>{
            window.addEventListener("beforereload", preventReload);
            return  window.removeEventListener("beforereload", preventReload);
        });


        const solvedAudios = computed( ()=> {
            return [];
        });

        const solvedOthers = computed( ()=> {
            return [];
        });

        const unsolvedAudios = computed( ()=> {
            return [];
        });

        const unsolvedOthers = computed( ()=> {
            return [];
        });


        return { total_audio, total_others, solvedAudios, solvedOthers,
            unsolvedAudios, unsolvedOthers, activeTab, tabChange, showList, 
            activeAudios, activeOthers, activeQuestion, answer,
        };
    }
}
).mount('#app')