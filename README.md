# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 396
- HTTP: 94 alive / 60 gold
- HTTPS: 61 alive / 17 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 184 alive / 161 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38707
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
