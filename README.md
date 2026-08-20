# SyndProxy private pool

## Current pool

- Alive now: 680
- Gold now: 348
- HTTP: 173 alive / 63 gold
- HTTPS: 144 alive / 18 gold
- SOCKS4: 173 alive / 130 gold
- SOCKS5: 190 alive / 137 gold

## Historical pool

- Discovered: 146875
- Ever alive: 25756
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
