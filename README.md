# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 344
- HTTP: 335 alive / 67 gold
- HTTPS: 197 alive / 17 gold
- SOCKS4: 251 alive / 137 gold
- SOCKS5: 206 alive / 123 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15343
- Ever gold: 495

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
