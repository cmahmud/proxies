# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 402
- HTTP: 114 alive / 66 gold
- HTTPS: 156 alive / 12 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40947
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
