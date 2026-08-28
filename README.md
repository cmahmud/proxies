# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 419
- HTTP: 99 alive / 74 gold
- HTTPS: 111 alive / 21 gold
- SOCKS4: 182 alive / 156 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42507
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
