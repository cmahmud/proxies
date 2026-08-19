# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 537
- HTTP: 372 alive / 165 gold
- HTTPS: 252 alive / 88 gold
- SOCKS4: 193 alive / 140 gold
- SOCKS5: 223 alive / 144 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18650
- Ever gold: 725

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
