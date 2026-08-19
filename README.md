# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 401
- HTTP: 288 alive / 77 gold
- HTTPS: 224 alive / 12 gold
- SOCKS4: 258 alive / 152 gold
- SOCKS5: 243 alive / 160 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20547
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
