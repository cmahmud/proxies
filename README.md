# SyndProxy private pool

## Current pool

- Alive now: 838
- Gold now: 414
- HTTP: 211 alive / 76 gold
- HTTPS: 168 alive / 25 gold
- SOCKS4: 242 alive / 155 gold
- SOCKS5: 217 alive / 158 gold

## Historical pool

- Discovered: 150519
- Ever alive: 27050
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
