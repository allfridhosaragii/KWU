# V15 Frontend-only deployment optimization

When only source UI code, CSS, cache-busting, or documentation changes, use tracked 3D assets instead of rebuilding all models and thousands of turntable frames. Model generation still runs when actual model scripts, GLB assets, previews, or 360 atlases change, and runs for manual workflow dispatch. This reduces publishing time and prevents stale 3D changes due to concurrency. All deployments still run npm build, TypeScript, and static integrity checks. 
