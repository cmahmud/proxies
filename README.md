# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 424
- HTTP: 98 alive / 74 gold
- HTTPS: 52 alive / 22 gold
- SOCKS4: 184 alive / 165 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49029
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
