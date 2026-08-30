# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 448
- HTTP: 122 alive / 83 gold
- HTTPS: 139 alive / 33 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44704
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
