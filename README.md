# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 446
- HTTP: 356 alive / 105 gold
- HTTPS: 247 alive / 31 gold
- SOCKS4: 202 alive / 147 gold
- SOCKS5: 274 alive / 163 gold

## Historical pool

- Discovered: 153731
- Ever alive: 28662
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
