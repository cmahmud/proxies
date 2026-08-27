# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 414
- HTTP: 100 alive / 71 gold
- HTTPS: 103 alive / 24 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 178 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41816
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
