# SyndProxy private pool

## Current pool

- Alive now: 594
- Gold now: 193
- HTTP: 152 alive / 19 gold
- HTTPS: 77 alive / 9 gold
- SOCKS4: 170 alive / 96 gold
- SOCKS5: 195 alive / 69 gold

## Historical pool

- Discovered: 91520
- Ever alive: 8004
- Ever gold: 346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
