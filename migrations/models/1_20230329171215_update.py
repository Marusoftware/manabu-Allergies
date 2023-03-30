from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP CONSTRAINT "user_name_key";
        DROP INDEX "idx_user_name_76f409";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD CONSTRAINT "user_name_key" UNIQUE ("name");
        CREATE UNIQUE INDEX "idx_user_name_76f409" ON "user" ("name");"""
