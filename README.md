# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 409
- HTTP: 90 alive / 59 gold
- HTTPS: 62 alive / 24 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45516
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
