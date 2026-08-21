# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 421
- HTTP: 179 alive / 80 gold
- HTTPS: 152 alive / 24 gold
- SOCKS4: 219 alive / 148 gold
- SOCKS5: 244 alive / 169 gold

## Historical pool

- Discovered: 155791
- Ever alive: 29332
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
