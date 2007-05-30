diff -ur gossip-0.25-o/src/gossip-galago.c gossip-0.25/src/gossip-galago.c
--- gossip-0.25-o/src/gossip-galago.c	2007-04-22 07:51:05.000000000 -0600
+++ gossip-0.25/src/gossip-galago.c	2007-05-29 18:11:49.000000000 -0600
@@ -104,7 +104,7 @@
 		const gchar         *account_param;
 
 		if (gossip_account_has_param (account, "account")) {
-			gossip_account_param_get (account, 
+			gossip_account_get_param(account, 
 						  "account", &account_param, 
 						  NULL);
 		} else {
