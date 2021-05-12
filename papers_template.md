---
title:  "Continual Learning Papers"
layout: page
---

## Papers graph
    
{% include embedding-plot.html %}

## Publications

In this section we maintain an updated list of publications related to Continual Learning.
This references list is automatically generated by a single bibtex file maintained
by the ContinualAI community through an open Mendeley group! Join our group [here](https://www.mendeley.com/community/continual-learning-papers/?__cf_chl_captcha_tk__=d4a16b2e7ba082bc24fbb7fb7cbba3149969ff33-1589287156-0-Aa1Wr5LQkCQwqaFz3Ho_5lc1NnR1Dn6bDEe8fZlbjwIKIQy-b28wKYYcbcdksrP0zP2e8x1BfyD3V0eiZWMVdFQ0AqGzm8qHQYklAGUPz0COhkQec_hu0O1_XFh7PtHXNKfIiyBb9TppP05KlSNIIxJk2u7lNAlGw1pWscPNhIvk_4p-5XDf-YFu3HpCDYN1IQ7bQgkGqMRYAdYtZS7gq1C_w6iykd2sA6IawsIbaCtdW08H77e-7T7rEdo91HndXMIJgV5UQBnJSwRHOl-g-8EKrUWUDHBdGQgLhiJli4y16AAGu979jkOyhtS7onFfRNXdUELb3pOiD0YS5zCnmHM6PURblRyb6HA2ma7f0JIC8DIjmK2xCcRlYqgiNrWVS3oEbS6uqn63IdxYgoSLq6vo68mS1e_Or8LGRpOE8uemjJfbVnPR4RI3mqevN5OxbgWz-CYkElgLAXeaEFqVitVCsaEmDygdit6flohhCpCd5vVs6gv1t_ALu6Q7nZIbFc386zRcqDb-MhIV7BpRIOA) to add a reference to your paper! Please, remember to follow the (very simple) [contributions guidelines](https://github.com/ContinualAI/wiki#how-to-contribute-to-the-continualai-database-of-publications) when adding new papers.

<PAPER_COUNT>

<script>
    function apply_filters() {
      li = get_papers_li();
      li = keyword_filter(li);
      li = regex_filter(li);
      year_filter(li);
    }
</script>

<script>
    function get_papers_li() {
      sec = document.getElementById("publications");
      li = sec.getElementsByTagName('li');
      return li;
    }
</script>

<script>
    function keyword_filter(li) {
      // Declare variables
      var input, filter, ul, a, i, txtValue;
      input = document.getElementById('myInput');
      filter = input.value.toUpperCase();
      remaining_li = [];

      // Loop through all list items, and hide those who don't match the search query
      for (i = 0; i < li.length; i++) {
        txtValue = li[i].textContent || li[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          li[i].style.display = "";
          remaining_li.push(li[i]);
        } else {
          li[i].style.display = "none";
        }
      }

      return remaining_li;
    }
</script>

<script>
    function regex_filter(li) {
      // Declare variables
      var input, filter, ul, a, i, txtValue;
      input = document.getElementById('myInputreg');
      // filter = input.value.toUpperCase();
      filter = input.value;
      remaining_li = [];

      // Loop through all list items, and hide those who don't match the search query
      for (i = 0; i < li.length; i++) {
        txtValue = li[i].textContent || li[i].innerText;
        if (txtValue.match(filter)) {
          li[i].style.display = "";
          remaining_li.push(li[i]);
        } else {
          li[i].style.display = "none";
        }
      }

      return remaining_li;
    }
</script>

<script>
    function year_filter(li) {
      // Declare variables
      var input, filter, ul, a, i, txtValue;
      start_year_input = document.getElementById('filterStartYearInput');
      filter_start_year_string = start_year_input.value;
      filter_start_year = parseInt(filter_start_year_string);
      end_year_input = document.getElementById('filterEndYearInput');
      filter_end_year_string = end_year_input.value;
      filter_end_year = parseInt(filter_end_year_string);
      // check for Not a Number:
      if (filter_start_year != filter_start_year) {
        filter_start_year = Number.MIN_VALUE;
      }

      if (filter_end_year != filter_end_year) {
        filter_end_year = Number.MAX_VALUE;
      }

      remaining_li = [];

      // Loop through all list items, and hide those who don't match the search query
      for (i = 0; i < li.length; i++) {
        year_string = li[i].getElementsByClassName("yearSpan")[0].textContent;
        year = parseInt(year_string);
        if (year >= filter_start_year && year <= filter_end_year) {
          li[i].style.display = "";
          remaining_li.push(li[i]);
        } else {
          li[i].style.display = "none";
        }
      }


      return remaining_li;
    }
</script>


**Filter list by keyword:** <input type="text" id="myInput" onkeyup="apply_filters()" placeholder="Insert keywords here..."><br>
**Filter list by regex:** <input type="text" id="myInputreg" onkeyup="apply_filters()" placeholder="Insert regex here..." style="margin-left:22px"><br>
**Filter list by year:** <input type="text" id="filterStartYearInput" onkeyup="apply_filters()" placeholder="Insert start year here..." style="margin-left:31px"><input type="text" id="filterEndYearInput" onkeyup="apply_filters()" placeholder="Insert end year here..." style="margin-left:10px">

<TAGLIST>

<TAG>

