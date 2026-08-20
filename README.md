# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 379
- HTTP: 263 alive / 70 gold
- HTTPS: 185 alive / 22 gold
- SOCKS4: 218 alive / 140 gold
- SOCKS5: 218 alive / 147 gold

## Historical pool

- Discovered: 144764
- Ever alive: 25267
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
