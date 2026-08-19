# SyndProxy private pool

## Current pool

- Alive now: 893
- Gold now: 356
- HTTP: 290 alive / 83 gold
- HTTPS: 183 alive / 17 gold
- SOCKS4: 217 alive / 142 gold
- SOCKS5: 203 alive / 114 gold

## Historical pool

- Discovered: 119837
- Ever alive: 18343
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
