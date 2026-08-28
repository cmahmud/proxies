# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 394
- HTTP: 80 alive / 54 gold
- HTTPS: 41 alive / 14 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42854
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
