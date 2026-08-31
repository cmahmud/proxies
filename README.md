# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 474
- HTTP: 142 alive / 97 gold
- HTTPS: 118 alive / 40 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 202 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45053
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
