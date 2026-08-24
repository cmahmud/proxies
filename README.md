# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 393
- HTTP: 141 alive / 62 gold
- HTTPS: 65 alive / 15 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 179 alive / 160 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33511
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
