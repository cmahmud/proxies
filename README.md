# SyndProxy private pool

## Current pool

- Alive now: 791
- Gold now: 385
- HTTP: 244 alive / 89 gold
- HTTPS: 141 alive / 21 gold
- SOCKS4: 170 alive / 117 gold
- SOCKS5: 236 alive / 158 gold

## Historical pool

- Discovered: 166329
- Ever alive: 32394
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
