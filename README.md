# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 404
- HTTP: 74 alive / 57 gold
- HTTPS: 55 alive / 23 gold
- SOCKS4: 163 alive / 160 gold
- SOCKS5: 176 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42789
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
