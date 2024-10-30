import globals from "globals";
import pluginJs from "@eslint/js";
import promise from "eslint-plugin-promise";
import neostandard from 'neostandard'

export default [
    ...neostandard(),
  {
    ignores: [
      "node_modules/",
      "venv/",
      "static/"
    ],
    languageOptions: { globals: globals.browser },
    plugins: {
      promise: promise,
    },
    rules: {
      "no-restricted-syntax": ["error", "TemplateLiteral"],
    },
    settings: {
      "import/core-modules": ["django"],
    },
  },
];
