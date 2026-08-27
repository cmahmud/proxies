# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 421
- HTTP: 103 alive / 77 gold
- HTTPS: 114 alive / 17 gold
- SOCKS4: 181 alive / 159 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42116
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
