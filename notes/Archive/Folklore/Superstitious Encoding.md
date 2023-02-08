The tribulations of obscure character encoding.

The following is taken from a comment on HN written by user jake_morrison on 2022-07-14.

---

In the 90s I worked on a project to digitize land registration in Taiwan.

In order to record deeds and property transfers, we needed to enter people's names and official registered addresses into the computer system. The problem was that some people used non-traditional writing variants for their names, and some of their birthplaces were tiny places in China with weird names.

Someone might write their name with a two-dot water radical instead of three-dot radical. We would print it out in the normal font, and the people would lose their minds, saying that it was wrong. Chinese people can be superstitious about the number of strokes in their name, so adding a stroke might make it unlucky, so they would not buy the property.

The customer went to the agency responsible for managing the big character set, https://en.wikipedia.org/wiki/CNS_11643 Despite having more characters than anything else on earth, it didn't have those variants. The agency said they would not encode them, because they were not real characters, just printing differences.

The solution was for the staff in the office to use a "font maker" program to create a custom font with these characters. Then they could print out the deeds using a Chinese variant of Adobe Acrobat, and everyone was happy. 