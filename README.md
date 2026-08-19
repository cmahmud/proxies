# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 480
- HTTP: 348 alive / 145 gold
- HTTPS: 254 alive / 87 gold
- SOCKS4: 208 alive / 118 gold
- SOCKS5: 227 alive / 130 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17572
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
