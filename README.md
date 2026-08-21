# SyndProxy private pool

## Current pool

- Alive now: 846
- Gold now: 405
- HTTP: 260 alive / 92 gold
- HTTPS: 131 alive / 22 gold
- SOCKS4: 220 alive / 142 gold
- SOCKS5: 235 alive / 149 gold

## Historical pool

- Discovered: 155807
- Ever alive: 29406
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
