# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 388
- HTTP: 88 alive / 63 gold
- HTTPS: 89 alive / 10 gold
- SOCKS4: 157 alive / 154 gold
- SOCKS5: 178 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43209
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
