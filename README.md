# SyndProxy private pool

## Current pool

- Alive now: 714
- Gold now: 372
- HTTP: 167 alive / 67 gold
- HTTPS: 124 alive / 22 gold
- SOCKS4: 197 alive / 120 gold
- SOCKS5: 226 alive / 163 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26076
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
