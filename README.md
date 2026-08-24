# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 378
- HTTP: 104 alive / 53 gold
- HTTPS: 39 alive / 8 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 189 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33434
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
