# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 378
- HTTP: 99 alive / 56 gold
- HTTPS: 37 alive / 9 gold
- SOCKS4: 169 alive / 151 gold
- SOCKS5: 189 alive / 162 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33433
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
