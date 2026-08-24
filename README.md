# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 391
- HTTP: 127 alive / 62 gold
- HTTPS: 27 alive / 9 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 193 alive / 165 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33435
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
