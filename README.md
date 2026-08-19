# SyndProxy private pool

## Current pool

- Alive now: 1099
- Gold now: 522
- HTTP: 443 alive / 178 gold
- HTTPS: 255 alive / 100 gold
- SOCKS4: 205 alive / 114 gold
- SOCKS5: 196 alive / 130 gold

## Historical pool

- Discovered: 124851
- Ever alive: 19404
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
