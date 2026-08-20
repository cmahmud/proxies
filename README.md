# SyndProxy private pool

## Current pool

- Alive now: 1690
- Gold now: 599
- HTTP: 626 alive / 217 gold
- HTTPS: 513 alive / 107 gold
- SOCKS4: 199 alive / 135 gold
- SOCKS5: 352 alive / 140 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23887
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
