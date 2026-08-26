# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 379
- HTTP: 123 alive / 66 gold
- HTTPS: 173 alive / 17 gold
- SOCKS4: 161 alive / 147 gold
- SOCKS5: 173 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40095
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
