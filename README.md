# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 434
- HTTP: 116 alive / 82 gold
- HTTPS: 60 alive / 31 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43656
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
