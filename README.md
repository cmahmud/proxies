# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 394
- HTTP: 77 alive / 56 gold
- HTTPS: 77 alive / 14 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 170 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42928
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
