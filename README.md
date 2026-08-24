# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 385
- HTTP: 96 alive / 56 gold
- HTTPS: 38 alive / 10 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 179377
- Ever alive: 33462
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
