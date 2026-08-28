# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 392
- HTTP: 91 alive / 72 gold
- HTTPS: 86 alive / 11 gold
- SOCKS4: 162 alive / 152 gold
- SOCKS5: 174 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43177
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
