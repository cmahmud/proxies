# SyndProxy validated proxy pool

## Current pool

- Alive now: 383
- Gold now: 291
- HTTP: 112 alive / 77 gold
- HTTPS: 38 alive / 17 gold
- SOCKS4: 76 alive / 65 gold
- SOCKS5: 157 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47863
- Ever gold: 1499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
