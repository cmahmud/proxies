# SyndProxy private pool

## Current pool

- Alive now: 895
- Gold now: 367
- HTTP: 287 alive / 81 gold
- HTTPS: 181 alive / 25 gold
- SOCKS4: 204 alive / 136 gold
- SOCKS5: 223 alive / 125 gold

## Historical pool

- Discovered: 165832
- Ever alive: 32354
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
