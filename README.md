# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 437
- HTTP: 122 alive / 76 gold
- HTTPS: 95 alive / 27 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 202 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45461
- Ever gold: 1433

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
