# SyndProxy private pool

## Current pool

- Alive now: 699
- Gold now: 373
- HTTP: 179 alive / 78 gold
- HTTPS: 102 alive / 17 gold
- SOCKS4: 210 alive / 145 gold
- SOCKS5: 208 alive / 133 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25947
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
