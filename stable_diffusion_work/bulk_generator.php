<?php

$ideas = [
    // example images
    // landscapes
    "https://image.lexica.art/md/2b2e420f-e782-4bc8-98a6-5dfca8cb7f98",
    "https://image.lexica.art/md/20a28de0-797d-4b7b-8d7e-84cec6e11459",
    "https://image.lexica.art/md/a0cf59af-cb97-40e4-b7fc-97d62ea85f2a",
    "https://image.lexica.art/md/fb7955b7-30a8-4d52-bcf1-1916503f5e92",
    "https://image.lexica.art/md/bff30d8a-3012-4228-b548-c954e1e79d96",
    "https://image.lexica.art/md/31304c0e-563d-4645-a025-8d6480214ba3",
    "https://image.lexica.art/md/0e223d50-b1a5-4ae3-82d5-14f6360c7398",
    "https://image.lexica.art/md/c0d1b06f-d5f9-43b3-bf9f-d3e4b079b275",
    "https://image.lexica.art/md/70785c22-ee53-4804-9116-b25ba78b8b3d",
    "https://image.lexica.art/md/f1b370f0-6eb0-4c7d-a7cd-25ab2cfda29d",
    "https://image.lexica.art/md/39c59406-8495-4c5b-8d3a-4c0090095e9f",
    "https://image.lexica.art/md/d3817917-c726-4044-bb41-4c3b6c3ecc15",
    "https://image.lexica.art/md/c9af31af-8e78-4292-b89d-97d50219ab64",
    "https://image.lexica.art/md/cfa0d369-2e9f-45c4-a146-d70dfcd297b7",
    "https://image.lexica.art/md/11cf124d-e64f-4b5c-b3a1-caa0704afff3",
    "https://image.lexica.art/md/7bbd6ce2-a65e-4941-8920-4bf2bbc6bbe8",
    "https://image.lexica.art/md/95661eb9-898f-47b4-a7ab-85b909ca2409",
    "https://image.lexica.art/md/3aef5c0b-d46f-487f-8719-0ea1a96b889a",
    "https://image.lexica.art/md/05f41068-fcbf-4927-86b6-fb95b1dbc591",
    "https://image.lexica.art/md/51730d10-5452-49c0-9bd0-60bb90ea6803",
    "https://image.lexica.art/md/6aa9d32f-5f43-4fcc-8daa-4715c605ca5d",
    "https://image.lexica.art/md/ea1c8652-ee91-4de7-8882-5954c6079911",
    // nature paints
    "https://image.lexica.art/md/4ae7fe6a-c156-4944-9a98-a9f785f5fd15",
    "https://image.lexica.art/md/731bc39c-215b-4d51-9757-983b39140325",
    "https://image.lexica.art/md/f85e265c-04b8-4a24-9ba9-9e7f3bdce72f",
    "https://image.lexica.art/md/09615937-1aee-4c1c-9310-798f9f227e58",
    "https://image.lexica.art/md/27458b38-a83e-4e68-9cc2-3f32dcdcda32",
    "https://image.lexica.art/md/4c4f0f9e-3cb7-4db3-b2bc-dfc764e14b58",
    "https://image.lexica.art/md/39d3ac7c-23b6-4911-aec8-77c50bc56c92",
    "https://image.lexica.art/md/eb8c102d-9e4a-4c4f-a768-c8760369e5db",
    "https://image.lexica.art/md/0ff04f79-ef0f-40f8-bde7-07a994bf1451",
    "https://image.lexica.art/md/3b454a37-0fe8-44a6-8d5b-18524d8b9b20",
    "https://image.lexica.art/md/3b454a37-0fe8-44a6-8d5b-18524d8b9b20",
    "https://image.lexica.art/md/e5d3e780-d1fc-44d1-b299-fd7dd9bb4e97",
    "https://image.lexica.art/md/35597b01-7c6b-425f-87d1-8eaa147cca20",
    "beautiful+jungle+landscape",
    "https://image.lexica.art/md/0edd4b00-13f8-4b19-aa1f-bdc684d19cf7",
    "https://image.lexica.art/md/7f3836b4-b7cd-444e-b34b-e8982fcaab74",
    "https://image.lexica.art/md/95e93561-2b8c-438a-bfbf-eb8dc1e7bb11",
    "https://image.lexica.art/md/e653bc87-b9fb-4325-a670-e421e756f2d3",
  
    "https://image.lexica.art/md/79578f19-5c41-4ff0-8b29-ad47be5f2d84",
    "Landscape Brazil",
    "Heavenly Places ",
    "A beautiful and highly detailed photo of the most epic lush mountains ever",
    "Single red maple tree growing in grand canyon",
    "a beautiful awesome artistic tree with flowers like leaves and many birds, all in the amazing outdoors view, mountain in the background",
    "a beautiful landscape, 8K, RTX REnder",

    "amazing landscape photo of mountains with lake in sunset by marc adamus, beautiful dramatic lighting",
    "Buddha Garden, RTX Render",
    "Dream Garden, night, Sci-fi",
    "Landscape Peacefull dynamic dramatic moody lighting",
    "viking stone dark age castle sitting by the seaside with rolling hills and a small village and a moat by eugene von guerard",
    "Landscape Mountains, Rivers, dramatic lighting, Rendered RTX",
    "A rocky mountain with a few patches of snow.",
    "A lush green forest with a few clearings and a river running through it.",
    "A tranquil landscape with a calm lake surrounded by trees, cinematic, 8k, RTX Render",
    "A world with dense forests, verdant fields, and abundant wildlife.",
    "A tranquil lake surrounded by mountains",
    "A starry night sky over a quiet lake",
    "A brightly lit skyline of a city at night, RTX Render, Modern, Cinematic",
    "Privacy Fence Landscaping",
    "skyscraper landscape vista",
];


function stableDiffusionGenerateRequest($prompt)
{
    $header = array(
        "content-type: application/json"
    );

 
    $fimages = [];



    $curl = curl_init();

    $jsArray = [
        "data" => [
            "prompt" => $prompt, 
            "iterations" => 7, 
            "steps" => 98, 
            "cfg_scale" => 7.5, 
            "threshold" => 0, 
            "perlin" => 0, 
            "height" => 512, 
            "width" => 512, 
            "sampler_name" => "k_lms", 
            "seamless" => false, 
            "progress_images" => false, 
            "variation_amount" => 0
        ]
    ]; 
    
    curl_setopt_array($curl, array(
      CURLOPT_URL => 'http://127.0.0.1:5643/inference',
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => '',
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 0,
      CURLOPT_FOLLOWLOCATION => true,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => 'POST',
      CURLOPT_POSTFIELDS =>json_encode($jsArray),
      CURLOPT_HTTPHEADER => array(
        'Content-Type: application/json'
      ),
    ));
    
    $response = curl_exec($curl);

    
    curl_close($curl);
    if($response){
        $response = json_decode($response);
    }

    return $response;

 
}


$promps = explode("\n", file_get_contents('prompt-extract.txt'));


foreach($promps as $prompt){
    $pRequest = trim($prompt);
    echo "Working On " . $pRequest . "\n";
    $generateRequest = stableDiffusionGenerateRequest($pRequest);

    print_r($generateRequest);
}