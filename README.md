# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 439
- HTTP: 124 alive / 88 gold
- HTTPS: 60 alive / 26 gold
- SOCKS4: 162 alive / 156 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43662
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
