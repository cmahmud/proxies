# SyndProxy private pool

## Current pool

- Alive now: 997
- Gold now: 320
- HTTP: 295 alive / 36 gold
- HTTPS: 213 alive / 10 gold
- SOCKS4: 250 alive / 142 gold
- SOCKS5: 239 alive / 132 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14238
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
