# SyndProxy private pool

## Current pool

- Alive now: 1476
- Gold now: 619
- HTTP: 564 alive / 219 gold
- HTTPS: 457 alive / 114 gold
- SOCKS4: 209 alive / 139 gold
- SOCKS5: 246 alive / 147 gold

## Historical pool

- Discovered: 141134
- Ever alive: 23805
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
