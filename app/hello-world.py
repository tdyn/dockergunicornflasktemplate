from flask import Flask
import configparser,sys,os
app = Flask(__name__)

print(" Running Your App!")
#setting configuration
conf = configparser.ConfigParser()
conf.read(filenames=os.environ["pyconf"])

@app.route('/')
def hello():
    return """
    <style>
    @import url(
  https://fonts.googleapis.com/css?family=Roboto:400,
  100,
  300,
  500,
  700
);

body {
  background: #eeeef4;
  color: #999;
  font-family: Roboto;
}

h1 {
  font-weight: 100;
  font-size: 27pt;
  color: #e43;
}

p {
  font-weight: 300;
}

.warning-content {
  position: absolute;
  top: 25%;
  width: 100%;
  height: 300px;
  text-align: center;
  margin: 0;
}
 </style>
 <body>
 <div class="warning-content">
  <h1>New Site Under Construction</h1>
  <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="100.001px" height="70px" viewBox="0 0 100 68">
    <g id="large">
      <g>
        <path d="M55.777,38.473l6.221-1.133c0.017-1.791-0.123-3.573-0.41-5.324l-6.321-0.19c-0.438-2.053-1.135-4.048-2.076-5.931
		l4.82-4.094c-0.868-1.552-1.874-3.028-3.005-4.417l-5.569,2.999c-1.385-1.54-2.98-2.921-4.771-4.099l2.124-5.954
		c-0.759-0.452-1.543-0.878-2.357-1.269c-0.811-0.39-1.625-0.732-2.449-1.046l-3.325,5.381c-2.038-0.665-4.113-1.052-6.183-1.174
		L31.34,6.002c-1.792-0.02-3.571,0.119-5.32,0.406l-0.191,6.32c-2.056,0.439-4.051,1.137-5.936,2.08l-4.097-4.82
		c-1.546,0.872-3.022,1.875-4.407,3.006l2.996,5.566c-1.54,1.384-2.925,2.985-4.104,4.778c-2.16-0.771-4.196-1.498-5.953-2.127
		c-0.449,0.765-0.875,1.544-1.265,2.354c-0.39,0.811-0.733,1.63-1.049,2.457c1.587,0.981,3.424,2.119,5.377,3.325
		c-0.662,2.037-1.049,4.117-1.172,6.186l-6.218,1.136c-0.021,1.789,0.12,3.566,0.407,5.321l6.32,0.188
		c0.442,2.06,1.143,4.057,2.082,5.937l-4.818,4.095c0.872,1.549,1.873,3.026,3.009,4.412l5.563-2.998
		c1.392,1.54,2.989,2.92,4.777,4.099l-2.121,5.954c0.756,0.446,1.538,0.871,2.348,1.258c0.813,0.394,1.633,0.739,2.462,1.05
		l3.326-5.375c2.033,0.662,4.109,1.05,6.175,1.17l1.137,6.221c1.791,0.019,3.569-0.123,5.323-0.407l0.194-6.324
		c2.053-0.438,4.045-1.136,5.927-2.079l4.093,4.817c1.55-0.865,3.026-1.87,4.414-2.999l-2.995-5.572
		c1.537-1.385,2.914-2.98,4.093-4.772l5.953,2.127c0.448-0.761,0.878-1.545,1.268-2.356c0.388-0.808,0.729-1.631,1.047-2.458
		l-5.378-3.324C55.268,42.615,55.655,40.542,55.777,38.473z M42.302,42.435c-3.002,6.243-10.495,8.872-16.737,5.866
		c-6.244-2.999-8.872-10.493-5.867-16.736c3.002-6.244,10.495-8.873,16.736-5.869C42.676,28.698,45.306,36.19,42.302,42.435z" fill="none" stroke="#E43" />
        <animateTransform attributeName="transform" begin="0s" dur="3s" type="rotate" from="0 31 37" to="360 31 37" repeatCount="indefinite" </animateTransform>
      </g>
      <g id="small">
        <path d="M93.068,19.253L99,16.31c-0.371-1.651-0.934-3.257-1.679-4.776l-6.472,1.404c-0.902-1.436-2.051-2.735-3.42-3.819
		l2.115-6.273c-0.706-0.448-1.443-0.867-2.213-1.238c-0.774-0.371-1.559-0.685-2.351-0.958l-3.584,5.567
		c-1.701-0.39-3.432-0.479-5.118-0.284L73.335,0c-1.652,0.367-3.256,0.931-4.776,1.672l1.404,6.47
		c-1.439,0.899-2.744,2.047-3.835,3.419c-2.208-0.746-4.38-1.476-6.273-2.114c-0.451,0.71-0.874,1.448-1.244,2.229
		c-0.371,0.764-0.68,1.541-0.954,2.329c1.681,1.078,3.612,2.323,5.569,3.579c-0.399,1.711-0.486,3.449-0.291,5.145
		c-2.086,1.034-4.143,2.055-5.936,2.945c0.368,1.648,0.929,3.25,1.67,4.769c1.954-0.426,4.193-0.912,6.468-1.405
		c0.906,1.449,2.06,2.758,3.442,3.853l-2.117,6.27c0.708,0.449,1.439,0.865,2.218,1.236c0.767,0.371,1.551,0.685,2.338,0.96
		c1.081-1.68,2.319-3.612,3.583-5.574c1.714,0.401,3.457,0.484,5.156,0.288L82.695,42c1.651-0.371,3.252-0.931,4.773-1.676
		c-0.425-1.952-0.912-4.194-1.404-6.473c1.439-0.902,2.744-2.057,3.835-3.436l6.273,2.11c0.444-0.7,0.856-1.43,1.225-2.197
		c0.372-0.777,0.691-1.569,0.963-2.361l-5.568-3.586C93.181,22.677,93.269,20.939,93.068,19.253z M84.365,24.062
		c-1.693,3.513-5.908,4.991-9.418,3.302c-3.513-1.689-4.99-5.906-3.301-9.419c1.688-3.513,5.906-4.991,9.417-3.302
		C84.573,16.331,86.05,20.549,84.365,24.062z" fill="none" stroke="#E43" />
        <animateTransform attributeName="transform" begin="0s" dur="2s" type="rotate" from="0 78 21" to="-360 78 21" repeatCount="indefinite" </animateTransform>
      </g>
  </svg>
  <p>
    Please forgive the inconvenience. <br />
    We are currently initializing our brand new site.
  </p>
  <p>
    It's okay, we're excited too!
  </p>

</div>
 </body>
    """
import subprocess
import sys
def shell_output(param):
    """
        This method just takes the shell commands to be executed and returns what
        this command outputs in shell
        :param param: command (example "ls")
        :return: string of commands output on shell
        """
    try:
        #the power of this function shall not be looked down,
        #if you are an admin, you know what it is to have a
        #shell command that can do job for you
        #what if I say, you can leverage the power python brings to you
        #and also the shell commands combined? is it not a gizmo for you?
        #well atleast it is sure an important thing for me
        #do not touch the variable x, it is but to make a
        #comfortable operation and to make use of it later
        x = ((subprocess.Popen(
                    [str(param)],#takes each part of command as a list element, but bro! i can also pass everything
                                 # in one element
                    shell=True,#to run in shell
                    bufsize=0, #need to check why
                    stdout=subprocess.PIPE, #to give it to pipe
                    stderr=subprocess.PIPE, #to give errors also to pipe
                    universal_newlines=False,#shall it include the newline charecters?
                                             # i wonder if anyone likes it that way
                                             #it gives a list instead of string
                )).communicate()[0]#this is to get the value from shell
            .decode("utf-8")#this is to remove 'b i.e to convert from byte to string
        ).strip()
        return x #this function does only one thing, but does it quiet well.
    except Exception as e:
        print("Error with execution in get_str " + str(e))
        return e

@app.route('/stats')
def stats():
	return shell_output("awk '{ print $1 } '/tmp/logfile'| uniq") 

if __name__ == '__main__':
    app.run(host=conf.get("default","host"))
