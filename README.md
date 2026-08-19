# SyndProxy private pool

## Current pool

- Alive now: 1221
- Gold now: 397
- HTTP: 425 alive / 90 gold
- HTTPS: 330 alive / 14 gold
- SOCKS4: 226 alive / 130 gold
- SOCKS5: 240 alive / 163 gold

## Historical pool

- Discovered: 131850
- Ever alive: 21255
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
