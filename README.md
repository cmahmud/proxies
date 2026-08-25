# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 400
- HTTP: 99 alive / 57 gold
- HTTPS: 46 alive / 15 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36779
- Ever gold: 1279

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
