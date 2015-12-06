import html2text
content = """


<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name="robots" content="NONE,NOARCHIVE">
  <title>TypeError at /</title>
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; }
    h2 { margin-bottom:.8em; }
    h2 span { font-size:80%; color:#666; font-weight:normal; }
    h3 { margin:1em 0 .5em 0; }
    h4 { margin:0 0 .5em 0; font-weight: normal; }
    code, pre { font-size: 100%; white-space: pre-wrap; }
    table { border:1px solid #ccc; border-collapse: collapse; width:100%; background:white; }
    tbody td, tbody th { vertical-align:top; padding:2px 3px; }
    thead th {
      padding:1px 6px 1px 3px; background:#fefefe; text-align:left;
      font-weight:normal; font-size:11px; border:1px solid #ddd;
    }
    tbody th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    table.vars { margin:5px 0 2px 40px; }
    table.vars td, table.req td { font-family:monospace; }
    table td.code { width:100%; }
    table td.code pre { overflow:hidden; }
    table.source th { color:#666; }
    table.source td { font-family:monospace; white-space:pre; border-bottom:1px solid #eee; }
    ul.traceback { list-style-type:none; color: #222; }
    ul.traceback li.frame { padding-bottom:1em; color:#666; }
    ul.traceback li.user { background-color:#e0e0e0; color:#000 }
    div.context { padding:10px 0; overflow:hidden; }
    div.context ol { padding-left:30px; margin:0 10px; list-style-position: inside; }
    div.context ol li { font-family:monospace; white-space:pre; color:#777; cursor:pointer; }
    div.context ol li pre { display:inline; }
    div.context ol.context-line li { color:#505050; background-color:#dfdfdf; }
    div.context ol.context-line li span { position:absolute; right:32px; }
    .user div.context ol.context-line li { background-color:#bbb; color:#000; }
    .user div.context ol li { color:#666; }
    div.commands { margin-left: 40px; }
    div.commands a { color:#555; text-decoration:none; }
    .user div.commands a { color: black; }
    #summary { background: #ffc; }
    #summary h2 { font-weight: normal; color: #666; }
    #explanation { background:#eee; }
    #template, #template-not-exist { background:#f6f6f6; }
    #template-not-exist ul { margin: 0 0 0 20px; }
    #unicode-hint { background:#eee; }
    #traceback { background:#eee; }
    #requestinfo { background:#f6f6f6; padding-left:120px; }
    #summary table { border:none; background:transparent; }
    #requestinfo h2, #requestinfo h3 { position:relative; margin-left:-100px; }
    #requestinfo h3 { margin-bottom:-1em; }
    .error { background: #ffc; }
    .specific { color:#cc3300; font-weight:bold; }
    h2 span.commands { font-size:.7em;}
    span.commands a:link {color:#5E5694;}
    pre.exception_value { font-family: sans-serif; color: #666; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
  
  <script type="text/javascript">
  //<!--
    function getElementsByClassName(oElm, strTagName, strClassName){
        // Written by Jonathan Snook, http://www.snook.ca/jon; Add-ons by Robert Nyman, http://www.robertnyman.com
        var arrElements = (strTagName == "*" && document.all)? document.all :
        oElm.getElementsByTagName(strTagName);
        var arrReturnElements = new Array();
        strClassName = strClassName.replace(/\-/g, "\-");
        var oRegExp = new RegExp("(^|\s)" + strClassName + "(\s|$)");
        var oElement;
        for(var i=0; i<arrElements.length; i++){
            oElement = arrElements[i];
            if(oRegExp.test(oElement.className)){
                arrReturnElements.push(oElement);
            }
        }
        return (arrReturnElements)
    }
    function hideAll(elems) {
      for (var e = 0; e < elems.length; e++) {
        elems[e].style.display = 'none';
      }
    }
    window.onload = function() {
      hideAll(getElementsByClassName(document, 'table', 'vars'));
      hideAll(getElementsByClassName(document, 'ol', 'pre-context'));
      hideAll(getElementsByClassName(document, 'ol', 'post-context'));
      hideAll(getElementsByClassName(document, 'div', 'pastebin'));
    }
    function toggle() {
      for (var i = 0; i < arguments.length; i++) {
        var e = document.getElementById(arguments[i]);
        if (e) {
          e.style.display = e.style.display == 'none' ? 'block': 'none';
        }
      }
      return false;
    }
    function varToggle(link, id) {
      toggle('v' + id);
      var s = link.getElementsByTagName('span')[0];
      var uarr = String.fromCharCode(0x25b6);
      var darr = String.fromCharCode(0x25bc);
      s.innerHTML = s.innerHTML == uarr ? darr : uarr;
      return false;
    }
    function switchPastebinFriendly(link) {
      s1 = "Switch to copy-and-paste view";
      s2 = "Switch back to interactive view";
      link.innerHTML = link.innerHTML.trim() == s1 ? s2: s1;
      toggle('browserTraceback', 'pastebinTraceback');
      return false;
    }
    //-->
  </script>
  
</head>
<body>
<div id="summary">
  <h1>TypeError at /</h1>
  <pre class="exception_value">&#39;NoneType&#39; object is not callable</pre>
  <table class="meta">

    <tr>
      <th>Request Method:</th>
      <td>GET</td>
    </tr>
    <tr>
      <th>Request URL:</th>
      <td>http://127.0.0.1:8000/</td>
    </tr>

    <tr>
      <th>Django Version:</th>
      <td>1.8.7</td>
    </tr>

    <tr>
      <th>Exception Type:</th>
      <td>TypeError</td>
    </tr>


    <tr>
      <th>Exception Value:</th>
      <td><pre>&#39;NoneType&#39; object is not callable</pre></td>
    </tr>


    <tr>
      <th>Exception Location:</th>
      <td>C:\Users\Miles\AppData\Local\Programs\Python\Python35-32\lib\site-packages\html2text\__init__.py in feed, line 125</td>
    </tr>

    <tr>
      <th>Python Executable:</th>
      <td>C:\Users\Miles\AppData\Local\Programs\Python\Python35-32\python.exe</td>
    </tr>
    <tr>
      <th>Python Version:</th>
      <td>3.5.0</td>
    </tr>
    <tr>
      <th>Python Path:</th>
      <td><pre>[&#39;C:\\Users\\Miles\\Documents\\GitHub\\news-graph\\newsgraph&#39;,
 &#39;C:\\Users\\Miles\\AppData\\Local\\Programs\\Python\\Python35-32\\lib\\site-packages\\setuptools-18.6.1-py3.5.egg&#39;,
 &#39;C:\\Users\\Miles\\AppData\\Local\\Programs\\Python\\Python35-32\\python35.zip&#39;,
 &#39;C:\\Users\\Miles\\AppData\\Local\\Programs\\Python\\Python35-32\\DLLs&#39;,
 &#39;C:\\Users\\Miles\\AppData\\Local\\Programs\\Python\\Python35-32\\lib&#39;,
 &#39;C:\\Users\\Miles\\AppData\\Local\\Programs\\Python\\Python35-32&#39;,
 &#39;C:\\Users\\Miles\\AppData\\Local\\Programs\\Python\\Python35-32\\lib\\site-packages&#39;]</pre></td>
    </tr>
    <tr>
      <th>Server time:</th>
      <td>Thu, 3 Dec 2015 21:01:28 +0000</td>
    </tr>
  </table>
</div>




<div id="traceback">
  <h2>Traceback <span class="commands"><a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a></span>
  </h2>
  
  <div id="browserTraceback">
    <ul class="traceback">
      
        <li class="frame django">
          <code>C:\Users\Miles\AppData\Local\Programs\Python\Python35-32\lib\site-packages\django\core\handlers\base.py</code> in <code>get_response</code>

          
            <div class="context" id="c80160368">
              
                <ol start="125" class="pre-context" id="pre80160368">
                
                  <li onclick="toggle('pre80160368', 'post80160368')"><pre>                    response = middleware_method(request, callback, callback_args, callback_kwargs)</pre></li>
                
                  <li onclick="toggle('pre80160368', 'post80160368')"><pre>                    if response:</pre></li>
                
                  <li onclick="toggle('pre80160368', 'post80160368')"><pre>                        break</pre></li>
                
                  <li onclick="toggle('pre80160368', 'post80160368')"><pre></pre></li>
                
                  <li onclick="toggle('pre80160368', 'post80160368')"><pre>            if response is None:</pre></li>
                
                  <li onclick="toggle('pre80160368', 'post80160368')"><pre>                wrapped_callback = self.make_view_atomic(callback)</pre></li>
                
                  <li onclick="toggle('pre80160368', 'post80160368')"><pre>                try:</pre></li>
                
                </ol>
              
              <ol start="132" class="context-line">
                <li onclick="toggle('pre80160368', 'post80160368')"><pre>
                                response = wrapped_callback(request, *callback_args, **callback_kwargs)</pre> <span>...</span></li></ol>
              
                <ol start='133' class="post-context" id="post80160368">
                  
                  <li onclick="toggle('pre80160368', 'post80160368')"><pre>                except Exception as e:</pre></li>
                  
                  <li onclick="toggle('pre80160368', 'post80160368')"><pre>                    # If the view raised an exception, run it through exception</pre></li>
                  
                  <li onclick="toggle('pre80160368', 'post80160368')"><pre>                    # middleware, and if the exception middleware returns a</pre></li>
                  
                  <li onclick="toggle('pre80160368', 'post80160368')"><pre>                    # response, use that. Otherwise, reraise the exception.</pre></li>
                  
                  <li onclick="toggle('pre80160368', 'post80160368')"><pre>                    for middleware_method in self._exception_middleware:</pre></li>
                  
                  <li onclick="toggle('pre80160368', 'post80160368')"><pre>                        response = middleware_method(request, e)</pre></li>
                  
              </ol>
              
            </div>
          

          
            <div class="commands">
                
                    <a href="#" onclick="return varToggle(this, '80160368')"><span>&#x25b6;</span> Local vars</a>
                
            </div>
            <table class="vars" id="v80160368">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>wrapped_callback</td>
                    <td class="code"><pre>&lt;function index at 0x04E6A930&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback</td>
                    <td class="code"><pre>&lt;function index at 0x04E6A930&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>urlconf</td>
                    <td class="code"><pre>&#39;newsgraph.urls&#39;</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>resolver</td>
                    <td class="code"><pre>&lt;RegexURLResolver &#39;newsgraph.urls&#39; (None:None) ^/&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>middleware_method</td>
                    <td class="code"><pre>&lt;bound method CsrfViewMiddleware.process_view of &lt;django.middleware.csrf.CsrfViewMiddleware object at 0x036418F0&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>resolver_match</td>
                    <td class="code"><pre>ResolverMatch(func=news.views.index, args=(), kwargs={}, url_name=index, app_name=None, namespaces=[])</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;django.core.handlers.wsgi.WSGIHandler object at 0x0298A450&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>(&#39;&lt;WSGIRequest\n&#39;
 &#39;path:/,\n&#39;
 &#39;GET:&lt;QueryDict: {}&gt;,\n&#39;
 &#39;POST:&lt;QueryDict: {}&gt;,\n&#39;
 &quot;COOKIES:{&#39;csrftoken&#39;: &#39;SICpi4lBvSpqYHYhoFiJ3wql1WmIAKA3&#39;,\n&quot;
 &quot; &#39;sessionid&#39;: &#39;f0xs8zzcejuvo8grr5dvk61p7dhf958g&#39;},\n&quot;
 &quot;META:{&#39;ALLUSERSPROFILE&#39;: &#39;C:\\\\ProgramData&#39;,\n&quot;
 &quot; &#39;APPDATA&#39;: &#39;C:\\\\Users\\\\Miles\\\\AppData\\\\Roaming&#39;,\n&quot;
 &quot; &#39;COMMONPROGRAMFILES&#39;: &#39;C:\\\\Program Files (x86)\\\\Common Files&#39;,\n&quot;
 &quot; &#39;COMMONPROGRAMFILES(X86)&#39;: &#39;C:\\\\Program Files (x86)\\\\Common Files&#39;,\n&quot;
 &quot; &#39;COMMONPROGRAMW6432&#39;: &#39;C:\\\\Program Files\\\\Common Files&#39;,\n&quot;
 &quot; &#39;COMPUTERNAME&#39;: &#39;MILES-PC&#39;,\n&quot;
 &quot; &#39;COMSPEC&#39;: &#39;C:\\\\WINDOWS\\\\system32\\\\cmd.exe&#39;,\n&quot;
 &quot; &#39;CONTENT_LENGTH&#39;: &#39;&#39;,\n&quot;
 &quot; &#39;CONTENT_TYPE&#39;: &#39;text/plain&#39;,\n&quot;
 &quot; &#39;CSRF_COOKIE&#39;: &#39;SICpi4lBvSpqYHYhoFiJ3wql1WmIAKA3&#39;,\n&quot;
 &quot; &#39;DJANGO_SETTINGS_MODULE&#39;: &#39;newsgraph.settings&#39;,\n&quot;
 &quot; &#39;FP_NO_HOST_CHECK&#39;: &#39;NO&#39;,\n&quot;
 &quot; &#39;GATEWAY_INTERFACE&#39;: &#39;CGI/1.1&#39;,\n&quot;
 &quot; &#39;HOMEDRIVE&#39;: &#39;C:&#39;,\n&quot;
 &quot; &#39;HOMEPATH&#39;: &#39;\\\\Users\\\\Miles&#39;,\n&quot;
 &quot; &#39;HTTP_ACCEPT&#39;: &quot;
 &quot;&#39;text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8&#39;,\n&quot;
 &quot; &#39;HTTP_ACCEPT_ENCODING&#39;: &#39;gzip, deflate, sdch&#39;,\n&quot;
 &quot; &#39;HTTP_ACCEPT_LANGUAGE&#39;: &#39;en-US,en;q=0.8,en-GB;q=0.6&#39;,\n&quot;
 &quot; &#39;HTTP_CACHE_CONTROL&#39;: &#39;max-age=0&#39;,\n&quot;
 &quot; &#39;HTTP_CONNECTION&#39;: &#39;keep-alive&#39;,\n&quot;
 &quot; &#39;HTTP_COOKIE&#39;: &#39;sessionid=f0xs8zzcejuvo8grr5dvk61p7dhf958g; &#39;\n&quot;
 &quot;                &#39;csrftoken=SICpi4lBvSpqYHYhoFiJ3wql1WmIAKA3&#39;,\n&quot;
 &quot; &#39;HTTP_DNT&#39;: &#39;1&#39;,\n&quot;
 &quot; &#39;HTTP_HOST&#39;: &#39;127.0.0.1:8000&#39;,\n&quot;
 &quot; &#39;HTTP_UPGRADE_INSECURE_REQUESTS&#39;: &#39;1&#39;,\n&quot;
 &quot; &#39;HTTP_USER_AGENT&#39;: &#39;Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 &quot;
 &quot;&#39;\n&quot;
 &quot;                    &#39;(KHTML, like Gecko) Chrome/46.0.2490.86 &quot;
 &quot;Safari/537.36&#39;,\n&quot;
 &quot; &#39;LOCALAPPDATA&#39;: &#39;C:\\\\Users\\\\Miles\\\\AppData\\\\Local&#39;,\n&quot;
 &quot; &#39;LOGONSERVER&#39;: &#39;\\\\\\\\MicrosoftAccount&#39;,\n&quot;
 &quot; &#39;LYNX_CFG&#39;: &#39;C:\\\\Program Files (x86)\\\\Lynx - web browser\\\\lynx.cfg&#39;,\n&quot;
 &quot; &#39;NUMBER_OF_PROCESSORS&#39;: &#39;4&#39;,\n&quot;
 &quot; &#39;OS&#39;: &#39;Windows_NT&#39;,\n&quot;
 &quot; &#39;PATH&#39;: &#39;C:\\\\ProgramData\\\\Oracle\\\\Java\\\\javapath;C:\\\\Program &quot;
 &quot;Files &#39;\n&quot;
 &quot;         &#39;(x86)\\\\NVIDIA &#39;\n&quot;
 &#39;         &#39;
 &quot;&#39;Corporation\\\\PhysX\\\\Common;C:\\\\Windows\\\\system32;C:\\\\Windows;C:\\\\Windows\\\\System32\\\\Wbem;C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\;C:\\\\Program &quot;
 &quot;&#39;\n&quot;
 &quot;         &#39;Files (x86)\\\\AMD\\\\ATI.ACE\\\\Core-Static;C:\\\\Program Files &quot;
 &quot;&#39;\n&quot;
 &quot;         &#39;(x86)\\\\Skype\\\\Phone\\\\;C:\\\\Program &#39;\n&quot;
 &#39;         &#39;
 &quot;&#39;Files\\\\nodejs\\\\;C:\\\\Users\\\\Miles\\\\.dnx\\\\bin;C:\\\\Program &#39;\n&quot;
 &quot;         &#39;Files\\\\Microsoft DNX\\\\Dnvm\\\\;C:\\\\Program Files &quot;
 &quot;(x86)\\\\Windows &#39;\n&quot;
 &quot;         &#39;Kits\\\\8.1\\\\Windows Performance Toolkit\\\\;C:\\\\Program &#39;\n&quot;
 &quot;         &#39;Files\\\\Git\\\\cmd;C:\\\\Program Files &#39;\n&quot;
 &quot;         &#39;(x86)\\\\Brackets\\\\command;C:\\\\Program Files (x86)\\\\MiKTeX &quot;
 &quot;&#39;\n&quot;
 &#39;         &#39;
 &quot;&#39;2.9\\\\miktex\\\\bin\\\\;C:\\\\WINDOWS\\\\system32;C:\\\\WINDOWS;C:\\\\WINDOWS\\\\System32\\\\Wbem;C:\\\\WINDOWS\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\;C:\\\\Program &quot;
 &quot;&#39;\n&quot;
 &quot;         &#39;Files (x86)\\\\ATI &#39;\n&quot;
 &#39;         &#39;
 &quot;&#39;Technologies\\\\ATI.ACE\\\\Core-Static;C:\\\\Users\\\\Miles\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python35-32\\\\Scripts\\\\;C:\\\\Users\\\\Miles\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python35-32\\\\;C:\\\\Users\\\\Miles\\\\AppData\\\\Roaming\\\\npm;C:\\\\Program &quot;
 &quot;&#39;\n&quot;
 &quot;         &#39;Files (x86)\\\\pdfToHTML;C:\\\\python27;C:\\\\Program Files &#39;\n&quot;
 &quot;         &#39;(x86)\\\\Microsoft VS Code\\\\bin&#39;,\n&quot;
 &quot; &#39;PATHEXT&#39;: &#39;.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC&#39;,\n&quot;
 &quot; &#39;PATH_INFO&#39;: &#39;/&#39;,\n&quot;
 &quot; &#39;PROCESSOR_ARCHITECTURE&#39;: &#39;x86&#39;,\n&quot;
 &quot; &#39;PROCESSOR_ARCHITEW6432&#39;: &#39;AMD64&#39;,\n&quot;
 &quot; &#39;PROCESSOR_IDENTIFIER&#39;: &#39;Intel64 Family 6 Model 60 Stepping 3, &quot;
 &quot;GenuineIntel&#39;,\n&quot;
 &quot; &#39;PROCESSOR_LEVEL&#39;: &#39;6&#39;,\n&quot;
 &quot; &#39;PROCESSOR_REVISION&#39;: &#39;3c03&#39;,\n&quot;
 &quot; &#39;PROGRAMDATA&#39;: &#39;C:\\\\ProgramData&#39;,\n&quot;
 &quot; &#39;PROGRAMFILES&#39;: &#39;C:\\\\Program Files (x86)&#39;,\n&quot;
 &quot; &#39;PROGRAMFILES(X86)&#39;: &#39;C:\\\\Program Files (x86)&#39;,\n&quot;
 &quot; &#39;PROGRAMW6432&#39;: &#39;C:\\\\Program Files&#39;,\n&quot;
 &quot; &#39;PROMPT&#39;: &#39;$P$G&#39;,\n&quot;
 &quot; &#39;PSMODULEPATH&#39;: &quot;
 &quot;&#39;C:\\\\WINDOWS\\\\system32\\\\WindowsPowerShell\\\\v1.0\\\\Modules\\\\&#39;,\n&quot;
 &quot; &#39;P... &lt;trimmed 5435 bytes string&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
          
        </li>
      
        <li class="frame user">
          <code>C:\Users\Miles\Documents\GitHub\news-graph\newsgraph\news\views.py</code> in <code>index</code>

          
            <div class="context" id="c82927168">
              
                <ol start="48" class="pre-context" id="pre82927168">
                
                  <li onclick="toggle('pre82927168', 'post82927168')"><pre>				html = response.read()</pre></li>
                
                  <li onclick="toggle('pre82927168', 'post82927168')"><pre>				soup = BeautifulSoup(html, &quot;html.parser&quot;)</pre></li>
                
                  <li onclick="toggle('pre82927168', 'post82927168')"><pre>				# try:</pre></li>
                
                  <li onclick="toggle('pre82927168', 'post82927168')"><pre>				content = soup.find(&quot;div&quot;, {&quot;class&quot;: &quot;story-body&quot;})</pre></li>
                
                  <li onclick="toggle('pre82927168', 'post82927168')"><pre>				print(&quot;Content =&quot;, content)</pre></li>
                
                  <li onclick="toggle('pre82927168', 'post82927168')"><pre>				cleaner = html2text.HTML2Text()</pre></li>
                
                  <li onclick="toggle('pre82927168', 'post82927168')"><pre>				cleaner.ignore_links = True</pre></li>
                
                </ol>
              
              <ol start="55" class="context-line">
                <li onclick="toggle('pre82927168', 'post82927168')"><pre>
            				content = cleaner.handle(content)</pre> <span>...</span></li></ol>
              
                <ol start='56' class="post-context" id="post82927168">
                  
                  <li onclick="toggle('pre82927168', 'post82927168')"><pre>				print(content)</pre></li>
                  
                  <li onclick="toggle('pre82927168', 'post82927168')"><pre>				# except:</pre></li>
                  
                  <li onclick="toggle('pre82927168', 'post82927168')"><pre>				# 	print(&quot;No content found&quot;)</pre></li>
                  
                  <li onclick="toggle('pre82927168', 'post82927168')"><pre>			s = Story(source=story, content=content)</pre></li>
                  
                  <li onclick="toggle('pre82927168', 'post82927168')"><pre>			s.save()</pre></li>
                  
                  <li onclick="toggle('pre82927168', 'post82927168')"><pre>			if content != &quot;&quot;:</pre></li>
                  
              </ol>
              
            </div>
          

          
            <div class="commands">
                
                    <a href="#" onclick="return varToggle(this, '82927168')"><span>&#x25b6;</span> Local vars</a>
                
            </div>
            <table class="vars" id="v82927168">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>cleaner</td>
                    <td class="code"><pre>&lt;html2text.HTML2Text object at 0x04E9E9D0&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>matches</td>
                    <td class="code"><pre>[]</pre></td>
                  </tr>
                
                  <tr>
                    <td>content</td>
                    <td class="code"><pre>&lt;div class=&quot;story-body&quot;&gt;
&lt;h1 class=&quot;story-body__h1&quot;&gt;San Bernardino shooting: Explosives found at California attackers&#39; home&lt;/h1&gt;
&lt;div class=&quot;story-body__mini-info-list-and-share&quot;&gt;
&lt;ul class=&quot;mini-info-list&quot;&gt;
&lt;li class=&quot;mini-info-list__item&quot;&gt; &lt;div class=&quot;date date--v2&quot; data-datetime=&quot;3 December 2015&quot; data-seconds=&quot;1449173319&quot;&gt;3 December 2015&lt;/div&gt;
&lt;/li&gt;
&lt;li class=&quot;mini-info-list__item&quot;&gt;&lt;span class=&quot;mini-info-list__section-desc off-screen&quot;&gt;From the section &lt;/span&gt;&lt;a class=&quot;mini-info-list__section&quot; data-entityid=&quot;section-label&quot; href=&quot;/news/world/us_and_canada&quot;&gt;US &amp;amp; Canada&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/div&gt;
&lt;div class=&quot;story-body__inner&quot; property=&quot;articleBody&quot;&gt;
&lt;figure class=&quot;media-landscape has-caption full-width lead&quot;&gt;
&lt;span class=&quot;image-and-copyright-container&quot;&gt;
&lt;img alt=&quot;Police search for bullet casings outside of the scene of the raid&quot; class=&quot;js-image-replace&quot; height=&quot;549&quot; src=&quot;http://ichef.bbci.co.uk/news/320/cpsprodpb/BBBE/production/_87026084_hi030414789.jpg&quot; width=&quot;976&quot;&gt;
&lt;span class=&quot;off-screen&quot;&gt;Image copyright&lt;/span&gt;
&lt;span class=&quot;story-image-copyright&quot;&gt;AP&lt;/span&gt;
&lt;/img&gt;&lt;/span&gt;
&lt;figcaption class=&quot;media-caption&quot;&gt;
&lt;span class=&quot;off-screen&quot;&gt;Image caption&lt;/span&gt;
&lt;span class=&quot;media-caption__text&quot;&gt;
                    Police found thousands of rounds of ammunition for multiple types of guns at the scene
                &lt;/span&gt;
&lt;/figcaption&gt;
&lt;/figure&gt;&lt;p class=&quot;story-body__introduction&quot;&gt;The attackers who killed 14 people and wounded 21 at a social services centre in California had an arsenal of weaponry in their home, police said.&lt;/p&gt;&lt;p&gt;Bomb equipment, weapons and thousands of rounds of ammunition were found by police in a raid after a shootout that killed the two suspects.&lt;/p&gt;&lt;p&gt;Authorities still have not found a motive in the attack by Syed Rizwan Farook, 28, and Tashfeen Malik, 27.&lt;/p&gt;&lt;p&gt;Police said the attack indicated there had been &quot;some degree of planning&quot;&lt;strong&gt;.&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;San Bernardino Police Chief Jarrod Burguan said it appeared that the duo was prepared to carry out another attack.&lt;/p&gt;&lt;div aria-hidden=&quot;true&quot; class=&quot;bbccom_slot mpu-ad&quot; id=&quot;bbccom_mpu_1_2_3&quot;&gt;
&lt;div class=&quot;bbccom_advert&quot;&gt;
&lt;script type=&quot;text/javascript&quot;&gt;
            /**/
            (function() {
                if (window.bbcdotcom &amp;&amp; bbcdotcom.adverts &amp;&amp; bbcdotcom.adverts.slotAsync) {
                    bbcdotcom.adverts.slotAsync(&#39;mpu&#39;, [1,2,3]);
                }
            })();
            /**/
        &lt;/script&gt;
&lt;/div&gt;
&lt;/div&gt;&lt;p&gt;&quot;There was obviously a mission here. We know that. We do not know why. We don&#39;t know if this was the intended target or if there was something that triggered him to do this immediately,&quot; said David Bowdich, assistant director of the FBI&#39;s Los Angeles office.&lt;/p&gt;&lt;p&gt;In the shootout with police hours after the attack, Farook and Malik fired 76 rounds of ammunition at the officers and the officers fired 380 rounds back.&lt;/p&gt;&lt;p&gt;Two police officers were injured during the pursuit.&lt;/p&gt; &lt;p&gt;It marks the deadliest mass shooting in the US since 26 people were killed at a school in Newtown, Connecticut in 2012.&lt;/p&gt;&lt;hr class=&quot;story-body__line&quot;&gt;&lt;h2 class=&quot;story-body__crosshead&quot;&gt;San Bernardino shooting - in depth&lt;/h2&gt;&lt;figure class=&quot;media-with-caption&quot;&gt;
&lt;div class=&quot;media-player-wrapper&quot;&gt;
&lt;figure class=&quot;js-media-player-unprocessed media-player&quot; data-playable=&#39;{&quot;settings&quot;:{&quot;counterName&quot;:&quot;news.world.us_and_canada.story.35000998.page&quot;,&quot;edition&quot;:&quot;Domestic&quot;,&quot;pageType&quot;:&quot;eav2&quot;,&quot;uniqueID&quot;:&quot;35000998&quot;,&quot;ui&quot;:{&quot;locale&quot;:{&quot;lang&quot;:&quot;en-gb&quot;}},&quot;externalEmbedUrl&quot;:&quot;http:\/\/www.bbc.co.uk\/news\/world-us-canada-35000998\/embed&quot;,&quot;insideIframe&quot;:false,&quot;playlistObject&quot;:{&quot;title&quot;:&quot;This is how events unfolded.&quot;,&quot;holdingImageURL&quot;:null,&quot;guidance&quot;:null,&quot;simulcast&quot;:false,&quot;liveRewind&quot;:false,&quot;embedRights&quot;:&quot;blocked&quot;,&quot;items&quot;:[{&quot;vpid&quot;:&quot;p03b0j76&quot;,&quot;live&quot;:false,&quot;duration&quot;:134,&quot;kind&quot;:&quot;programme&quot;}],&quot;summary&quot;:&quot;This is how events unfolded.&quot;}},&quot;otherSettings&quot;:{&quot;advertisingAllowed&quot;:true,&quot;continuousPlayCfg&quot;:{&quot;enabled&quot;:false},&quot;isAutoplayOnForAudience&quot;:false,&quot;unProcessedImageUrl&quot;:&quot;http:\/\/ichef-1.bbci.co.uk\/news\/640\/cpsprodpb\/C2CE\/production\/_87007894_87007893.jpg&quot;}}&#39;&gt;&lt;/figure&gt;
&lt;/div&gt;... &lt;trimmed 8758 bytes string&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>html</td>
                    <td class="code"><pre>(b&#39;&lt;!DOCTYPE html&gt;\n&lt;html lang=&quot;en-GB&quot; id=&quot;responsive-news&quot; prefix=&quot;og: http&#39;
 b&#39;://ogp.me/ns#&quot;&gt;\n&lt;head &gt;\n    &lt;meta charset=&quot;utf-8&quot;&gt;\n    &lt;meta http-equiv=&#39;
 b&#39;&quot;X-UA-Compatible&quot; content=&quot;IE=edge,chrome=1&quot;&gt;\n    &lt;title&gt;San Bernardino &#39;
 b&quot;shooting: Explosives found at California attackers&#39; home - BBC News&lt;/tit&quot;
 b&#39;le&gt;\n    &lt;meta name=&quot;description&quot; content=&quot;Bomb equipment and a horde of &#39;
 b&#39;weapons are found at the home of two people who killed 14 at a workplace Chr&#39;
 b&#39;istmas party in California, say police.&quot;&gt;\n\n    &lt;link rel=&quot;dns-prefetch&quot; &#39;
 b&#39;href=&quot;https://ssl.bbc.co.uk/&quot;&gt;\n    &lt;link rel=&quot;dns-prefetch&quot; href=&quot;http:/&#39;
 b&#39;/sa.bbc.co.uk/&quot;&gt;\n    &lt;link rel=&quot;dns-prefetch&quot; href=&quot;http://ichef-1.bbci.&#39;
 b&#39;co.uk/&quot;&gt;\n    &lt;link rel=&quot;dns-prefetch&quot; href=&quot;http://ichef.bbci.co.uk/&quot;&gt;\n\n&#39;
 b&#39;    &lt;meta name=&quot;x-country&quot; content=&quot;gb&quot;&gt;\n    &lt;meta name=&quot;x-audience&quot; con&#39;
 b&#39;tent=&quot;Domestic&quot;&gt;\n    &lt;meta name=&quot;CPS_AUDIENCE&quot; content=&quot;Domestic&quot;&gt;\n    &lt;&#39;
 b&#39;meta name=&quot;CPS_CHANGEQUEUEID&quot; content=&quot;263948193&quot;&gt;\n    &lt;link rel=&quot;canoni&#39;
 b&#39;cal&quot; href=&quot;http://www.bbc.co.uk/news/world-us-canada-35000998&quot;&gt;\n\n       &#39;
 b&#39;                 &lt;link rel=&quot;alternate&quot; hreflang=&quot;en-gb&quot; href=&quot;http://www.bbc&#39;
 b&#39;.co.uk/news/world-us-canada-35000998&quot;&gt;\n                                &lt;&#39;
 b&#39;link rel=&quot;alternate&quot; hreflang=&quot;en&quot; href=&quot;http://www.bbc.com/news/world-us-ca&#39;
 b&#39;nada-35000998&quot;&gt;\n                            &lt;meta property=&quot;og:title&quot; co&#39;
 b&#39;ntent=&quot;San Bernardino shooting: Explosives found at California attackers&#39;
 b&#39;\&#39; home - BBC News&quot; /&gt;\n    &lt;meta property=&quot;og:type&quot; content=&quot;article&quot; /&gt;\n&#39;
 b&#39;    &lt;meta property=&quot;og:description&quot; content=&quot;Bomb equipment and a horde of w&#39;
 b&#39;eapons are found at the home of two people who killed 14 at a workplace Chri&#39;
 b&#39;stmas party in California, say police.&quot; /&gt;\n    &lt;meta property=&quot;og:site_n&#39;
 b&#39;ame&quot; content=&quot;BBC News&quot; /&gt;\n    &lt;meta property=&quot;og:locale&quot; content=&quot;en_GB&#39;
 b&#39;&quot; /&gt;\n    &lt;meta property=&quot;og:article:author&quot; content=&quot;BBC News&quot; /&gt;\n    &lt;m&#39;
 b&#39;eta property=&quot;og:article:section&quot; content=&quot;US &amp;amp; Canada&quot; /&gt;\n    &lt;meta&#39;
 b&#39; property=&quot;og:url&quot; content=&quot;http://www.bbc.co.uk/news/world-us-canada-350009&#39;
 b&#39;98&quot; /&gt;\n    &lt;meta property=&quot;og:image&quot; content=&quot;http://ichef.bbci.co.uk/ne&#39;
 b&#39;ws/1024/cpsprodpb/E2CE/production/_87026085_hi030414789.jpg&quot; /&gt;\n\n    &lt;me&#39;
 b&#39;ta name=&quot;twitter:card&quot; content=&quot;summary_large_image&quot;&gt;\n    &lt;meta name=&quot;tw&#39;
 b&#39;itter:site&quot; content=&quot;@BBCNews&quot;&gt;\n    &lt;meta name=&quot;twitter:title&quot; content=&quot;&#39;
 b&quot;San Bernardino shooting: Explosives found at California attackers&#39; home - BB&quot;
 b&#39;C News&quot;&gt;\n    &lt;meta name=&quot;twitter:description&quot; content=&quot;Bomb equipment an&#39;
 b&#39;d a horde of weapons are found at the home of two people who killed 14 at a &#39;
 b&#39;workplace Christmas party in California, say police.&quot;&gt;\n    &lt;meta name=&quot;t&#39;
 b&#39;witter:creator&quot; content=&quot;@BBCNews&quot;&gt;\n    &lt;meta name=&quot;twitter:image:src&quot; c&#39;
 b&#39;ontent=&quot;http://ichef.bbci.co.uk/news/560/cpsprodpb/E2CE/production/_87026085&#39;
 b&#39;_hi030414789.jpg&quot;&gt;\n    &lt;meta name=&quot;twitter:image:alt&quot; content=&quot;Police se&#39;
 b&#39;arch for bullet casings outside of the scene of the raid&quot; /&gt;\n    &lt;meta n&#39;
 b&#39;ame=&quot;twitter:domain&quot; content=&quot;www.bbc.co.uk&quot;&gt;\n\n    &lt;script type=&quot;applica&#39;
 b&#39;tion/ld+json&quot;&gt;\n    {\n        &quot;@context&quot;: &quot;http://schema.org&quot;\n        ,&quot;@&#39;
 b&#39;type&quot;: &quot;Article&quot;\n        \n        ,&quot;url&quot;: &quot;http://www.bbc.co.uk/news/wor&#39;
 b&#39;ld-us-canada-35000998&quot;\n        ,&quot;publisher&quot;: {\n            &quot;@type&quot;: &quot;Org&#39;
 b&#39;anization&quot;,\n            &quot;name&quot;: &quot;BBC News&quot;,\n            &quot;logo&quot;: &quot;http://&#39;
 b&#39;www.bbc.co.uk/news/special/2015/newsspec_10857/bbc_news_logo.png?cb=1&quot;\n &#39;
 b&#39;       }\n        \n        ,&quot;headline&quot;: &quot;San Bernardino shooting: Explosi&#39;
 b&#39;ves found at California attackers\&#39; home&quot;\n        \n        ,&quot;mainEntityOf&#39;
 b&#39;Page&quot;: &quot;http://www.bbc.co.uk/news/world-us-canada-35000998&quot;\n        ,&quot;ar&#39;
 b&#39;ticleBody&quot;: &quot;Bomb equipment and a horde of weapons are found at the home of &#39;
 b&#39;two people who killed 14 at a workplace Christmas party in California, say p&#39;
 b&#39;olice.&quot;\n        \n        ,&quot;image&quot;: {\n            &quot;@list&quot;: [\n            &#39;
 b&#39;    &quot;http://ichef-1.bbci.co.uk/news/560/cpsprodpb/B77A/produc... &lt;trimmed 141544 bytes string&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>(&#39;&lt;WSGIRequest\n&#39;
 &#39;path:/,\n&#39;
 &#39;GET:&lt;QueryDict: {}&gt;,\n&#39;
 &#39;POST:&lt;QueryDict: {}&gt;,\n&#39;
 &quot;COOKIES:{&#39;csrftoken&#39;: &#39;SICpi4lBvSpqYHYhoFiJ3wql1WmIAKA3&#39;,\n&quot;
 &quot; &#39;sessionid&#39;: &#39;f0xs8zzcejuvo8grr5dvk61p7dhf958g&#39;},\n&quot;
 &quot;META:{&#39;ALLUSERSPROFILE&#39;: &#39;C:\\\\ProgramData&#39;,\n&quot;
 &quot; &#39;APPDATA&#39;: &#39;C:\\\\Users\\\\Miles\\\\AppData\\\\Roaming&#39;,\n&quot;
 &quot; &#39;COMMONPROGRAMFILES&#39;: &#39;C:\\\\Program Files (x86)\\\\Common Files&#39;,\n&quot;
 &quot; &#39;COMMONPROGRAMFILES(X86)&#39;: &#39;C:\\\\Program Files (x86)\\\\Common Files&#39;,\n&quot;
 &quot; &#39;COMMONPROGRAMW6432&#39;: &#39;C:\\\\Program Files\\\\Common Files&#39;,\n&quot;
 &quot; &#39;COMPUTERNAME&#39;: &#39;MILES-PC&#39;,\n&quot;
 &quot; &#39;COMSPEC&#39;: &#39;C:\\\\WINDOWS\\\\system32\\\\cmd.exe&#39;,\n&quot;
 &quot; &#39;CONTENT_LENGTH&#39;: &#39;&#39;,\n&quot;
 &quot; &#39;CONTENT_TYPE&#39;: &#39;text/plain&#39;,\n&quot;
 &quot; &#39;CSRF_COOKIE&#39;: &#39;SICpi4lBvSpqYHYhoFiJ3wql1WmIAKA3&#39;,\n&quot;
 &quot; &#39;DJANGO_SETTINGS_MODULE&#39;: &#39;newsgraph.settings&#39;,\n&quot;
 &quot; &#39;FP_NO_HOST_CHECK&#39;: &#39;NO&#39;,\n&quot;
 &quot; &#39;GATEWAY_INTERFACE&#39;: &#39;CGI/1.1&#39;,\n&quot;
 &quot; &#39;HOMEDRIVE&#39;: &#39;C:&#39;,\n&quot;
 &quot; &#39;HOMEPATH&#39;: &#39;\\\\Users\\\\Miles&#39;,\n&quot;
 &quot; &#39;HTTP_ACCEPT&#39;: &quot;
 &quot;&#39;text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8&#39;,\n&quot;
 &quot; &#39;HTTP_ACCEPT_ENCODING&#39;: &#39;gzip, deflate, sdch&#39;,\n&quot;
 &quot; &#39;HTTP_ACCEPT_LANGUAGE&#39;: &#39;en-US,en;q=0.8,en-GB;q=0.6&#39;,\n&quot;
 &quot; &#39;HTTP_CACHE_CONTROL&#39;: &#39;max-age=0&#39;,\n&quot;
 &quot; &#39;HTTP_CONNECTION&#39;: &#39;keep-alive&#39;,\n&quot;
 &quot; &#39;HTTP_COOKIE&#39;: &#39;sessionid=f0xs8zzcejuvo8grr5dvk61p7dhf958g; &#39;\n&quot;
 &quot;                &#39;csrftoken=SICpi4lBvSpqYHYhoFiJ3wql1WmIAKA3&#39;,\n&quot;
 &quot; &#39;HTTP_DNT&#39;: &#39;1&#39;,\n&quot;
 &quot; &#39;HTTP_HOST&#39;: &#39;127.0.0.1:8000&#39;,\n&quot;
 &quot; &#39;HTTP_UPGRADE_INSECURE_REQUESTS&#39;: &#39;1&#39;,\n&quot;
 &quot; &#39;HTTP_USER_AGENT&#39;: &#39;Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 &quot;
 &quot;&#39;\n&quot;
 &quot;                    &#39;(KHTML, like Gecko) Chrome/46.0.2490.86 &quot;
 &quot;Safari/537.36&#39;,\n&quot;
 &quot; &#39;LOCALAPPDATA&#39;: &#39;C:\\\\Users\\\\Miles\\\\AppData\\\\Local&#39;,\n&quot;
 &quot; &#39;LOGONSERVER&#39;: &#39;\\\\\\\\MicrosoftAccount&#39;,\n&quot;
 &quot; &#39;LYNX_CFG&#39;: &#39;C:\\\\Program Files (x86)\\\\Lynx - web browser\\\\lynx.cfg&#39;,\n&quot;
 &quot; &#39;NUMBER_OF_PROCESSORS&#39;: &#39;4&#39;,\n&quot;
 &quot; &#39;OS&#39;: &#39;Windows_NT&#39;,\n&quot;
 &quot; &#39;PATH&#39;: &#39;C:\\\\ProgramData\\\\Oracle\\\\Java\\\\javapath;C:\\\\Program &quot;
 &quot;Files &#39;\n&quot;
 &quot;         &#39;(x86)\\\\NVIDIA &#39;\n&quot;
 &#39;         &#39;
 &quot;&#39;Corporation\\\\PhysX\\\\Common;C:\\\\Windows\\\\system32;C:\\\\Windows;C:\\\\Windows\\\\System32\\\\Wbem;C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\;C:\\\\Program &quot;
 &quot;&#39;\n&quot;
 &quot;         &#39;Files (x86)\\\\AMD\\\\ATI.ACE\\\\Core-Static;C:\\\\Program Files &quot;
 &quot;&#39;\n&quot;
 &quot;         &#39;(x86)\\\\Skype\\\\Phone\\\\;C:\\\\Program &#39;\n&quot;
 &#39;         &#39;
 &quot;&#39;Files\\\\nodejs\\\\;C:\\\\Users\\\\Miles\\\\.dnx\\\\bin;C:\\\\Program &#39;\n&quot;
 &quot;         &#39;Files\\\\Microsoft DNX\\\\Dnvm\\\\;C:\\\\Program Files &quot;
 &quot;(x86)\\\\Windows &#39;\n&quot;
 &quot;         &#39;Kits\\\\8.1\\\\Windows Performance Toolkit\\\\;C:\\\\Program &#39;\n&quot;
 &quot;         &#39;Files\\\\Git\\\\cmd;C:\\\\Program Files &#39;\n&quot;
 &quot;         &#39;(x86)\\\\Brackets\\\\command;C:\\\\Program Files (x86)\\\\MiKTeX &quot;
 &quot;&#39;\n&quot;
 &#39;         &#39;
 &quot;&#39;2.9\\\\miktex\\\\bin\\\\;C:\\\\WINDOWS\\\\system32;C:\\\\WINDOWS;C:\\\\WINDOWS\\\\System32\\\\Wbem;C:\\\\WINDOWS\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\;C:\\\\Program &quot;
 &quot;&#39;\n&quot;
 &quot;         &#39;Files (x86)\\\\ATI &#39;\n&quot;
 &#39;         &#39;
 &quot;&#39;Technologies\\\\ATI.ACE\\\\Core-Static;C:\\\\Users\\\\Miles\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python35-32\\\\Scripts\\\\;C:\\\\Users\\\\Miles\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python35-32\\\\;C:\\\\Users\\\\Miles\\\\AppData\\\\Roaming\\\\npm;C:\\\\Program &quot;
 &quot;&#39;\n&quot;
 &quot;         &#39;Files (x86)\\\\pdfToHTML;C:\\\\python27;C:\\\\Program Files &#39;\n&quot;
 &quot;         &#39;(x86)\\\\Microsoft VS Code\\\\bin&#39;,\n&quot;
 &quot; &#39;PATHEXT&#39;: &#39;.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC&#39;,\n&quot;
 &quot; &#39;PATH_INFO&#39;: &#39;/&#39;,\n&quot;
 &quot; &#39;PROCESSOR_ARCHITECTURE&#39;: &#39;x86&#39;,\n&quot;
 &quot; &#39;PROCESSOR_ARCHITEW6432&#39;: &#39;AMD64&#39;,\n&quot;
 &quot; &#39;PROCESSOR_IDENTIFIER&#39;: &#39;Intel64 Family 6 Model 60 Stepping 3, &quot;
 &quot;GenuineIntel&#39;,\n&quot;
 &quot; &#39;PROCESSOR_LEVEL&#39;: &#39;6&#39;,\n&quot;
 &quot; &#39;PROCESSOR_REVISION&#39;: &#39;3c03&#39;,\n&quot;
 &quot; &#39;PROGRAMDATA&#39;: &#39;C:\\\\ProgramData&#39;,\n&quot;
 &quot; &#39;PROGRAMFILES&#39;: &#39;C:\\\\Program Files (x86)&#39;,\n&quot;
 &quot; &#39;PROGRAMFILES(X86)&#39;: &#39;C:\\\\Program Files (x86)&#39;,\n&quot;
 &quot; &#39;PROGRAMW6432&#39;: &#39;C:\\\\Program Files&#39;,\n&quot;
 &quot; &#39;PROMPT&#39;: &#39;$P$G&#39;,\n&quot;
 &quot; &#39;PSMODULEPATH&#39;: &quot;
 &quot;&#39;C:\\\\WINDOWS\\\\system32\\\\WindowsPowerShell\\\\v1.0\\\\Modules\\\\&#39;,\n&quot;
 &quot; &#39;P... &lt;trimmed 5435 bytes string&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>&lt;http.client.HTTPResponse object at 0x04E9E310&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>story</td>
                    <td class="code"><pre>&#39;http://www.bbc.co.uk/news/world-us-canada-35000998#sa-ns_mchannel=rss&amp;ns_source=PublicRSS20-sa&#39;</pre></td>
                  </tr>
                
                  <tr>
                    <td>soup</td>
                    <td class="code"><pre>&lt;!DOCTYPE html&gt;

&lt;html id=&quot;responsive-news&quot; lang=&quot;en-GB&quot; prefix=&quot;og: http://ogp.me/ns#&quot;&gt;
&lt;head&gt;
&lt;meta charset=&quot;utf-8&quot;&gt;
&lt;meta content=&quot;IE=edge,chrome=1&quot; http-equiv=&quot;X-UA-Compatible&quot;&gt;
&lt;title&gt;San Bernardino shooting: Explosives found at California attackers&#39; home - BBC News&lt;/title&gt;
&lt;meta content=&quot;Bomb equipment and a horde of weapons are found at the home of two people who killed 14 at a workplace Christmas party in California, say police.&quot; name=&quot;description&quot;&gt;
&lt;link href=&quot;https://ssl.bbc.co.uk/&quot; rel=&quot;dns-prefetch&quot;&gt;
&lt;link href=&quot;http://sa.bbc.co.uk/&quot; rel=&quot;dns-prefetch&quot;&gt;
&lt;link href=&quot;http://ichef-1.bbci.co.uk/&quot; rel=&quot;dns-prefetch&quot;&gt;
&lt;link href=&quot;http://ichef.bbci.co.uk/&quot; rel=&quot;dns-prefetch&quot;&gt;
&lt;meta content=&quot;gb&quot; name=&quot;x-country&quot;&gt;
&lt;meta content=&quot;Domestic&quot; name=&quot;x-audience&quot;&gt;
&lt;meta content=&quot;Domestic&quot; name=&quot;CPS_AUDIENCE&quot;&gt;
&lt;meta content=&quot;263948193&quot; name=&quot;CPS_CHANGEQUEUEID&quot;&gt;
&lt;link href=&quot;http://www.bbc.co.uk/news/world-us-canada-35000998&quot; rel=&quot;canonical&quot;&gt;
&lt;link href=&quot;http://www.bbc.co.uk/news/world-us-canada-35000998&quot; hreflang=&quot;en-gb&quot; rel=&quot;alternate&quot;&gt;
&lt;link href=&quot;http://www.bbc.com/news/world-us-canada-35000998&quot; hreflang=&quot;en&quot; rel=&quot;alternate&quot;&gt;
&lt;meta content=&quot;San Bernardino shooting: Explosives found at California attackers&#39; home - BBC News&quot; property=&quot;og:title&quot;/&gt;
&lt;meta content=&quot;article&quot; property=&quot;og:type&quot;/&gt;
&lt;meta content=&quot;Bomb equipment and a horde of weapons are found at the home of two people who killed 14 at a workplace Christmas party in California, say police.&quot; property=&quot;og:description&quot;/&gt;
&lt;meta content=&quot;BBC News&quot; property=&quot;og:site_name&quot;/&gt;
&lt;meta content=&quot;en_GB&quot; property=&quot;og:locale&quot;/&gt;
&lt;meta content=&quot;BBC News&quot; property=&quot;og:article:author&quot;/&gt;
&lt;meta content=&quot;US &amp;amp; Canada&quot; property=&quot;og:article:section&quot;/&gt;
&lt;meta content=&quot;http://www.bbc.co.uk/news/world-us-canada-35000998&quot; property=&quot;og:url&quot;/&gt;
&lt;meta content=&quot;http://ichef.bbci.co.uk/news/1024/cpsprodpb/E2CE/production/_87026085_hi030414789.jpg&quot; property=&quot;og:image&quot;/&gt;
&lt;meta content=&quot;summary_large_image&quot; name=&quot;twitter:card&quot;&gt;
&lt;meta content=&quot;@BBCNews&quot; name=&quot;twitter:site&quot;&gt;
&lt;meta content=&quot;San Bernardino shooting: Explosives found at California attackers&#39; home - BBC News&quot; name=&quot;twitter:title&quot;&gt;
&lt;meta content=&quot;Bomb equipment and a horde of weapons are found at the home of two people who killed 14 at a workplace Christmas party in California, say police.&quot; name=&quot;twitter:description&quot;&gt;
&lt;meta content=&quot;@BBCNews&quot; name=&quot;twitter:creator&quot;&gt;
&lt;meta content=&quot;http://ichef.bbci.co.uk/news/560/cpsprodpb/E2CE/production/_87026085_hi030414789.jpg&quot; name=&quot;twitter:image:src&quot;&gt;
&lt;meta content=&quot;Police search for bullet casings outside of the scene of the raid&quot; name=&quot;twitter:image:alt&quot;/&gt;
&lt;meta content=&quot;www.bbc.co.uk&quot; name=&quot;twitter:domain&quot;&gt;
&lt;script type=&quot;application/ld+json&quot;&gt;
    {
        &quot;@context&quot;: &quot;http://schema.org&quot;
        ,&quot;@type&quot;: &quot;Article&quot;
        
        ,&quot;url&quot;: &quot;http://www.bbc.co.uk/news/world-us-canada-35000998&quot;
        ,&quot;publisher&quot;: {
            &quot;@type&quot;: &quot;Organization&quot;,
            &quot;name&quot;: &quot;BBC News&quot;,
            &quot;logo&quot;: &quot;http://www.bbc.co.uk/news/special/2015/newsspec_10857/bbc_news_logo.png?cb=1&quot;
        }
        
        ,&quot;headline&quot;: &quot;San Bernardino shooting: Explosives found at California attackers&#39; home&quot;
        
        ,&quot;mainEntityOfPage&quot;: &quot;http://www.bbc.co.uk/news/world-us-canada-35000998&quot;
        ,&quot;articleBody&quot;: &quot;Bomb equipment and a horde of weapons are found at the home of two people who killed 14 at a workplace Christmas party in California, say police.&quot;
        
        ,&quot;image&quot;: {
            &quot;@list&quot;: [
                &quot;http://ichef-1.bbci.co.uk/news/560/cpsprodpb/B77A/production/_87007964_030405542.jpg&quot;
                ,&quot;http://ichef.bbci.co.uk/news/560/cpsprodpb/BBBE/production/_87026084_hi030414789.jpg&quot;
                ,&quot;http://ichef.bbci.co.uk/news/560/media/images/76020000/jpg/_76020974_line976.jpg&quot;
            ]
        }
        ,&quot;datePublished&quot;: &quot;2015-12-03T20:08:39+00:00&quot;
    }
    &lt;/script&gt;
&lt;link href=&quot;http://www.bbc.co.uk/news/amp/35000998&quot; rel=&quot;amphtml&quot;&gt;
&lt;meta content=&quot;BBC News&quot; name=&quot;apple-mobile-web-app-title&quot;&gt;
&lt;link href=&quot;http://static.bbci.co.uk/news/1.101.0483/apple-touch-icon-57x57-pre... &lt;trimmed 111107 bytes string&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
          
        </li>
      
        <li class="frame user">
          <code>C:\Users\Miles\AppData\Local\Programs\Python\Python35-32\lib\site-packages\html2text\__init__.py</code> in <code>handle</code>

          
            <div class="context" id="c82927128">
              
                <ol start="122" class="pre-context" id="pre82927128">
                
                  <li onclick="toggle('pre82927128', 'post82927128')"><pre>        config.UNIFIABLE[&#39;nbsp&#39;] = &#39;&amp;nbsp_place_holder;&#39;</pre></li>
                
                  <li onclick="toggle('pre82927128', 'post82927128')"><pre></pre></li>
                
                  <li onclick="toggle('pre82927128', 'post82927128')"><pre>    def feed(self, data):</pre></li>
                
                  <li onclick="toggle('pre82927128', 'post82927128')"><pre>        data = data.replace(&quot;&lt;/&#39; + &#39;script&gt;&quot;, &quot;&lt;/ignore&gt;&quot;)</pre></li>
                
                  <li onclick="toggle('pre82927128', 'post82927128')"><pre>        HTMLParser.HTMLParser.feed(self, data)</pre></li>
                
                  <li onclick="toggle('pre82927128', 'post82927128')"><pre></pre></li>
                
                  <li onclick="toggle('pre82927128', 'post82927128')"><pre>    def handle(self, data):</pre></li>
                
                </ol>
              
              <ol start="129" class="context-line">
                <li onclick="toggle('pre82927128', 'post82927128')"><pre>
                    self.feed(data)</pre> <span>...</span></li></ol>
              
                <ol start='130' class="post-context" id="post82927128">
                  
                  <li onclick="toggle('pre82927128', 'post82927128')"><pre>        self.feed(&quot;&quot;)</pre></li>
                  
                  <li onclick="toggle('pre82927128', 'post82927128')"><pre>        return self.optwrap(self.close())</pre></li>
                  
                  <li onclick="toggle('pre82927128', 'post82927128')"><pre></pre></li>
                  
                  <li onclick="toggle('pre82927128', 'post82927128')"><pre>    def outtextf(self, s):</pre></li>
                  
                  <li onclick="toggle('pre82927128', 'post82927128')"><pre>        self.outtextlist.append(s)</pre></li>
                  
                  <li onclick="toggle('pre82927128', 'post82927128')"><pre>        if s:</pre></li>
                  
              </ol>
              
            </div>
          

          
            <div class="commands">
                
                    <a href="#" onclick="return varToggle(this, '82927128')"><span>&#x25b6;</span> Local vars</a>
                
            </div>
            <table class="vars" id="v82927128">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;html2text.HTML2Text object at 0x04E9E9D0&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>data</td>
                    <td class="code"><pre>&lt;div class=&quot;story-body&quot;&gt;
&lt;h1 class=&quot;story-body__h1&quot;&gt;San Bernardino shooting: Explosives found at California attackers&#39; home&lt;/h1&gt;
&lt;div class=&quot;story-body__mini-info-list-and-share&quot;&gt;
&lt;ul class=&quot;mini-info-list&quot;&gt;
&lt;li class=&quot;mini-info-list__item&quot;&gt; &lt;div class=&quot;date date--v2&quot; data-datetime=&quot;3 December 2015&quot; data-seconds=&quot;1449173319&quot;&gt;3 December 2015&lt;/div&gt;
&lt;/li&gt;
&lt;li class=&quot;mini-info-list__item&quot;&gt;&lt;span class=&quot;mini-info-list__section-desc off-screen&quot;&gt;From the section &lt;/span&gt;&lt;a class=&quot;mini-info-list__section&quot; data-entityid=&quot;section-label&quot; href=&quot;/news/world/us_and_canada&quot;&gt;US &amp;amp; Canada&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/div&gt;
&lt;div class=&quot;story-body__inner&quot; property=&quot;articleBody&quot;&gt;
&lt;figure class=&quot;media-landscape has-caption full-width lead&quot;&gt;
&lt;span class=&quot;image-and-copyright-container&quot;&gt;
&lt;img alt=&quot;Police search for bullet casings outside of the scene of the raid&quot; class=&quot;js-image-replace&quot; height=&quot;549&quot; src=&quot;http://ichef.bbci.co.uk/news/320/cpsprodpb/BBBE/production/_87026084_hi030414789.jpg&quot; width=&quot;976&quot;&gt;
&lt;span class=&quot;off-screen&quot;&gt;Image copyright&lt;/span&gt;
&lt;span class=&quot;story-image-copyright&quot;&gt;AP&lt;/span&gt;
&lt;/img&gt;&lt;/span&gt;
&lt;figcaption class=&quot;media-caption&quot;&gt;
&lt;span class=&quot;off-screen&quot;&gt;Image caption&lt;/span&gt;
&lt;span class=&quot;media-caption__text&quot;&gt;
                    Police found thousands of rounds of ammunition for multiple types of guns at the scene
                &lt;/span&gt;
&lt;/figcaption&gt;
&lt;/figure&gt;&lt;p class=&quot;story-body__introduction&quot;&gt;The attackers who killed 14 people and wounded 21 at a social services centre in California had an arsenal of weaponry in their home, police said.&lt;/p&gt;&lt;p&gt;Bomb equipment, weapons and thousands of rounds of ammunition were found by police in a raid after a shootout that killed the two suspects.&lt;/p&gt;&lt;p&gt;Authorities still have not found a motive in the attack by Syed Rizwan Farook, 28, and Tashfeen Malik, 27.&lt;/p&gt;&lt;p&gt;Police said the attack indicated there had been &quot;some degree of planning&quot;&lt;strong&gt;.&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;San Bernardino Police Chief Jarrod Burguan said it appeared that the duo was prepared to carry out another attack.&lt;/p&gt;&lt;div aria-hidden=&quot;true&quot; class=&quot;bbccom_slot mpu-ad&quot; id=&quot;bbccom_mpu_1_2_3&quot;&gt;
&lt;div class=&quot;bbccom_advert&quot;&gt;
&lt;script type=&quot;text/javascript&quot;&gt;
            /**/
            (function() {
                if (window.bbcdotcom &amp;&amp; bbcdotcom.adverts &amp;&amp; bbcdotcom.adverts.slotAsync) {
                    bbcdotcom.adverts.slotAsync(&#39;mpu&#39;, [1,2,3]);
                }
            })();
            /**/
        &lt;/script&gt;
&lt;/div&gt;
&lt;/div&gt;&lt;p&gt;&quot;There was obviously a mission here. We know that. We do not know why. We don&#39;t know if this was the intended target or if there was something that triggered him to do this immediately,&quot; said David Bowdich, assistant director of the FBI&#39;s Los Angeles office.&lt;/p&gt;&lt;p&gt;In the shootout with police hours after the attack, Farook and Malik fired 76 rounds of ammunition at the officers and the officers fired 380 rounds back.&lt;/p&gt;&lt;p&gt;Two police officers were injured during the pursuit.&lt;/p&gt; &lt;p&gt;It marks the deadliest mass shooting in the US since 26 people were killed at a school in Newtown, Connecticut in 2012.&lt;/p&gt;&lt;hr class=&quot;story-body__line&quot;&gt;&lt;h2 class=&quot;story-body__crosshead&quot;&gt;San Bernardino shooting - in depth&lt;/h2&gt;&lt;figure class=&quot;media-with-caption&quot;&gt;
&lt;div class=&quot;media-player-wrapper&quot;&gt;
&lt;figure class=&quot;js-media-player-unprocessed media-player&quot; data-playable=&#39;{&quot;settings&quot;:{&quot;counterName&quot;:&quot;news.world.us_and_canada.story.35000998.page&quot;,&quot;edition&quot;:&quot;Domestic&quot;,&quot;pageType&quot;:&quot;eav2&quot;,&quot;uniqueID&quot;:&quot;35000998&quot;,&quot;ui&quot;:{&quot;locale&quot;:{&quot;lang&quot;:&quot;en-gb&quot;}},&quot;externalEmbedUrl&quot;:&quot;http:\/\/www.bbc.co.uk\/news\/world-us-canada-35000998\/embed&quot;,&quot;insideIframe&quot;:false,&quot;playlistObject&quot;:{&quot;title&quot;:&quot;This is how events unfolded.&quot;,&quot;holdingImageURL&quot;:null,&quot;guidance&quot;:null,&quot;simulcast&quot;:false,&quot;liveRewind&quot;:false,&quot;embedRights&quot;:&quot;blocked&quot;,&quot;items&quot;:[{&quot;vpid&quot;:&quot;p03b0j76&quot;,&quot;live&quot;:false,&quot;duration&quot;:134,&quot;kind&quot;:&quot;programme&quot;}],&quot;summary&quot;:&quot;This is how events unfolded.&quot;}},&quot;otherSettings&quot;:{&quot;advertisingAllowed&quot;:true,&quot;continuousPlayCfg&quot;:{&quot;enabled&quot;:false},&quot;isAutoplayOnForAudience&quot;:false,&quot;unProcessedImageUrl&quot;:&quot;http:\/\/ichef-1.bbci.co.uk\/news\/640\/cpsprodpb\/C2CE\/production\/_87007894_87007893.jpg&quot;}}&#39;&gt;&lt;/figure&gt;
&lt;/div&gt;... &lt;trimmed 8758 bytes string&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
          
        </li>
      
        <li class="frame user">
          <code>C:\Users\Miles\AppData\Local\Programs\Python\Python35-32\lib\site-packages\html2text\__init__.py</code> in <code>feed</code>

          
            <div class="context" id="c82927088">
              
                <ol start="118" class="pre-context" id="pre82927088">
                
                  <li onclick="toggle('pre82927088', 'post82927088')"><pre>        try:</pre></li>
                
                  <li onclick="toggle('pre82927088', 'post82927088')"><pre>            del unifiable_n[name2cp(&#39;nbsp&#39;)]</pre></li>
                
                  <li onclick="toggle('pre82927088', 'post82927088')"><pre>        except KeyError:</pre></li>
                
                  <li onclick="toggle('pre82927088', 'post82927088')"><pre>            pass</pre></li>
                
                  <li onclick="toggle('pre82927088', 'post82927088')"><pre>        config.UNIFIABLE[&#39;nbsp&#39;] = &#39;&amp;nbsp_place_holder;&#39;</pre></li>
                
                  <li onclick="toggle('pre82927088', 'post82927088')"><pre></pre></li>
                
                  <li onclick="toggle('pre82927088', 'post82927088')"><pre>    def feed(self, data):</pre></li>
                
                </ol>
              
              <ol start="125" class="context-line">
                <li onclick="toggle('pre82927088', 'post82927088')"><pre>
                    data = data.replace(&quot;&lt;/&#39; + &#39;script&gt;&quot;, &quot;&lt;/ignore&gt;&quot;)</pre> <span>...</span></li></ol>
              
                <ol start='126' class="post-context" id="post82927088">
                  
                  <li onclick="toggle('pre82927088', 'post82927088')"><pre>        HTMLParser.HTMLParser.feed(self, data)</pre></li>
                  
                  <li onclick="toggle('pre82927088', 'post82927088')"><pre></pre></li>
                  
                  <li onclick="toggle('pre82927088', 'post82927088')"><pre>    def handle(self, data):</pre></li>
                  
                  <li onclick="toggle('pre82927088', 'post82927088')"><pre>        self.feed(data)</pre></li>
                  
                  <li onclick="toggle('pre82927088', 'post82927088')"><pre>        self.feed(&quot;&quot;)</pre></li>
                  
                  <li onclick="toggle('pre82927088', 'post82927088')"><pre>        return self.optwrap(self.close())</pre></li>
                  
              </ol>
              
            </div>
          

          
            <div class="commands">
                
                    <a href="#" onclick="return varToggle(this, '82927088')"><span>&#x25b6;</span> Local vars</a>
                
            </div>
            <table class="vars" id="v82927088">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;html2text.HTML2Text object at 0x04E9E9D0&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>data</td>
                    <td class="code"><pre>&lt;div class=&quot;story-body&quot;&gt;
&lt;h1 class=&quot;story-body__h1&quot;&gt;San Bernardino shooting: Explosives found at California attackers&#39; home&lt;/h1&gt;
&lt;div class=&quot;story-body__mini-info-list-and-share&quot;&gt;
&lt;ul class=&quot;mini-info-list&quot;&gt;
&lt;li class=&quot;mini-info-list__item&quot;&gt; &lt;div class=&quot;date date--v2&quot; data-datetime=&quot;3 December 2015&quot; data-seconds=&quot;1449173319&quot;&gt;3 December 2015&lt;/div&gt;
&lt;/li&gt;
&lt;li class=&quot;mini-info-list__item&quot;&gt;&lt;span class=&quot;mini-info-list__section-desc off-screen&quot;&gt;From the section &lt;/span&gt;&lt;a class=&quot;mini-info-list__section&quot; data-entityid=&quot;section-label&quot; href=&quot;/news/world/us_and_canada&quot;&gt;US &amp;amp; Canada&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/div&gt;
&lt;div class=&quot;story-body__inner&quot; property=&quot;articleBody&quot;&gt;
&lt;figure class=&quot;media-landscape has-caption full-width lead&quot;&gt;
&lt;span class=&quot;image-and-copyright-container&quot;&gt;
&lt;img alt=&quot;Police search for bullet casings outside of the scene of the raid&quot; class=&quot;js-image-replace&quot; height=&quot;549&quot; src=&quot;http://ichef.bbci.co.uk/news/320/cpsprodpb/BBBE/production/_87026084_hi030414789.jpg&quot; width=&quot;976&quot;&gt;
&lt;span class=&quot;off-screen&quot;&gt;Image copyright&lt;/span&gt;
&lt;span class=&quot;story-image-copyright&quot;&gt;AP&lt;/span&gt;
&lt;/img&gt;&lt;/span&gt;
&lt;figcaption class=&quot;media-caption&quot;&gt;
&lt;span class=&quot;off-screen&quot;&gt;Image caption&lt;/span&gt;
&lt;span class=&quot;media-caption__text&quot;&gt;
                    Police found thousands of rounds of ammunition for multiple types of guns at the scene
                &lt;/span&gt;
&lt;/figcaption&gt;
&lt;/figure&gt;&lt;p class=&quot;story-body__introduction&quot;&gt;The attackers who killed 14 people and wounded 21 at a social services centre in California had an arsenal of weaponry in their home, police said.&lt;/p&gt;&lt;p&gt;Bomb equipment, weapons and thousands of rounds of ammunition were found by police in a raid after a shootout that killed the two suspects.&lt;/p&gt;&lt;p&gt;Authorities still have not found a motive in the attack by Syed Rizwan Farook, 28, and Tashfeen Malik, 27.&lt;/p&gt;&lt;p&gt;Police said the attack indicated there had been &quot;some degree of planning&quot;&lt;strong&gt;.&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;San Bernardino Police Chief Jarrod Burguan said it appeared that the duo was prepared to carry out another attack.&lt;/p&gt;&lt;div aria-hidden=&quot;true&quot; class=&quot;bbccom_slot mpu-ad&quot; id=&quot;bbccom_mpu_1_2_3&quot;&gt;
&lt;div class=&quot;bbccom_advert&quot;&gt;
&lt;script type=&quot;text/javascript&quot;&gt;
            /**/
            (function() {
                if (window.bbcdotcom &amp;&amp; bbcdotcom.adverts &amp;&amp; bbcdotcom.adverts.slotAsync) {
                    bbcdotcom.adverts.slotAsync(&#39;mpu&#39;, [1,2,3]);
                }
            })();
            /**/
        &lt;/script&gt;
&lt;/div&gt;
&lt;/div&gt;&lt;p&gt;&quot;There was obviously a mission here. We know that. We do not know why. We don&#39;t know if this was the intended target or if there was something that triggered him to do this immediately,&quot; said David Bowdich, assistant director of the FBI&#39;s Los Angeles office.&lt;/p&gt;&lt;p&gt;In the shootout with police hours after the attack, Farook and Malik fired 76 rounds of ammunition at the officers and the officers fired 380 rounds back.&lt;/p&gt;&lt;p&gt;Two police officers were injured during the pursuit.&lt;/p&gt; &lt;p&gt;It marks the deadliest mass shooting in the US since 26 people were killed at a school in Newtown, Connecticut in 2012.&lt;/p&gt;&lt;hr class=&quot;story-body__line&quot;&gt;&lt;h2 class=&quot;story-body__crosshead&quot;&gt;San Bernardino shooting - in depth&lt;/h2&gt;&lt;figure class=&quot;media-with-caption&quot;&gt;
&lt;div class=&quot;media-player-wrapper&quot;&gt;
&lt;figure class=&quot;js-media-player-unprocessed media-player&quot; data-playable=&#39;{&quot;settings&quot;:{&quot;counterName&quot;:&quot;news.world.us_and_canada.story.35000998.page&quot;,&quot;edition&quot;:&quot;Domestic&quot;,&quot;pageType&quot;:&quot;eav2&quot;,&quot;uniqueID&quot;:&quot;35000998&quot;,&quot;ui&quot;:{&quot;locale&quot;:{&quot;lang&quot;:&quot;en-gb&quot;}},&quot;externalEmbedUrl&quot;:&quot;http:\/\/www.bbc.co.uk\/news\/world-us-canada-35000998\/embed&quot;,&quot;insideIframe&quot;:false,&quot;playlistObject&quot;:{&quot;title&quot;:&quot;This is how events unfolded.&quot;,&quot;holdingImageURL&quot;:null,&quot;guidance&quot;:null,&quot;simulcast&quot;:false,&quot;liveRewind&quot;:false,&quot;embedRights&quot;:&quot;blocked&quot;,&quot;items&quot;:[{&quot;vpid&quot;:&quot;p03b0j76&quot;,&quot;live&quot;:false,&quot;duration&quot;:134,&quot;kind&quot;:&quot;programme&quot;}],&quot;summary&quot;:&quot;This is how events unfolded.&quot;}},&quot;otherSettings&quot;:{&quot;advertisingAllowed&quot;:true,&quot;continuousPlayCfg&quot;:{&quot;enabled&quot;:false},&quot;isAutoplayOnForAudience&quot;:false,&quot;unProcessedImageUrl&quot;:&quot;http:\/\/ichef-1.bbci.co.uk\/news\/640\/cpsprodpb\/C2CE\/production\/_87007894_87007893.jpg&quot;}}&#39;&gt;&lt;/figure&gt;
&lt;/div&gt;... &lt;trimmed 8758 bytes string&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
          
        </li>
      
    </ul>
  </div>
  
  <form action="http://dpaste.com/" name="pasteform" id="pasteform" method="post">

  <div id="pastebinTraceback" class="pastebin">
    <input type="hidden" name="language" value="PythonConsole">
    <input type="hidden" name="title"
      value="TypeError at /">
    <input type="hidden" name="source" value="Django Dpaste Agent">
    <input type="hidden" name="poster" value="Django">
    <textarea name="content" id="traceback_area" cols="140" rows="25">
Environment:


Request Method: GET
Request URL: http://127.0.0.1:8000/

Django Version: 1.8.7
Python Version: 3.5.0
Installed Applications:
(&#39;django.contrib.admin&#39;,
 &#39;django.contrib.auth&#39;,
 &#39;django.contrib.contenttypes&#39;,
 &#39;django.contrib.sessions&#39;,
 &#39;django.contrib.messages&#39;,
 &#39;django.contrib.staticfiles&#39;,
 &#39;news&#39;)
Installed Middleware:
(&#39;django.contrib.sessions.middleware.SessionMiddleware&#39;,
 &#39;django.middleware.common.CommonMiddleware&#39;,
 &#39;django.middleware.csrf.CsrfViewMiddleware&#39;,
 &#39;django.contrib.auth.middleware.AuthenticationMiddleware&#39;,
 &#39;django.contrib.auth.middleware.SessionAuthenticationMiddleware&#39;,
 &#39;django.contrib.messages.middleware.MessageMiddleware&#39;,
 &#39;django.middleware.clickjacking.XFrameOptionsMiddleware&#39;,
 &#39;django.middleware.security.SecurityMiddleware&#39;)


Traceback:
File "C:\Users\Miles\AppData\Local\Programs\Python\Python35-32\lib\site-packages\django\core\handlers\base.py" in get_response
  132.                     response = wrapped_callback(request, *callback_args, **callback_kwargs)
File "C:\Users\Miles\Documents\GitHub\news-graph\newsgraph\news\views.py" in index
  55. 				content = cleaner.handle(content)
File "C:\Users\Miles\AppData\Local\Programs\Python\Python35-32\lib\site-packages\html2text\__init__.py" in handle
  129.         self.feed(data)
File "C:\Users\Miles\AppData\Local\Programs\Python\Python35-32\lib\site-packages\html2text\__init__.py" in feed
  125.         data = data.replace(&quot;&lt;/&#39; + &#39;script&gt;&quot;, &quot;&lt;/ignore&gt;&quot;)

Exception Type: TypeError at /
Exception Value: &#39;NoneType&#39; object is not callable
</textarea>
  <br><br>
  <input type="submit" value="Share this traceback on a public Web site">
  </div>
</form>
</div>



<div id="requestinfo">
  <h2>Request information</h2>


  <h3 id="get-info">GET</h3>
  
    <p>No GET data</p>
  

  <h3 id="post-info">POST</h3>
  
    <p>No POST data</p>
  
  <h3 id="files-info">FILES</h3>
  
    <p>No FILES data</p>
  


  <h3 id="cookie-info">COOKIES</h3>
  
    <table class="req">
      <thead>
        <tr>
          <th>Variable</th>
          <th>Value</th>
        </tr>
      </thead>
      <tbody>
        
          <tr>
            <td>csrftoken</td>
            <td class="code"><pre>&#39;SICpi4lBvSpqYHYhoFiJ3wql1WmIAKA3&#39;</pre></td>
          </tr>
        
          <tr>
            <td>sessionid</td>
            <td class="code"><pre>&#39;f0xs8zzcejuvo8grr5dvk61p7dhf958g&#39;</pre></td>
          </tr>
        
      </tbody>
    </table>
  

  <h3 id="meta-info">META</h3>
  <table class="req">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>CONTENT_LENGTH</td>
          <td class="code"><pre>&#39;&#39;</pre></td>
        </tr>
      
        <tr>
          <td>FP_NO_HOST_CHECK</td>
          <td class="code"><pre>&#39;NO&#39;</pre></td>
        </tr>
      
        <tr>
          <td>WINDIR</td>
          <td class="code"><pre>&#39;C:\\WINDOWS&#39;</pre></td>
        </tr>
      
        <tr>
          <td>USERDOMAIN</td>
          <td class="code"><pre>&#39;MILES-PC&#39;</pre></td>
        </tr>
      
        <tr>
          <td>QUERY_STRING</td>
          <td class="code"><pre>&#39;&#39;</pre></td>
        </tr>
      
        <tr>
          <td>USERNAME</td>
          <td class="code"><pre>&#39;Miles&#39;</pre></td>
        </tr>
      
        <tr>
          <td>PROGRAMFILES</td>
          <td class="code"><pre>&#39;C:\\Program Files (x86)&#39;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_DNT</td>
          <td class="code"><pre>&#39;1&#39;</pre></td>
        </tr>
      
        <tr>
          <td>VS140COMNTOOLS</td>
          <td class="code"><pre>&#39;C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\Common7\\Tools\\&#39;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE</td>
          <td class="code"><pre>&#39;SICpi4lBvSpqYHYhoFiJ3wql1WmIAKA3&#39;</pre></td>
        </tr>
      
        <tr>
          <td>APPDATA</td>
          <td class="code"><pre>&#39;C:\\Users\\Miles\\AppData\\Roaming&#39;</pre></td>
        </tr>
      
        <tr>
          <td>TMP</td>
          <td class="code"><pre>&#39;C:\\Users\\Miles\\AppData\\Local\\Temp&#39;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multiprocess</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>PATH_INFO</td>
          <td class="code"><pre>&#39;/&#39;</pre></td>
        </tr>
      
        <tr>
          <td>COMMONPROGRAMFILES(X86)</td>
          <td class="code"><pre>&#39;C:\\Program Files (x86)\\Common Files&#39;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multithread</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>PROGRAMW6432</td>
          <td class="code"><pre>&#39;C:\\Program Files&#39;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.run_once</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.url_scheme</td>
          <td class="code"><pre>&#39;http&#39;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT_LANGUAGE</td>
          <td class="code"><pre>&#39;en-US,en;q=0.8,en-GB;q=0.6&#39;</pre></td>
        </tr>
      
        <tr>
          <td>COMMONPROGRAMW6432</td>
          <td class="code"><pre>&#39;C:\\Program Files\\Common Files&#39;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.file_wrapper</td>
          <td class="code"><pre>&#39;&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_NAME</td>
          <td class="code"><pre>&#39;Miles-PC&#39;</pre></td>
        </tr>
      
        <tr>
          <td>PSMODULEPATH</td>
          <td class="code"><pre>&#39;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules\\&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_SOFTWARE</td>
          <td class="code"><pre>&#39;WSGIServer/0.2&#39;</pre></td>
        </tr>
      
        <tr>
          <td>PROCESSOR_ARCHITECTURE</td>
          <td class="code"><pre>&#39;x86&#39;</pre></td>
        </tr>
      
        <tr>
          <td>USERDOMAIN_ROAMINGPROFILE</td>
          <td class="code"><pre>&#39;MILES-PC&#39;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.errors</td>
          <td class="code"><pre>&lt;_io.TextIOWrapper name=&#39;&lt;stderr&gt;&#39; mode=&#39;w&#39; encoding=&#39;cp850&#39;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PORT</td>
          <td class="code"><pre>&#39;8000&#39;</pre></td>
        </tr>
      
        <tr>
          <td>COMSPEC</td>
          <td class="code"><pre>&#39;C:\\WINDOWS\\system32\\cmd.exe&#39;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_UPGRADE_INSECURE_REQUESTS</td>
          <td class="code"><pre>&#39;1&#39;</pre></td>
        </tr>
      
        <tr>
          <td>PROCESSOR_ARCHITEW6432</td>
          <td class="code"><pre>&#39;AMD64&#39;</pre></td>
        </tr>
      
        <tr>
          <td>ALLUSERSPROFILE</td>
          <td class="code"><pre>&#39;C:\\ProgramData&#39;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT_ENCODING</td>
          <td class="code"><pre>&#39;gzip, deflate, sdch&#39;</pre></td>
        </tr>
      
        <tr>
          <td>PROGRAMFILES(X86)</td>
          <td class="code"><pre>&#39;C:\\Program Files (x86)&#39;</pre></td>
        </tr>
      
        <tr>
          <td>REQUEST_METHOD</td>
          <td class="code"><pre>&#39;GET&#39;</pre></td>
        </tr>
      
        <tr>
          <td>GATEWAY_INTERFACE</td>
          <td class="code"><pre>&#39;CGI/1.1&#39;</pre></td>
        </tr>
      
        <tr>
          <td>OS</td>
          <td class="code"><pre>&#39;Windows_NT&#39;</pre></td>
        </tr>
      
        <tr>
          <td>LOCALAPPDATA</td>
          <td class="code"><pre>&#39;C:\\Users\\Miles\\AppData\\Local&#39;</pre></td>
        </tr>
      
        <tr>
          <td>PROMPT</td>
          <td class="code"><pre>&#39;$P$G&#39;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT</td>
          <td class="code"><pre>&#39;text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8&#39;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_COOKIE</td>
          <td class="code"><pre>(&#39;sessionid=f0xs8zzcejuvo8grr5dvk61p7dhf958g; &#39;
 &#39;csrftoken=SICpi4lBvSpqYHYhoFiJ3wql1WmIAKA3&#39;)</pre></td>
        </tr>
      
        <tr>
          <td>USERPROFILE</td>
          <td class="code"><pre>&#39;C:\\Users\\Miles&#39;</pre></td>
        </tr>
      
        <tr>
          <td>VBOX_MSI_INSTALL_PATH</td>
          <td class="code"><pre>&#39;C:\\Program Files\\Oracle\\VirtualBox\\&#39;</pre></td>
        </tr>
      
        <tr>
          <td>RUN_MAIN</td>
          <td class="code"><pre>&#39;true&#39;</pre></td>
        </tr>
      
        <tr>
          <td>PUBLIC</td>
          <td class="code"><pre>&#39;C:\\Users\\Public&#39;</pre></td>
        </tr>
      
        <tr>
          <td>LYNX_CFG</td>
          <td class="code"><pre>&#39;C:\\Program Files (x86)\\Lynx - web browser\\lynx.cfg&#39;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_HOST</td>
          <td class="code"><pre>&#39;127.0.0.1:8000&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PROTOCOL</td>
          <td class="code"><pre>&#39;HTTP/1.1&#39;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_CACHE_CONTROL</td>
          <td class="code"><pre>&#39;max-age=0&#39;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.version</td>
          <td class="code"><pre>(1, 0)</pre></td>
        </tr>
      
        <tr>
          <td>PROGRAMDATA</td>
          <td class="code"><pre>&#39;C:\\ProgramData&#39;</pre></td>
        </tr>
      
        <tr>
          <td>COMMONPROGRAMFILES</td>
          <td class="code"><pre>&#39;C:\\Program Files (x86)\\Common Files&#39;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_TYPE</td>
          <td class="code"><pre>&#39;text/plain&#39;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_HOST</td>
          <td class="code"><pre>&#39;&#39;</pre></td>
        </tr>
      
        <tr>
          <td>TEMP</td>
          <td class="code"><pre>&#39;C:\\Users\\Miles\\AppData\\Local\\Temp&#39;</pre></td>
        </tr>
      
        <tr>
          <td>LOGONSERVER</td>
          <td class="code"><pre>&#39;\\\\MicrosoftAccount&#39;</pre></td>
        </tr>
      
        <tr>
          <td>PATHEXT</td>
          <td class="code"><pre>&#39;.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC&#39;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEDRIVE</td>
          <td class="code"><pre>&#39;C:&#39;</pre></td>
        </tr>
      
        <tr>
          <td>PATH</td>
          <td class="code"><pre>(&#39;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Program Files (x86)\\NVIDIA &#39;
 &#39;Corporation\\PhysX\\Common;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program &#39;
 &#39;Files (x86)\\AMD\\ATI.ACE\\Core-Static;C:\\Program Files &#39;
 &#39;(x86)\\Skype\\Phone\\;C:\\Program &#39;
 &#39;Files\\nodejs\\;C:\\Users\\Miles\\.dnx\\bin;C:\\Program Files\\Microsoft &#39;
 &#39;DNX\\Dnvm\\;C:\\Program Files (x86)\\Windows Kits\\8.1\\Windows Performance &#39;
 &#39;Toolkit\\;C:\\Program Files\\Git\\cmd;C:\\Program Files &#39;
 &#39;(x86)\\Brackets\\command;C:\\Program Files (x86)\\MiKTeX &#39;
 &#39;2.9\\miktex\\bin\\;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program &#39;
 &#39;Files (x86)\\ATI &#39;
 &#39;Technologies\\ATI.ACE\\Core-Static;C:\\Users\\Miles\\AppData\\Local\\Programs\\Python\\Python35-32\\Scripts\\;C:\\Users\\Miles\\AppData\\Local\\Programs\\Python\\Python35-32\\;C:\\Users\\Miles\\AppData\\Roaming\\npm;C:\\Program &#39;
 &#39;Files (x86)\\pdfToHTML;C:\\python27;C:\\Program Files (x86)\\Microsoft VS &#39;
 &#39;Code\\bin&#39;)</pre></td>
        </tr>
      
        <tr>
          <td>COMPUTERNAME</td>
          <td class="code"><pre>&#39;MILES-PC&#39;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_USER_AGENT</td>
          <td class="code"><pre>(&#39;Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) &#39;
 &#39;Chrome/46.0.2490.86 Safari/537.36&#39;)</pre></td>
        </tr>
      
        <tr>
          <td>PROCESSOR_IDENTIFIER</td>
          <td class="code"><pre>&#39;Intel64 Family 6 Model 60 Stepping 3, GenuineIntel&#39;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.input</td>
          <td class="code"><pre>&lt;_io.BufferedReader name=1004&gt;</pre></td>
        </tr>
      
        <tr>
          <td>PROCESSOR_REVISION</td>
          <td class="code"><pre>&#39;3c03&#39;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_ADDR</td>
          <td class="code"><pre>&#39;127.0.0.1&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SYSTEMROOT</td>
          <td class="code"><pre>&#39;C:\\WINDOWS&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SCRIPT_NAME</td>
          <td class="code"><pre>&#39;&#39;</pre></td>
        </tr>
      
        <tr>
          <td>NUMBER_OF_PROCESSORS</td>
          <td class="code"><pre>&#39;4&#39;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_CONNECTION</td>
          <td class="code"><pre>&#39;keep-alive&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SESSIONNAME</td>
          <td class="code"><pre>&#39;Console&#39;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEPATH</td>
          <td class="code"><pre>&#39;\\Users\\Miles&#39;</pre></td>
        </tr>
      
        <tr>
          <td>PROCESSOR_LEVEL</td>
          <td class="code"><pre>&#39;6&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SYSTEMDRIVE</td>
          <td class="code"><pre>&#39;C:&#39;</pre></td>
        </tr>
      
        <tr>
          <td>DJANGO_SETTINGS_MODULE</td>
          <td class="code"><pre>&#39;newsgraph.settings&#39;</pre></td>
        </tr>
      
    </tbody>
  </table>


  <h3 id="settings-info">Settings</h3>
  <h4>Using settings module <code>newsgraph.settings</code></h4>
  <table class="req">
    <thead>
      <tr>
        <th>Setting</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>SECURE_CONTENT_TYPE_NOSNIFF</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>ALLOWED_HOSTS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_BROWSER_XSS_FILTER</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_CONTENT_TYPE</td>
          <td class="code"><pre>&#39;text/html&#39;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FROM_EMAIL</td>
          <td class="code"><pre>&#39;webmaster@localhost&#39;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_SSL</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SILENCED_SYSTEM_CHECKS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_RUNNER</td>
          <td class="code"><pre>&#39;django.test.runner.DiscoverRunner&#39;</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_TEMP_DIR</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>DECIMAL_SEPARATOR</td>
          <td class="code"><pre>&#39;.&#39;</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_RESET_TIMEOUT_DAYS</td>
          <td class="code"><pre>&#39;********************&#39;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER_FILTER</td>
          <td class="code"><pre>&#39;django.views.debug.SafeExceptionReporterFilter&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY</td>
          <td class="code"><pre>&#39;********************&#39;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FILE_STORAGE</td>
          <td class="code"><pre>&#39;django.core.files.storage.FileSystemStorage&#39;</pre></td>
        </tr>
      
        <tr>
          <td>LOGOUT_URL</td>
          <td class="code"><pre>&#39;/accounts/logout/&#39;</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_STORAGE</td>
          <td class="code"><pre>&#39;django.contrib.staticfiles.storage.StaticFilesStorage&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SERIALIZER</td>
          <td class="code"><pre>&#39;django.contrib.sessions.serializers.JSONSerializer&#39;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_SECONDS</td>
          <td class="code"><pre>600</pre></td>
        </tr>
      
        <tr>
          <td>DATABASES</td>
          <td class="code"><pre>{&#39;default&#39;: {&#39;ATOMIC_REQUESTS&#39;: False,
             &#39;AUTOCOMMIT&#39;: True,
             &#39;CONN_MAX_AGE&#39;: 0,
             &#39;ENGINE&#39;: &#39;django.db.backends.sqlite3&#39;,
             &#39;HOST&#39;: &#39;&#39;,
             &#39;NAME&#39;: &#39;C:\\Users\\Miles\\Documents\\GitHub\\news-graph\\newsgraph\\db.sqlite3&#39;,
             &#39;OPTIONS&#39;: {},
             &#39;PASSWORD&#39;: &#39;********************&#39;,
             &#39;PORT&#39;: &#39;&#39;,
             &#39;TEST&#39;: {&#39;CHARSET&#39;: None,
                      &#39;COLLATION&#39;: None,
                      &#39;MIRROR&#39;: None,
                      &#39;NAME&#39;: None},
             &#39;TIME_ZONE&#39;: &#39;UTC&#39;,
             &#39;USER&#39;: &#39;&#39;}}</pre></td>
        </tr>
      
        <tr>
          <td>FILE_CHARSET</td>
          <td class="code"><pre>&#39;utf-8&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_SECONDS</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_HANDLERS</td>
          <td class="code"><pre>(&#39;django.core.files.uploadhandler.MemoryFileUploadHandler&#39;,
 &#39;django.core.files.uploadhandler.TemporaryFileUploadHandler&#39;)</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_PORT</td>
          <td class="code"><pre>25</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATE_FORMAT</td>
          <td class="code"><pre>&#39;m/d/Y&#39;</pre></td>
        </tr>
      
        <tr>
          <td>DATE_FORMAT</td>
          <td class="code"><pre>&#39;N j, Y&#39;</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_HASHERS</td>
          <td class="code"><pre>&#39;********************&#39;</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_URL</td>
          <td class="code"><pre>&#39;&#39;</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_DIRS</td>
          <td class="code"><pre>()</pre></td>
        </tr>
      
        <tr>
          <td>USE_TZ</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>TEST_NON_SERIALIZED_APPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_REDIRECT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_PASSWORD</td>
          <td class="code"><pre>&#39;********************&#39;</pre></td>
        </tr>
      
        <tr>
          <td>CACHES</td>
          <td class="code"><pre>{&#39;default&#39;: {&#39;BACKEND&#39;: &#39;django.core.cache.backends.locmem.LocMemCache&#39;}}</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATETIME_FORMAT</td>
          <td class="code"><pre>&#39;m/d/Y P&#39;</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_HOST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_CODE</td>
          <td class="code"><pre>&#39;en-us&#39;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_INPUT_FORMATS</td>
          <td class="code"><pre>(&#39;%H:%M:%S&#39;, &#39;%H:%M:%S.%f&#39;, &#39;%H:%M&#39;)</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_AGE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>USE_L10N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_INPUT_FORMATS</td>
          <td class="code"><pre>(&#39;%Y-%m-%d %H:%M:%S&#39;,
 &#39;%Y-%m-%d %H:%M:%S.%f&#39;,
 &#39;%Y-%m-%d %H:%M&#39;,
 &#39;%Y-%m-%d&#39;,
 &#39;%m/%d/%Y %H:%M:%S&#39;,
 &#39;%m/%d/%Y %H:%M:%S.%f&#39;,
 &#39;%m/%d/%Y %H:%M&#39;,
 &#39;%m/%d/%Y&#39;,
 &#39;%m/%d/%y %H:%M:%S&#39;,
 &#39;%m/%d/%y %H:%M:%S.%f&#39;,
 &#39;%m/%d/%y %H:%M&#39;,
 &#39;%m/%d/%y&#39;)</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_CERTFILE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>ABSOLUTE_URL_OVERRIDES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>TEMPLATES</td>
          <td class="code"><pre>[{&#39;APP_DIRS&#39;: True,
  &#39;BACKEND&#39;: &#39;django.template.backends.django.DjangoTemplates&#39;,
  &#39;DIRS&#39;: [],
  &#39;OPTIONS&#39;: {&#39;context_processors&#39;: [&#39;django.template.context_processors.debug&#39;,
                                     &#39;django.template.context_processors.request&#39;,
                                     &#39;django.contrib.auth.context_processors.auth&#39;,
                                     &#39;django.contrib.messages.context_processors.messages&#39;]}}]</pre></td>
        </tr>
      
        <tr>
          <td>MONTH_DAY_FORMAT</td>
          <td class="code"><pre>&#39;F j&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_NAME</td>
          <td class="code"><pre>&#39;sessionid&#39;</pre></td>
        </tr>
      
        <tr>
          <td>FIRST_DAY_OF_WEEK</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES</td>
          <td class="code"><pre>((&#39;af&#39;, &#39;Afrikaans&#39;),
 (&#39;ar&#39;, &#39;Arabic&#39;),
 (&#39;ast&#39;, &#39;Asturian&#39;),
 (&#39;az&#39;, &#39;Azerbaijani&#39;),
 (&#39;bg&#39;, &#39;Bulgarian&#39;),
 (&#39;be&#39;, &#39;Belarusian&#39;),
 (&#39;bn&#39;, &#39;Bengali&#39;),
 (&#39;br&#39;, &#39;Breton&#39;),
 (&#39;bs&#39;, &#39;Bosnian&#39;),
 (&#39;ca&#39;, &#39;Catalan&#39;),
 (&#39;cs&#39;, &#39;Czech&#39;),
 (&#39;cy&#39;, &#39;Welsh&#39;),
 (&#39;da&#39;, &#39;Danish&#39;),
 (&#39;de&#39;, &#39;German&#39;),
 (&#39;el&#39;, &#39;Greek&#39;),
 (&#39;en&#39;, &#39;English&#39;),
 (&#39;en-au&#39;, &#39;Australian English&#39;),
 (&#39;en-gb&#39;, &#39;British English&#39;),
 (&#39;eo&#39;, &#39;Esperanto&#39;),
 (&#39;es&#39;, &#39;Spanish&#39;),
 (&#39;es-ar&#39;, &#39;Argentinian Spanish&#39;),
 (&#39;es-mx&#39;, &#39;Mexican Spanish&#39;),
 (&#39;es-ni&#39;, &#39;Nicaraguan Spanish&#39;),
 (&#39;es-ve&#39;, &#39;Venezuelan Spanish&#39;),
 (&#39;et&#39;, &#39;Estonian&#39;),
 (&#39;eu&#39;, &#39;Basque&#39;),
 (&#39;fa&#39;, &#39;Persian&#39;),
 (&#39;fi&#39;, &#39;Finnish&#39;),
 (&#39;fr&#39;, &#39;French&#39;),
 (&#39;fy&#39;, &#39;Frisian&#39;),
 (&#39;ga&#39;, &#39;Irish&#39;),
 (&#39;gl&#39;, &#39;Galician&#39;),
 (&#39;he&#39;, &#39;Hebrew&#39;),
 (&#39;hi&#39;, &#39;Hindi&#39;),
 (&#39;hr&#39;, &#39;Croatian&#39;),
 (&#39;hu&#39;, &#39;Hungarian&#39;),
 (&#39;ia&#39;, &#39;Interlingua&#39;),
 (&#39;id&#39;, &#39;Indonesian&#39;),
 (&#39;io&#39;, &#39;Ido&#39;),
 (&#39;is&#39;, &#39;Icelandic&#39;),
 (&#39;it&#39;, &#39;Italian&#39;),
 (&#39;ja&#39;, &#39;Japanese&#39;),
 (&#39;ka&#39;, &#39;Georgian&#39;),
 (&#39;kk&#39;, &#39;Kazakh&#39;),
 (&#39;km&#39;, &#39;Khmer&#39;),
 (&#39;kn&#39;, &#39;Kannada&#39;),
 (&#39;ko&#39;, &#39;Korean&#39;),
 (&#39;lb&#39;, &#39;Luxembourgish&#39;),
 (&#39;lt&#39;, &#39;Lithuanian&#39;),
 (&#39;lv&#39;, &#39;Latvian&#39;),
 (&#39;mk&#39;, &#39;Macedonian&#39;),
 (&#39;ml&#39;, &#39;Malayalam&#39;),
 (&#39;mn&#39;, &#39;Mongolian&#39;),
 (&#39;mr&#39;, &#39;Marathi&#39;),
 (&#39;my&#39;, &#39;Burmese&#39;),
 (&#39;nb&#39;, &#39;Norwegian Bokmal&#39;),
 (&#39;ne&#39;, &#39;Nepali&#39;),
 (&#39;nl&#39;, &#39;Dutch&#39;),
 (&#39;nn&#39;, &#39;Norwegian Nynorsk&#39;),
 (&#39;os&#39;, &#39;Ossetic&#39;),
 (&#39;pa&#39;, &#39;Punjabi&#39;),
 (&#39;pl&#39;, &#39;Polish&#39;),
 (&#39;pt&#39;, &#39;Portuguese&#39;),
 (&#39;pt-br&#39;, &#39;Brazilian Portuguese&#39;),
 (&#39;ro&#39;, &#39;Romanian&#39;),
 (&#39;ru&#39;, &#39;Russian&#39;),
 (&#39;sk&#39;, &#39;Slovak&#39;),
 (&#39;sl&#39;, &#39;Slovenian&#39;),
 (&#39;sq&#39;, &#39;Albanian&#39;),
 (&#39;sr&#39;, &#39;Serbian&#39;),
 (&#39;sr-latn&#39;, &#39;Serbian Latin&#39;),
 (&#39;sv&#39;, &#39;Swedish&#39;),
 (&#39;sw&#39;, &#39;Swahili&#39;),
 (&#39;ta&#39;, &#39;Tamil&#39;),
 (&#39;te&#39;, &#39;Telugu&#39;),
 (&#39;th&#39;, &#39;Thai&#39;),
 (&#39;tr&#39;, &#39;Turkish&#39;),
 (&#39;tt&#39;, &#39;Tatar&#39;),
 (&#39;udm&#39;, &#39;Udmurt&#39;),
 (&#39;uk&#39;, &#39;Ukrainian&#39;),
 (&#39;ur&#39;, &#39;Urdu&#39;),
 (&#39;vi&#39;, &#39;Vietnamese&#39;),
 (&#39;zh-cn&#39;, &#39;Simplified Chinese&#39;),
 (&#39;zh-hans&#39;, &#39;Simplified Chinese&#39;),
 (&#39;zh-hant&#39;, &#39;Traditional Chinese&#39;),
 (&#39;zh-tw&#39;, &#39;Traditional Chinese&#39;))</pre></td>
        </tr>
      
        <tr>
          <td>WSGI_APPLICATION</td>
          <td class="code"><pre>&#39;newsgraph.wsgi.application&#39;</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_PERMISSIONS</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_AGE</td>
          <td class="code"><pre>1209600</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_NAME</td>
          <td class="code"><pre>&#39;django_language&#39;</pre></td>
        </tr>
      
        <tr>
          <td>TEMPLATE_DIRS</td>
          <td class="code"><pre>()</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_CACHE_ALIAS</td>
          <td class="code"><pre>&#39;default&#39;</pre></td>
        </tr>
      
        <tr>
          <td>USE_THOUSAND_SEPARATOR</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>BASE_DIR</td>
          <td class="code"><pre>&#39;C:\\Users\\Miles\\Documents\\GitHub\\news-graph\\newsgraph&#39;</pre></td>
        </tr>
      
        <tr>
          <td>MANAGERS</td>
          <td class="code"><pre>()</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_USER_MODEL</td>
          <td class="code"><pre>&#39;auth.User&#39;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_TIMEOUT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>MIDDLEWARE_CLASSES</td>
          <td class="code"><pre>(&#39;django.contrib.sessions.middleware.SessionMiddleware&#39;,
 &#39;django.middleware.common.CommonMiddleware&#39;,
 &#39;django.middleware.csrf.CsrfViewMiddleware&#39;,
 &#39;django.contrib.auth.middleware.AuthenticationMiddleware&#39;,
 &#39;django.contrib.auth.middleware.SessionAuthenticationMiddleware&#39;,
 &#39;django.contrib.messages.middleware.MessageMiddleware&#39;,
 &#39;django.middleware.clickjacking.XFrameOptionsMiddleware&#39;,
 &#39;django.middleware.security.SecurityMiddleware&#39;)</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING_CONFIG</td>
          <td class="code"><pre>&#39;logging.config.dictConfig&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_INCLUDE_SUBDOMAINS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>ROOT_URLCONF</td>
          <td class="code"><pre>&#39;newsgraph.urls&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_ENGINE</td>
          <td class="code"><pre>&#39;django.contrib.sessions.backends.db&#39;</pre></td>
        </tr>
      
        <tr>
          <td>APPEND_SLASH</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>IGNORABLE_404_URLS</td>
          <td class="code"><pre>()</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_CHARSET</td>
          <td class="code"><pre>&#39;utf-8&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_EXPIRE_AT_BROWSER_CLOSE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_TABLESPACE</td>
          <td class="code"><pre>&#39;&#39;</pre></td>
        </tr>
      
        <tr>
          <td>YEAR_MONTH_FORMAT</td>
          <td class="code"><pre>&#39;F Y&#39;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_USER</td>
          <td class="code"><pre>&#39;&#39;</pre></td>
        </tr>
      
        <tr>
          <td>ALLOWED_INCLUDE_ROOTS</td>
          <td class="code"><pre>()</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_DIRECTORY_PERMISSIONS</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REDIRECT_EXEMPT</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>AUTHENTICATION_BACKENDS</td>
          <td class="code"><pre>(&#39;django.contrib.auth.backends.ModelBackend&#39;,)</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_KEY_PREFIX</td>
          <td class="code"><pre>&#39;********************&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SIGNING_BACKEND</td>
          <td class="code"><pre>&#39;django.core.signing.TimestampSigner&#39;</pre></td>
        </tr>
      
        <tr>
          <td>X_FRAME_OPTIONS</td>
          <td class="code"><pre>&#39;SAMEORIGIN&#39;</pre></td>
        </tr>
      
        <tr>
          <td>USE_I18N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_FINDERS</td>
          <td class="code"><pre>(&#39;django.contrib.staticfiles.finders.FileSystemFinder&#39;,
 &#39;django.contrib.staticfiles.finders.AppDirectoriesFinder&#39;)</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST</td>
          <td class="code"><pre>&#39;localhost&#39;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_TLS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_FAILURE_VIEW</td>
          <td class="code"><pre>&#39;django.views.csrf.csrf_failure&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_PATH</td>
          <td class="code"><pre>&#39;/&#39;</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG_PROPAGATE_EXCEPTIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>MESSAGE_STORAGE</td>
          <td class="code"><pre>&#39;django.contrib.messages.storage.fallback.FallbackStorage&#39;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES_BIDI</td>
          <td class="code"><pre>(&#39;he&#39;, &#39;ar&#39;, &#39;fa&#39;, &#39;ur&#39;)</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_ALIAS</td>
          <td class="code"><pre>&#39;default&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_EMAIL</td>
          <td class="code"><pre>&#39;root@localhost&#39;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_INDEX_TABLESPACE</td>
          <td class="code"><pre>&#39;&#39;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_REDIRECT_URL</td>
          <td class="code"><pre>&#39;/accounts/profile/&#39;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_KEYFILE</td>
          <td class="code"><pre>&#39;********************&#39;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_BACKEND</td>
          <td class="code"><pre>&#39;django.core.mail.backends.smtp.EmailBackend&#39;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_NAME</td>
          <td class="code"><pre>&#39;csrftoken&#39;</pre></td>
        </tr>
      
        <tr>
          <td>USE_ETAGS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>TEMPLATE_DEBUG</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>THOUSAND_SEPARATOR</td>
          <td class="code"><pre>&#39;,&#39;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SAVE_EVERY_REQUEST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_ROOT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>TIME_FORMAT</td>
          <td class="code"><pre>&#39;P&#39;</pre></td>
        </tr>
      
        <tr>
          <td>DISALLOWED_USER_AGENTS</td>
          <td class="code"><pre>()</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_HTTPONLY</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>ADMINS</td>
          <td class="code"><pre>()</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_AGE</td>
          <td class="code"><pre>31449600</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_PATH</td>
          <td class="code"><pre>&#39;/&#39;</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_URL</td>
          <td class="code"><pre>&#39;/static/&#39;</pre></td>
        </tr>
      
        <tr>
          <td>FORMAT_MODULE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>DATABASE_ROUTERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>DATE_INPUT_FORMATS</td>
          <td class="code"><pre>(&#39;%Y-%m-%d&#39;,
 &#39;%m/%d/%Y&#39;,
 &#39;%m/%d/%y&#39;,
 &#39;%b %d %Y&#39;,
 &#39;%b %d, %Y&#39;,
 &#39;%d %b %Y&#39;,
 &#39;%d %b, %Y&#39;,
 &#39;%B %d %Y&#39;,
 &#39;%B %d, %Y&#39;,
 &#39;%d %B %Y&#39;,
 &#39;%d %B, %Y&#39;)</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_FILE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>TEMPLATE_STRING_IF_INVALID</td>
          <td class="code"><pre>&#39;&#39;</pre></td>
        </tr>
      
        <tr>
          <td>INSTALLED_APPS</td>
          <td class="code"><pre>(&#39;django.contrib.admin&#39;,
 &#39;django.contrib.auth&#39;,
 &#39;django.contrib.contenttypes&#39;,
 &#39;django.contrib.sessions&#39;,
 &#39;django.contrib.messages&#39;,
 &#39;django.contrib.staticfiles&#39;,
 &#39;news&#39;)</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_ROOT</td>
          <td class="code"><pre>&#39;&#39;</pre></td>
        </tr>
      
        <tr>
          <td>LOCALE_PATHS</td>
          <td class="code"><pre>()</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_FORMAT</td>
          <td class="code"><pre>&#39;N j, Y, P&#39;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_ZONE</td>
          <td class="code"><pre>&#39;UTC&#39;</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_PROXY_SSL_HEADER</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_SCRIPT_NAME</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SETTINGS_MODULE</td>
          <td class="code"><pre>&#39;newsgraph.settings&#39;</pre></td>
        </tr>
      
        <tr>
          <td>TEMPLATE_CONTEXT_PROCESSORS</td>
          <td class="code"><pre>(&#39;django.contrib.auth.context_processors.auth&#39;,
 &#39;django.template.context_processors.debug&#39;,
 &#39;django.template.context_processors.i18n&#39;,
 &#39;django.template.context_processors.media&#39;,
 &#39;django.template.context_processors.static&#39;,
 &#39;django.template.context_processors.tz&#39;,
 &#39;django.contrib.messages.context_processors.messages&#39;)</pre></td>
        </tr>
      
        <tr>
          <td>NUMBER_GROUPING</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_PATH</td>
          <td class="code"><pre>&#39;/&#39;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_URL</td>
          <td class="code"><pre>&#39;/accounts/login/&#39;</pre></td>
        </tr>
      
        <tr>
          <td>TEMPLATE_LOADERS</td>
          <td class="code"><pre>(&#39;django.template.loaders.filesystem.Loader&#39;,
 &#39;django.template.loaders.app_directories.Loader&#39;)</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>PREPEND_WWW</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SUBJECT_PREFIX</td>
          <td class="code"><pre>&#39;[Django] &#39;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_HOST</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FIXTURE_DIRS</td>
          <td class="code"><pre>()</pre></td>
        </tr>
      
        <tr>
          <td>INTERNAL_IPS</td>
          <td class="code"><pre>()</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>MIGRATION_MODULES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
    </tbody>
  </table>

</div>

  <div id="explanation">
    <p>
      You're seeing this error because you have <code>DEBUG = True</code> in your
      Django settings file. Change that to <code>False</code>, and Django will
      display a standard page generated by the handler for this status code.
    </p>
  </div>

</body>
</html>


"""
cleaner = html2text.HTML2Text()
cleaner.ignore_links = True
content = cleaner.handle(content)
print(content)