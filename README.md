# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 390
- HTTP: 85 alive / 53 gold
- HTTPS: 72 alive / 16 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 173 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42898
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
