# SyndProxy private pool

## Current pool

- Alive now: 734
- Gold now: 379
- HTTP: 207 alive / 73 gold
- HTTPS: 123 alive / 18 gold
- SOCKS4: 212 alive / 150 gold
- SOCKS5: 192 alive / 138 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25617
- Ever gold: 1069

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
