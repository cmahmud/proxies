# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 442
- HTTP: 316 alive / 92 gold
- HTTPS: 262 alive / 24 gold
- SOCKS4: 223 alive / 157 gold
- SOCKS5: 233 alive / 169 gold

## Historical pool

- Discovered: 144729
- Ever alive: 24914
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
