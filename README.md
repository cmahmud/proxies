# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 395
- HTTP: 75 alive / 58 gold
- HTTPS: 67 alive / 16 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 175 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42882
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
