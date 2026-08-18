# SyndProxy private pool

## Current pool

- Alive now: 872
- Gold now: 347
- HTTP: 256 alive / 67 gold
- HTTPS: 193 alive / 15 gold
- SOCKS4: 220 alive / 142 gold
- SOCKS5: 203 alive / 123 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15245
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
