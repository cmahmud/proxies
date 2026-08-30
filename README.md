# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 446
- HTTP: 121 alive / 86 gold
- HTTPS: 53 alive / 28 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 179 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43678
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
