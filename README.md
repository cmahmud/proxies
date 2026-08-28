# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 395
- HTTP: 80 alive / 55 gold
- HTTPS: 56 alive / 19 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 194 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42793
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
