# SyndProxy private pool

## Current pool

- Alive now: 818
- Gold now: 398
- HTTP: 208 alive / 100 gold
- HTTPS: 200 alive / 24 gold
- SOCKS4: 195 alive / 127 gold
- SOCKS5: 215 alive / 147 gold

## Historical pool

- Discovered: 162001
- Ever alive: 31371
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
