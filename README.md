# SyndProxy private pool

## Current pool

- Alive now: 772
- Gold now: 385
- HTTP: 209 alive / 77 gold
- HTTPS: 123 alive / 16 gold
- SOCKS4: 216 alive / 142 gold
- SOCKS5: 224 alive / 150 gold

## Historical pool

- Discovered: 147689
- Ever alive: 25969
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
