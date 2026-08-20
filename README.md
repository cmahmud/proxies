# SyndProxy private pool

## Current pool

- Alive now: 664
- Gold now: 345
- HTTP: 160 alive / 61 gold
- HTTPS: 139 alive / 18 gold
- SOCKS4: 178 alive / 130 gold
- SOCKS5: 187 alive / 136 gold

## Historical pool

- Discovered: 146875
- Ever alive: 25756
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
