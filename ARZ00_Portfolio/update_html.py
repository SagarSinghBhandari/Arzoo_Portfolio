import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Replace Skills Section
skills_new = """        <!--=============== SKILLS ===============-->
        <section class="skills section" id="skills">
            <span class="section__subtitle">My Abilities</span>
            <h2 class="section__title">My Skills</h2>

            <div class="skills__container container grid">
                <div class="skills__content">
                    <h3 class="skills__title">Languages & Core CS</h3>

                    <div class="skills__box">
                        <div class="skills__group">
                            <div class="skills__data">
                                <i class='bx bxs-badge-check'></i>

                                <div>
                                    <h3 class="skills__name">C++ & Java</h3>
                                    <span class="skills__level">Advanced</span>
                                </div>
                            </div>

                            <div class="skills__data">
                                <i class='bx bxs-badge-check'></i>

                                <div>
                                    <h3 class="skills__name">Python</h3>
                                    <span class="skills__level">Advanced</span>
                                </div>
                            </div>

                            <div class="skills__data">
                                <i class='bx bxs-badge-check'></i>

                                <div>
                                    <h3 class="skills__name">JavaScript</h3>
                                    <span class="skills__level">Advanced</span>
                                </div>
                            </div>

                        </div>
                        <div class="skills__group">
                            <div class="skills__data">
                                <i class='bx bxs-badge-check'></i>

                                <div>
                                    <h3 class="skills__name">DSA</h3>
                                    <span class="skills__level">Advanced</span>
                                </div>
                            </div>

                            <div class="skills__data">
                                <i class='bx bxs-badge-check'></i>

                                <div>
                                    <h3 class="skills__name">OS & DBMS</h3>
                                    <span class="skills__level">Intermediate</span>
                                </div>
                            </div>

                            <div class="skills__data">
                                <i class='bx bxs-badge-check'></i>

                                <div>
                                    <h3 class="skills__name">Networks</h3>
                                    <span class="skills__level">Intermediate</span>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>

                <div class="skills__content">
                    <h3 class="skills__title">Big Data & Backend</h3>

                    <div class="skills__box">
                        <div class="skills__group">
                            <div class="skills__data">
                                <i class='bx bxs-badge-check'></i>

                                <div>
                                    <h3 class="skills__name">Hadoop</h3>
                                    <span class="skills__level">Intermediate</span>
                                </div>
                            </div>

                            <div class="skills__data">
                                <i class='bx bxs-badge-check'></i>

                                <div>
                                    <h3 class="skills__name">PySpark</h3>
                                    <span class="skills__level">Intermediate</span>
                                </div>
                            </div>

                            <div class="skills__data">
                                <i class='bx bxs-badge-check'></i>

                                <div>
                                    <h3 class="skills__name">SQL / NoSQL</h3>
                                    <span class="skills__level">Advanced</span>
                                </div>
                            </div>

                        </div>
                        <div class="skills__group">
                            <div class="skills__data">
                                <i class='bx bxs-badge-check'></i>

                                <div>
                                    <h3 class="skills__name">Node.js</h3>
                                    <span class="skills__level">Advanced</span>
                                </div>
                            </div>

                            <div class="skills__data">
                                <i class='bx bxs-badge-check'></i>

                                <div>
                                    <h3 class="skills__name">FastAPI</h3>
                                    <span class="skills__level">Intermediate</span>
                                </div>
                            </div>

                            <div class="skills__data">
                                <i class='bx bxs-badge-check'></i>

                                <div>
                                    <h3 class="skills__name">Docker</h3>
                                    <span class="skills__level">Intermediate</span>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </section>

"""
html = re.sub(r'<!--=============== SKILLS ===============-->.*?<!--=============== SERVICES ===============-->', skills_new + '        <!--=============== SERVICES ===============-->', html, flags=re.DOTALL)

# 2. Replace Services Section
services_new = """        <!--=============== SERVICES ===============-->
        <section class="services section">
            <span class="section__subtitle">My Domains</span>
            <h2 class="section__title">What I Offer</h2>

            <div class="services__container container grid">
                <div class="services__card">
                    <div class="serv">
                        <h3 class="services__title">Software <br> Development</h3>

                        <span class="services__button">
                            See More <i class='bx bx-right-arrow services__icon'></i>
                        </span>
                    </div>

                    <div class="services__modal">
                        <div class="services__modal-content">
                            <i class='bx bx-x services__modal-close'></i>

                            <h3 class="services__modal-title">Software Development</h3>

                            <p class="services__modal-description">
                                Delivering robust applications and algorithms with a strong focus on clean code and performance.
                            </p>

                            <ul class="services__modal-list">
                                <li class="services__modal-item">
                                    <i class='bx bx-check-circle'></i>
                                    <p class="services__modal-info">Optimized algorithmic solutions in C++ & Java.</p>
                                </li>
                                <li class="services__modal-item">
                                    <i class='bx bx-check-circle'></i>
                                    <p class="services__modal-info">Full-stack web application development.</p>
                                </li>
                                <li class="services__modal-item">
                                    <i class='bx bx-check-circle'></i>
                                    <p class="services__modal-info">System orchestration and containerization.</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="services__card">
                    <h3 class="services__title">Data <br> Engineering</h3>

                    <span class="services__button">
                        See More <i class='bx bx-right-arrow services__icon'></i>
                    </span>

                    <div class="services__modal">
                        <div class="services__modal-content">
                            <i class='bx bx-x services__modal-close'></i>

                            <h3 class="services__modal-title">Data Engineering</h3>

                            <p class="services__modal-description">
                                Processing large-scale datasets using distributed pipelines to uncover actionable insights.
                            </p>

                            <ul class="services__modal-list">
                                <li class="services__modal-item">
                                    <i class='bx bx-check-circle'></i>
                                    <p class="services__modal-info">Hadoop & Spark distributed architectures.</p>
                                </li>
                                <li class="services__modal-item">
                                    <i class='bx bx-check-circle'></i>
                                    <p class="services__modal-info">SQL Analytics and complex aggregations.</p>
                                </li>
                                <li class="services__modal-item">
                                    <i class='bx bx-check-circle'></i>
                                    <p class="services__modal-info">Data Visualization with Power BI.</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="services__card">
                    <h3 class="services__title">Backend <br> Architecture</h3>

                    <span class="services__button">
                        See More <i class='bx bx-right-arrow services__icon'></i>
                    </span>

                    <div class="services__modal">
                        <div class="services__modal-content">
                            <i class='bx bx-x services__modal-close'></i>

                            <h3 class="services__modal-title">Backend Architecture</h3>

                            <p class="services__modal-description">
                                Designing scalable and secure RESTful APIs to handle highly concurrent environments.
                            </p>

                            <ul class="services__modal-list">
                                <li class="services__modal-item">
                                    <i class='bx bx-check-circle'></i>
                                    <p class="services__modal-info">FastAPI & Node.js scalable servers.</p>
                                </li>
                                <li class="services__modal-item">
                                    <i class='bx bx-check-circle'></i>
                                    <p class="services__modal-info">Database management (MongoDB, PostgreSQL).</p>
                                </li>
                                <li class="services__modal-item">
                                    <i class='bx bx-check-circle'></i>
                                    <p class="services__modal-info">Dockerized deployment for reliability.</p>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>

"""
html = re.sub(r'<!--=============== SERVICES ===============-->.*?<!--=============== WORK ===============-->', services_new + '        <!--=============== WORK ===============-->', html, flags=re.DOTALL)

# 3. Replace Portfolio Works
works_new = """        <!--=============== WORK ===============-->
        <section class="work section" id="work">
            <span class="section__subtitle">My Portfolio</span>
            <h2 class="section__title">Recent Works</h2>

            <div class="work__filters">
                <span class="work__item active-work" data-filter='all'>All</span>
                <span class=" work__item" data-filter='.data'>Data</span>
                <span class=" work__item" data-filter='.web'>Web</span>
                <span class=" work__item" data-filter='.system'>System</span>
            </div>

            <div class="work__container container grid">
                <div class="work__card mix data">
                    <img src="assets/img/work1.jpg" alt="" class="work__img">

                    <h3 class="work__title">RidePulse Analytics</h3>

                    <a href="#" class="work__button">
                        Details <i class='bx bx-right-arrow work__icon'></i>
                    </a>
                </div>

                <div class="work__card mix web">
                    <img src="assets/img/work2.jpg" alt="" class="work__img">

                    <h3 class="work__title">CodeShield Platform</h3>

                    <a href="#" class="work__button">
                        Details <i class='bx bx-right-arrow work__icon'></i>
                    </a>
                </div>

                <div class="work__card mix system">
                    <img src="assets/img/work3.jpg" alt="" class="work__img">

                    <h3 class="work__title">Interview Scheduler</h3>

                    <a href="#" class="work__button">
                        Details <i class='bx bx-right-arrow work__icon'></i>
                    </a>
                </div>

            </div>
        </section>

"""

html = re.sub(r'<!--=============== WORK ===============-->.*?<!--=============== CONTACT ===============-->', works_new + '        <!--=============== CONTACT ===============-->', html, flags=re.DOTALL)


# 4. Contact Fixes
# Email
html = re.sub(r'user@gmail\.com', r'arzoodhoundiyal31@gmail.com', html)
html = re.sub(r'mailto:example@domain\.com', r'mailto:arzoodhoundiyal31@gmail.com', html)
# Whatsapp
html = re.sub(r'>6969696969<', r'>+91 8077891737<', html)
html = re.sub(r'phone=\+916969696969', r'phone=+918077891737', html)
# Twitter to Location
html = re.sub(r'<h3 class="contact__card-title">Twitter</h3>\s*<span class="contact__card-data">usertw</span>\s*<a href="https://twitter\.com/usertw" target="_blank" class="contact__button">\s*Write Me <i class=\'bx bx-right-arrow contact__button-icon\'></i>\s*</a>', r'<h3 class="contact__card-title">Location</h3>\n                            <span class="contact__card-data">Dehradun, India</span>\n\n                            <a href="#" class="contact__button">\n                                Visit <i class=\'bx bx-right-arrow contact__button-icon\'></i>\n                            </a>', html)
html = re.sub(r'bx bxl-twitter contact__card-icon', r'bx bx-map contact__card-icon', html)

# Footer Name and Links
html = re.sub(r'&#169; 2022 S44WN\. All rights reserved\.', r'&#169; 2024 Arzoo Dhoundiyal. All rights reserved.', html)
html = re.sub(r'<i class=\'bx bxl-facebook footer__social-icon\'></i>', r'<i class=\'bx bxl-github footer__social-icon\'></i>', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated perfectly.")
