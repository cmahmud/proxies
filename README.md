# SyndProxy validated proxy pool

## Current pool

- Alive now: 405
- Gold now: 318
- HTTP: 77 alive / 52 gold
- HTTPS: 33 alive / 12 gold
- SOCKS4: 150 alive / 133 gold
- SOCKS5: 145 alive / 121 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48333
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
