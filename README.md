# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 400
- HTTP: 100 alive / 62 gold
- HTTPS: 39 alive / 16 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38979
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
