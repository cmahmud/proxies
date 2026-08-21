# SyndProxy private pool

## Current pool

- Alive now: 731
- Gold now: 399
- HTTP: 198 alive / 86 gold
- HTTPS: 122 alive / 19 gold
- SOCKS4: 210 alive / 142 gold
- SOCKS5: 201 alive / 152 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27740
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
