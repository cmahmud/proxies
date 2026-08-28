# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 414
- HTTP: 99 alive / 60 gold
- HTTPS: 111 alive / 25 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42994
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
