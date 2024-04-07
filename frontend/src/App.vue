<script setup>
import {ref, reactive, watch} from "vue";

const operator = ref("+")
const valueA = ref()
const valueB = ref()
const result = ref()


watch([valueA, () => valueB.value, () => operator.value], ([valueA, valueB, operator]) => {
  requestOptions.body = JSON.stringify({"operators": [operator], "operands": [Number(valueA), Number(valueB)]})

})
const requestOptions = reactive({
  method: 'POST',
  headers: {'accept': 'application/json', 'Content-Type': 'application/json', 'Access-Control-Allow-Headers': '*'},
});
const calculate = async () => {
  const response = await fetch(`http://127.0.0.1:8000/calculate`, requestOptions)
  await response.json().then(re => result.value = re["result"]);
}

</script>

<template>

  <main>
    <div class="calculator">
      <input type="text" required v-model="valueA"/>
      <select v-model="operator">
        <option>+</option>
        <option>-</option>
        <option>*</option>
        <option>/</option>
      </select>
      <input type="number" v-model="valueB"/>
      =
      <input type="number" v-model="result"/>
      <button @click="calculate">Count</button>
    </div>
  </main>
</template>
