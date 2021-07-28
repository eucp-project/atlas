<template>
  <div class="container mx-auto p-4 h-screen self-center">
    <div class="flex p-4">
      <NuxtLink :to="`/`">
            <img src="~/static/eucp_logo.png" alt="EUCP Logo">
      </NuxtLink>
    </div>
    <div class="bg-gray-100 p-4 text-4xl">
      <p>
        Title
      </p>
    </div>
    <div class="pl-4 mb-0 text-gray-400">
      <p>
        Publications
      </p>
    </div>
    <div class="flex flex-row mb-8">
      <div class="pl-4 w-1/3 no-wrap text-left">
        <div>
          <p>
            Authors
          </p>
          <p>
            Citation info
          </p>
        </div>
        <div class ="space-y-6 space-y-reverse">
          <h2 class ="text-xl mt-8">
            Highlights
          </h2>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat aperiam
            laudantium maxime optio, ratione adipisci temporibus earum accusamus
            soluta obcaecati porro quasi inventore cum ducimus veritatis?
          </p>
          <p>
            <em>
              Background
              <br>
            </em>
            Culpa sedvitae nostrum quod ipsum facilis aliquam nihil doloribus,
            eum sequi cupiditate, quae porro aspernatur quas quo tempora
            consectetur architecto, asperiores quasi dolorum iste cumque omnis
            sapiente non.
          </p>
          <p>
            <em>
              Results
              <br>
            </em>
            Aut consequatur vero, labore cum illum nisi! Adipisci reiciendis
            nostrum labore eveniet saepe tempora dolorem dolores harum earum.
            Vero illo fugit libero ullam amet vel veniam ad fuga, temporibus id
            sint maxime, incidunt, dolore dolor quam eos labore a tempora
            soluta.
          </p>
          <p>
            <em>
              Methods
              <br>
            </em>
            Accusantium non maiores iure quis quidem fugit qui commodi
            necessitatibus. Voluptates sapiente ab architecto exercitationem
            repellat amet veritatis cupiditate ullam repudiandae reiciendis,
            tempore iure alias ratione porro, quibusdam veniam voluptatibus
            deserunt tenetur, distinctio unde repellendus?
          </p>
          <p>
            <em>
              Policy relevance
              <br>
            </em>
            A maiores consequuntur rem ea explicabo obcaecati, ad quis
            inventore dolore ullam saepe ipsum veritatis sunt totam et
            quisquam!
          </p>
        </div>
      </div>
      <div class="p-4 w-1/3 no-wrap text-left bg-blue-900 p-4 text-white">
        <p>
          Abstract
        </p>
      </div>
    </div>
    <Button :text="`Back`" :target="`/`" />
  </div>
</template>
