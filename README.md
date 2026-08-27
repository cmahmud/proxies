# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 395
- HTTP: 83 alive / 52 gold
- HTTPS: 58 alive / 14 gold
- SOCKS4: 175 alive / 165 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41623
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
