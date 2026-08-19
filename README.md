# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 535
- HTTP: 365 alive / 163 gold
- HTTPS: 237 alive / 88 gold
- SOCKS4: 198 alive / 140 gold
- SOCKS5: 227 alive / 144 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18649
- Ever gold: 725

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
