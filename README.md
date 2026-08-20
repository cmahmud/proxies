# SyndProxy private pool

## Current pool

- Alive now: 717
- Gold now: 386
- HTTP: 196 alive / 73 gold
- HTTPS: 115 alive / 18 gold
- SOCKS4: 212 alive / 154 gold
- SOCKS5: 194 alive / 141 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25621
- Ever gold: 1070

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
