<template>
  <div class="home">
    <div class="container mt-2">
      <div v-for='question in questions' :key="question.pk">
        <p class="mb-0">Post by:
          <span class="question-author">{{ question.author}}</span>
        </p>
        <h2>
          <router-link :to="{ name: 'question', params: { slug: question.slug} }" class="question-link">
            {{ question.content }}
            </router-link>
          </h2>
        <p>Answers : {{ question.answer_count }}</p>
        <hr>
        <div class="my-4"><p v-show="loadingQuestions">...loading...</p></div>
      </div>
      <button v-show="next" @click="getQuestions" class="btn btn-sm btn-outline-success">Load More</button>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from '../common/api.service'

export default {
  name: "home",
  data() {
    return {
      questions: [],
      next: null,
      loadingQuestions: false
    }
  },
  methods: {
    getQuestions(){
      let endpoint = '/api/questions/';
      if (this.next){
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      apiService(endpoint)
      .then(data => {
        this.questions.push(...data.results);
         this.loadingQuestions = false;
        if (data.next){
          this.next = data.next;
        }else{
          this.next = null;
        }
      })
    }
  },
  created(){
    this.getQuestions()
    document.title = 'QuestionTime';
    // console.log(this.questions)
  }
};
</script>

<style scoped>
  .question-author{
    font-weight: bold;
    color: #DC3545;
  }

  .question-link{
    font-weight: bold;
    color: black;
  }

  .question-link:hover{
    color: #343a40;
    text-decoration: none;
  }
</style>
