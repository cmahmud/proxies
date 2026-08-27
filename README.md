# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 402
- HTTP: 93 alive / 60 gold
- HTTPS: 53 alive / 17 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41647
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
