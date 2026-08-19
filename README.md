# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 386
- HTTP: 359 alive / 94 gold
- HTTPS: 231 alive / 15 gold
- SOCKS4: 230 alive / 138 gold
- SOCKS5: 293 alive / 139 gold

## Historical pool

- Discovered: 131826
- Ever alive: 20990
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
