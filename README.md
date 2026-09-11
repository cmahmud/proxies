# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 420
- HTTP: 102 alive / 73 gold
- HTTPS: 44 alive / 20 gold
- SOCKS4: 180 alive / 165 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49014
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
