# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 383
- HTTP: 120 alive / 57 gold
- HTTPS: 39 alive / 9 gold
- SOCKS4: 166 alive / 157 gold
- SOCKS5: 183 alive / 160 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33458
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
