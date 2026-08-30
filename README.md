# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 429
- HTTP: 96 alive / 73 gold
- HTTPS: 63 alive / 26 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44430
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
