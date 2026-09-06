# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 395
- HTTP: 104 alive / 79 gold
- HTTPS: 47 alive / 15 gold
- SOCKS4: 170 alive / 151 gold
- SOCKS5: 178 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48200
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
