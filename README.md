# SyndProxy validated proxy pool

## Current pool

- Alive now: 677
- Gold now: 481
- HTTP: 151 alive / 102 gold
- HTTPS: 129 alive / 40 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 224 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45257
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
