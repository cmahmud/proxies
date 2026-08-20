# SyndProxy private pool

## Current pool

- Alive now: 613
- Gold now: 384
- HTTP: 140 alive / 68 gold
- HTTPS: 79 alive / 16 gold
- SOCKS4: 191 alive / 150 gold
- SOCKS5: 203 alive / 150 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25709
- Ever gold: 1072

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
