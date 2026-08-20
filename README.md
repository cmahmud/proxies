# SyndProxy private pool

## Current pool

- Alive now: 752
- Gold now: 378
- HTTP: 200 alive / 68 gold
- HTTPS: 160 alive / 22 gold
- SOCKS4: 201 alive / 148 gold
- SOCKS5: 191 alive / 140 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26184
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
