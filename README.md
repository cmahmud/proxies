# SyndProxy private pool

## Current pool

- Alive now: 755
- Gold now: 401
- HTTP: 210 alive / 89 gold
- HTTPS: 123 alive / 20 gold
- SOCKS4: 220 alive / 142 gold
- SOCKS5: 202 alive / 150 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27743
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
