<template>
  <div id="box">
    <div class="form__group field">
      <input type="input" class="form__field" placeholder="Question" name="question" id='question_input' v-model="question_text" required />
      <label for="name" class="form__label">Question</label>
    </div>
    <br><br>
    <a class="btn" v-on:click="postQuestion()">Sasha ?</a>
    <br><br><br>
    <p>{{ answer_text }}</p>
  </div>
</template>

<script>
export default {
  name: 'InputComponent',
  data: () => {
    return {
      question_text: '',
      answer_text: ''
    }
  },
  props: {
    backend_url: String
  },
  methods: {
    postQuestion() {
      // Disable input
      document.getElementById('question_input').disabled = true

      // Send post request
      const xhr = new XMLHttpRequest()
      xhr.open('post', this.backend_url + '/question', true)

      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

      xhr.onreadystatechange = () => { // Callback post request
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
          // Request finish
          // Get response
          this.answer_text = xhr.response
          // Enable input
          document.getElementById('question_input').disabled = false
        }
      }

      xhr.send('question=' + this.question_text);
      this.answer_text = 'En cours de traitement...'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.form__group {
  position: relative;
  padding: 15px 0 0;
  margin-top: -10px;
  width: 50%;
}

.form__field {
  font-family: inherit;
  width: 100%;
  border: 0;
  border-bottom: 2px solid #9b9b9b;
  outline: 0;
  font-size: 1.3rem;
  color: #fff;
  padding: 7px 0;
  background: transparent;
  transition: border-color 0.2s;
}
.form__field::placeholder {
  color: transparent;
}
.form__field:placeholder-shown ~ .form__label {
  font-size: 1.3rem;
  cursor: text;
  top: 20px;
}

.form__label {
  position: absolute;
  top: 0;
  display: block;
  transition: 0.2s;
  font-size: 1rem;
  color: #9b9b9b;
}

.form__field:focus {
  padding-bottom: 6px;
  font-weight: 700;
  border-width: 3px;
  border-image: linear-gradient(to right, #11998e, #38ef7d);
  border-image-slice: 1;
}
.form__field:focus ~ .form__label {
  position: absolute;
  top: 0;
  display: block;
  transition: 0.2s;
  font-size: 1rem;
  color: #ffffff;
  font-weight: 700;
}

/* reset input */
.form__field:required, .form__field:invalid {
  box-shadow: none;
}

/* demo */
#box {
  font-family: "Poppins", sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 1.5rem;
  background-color: #222222;
}

a {
  font-size: 1.5rem;
  padding: 1rem 3rem;
  color: #f4f4f4;
  text-transform: uppercase;
}

.btn {
  text-decoration: none;
  border: 1px solid rgb(146, 148, 248);
  position: relative;
  overflow: hidden;
  cursor: pointer;
}

.btn:hover {
  box-shadow: 1px 1px 25px 10px rgba(146, 148, 248, 0.4);
}

.btn:before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent,
    rgba(146, 148, 248, 0.4),
    transparent
  );
  transition: all 650ms;
}

.btn:hover:before {
  left: 100%;
}

p {
  color: white;
}

</style>
