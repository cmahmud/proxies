# SyndProxy validated proxy pool

## Current pool

- Alive now: 429
- Gold now: 362
- HTTP: 63 alive / 47 gold
- HTTPS: 31 alive / 6 gold
- SOCKS4: 163 alive / 157 gold
- SOCKS5: 172 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43541
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
