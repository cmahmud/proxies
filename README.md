# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 378
- HTTP: 68 alive / 52 gold
- HTTPS: 53 alive / 6 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 171 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43520
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
