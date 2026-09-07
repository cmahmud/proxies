# SyndProxy validated proxy pool

## Current pool

- Alive now: 428
- Gold now: 340
- HTTP: 84 alive / 57 gold
- HTTPS: 32 alive / 11 gold
- SOCKS4: 145 alive / 138 gold
- SOCKS5: 167 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48403
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
