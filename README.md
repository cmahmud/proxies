# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 393
- HTTP: 101 alive / 56 gold
- HTTPS: 55 alive / 12 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33553
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
