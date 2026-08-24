# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 399
- HTTP: 151 alive / 68 gold
- HTTPS: 77 alive / 14 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 188 alive / 161 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33305
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
