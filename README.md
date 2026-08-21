# SyndProxy private pool

## Current pool

- Alive now: 920
- Gold now: 408
- HTTP: 274 alive / 76 gold
- HTTPS: 154 alive / 24 gold
- SOCKS4: 240 alive / 158 gold
- SOCKS5: 252 alive / 150 gold

## Historical pool

- Discovered: 156825
- Ever alive: 29612
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
