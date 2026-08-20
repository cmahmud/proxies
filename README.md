# SyndProxy private pool

## Current pool

- Alive now: 1470
- Gold now: 622
- HTTP: 570 alive / 219 gold
- HTTPS: 448 alive / 116 gold
- SOCKS4: 209 alive / 139 gold
- SOCKS5: 243 alive / 148 gold

## Historical pool

- Discovered: 141134
- Ever alive: 23804
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
