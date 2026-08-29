# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 400
- HTTP: 97 alive / 70 gold
- HTTPS: 92 alive / 17 gold
- SOCKS4: 165 alive / 152 gold
- SOCKS5: 171 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43297
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
