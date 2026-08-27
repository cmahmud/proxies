# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 413
- HTTP: 94 alive / 71 gold
- HTTPS: 123 alive / 18 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41917
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
