# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 378
- HTTP: 96 alive / 56 gold
- HTTPS: 54 alive / 22 gold
- SOCKS4: 157 alive / 150 gold
- SOCKS5: 163 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43645
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
