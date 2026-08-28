# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 405
- HTTP: 101 alive / 72 gold
- HTTPS: 81 alive / 15 gold
- SOCKS4: 158 alive / 154 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43194
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
