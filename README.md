# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 415
- HTTP: 351 alive / 87 gold
- HTTPS: 234 alive / 30 gold
- SOCKS4: 231 alive / 144 gold
- SOCKS5: 239 alive / 154 gold

## Historical pool

- Discovered: 159211
- Ever alive: 30199
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
