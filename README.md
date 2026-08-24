# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 403
- HTTP: 143 alive / 71 gold
- HTTPS: 74 alive / 13 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 200 alive / 163 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33305
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
