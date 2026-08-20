# SyndProxy private pool

## Current pool

- Alive now: 684
- Gold now: 383
- HTTP: 163 alive / 75 gold
- HTTPS: 122 alive / 21 gold
- SOCKS4: 204 alive / 148 gold
- SOCKS5: 195 alive / 139 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26233
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
