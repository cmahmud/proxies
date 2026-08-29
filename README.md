# SyndProxy validated proxy pool

## Current pool

- Alive now: 356
- Gold now: 332
- HTTP: 36 alive / 24 gold
- HTTPS: 0 alive / 0 gold
- SOCKS4: 157 alive / 153 gold
- SOCKS5: 163 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43613
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
