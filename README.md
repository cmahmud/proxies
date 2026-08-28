# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 399
- HTTP: 93 alive / 69 gold
- HTTPS: 72 alive / 15 gold
- SOCKS4: 161 alive / 154 gold
- SOCKS5: 166 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43139
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
