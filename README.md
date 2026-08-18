# SyndProxy private pool

## Current pool

- Alive now: 839
- Gold now: 261
- HTTP: 239 alive / 30 gold
- HTTPS: 153 alive / 3 gold
- SOCKS4: 220 alive / 118 gold
- SOCKS5: 227 alive / 110 gold

## Historical pool

- Discovered: 99160
- Ever alive: 12099
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
