# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 422
- HTTP: 116 alive / 79 gold
- HTTPS: 124 alive / 21 gold
- SOCKS4: 180 alive / 159 gold
- SOCKS5: 196 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42387
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
