const { S3Client } = require('@aws-sdk/client-s3');

function createS3Client() {
  const endpoint = process.env.S3_ENDPOINT;
  const region = process.env.S3_REGION || 'us-east-1';
  const accessKey = process.env.S3_ACCESS_KEY;
  const secretKey = process.env.S3_SECRET_KEY;
  const forcePathStyle = !!process.env.S3_FORCE_PATH_STYLE || !!endpoint;

  const opts: any = {
    region,
    credentials: { accessKeyId: accessKey, secretAccessKey: secretKey },
  };
  if (endpoint) opts.endpoint = endpoint;
  if (forcePathStyle) opts.forcePathStyle = true;
  return new S3Client(opts);
}

module.exports = createS3Client;