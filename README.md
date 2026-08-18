# SyndProxy private pool

## Current pool

- Alive now: 842
- Gold now: 263
- HTTP: 212 alive / 31 gold
- HTTPS: 169 alive / 3 gold
- SOCKS4: 222 alive / 119 gold
- SOCKS5: 239 alive / 110 gold

## Historical pool

- Discovered: 99160
- Ever alive: 12113
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
