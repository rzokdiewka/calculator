<script setup>
import {ref, reactive, watch, onMounted} from "vue";

const operator = ref("+")
const valueA = ref(0)
const valueB = ref(0)
const result = ref()


watch([valueA, () => valueB.value, () => operator.value], ([valueA, valueB, operator]) => {
  requestOptions.body = JSON.stringify({"operators": [operator], "operands": [Number(valueA), Number(valueB)]})

})
const requestOptions = reactive({
  method: 'POST',
  headers: {'accept': 'application/json', 'Content-Type': 'application/json', 'Access-Control-Allow-Headers': '*'},
});
const calculate = async () => {
  const response = await fetch(`http://127.0.0.1:8000/calculate?app_id=AppID`, requestOptions)
  await response.json().then(re => result.value = re["result"]);
}

onMounted(
    requestOptions.body = JSON.stringify({
      "operators": [operator.value],
      "operands": [Number(valueA.value), Number(valueB.value)]
    })
)
</script>

<template>

  <main>
    <div class="calculator">
      <input type="number" required v-model="valueA"/>
      <select v-model="operator">
        <option>+</option>
        <option>-</option>
        <option>*</option>
        <option>/</option>
      </select>
      <input type="number" v-model="valueB"/>
      <p>=</p>
      <input type="number" v-model="result" disabled/>
      <button @click="calculate">Count</button>
    </div>
  </main>
</template>
