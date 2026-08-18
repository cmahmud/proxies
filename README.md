# SyndProxy private pool

## Current pool

- Alive now: 713
- Gold now: 244
- HTTP: 201 alive / 23 gold
- HTTPS: 115 alive / 2 gold
- SOCKS4: 189 alive / 110 gold
- SOCKS5: 208 alive / 109 gold

## Historical pool

- Discovered: 99103
- Ever alive: 11491
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
