# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 406
- HTTP: 102 alive / 62 gold
- HTTPS: 130 alive / 16 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41329
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
