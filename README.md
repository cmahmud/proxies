# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 402
- HTTP: 95 alive / 73 gold
- HTTPS: 71 alive / 15 gold
- SOCKS4: 155 alive / 154 gold
- SOCKS5: 166 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43133
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
