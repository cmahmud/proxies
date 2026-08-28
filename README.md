# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 395
- HTTP: 72 alive / 57 gold
- HTTPS: 44 alive / 16 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 173 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42811
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
