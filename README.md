# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 384
- HTTP: 106 alive / 60 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 179 alive / 157 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33438
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
