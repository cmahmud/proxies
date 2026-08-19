# SyndProxy private pool

## Current pool

- Alive now: 966
- Gold now: 327
- HTTP: 338 alive / 60 gold
- HTTPS: 183 alive / 15 gold
- SOCKS4: 199 alive / 124 gold
- SOCKS5: 246 alive / 128 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20116
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
