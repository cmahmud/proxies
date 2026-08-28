# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 431
- HTTP: 108 alive / 80 gold
- HTTPS: 140 alive / 22 gold
- SOCKS4: 184 alive / 160 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42352
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
