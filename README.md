# SyndProxy private pool

## Current pool

- Alive now: 684
- Gold now: 375
- HTTP: 179 alive / 69 gold
- HTTPS: 87 alive / 13 gold
- SOCKS4: 198 alive / 137 gold
- SOCKS5: 220 alive / 156 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25799
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
