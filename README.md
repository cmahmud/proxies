# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 405
- HTTP: 112 alive / 67 gold
- HTTPS: 157 alive / 11 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40943
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
