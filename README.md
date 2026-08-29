# SyndProxy validated proxy pool

## Current pool

- Alive now: 416
- Gold now: 357
- HTTP: 50 alive / 35 gold
- HTTPS: 36 alive / 6 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 167 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43551
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
