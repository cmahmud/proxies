# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 440
- HTTP: 136 alive / 87 gold
- HTTPS: 53 alive / 23 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43665
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
