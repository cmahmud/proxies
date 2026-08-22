# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 347
- HTTP: 267 alive / 75 gold
- HTTPS: 170 alive / 22 gold
- SOCKS4: 192 alive / 118 gold
- SOCKS5: 227 alive / 132 gold

## Historical pool

- Discovered: 167924
- Ever alive: 32594
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
