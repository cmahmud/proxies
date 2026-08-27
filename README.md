# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 416
- HTTP: 102 alive / 75 gold
- HTTPS: 98 alive / 21 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 178 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41835
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
