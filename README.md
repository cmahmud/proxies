# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 371
- HTTP: 331 alive / 80 gold
- HTTPS: 247 alive / 25 gold
- SOCKS4: 218 alive / 124 gold
- SOCKS5: 238 alive / 142 gold

## Historical pool

- Discovered: 165816
- Ever alive: 32324
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
