# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 400
- HTTP: 75 alive / 61 gold
- HTTPS: 43 alive / 18 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 176 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42803
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
