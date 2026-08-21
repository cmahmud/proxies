# SyndProxy private pool

## Current pool

- Alive now: 734
- Gold now: 401
- HTTP: 197 alive / 89 gold
- HTTPS: 120 alive / 21 gold
- SOCKS4: 212 alive / 141 gold
- SOCKS5: 205 alive / 150 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27751
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
