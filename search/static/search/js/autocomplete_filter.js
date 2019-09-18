function filter() {
    //year
    let min_year = document.getElementById("min_year");
    let max_year = document.getElementById("max_year");

    //Time
    let min_time = document.getElementById("min_time");
    let max_time = document.getElementById("max_time");
    console.log(min_time.value);

    //Criteria
    let min_alcohol = document.getElementById("min_alcohol");
    let min_language = document.getElementById("min_language");
    let min_lgbtq = document.getElementById("min_lgbtq");
    let min_nudity = document.getElementById("min_nudity");
    let min_sex = document.getElementById("min_sex");
    let min_violence = document.getElementById("min_violence");
    let max_alcohol = document.getElementById("max_alcohol");
    let max_language = document.getElementById("max_language");
    let max_lgbtq = document.getElementById("max_lgbtq");
    let max_nudity = document.getElementById("max_nudity");
    let max_sex = document.getElementById("max_sex");
    let max_violence = document.getElementById("max_violence");

    //Genres
    let action = document.getElementById("Action");
    let adventure = document.getElementById("Adventure");
    let animation = document.getElementById("Animation");
    let comedy = document.getElementById("Comedy");
    let crime = document.getElementById("Crime");
    let drama = document.getElementById("Drama");
    let fantasy = document.getElementById("Fantasy");
    let historical = document.getElementById("Historical");
    let horror = document.getElementById("Horror");
    let mystery = document.getElementById("Mystery");
    let political = document.getElementById("Political");
    let romance = document.getElementById("Romance");
    let satire = document.getElementById("Satire");
    let sci_fi = document.getElementById("Sci-Fi");

    let genres = "";
    if (action.checked)
        genres = genres + "Action_";
    if (adventure.checked)
        genres = genres + "Adventure_";
    if (animation.checked)
        genres = genres + "Animation_";
    if (comedy.checked)
        genres = genres + "Comedy_";
    if (crime.checked)
        genres = genres + "Crime_";
    if (drama.checked)
        genres = genres + "Drama_";
    if (fantasy.checked)
        genres = genres + "Fantasy_";
    if (historical.checked)
        genres = genres + "Historical_";
    if (horror.checked)
        genres = genres + "Horror_";
    if (mystery.checked)
        genres = genres + "Mystery_";
    if (political.checked)
        genres = genres + "Political_";
    if (romance.checked)
        genres = genres + "Romance_";
    if (satire.checked)
        genres = genres + "Satire_";
    if (sci_fi.checked)
        genres = genres + "Sci-Fi_";

    genres = genres.substring(0, genres.length - 1);
    if (genres === '')
        genres = 'NAN';
    $(".search-results1").load("search/auto_filter/" + max_year.value + "/" + min_year.value + "/" + max_time.value +
        "/" + min_time.value + "/" + Math.floor(max_alcohol.value * 10) + "/" + Math.floor(min_alcohol.value * 10) +
        "/" + Math.floor(max_language.value * 10) + "/" + Math.floor(min_language.value * 10) +
        "/" + Math.floor(max_lgbtq.value * 10) + "/" + Math.floor(min_lgbtq.value * 10) +
        "/" + Math.floor(max_nudity.value * 10) + "/" + Math.floor(min_nudity.value * 10) +
        "/" + Math.floor(max_sex.value * 10) + "/" + Math.floor(min_sex.value * 10) +
        "/" + Math.floor(max_violence.value * 10) + "/" + Math.floor(min_violence.value * 10) +
        "/" + genres);
}