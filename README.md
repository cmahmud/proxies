# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 402
- HTTP: 88 alive / 57 gold
- HTTPS: 85 alive / 22 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 178 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42983
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
