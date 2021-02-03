from itemadapter import ItemAdapter

class AmazonscrapPipeline(object):
  def process_item(self, item, spider):
    return item

    # conn = None
    # cur = None

    # def process_item(self, item, spider):
    #     # save book
    #     sql = "insert into books (book_id, title, author, rating, review_count) " \
    #           "VALUES ('%s', '%s', '%s', '%s', '%s' )" % \
    #           (item["book_id"], item["title"], item["author"], item["rating"], item["review_count"])
    #     try:
    #         self.cur.execute(sql)
    #         self.conn.commit()
    #     except Exception as e:
    #         self.conn.rollback()
    #         print(repr(e))

    # def open_spider(self, spider):
    #     self.conn = MySQLdb.connect(host="localhost",  # your host
    #                          user="root",  # username
    #                          passwd="p",  # password
    #                          db="amazoncrap_db")  # name of the database

    #     # Create a Cursor object to execute queries.
    #     self.cur = self.conn.cursor()

    # def close_spider(self, spider):
    #     self.cur.close()
    #     self.conn.close()

    
