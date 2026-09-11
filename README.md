# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 422
- HTTP: 104 alive / 73 gold
- HTTPS: 39 alive / 19 gold
- SOCKS4: 173 alive / 165 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49006
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
