# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 406
- HTTP: 98 alive / 64 gold
- HTTPS: 105 alive / 17 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41419
- Ever gold: 1328

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
