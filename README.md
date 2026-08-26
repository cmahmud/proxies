# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 395
- HTTP: 180 alive / 69 gold
- HTTPS: 100 alive / 22 gold
- SOCKS4: 166 alive / 150 gold
- SOCKS5: 207 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39464
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
