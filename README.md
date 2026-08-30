# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 484
- HTTP: 156 alive / 100 gold
- HTTPS: 129 alive / 45 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 196 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44963
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
