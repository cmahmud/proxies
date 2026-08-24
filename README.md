# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 381
- HTTP: 99 alive / 62 gold
- HTTPS: 49 alive / 14 gold
- SOCKS4: 160 alive / 152 gold
- SOCKS5: 169 alive / 153 gold

## Historical pool

- Discovered: 176375
- Ever alive: 33204
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
