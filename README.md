# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 381
- HTTP: 92 alive / 52 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33429
- Ever gold: 1237

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
