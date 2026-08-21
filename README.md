# SyndProxy private pool

## Current pool

- Alive now: 1142
- Gold now: 439
- HTTP: 388 alive / 108 gold
- HTTPS: 299 alive / 32 gold
- SOCKS4: 203 alive / 151 gold
- SOCKS5: 252 alive / 148 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28625
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
