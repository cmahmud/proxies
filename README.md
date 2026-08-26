# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 401
- HTTP: 120 alive / 73 gold
- HTTPS: 159 alive / 18 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 189 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40185
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
