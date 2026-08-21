# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 366
- HTTP: 305 alive / 95 gold
- HTTPS: 183 alive / 28 gold
- SOCKS4: 224 alive / 137 gold
- SOCKS5: 215 alive / 106 gold

## Historical pool

- Discovered: 154713
- Ever alive: 28974
- Ever gold: 1117

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
