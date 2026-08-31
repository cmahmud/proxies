# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 474
- HTTP: 144 alive / 98 gold
- HTTPS: 120 alive / 40 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 204 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45052
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
