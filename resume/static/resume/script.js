// card measurements in mm
card_width = 63;
card_height = 88;
outer_border_width = 2;
bottom_border_height = 6;
bottom_border_inner_height = 1;
inner_border_width = 2;
inner_band = 1;
top_field_height = 5;
type_field_height = 5;
// outer border has rounded outside and inside corners, outside over 2 mil and inside over .5 mil
// all side borders on name box 1 mil with .4 mil as top highlight
// side borders on picture frame 1 mil
// all side borders on creature type 1 mil
// side and bottom border on text box 1 mil
// .5 mil border on power/toughness with .5 mil drop shadow (down and left)



document.addEventListener('DOMContentLoaded', function(){
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
})