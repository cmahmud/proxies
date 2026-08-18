# SyndProxy private pool

## Current pool

- Alive now: 1085
- Gold now: 319
- HTTP: 379 alive / 41 gold
- HTTPS: 211 alive / 11 gold
- SOCKS4: 253 alive / 138 gold
- SOCKS5: 242 alive / 129 gold

## Historical pool

- Discovered: 107044
- Ever alive: 14390
- Ever gold: 442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
