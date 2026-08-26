# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 398
- HTTP: 98 alive / 60 gold
- HTTPS: 37 alive / 15 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 178 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38970
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
