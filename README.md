# SyndProxy validated proxy pool

## Current pool

- Alive now: 679
- Gold now: 479
- HTTP: 152 alive / 101 gold
- HTTPS: 130 alive / 39 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 225 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45257
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
