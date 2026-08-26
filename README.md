# SyndProxy validated proxy pool

## Current pool

- Alive now: 667
- Gold now: 394
- HTTP: 147 alive / 71 gold
- HTTPS: 181 alive / 23 gold
- SOCKS4: 161 alive / 147 gold
- SOCKS5: 178 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40046
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
