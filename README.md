# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 410
- HTTP: 99 alive / 70 gold
- HTTPS: 98 alive / 22 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 175 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41799
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
