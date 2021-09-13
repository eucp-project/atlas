<template>
  <div>
    <div class="flex place-content-center bg-gray-100 m-4">
      <h1 class="text-2xl p-6 align-middle">
        Comparing Constrained Future European Climate Projections
      </h1>
    </div>
    <div class="flex flex-row mb-2 mt-2 p-4">
      <div class="pl-4 w-2/3 no-wrap text-left">
        <div class="space-y-6 space-y-reverse pt-8">
          <h2 class="text-xl">
            How do these methods work?
          </h2>
          <p>
            Summary in accessible language about how constraints work.
          </p>
          <h2 class="text-xl">
            What are the differences between the methods?
          </h2>
          <p>
            <ul class="list-disc list-inside">
              <li>Weighting available models vs scaling model responses. ETH, CNRS, ICTP and UKMO methods are based on weighting available historical-future simulations (based on how well they reproduce observed climate). As such the probabilistic projections will always reflect a subset of existing simulations. Edin and Oxford methods both scale the simulations to best match observations. Unlike the former category, their projected future changes can fall outside the range of the underlying simulations. Where projected changes do fall outside this range, there are potential strengths and reasons to be cautious about the how we interpret these changes. The strength of these methods is that they can potential compensate for real world processes that are missing or unrepresented in the simulations. For example, there are cases of observed historical rainfall changes being larger than any simulated. In these cases, the methods may be better able to compensate for any simulated underestimation of the actual climate response. Caution may also be warranted in that available simulations represent the range of responses arising from our current physical understanding of these process - so methods that adjust projected changes outside these ranges may push these into responses which are less physically realistic.</li>
              <li>Differences in sources of uncertainty accounted for. The majority of methods employed in D2.3 make use of available CMIP data. These represent snapshots of climate simulations from our current international archives. the UKMO method, however, also include uncertainties from other terms (carbon cycle, model parametric uncertainty). As such its ranges are wider</li>
              <li>Differences in ease of application. Some methods are easy to set up, whilst other require more involved implementation relient on data sources or expert judgement.</li>
            </ul>
          </p>
          <h2 class="text-xl">
            Which method is "best"?
          </h2>
          <p>
            Summary of perfect-model analysis take-home messages.
          </p>
          <h2 class="text-xl">
            Hypothetical cases
          </h2>
          <p>
            <ul class="list-disc list-inside">
              <li>User X wants to ... . In this case, they used ... because ...</li>
              <li>For ..., user Y was mainly interested in ... over ... They used method ... because ...</li>
              <li>User Z is planning to ... Since ...., they decided to go with the ... method.</li>
            </ul>
          </p>
        </div>
      </div>
      <div class="p-4 w-1/3 ml-8 no-wrap text-left bg-blue-900 text-white space-y-6">
        <h2 class="text-xl mt-2">
          Publications
        </h2>
        <p>
          Comparing Methods to Constrain Future European Climate Projections Using a Consistent Framework: <br>
          <strong>
            <a href="https://doi.org/10.1175/JCLI-D-19-0953.1">https://doi.org/10.1175/JCLI-D-19-0953.1</a>
          </strong>
        </p>
        <p>
          Another paper
        </p>
      </div>
    </div>
    <Button :text="`Back`" :target="`/`" />
  </div>
</template>
