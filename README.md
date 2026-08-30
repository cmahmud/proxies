# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 418
- HTTP: 125 alive / 81 gold
- HTTPS: 56 alive / 28 gold
- SOCKS4: 164 alive / 150 gold
- SOCKS5: 168 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43698
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
