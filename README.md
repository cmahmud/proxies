# SyndProxy private pool

## Current pool

- Alive now: 747
- Gold now: 368
- HTTP: 164 alive / 67 gold
- HTTPS: 141 alive / 20 gold
- SOCKS4: 200 alive / 120 gold
- SOCKS5: 242 alive / 161 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26091
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
