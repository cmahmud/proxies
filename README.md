# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 364
- HTTP: 95 alive / 52 gold
- HTTPS: 45 alive / 18 gold
- SOCKS4: 158 alive / 148 gold
- SOCKS5: 165 alive / 146 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43642
- Ever gold: 1373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
