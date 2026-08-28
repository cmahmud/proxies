# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 402
- HTTP: 102 alive / 70 gold
- HTTPS: 85 alive / 15 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43192
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
