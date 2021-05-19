const swiper = new Swiper('.swiper-container', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
  
    breakpoints: {
        601: {
            slidesPerView: 2,
            spaceBetween: 5
        },
        1001: {
            slidesPerView: 3,
            spaceBetween: 5
        },
        1401: {
            slidesPerView: 4,
            spaceBetween: 5
        },
        1601: {
            slidesPerView: 5,
            spaceBetween: 0
        },
        1801: {
            slidesPerView: 6,
            spaceBetween: 0
        }
    }
  });

$(document).ready(function () {
    $('.slide2').owlCarousel({        
        autoplay: true,
        loop: true,
        margin: 10,
        nav: true,
        dots: false,
        center:false,
        autoplayHoverPause: true,
        smartSpeed: 1000,
        navText:[
            "",""
        ],
        responsive: {
            0: {
                items: 1
            },
            500: {
                items: 1
            },
            600: {
                items: 2
            },
            800: {
                items: 2
            },
            1000: {
                items: 3
            },
            1400: {
                items: 5
            },
            1801: {
                items: 6
            }
        }
    })
    $('.slide3').owlCarousel({        
        autoplay: true,
        loop: true,
        margin: 0,
        nav: false,
        dots: false,
        center:false,
        autoplayHoverPause: true,
        smartSpeed: 1000,
        navText:[
           "",""
        ],
        responsive: {
            0: {
                items: 1
            },
        }
    })
    $('.slide1').owlCarousel({
        autoplay: true,
        loop: true,
        margin: 10,
        nav: true,
        dots: false,
        center:false,
        autoplayHoverPause: true,
        smartSpeed: 1000,
        navText:[
           "",""
        ],
        responsive: {
            0: {
                items: 2
            },
            500: {
                items: 2
            },
            600: {
                items: 3
            },
            700: {
                items: 3
            },
            800: {
                items: 4
            },
            900: {
                items: 5
            },
            1000: {
                items: 5
            },
            1600:{
                items: 7
            },
            1800: {
                items: 9
            }
        }
    })  
});

const menuToggle = document.querySelector('#menu-togle');
const mobileNavContainer = document.querySelector('#mobile-nav');

menuToggle.onclick = function () {
    menuToggle.classList.toggle('menu-icon-active');
    mobileNavContainer.classList.toggle('mobile-nav--active');
}



