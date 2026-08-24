# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 382
- HTTP: 113 alive / 55 gold
- HTTPS: 34 alive / 10 gold
- SOCKS4: 164 alive / 157 gold
- SOCKS5: 180 alive / 160 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33458
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
