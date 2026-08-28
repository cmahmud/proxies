# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 390
- HTTP: 76 alive / 56 gold
- HTTPS: 60 alive / 12 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 170 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42900
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
