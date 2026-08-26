# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 388
- HTTP: 121 alive / 68 gold
- HTTPS: 165 alive / 24 gold
- SOCKS4: 157 alive / 146 gold
- SOCKS5: 178 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39831
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
