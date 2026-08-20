# SyndProxy private pool

## Current pool

- Alive now: 818
- Gold now: 365
- HTTP: 242 alive / 64 gold
- HTTPS: 157 alive / 13 gold
- SOCKS4: 212 alive / 150 gold
- SOCKS5: 207 alive / 138 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25905
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
