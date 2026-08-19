# SyndProxy private pool

## Current pool

- Alive now: 898
- Gold now: 472
- HTTP: 285 alive / 121 gold
- HTTPS: 210 alive / 86 gold
- SOCKS4: 183 alive / 125 gold
- SOCKS5: 220 alive / 140 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17495
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
