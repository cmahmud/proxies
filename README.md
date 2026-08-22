# SyndProxy private pool

## Current pool

- Alive now: 808
- Gold now: 347
- HTTP: 268 alive / 85 gold
- HTTPS: 146 alive / 22 gold
- SOCKS4: 185 alive / 114 gold
- SOCKS5: 209 alive / 126 gold

## Historical pool

- Discovered: 167412
- Ever alive: 32583
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
