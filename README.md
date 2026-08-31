# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 483
- HTTP: 149 alive / 105 gold
- HTTPS: 136 alive / 39 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 195 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45227
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
