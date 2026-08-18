# SyndProxy private pool

## Current pool

- Alive now: 845
- Gold now: 260
- HTTP: 238 alive / 29 gold
- HTTPS: 158 alive / 3 gold
- SOCKS4: 222 alive / 119 gold
- SOCKS5: 227 alive / 109 gold

## Historical pool

- Discovered: 99160
- Ever alive: 12099
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
