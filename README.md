# SyndProxy validated proxy pool

## Current pool

- Alive now: 353
- Gold now: 262
- HTTP: 37 alive / 23 gold
- HTTPS: 3 alive / 0 gold
- SOCKS4: 153 alive / 127 gold
- SOCKS5: 160 alive / 112 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43618
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
