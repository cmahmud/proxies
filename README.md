# SyndProxy validated proxy pool

## Current pool

- Alive now: 732
- Gold now: 472
- HTTP: 189 alive / 98 gold
- HTTPS: 130 alive / 35 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 234 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45295
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
