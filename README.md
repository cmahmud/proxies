# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 378
- HTTP: 107 alive / 54 gold
- HTTPS: 37 alive / 8 gold
- SOCKS4: 167 alive / 153 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33434
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
