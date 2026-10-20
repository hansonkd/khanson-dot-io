const year = document.querySelector('#year');
year.textContent = new Date().getFullYear();

const copyButton = document.querySelector('.copy-email');
const status = document.querySelector('.copy-status');
if (navigator.clipboard?.writeText) {
  copyButton.hidden = false;
  copyButton.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText('me@khanson.io');
      status.textContent = 'Email address copied.';
    } catch {
      status.textContent = 'Select and copy: me@khanson.io';
    }
  });
}
