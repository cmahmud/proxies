# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 391
- HTTP: 126 alive / 68 gold
- HTTPS: 49 alive / 13 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 180 alive / 151 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33280
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
