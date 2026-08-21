# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 407
- HTTP: 277 alive / 95 gold
- HTTPS: 202 alive / 19 gold
- SOCKS4: 224 alive / 150 gold
- SOCKS5: 242 alive / 143 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29274
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
