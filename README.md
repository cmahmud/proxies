# SyndProxy validated proxy pool

## Current pool

- Alive now: 445
- Gold now: 330
- HTTP: 106 alive / 76 gold
- HTTPS: 61 alive / 24 gold
- SOCKS4: 106 alive / 89 gold
- SOCKS5: 172 alive / 141 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47952
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
