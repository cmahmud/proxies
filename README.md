# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 402
- HTTP: 83 alive / 59 gold
- HTTPS: 79 alive / 17 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42917
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
