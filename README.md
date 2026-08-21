# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 420
- HTTP: 303 alive / 96 gold
- HTTPS: 210 alive / 26 gold
- SOCKS4: 206 alive / 138 gold
- SOCKS5: 273 alive / 160 gold

## Historical pool

- Discovered: 154717
- Ever alive: 29025
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
