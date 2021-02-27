# NAME

stats - calcurate statistics of values in each column

# SYNOPSIS

  stats [-v] [-t type[,type...]] [file...]

# DESCRIPTION

This manual page documents *stats*.  This program is for calcurating various
statistics of values in each column.  *stats* can compute several statistics:
the number of values, sum, minimum, maximum, mean, variance, standard
deviation, coefficient of variation, 25%/50%/75% quantiles, and 90%/95%/99%
confidence interlvals.  *stats* can also compute statistic for multiple data
sets: covariance and correlation coefficient.

*stats* calcurates statistics of numbers in all lines, located at the same
column position.  For instance, if the input file has N colums, *stats*
displays statistics for all N columns.

The input file format of *stats* is a typical plain text; each column is
seperated by whitespace, and each value is any valid Python float.  See
Python references for `float()` function and floating point literals.

- class float([x])
  https://docs.python.org/3/library/functions.html#float

- 2.4.6. Floating point literals¶
  https://docs.python.org/3/reference/lexical_analysis.html#floating

# OPTIONS

`-v`

Display label for each statistic.

`-a`

Display all statistics.

`-t type[,type...]`

Specify statistic to display.  *type* must be one of the following keywordss.

```
count      the number of values
sum        sum
min        minimum
max        maximum
mean       sample mean
median     median
mode       mode
var        sample variance
stddev     standard deviation
skew       skewness
kurt       kurtosis
cv         coefficient of variation
quant10    10% quantile
quant25    25% quantile
quant50    50% quantile
quant75    75% quantile
quant90    90% quantile
conf90     90% confidence interval
conf95     95% confidence interval
conf99     99% confidence interval
covar      covariance
corr       correlation coefficient
spearmn    Spearman's rank correlation
kendall    Kendall's rank correlation
findex     Jain's fairness index
```

# EXAMPLE

- Read numbers from standard input

```
$ seq 10
1
2
3
4
5
6
7
8
9
10

$ seq 10 | stats -v
count   10
sum     55
min     1
max     10
mean    5.5
median  5
mode    6
var     8.25
stddev  2.87228
cv      52.2233
skew    0
kurt    -1.22424
quant10 2
quant25 3
quant50 6
quant75 8
quant90 10
conf90  1.49415
conf95  1.78026
conf99  2.33977
findex  0.785714
```
  
- Select statistic to display

```
$ seq 10 | stats -t mean
        5.5000
```

Also, you can specify list of statistics to display.

```
$ seq 1 10 | stats -t mean,var
        5.5000
        8.2500
```

- *stats* displays statistics for multiple columns

```
$ seq 10 | column -c 16
1       6
2       7
3       8
4       9
5       10

$ seq 10 | column -c 16 | stats -v
count   5       5
sum     15      40
min     1       6
max     5       10
mean    3       8
median  3       8
mode    5       6
var     2       2
stddev  1.41421 1.41421
cv      47.1405 17.6777
skew    0       0
kurt    -1.3    -1.3
quant10 1       6
quant25 2       7
quant50 3       8
quant75 4       9
quant90 5       10
conf90  1.04039 1.04039
conf95  1.23961 1.23961
conf99  1.62921 1.62921
findex  0.818182        0.969697
```
  
- Check file size statistics of some device driver

```
% cd /usr/src/linux/net/ipv4

% ls -l *.c
-rw-rw-r-- 1 root root  45818 Nov  2 09:05 af_inet.c
-rw-rw-r-- 1 root root  13814 Nov  2 09:05 ah4.c
-rw-rw-r-- 1 root root  35054 Nov  2 09:05 arp.c
-rw-rw-r-- 1 root root  64272 Nov  2 09:05 cipso_ipv4.c
-rw-rw-r-- 1 root root   3245 Nov  2 09:05 datagram.c
-rw-rw-r-- 1 root root  60368 Nov  2 09:05 devinet.c
-rw-rw-r-- 1 root root  17715 Nov  2 09:05 esp4.c
-rw-rw-r-- 1 root root  31111 Nov  2 09:05 fib_frontend.c
-rw-rw-r-- 1 root root   8404 Nov  2 09:05 fib_rules.c
-rw-rw-r-- 1 root root  37178 Nov  2 09:05 fib_semantics.c
-rw-rw-r-- 1 root root  65563 Nov  2 09:05 fib_trie.c
-rw-rw-r-- 1 root root  21349 Nov  2 09:05 fou.c
-rw-rw-r-- 1 root root   2909 Nov  2 09:05 gre_demux.c
-rw-rw-r-- 1 root root   6387 Nov  2 09:05 gre_offload.c
-rw-rw-r-- 1 root root  29472 Nov  2 09:05 icmp.c
-rw-rw-r-- 1 root root  72215 Nov  2 09:05 igmp.c
-rw-rw-r-- 1 root root  27977 Nov  2 09:05 inet_connection_sock.c
-rw-rw-r-- 1 root root  29166 Nov  2 09:05 inet_diag.c
-rw-rw-r-- 1 root root  10850 Nov  2 09:05 inet_fragment.c
-rw-rw-r-- 1 root root  16957 Nov  2 09:05 inet_hashtables.c
-rw-rw-r-- 1 root root   9482 Nov  2 09:05 inet_lro.c
-rw-rw-r-- 1 root root   9165 Nov  2 09:05 inet_timewait_sock.c
-rw-rw-r-- 1 root root  16266 Nov  2 09:05 inetpeer.c
-rw-rw-r-- 1 root root   3998 Nov  2 09:05 ip_forward.c
-rw-rw-r-- 1 root root  21583 Nov  2 09:05 ip_fragment.c
-rw-rw-r-- 1 root root  34240 Nov  2 09:05 ip_gre.c
-rw-rw-r-- 1 root root  13810 Nov  2 09:05 ip_input.c
-rw-rw-r-- 1 root root  15637 Nov  2 09:05 ip_options.c
-rw-rw-r-- 1 root root  40333 Nov  2 09:05 ip_output.c
-rw-rw-r-- 1 root root  35675 Nov  2 09:05 ip_sockglue.c
-rw-rw-r-- 1 root root  28418 Nov  2 09:05 ip_tunnel.c
-rw-rw-r-- 1 root root  11741 Nov  2 09:05 ip_tunnel_core.c
-rw-rw-r-- 1 root root  14330 Nov  2 09:05 ip_vti.c
-rw-rw-r-- 1 root root   4756 Nov  2 09:05 ipcomp.c
-rw-rw-r-- 1 root root  40057 Nov  2 09:05 ipconfig.c
-rw-rw-r-- 1 root root  15510 Nov  2 09:05 ipip.c
-rw-rw-r-- 1 root root  65328 Nov  2 09:05 ipmr.c
-rw-rw-r-- 1 root root   5302 Nov  2 09:05 netfilter.c
-rw-rw-r-- 1 root root  29801 Nov  2 09:05 ping.c
-rw-rw-r-- 1 root root  20748 Nov  2 09:05 proc.c
-rw-rw-r-- 1 root root   2339 Nov  2 09:05 protocol.c
-rw-rw-r-- 1 root root  25900 Nov  2 09:05 raw.c
-rw-rw-r-- 1 root root  69929 Nov  2 09:05 route.c
-rw-rw-r-- 1 root root  11639 Nov  2 09:05 syncookies.c
-rw-rw-r-- 1 root root  24418 Nov  2 09:05 sysctl_net_ipv4.c
-rw-rw-r-- 1 root root  84459 Nov  2 09:05 tcp.c
-rw-rw-r-- 1 root root   6349 Nov  2 09:05 tcp_bic.c
-rw-rw-r-- 1 root root  11399 Nov  2 09:05 tcp_cdg.c
-rw-rw-r-- 1 root root  10984 Nov  2 09:05 tcp_cong.c
-rw-rw-r-- 1 root root  15058 Nov  2 09:05 tcp_cubic.c
-rw-rw-r-- 1 root root   9674 Nov  2 09:05 tcp_dctcp.c
-rw-rw-r-- 1 root root   1969 Nov  2 09:05 tcp_diag.c
-rw-rw-r-- 1 root root   9302 Nov  2 09:05 tcp_fastopen.c
-rw-rw-r-- 1 root root   4966 Nov  2 09:05 tcp_highspeed.c
-rw-rw-r-- 1 root root   7565 Nov  2 09:05 tcp_htcp.c
-rw-rw-r-- 1 root root   4968 Nov  2 09:05 tcp_hybla.c
-rw-rw-r-- 1 root root   8350 Nov  2 09:05 tcp_illinois.c
-rw-rw-r-- 1 root root 181897 Nov  2 09:05 tcp_input.c
-rw-rw-r-- 1 root root  63388 Nov  2 09:05 tcp_ipv4.c
-rw-rw-r-- 1 root root   8900 Nov  2 09:05 tcp_lp.c
-rw-rw-r-- 1 root root   5661 Nov  2 09:05 tcp_memcontrol.c
-rw-rw-r-- 1 root root  31129 Nov  2 09:05 tcp_metrics.c
-rw-rw-r-- 1 root root  26301 Nov  2 09:05 tcp_minisocks.c
-rw-rw-r-- 1 root root   7777 Nov  2 09:05 tcp_offload.c
-rw-rw-r-- 1 root root 103411 Nov  2 09:05 tcp_output.c
-rw-rw-r-- 1 root root   7564 Nov  2 09:05 tcp_probe.c
-rw-rw-r-- 1 root root   1406 Nov  2 09:05 tcp_scalable.c
-rw-rw-r-- 1 root root  18837 Nov  2 09:05 tcp_timer.c
-rw-rw-r-- 1 root root   9805 Nov  2 09:05 tcp_vegas.c
-rw-rw-r-- 1 root root   5767 Nov  2 09:05 tcp_veno.c
-rw-rw-r-- 1 root root   8361 Nov  2 09:05 tcp_westwood.c
-rw-rw-r-- 1 root root   7041 Nov  2 09:05 tcp_yeah.c
-rw-rw-r-- 1 root root   4220 Nov  2 09:05 tunnel4.c
-rw-rw-r-- 1 root root  66396 Nov  2 09:05 udp.c
-rw-rw-r-- 1 root root   5633 Nov  2 09:05 udp_diag.c
-rw-rw-r-- 1 root root  11360 Nov  2 09:05 udp_offload.c
-rw-rw-r-- 1 root root   3189 Nov  2 09:05 udp_tunnel.c
-rw-rw-r-- 1 root root   3483 Nov  2 09:05 udplite.c
-rw-rw-r-- 1 root root   3975 Nov  2 09:05 xfrm4_input.c
-rw-rw-r-- 1 root root   3773 Nov  2 09:05 xfrm4_mode_beet.c
-rw-rw-r-- 1 root root   2135 Nov  2 09:05 xfrm4_mode_transport.c
-rw-rw-r-- 1 root root   3031 Nov  2 09:05 xfrm4_mode_tunnel.c
-rw-rw-r-- 1 root root   2592 Nov  2 09:05 xfrm4_output.c
-rw-rw-r-- 1 root root   7664 Nov  2 09:05 xfrm4_policy.c
-rw-rw-r-- 1 root root   6813 Nov  2 09:05 xfrm4_protocol.c
-rw-rw-r-- 1 root root   2494 Nov  2 09:05 xfrm4_state.c
-rw-rw-r-- 1 root root   2765 Nov  2 09:05 xfrm4_tunnel.c

% ls -l *.c | awk '{ print $5 }' | stats -v
count   87
sum     1.96204e+06
min     1406
max     181897
mean    22552.2
median  11399
mode    13810
var     7.60447e+08
stddev  27576.2
cv      122.277
skew    2.90083
kurt    11.6306
quant10 3031
quant25 5661
quant50 11399
quant75 29472
quant90 64272
conf90  4863.41
conf95  5794.7
conf99  7615.89
findex  0.400774
```
  
# AVAILABILITY

The latest version of *stats* is available at https://pypi.org/project/py-stats/ .

# AUTHOR

Hiroyuki Ohsaki <ohsaki[atmark]lsnl.jp>
