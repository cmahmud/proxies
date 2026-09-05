# SyndProxy validated proxy pool

## Current pool

- Alive now: 399
- Gold now: 308
- HTTP: 106 alive / 76 gold
- HTTPS: 37 alive / 15 gold
- SOCKS4: 84 alive / 72 gold
- SOCKS5: 172 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47834
- Ever gold: 1497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
