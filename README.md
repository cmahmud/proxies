# SyndProxy private pool

## Current pool

- Alive now: 736
- Gold now: 363
- HTTP: 204 alive / 66 gold
- HTTPS: 154 alive / 17 gold
- SOCKS4: 182 alive / 140 gold
- SOCKS5: 196 alive / 140 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25655
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
