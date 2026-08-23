# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 378
- HTTP: 88 alive / 60 gold
- HTTPS: 32 alive / 8 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 180 alive / 154 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33093
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
