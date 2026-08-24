# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 384
- HTTP: 98 alive / 54 gold
- HTTPS: 39 alive / 12 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 179377
- Ever alive: 33469
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
