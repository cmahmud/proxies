# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 463
- HTTP: 297 alive / 119 gold
- HTTPS: 203 alive / 87 gold
- SOCKS4: 195 alive / 124 gold
- SOCKS5: 213 alive / 133 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17494
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
