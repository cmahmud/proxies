# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 442
- HTTP: 128 alive / 81 gold
- HTTPS: 55 alive / 27 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43688
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
