# SyndProxy private pool

## Current pool

- Alive now: 1132
- Gold now: 593
- HTTP: 370 alive / 193 gold
- HTTPS: 318 alive / 99 gold
- SOCKS4: 210 alive / 146 gold
- SOCKS5: 234 alive / 155 gold

## Historical pool

- Discovered: 138957
- Ever alive: 23451
- Ever gold: 921

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
