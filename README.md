# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 400
- HTTP: 93 alive / 62 gold
- HTTPS: 43 alive / 17 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38970
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
