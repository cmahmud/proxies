# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 474
- HTTP: 137 alive / 98 gold
- HTTPS: 130 alive / 41 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 196 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45054
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
