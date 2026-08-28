# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 402
- HTTP: 111 alive / 77 gold
- HTTPS: 67 alive / 14 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 169 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43123
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
