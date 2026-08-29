# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 425
- HTTP: 119 alive / 82 gold
- HTTPS: 75 alive / 27 gold
- SOCKS4: 161 alive / 155 gold
- SOCKS5: 176 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43656
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
