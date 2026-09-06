# SyndProxy validated proxy pool

## Current pool

- Alive now: 403
- Gold now: 334
- HTTP: 76 alive / 55 gold
- HTTPS: 37 alive / 19 gold
- SOCKS4: 141 alive / 134 gold
- SOCKS5: 149 alive / 126 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48340
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
