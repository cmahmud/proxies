# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 405
- HTTP: 87 alive / 62 gold
- HTTPS: 82 alive / 19 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42697
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
