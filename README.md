# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 411
- HTTP: 104 alive / 67 gold
- HTTPS: 110 alive / 17 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42546
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
