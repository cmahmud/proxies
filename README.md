# SyndProxy private pool

## Current pool

- Alive now: 1028
- Gold now: 425
- HTTP: 274 alive / 85 gold
- HTTPS: 236 alive / 28 gold
- SOCKS4: 233 alive / 142 gold
- SOCKS5: 285 alive / 170 gold

## Historical pool

- Discovered: 164944
- Ever alive: 32213
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
