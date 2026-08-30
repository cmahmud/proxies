# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 451
- HTTP: 127 alive / 90 gold
- HTTPS: 57 alive / 31 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43676
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
