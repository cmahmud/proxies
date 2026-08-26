# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 394
- HTTP: 116 alive / 73 gold
- HTTPS: 156 alive / 22 gold
- SOCKS4: 161 alive / 147 gold
- SOCKS5: 172 alive / 152 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40129
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
