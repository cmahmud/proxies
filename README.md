# SyndProxy private pool

## Current pool

- Alive now: 1191
- Gold now: 399
- HTTP: 421 alive / 91 gold
- HTTPS: 298 alive / 14 gold
- SOCKS4: 226 alive / 130 gold
- SOCKS5: 246 alive / 164 gold

## Historical pool

- Discovered: 131850
- Ever alive: 21253
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
