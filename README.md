# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 435
- HTTP: 116 alive / 84 gold
- HTTPS: 67 alive / 30 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43656
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
