# SyndProxy private pool

## Current pool

- Alive now: 893
- Gold now: 360
- HTTP: 290 alive / 85 gold
- HTTPS: 186 alive / 18 gold
- SOCKS4: 218 alive / 142 gold
- SOCKS5: 199 alive / 115 gold

## Historical pool

- Discovered: 119837
- Ever alive: 18343
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
