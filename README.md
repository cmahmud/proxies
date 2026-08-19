# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 400
- HTTP: 308 alive / 76 gold
- HTTPS: 233 alive / 13 gold
- SOCKS4: 264 alive / 152 gold
- SOCKS5: 251 alive / 159 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20547
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
