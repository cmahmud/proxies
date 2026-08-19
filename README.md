# SyndProxy private pool

## Current pool

- Alive now: 1118
- Gold now: 530
- HTTP: 416 alive / 154 gold
- HTTPS: 255 alive / 90 gold
- SOCKS4: 227 alive / 149 gold
- SOCKS5: 220 alive / 137 gold

## Historical pool

- Discovered: 119808
- Ever alive: 18030
- Ever gold: 706

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
