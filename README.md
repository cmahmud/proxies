# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 407
- HTTP: 85 alive / 60 gold
- HTTPS: 55 alive / 21 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41713
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
