# SyndProxy validated proxy pool

## Current pool

- Alive now: 683
- Gold now: 478
- HTTP: 154 alive / 99 gold
- HTTPS: 131 alive / 38 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 228 alive / 180 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45260
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
