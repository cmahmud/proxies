# SyndProxy private pool

## Current pool

- Alive now: 963
- Gold now: 370
- HTTP: 331 alive / 78 gold
- HTTPS: 198 alive / 23 gold
- SOCKS4: 209 alive / 138 gold
- SOCKS5: 225 alive / 131 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32360
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
