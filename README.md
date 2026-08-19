# SyndProxy private pool

## Current pool

- Alive now: 1132
- Gold now: 598
- HTTP: 441 alive / 188 gold
- HTTPS: 262 alive / 110 gold
- SOCKS4: 213 alive / 144 gold
- SOCKS5: 216 alive / 156 gold

## Historical pool

- Discovered: 124852
- Ever alive: 19415
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
