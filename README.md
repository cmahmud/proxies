# SyndProxy private pool

## Current pool

- Alive now: 1143
- Gold now: 606
- HTTP: 432 alive / 189 gold
- HTTPS: 265 alive / 113 gold
- SOCKS4: 226 alive / 146 gold
- SOCKS5: 220 alive / 158 gold

## Historical pool

- Discovered: 124855
- Ever alive: 19426
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
