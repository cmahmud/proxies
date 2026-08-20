# SyndProxy private pool

## Current pool

- Alive now: 728
- Gold now: 390
- HTTP: 150 alive / 78 gold
- HTTPS: 149 alive / 23 gold
- SOCKS4: 198 alive / 128 gold
- SOCKS5: 231 alive / 161 gold

## Historical pool

- Discovered: 150719
- Ever alive: 27079
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
