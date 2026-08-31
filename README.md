# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 438
- HTTP: 114 alive / 77 gold
- HTTPS: 63 alive / 27 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45550
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
