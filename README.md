# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 410
- HTTP: 96 alive / 61 gold
- HTTPS: 71 alive / 22 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36934
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
