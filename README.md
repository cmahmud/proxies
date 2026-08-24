# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 391
- HTTP: 119 alive / 63 gold
- HTTPS: 55 alive / 9 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 185 alive / 160 gold

## Historical pool

- Discovered: 177586
- Ever alive: 33322
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
