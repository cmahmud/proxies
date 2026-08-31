# SyndProxy validated proxy pool

## Current pool

- Alive now: 736
- Gold now: 476
- HTTP: 195 alive / 99 gold
- HTTPS: 129 alive / 39 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 235 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45295
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
