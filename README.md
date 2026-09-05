# SyndProxy validated proxy pool

## Current pool

- Alive now: 399
- Gold now: 308
- HTTP: 106 alive / 75 gold
- HTTPS: 36 alive / 15 gold
- SOCKS4: 85 alive / 72 gold
- SOCKS5: 172 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47834
- Ever gold: 1498

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
