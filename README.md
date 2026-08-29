# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 384
- HTTP: 84 alive / 63 gold
- HTTPS: 61 alive / 17 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 167 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43391
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
