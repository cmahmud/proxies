# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 428
- HTTP: 113 alive / 80 gold
- HTTPS: 145 alive / 21 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42366
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
