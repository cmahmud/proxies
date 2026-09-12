# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 461
- HTTP: 134 alive / 98 gold
- HTTPS: 65 alive / 33 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49329
- Ever gold: 1577

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
