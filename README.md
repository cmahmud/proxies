# SyndProxy validated proxy pool

## Current pool

- Alive now: 429
- Gold now: 343
- HTTP: 85 alive / 63 gold
- HTTPS: 30 alive / 15 gold
- SOCKS4: 151 alive / 134 gold
- SOCKS5: 163 alive / 131 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48396
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
