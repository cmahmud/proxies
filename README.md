# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 395
- HTTP: 81 alive / 65 gold
- HTTPS: 76 alive / 18 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 165 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43361
- Ever gold: 1370

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
