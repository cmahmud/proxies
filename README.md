# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 382
- HTTP: 103 alive / 58 gold
- HTTPS: 44 alive / 11 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 179 alive / 158 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33436
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
