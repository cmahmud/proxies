# SyndProxy private pool

## Current pool

- Alive now: 1125
- Gold now: 399
- HTTP: 399 alive / 92 gold
- HTTPS: 275 alive / 14 gold
- SOCKS4: 210 alive / 130 gold
- SOCKS5: 241 alive / 163 gold

## Historical pool

- Discovered: 131850
- Ever alive: 21250
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
