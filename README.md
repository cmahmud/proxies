# SyndProxy validated proxy pool

## Current pool

- Alive now: 667
- Gold now: 395
- HTTP: 141 alive / 75 gold
- HTTPS: 189 alive / 22 gold
- SOCKS4: 166 alive / 146 gold
- SOCKS5: 171 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39946
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
