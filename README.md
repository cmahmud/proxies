# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 402
- HTTP: 95 alive / 74 gold
- HTTPS: 78 alive / 13 gold
- SOCKS4: 161 alive / 155 gold
- SOCKS5: 171 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43076
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
