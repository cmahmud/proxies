# SyndProxy validated proxy pool

## Current pool

- Alive now: 395
- Gold now: 315
- HTTP: 103 alive / 80 gold
- HTTPS: 54 alive / 24 gold
- SOCKS4: 82 alive / 74 gold
- SOCKS5: 156 alive / 137 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47932
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
