# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 407
- HTTP: 82 alive / 59 gold
- HTTPS: 65 alive / 20 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 195 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42728
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
