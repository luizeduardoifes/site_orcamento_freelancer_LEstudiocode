// js/menu.js
(function () {

    function formatPhone(value) {
        const nums = value.replace(/\D/g, '').slice(0, 11);

        if (!nums) return '';

        if (nums.length <= 2) return '(' + nums;

        const ddd = nums.slice(0, 2);
        const rest = nums.slice(2);

        if (rest.length > 4) {
            const left = rest.slice(0, rest.length - 4);
            const right = rest.slice(-4);
            return `(${ddd}) ${left}-${right}`;
        }

        return `(${ddd}) ${rest}`;
    }

    function onInput(e) {
        const el = e.target;
        const cursor = el.selectionStart;
        const oldLength = el.value.length;

        el.value = formatPhone(el.value);

        const newLength = el.value.length;
        const diff = newLength - oldLength;
        const newPos = cursor + diff;

        el.setSelectionRange(newPos, newPos);
    }

    function init() {
        document.querySelectorAll(
            'input.telefone, input[data-mask="telefone"], input[type="tel"]'
        ).forEach(input => {
            input.addEventListener('input', onInput);
            input.value = formatPhone(input.value);
        });
    }

    document.addEventListener('DOMContentLoaded', init);

})();
