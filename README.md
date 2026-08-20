# SyndProxy private pool

## Current pool

- Alive now: 627
- Gold now: 381
- HTTP: 150 alive / 60 gold
- HTTPS: 72 alive / 13 gold
- SOCKS4: 200 alive / 152 gold
- SOCKS5: 205 alive / 156 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25720
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
