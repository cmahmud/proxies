# SyndProxy private pool

## Current pool

- Alive now: 909
- Gold now: 397
- HTTP: 290 alive / 96 gold
- HTTPS: 177 alive / 30 gold
- SOCKS4: 227 alive / 141 gold
- SOCKS5: 215 alive / 130 gold

## Historical pool

- Discovered: 163255
- Ever alive: 31770
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
