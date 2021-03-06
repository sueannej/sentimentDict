# sentimentDict
(A try for) A digital dictionary interface based on sentiment analysis

* * *

## 1. 서론
  언어 사전은 읽기 활동의 효율성, 생산성을 높이는 데 필수적인 도구다. 특히 국가의 장벽이 낮아지고 외국어 사전이 디지털화되면서 생산성은 더욱 중시되었다. 그러나 현재의 디지털화된 사전들은 단순히 오프라인의 자료를 온라인으로 옮긴 것에 불과하고, 여전히 정형화된 인터페이스를 벗어나지 못했다. 인터페이스 기술이 사용자와 환경에 맞추어 스스로 적응하도록 발전했음에도 불구하고, 사전은 여전히 문자(혹은 음성) 형태의 입력을 받아 해당하는 문자 형태의 데이터를 출력하는 데 머무르고 있는 것이다.
  
  사전이 보다 효율적, 생산적이기 위해서는 출력 방식의 개선이 필요하다. 현재, 단어의 뜻을 찾는 행동 패턴이 주로 읽기 활동 도중에 발생한다는 관찰 결과에 따라, 앱이나 브라우저 차원에서 클릭과 같은 단순한 방법만으로 사전 기능을 활성화하도록 입력 방식에 변화를 준 사례들은 있다. 하지만 입력 방식의 개선은 사전을 사용하는 활동에 관한 생산성은 증가시킬 수는 있지만, 사전을 사용하는 목적, 즉 단어를 학습하는 활동에 관한 생산성은 증가시키지 못한다. 다시 말해, 종이 사전을 사용하다 마우스를 클릭하는 것, 혹은 반대로 마우스를 클릭하다 종이 사전을 사용하는 등 사전을 사용하는 방법에 관련된 것은 경험과 훈련을 통해 쉽게 터득할 수 있지만, 어떤 단어의 뜻을 보았을 때 이를 얼마나 빠르고 쉽게 이해하는가는 학습 전략, 학습 능력과 관련 있기 때문에 학습자가 스스로 조절하기 어렵고 인터페이스 차원의 지원이 필요하다는 것이다.
  
  따라서 본 논문은 디지털 사전의 효율성과 생산성을 높이기 위해 출력 방식에 변화를 줄 방안을 제시한다. 첫째, 문자라는 하나의 모달리티가 아닌 두 개의 모달리티를 사용해야 한다. 둘째, 두 모달리티를 사용하기 위해 감정 분석 기술을 활용해야 한다. 이에 따라, 본 논문의 2절에서는 어떤 두 모달리티를 사용할 것인지, 왜 두 모달리티를 사용해야 하는지에 대해 설명하고, 3절에서는 두 모달리티를 혼용할 수 있는 기술적인 방안을 설명한다.

## 2. 두 가지 모달리티: 언어와 심상
  심리학자들은 생각이 두 개의 다른 과정을 통해 일어난다고 주장해왔다. 스타노비치와 웨스트는 이를 ‘시스템 1’과 ‘시스템 2’라고 칭했는데, 두 시스템은 카너먼과 이후경에 따라 아래와 같이 정리된다. 간단히 말해, ‘시스템 1’은 직관과 관련되어 빠르게 처리되는 시스템, ‘시스템 2’는 이성과 관련되어 천천히 처리되는 시스템이다.

#### 시스템 1
무의식적 추론, 암시적, 노력없이, 빠르게, 비언어적, 비논리적, 연상적, 맥락적, 결합적, 인식/직관, 경험적 의사결정
#### 시스템 2
의식적 추론, 명시적, 노력이 필요한, 천천히, 언어적, 논리적, 규칙적, 추상적, 연역적, 분석/이성, 분석적 의사결정

  이는, 언어적 정보와 비언어적 정보, 즉 언어와 심상이 이중으로 처리된다고 주장한 파이비오의 이중부호화모형(Dual Coding Approach)의 확장으로서, 본 논문은 이 이론들에 근거하여 언어와 심상을 디지털 사전의 두 모달리티로 선택하였다.
  
  즉, 본 논문은 학습자가 디지털 사전을 사용할 때 어휘(혹은 개념)에 따라 두 가지의 다른 이해 방식을 거칠 것이라는 가정에서 출발한다. 현재의 디지털 사전은 관련 정보를 문자 형태, 즉 언어적 방식으로만 출력하지만, 새로운 접근법은 어휘의 특성에 따라 언어적/비언어적인 두 가지 방식으로 관련 정보를 제공하는 것이다. 그러면, 어휘의 특성을 반영하여 두 모달리티를 효과적으로 사용할 방법을 다음 절에서 다루겠다.
  
## 하고, 3. 방법, 부분을 쓰다 그만둠...,,,,...,,.,,.,.. ㅠ^ㅠ

## 참고자료
* 이후경, 2014. 선택의 함정.
* Kahneman, D., 2013. Thinking, fast and slow / Daniel Kahneman. 1st pbk., New York: Farrar, Straus and Giroux. 
* Stanovich, K.E. & West, R.F., 2000. Individual differences in reasoning: Implications for the rationality debate? Behavioral and Brain Sciences, 23(5), pp.645–665.
* Paivio, A., 1986. Mental representations ; a dual coding approach / Allan Paivio., Oxford: Oxford Univ. Press.

* 한국어 감정 분석
  * http://hosting02.snu.ac.kr/~snucss/wp-content/uploads/2016/04/11.11_신효필교수.pdf
  * https://github.com/mrlee23/KoreanSentimentAnalyzer
  * http://word.snu.ac.kr/kosac/lexicon.php
* Sentiment Analysis
  * http://text-processing.com/demo/sentiment/, http://text-processing.com/docs/sentiment.html
* SentiWordNet
  * http://www.lifebloom.biz/2017/07/29/python을-활용한-텍스트-마이닝-8-텍스트-분석-감성-분석sentiment-ana/
* Curl
  * https://curl.trillworks.com
* Oxford Dictionaries API
  * https://developer.oxforddictionaries.com/documentation
