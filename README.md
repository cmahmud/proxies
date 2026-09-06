# SyndProxy validated proxy pool

## Current pool

- Alive now: 435
- Gold now: 322
- HTTP: 89 alive / 57 gold
- HTTPS: 31 alive / 9 gold
- SOCKS4: 146 alive / 138 gold
- SOCKS5: 169 alive / 118 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48403
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
