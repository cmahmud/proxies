# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 474
- HTTP: 139 alive / 98 gold
- HTTPS: 112 alive / 38 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 203 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45114
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
