import { reactive } from 'vue'

export const indicies = reactive({
  arr: [...Array(3000).keys()],
})

export const pageOpt = reactive({
    currIdx: 1,
    perPage: 20
})

export const pageState = reactive({
  loading: false,
})