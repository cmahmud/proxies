# SyndProxy validated proxy pool

## Current pool

- Alive now: 419
- Gold now: 307
- HTTP: 56 alive / 33 gold
- HTTPS: 28 alive / 5 gold
- SOCKS4: 160 alive / 142 gold
- SOCKS5: 175 alive / 127 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43587
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
