# SyndProxy validated proxy pool

## Current pool

- Alive now: 372
- Gold now: 298
- HTTP: 108 alive / 80 gold
- HTTPS: 33 alive / 19 gold
- SOCKS4: 75 alive / 66 gold
- SOCKS5: 156 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47855
- Ever gold: 1499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
