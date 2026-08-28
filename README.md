# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 403
- HTTP: 87 alive / 58 gold
- HTTPS: 88 alive / 22 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42988
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
