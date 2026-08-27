# SyndProxy validated proxy pool

## Current pool

- Alive now: 682
- Gold now: 413
- HTTP: 131 alive / 66 gold
- HTTPS: 184 alive / 14 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40824
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
