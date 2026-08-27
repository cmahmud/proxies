# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 411
- HTTP: 113 alive / 64 gold
- HTTPS: 140 alive / 19 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41359
- Ever gold: 1326

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
