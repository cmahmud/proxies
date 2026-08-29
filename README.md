# SyndProxy validated proxy pool

## Current pool

- Alive now: 359
- Gold now: 336
- HTTP: 41 alive / 26 gold
- HTTPS: 1 alive / 0 gold
- SOCKS4: 155 alive / 155 gold
- SOCKS5: 162 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43618
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
