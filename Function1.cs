using System;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Newtonsoft.Json;

public static class Function1
{
    private static readonly HttpClient client = new HttpClient();

    [FunctionName("Function1")]
    public static async Task Run([ServiceBusTrigger("reviewstobeprocessed", Connection = "Endpoint=sb://surveyedbus.servicebus.windows.net/;SharedAccessKeyName=full_access;SharedAccessKey=vn+Mb5dOZ6cbk8XwHJd4CfJS1FBixicZM+ASbHjVH2o=")]string myQueueItem, TraceWriter log)
    {
        log.Info($"C# ServiceBus queue trigger function processed message: {myQueueItem}");

        var credentials = JsonConvert.DeserializeObject<Credentials>(myQueueItem);

        await FetchFacebookReviews(credentials);
    }

    public class Credentials
    {
        public string AccessToken { get; set; }
        public string AppId { get; set; }
        public string AppSecret { get; set; }
        public string PageId { get; set; }
    }

    public static async Task FetchFacebookReviews(Credentials credentials)
    {
        string requestUri = $"https://graph.facebook.com/v12.0/{credentials.PageId}/ratings?access_token={credentials.AccessToken}";
        
        HttpResponseMessage response = await client.GetAsync(requestUri);

        if (response.IsSuccessStatusCode)
        {
            string responseBody = await response.Content.ReadAsStringAsync();
            // Log the response body for debugging purposes
            Console.WriteLine(responseBody);
            // Parse the response body. A more detailed parsing might be needed based on the structure of the returned JSON.
            var reviews = JsonConvert.DeserializeObject<Reviews>(responseBody);
            // Process the reviews as needed
        }
        else
        {
            Console.WriteLine($"Failed to fetch reviews: {response.StatusCode}");
        }
    }

    public class Review
    {
        public string CreatedTime { get; set; }
        public From From { get; set; }
        public string Message { get; set; }
    }

    public class From
    {
        public string Name { get; set; }
        public string Id { get; set; }
    }

    public class Reviews
    {
        public List<Review> Data { get; set; }
        public Paging Paging { get; set; }
    }

    public class Paging
    {
        public Cursors Cursors { get; set; }
        public string Next { get; set; }
    }

    public class Cursors
    {
        public string Before { get; set; }
        public string After { get; set; }
    }
}
