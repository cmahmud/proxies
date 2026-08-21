# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 411
- HTTP: 217 alive / 90 gold
- HTTPS: 144 alive / 23 gold
- SOCKS4: 206 alive / 137 gold
- SOCKS5: 213 alive / 161 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27721
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
