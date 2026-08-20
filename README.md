# SyndProxy private pool

## Current pool

- Alive now: 812
- Gold now: 373
- HTTP: 198 alive / 80 gold
- HTTPS: 216 alive / 19 gold
- SOCKS4: 199 alive / 135 gold
- SOCKS5: 199 alive / 139 gold

## Historical pool

- Discovered: 148840
- Ever alive: 26516
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
