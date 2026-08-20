# SyndProxy private pool

## Current pool

- Alive now: 1690
- Gold now: 654
- HTTP: 650 alive / 212 gold
- HTTPS: 497 alive / 116 gold
- SOCKS4: 231 alive / 159 gold
- SOCKS5: 312 alive / 167 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23931
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
