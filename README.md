# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 378
- HTTP: 95 alive / 65 gold
- HTTPS: 33 alive / 13 gold
- SOCKS4: 177 alive / 150 gold
- SOCKS5: 169 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48167
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
