# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 419
- HTTP: 115 alive / 75 gold
- HTTPS: 168 alive / 21 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40560
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
