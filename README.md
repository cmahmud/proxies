# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 371
- HTTP: 134 alive / 77 gold
- HTTPS: 61 alive / 26 gold
- SOCKS4: 150 alive / 119 gold
- SOCKS5: 180 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47999
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
