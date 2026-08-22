# SyndProxy private pool

## Current pool

- Alive now: 897
- Gold now: 407
- HTTP: 284 alive / 86 gold
- HTTPS: 167 alive / 25 gold
- SOCKS4: 213 alive / 143 gold
- SOCKS5: 233 alive / 153 gold

## Historical pool

- Discovered: 164921
- Ever alive: 32159
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
