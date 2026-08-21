# SyndProxy private pool

## Current pool

- Alive now: 935
- Gold now: 385
- HTTP: 277 alive / 69 gold
- HTTPS: 195 alive / 19 gold
- SOCKS4: 231 alive / 142 gold
- SOCKS5: 232 alive / 155 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29572
- Ever gold: 1130

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
