# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 385
- HTTP: 87 alive / 53 gold
- HTTPS: 55 alive / 14 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 185 alive / 161 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33484
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
