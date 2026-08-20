# SyndProxy private pool

## Current pool

- Alive now: 1701
- Gold now: 637
- HTTP: 716 alive / 237 gold
- HTTPS: 523 alive / 135 gold
- SOCKS4: 184 alive / 103 gold
- SOCKS5: 278 alive / 162 gold

## Historical pool

- Discovered: 143421
- Ever alive: 24683
- Ever gold: 1031

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
