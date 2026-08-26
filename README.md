# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 421
- HTTP: 146 alive / 81 gold
- HTTPS: 163 alive / 25 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 186 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40297
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
