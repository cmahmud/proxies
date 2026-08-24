# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 383
- HTTP: 108 alive / 59 gold
- HTTPS: 41 alive / 11 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 179 alive / 158 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33436
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
