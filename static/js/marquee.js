function startMarquee() {
            const marquee = document.querySelector('.marquee');
            const text = document.getElementById('marquee-text');
            const marqueeWidth = marquee.offsetWidth;
            const textWidth = text.offsetWidth;
            const duration = (textWidth + marqueeWidth) / 50; // Скорость в пикселях в секунду

            text.style.animation = `marquee ${duration}s linear infinite`;
        }

        window.onload = startMarquee;
        window.onresize = startMarquee;