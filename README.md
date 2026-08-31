# SyndProxy validated proxy pool

## Current pool

- Alive now: 701
- Gold now: 459
- HTTP: 167 alive / 87 gold
- HTTPS: 124 alive / 36 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 237 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45324
- Ever gold: 1429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
