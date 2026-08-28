# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 400
- HTTP: 104 alive / 69 gold
- HTTPS: 82 alive / 14 gold
- SOCKS4: 162 alive / 153 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43190
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
