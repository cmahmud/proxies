# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 429
- HTTP: 106 alive / 80 gold
- HTTPS: 47 alive / 21 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44521
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
