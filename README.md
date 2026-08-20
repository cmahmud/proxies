# SyndProxy private pool

## Current pool

- Alive now: 829
- Gold now: 379
- HTTP: 191 alive / 76 gold
- HTTPS: 225 alive / 17 gold
- SOCKS4: 204 alive / 150 gold
- SOCKS5: 209 alive / 136 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26858
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
