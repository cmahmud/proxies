# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 539
- HTTP: 439 alive / 181 gold
- HTTPS: 255 alive / 110 gold
- SOCKS4: 184 alive / 116 gold
- SOCKS5: 186 alive / 132 gold

## Historical pool

- Discovered: 124851
- Ever alive: 19410
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
