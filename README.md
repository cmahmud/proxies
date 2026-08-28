# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 413
- HTTP: 111 alive / 69 gold
- HTTPS: 103 alive / 17 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42543
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
