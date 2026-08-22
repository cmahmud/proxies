# SyndProxy private pool

## Current pool

- Alive now: 754
- Gold now: 414
- HTTP: 190 alive / 86 gold
- HTTPS: 148 alive / 31 gold
- SOCKS4: 190 alive / 138 gold
- SOCKS5: 226 alive / 159 gold

## Historical pool

- Discovered: 162438
- Ever alive: 31419
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
