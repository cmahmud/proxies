# SyndProxy validated proxy pool

## Current pool

- Alive now: 662
- Gold now: 416
- HTTP: 156 alive / 79 gold
- HTTPS: 156 alive / 22 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 185 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40326
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
