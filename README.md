# SyndProxy private pool

## Current pool

- Alive now: 714
- Gold now: 378
- HTTP: 177 alive / 73 gold
- HTTPS: 139 alive / 19 gold
- SOCKS4: 203 alive / 148 gold
- SOCKS5: 195 alive / 138 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26222
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
