# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 395
- HTTP: 107 alive / 68 gold
- HTTPS: 93 alive / 14 gold
- SOCKS4: 161 alive / 152 gold
- SOCKS5: 177 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43187
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
