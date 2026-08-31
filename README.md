# SyndProxy validated proxy pool

## Current pool

- Alive now: 686
- Gold now: 457
- HTTP: 156 alive / 89 gold
- HTTPS: 117 alive / 33 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 238 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45321
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
