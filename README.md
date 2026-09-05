# SyndProxy validated proxy pool

## Current pool

- Alive now: 376
- Gold now: 292
- HTTP: 109 alive / 78 gold
- HTTPS: 39 alive / 19 gold
- SOCKS4: 74 alive / 65 gold
- SOCKS5: 154 alive / 130 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47885
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
