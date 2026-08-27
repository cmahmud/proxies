# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 404
- HTTP: 110 alive / 65 gold
- HTTPS: 178 alive / 16 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40585
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
