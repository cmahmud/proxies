# SyndProxy private pool

## Current pool

- Alive now: 729
- Gold now: 374
- HTTP: 186 alive / 78 gold
- HTTPS: 138 alive / 17 gold
- SOCKS4: 216 alive / 150 gold
- SOCKS5: 189 alive / 129 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25935
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
