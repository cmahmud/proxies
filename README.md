# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 394
- HTTP: 81 alive / 52 gold
- HTTPS: 49 alive / 16 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41683
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
