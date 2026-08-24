# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 385
- HTTP: 148 alive / 55 gold
- HTTPS: 46 alive / 14 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 179 alive / 159 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33500
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
