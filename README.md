# SyndProxy private pool

## Current pool

- Alive now: 763
- Gold now: 406
- HTTP: 206 alive / 82 gold
- HTTPS: 122 alive / 16 gold
- SOCKS4: 193 alive / 148 gold
- SOCKS5: 242 alive / 160 gold

## Historical pool

- Discovered: 155790
- Ever alive: 29319
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
