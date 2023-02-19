import time
import random
from trie.trie import Trie


trie = Trie()
ten_notes = ['w_1.0', 'n_65_quarter', 'n_38_half', 'w_0.5', 'n_62_eighth', 'w_0.5', 'n_65_quarter',
             'w_0.5', 'n_67_eighth', 'w_0.5',
             ]

hundred_notes = ['w_1.0', 'n_65_quarter', 'n_38_half', 'w_0.5', 'n_62_eighth', 'w_0.5',
                 'n_65_quarter','w_0.5', 'n_67_eighth', 'w_0.5', 'n_65_eighth', 'n_69_quarter',
                 'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_eighth', 'n_62_quarter', 'w_0.5',
                 'n_62_eighth', 'n_36_eighth', 'w_0.5', 'n_70_half', 'n_38_half', 'w_0.5',
                 'n_62_eighth', 'w_0.5', 'n_65_eighth', 'w_0.5', 'n_67_eighth', 'w_0.5',
                 'n_65_quarter', 'n_70_quarter', 'w_1.0', 'n_62_quarter', 'n_65_quarter',
                 'w_0.5', 'n_38_eighth', 'w_0.5', 'n_67_half', 'n_40_half', 'w_0.5',
                 'n_60_eighth', 'w_0.5', 'n_64_eighth', 'w_0.5', 'n_65_eighth', 'w_0.5',
                 'n_60_quarter', 'n_67_quarter', 'w_1.0', 'n_72_quarter', 'n_60_quarter',
                 'w_0.5', 'n_40_eighth', 'w_0.5', 'n_69_half', 'n_41_half', 'w_0.5', 'n_60_eighth',
                 'w_0.5', 'n_65_eighth', 'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_quarter', 'w_1.0',
                 'n_60_quarter', 'n_69_quarter', 'w_0.5', 'n_41_eighth', 'w_0.5', 'n_42_half',
                 'w_0.5', 'n_62_eighth', 'w_0.5', 'n_66_eighth', 'w_0.5', 'n_62_eighth',
                 'n_69_eighth', 'w_0.5', 'n_69_eighth', 'n_72_eighth', 'w_0.5', 'n_70_eighth',
                 'n_70_eighth', 'w_0.5', 'n_72_eighth', 'n_69_eighth', 'w_0.5', 'n_69_eighth',
                 'n_66_eighth', 'n_42_eighth', 'w_0.5', 'n_70_quarter', 'n_43_half', 'w_0.5',
                 'n_67_eighth', 'w_0.5', 'n_62_eighth', 'w_0.5',
                 ]

thousand_notes = ['w_1.0', 'n_65_quarter', 'n_38_half', 'w_0.5', 'n_62_eighth', 'w_0.5',
                  'n_65_quarter', 'w_0.5', 'n_67_eighth', 'w_0.5', 'n_65_eighth', 'n_69_quarter',
                  'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_eighth', 'n_62_quarter', 'w_0.5',
                  'n_62_eighth', 'n_36_eighth', 'w_0.5', 'n_70_half', 'n_38_half', 'w_0.5',
                  'n_62_eighth', 'w_0.5', 'n_65_eighth', 'w_0.5', 'n_67_eighth', 'w_0.5',
                  'n_65_quarter', 'n_70_quarter', 'w_1.0', 'n_62_quarter', 'n_65_quarter',
                  'w_0.5', 'n_38_eighth', 'w_0.5', 'n_67_half', 'n_40_half', 'w_0.5',
                  'n_60_eighth', 'w_0.5', 'n_64_eighth', 'w_0.5', 'n_65_eighth', 'w_0.5',
                  'n_60_quarter', 'n_67_quarter', 'w_1.0', 'n_72_quarter', 'n_60_quarter',
                  'w_0.5', 'n_40_eighth', 'w_0.5', 'n_69_half', 'n_41_half', 'w_0.5',
                  'n_60_eighth', 'w_0.5', 'n_65_eighth', 'w_0.5', 'n_67_eighth', 'w_0.5',
                  'n_69_quarter', 'w_1.0', 'n_60_quarter', 'n_69_quarter', 'w_0.5', 'n_41_eighth',
                  'w_0.5', 'n_42_half', 'w_0.5', 'n_62_eighth', 'w_0.5', 'n_66_eighth',
                  'w_0.5', 'n_62_eighth', 'n_69_eighth', 'w_0.5', 'n_69_eighth', 'n_72_eighth',
                  'w_0.5', 'n_70_eighth', 'n_70_eighth', 'w_0.5', 'n_72_eighth', 'n_69_eighth',
                  'w_0.5', 'n_69_eighth', 'n_66_eighth', 'n_42_eighth', 'w_0.5', 'n_70_quarter',
                  'n_43_half', 'w_0.5', 'n_67_eighth', 'w_0.5', 'n_62_eighth', 'w_0.5',
                  'n_62_quarter',
                  'n_70_eighth', 'w_0.5', 'n_72_eighth', 'w_0.5', 'n_70_16th', 'n_72_16th',
                  'w_0.25', 'n_70_16th', 'w_0.25', 'n_67_quarter', 'n_69_eighth', 'w_0.5',
                  'n_62_eighth', 'n_43_eighth', 'w_0.5', 'n_65_quarter', 'n_44_half',
                  'w_0.5', 'n_65_quarter', 'w_0.5', 'n_59_eighth', 'w_0.5', 'n_62_eighth',
                  'w_0.5', 'n_65_eighth', 'w_0.5', 'n_67_eighth', 'n_59_eighth', 'w_0.25',
                  'n_68_16th', 'w_0.25', 'n_67_eighth', 'n_68_eighth', 'w_0.5', 'n_65_eighth',
                  'n_65_eighth', 'n_44_eighth', 'w_0.5', 'n_65_quarter', 'n_62_quarter',
                  'n_45_quarter', 'w_1.0', 'n_33_quarter', 'w_0.5', 'n_65_16th', 'n_62_16th',
                  'w_0.25', 'n_67_16th', 'n_64_16th', 'w_0.25', 'n_64_quarter', 'n_61_quarter',
                  'w_2.0', 'n_41_16th', 'n_64_quarter', 'n_61_quarter', 'w_0.25', 'n_40_16th',
                  'w_0.25', 'n_38_16th', 'w_0.25', 'n_37_16th', 'w_0.25', 'n_65_quarter',
                  'n_38_half', 'w_0.5', 'n_62_eighth', 'w_0.5', 'n_65_quarter', 'w_0.5',
                  'n_67_eighth', 'w_0.5', 'n_65_eighth', 'n_69_quarter', 'w_0.5', 'n_67_eighth',
                  'w_0.5', 'n_69_eighth', 'n_62_quarter', 'w_0.5', 'n_62_eighth', 'n_36_eighth',
                  'w_0.5', 'n_70_half', 'n_38_half', 'w_0.5', 'n_62_eighth', 'w_0.5', 'n_65_eighth',
                  'w_0.5', 'n_67_eighth', 'w_0.5', 'n_65_quarter', 'n_70_quarter',
                  'w_1.0', 'n_62_quarter',
                  'n_65_quarter', 'w_0.5', 'n_38_eighth', 'w_0.5', 'n_67_half', 'n_40_half',
                  'w_0.5', 'n_60_eighth', 'w_0.5', 'n_64_eighth', 'w_0.5', 'n_65_eighth', 'w_0.5',
                  'n_60_quarter', 'n_67_quarter', 'w_1.0', 'n_72_quarter', 'n_60_quarter', 'w_0.5',
                  'n_40_eighth', 'w_0.5', 'n_69_half', 'n_41_half', 'w_0.5', 'n_60_eighth', 'w_0.5',
                  'n_65_eighth', 'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_quarter', 'w_1.0',
                  'n_60_quarter', 'n_69_quarter', 'w_0.5', 'n_41_eighth', 'w_0.5', 'n_42_half',
                  'w_0.5', 'n_62_eighth', 'w_0.5', 'n_66_eighth', 'w_0.5',
                  'n_62_eighth', 'n_69_eighth', 'w_0.5', 'n_69_eighth', 'n_72_eighth', 'w_0.5',
                  'n_70_eighth', 'n_70_eighth', 'w_0.5', 'n_72_eighth', 'n_69_eighth', 'w_0.5',
                  'n_69_eighth', 'n_66_eighth', 'n_42_eighth', 'w_0.5', 'n_70_quarter', 'n_43_half',
                  'w_0.5', 'n_67_eighth', 'w_0.5', 'n_62_eighth', 'w_0.5', 'n_62_quarter',
                  'n_70_eighth', 'w_0.5', 'n_72_eighth', 'w_0.5', 'n_70_16th', 'n_72_16th',
                  'w_0.25', 'n_70_16th', 'w_0.25', 'n_67_quarter', 'n_69_eighth', 'w_0.5',
                  'n_62_eighth', 'n_43_eighth', 'w_0.5', 'n_65_quarter', 'n_44_half',
                  'w_0.5', 'n_65_quarter', 'w_0.5', 'n_59_eighth', 'w_0.5', 'n_62_eighth', 'w_0.5',
                  'n_65_eighth', 'w_0.5', 'n_67_eighth', 'n_59_eighth', 'w_0.25', 'n_68_16th',
                  'w_0.25', 'n_67_eighth', 'n_68_eighth', 'w_0.5', 'n_65_eighth', 'n_65_eighth',
                  'n_44_eighth', 'w_0.5', 'n_65_quarter', 'n_62_quarter', 'n_45_quarter',
                  'w_1.0', 'n_33_quarter', 'w_0.5', 'n_65_16th', 'n_62_16th', 'w_0.25',
                  'n_67_16th', 'n_64_16th', 'w_0.25', 'n_64_quarter', 'n_61_quarter', 'w_2.0',
                  'n_41_16th', 'n_64_quarter', 'n_61_quarter', 'w_0.25', 'n_40_16th',
                  'w_0.25', 'n_38_16th', 'w_0.25', 'n_37_16th', 'w_0.25', 'n_76_eighth',
                  'n_35_quarter', 'w_0.5', 'n_77_eighth', 'n_74_16th', 'w_0.25', 'n_76_16th',
                  'w_0.25', 'n_77_eighth', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_79_16th',
                  'n_74_16th', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_76_quarter', 'n_35_quarter',
                  'w_0.5', 'n_74_16th', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_77_16th', 'n_76_eighth',
                  'w_0.25', 'n_76_eighth', 'w_0.25', 'n_74_16th', 'w_0.25',
                  'n_76_16th', 'w_0.25', 'n_76_eighth', 'n_35_quarter', 'w_0.5', 'n_77_eighth',
                  'n_74_16th', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_77_eighth',
                  'w_0.25', 'n_76_16th', 'w_0.25', 'n_79_16th', 'n_74_16th', 'w_0.25',
                  'n_76_16th', 'w_0.25', 'n_81_eighth',
                  'n_35_quarter', 'w_0.5', 'n_79_16th', 'n_74_16th', 'n_81_16th',
                  'w_0.25', 'n_79_16th', 'n_76_16th', 'w_0.25', 'n_77_eighth', 'n_77_eighth',
                  'w_0.25', 'n_76_16th', 'w_0.25', 'n_76_16th', 'n_74_16th', 'w_0.25', 'n_76_16th',
                  'w_0.25', 'n_74_quarter', 'n_33_quarter', 'w_0.5', 'n_72_16th',
                  'w_0.25', 'n_74_16th', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_74_16th',
                  'w_0.25', 'n_72_16th', 'n_72_quarter', 'w_0.25', 'n_74_16th',
                  'w_0.25', 'n_33_quarter',
                  'w_0.5', 'n_72_eighth', 'w_0.25', 'n_74_16th', 'w_0.25',
                  'n_76_16th', 'n_72_eighth', 'w_0.25', 'n_74_16th', 'w_0.25', 'n_72_16th',
                  'w_0.25', 'n_74_16th', 'w_0.25', 'n_72_16th', 'n_69_16th', 'n_33_quarter',
                  'w_0.3333333333333286', 'n_72_eighth', 'n_69_eighth', 'w_1/3',
                  'n_74_16th', 'n_70_16th', 'w_0.3333333333333286', 'n_74_eighth', 'n_70_eighth',
                  'w_0.3333333333333286', 'n_76_eighth', 'n_72_eighth', 'w_1/3', 'n_76_16th',
                  'n_72_16th', 'w_0.3333333333333286', 'n_76_16th', 'n_72_16th', 'n_33_quarter',
                  'w_0.3333333333333286', 'n_76_eighth', 'n_72_eighth', 'w_1/3', 'n_77_16th',
                  'n_74_16th', 'w_0.3333333333333286', 'n_77_eighth', 'n_74_eighth',
                  'w_0.3333333333333286', 'n_79_eighth', 'n_76_eighth', 'w_1/3', 'n_79_16th',
                  'n_76_16th', 'w_0.3333333333333286', 'n_76_eighth', 'n_35_quarter',
                  'w_0.5', 'n_77_eighth', 'n_74_16th', 'w_0.25', 'n_76_16th',
                  'w_0.25', 'n_77_eighth', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_79_16th',
                  'n_74_16th', 'w_0.25', 'n_76_16th',
                  'w_0.25', 'n_76_quarter', 'n_35_quarter', 'w_0.5', 'n_74_16th',
                  'w_0.25', 'n_76_16th',
                  'w_0.25', 'n_77_16th', 'n_76_eighth', 'w_0.25', 'n_76_eighth',
                  'w_0.25', 'n_74_16th', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_76_eighth',
                  'n_35_quarter', 'w_0.5', 'n_77_eighth', 'n_74_16th', 'w_0.25',
                  'n_76_16th', 'w_0.25', 'n_77_eighth',
                  'w_0.25', 'n_76_16th', 'w_0.25', 'n_79_16th', 'n_74_16th', 'w_0.25', 'n_76_16th',
                  'w_0.25', 'n_81_eighth', 'n_35_quarter', 'w_0.5', 'n_79_16th', 'n_74_16th',
                  'n_81_16th', 'w_0.25', 'n_79_16th', 'n_76_16th', 'w_0.25', 'n_77_eighth',
                  'n_77_eighth', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_76_16th', 'n_74_16th',
                  'w_0.25', 'n_76_16th', 'w_0.25', 'n_74_quarter', 'n_33_quarter',
                  'w_0.5', 'n_72_16th',
                  'w_0.25', 'n_74_16th', 'w_0.25', 'n_76_16th', 'w_0.25', 'n_74_16th',
                  'w_0.25', 'n_72_16th', 'n_72_quarter', 'w_0.25', 'n_74_16th', 'w_0.25',
                  'n_33_quarter', 'w_0.5', 'n_72_eighth', 'w_0.25', 'n_74_16th',
                  'w_0.25', 'n_76_16th',
                  'n_72_eighth', 'w_0.25', 'n_74_16th', 'w_0.25', 'n_72_16th',
                  'w_0.25', 'n_74_16th', 'w_0.25', 'n_72_16th', 'n_69_16th',
                  'n_33_quarter', 'w_0.3333333333333286',
                  'n_72_eighth', 'n_69_eighth', 'w_1/3', 'n_74_16th', 'n_70_16th',
                  'w_0.3333333333333286', 'n_74_eighth', 'n_70_eighth',
                  'w_0.3333333333333286', 'n_76_eighth', 'n_72_eighth',
                  'w_1/3', 'n_76_16th', 'n_72_16th', 'w_0.3333333333333286', 'n_76_16th',
                  'n_72_16th', 'n_33_quarter', 'w_0.3333333333333286', 'n_76_eighth',
                  'n_72_eighth', 'w_1/3',
                  'n_77_16th', 'n_74_16th', 'w_0.3333333333333286', 'n_77_eighth', 'n_74_eighth',
                  'w_0.3333333333333286', 'n_79_eighth', 'n_76_eighth', 'w_1/3', 'n_79_16th',
                  'n_76_16th', 'w_0.3333333333333286', 'n_80_eighth', 'n_77_eighth', 'n_32_eighth',
                  'w_0.5', 'n_77_eighth', 'n_74_eighth', 'n_35_eighth', 'w_0.5', 'n_77_eighth',
                  'n_74_eighth', 'n_38_eighth', 'w_0.5', 'n_74_eighth', 'n_71_eighth',
                  'n_41_eighth',
                  'w_0.5', 'n_74_eighth', 'n_71_eighth', 'w_0.5', 'n_71_eighth', 'n_68_eighth',
                  'n_41_eighth', 'w_0.5', 'n_38_eighth', 'n_71_eighth', 'n_68_eighth', 'w_0.5',
                  'n_80_eighth', 'n_77_eighth', 'n_35_eighth', 'w_0.5',
                  'n_80_eighth', 'n_77_eighth',
                  'n_32_eighth', 'w_0.5', 'n_77_eighth', 'n_74_eighth', 'n_35_eighth',
                  'w_0.5', 'n_77_eighth', 'n_74_eighth', 'n_38_eighth', 'w_0.5',
                  'n_74_eighth', 'n_71_eighth', 'n_41_eighth', 'w_0.5', 'n_74_eighth',
                  'n_71_eighth', 'w_0.5', 'n_71_eighth', 'n_68_eighth',
                  'n_41_eighth', 'w_1.0', 'n_38_eighth', 'n_71_eighth', 'n_68_eighth',
                  'w_0.5', 'n_35_eighth', 'w_0.5', 'n_76_quarter', 'n_73_quarter',
                  'n_33_eighth', 'w_0.5', 'n_45_eighth', 'w_0.5',
                  'n_33_eighth', 'w_0.5', 'n_76_eighth', 'n_73_eighth', 'n_45_eighth', 'w_0.25',
                  'n_77_16th', 'n_74_16th', 'w_0.25', 'n_79_quarter', 'n_76_quarter', 'n_33_eighth',
                  'w_0.5', 'n_45_eighth', 'w_1.0', 'n_79_16th', 'n_76_16th', 'w_0.25', 'n_81_16th',
                  'n_77_16th', 'w_0.25', 'n_82_quarter', 'n_79_quarter', 'n_45_16th', 'w_0.25',
                  'n_43_16th', 'w_0.25', 'n_40_16th', 'w_0.25', 'n_33_16th', 'w_0.25', 'n_45_16th',
                  'w_0.25', 'n_43_16th', 'w_0.25', 'n_82_16th', 'n_79_16th', 'n_40_16th',
                  'w_0.25', 'n_84_16th', 'n_81_16th', 'n_33_16th', 'w_0.25',
                  'n_81_quarter', 'n_76_quarter',
                  'n_33_eighth', 'w_0.5', 'n_33_eighth', 'w_0.5', 'n_36_eighth', 'n_81_quarter',
                  'n_76_quarter', 'w_0.5', 'n_36_eighth', 'w_0.5', 'n_65_quarter', 'n_38_half',
                  'w_0.5', 'n_62_eighth', 'w_0.5', 'n_65_quarter', 'w_0.5', 'n_67_eighth', 'w_0.5',
                  'n_65_eighth', 'n_69_quarter', 'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_eighth',
                  'n_62_quarter', 'w_0.5', 'n_62_eighth', 'n_36_eighth',
                  'w_0.5', 'n_70_half', 'n_38_half', 'w_0.5', 'n_62_eighth', 'w_0.5',
                  'n_65_eighth', 'w_0.5', 'n_67_eighth', 'w_0.5',
                  'n_65_quarter', 'n_70_quarter', 'w_1.0', 'n_62_quarter', 'n_65_quarter', 'w_0.5',
                  'n_38_eighth', 'w_0.5', 'n_67_half', 'n_40_half', 'w_0.5', 'n_60_eighth', 'w_0.5',
                  'n_64_eighth', 'w_0.5', 'n_65_eighth', 'w_0.5', 'n_60_quarter',
                  'n_67_quarter', 'w_1.0', 'n_72_quarter', 'n_60_quarter', 'w_0.5', 'n_40_eighth',
                  'w_0.5', 'n_69_half', 'n_41_half', 'w_0.5', 'n_60_eighth', 'w_0.5', 'n_65_eighth',
                  'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_quarter', 'w_1.0', 'n_60_quarter',
                  'n_69_quarter', 'w_0.5', 'n_41_eighth', 'w_0.5', 'n_42_half', 'w_0.5',
                  'n_62_eighth',
                  'w_0.5', 'n_66_eighth', 'w_0.5', 'n_62_eighth', 'n_69_eighth', 'w_0.5',
                  'n_69_eighth', 'n_72_eighth', 'w_0.5', 'n_70_eighth', 'n_70_eighth', 'w_0.5',
                  'n_72_eighth', 'n_69_eighth', 'w_0.5', 'n_69_eighth', 'n_66_eighth',
                  'n_42_eighth', 'w_0.5', 'n_70_quarter', 'n_43_half', 'w_0.5', 'n_67_eighth',
                  'w_0.5', 'n_62_eighth', 'w_0.5', 'n_62_quarter', 'n_70_eighth', 'w_0.5',
                  'n_72_eighth', 'w_0.5', 'n_70_16th',
                  'n_72_16th', 'w_0.25', 'n_70_16th', 'w_0.25', 'n_67_quarter', 'n_69_eighth',
                  'w_0.5', 'n_62_eighth', 'n_43_eighth', 'w_0.5', 'n_65_quarter',
                  'n_44_half', 'w_0.5',
                  'n_65_quarter', 'w_0.5', 'n_59_eighth', 'w_0.5', 'n_62_eighth', 'w_0.5',
                  'n_65_eighth', 'w_0.5', 'n_67_eighth', 'n_59_eighth', 'w_0.25',
                  'n_68_16th', 'w_0.25', 'n_67_eighth', 'n_68_eighth', 'w_0.5',
                  'n_65_eighth', 'n_65_eighth', 'n_44_eighth',
                  'w_0.5', 'n_65_quarter', 'n_62_quarter', 'n_45_quarter', 'w_1.0', 'n_33_quarter',
                  'w_0.5', 'n_65_16th', 'n_62_16th', 'w_0.25', 'n_67_16th', 'n_64_16th', 'w_0.25',
                  'n_64_quarter', 'n_61_quarter', 'w_2.0', 'n_41_16th', 'n_64_quarter',
                  'n_61_quarter', 'w_0.25', 'n_40_16th', 'w_0.25', 'n_38_16th',
                  'w_0.25', 'n_37_16th', 'w_0.25', 'n_65_quarter', 'n_38_half',
                  'w_0.5', 'n_62_eighth', 'w_0.5', 'n_65_quarter',
                  'w_0.5', 'n_67_eighth', 'w_0.5', 'n_65_eighth', 'n_69_quarter',
                  'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_eighth', 'n_62_quarter',
                  'w_0.5', 'n_62_eighth', 'n_36_eighth', 'w_0.5',
                  'n_70_half', 'n_38_half', 'w_0.5', 'n_62_eighth',
                  'w_0.5', 'n_65_eighth', 'w_0.5', 'n_67_eighth', 'w_0.5', 'n_65_quarter',
                  'n_70_quarter', 'w_1.0', 'n_62_quarter', 'n_65_quarter', 'w_0.5',
                  'n_38_eighth', 'w_0.5', 'n_67_half', 'n_40_half',
                  'w_0.5', 'n_60_eighth', 'w_0.5', 'n_64_eighth', 'w_0.5', 'n_65_eighth',
                  'w_0.5', 'n_60_quarter', 'n_67_quarter', 'w_1.0', 'n_72_quarter',
                  'n_60_quarter', 'w_0.5', 'n_40_eighth', 'w_0.5',
                  'n_69_half', 'n_41_half', 'w_0.5', 'n_60_eighth', 'w_0.5', 'n_65_eighth',
                  'w_0.5', 'n_67_eighth', 'w_0.5', 'n_69_quarter', 'w_1.0', 'n_60_quarter',
                  'n_69_quarter', 'w_0.5', 'n_41_eighth', 'w_0.5',
                  'n_42_half', 'w_0.5', 'n_62_eighth', 'w_0.5', 'n_66_eighth', 'w_0.5',
                  'n_62_eighth', 'n_69_eighth', 'w_0.5', 'n_69_eighth', 'n_72_eighth',
                  'w_0.5', 'n_70_eighth', 'n_70_eighth', 'w_0.5', 'n_72_eighth',
                  'n_69_eighth', 'w_0.5', 'n_69_eighth', 'n_66_eighth', 'n_42_eighth',
                  'w_0.5', 'n_70_quarter', 'n_43_half', 'w_0.5', 'n_67_eighth', 'w_0.5',
                  'n_62_eighth', 'w_0.5', 'n_62_quarter', 'n_70_eighth',
                  'w_0.5', 'n_72_eighth', 'w_0.5', 'n_70_16th', 'n_72_16th', 'w_0.25',
                  'n_70_16th', 'w_0.25', 'n_67_quarter', 'n_69_eighth',
                  ]

# pylint: disable=assignment-from-no-return
# pylint: disable=invalid-name

print("-----------------------------------------------------------------------------")
print("Suorituskykytesti: tietojen tallentaminen Trie-tietorakenteeseen")

print("   Tallennetaan 100 000 nuottia")
print("-----------------------------------------------------------------------------")
print("      10 nuotin pituisen midi-tiedoston tallentaminen")
total_time = 0                                          # pylint: disable=C0103

for i in range(0, 100000):
    start_time = time.time()                            # pylint: disable=C0103
    saved_trie = trie.add_list_to_trie(ten_notes)       # pylint: disable=C0103
    total_time += time.time() - start_time              # pylint: disable=C0103
avg_time_per_midi = total_time / 100000                 # pylint: disable=C0103
avg_time_per_note = total_time / 100000                 # pylint: disable=C0103
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(
    f"         Keskimääräinen aika per midi-tiedosto {avg_time_per_midi:6f} sekuntia")
print(
    f"         Keskimääräinen aika per nuotti {avg_time_per_note:6f} sekuntia")

print("-----------------------------------------------------------------------------")
print("      100 nuotin pituisen midi-tiedoston tallentaminen")
total_time = 0                                          # pylint: disable=C0103

for i in range(0, 10000):
    start_time = time.time()
    saved_trie = trie.add_list_to_trie(hundred_notes)   # pylint: disable=C0103
    total_time += time.time() - start_time              # pylint: disable=C0103
avg_time_per_midi = total_time / 10000                  # pylint: disable=C0103
avg_time_per_note = total_time / 100000                 # pylint: disable=C0103
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(
    f"         Keskimääräinen aika per midi-tiedosto {avg_time_per_midi:6f} sekuntia")
print(
    f"         Keskimääräinen aika per nuotti {avg_time_per_note:6f} sekuntia")

print("-----------------------------------------------------------------------------")
print("      1000 nuotin pituisen midi-tiedoston tallentaminen")
total_time = 0                                         # pylint: disable=C0103

for i in range(0, 1000):
    start_time = time.time()                           # pylint: disable=C0103
    saved_trie = trie.add_list_to_trie(thousand_notes) # pylint: disable=C0103
    total_time += time.time() - start_time             # pylint: disable=C0103
avg_time_per_midi = total_time / 1000                  # pylint: disable=C0103
avg_time_per_note = total_time / 100000                # pylint: disable=C0103
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(
    f"         Keskimääräinen aika per midi-tiedosto {avg_time_per_midi:6f} sekuntia")
print(
    f"         Keskimääräinen aika per nuotti {avg_time_per_note:6f} sekuntia")


print("-----------------------------------------------------------------------------")
print("Suorituskykytesti: tietojen hakeminen Trie-tietorakenteesta")

print("   Haetaan 100 000 nuottia 1 pituisella prefixillä")
print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choice(ten_notes)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choice(hundred_notes)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choice(thousand_notes)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("   Haetaan 100 000 nuottia 2 pituisella prefixillä")
print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choices(ten_notes, k=2)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choices(ten_notes, k=2)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choices(ten_notes, k=2)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("   Haetaan 100 000 nuottia 3 pituisella prefixillä")
print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choices(ten_notes, k=3)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choices(ten_notes, k=3)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choices(ten_notes, k=3)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("   Haetaan 100 000 nuottia 4 pituisella prefixillä")
print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choices(ten_notes, k=4)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choices(ten_notes, k=4)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choices(ten_notes, k=4)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("   Haetaan 100 000 nuottia 5 pituisella prefixillä")
print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 10 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choices(ten_notes, k=5)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 100 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choices(ten_notes, k=5)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")

print("-----------------------------------------------------------------------------")
print("      Haku Triestä, johon tallennettu 1000 nuotin pituisen midi-tiedosto")
total_time = 0

for i in range(0, 100000):
    start_time = time.time()
    prefix = random.choices(ten_notes, k=5)
    trie.return_choices(prefix)
    total_time += time.time() - start_time
avg_time = total_time / 100000
print(f"         Aikaa kului: {total_time:6f} sekuntia")
print(f"         Keskimääräinen aika {avg_time:6f} sekuntia")
