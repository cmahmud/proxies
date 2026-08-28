# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 402
- HTTP: 103 alive / 79 gold
- HTTPS: 75 alive / 13 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 170 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43120
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
