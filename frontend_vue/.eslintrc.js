module.exports = {
  root: true,
  env: {
    node: true
  },
  'extends': [
    'plugin:vue/vue3-essential',
    'eslint:recommended',
  ],
  parserOptions: {
    ecmaVersion: 2020
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'vue/no-deprecated-slot-attribute': 'off',
    'vue/no-useless-template-attributes':'off',
    'vue/no-deprecated-slot-scope-attribute':'off',
    'vue/multi-word-component-names': 'off', 
    'no-prototype-builtins': 'off',
    'vue/no-parsing-error' : 'off',
    'vue/no-use-v-if-with-v-for' :'off'
  }
}
