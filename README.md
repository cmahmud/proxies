# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 452
- HTTP: 367 alive / 113 gold
- HTTPS: 227 alive / 34 gold
- SOCKS4: 210 alive / 154 gold
- SOCKS5: 242 alive / 151 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28598
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
