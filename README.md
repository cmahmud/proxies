# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 387
- HTTP: 97 alive / 66 gold
- HTTPS: 31 alive / 13 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 185 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48238
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
