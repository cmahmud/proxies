# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 424
- HTTP: 100 alive / 74 gold
- HTTPS: 78 alive / 27 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 171 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41771
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
