# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 431
- HTTP: 128 alive / 79 gold
- HTTPS: 105 alive / 23 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34044
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
