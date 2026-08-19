# SyndProxy private pool

## Current pool

- Alive now: 1251
- Gold now: 530
- HTTP: 455 alive / 183 gold
- HTTPS: 346 alive / 58 gold
- SOCKS4: 206 alive / 124 gold
- SOCKS5: 244 alive / 165 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19662
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
