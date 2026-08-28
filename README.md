# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 398
- HTTP: 85 alive / 56 gold
- HTTPS: 41 alive / 15 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42848
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
