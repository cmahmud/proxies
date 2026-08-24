# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 388
- HTTP: 108 alive / 59 gold
- HTTPS: 52 alive / 10 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 177586
- Ever alive: 33321
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
