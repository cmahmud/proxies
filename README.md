# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 387
- HTTP: 96 alive / 61 gold
- HTTPS: 42 alive / 10 gold
- SOCKS4: 160 alive / 156 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33438
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
