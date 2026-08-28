# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 395
- HTTP: 85 alive / 64 gold
- HTTPS: 97 alive / 10 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43052
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
