# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 445
- HTTP: 120 alive / 88 gold
- HTTPS: 53 alive / 28 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 178 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43677
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
