# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 402
- HTTP: 117 alive / 75 gold
- HTTPS: 146 alive / 23 gold
- SOCKS4: 167 alive / 149 gold
- SOCKS5: 186 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40156
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
