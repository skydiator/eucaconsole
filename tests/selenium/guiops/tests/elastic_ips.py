from guiops.guiops import GuiOps
from option_parser import Option_parser


class ElasticIPsOperationsSequence(GuiOps):

    def __init__(self):
        parser = Option_parser()
        self.console_url = parser.parse_options()['console_url']
        self.webdriver_url = parser.parse_options()['web_driver']
        self.account = parser.parse_options()['account']
        self.user = parser.parse_options()['user_name']
        self.password = parser.parse_options()['password']
        self.sauce = parser.parse_options()['sauce']
        self.browser = parser.parse_options()['browser']
        self.version = parser.parse_options()['version']
        self.platform = parser.parse_options()['platform']
        self.tester = GuiOps(console_url=self.console_url, webdriver_url=self.webdriver_url,
                             sauce=self.sauce, browser=self.browser, version=self.version, platform=self.platform)

    def elastic_ip_ops_test(self):
        self.tester.login(self.account, self.user, self.password)
        # Allocate multiple IPs, then batch-release
        elastic_ips = self.tester.allocate_eip_from_dashboard(2)
        released_ips = self.tester.release_eips_from_eip_lp(elastic_ips)
        assert elastic_ips == released_ips
        self.tester.logout()
        self.tester.exit_browser()


if __name__ == '__main__':
        tester = ElasticIPsOperationsSequence()
        ElasticIPsOperationsSequence.elastic_ip_ops_test(tester)
