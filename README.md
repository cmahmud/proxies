# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 413
- HTTP: 96 alive / 63 gold
- HTTPS: 87 alive / 23 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42720
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
