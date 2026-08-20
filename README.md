# SyndProxy private pool

## Current pool

- Alive now: 800
- Gold now: 364
- HTTP: 236 alive / 63 gold
- HTTPS: 154 alive / 13 gold
- SOCKS4: 206 alive / 150 gold
- SOCKS5: 204 alive / 138 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25905
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
