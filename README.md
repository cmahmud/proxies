# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 371
- HTTP: 135 alive / 78 gold
- HTTPS: 64 alive / 25 gold
- SOCKS4: 145 alive / 119 gold
- SOCKS5: 179 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47999
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
