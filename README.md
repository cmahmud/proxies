# SyndProxy validated proxy pool

## Current pool

- Alive now: 378
- Gold now: 291
- HTTP: 108 alive / 76 gold
- HTTPS: 43 alive / 21 gold
- SOCKS4: 72 alive / 64 gold
- SOCKS5: 155 alive / 130 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47887
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
