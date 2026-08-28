# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 376
- HTTP: 92 alive / 59 gold
- HTTPS: 88 alive / 11 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 179 alive / 147 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43047
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
