# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 383
- HTTP: 100 alive / 60 gold
- HTTPS: 52 alive / 11 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 178 alive / 157 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33437
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
