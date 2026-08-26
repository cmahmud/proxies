# SyndProxy validated proxy pool

## Current pool

- Alive now: 667
- Gold now: 417
- HTTP: 152 alive / 79 gold
- HTTPS: 165 alive / 24 gold
- SOCKS4: 166 alive / 154 gold
- SOCKS5: 184 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40316
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
