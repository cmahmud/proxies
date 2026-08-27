# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 405
- HTTP: 120 alive / 60 gold
- HTTPS: 174 alive / 11 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40813
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
