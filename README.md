# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 419
- HTTP: 97 alive / 74 gold
- HTTPS: 115 alive / 21 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42009
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
