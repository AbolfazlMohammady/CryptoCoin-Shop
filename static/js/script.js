document.addEventListener('DOMContentLoaded', function() {
  let menu = document.querySelector('#menu-bar');
  let navbar = document.querySelector('.navbar');

  if (menu && navbar) {
    menu.onclick = () => {
      menu.classList.toggle('fa-times');
      navbar.classList.toggle('active');
    };

    window.onscroll = () => {
      menu.classList.remove('fa-times');
      navbar.classList.remove('active');
    };
  }

  let slides = document.querySelectorAll('.slide-container');
  let index = 0;

  if (slides.length > 0) {
    function next() {
      slides[index].classList.remove('active');
      index = (index + 1) % slides.length;
      slides[index].classList.add('active');
    }

    function prev() {
      slides[index].classList.remove('active');
      index = (index - 1 + slides.length) % slides.length;
      slides[index].classList.add('active');
    }

    // اگر نیاز به فراخوانی توابع `next` و `prev` دارید، کلیدهای خاص یا دکمه‌ها را مدیریت کنید
    document.querySelector('#next-slide')?.addEventListener('click', next);
    document.querySelector('#prev-slide')?.addEventListener('click', prev);
  }

  document.querySelectorAll('.featured-image-1').forEach(image_1 => {
    image_1.addEventListener('click', () => {
      var src = image_1.getAttribute('src');
      let bigImage = document.querySelector('.big-image-1');
      if (bigImage) {
        bigImage.src = src;
      }
    });
  });

  document.querySelectorAll('.featured-image-2').forEach(image_2 => {
    image_2.addEventListener('click', () => {
      var src = image_2.getAttribute('src');
      let bigImage = document.querySelector('.big-image-2');
      if (bigImage) {
        bigImage.src = src;
      }
    });
  });

  document.querySelectorAll('.featured-image-3').forEach(image_3 => {
    image_3.addEventListener('click', () => {
      var src = image_3.getAttribute('src');
      let bigImage = document.querySelector('.big-image-3');
      if (bigImage) {
        bigImage.src = src;
      }
    });
  });
});
