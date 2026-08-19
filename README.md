# SyndProxy private pool

## Current pool

- Alive now: 1211
- Gold now: 526
- HTTP: 439 alive / 183 gold
- HTTPS: 342 alive / 78 gold
- SOCKS4: 221 alive / 126 gold
- SOCKS5: 209 alive / 139 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19789
- Ever gold: 797

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
