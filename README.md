# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 400
- HTTP: 99 alive / 57 gold
- HTTPS: 43 alive / 14 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36779
- Ever gold: 1279

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
