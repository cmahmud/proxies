# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 424
- HTTP: 86 alive / 68 gold
- HTTPS: 63 alive / 25 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47070
- Ever gold: 1464

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
