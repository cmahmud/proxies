# SyndProxy private pool

## Current pool

- Alive now: 1231
- Gold now: 530
- HTTP: 446 alive / 186 gold
- HTTPS: 341 alive / 63 gold
- SOCKS4: 203 alive / 122 gold
- SOCKS5: 241 alive / 159 gold

## Historical pool

- Discovered: 125667
- Ever alive: 19605
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
