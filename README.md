# SyndProxy private pool

## Current pool

- Alive now: 1330
- Gold now: 548
- HTTP: 492 alive / 178 gold
- HTTPS: 357 alive / 81 gold
- SOCKS4: 241 alive / 131 gold
- SOCKS5: 240 alive / 158 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22977
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
