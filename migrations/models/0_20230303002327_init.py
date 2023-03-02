from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(1024) NOT NULL UNIQUE,
    "email" VARCHAR(1024) NOT NULL,
    "password" VARCHAR(1024)
);
CREATE INDEX IF NOT EXISTS "idx_user_name_76f409" ON "user" ("name");
COMMENT ON COLUMN "user"."id" IS 'User ID';
COMMENT ON COLUMN "user"."name" IS 'User short name';
COMMENT ON COLUMN "user"."email" IS 'User email';
COMMENT ON COLUMN "user"."password" IS 'User password';
CREATE TABLE IF NOT EXISTS "token" (
    "token" VARCHAR(200) NOT NULL  PRIMARY KEY,
    "token_type" VARCHAR(10) NOT NULL,
    "expired_in" TIMESTAMPTZ NOT NULL,
    "user_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "token"."token" IS 'Token';
COMMENT ON COLUMN "token"."token_type" IS 'Token Type';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
