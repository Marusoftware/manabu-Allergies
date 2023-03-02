from fastapi import APIRouter

router=APIRouter()

from .auth import router as auth
router.include_router(auth, prefix="/auth")