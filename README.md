# SyndProxy private pool

## Current pool

- Alive now: 770
- Gold now: 379
- HTTP: 202 alive / 68 gold
- HTTPS: 165 alive / 22 gold
- SOCKS4: 207 alive / 148 gold
- SOCKS5: 196 alive / 141 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26184
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
