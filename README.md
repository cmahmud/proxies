# SyndProxy private pool

## Current pool

- Alive now: 1436
- Gold now: 625
- HTTP: 529 alive / 208 gold
- HTTPS: 447 alive / 115 gold
- SOCKS4: 222 alive / 144 gold
- SOCKS5: 238 alive / 158 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24037
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
