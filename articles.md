# ARTICLE 1: The Importance of Guardrails for Secure and Responsible AI Applications
[Read More](https://www.3pillarglobal.com/insights/blog/importance-of-guardrails-for-secure-and-responsible-ai-applications/)
--------------------------------------------------

The Importance of Guardrails for Secure and Responsible AI Applications
=======================================================================

January 13, 2025

Artificial Intelligence (AI) and Large Language Models (LLMs) are reshaping industries by enabling smarter, more intuitive interactions with technology. However, with great power comes great responsibility. Without appropriate safeguards, these applications can produce unpredictable outputs, leak sensitive information, or even amplify harmful content. This is where **guardrails** come into play.

Guardrails are an essential layer of defense, ensuring AI systems remain safe, reliable, and aligned with ethical guidelines. They not only enhance security but also optimize performance, enabling organizations to strike the right balance between innovation and risk mitigation.

What Are Guardrails in AI?
--------------------------

In AI applications, guardrails refer to a collection of frameworks, processes, and tools designed to monitor and regulate system behavior. These mechanisms proactively prevent unintended or harmful outcomes by:

* Blocking malicious or inappropriate inputs.
* Filtering harmful or false outputs.
* Detecting vulnerabilities, such as prompt injections or hallucinations.
* Protecting sensitive or proprietary data from leaks.

Guardrails are especially critical for LLM-powered applications, such as chatbots and virtual assistants, where user trust is paramount. They ensure that while AI delivers accurate, efficient, and innovative responses, it also remains secure, ethical, and compliant.

The Many Forms of Guardrails
----------------------------

Not all guardrails are created equal, and their effectiveness depends on the application’s specific needs. Below are the primary types of guardrails and their unique advantages:

### Rule-Based String Manipulation

The simplest and fastest method, rule-based guardrails rely on predefined criteria, such as regular expressions or keyword lists, to block or validate content. For example, a profanity filter might block offensive language, while a format validator ensures inputs meet specific structural requirements. Though straightforward, this approach is limited in handling nuanced or context-dependent issues.

### LLM-Based Metrics

These guardrails leverage LLMs themselves to assess the coherence, relevance, or alignment of inputs and outputs. Metrics like perplexity (measuring word coherence) or alignment scores (ensuring outputs match guidelines) help detect deeper semantic issues. This approach is ideal for applications requiring a sophisticated understanding of language patterns but may involve higher latency.

### LLM Judges

More advanced than metrics, LLM judges are models specifically trained to assess and validate content. They can identify toxic language, verify factual accuracy, or evaluate responses against specific criteria. While powerful, their reliance on multiple LLM calls can increase latency and costs.

### Prompt Engineering and Chain-of-Thought Techniques

By designing prompts that guide the AI’s behavior, developers can reduce the likelihood of generating harmful or irrelevant content. For example, prompts can instruct the model to avoid answering personal or inappropriate questions. Chain-of-thought (CoT) techniques further enhance precision by structuring prompts with step-by-step instructions and examples.

Popular Guardrail Tools and Frameworks
--------------------------------------

The growing need for robust guardrails has spurred the development of tools and frameworks. Here are some leading solutions:

* **Aporia**: A real-time platform for mitigating LLM hallucinations, inappropriate responses, and prompt injections, complete with pre-made policies and dashboards.
* **NeMo Guardrails**: An open-source toolkit by NVIDIA, offering customizable input, dialog, and output safeguards.
* **Guardrails AI**: A flexible Python framework for validating inputs and outputs, enabling tailored guardrails for any AI application.
* **Azure Guardrails**: Microsoft Azure’s built-in safety features, providing prompt injection shields, sensitive data filters, and groundedness detection.

These tools simplify the implementation of guardrails, enabling developers to focus on creating impactful applications without compromising safety.

Addressing Critical AI Security Challenges
------------------------------------------

According to the Open Worldwide Application Security Project (OWASP), AI systems face unique vulnerabilities. Here is how guardrails provide essential protection against some of the risks pointed out by OWASP’s security study:

### Prompt Injection

Prevent attackers from injecting harmful instructions into AI inputs using prompt injection shields. These guardrails block malicious user prompts before they reach the AI model.

### Insecure Output Handling

Guardrails can validate outputs to ensure they don’t trigger unsafe downstream processes, such as unauthorized database queries or code execution.

### Sensitive Information Disclosure

Filters are able to detect and redact personal or proprietary information from AI responses, ensuring compliance with privacy regulations.

### Misinformation

Hallucination detectors validate the factual accuracy of outputs by cross-referencing trusted data sources, reducing the risk of misinformation.

### Excessive Agency

Guardrails can be made to limit the scope of actions AI can take autonomously, preventing unintended consequences due to excessive permissions or autonomy.

By addressing these challenges, guardrails ensure AI applications remain secure and trustworthy.

Why One Size Does Not Fit All
-----------------------------

The “ideal” set of guardrails depends on several factors, including application type, user expectations, and budget constraints. For instance:

* Real-time chatbots require faster, rule-based solutions to minimize latency.
* Applications processing sensitive data may prioritize advanced LLM-based safeguards.
* Organizations with limited budgets might adopt open-source frameworks like Guardrails AI or NeMo.

Moreover, asynchronous guardrails—where validation occurs parallel to output delivery—can enhance speed without sacrificing security. This flexibility allows organizations to customize their approach, ensuring guardrails align with their unique objectives.

Conclusion: Responsible AI Starts With Guardrails
-------------------------------------------------

As AI continues to transform industries, guardrails are no longer optional—they’re a necessity. These safeguards not only protect users and organizations from risks but also reinforce trust, paving the way for more responsible AI adoption.

By integrating the right combination of rule-based, AI-powered, and engineered safeguards, developers can build applications that are secure, ethical, and effective. The journey toward responsible AI begins with the right guardrails in place.

If you would like to explore how our Innovation Lab can help you implement effective AI guardrails, don’t hesitate to [reach out](https://www.3pillarglobal.com/contact-us/). Our team is here to guide you in building secure, ethical, and high-performing AI solutions.

About the author
----------------

![Jakub Mlady](https://www.3pillarglobal.com/wp-content/uploads/2025/01/jakub-mlady.jpg)

### Jakub Mlady

Senior Software Engineer

[Read bio](https://www.3pillarglobal.com/leadership/jakub-mlady/)

==================================================

# ARTICLE 2: A GenAI Playbook for Healthcare Leaders
[Read More](https://www.3pillarglobal.com/insights/blog/a-genai-playbook-for-healthcare-leaders/)
--------------------------------------------------

A GenAI Playbook for Healthcare Leaders
=======================================

September 25, 2024

Healthcare organizations are rapidly moving forward with AI. The technology is opening up possibilities to improve operations, increase business efficiency and profitability, and drive better patient outcomes.

[According to Gartner](https://www.gartner.com/en/documents/5150331), 79% of US healthcare payers indicate that they have started, or will start within the next two years, formal use-case assessments and copilot solutions from enterprise vendors to bring GenAI capabilities into the organization. [Another survey](https://www.gartner.com/en/documents/5176063) shows a striking majority of healthcare organizations (78%) are formally assessing use cases, while 66% are developing the ethics and policies for appropriate use and 47% are funding initiatives.

If you’re not planning on implementing AI, you’re already falling behind. This playbook for healthcare leaders will help you know what to ask your CIO/CTO, which criteria to use to decide on use cases, and how to prepare for success with GenAI.

Getting Past the GenAI Hurdles
------------------------------

While AI brings many advantages, some healthcare leaders are hesitant to implement the technology due to some of the technical challenges. Accuracy and reliability can be difficult; you’ll have to stop hallucinations and make sure your AI is grabbing data from the right places. If you’ll be deploying AI widely, it needs to be done carefully so it doesn’t run up high expenses. Additionally, data privacy—both for your organization and for patients—has to be a priority.

You know you’re ready to implement GenAI when you’re ready to address those challenges. We wrote about how to understand and avoid those pitfalls in [this blog pos](https://www.3pillarglobal.com/insights/blog/genai-in-healthcare-how-to-stop-hallucinations-scale-cost-effectively-and-protect-patient-data/)t. If you solidly understand how to navigate those hurdles and you’re ready to build, here’s what to do next.

### Step 1: Identifying Use Cases

While GenAI is a useful tool for accelerating business, it’s not a comprehensive solution that will magically solve all your company’s problems. Its greatest impact comes from combining it with other technologies and user interfaces. To make sure you’re getting the most value out of your GenAI, be sure to prepare your organization by identifying use cases ahead of time. GenAI is well suited for use cases such as:

* **Content generation.** GenAI has a particular strength in content generation. Use GenAI to create personalized member communications and to take notes and summaries of previous member interactions. You can also use it as an ambient digital scribe for call service reps and care management specialists.
* **Discovery.** Healthcare leaders can use GenAI to help members find care and services in their area based on their unique needs. Members can compare different plan options to find the plan that’s best for them. Member onboarding and services enrollment is also an area where GenAI is beneficial as it helps members discover your offerings. If you need to consult medical processes, understand eligibility data, and see if prior authorization is required, GenAI can help.
* **Decision making.** If healthcare leaders or patients have questions, decision-making GenAI can provide answers. Healthcare companies can use GenAI to schedule appointments on behalf of members and see available appointment times, create member-friendly EOBs and provider bill audits, refill prescriptions, transfer data between healthcare providers, and provide information to help members make decisions based on their unique situations.
* **Data extraction + summary.** Use GenAI for member chatbots to answer member questions, explain plan details and ancillary benefits, give you insights into plan usage, and perform data analysis and reporting on plan and member insights.

### Step 2: Assess Use Cases

Once you’ve identified possible use cases for your organization, you can assess the use cases to see which ones would be most easily implemented and which ones would provide the greatest value. Healthcare leaders can evaluate each proposed use case against the following criteria to select the most impactful use cases.

One major consideration for use cases is technical feasibility. The use case needs to be compatible with your organization’s existing data architecture and systems. You’ll also need to understand how implementing this use case of GenAI would impact your existing operations and how products and product features could potentially be affected.

As you’re doing your due diligence on potential use cases, you’ll also want to consider speed to value. How quickly can you stand up this particular use case? How much labor and money—both up-front and over time—would it take for this use case to start providing value? Similar to speed and value, you’ll also want to consider return on investment. Each potential use case should have an estimated ROI and an approximate timeline of when the use case would start realizing that ROI.

Your assessment criteria should also include an analysis of how this use case would fit into a broader AI strategy. Certain use cases of GenAI may be a good idea but may not fit with the organization’s broader AI and corporate strategy. Healthcare companies need to be especially aware of data privacy and other risk factors that may need to be addressed as part of their AI strategy.

### Step 3: Evaluate Technical Approaches

You’ll need to evaluate the technical approach to your use case carefully, because it could impact the cost, accuracy, and effectiveness of your project. Work with your CTO to consider some of the following technical components:

* Language Processing Units (LPUs)
  + How are we selecting the LPUs with the right capabilities while controlling run-time costs?
  + What strategies will we employ to handle complex processing tasks such as planning, reasoning, and agentic behavior?
* Orchestration
  + How will we integrate and manage the workflow for various components within the AI application system?
  + How do we build the AI application so you can swap in different components to evolve AI capabilities?
* Memory
  + How do we build conversational memory across multiple member interactions and other domain-specific knowledge bases so the AI applications become increasingly personalized and useful?
* Infrastructure
  + What deployment infrastructure is needed to ensure scalable and reliable application management?
  + How can observability tools be leveraged to monitor and maintain the performance of our AI system?
* Data Engineering
  + Is our data ready to support the AI model and consumption? What additional data acquisition, integration, and transformation is needed?
  + How do we design robust data pipelines and fine-tuning mechanisms to support the AI system?
* Services + Tools
  + What enterprise systems and productivity tools need to be integrated with the AI application to create a bi-directional feedback loop?
  + What project management and optimization services do we need to ensure comprehensive support and enhancement of the AI platform?
* Security + Compliance
  + What security measures are necessary to protect sensitive data processed by the AI system?
  + How will we ensure the AI platform complies with relevant regulatory standards and legal requirements?

Getting Expert Guidance on GenAI Implementation
-----------------------------------------------

How do you know how much up-front investment it would take to implement GenAI? What GenAI options are compatible with your existing data architecture? As you consider questions and use cases related to implementing GenAI, 3Pillar can help. To get tailored support as you find the most profitable use cases and identify the projects with the fastest speed to value, [contact us today.](https://www.3pillarglobal.com/contact-us/)

==================================================

# ARTICLE 3: GenAI in Healthcare: How to Stop Hallucinations, Scale Cost Effectively, and Protect Patient Data
[Read More](https://www.3pillarglobal.com/insights/blog/genai-in-healthcare-how-to-stop-hallucinations-scale-cost-effectively-and-protect-patient-data/)
--------------------------------------------------

GenAI in Healthcare: How to Stop Hallucinations, Scale Cost Effectively, and Protect Patient Data
=================================================================================================

September 23, 2024

Healthcare providers and payers alike have explored GenAI’s applications to improve efficiency and enhance patient care. In a recent [Gartner survey](https://www.gartner.com/account/signin?method=initialize&TARGET=http%3A%2F%2Fwww.gartner.com%2Fdocument%2F5176063), 80% of health system CIOs indicated they’re actively exploring AI use cases. The rate for payers is comparable.

Providers, no stranger to using advanced technology, have used GenAI to improve clinical documentation, brought efficiency to patient messaging, and [leveled up revenue cycle management](https://www.3pillarglobal.com/insights/whitepapers-ebooks/the-revenue-cycle-playbook-7-opportunities-to-modernize-the-healthcare-payment-ecosystem/). Payers have reported success with real-time [prior authorizations](https://www.3pillarglobal.com/insights/blog/key-takeaways-from-modern-healthcares-digital-innovation-summit/) and offering [personalized assistance via chatbots.](https://www.3pillarglobal.com/insights/blog/creating-member-centric-chatbots/) Beyond introducing AI for specific products, contexts, and workflows, business leaders are also deploying AI enterprise-wide to help employees perform at a higher level.

However, this adoption doesn’t come without a cost. Stakeholders are increasingly worried about concerns related to hallucinations, costs, and data protection. With that in mind, I recently hosted 3Pillar’s Chief Innovation Officer, Pankaj Chawla, and Director of Global Innovation, David Evans on the podcast.

[This episode](https://podcasts.apple.com/us/podcast/214-a-generative-ai-primer-for-healthcare-business-leaders/id814135639?i=1000668145039) is a primer on GenAI for healthcare business leaders. We explored questions healthcare leaders like yourself might have as you consider where and how to deploy GenAI in your organization. For instance:

* How do you guard against hallucinations?
* Is GenAI too expensive to scale across your organization?
* How do you protect patient and company data?

We addressed these considerations and more. Following is a summary of their comments and a roadmap for future action around GenAI in healthcare:

Data Accuracy: Avoiding Hallucinations
--------------------------------------

Large language models, the engines behind AI writ large, are trained on data at scale. However, this data can produce inaccurate outputs, also known as hallucinations. These models are trained on a predictive basis, meaning they anticipate the next best word or phrase to complete the thought, paragraph, or document. What can follow is called “drift,’ meaning the language model will produce responses that seem plausible but aren’t accurate. Naturally, this raises concerns about whether using AI at scale is practical or useful.

Feeding the large language model with trusted data sources like fee schedules or procedure code ontologies can offer assurance that the AI will base its answers on facts.

By augmenting the AI system with curated data sources, we can have peace of mind knowing the generated responses are reliable and trustworthy. Instead of relying solely on the model’s ability to predict the next best word or phrase, we provide it with inputs that directly relate to the question at hand.

For example, when determining whether an urgent care facility is in-network, the AI should rely on a dataset containing information about the payer’s network. By incorporating this data, we can avoid hallucinations and provide accurate, informative responses.

[3Pillars’ Innovation Lab](https://www.3pillarglobal.com/why-3pillar/innovation-lab/) has developed a framework for measuring response quality. This assessment evaluates noise levels and verbosity to ensure the AI application delivers clear and concise responses grounded in accuracy.

Scaling Cost Effectively
------------------------

The cost of implementing GenAI solutions is a valid concern for decision-makers. Pankaj likens the current state of affairs to the early days of cloud services: Cloud providers are now offering GenAI as a service, similar to how they provide cloud storage or computing power. While the initial cost might be daunting, the long-term benefits of improved efficiency and productivity can make the case for the investment.

David emphasizes cost optimization strategies:

**Targeted Audiences:** Determine the specific user cohorts that will benefit most from GenAI applications. Avoid deploying solutions across the entire organization if unnecessary.

**Internal Hosting:**  Consider hosting large language models internally to gain more control over costs. Experiment with different models for various use cases. With such infrastructure in place, you can experiment with different AI models to find the best match for specific use cases. This allows you to control costs by avoiding the use of overly powerful models for tasks that do not require them.

**Model Flexibility:** Design your AI application to allow for easy switching between different large language models based on their performance and cost.

Protecting Patient and Enterprise Data
--------------------------------------

The recent uptick in healthcare data breaches, like [Change Healthcare](https://www.hhs.gov/hipaa/for-professionals/special-topics/change-healthcare-cybersecurity-incident-frequently-asked-questions/index.html), has highlighted the critical importance of protecting user and enterprise data. This is only exacerbated by the fact that healthcare organizations are increasingly adopting AI technologies to improve patient care and drive efficiency. At the same time, protecting sensitive patient information should be at the forefront but that’s not necessarily a given.

One of the primary concerns is the potential misuse of patient data to train AI models. There is a risk that confidential information could be inadvertently shared with other parties or used to develop AI applications that could compromise patient privacy. For example, a healthcare organization might use Gemini to analyze patient data, only to find that the model has inadvertently learned sensitive details that could end up in the wrong hands. Not to mention different language processing units (LPUs) have different licensing agreements about whether your data will help train their model.

All of this to say: The sensitive nature of patient data necessitates robust security measures. Our design separates data concerns from language processing. Similar to secure cloud applications, we create private data lakes within walled gardens with firewalls for each client. This ensures patient data remains secure while leveraging the power of GenAI.

Deploy GenAI at Scale with 3Pillar
----------------------------------

When evaluating a potential vendor, it’s crucial to carefully review the terms and conditions of the service provider. While some explicitly state that they will not use your data for training purposes, others may reserve the right to do so. Be intentional about opting out of data usage if desired and be mindful of the potential risks associated with accessing these models through the internet.

We’re actively collaborating with healthcare organizations to help them implement GenAI solutions. Our Platform in a Box tool enables rapid deployment of AI technology, making it easy for organizations to explore various use cases. If you’re interested in learning more, please [contact us.](https://www.3pillarglobal.com/contact-us/)

==================================================

# ARTICLE 4: 3Pillar Announces New Innovation Hub to Drive Market-Leading Digital Product Engineering and AI Transformation Advancements
[Read More](https://www.3pillarglobal.com/news/3pillar-announces-new-innovation-hub/)
--------------------------------------------------

3Pillar Announces New Innovation Hub to Drive Market-Leading Digital Product Engineering and AI Transformation Advancements
===========================================================================================================================

September 17, 2024

[News](/news/?type=news), [Press Release](/news/?type=press-release)

*3Pillar’s Chief Innovation Officer Pankaj Chawla to Lead Global Innovation-at-Scale Initiatives*

**FAIRFAX, Va., September 17, 2024** – [3Pillar](https://www.3pillarglobal.com/), a leading modern application strategy, design and engineering firm, today announced its intention to build a new Innovation Hub in India aimed at expanding its expertise at the intersection of product engineering and cognitive computing. 3Pillar’s Chief Innovation Officer, Pankaj Chawla, will relocate to India to lead the Innovation Hub and direct other key global initiatives. This senior executive presence in India highlights 3Pillar’s dedication to aligning our global expertise with the needs of our clients, ensuring they benefit from cutting-edge talent and solutions.

Chawla will focus on key initiatives including:

* **Innovation Hub:** Expanding on the success of 3Pillar’s US Innovation Lab, the new Innovation Hub in 3Pillar’s Noida, India office will serve as an incubator, demonstrating the company’s proven expertise and providing clients with access to advanced technologies and expert teams skilled in fostering a culture of experimentation and innovation.
* **Deeper Client Engagement:** Strengthening client relationships by offering a unique opportunity to co-innovate directly with the 3Pillar Innovation team in a state-of-the-art facility that accelerates ideas from visionary concepts to market-ready ideas.
* **Emerging-Technology Capability & Asset Development:** Building solutions that empower clients to navigate today’s pressing digital and AI product development challenges.

“This move represents a unique opportunity to immerse myself in one of the most dynamic technology environments in the world and leverage my two plus decades of experience and expertise in expanding 3Pillar’s global innovation on behalf of its clients,” said Chawla. “I’m excited to work with our talented teams in the India and Eastern Europe regions to drive initiatives that will take 3Pillar’s clients’ businesses to new heights.”

**Helping Clients Make the Most of AI and Digital Transformation Investments**

3Pillar has a proud history of pioneering cutting-edge technology innovation, working to ensure the AI and digital transformation solutions they develop have immediate, tangible business impact for clients. Some of these innovations include:

* 3Pillar’s [Healthcare AI chatbot](https://www.3pillarglobal.com/why-3pillar/innovation-lab/healthcare-payer-chatbot/), trained on payer data to deliver price transparency to patients even before they enter a doctor’s office.
* 3Pillar NEXUS, a proprietary GenAI Application Platform, which offers a quickstart infrastructure for multiple LLMs, routing and private datasets that can be set up in minutes for a rapid GenAI application development and deployment.
* An IIOT Platform using 100K+ sensors powered by AI and machine learning for a client in the nuclear power industry with 40 reactors across 10+ sites to reduce operating and maintenance costs as well as improve performance.
* 3Pillar’s software archeology asset that allows clients to understand legacy code structure, and logic, create diagrams and documentation, and identify areas to refactor, improve and modernize their applications.
* Automated DevOps & testing tooling based on 3Pillar’s proprietary frameworks that allows for enhanced scalability in modernizing existing client processes and quickly delivering on new releases to compete effectively.

The new Innovation Hub will allow the 3Pillar team to showcase the company’s skills and host clients to collaborate on and build new solutions to solve their most pressing challenges. Building off 3Pillar’s deep history in product and data engineering, this next chapter will allow the company to aid modern businesses in their digital and AI transformation journeys.

“Our decision to have Pankaj lead from India is a testament to our commitment to our clients through global excellence and innovation,” said Mike Detwiler, CEO of 3Pillar. “By being located in India, Pankaj will be at the forefront of our efforts to foster innovation, create new capabilities, streamline operations, and expand our global footprint in the region – all in service of delivering significant benefits to our clients and stakeholders.”

**About 3Pillar**

At 3Pillar, we believe something truly incredible happens at the intersection of product engineering and cognitive computing. As the leading modern application strategy, design and engineering firm, 3Pillar brings unrivaled expertise that enables clients to execute the mission-critical software development initiatives needed to compete in the digital economy. Our global team doesn’t just develop software—we help clients set bold ideas into motion and accelerate innovation. 3Pillar supports its clients with offices across North America, Europe, Asia, and Latin America. Learn more at [www.3pillarglobal.com](http://www.3pillarglobal.com/).

**Media Contact:**

Shannon Brown  
508-277-0700  
[sbrown@wearetierone.com](mailto:sbrown@wearetierone.com)

==================================================

# ARTICLE 5: Trends in Digital Health: Headwinds and Opportunities to Reinvigorate Chronic Condition Management Through TEFCA and GenAI
[Read More](https://www.3pillarglobal.com/insights/blog/trends-in-digital-health-headwinds-and-opportunities-to-reinvigorate-chronic-condition-management-through-tefca-and-genai/)
--------------------------------------------------

Trends in Digital Health: Headwinds and Opportunities to Reinvigorate Chronic Condition Management Through TEFCA and GenAI
==========================================================================================================================

September 13, 2024

The 2010s experienced an explosion of digital health solutions. By 2021, [health management apps accounted for 47% of all apps in 2021](https://mindsea.com/health-apps/)—a sharp increase from 28% in 2015. The vision that many of the products’ creators had was for a companion app that could provide education and constant support and would be cheaper and more effective than going repeatedly to physicians.

Some of the popular products included:

* Livongo for diabetes
* Propeller for asthma
* Noom for weight loss
* Omada for hypertension
* Cricket Health for care of kidney disease (CKD)

These products had a lot in common. They were usually point solutions on a single condition. They tended to focus on education and tracking, and they catered to large employers as a complement to enterprise wellness programs and insurance benefits. Now, another trait they share is that they’re not working.

Why Digital Health for Chronic Conditions is Consolidating
----------------------------------------------------------

While there were a lot of innovative ideas that came with digital health management for chronic conditions, the industry had flaws. The space is now collapsing on two levels.

### HR and Employer Burnout

The first front where telehealth is experiencing challenges is employer burnout. For the past decade, many chronic condition management solutions sold to the market by going directly to employers. The HR leaders or employers who made purchasing essentially become mini health plan executives. In addition to their many other duties, they decided which digital solutions to roll out to their employees. Now a[round 81% of HR leaders are feeling burnout](https://www.sage.com/en-us/-/media/files/sagedotcom/master/documents/pdf/sage%20people/changing-face-of-hr-report-2024-fact-sheet-top-findings.pdf) and don’t have extra energy to do deep research on which digital health programs work best. While these leaders are often talented and capable, they don’t usually have a clinical health background to make optimal decisions about healthcare on an enterprise level.

When we look at what HR leaders want, we’re seeing the pendulum swing from customized detail back toward simplicity. They’re looking for simplicity of employee usage, simplicity of product administration, and simplicity of product pricing. The multitude of products and their complicated pricing structures are too disparate and complicated for HR leaders to wedge into their existing plans. Especially if the solution is only for a single condition, HR probably won’t deem it worth the time. Christina Farr has an [excellent article](https://secondopinion.media/p/point-solution-fatigue-real) that explains why HR leaders are feeling acute point-solution fatigue when it comes to health-tech solutions.

From a trend perspective, the era of the point solution is over. The majority of companies in the chronic condition and wellness spaces are consolidating into a few big players. There used to be many different companies each offering a point solution; now, there are fewer companies, but they are offering management for multiple chronic conditions. Now, the era of the chronic condition management platform is here. When it comes to regional payers, HR leaders’ and employers’ [new expectation](https://www.3pillarglobal.com/insights/blog/navigating-change-how-regional-payers-stay-ahead/) is that insurance companies act as their single platform partner, providing optionality for bespoke offerings for multiple chronic conditions, not just one, while shouldering the burden of complexity.

Additionally, big players are starting to have their own homegrown or white-labeled programs. For example, United Healthcare’s clinical and disease management support programs or Aetna’s chronic disease management program. This fits in with the trend mentioned above with HR leaders experiencing burnout: HR leaders want to collapse vendors and work with fewer companies. A single vendor across chronic condition management is much easier for HR leaders to manage.

### Education and Tracking Aren’t Enough

The second level where the telehealth and chronic condition space is consolidating is in functionality. Pure-play digital health didn’t work. The model of “educate users and track data” wasn’t enough; patients needed more nuanced support. Many apps don’t effectively measure usage, and [patients may not correctly interpret results](https://www.sciencedirect.com/science/article/abs/pii/S221188372400011X). If a patient needs medication or needs dosage adjustments, an app focused purely on education and tracking can’t help.

Many of the digital health products oversimplified treatment for chronic health conditions into a small checklist of educational modules and data tracking. To remedy the issues and bring up compliance rates, products in this space started offering expanded services beyond education and tracking to include elements such as:

* Social influencing
* Rewards
* Health coaches
* Wearables
* RNs who can do telehealth

Basically, digital health platforms have started turning into a medical practice that’s tech-enabled rather than software that’s supporting health services. At 3Pillar, we speculate that the services that digital health apps and traditional doctors’ offices will converge at a similar end-state. The most effective combination of services to help patients manage chronic conditions with digital health support needs to include human connections, a qualified physician, digital education, and habit tracking all together.

### The Future of Digital Health Management

Another trend that’s already shaping the future of digital health management is the Trusted Exchange Framework and Common Agreement (TEFCA). TEFCA is a set of terms outlined by the US government that helps facilitate the sharing of patient information between entities. For example, TEFCA legislation facilitates data-sharing between doctors’ offices and insurance companies. Previously, you had to be a physician directly providing care to access patient health information. Now, with TEFCA, more entities can access patient data (as long as they have patient permission).

This means that health apps and health insurance companies can get raw clinical data from health systems. The next-gen chronic condition management platforms could be able to access patients’ blood work labs and medical history.

“Companies have had a reactive approach to digital health apps. For example, if a health insurance company offers a diabetes management program, a user might not know about it. However, the company also doesn’t know that the user has diabetes. Halfway through the year, the company sees a bill from an endocrinologist, diagnosing the patient with diabetes. Only then are insurance companies directly reaching out to patients about the diabetes management program,” said Steve Rowe, Industry Leader, Healthcare Portfolio at 3Pillar. “TEFCA could change that and enable health insurance companies to be proactive about offering support to patient groups, saving money for both the company and the patient.”

In addition to TEFCA, another factor that will shape the future of digital health is AI. As AI continues to change the way companies work, a chatbot could be foundational to the future of chronic condition management. A chatbot could suggest and remind employees about digital health apps that are available or relevant to them that are covered by health insurance. To complement TEFCA data access, digital health apps could use AI to summarize a patient’s clinical notes and pull out relevant data to customize the app flow to a person’s individual needs.

3Pillar sees developments in AI and TEFCA regulations reviving digital health platforms for chronic condition management, both in terms of adoption as well as compliance.

How to Future-Proof Your Digital Health Products
------------------------------------------------

At 3Pillar, we help healthcare clients manage, plan for, and optimize their digital healthcare solutions. To work through challenges you’re currently facing as well as future-proofing your business, work with 3Pillar. We offer application technology strategy, digital product engineering, and AI implementation guidance specifically for the healthcare industry. To learn more about how we can build a future for your platform, [contact us today](https://www.3pillarglobal.com/contact-us/).

==================================================

