# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 423
- HTTP: 109 alive / 76 gold
- HTTPS: 121 alive / 18 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42439
- Ever gold: 1356

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
