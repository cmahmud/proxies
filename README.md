# SyndProxy private pool

## Current pool

- Alive now: 973
- Gold now: 315
- HTTP: 349 alive / 40 gold
- HTTPS: 161 alive / 11 gold
- SOCKS4: 236 alive / 137 gold
- SOCKS5: 227 alive / 127 gold

## Historical pool

- Discovered: 107043
- Ever alive: 14376
- Ever gold: 441

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
