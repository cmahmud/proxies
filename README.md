# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 391
- HTTP: 119 alive / 59 gold
- HTTPS: 64 alive / 12 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 178 alive / 160 gold

## Historical pool

- Discovered: 179921
- Ever alive: 33508
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
