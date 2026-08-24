# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 394
- HTTP: 130 alive / 61 gold
- HTTPS: 63 alive / 13 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 180 alive / 160 gold

## Historical pool

- Discovered: 179921
- Ever alive: 33508
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
