# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 419
- HTTP: 106 alive / 75 gold
- HTTPS: 117 alive / 20 gold
- SOCKS4: 183 alive / 157 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42107
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
