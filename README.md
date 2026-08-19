# SyndProxy private pool

## Current pool

- Alive now: 1216
- Gold now: 397
- HTTP: 426 alive / 90 gold
- HTTPS: 321 alive / 14 gold
- SOCKS4: 227 alive / 130 gold
- SOCKS5: 242 alive / 163 gold

## Historical pool

- Discovered: 131850
- Ever alive: 21253
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
