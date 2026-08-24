# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 392
- HTTP: 94 alive / 54 gold
- HTTPS: 55 alive / 13 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33553
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
