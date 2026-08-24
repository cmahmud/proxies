# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 390
- HTTP: 123 alive / 61 gold
- HTTPS: 29 alive / 9 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33436
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
