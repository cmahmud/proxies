# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 379
- HTTP: 88 alive / 60 gold
- HTTPS: 51 alive / 20 gold
- SOCKS4: 151 alive / 145 gold
- SOCKS5: 170 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38908
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
