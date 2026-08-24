# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 378
- HTTP: 127 alive / 55 gold
- HTTPS: 46 alive / 11 gold
- SOCKS4: 169 alive / 155 gold
- SOCKS5: 174 alive / 157 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33442
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
