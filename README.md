# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 402
- HTTP: 94 alive / 58 gold
- HTTPS: 93 alive / 19 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42693
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
