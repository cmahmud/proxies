# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 382
- HTTP: 129 alive / 67 gold
- HTTPS: 183 alive / 20 gold
- SOCKS4: 159 alive / 145 gold
- SOCKS5: 180 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39859
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
