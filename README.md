# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 398
- HTTP: 100 alive / 61 gold
- HTTPS: 110 alive / 16 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 189 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41426
- Ever gold: 1328

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
