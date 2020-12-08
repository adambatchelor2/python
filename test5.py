



counter = 0
acc = 0

mydict = {0: ['acc', 14, 0, 14], 1: ['acc', 11, 0, 25], 2: ['nop', 422, 0, 25], 3: ['acc', 14, 0, 39], 4: ['jmp', 443, 0, 39], 5: ['acc', 21, 0, 0], 6: ['nop', 524, 0, 0], 7: ['acc', -2, 0, 0], 8: ['jmp', 279, 0, 0], 9: ['jmp', 1, 0, 640], 10: ['acc', 28, 0, 668], 11: ['acc', 11, 0, 679], 12: ['jmp', 576, 0, 679], 13: ['acc', 32, 0, 0], 14: ['acc', -12, 0, 0], 15: ['acc', -8, 0, 0], 16: ['jmp', 291, 0, 0], 17: ['nop', 542, 0, 798], 18: ['acc', 41, 0, 839], 19: ['jmp', 320, 0, 839], 20: ['acc', 40, 0, 437], 21: ['jmp', 96, 0, 437], 22: ['jmp', 85, 0, 244], 23: ['acc', 38, 0, 1206], 24: ['acc', 8, 0, 1214], 25: ['jmp', 333, 0, 1214], 26: ['acc', 44, 0, 699], 27: ['nop', 231, 0, 699], 28: ['acc', 40, 0, 739], 29: ['jmp', 323, 0, 739], 30: ['acc', 18, 0, 0], 31: ['jmp', 251, 0, 0], 32: ['acc', -1, 0, 318], 33: ['jmp', 385, 0, 318], 34: ['acc', -9, 0, 1166], 35: ['acc', 48, 0, 1214], 36: ['acc', 20, 0, 1234], 37: ['acc', 34, 0, 1268], 38: ['jmp', 150, 0, 1268], 39: ['nop', 203, 0, 780], 40: ['acc', 4, 0, 784], 41: ['acc', 32, 0, 816], 42: ['acc', 44, 0, 860], 43: ['jmp', 168, 0, 860], 44: ['acc', 26, 0, 0], 45: ['acc', 46, 0, 0], 46: ['acc', 40, 0, 0], 47: ['jmp', -30, 0, 0], 48: ['jmp', 182, 0, 181], 49: ['acc', 18, 0, 548], 50: ['jmp', 404, 0, 548], 51: ['nop', 142, 0, 0], 52: ['jmp', 84, 0, 0], 53: ['acc', 30, 0, 0], 54: ['acc', 10, 0, 0], 55: ['jmp', 1, 0, 0], 56: ['acc', 40, 0, 0], 57: ['jmp', 370, 0, 0], 58: ['jmp', 381, 0, 0], 59: ['jmp', 239, 0, 0], 60: ['acc', -2, 0, 657], 61: ['acc', 47, 0, 704], 62: ['acc', -4, 0, 700], 63: ['jmp', 295, 0, 700], 64: ['jmp', -38, 0, 536], 65: ['acc', 40, 0, 1006], 66: ['acc', 44, 0, 1050], 67: ['acc', 4, 0, 1054], 68: ['acc', 4, 0, 1058], 69: ['jmp', 156, 0, 1058], 70: ['acc', 31, 0, 647], 71: ['acc', 20, 0, 667], 72: ['acc', 0, 0, 667], 73: ['acc', -12, 0, 655], 74: ['jmp', -48, 0, 655], 75: ['acc', 32, 0, 132], 76: ['acc', 38, 0, 170], 77: ['jmp', 1, 0, 170], 78: ['acc', -6, 0, 164], 79: ['jmp', 375, 0, 164], 80: ['acc', 33, 0, 1312], 81: ['acc', 27, 0, 1339], 82: ['acc', 28, 0, 1367], 83: ['jmp', 107, 0, 1367], 84: ['acc', 1, 0, 365], 85: ['acc', 6, 0, 371], 86: ['nop', 136, 0, 371], 87: ['jmp', 85, 0, 371], 88: ['acc', 31, 0, 99], 89: ['acc', 49, 0, 148], 90: ['acc', 46, 0, 194], 91: ['jmp', 167, 0, 194], 92: ['acc', 5, 0, 989], 93: ['acc', -5, 0, 984], 94: ['jmp', 148, 0, 984], 95: ['acc', 22, 0, 688], 96: ['acc', 44, 0, 732], 97: ['acc', -8, 0, 724], 98: ['acc', -2, 0, 722], 99: ['jmp', -60, 0, 722], 100: ['nop', 354, 0, 303], 101: ['jmp', 59, 0, 303], 102: ['acc', 48, 0, 187], 103: ['nop', 473, 0, 187], 104: ['acc', -7, 0, 180], 105: ['acc', 4, 0, 184], 106: ['jmp', 105, 0, 184], 107: ['jmp', 456, 0, 244], 108: ['acc', 16, 0, 1514], 109: ['acc', 33, 0, 1547], 110: ['acc', 24, 0, 1571], 111: ['jmp', -4, 0, 1571], 112: ['acc', 36, 0, 354], 113: ['acc', 10, 0, 364], 114: ['nop', 441, 0, 364], 115: ['jmp', 268, 0, 364], 116: ['jmp', 388, 0, 120], 117: ['acc', 0, 0, 633], 118: ['acc', 27, 0, 660], 119: ['acc', -1, 0, 659], 120: ['jmp', -60, 0, 659], 121: ['nop', 90, 0, 415], 122: ['jmp', -90, 0, 415], 123: ['acc', 48, 0, 268], 124: ['acc', 30, 0, 298], 125: ['jmp', 284, 0, 298], 126: ['acc', 4, 0, 0], 127: ['acc', 6, 0, 0], 128: ['acc', 1, 0, 0], 129: ['acc', -10, 0, 0], 130: ['jmp', 95, 0, 0], 131: ['acc', 35, 0, 1087], 132: ['jmp', 235, 0, 1087], 133: ['acc', 31, 0, 799], 134: ['acc', -19, 0, 780], 135: ['jmp', -96, 0, 780], 136: ['jmp', 326, 0, 0], 137: ['acc', -7, 0, 0], 138: ['acc', 0, 0, 0], 139: ['acc', -1, 0, 0], 140: ['jmp', 53, 0, 0], 141: ['acc', 15, 0, 539], 142: ['acc', -14, 0, 525], 143: ['jmp', 450, 0, 525], 144: ['nop', 8, 0, 206], 145: ['acc', -2, 0, 204], 146: ['acc', -1, 0, 203], 147: ['acc', 17, 0, 220], 148: ['jmp', -25, 0, 220], 149: ['nop', 444, 0, 629], 150: ['jmp', 65, 0, 629], 151: ['jmp', -86, 0, 104], 152: ['acc', 44, 0, 1171], 153: ['acc', 16, 0, 1187], 154: ['acc', 32, 0, 1219], 155: ['acc', -11, 0, 1208], 156: ['jmp', 32, 0, 1208], 157: ['acc', 14, 0, 697], 158: ['acc', 28, 0, 725], 159: ['jmp', 123, 0, 725], 160: ['jmp', 127, 0, 303], 161: ['jmp', -44, 0, 1335], 162: ['acc', 42, 0, 1462], 163: ['acc', 24, 0, 1486], 164: ['acc', -3, 0, 1483], 165: ['acc', 4, 0, 1487], 166: ['jmp', 219, 0, 1487], 167: ['acc', 28, 0, 882], 168: ['acc', 30, 0, 912], 169: ['acc', -14, 0, 898], 170: ['acc', -11, 0, 887], 171: ['jmp', 67, 0, 887], 172: ['acc', 5, 0, 376], 173: ['acc', 43, 0, 419], 174: ['acc', 23, 0, 442], 175: ['nop', 73, 0, 442], 176: ['jmp', 176, 0, 442], 177: ['acc', 28, 0, 655], 178: ['acc', 8, 0, 663], 179: ['acc', 42, 0, 705], 180: ['acc', 44, 0, 749], 181: ['jmp', 278, 0, 749], 182: ['acc', 9, 0, 0], 183: ['acc', 46, 0, 0], 184: ['acc', 0, 0, 0], 185: ['acc', 30, 0, 0], 186: ['jmp', 72, 0, 0], 187: ['jmp', 317, 0, 0], 188: ['jmp', 352, 0, 1208], 189: ['jmp', 273, 0, 1393], 190: ['jmp', 137, 0, 1356], 191: ['nop', 364, 0, 992], 192: ['jmp', 249, 0, 992], 193: ['nop', 79, 0, 181], 194: ['jmp', 1, 0, 181], 195: ['nop', -147, 0, 181], 196: ['acc', -10, 0, 0], 197: ['acc', -1, 0, 0], 198: ['acc', 12, 0, 0], 199: ['acc', 27, 0, 0], 200: ['jmp', 147, 0, 0], 201: ['acc', -5, 0, 228], 202: ['acc', 7, 0, 235], 203: ['jmp', 63, 0, 235], 204: ['acc', 33, 0, 0], 205: ['acc', 32, 0, 0], 206: ['nop', 81, 0, 0], 207: ['jmp', -185, 0, 0], 208: ['acc', 44, 0, 802], 209: ['jmp', 215, 0, 802], 210: ['jmp', 187, 0, 0], 211: ['acc', 14, 0, 874], 212: ['acc', 38, 0, 912], 213: ['jmp', -113, 0, 912], 214: ['jmp', 267, 0, 0], 215: ['acc', -9, 0, 620], 216: ['acc', 21, 0, 641], 217: ['acc', -5, 0, 636], 218: ['jmp', 143, 0, 636], 219: ['nop', -57, 0, 0], 220: ['nop', 281, 0, 0], 221: ['jmp', -170, 0, 0], 222: ['jmp', 267, 0, 303], 223: ['nop', -131, 0, 0], 224: ['jmp', -83, 0, 0], 225: ['acc', -6, 0, 1052], 226: ['jmp', -95, 0, 1052], 227: ['acc', -9, 0, 0], 228: ['acc', -8, 0, 0], 229: ['jmp', 184, 0, 0], 230: ['acc', 32, 0, 213], 231: ['acc', -16, 0, 197], 232: ['jmp', 171, 0, 197], 233: ['acc', 5, 0, 0], 234: ['acc', 22, 0, 0], 235: ['acc', -7, 0, 0], 236: ['acc', 20, 0, 0], 237: ['jmp', 45, 0, 0], 238: ['acc', 48, 0, 1420], 239: ['jmp', 239, 0, 1420], 240: ['acc', -4, 0, 0], 241: ['jmp', 75, 0, 0], 242: ['acc', -18, 0, 966], 243: ['jmp', -178, 0, 966], 244: ['nop', 349, 0, 0], 245: ['acc', -12, 0, 0], 246: ['nop', 313, 0, 0], 247: ['jmp', -57, 0, 0], 248: ['acc', 7, 0, 634], 249: ['acc', 6, 0, 640], 250: ['jmp', -241, 0, 640], 251: ['acc', 19, 0, 0], 252: ['jmp', 320, 0, 0], 253: ['acc', 13, 0, 181], 254: ['jmp', -61, 0, 181], 255: ['acc', 0, 0, 0], 256: ['nop', 337, 0, 0], 257: ['jmp', 66, 0, 0], 258: ['acc', 27, 0, 221], 259: ['acc', -11, 0, 210], 260: ['acc', -7, 0, 203], 261: ['jmp', 315, 0, 203], 262: ['acc', 23, 0, 0], 263: ['acc', 26, 0, 0], 264: ['acc', -5, 0, 0], 265: ['jmp', 132, 0, 0], 266: ['acc', 45, 0, 280], 267: ['acc', 21, 0, 301], 268: ['acc', -12, 0, 289], 269: ['jmp', 158, 0, 289], 270: ['acc', 19, 0, 0], 271: ['jmp', 176, 0, 0], 272: ['acc', 43, 0, 43], 273: ['jmp', 124, 0, 43], 274: ['nop', 227, 0, 0], 275: ['nop', -236, 0, 0], 276: ['acc', 11, 0, 0], 277: ['jmp', 1, 0, 0], 278: ['jmp', -67, 0, 0], 279: ['acc', 21, 0, 879], 280: ['jmp', 161, 0, 879], 281: ['jmp', 86, 0, 0], 282: ['acc', 26, 0, 751], 283: ['acc', 7, 0, 758], 284: ['jmp', 246, 0, 758], 285: ['acc', 0, 0, 0], 286: ['jmp', 215, 0, 0], 287: ['jmp', 1, 0, 303], 288: ['acc', 16, 0, 319], 289: ['jmp', -257, 0, 319], 290: ['acc', 2, 0, 0], 291: ['jmp', 281, 0, 0], 292: ['nop', -10, 0, 229], 293: ['acc', 46, 0, 275], 294: ['jmp', 124, 0, 275], 295: ['acc', 13, 0, 0], 296: ['acc', 24, 0, 0], 297: ['jmp', 204, 0, 0], 298: ['jmp', 1, 0, 0], 299: ['acc', 23, 0, 0], 300: ['jmp', 225, 0, 0], 301: ['nop', -243, 0, 0], 302: ['jmp', 167, 0, 0], 303: ['jmp', 1, 0, 1420], 304: ['jmp', -142, 0, 1420], 305: ['acc', -15, 0, 0], 306: ['jmp', -113, 0, 0], 307: ['acc', 27, 0, 0], 308: ['acc', -18, 0, 0], 309: ['acc', 12, 0, 0], 310: ['jmp', -259, 0, 0], 311: ['nop', 74, 0, 0], 312: ['acc', 35, 0, 0], 313: ['acc', 42, 0, 0], 314: ['acc', -4, 0, 0], 315: ['jmp', -166, 0, 0], 316: ['nop', 87, 0, 700], 317: ['nop', 86, 0, 700], 318: ['acc', 18, 0, 718], 319: ['acc', -2, 0, 716], 320: ['jmp', 212, 0, 716], 321: ['acc', -8, 0, 0], 322: ['jmp', -313, 0, 0], 323: ['acc', 36, 0, 995], 324: ['acc', -11, 0, 984], 325: ['jmp', -233, 0, 984], 326: ['jmp', 237, 0, 0], 327: ['nop', 67, 0, 1356], 328: ['acc', 16, 0, 1372], 329: ['nop', -57, 0, 1372], 330: ['jmp', -92, 0, 1372], 331: ['acc', 48, 0, 0], 332: ['acc', 2, 0, 0], 333: ['acc', 21, 0, 0], 334: ['jmp', 33, 0, 0], 335: ['acc', -15, 0, 0], 336: ['jmp', 145, 0, 0], 337: ['acc', 26, 0, 0], 338: ['jmp', -254, 0, 0], 339: ['acc', 30, 0, 869], 340: ['acc', 4, 0, 873], 341: ['acc', -1, 0, 872], 342: ['acc', -14, 0, 858], 343: ['jmp', -64, 0, 858], 344: ['acc', 32, 0, 0], 345: ['acc', 8, 0, 0], 346: ['jmp', -131, 0, 0], 347: ['acc', -13, 0, 0], 348: ['jmp', 138, 0, 0], 349: ['acc', 5, 0, 0], 350: ['acc', 4, 0, 0], 351: ['jmp', -4, 0, 0], 352: ['acc', 37, 0, 479], 353: ['nop', -278, 0, 479], 354: ['acc', 28, 0, 507], 355: ['acc', 17, 0, 524], 356: ['jmp', -215, 0, 524], 357: ['jmp', -104, 0, 0], 358: ['nop', -241, 0, 700], 359: ['jmp', -43, 0, 700], 360: ['jmp', -2, 0, 0], 361: ['acc', 5, 0, 641], 362: ['acc', -1, 0, 640], 363: ['jmp', 151, 0, 640], 364: ['jmp', 1, 0, 0], 365: ['acc', 21, 0, 0], 366: ['jmp', 19, 0, 0], 367: ['acc', 40, 0, 1127], 368: ['jmp', 91, 0, 1127], 369: ['acc', 50, 0, 0], 370: ['nop', 202, 0, 0], 371: ['acc', -12, 0, 0], 372: ['jmp', -333, 0, 0], 373: ['nop', -66, 0, 195], 374: ['acc', 42, 0, 237], 375: ['acc', 7, 0, 244], 376: ['jmp', 1, 0, 244], 377: ['jmp', 47, 0, 244], 378: ['acc', 32, 0, 0], 379: ['acc', 29, 0, 0], 380: ['acc', 42, 0, 0], 381: ['nop', -8, 0, 0], 382: ['jmp', 52, 0, 0], 383: ['jmp', -299, 0, 364], 384: ['jmp', 40, 0, 0], 385: ['acc', 36, 0, 1523], 386: ['acc', -5, 0, 1518], 387: ['acc', 39, 0, 1557], 388: ['jmp', -116, 0, 1557], 389: ['acc', 19, 0, 0], 390: ['acc', 30, 0, 0], 391: ['acc', 39, 0, 0], 392: ['acc', -1, 0, 0], 393: ['jmp', -276, 0, 0], 394: ['jmp', -245, 0, 629], 395: ['acc', 6, 0, 0], 396: ['jmp', -185, 0, 0], 397: ['acc', 50, 0, 93], 398: ['acc', 14, 0, 107], 399: ['acc', -7, 0, 100], 400: ['jmp', -325, 0, 100], 401: ['acc', 33, 0, 0], 402: ['jmp', -279, 0, 0], 403: ['nop', 173, 0, 197], 404: ['acc', 15, 0, 212], 405: ['acc', -17, 0, 195], 406: ['jmp', -33, 0, 195], 407: ['acc', 20, 0, 0], 408: ['jmp', -101, 0, 0], 409: ['acc', -17, 0, 281], 410: ['jmp', -335, 0, 281], 411: ['nop', -8, 0, 0], 412: ['jmp', 22, 0, 0], 413: ['acc', 0, 0, 0], 414: ['acc', 4, 0, 0], 415: ['jmp', -133, 0, 0], 416: ['nop', -81, 0, 0], 417: ['jmp', 64, 0, 0], 418: ['jmp', -306, 0, 318], 419: ['acc', -19, 0, 0], 420: ['acc', 31, 0, 0], 421: ['acc', 47, 0, 0], 422: ['acc', 26, 0, 0], 423: ['jmp', 55, 0, 0], 424: ['jmp', -402, 0, 244], 425: ['acc', 13, 0, 0], 426: ['jmp', -375, 0, 0], 427: ['acc', 6, 0, 295], 428: ['acc', -1, 0, 294], 429: ['acc', -6, 0, 288], 430: ['acc', 49, 0, 337], 431: ['jmp', -28, 0, 337], 432: ['acc', -7, 0, 0], 433: ['jmp', -203, 0, 0], 434: ['jmp', -395, 0, 0], 435: ['acc', 5, 0, 0], 436: ['acc', 38, 0, 0], 437: ['acc', 10, 0, 0], 438: ['jmp', 130, 0, 0], 439: ['jmp', 161, 0, 0], 440: ['jmp', -382, 0, 0], 441: ['acc', 45, 0, 924], 442: ['jmp', 113, 0, 924], 443: ['acc', 38, 0, 0], 444: ['acc', 48, 0, 0], 445: ['acc', 46, 0, 0], 446: ['jmp', 126, 0, 0], 447: ['acc', -1, 0, 38], 448: ['acc', -10, 0, 28], 449: ['acc', 4, 0, 32], 450: ['acc', 2, 0, 34], 451: ['jmp', -425, 0, 34], 452: ['acc', 0, 0, 0], 453: ['jmp', -80, 0, 0], 454: ['acc', 4, 0, 168], 455: ['jmp', -202, 0, 168], 456: ['acc', 25, 0, 0], 457: ['acc', 8, 0, 0], 458: ['jmp', -398, 0, 0], 459: ['jmp', -307, 0, 1127], 460: ['acc', 3, 0, 0], 461: ['jmp', 17, 0, 0], 462: ['acc', 13, 0, 1406], 463: ['acc', 33, 0, 1439], 464: ['acc', 7, 0, 1446], 465: ['jmp', -381, 0, 1446], 466: ['acc', 5, 0, 0], 467: ['acc', 12, 0, 0], 468: ['jmp', -308, 0, 0], 469: ['jmp', 1, 0, 0], 470: ['acc', 3, 0, 0], 471: ['acc', -14, 0, 0], 472: ['acc', 46, 0, 0], 473: ['jmp', -415, 0, 0], 474: ['acc', 31, 0, 0], 475: ['acc', 7, 0, 0], 476: ['acc', 28, 0, 0], 477: ['jmp', -419, 0, 0], 478: ['jmp', -175, 0, 1420], 479: ['jmp', 1, 0, 0], 480: ['jmp', -141, 0, 0], 481: ['acc', 20, 0, 0], 482: ['nop', -35, 0, 0], 483: ['jmp', -36, 0, 0], 484: ['acc', -6, 0, 0], 485: ['jmp', 108, 0, 0], 486: ['nop', 1, 0, 0], 487: ['jmp', 8, 0, 0], 488: ['jmp', -49, 0, 0], 489: ['jmp', -389, 0, 303], 490: ['acc', 24, 0, 0], 491: ['nop', -482, 0, 0], 492: ['acc', 41, 0, 0], 493: ['acc', 25, 0, 0], 494: ['jmp', -167, 0, 0], 495: ['nop', -26, 0, 0], 496: ['jmp', -198, 0, 0], 497: ['nop', -199, 0, 0], 498: ['acc', 23, 0, 0], 499: ['acc', -19, 0, 0], 500: ['jmp', -202, 0, 0], 501: ['jmp', 58, 0, 0], 502: ['acc', 3, 0, 0], 503: ['jmp', -237, 0, 0], 504: ['acc', 44, 0, 164], 505: ['acc', 42, 0, 206], 506: ['acc', 22, 0, 228], 507: ['acc', 5, 0, 233], 508: ['jmp', -307, 0, 233], 509: ['acc', 45, 0, 0], 510: ['nop', -418, 0, 0], 511: ['acc', 41, 0, 0], 512: ['nop', -88, 0, 0], 513: ['jmp', 63, 0, 0], 514: ['acc', 12, 0, 652], 515: ['nop', -56, 0, 652], 516: ['acc', -19, 0, 633], 517: ['jmp', 55, 0, 633], 518: ['acc', -13, 0, 0], 519: ['acc', -7, 0, 0], 520: ['jmp', -213, 0, 0], 521: ['acc', 42, 0, 0], 522: ['jmp', -88, 0, 0], 523: ['acc', 20, 0, 0], 524: ['jmp', -115, 0, 0], 525: ['acc', 6, 0, 0], 526: ['jmp', -57, 0, 0], 527: ['acc', 25, 0, 0], 528: ['acc', 49, 0, 0], 529: ['jmp', -43, 0, 0], 530: ['jmp', -322, 0, 758], 531: ['jmp', -456, 0, 0], 532: ['acc', 7, 0, 723], 533: ['acc', 40, 0, 763], 534: ['acc', 35, 0, 798], 535: ['jmp', -518, 0, 798], 536: ['nop', -461, 0, 0], 537: ['acc', 43, 0, 0], 538: ['acc', 33, 0, 0], 539: ['jmp', 7, 0, 0], 540: ['acc', 27, 0, 1235], 541: ['jmp', 5, 0, 1235], 542: ['acc', -15, 0, 0], 543: ['acc', -19, 0, 0], 544: ['acc', -2, 0, 0], 545: ['jmp', -238, 0, 0], 546: ['acc', 49, 0, 1284], 547: ['acc', 48, 0, 1332], 548: ['acc', -16, 0, 1316], 549: ['jmp', 34, 0, 1316], 550: ['acc', -6, 0, 0], 551: ['acc', 49, 0, 0], 552: ['acc', -4, 0, 0], 553: ['acc', 4, 0, 0], 554: ['jmp', 1, 0, 0], 555: ['acc', 35, 0, 959], 556: ['nop', -264, 0, 959], 557: ['jmp', -234, 0, 959], 558: ['jmp', -365, 0, 0], 559: ['jmp', -436, 0, 356], 560: ['acc', 20, 0, 0], 561: ['acc', 36, 0, 0], 562: ['jmp', -426, 0, 0], 563: ['acc', 39, 0, 283], 564: ['acc', 20, 0, 303], 565: ['jmp', -343, 0, 303], 566: ['nop', -443, 0, 0], 567: ['jmp', -325, 0, 0], 568: ['jmp', -127, 0, 680], 569: ['nop', -560, 0, 0], 570: ['acc', 10, 0, 0], 571: ['jmp', -511, 0, 0], 572: ['jmp', -455, 0, 633], 573: ['acc', -16, 0, 0], 574: ['acc', 18, 0, 0], 575: ['jmp', -61, 0, 0], 576: ['acc', 26, 0, 229], 577: ['jmp', -285, 0, 229], 578: ['jmp', 1, 0, 0], 579: ['nop', -397, 0, 0], 580: ['acc', 12, 0, 0], 581: ['nop', -67, 0, 0], 582: ['jmp', -371, 0, 0], 583: ['acc', 27, 0, 1343], 584: ['acc', 13, 0, 1356], 585: ['jmp', -395, 0, 1356], 586: ['acc', 44, 0, 0], 587: ['jmp', -565, 0, 0], 588: ['acc', 1, 0, 680], 589: ['jmp', -21, 0, 680], 590: ['nop', -428, 0, 0], 591: ['acc', -4, 0, 0], 592: ['jmp', -265, 0, 0], 593: ['acc', 48, 0, 573], 594: ['acc', 10, 0, 583], 595: ['acc', 46, 0, 629], 596: ['jmp', -202, 0, 629], 597: ['acc', -4, 0, 0], 598: ['acc', -10, 0, 0], 599: ['jmp', -152, 0, 0], 600: ['acc', 17, 0, 0], 601: ['acc', -10, 0, 0], 602: ['acc', 22, 0, 0], 603: ['acc', 10, 0, 0], 604: ['jmp', 1, 0, 0]}
for z in range(0, len(mydict)):
  mydict[z][2] = 0
# while counter < 10:
while mydict[counter][2] == 0:

    if mydict[counter][0] == 'jmp':# and mydict[counter][2] == 0:
        mydict[counter] = [mydict[counter][0], mydict[counter][1], 1]
        counter = counter+mydict[counter][1]

    elif mydict[counter][0] == 'acc':
        acc += mydict[counter][1]
        mydict[counter] = [mydict[counter][0], mydict[counter][1], 1]
        counter += 1
    else: #mydict[counter][2] == 0:
        mydict[counter] = [mydict[counter][0], mydict[counter][1], 1]
        counter += 1
    print(acc)

print(acc)
print(mydict)