# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 416
- HTTP: 102 alive / 73 gold
- HTTPS: 105 alive / 24 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 173 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41963
- Ever gold: 1346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
