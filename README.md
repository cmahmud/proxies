# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 424
- HTTP: 124 alive / 81 gold
- HTTPS: 65 alive / 28 gold
- SOCKS4: 156 alive / 152 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43696
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
