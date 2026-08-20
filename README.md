# SyndProxy private pool

## Current pool

- Alive now: 791
- Gold now: 369
- HTTP: 241 alive / 67 gold
- HTTPS: 145 alive / 15 gold
- SOCKS4: 210 alive / 150 gold
- SOCKS5: 195 alive / 137 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25907
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
