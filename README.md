# SyndProxy private pool

## Current pool

- Alive now: 767
- Gold now: 378
- HTTP: 203 alive / 68 gold
- HTTPS: 156 alive / 22 gold
- SOCKS4: 210 alive / 149 gold
- SOCKS5: 198 alive / 139 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26178
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
