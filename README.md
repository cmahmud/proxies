# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 421
- HTTP: 333 alive / 102 gold
- HTTPS: 190 alive / 36 gold
- SOCKS4: 217 alive / 139 gold
- SOCKS5: 230 alive / 144 gold

## Historical pool

- Discovered: 160257
- Ever alive: 30701
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
