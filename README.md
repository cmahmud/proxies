# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 416
- HTTP: 85 alive / 61 gold
- HTTPS: 66 alive / 19 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36190
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
