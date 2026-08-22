# SyndProxy private pool

## Current pool

- Alive now: 941
- Gold now: 420
- HTTP: 303 alive / 85 gold
- HTTPS: 212 alive / 29 gold
- SOCKS4: 199 alive / 141 gold
- SOCKS5: 227 alive / 165 gold

## Historical pool

- Discovered: 163875
- Ever alive: 32025
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
