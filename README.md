# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 409
- HTTP: 134 alive / 75 gold
- HTTPS: 155 alive / 22 gold
- SOCKS4: 162 alive / 151 gold
- SOCKS5: 184 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40218
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
