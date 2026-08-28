# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 436
- HTTP: 117 alive / 84 gold
- HTTPS: 134 alive / 21 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42277
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
