# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 382
- HTTP: 102 alive / 52 gold
- HTTPS: 37 alive / 11 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33425
- Ever gold: 1237

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
