# SyndProxy validated proxy pool

## Current pool

- Alive now: 358
- Gold now: 318
- HTTP: 53 alive / 30 gold
- HTTPS: 10 alive / 0 gold
- SOCKS4: 147 alive / 145 gold
- SOCKS5: 148 alive / 143 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43631
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
