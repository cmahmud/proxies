# SyndProxy private pool

## Current pool

- Alive now: 772
- Gold now: 375
- HTTP: 202 alive / 67 gold
- HTTPS: 162 alive / 22 gold
- SOCKS4: 209 alive / 148 gold
- SOCKS5: 199 alive / 138 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26177
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
