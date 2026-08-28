# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 398
- HTTP: 88 alive / 57 gold
- HTTPS: 69 alive / 17 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 183 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42736
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
