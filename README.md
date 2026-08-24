# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 378
- HTTP: 93 alive / 48 gold
- HTTPS: 40 alive / 14 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33497
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
