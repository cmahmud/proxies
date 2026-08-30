# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 461
- HTTP: 137 alive / 94 gold
- HTTPS: 117 alive / 38 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 203 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44834
- Ever gold: 1415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
