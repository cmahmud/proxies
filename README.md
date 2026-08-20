# SyndProxy private pool

## Current pool

- Alive now: 698
- Gold now: 362
- HTTP: 187 alive / 70 gold
- HTTPS: 136 alive / 18 gold
- SOCKS4: 182 alive / 135 gold
- SOCKS5: 193 alive / 139 gold

## Historical pool

- Discovered: 149498
- Ever alive: 26689
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
