# SyndProxy private pool

## Current pool

- Alive now: 740
- Gold now: 375
- HTTP: 180 alive / 65 gold
- HTTPS: 157 alive / 20 gold
- SOCKS4: 207 alive / 152 gold
- SOCKS5: 196 alive / 138 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25924
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
