# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 413
- HTTP: 111 alive / 74 gold
- HTTPS: 105 alive / 21 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 182 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41842
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
