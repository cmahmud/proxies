# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 430
- HTTP: 98 alive / 72 gold
- HTTPS: 54 alive / 28 gold
- SOCKS4: 177 alive / 167 gold
- SOCKS5: 184 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49051
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
