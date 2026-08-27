# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 394
- HTTP: 79 alive / 49 gold
- HTTPS: 51 alive / 15 gold
- SOCKS4: 174 alive / 165 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41617
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
