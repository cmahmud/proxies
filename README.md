# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 399
- HTTP: 78 alive / 52 gold
- HTTPS: 45 alive / 19 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41683
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
