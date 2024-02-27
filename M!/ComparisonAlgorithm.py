
def cleanPrice(price:str):
    return int(price.lower().replace(',','').replace('.','').replace('₹','').replace('rs','').strip())

def cleanRating(rating:str):
    if 'out' in rating:
        return float(rating.split(' out')[0])
    else:
        return float(rating)

def cleanReviews(reviews:str):
    return int(reviews.lower().replace(',','').replace('reviews','').strip())


def Best_Platform_Identifier_Algorithm(amaz_price,amz_rat,flp_prirce,flp_rat,snap_price,snap_rev,rel_pric,rel_rat):


    amaz_price = cleanPrice(amaz_price)
    flp_prirce = cleanPrice(flp_prirce)

    amz_rat = cleanRating(amz_rat)
    flp_rat = cleanRating(flp_rat)

    best_platform = ''

    if amaz_price-flp_prirce > 0:
        if (amaz_price-flp_prirce) > amaz_price*0.01:
            best_platform = "Flipkart"    
    else:
        if (flp_prirce-amaz_price) > flp_prirce*0.01:
            best_platform = "Amazon"

    if best_platform=='':
        if amz_rat>flp_rat:
            if (amz_rat-flp_rat) > 0.8:
                best_platform = "Amazon"    
        else:
            if (flp_rat-amz_rat) > 0.8:
                best_platform = "Flipkart"


    if best_platform=='':
        best_platform = 'Amazon'        
    
    try:
        snp_price = cleanPrice(snap_price)
        rel_prirce = cleanPrice(rel_pric)

        snp_rat = cleanRating(snap_rev)
        rel_rat = cleanRating(rel_rat)

        worst_platform = ''

        if snp_price-flp_prirce > 0:
            if (snp_price-flp_prirce) > snp_price*0.01:
                worst_platform = "Snapdeal"    
        else:
            if (flp_prirce-amaz_price) > flp_prirce*0.01:
                worst_platform = "Relience"

        if worst_platform=='':
            if amz_rat>flp_rat:
                if (amz_rat-flp_rat) > 0.8:
                    worst_platform = "Snapdeal"    
            else:
                if (flp_rat-amz_rat) > 0.8:
                    worst_platform = "Relience"

    except Exception as e:
        e
        # print(e)
    
    return best_platform



# print(Best_Platform_Identifier_Algorithm('5000','2.5','2000','2.0'))
# print(Best_Platform_Identifier_Algorithm('2000','5.0','2000','2.0'))
# print(Best_Platform_Identifier_Algorithm('2000','2.0','2000','5.0'))
# print(Best_Platform_Identifier_Algorithm('2000','2.0','2000','2.0'))
















