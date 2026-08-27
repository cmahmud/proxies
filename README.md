# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 411
- HTTP: 106 alive / 62 gold
- HTTPS: 159 alive / 18 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40784
- Ever gold: 1312

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
