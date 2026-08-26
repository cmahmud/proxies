# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 398
- HTTP: 102 alive / 58 gold
- HTTPS: 47 alive / 16 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38969
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
