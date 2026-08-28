# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 400
- HTTP: 76 alive / 53 gold
- HTTPS: 68 alive / 22 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42773
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
