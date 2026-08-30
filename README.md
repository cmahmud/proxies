# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 456
- HTTP: 121 alive / 85 gold
- HTTPS: 118 alive / 42 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 204 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44771
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
