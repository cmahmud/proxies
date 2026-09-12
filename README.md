# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 423
- HTTP: 107 alive / 79 gold
- HTTPS: 42 alive / 21 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49469
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
