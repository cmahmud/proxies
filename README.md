# SyndProxy private pool

## Current pool

- Alive now: 806
- Gold now: 382
- HTTP: 226 alive / 82 gold
- HTTPS: 166 alive / 22 gold
- SOCKS4: 206 alive / 144 gold
- SOCKS5: 208 alive / 134 gold

## Historical pool

- Discovered: 163332
- Ever alive: 31878
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
