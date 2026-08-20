# SyndProxy private pool

## Current pool

- Alive now: 1425
- Gold now: 569
- HTTP: 551 alive / 190 gold
- HTTPS: 404 alive / 89 gold
- SOCKS4: 207 alive / 130 gold
- SOCKS5: 263 alive / 160 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23094
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
