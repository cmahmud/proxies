# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 401
- HTTP: 123 alive / 73 gold
- HTTPS: 159 alive / 24 gold
- SOCKS4: 167 alive / 149 gold
- SOCKS5: 185 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40144
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
