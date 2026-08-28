# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 392
- HTTP: 68 alive / 52 gold
- HTTPS: 60 alive / 17 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42764
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
