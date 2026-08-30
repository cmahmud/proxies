# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 443
- HTTP: 109 alive / 81 gold
- HTTPS: 62 alive / 30 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 198 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44569
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
