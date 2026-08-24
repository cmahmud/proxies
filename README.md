# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 391
- HTTP: 128 alive / 62 gold
- HTTPS: 30 alive / 9 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33435
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
