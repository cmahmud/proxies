# SyndProxy validated proxy pool

## Current pool

- Alive now: 382
- Gold now: 292
- HTTP: 109 alive / 75 gold
- HTTPS: 45 alive / 21 gold
- SOCKS4: 72 alive / 65 gold
- SOCKS5: 156 alive / 131 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47893
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
