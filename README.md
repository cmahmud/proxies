# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 417
- HTTP: 86 alive / 60 gold
- HTTPS: 81 alive / 23 gold
- SOCKS4: 180 alive / 167 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41540
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
