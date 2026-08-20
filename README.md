# SyndProxy private pool

## Current pool

- Alive now: 692
- Gold now: 373
- HTTP: 178 alive / 78 gold
- HTTPS: 104 alive / 17 gold
- SOCKS4: 208 alive / 145 gold
- SOCKS5: 202 alive / 133 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25947
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
