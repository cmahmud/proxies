# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 403
- HTTP: 296 alive / 94 gold
- HTTPS: 196 alive / 23 gold
- SOCKS4: 210 alive / 133 gold
- SOCKS5: 268 alive / 153 gold

## Historical pool

- Discovered: 154717
- Ever alive: 29026
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
