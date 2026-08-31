# SyndProxy validated proxy pool

## Current pool

- Alive now: 668
- Gold now: 467
- HTTP: 161 alive / 95 gold
- HTTPS: 121 alive / 35 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 204 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45250
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
