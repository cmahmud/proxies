# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 383
- HTTP: 128 alive / 68 gold
- HTTPS: 172 alive / 20 gold
- SOCKS4: 161 alive / 147 gold
- SOCKS5: 175 alive / 148 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40094
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
