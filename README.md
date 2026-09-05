# SyndProxy validated proxy pool

## Current pool

- Alive now: 370
- Gold now: 298
- HTTP: 107 alive / 80 gold
- HTTPS: 33 alive / 19 gold
- SOCKS4: 74 alive / 65 gold
- SOCKS5: 156 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47853
- Ever gold: 1499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
