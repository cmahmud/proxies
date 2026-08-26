# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 407
- HTTP: 133 alive / 74 gold
- HTTPS: 152 alive / 22 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 185 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40215
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
