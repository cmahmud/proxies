# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 395
- HTTP: 73 alive / 58 gold
- HTTPS: 44 alive / 18 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 173 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42804
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
