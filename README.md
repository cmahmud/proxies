# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 408
- HTTP: 98 alive / 60 gold
- HTTPS: 63 alive / 21 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36928
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
