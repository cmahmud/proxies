# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 390
- HTTP: 300 alive / 76 gold
- HTTPS: 210 alive / 12 gold
- SOCKS4: 248 alive / 148 gold
- SOCKS5: 227 alive / 154 gold

## Historical pool

- Discovered: 129305
- Ever alive: 20395
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
