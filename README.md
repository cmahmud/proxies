# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 461
- HTTP: 133 alive / 98 gold
- HTTPS: 61 alive / 34 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49329
- Ever gold: 1577

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
