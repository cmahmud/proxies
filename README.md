# SyndProxy private pool

## Current pool

- Alive now: 771
- Gold now: 392
- HTTP: 197 alive / 77 gold
- HTTPS: 158 alive / 27 gold
- SOCKS4: 204 alive / 132 gold
- SOCKS5: 212 alive / 156 gold

## Historical pool

- Discovered: 150519
- Ever alive: 27055
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
