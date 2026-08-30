# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 464
- HTTP: 140 alive / 95 gold
- HTTPS: 110 alive / 39 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44836
- Ever gold: 1415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
