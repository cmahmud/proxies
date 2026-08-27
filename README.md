# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 413
- HTTP: 92 alive / 70 gold
- HTTPS: 84 alive / 21 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41753
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
