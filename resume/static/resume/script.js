// card measurements in mm
// card_width = 63;
// card_height = 88;
// outer_border_width = 2;
// bottom_border_height = 6;
// bottom_border_inner_height = 1;
// inner_border_width = 2;
// inner_band = 1;
// top_field_height = 5;
// type_field_height = 5;
// outer border has rounded outside and inside corners, outside over 2 mil and inside over .5 mil
// all side borders on name box 1 mil with .4 mil as top/right highlight
// side borders on picture frame 1 mil
// all side borders on creature type 1 mil
// side and bottom border on text box 1 mil
// .5 mil border on power/toughness with .5 mil drop shadow (down and left)


// const card_width = 63;
// const card_height = 88;
// const outer_card_border = 3;
// const inner_card_width = 59;
// const inner_card_height = 76;
// const inner_card_margin = 2;
// const inner_card_border = 2;
// const inner_card_padding = 1;
// const inner_card_border_radius = [2, 2, 5, 5];

// const text_bar_width = 55;
// const text_bar_height = 55;
// const text_bar_border_radius = 55;
// const text_bar_box_shadow = [[0, 0, 0, .5], [1, -1, .25, -.75], [-1, 1, .25, -.75]];
// const text_bar_font_size = .80; //percentage
// const text_bar_padding_left = .02; //percentage
// const text_bar_line_height = 5;

// const name_box_margin_top = 2;

// const image_box_width = 53;
// const image_box_height = 39;
// const image_box_margin_top_bottom = .6;
// const image_box_box_shadow = [0, 0, 0, .5];

// const text_box_width = 53;
// const text_box_height = 26;
// const text_box_margin_top = .6;
// const text_box_box_shadow = [0, 0, 0, .5];
// const text_box_font_size = .5; //percentage

// const text_box_ul_padding_left = .05; //percentage
// const text_box_ul_margin = 0;

// const text_box_ul_li_margin_bottom = 1;

// const power_box_height = 4;
// const power_box_border_radius = [3, 10];
// const power_box_box_shadow = [[0, 0, 0, .5], [-1, 1, .25, -.75]];
// const power_box_font_size = .5; //percentage
// const power_box_line_height = 4;
// const power_box_padding_left_right = 1;
// const power_box_margin_top = -2;


const measure = document.createElement('span');

document.addEventListener('DOMContentLoaded', function(){
    draw_socials();

    let [card_container, children, next, previous] = initialize_cards();
    let current_idx = 0;
    next.addEventListener('click', () => {
        current_idx = (current_idx + 1) % children.length;
        switch_child(current_idx, children);
    })
    previous.addEventListener('click', () => {
        current_idx = (current_idx - 1 + children.length) % children.length;
        switch_child(current_idx, children);
    })

    

    measure.style.position = 'absolute';
    measure.style.visibility = 'hidden';
    measure.style.whiteSpace = 'nowrap';
    measure.style.top = '-9999px';
    measure.style.left = '-9999px';

    document.body.appendChild(measure);
    console.log('measure: ' + measure);

    document.querySelectorAll('.name_box_text').forEach(fit_text);
})

window.addEventListener('resize', function(){
//     let text_bar = document.getElementsByClassName('text_bar')[0];
//     let text_bar_width = this.getComputedStyle(text_bar).width.slice(0, -2);
//     // text_bar_width = Math.floor(text_bar_width);
//     // let text_bar_width2 = text_bar.getBoundingClientRect().width;
//     console.log('text bar width type: '+ typeof(text_bar_width))
//     console.log('text bar width: ' + text_bar_width);
//     // console.log('text bar width2: ' + text_bar_width2);
//     let text_content = text_bar.innerText;
//     console.log('text bar content: ' + text_content)
//     console.log('text bar content length: ' + text_content.length)
//     console.log('space per char: ' + (text_bar_width/text_content.length))

    let element = document.querySelectorAll('#name_box_text')[0]
    
    fit_text(element);
})


function fit_text(el, base_size=100){
    console.log('fitting text');
    const parent = el.parentElement;
    console.log('parent: '+ parent);

    measure.style.font = window.getComputedStyle(el).font;
    measure.style.fontSize = base_size + 'px';
    measure.textContent = el.textContent;
    console.log('el.textcontent ' + el.textContent);
    console.log('measure.textcontent ' + measure.textContent);

    const text_width = measure.offsetWidth;
    const text_height = measure.offsetHeight;
    console.log('offset width: ' + measure.offsetWidth);
    console.log('offset height: ' + measure.offsetHeight);

    console.log('parentWidth: '+ parent.clientWidth);
    console.log('parentHeight: '+ parent.clientHeight);
    const scale_x = parent.clientWidth / text_width;
    const scale_y = parent.clientHeight / text_height;
    console.log('scale_x: ' + scale_x);
    console.log('scale_y: ' + scale_y);

    const scale = Math.min(scale_x, scale_y);
    console.log('scale: ' + scale);
    console.log('scale*base_size: ' + scale*base_size);

    el.style.fontSize = (base_size * scale) + 'px';
}

function draw_socials(){
    linkedin_svg_element = document.getElementById('linkedin_svg');
    linkedin_color = '#0A66C2';
    linkedin_svg_element.setAttribute('fill', linkedin_color);
    linkedin_path_element = document.getElementById('linkedin_path');
    linkedin_path = 'M20.5 2h-17A1.5 1.5 0 0 0 2 3.5v17A1.5 1.5 0 0 0 3.5 22h17a1.5 1.5 0 0 0 1.5-1.5v-17A1.5 1.5 0 0 0 20.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 1 1 8.3 6.5a1.78 1.78 0 0 1-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0 0 13 14.19a.66.66 0 0 0 0 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 0 1 2.7-1.4c1.55 0 3.36.86 3.36 3.66z';
    linkedin_path_element.setAttribute('d', linkedin_path);
    github_svg_element = document.getElementById('github_svg');
    github_color = '#000000';
    github_svg_element.setAttribute('fill', github_color);
    github_path_element = document.getElementById('github_path');
    github_path = 'M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.026 2.747-1.026.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z';
    github_path_element.setAttribute('d', github_path);
}

function switch_child(idx, children){
    children.forEach((child, i) => {
        child.style.display = i === idx ? 'block' : 'none';
    });
}

function initialize_cards(){
    let card_container = document.getElementById('job_div');
    let children = card_container.querySelectorAll('.card_outer')
    let next_button = document.getElementById('next');
    let previous_button = document.getElementById('previous');
    return [card_container, children, next_button, previous_button];
}
