# SyndProxy private pool

## Current pool

- Alive now: 592
- Gold now: 216
- HTTP: 142 alive / 21 gold
- HTTPS: 78 alive / 9 gold
- SOCKS4: 164 alive / 100 gold
- SOCKS5: 208 alive / 86 gold

## Historical pool

- Discovered: 91520
- Ever alive: 8004
- Ever gold: 346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
