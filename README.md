# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 411
- HTTP: 99 alive / 62 gold
- HTTPS: 75 alive / 20 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 37021
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
