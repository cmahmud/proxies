# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 474
- HTTP: 132 alive / 102 gold
- HTTPS: 57 alive / 35 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49358
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
