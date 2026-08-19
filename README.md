# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 600
- HTTP: 439 alive / 185 gold
- HTTPS: 263 alive / 113 gold
- SOCKS4: 230 alive / 147 gold
- SOCKS5: 224 alive / 155 gold

## Historical pool

- Discovered: 124855
- Ever alive: 19436
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
