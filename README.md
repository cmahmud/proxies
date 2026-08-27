# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 414
- HTTP: 96 alive / 72 gold
- HTTPS: 117 alive / 21 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41972
- Ever gold: 1346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
