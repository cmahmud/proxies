# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 381
- HTTP: 96 alive / 54 gold
- HTTPS: 39 alive / 12 gold
- SOCKS4: 171 alive / 153 gold
- SOCKS5: 180 alive / 162 gold

## Historical pool

- Discovered: 179377
- Ever alive: 33467
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
