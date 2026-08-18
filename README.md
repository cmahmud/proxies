# SyndProxy private pool

## Current pool

- Alive now: 522
- Gold now: 137
- HTTP: 143 alive / 34 gold
- HTTPS: 87 alive / 10 gold
- SOCKS4: 149 alive / 54 gold
- SOCKS5: 143 alive / 39 gold

## Historical pool

- Discovered: 82958
- Ever alive: 5060
- Ever gold: 259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
