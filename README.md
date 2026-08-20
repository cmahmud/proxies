# SyndProxy private pool

## Current pool

- Alive now: 755
- Gold now: 389
- HTTP: 195 alive / 82 gold
- HTTPS: 149 alive / 21 gold
- SOCKS4: 218 alive / 145 gold
- SOCKS5: 193 alive / 141 gold

## Historical pool

- Discovered: 149513
- Ever alive: 26920
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
