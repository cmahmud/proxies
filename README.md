# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 390
- HTTP: 112 alive / 60 gold
- HTTPS: 63 alive / 14 gold
- SOCKS4: 173 alive / 156 gold
- SOCKS5: 178 alive / 160 gold

## Historical pool

- Discovered: 179921
- Ever alive: 33511
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
