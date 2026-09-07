# SyndProxy validated proxy pool

## Current pool

- Alive now: 422
- Gold now: 313
- HTTP: 82 alive / 57 gold
- HTTPS: 26 alive / 10 gold
- SOCKS4: 145 alive / 121 gold
- SOCKS5: 169 alive / 125 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48404
- Ever gold: 1532

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
