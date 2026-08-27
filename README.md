# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 419
- HTTP: 101 alive / 72 gold
- HTTPS: 114 alive / 24 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 180 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41809
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
