# SyndProxy private pool

## Current pool

- Alive now: 733
- Gold now: 399
- HTTP: 198 alive / 87 gold
- HTTPS: 119 alive / 18 gold
- SOCKS4: 216 alive / 142 gold
- SOCKS5: 200 alive / 152 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27737
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
