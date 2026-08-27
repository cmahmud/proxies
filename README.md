# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 396
- HTTP: 69 alive / 52 gold
- HTTPS: 48 alive / 18 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41683
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
