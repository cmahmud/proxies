# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 381
- HTTP: 95 alive / 53 gold
- HTTPS: 35 alive / 12 gold
- SOCKS4: 170 alive / 154 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 179377
- Ever alive: 33468
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
