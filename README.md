# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 404
- HTTP: 241 alive / 86 gold
- HTTPS: 113 alive / 16 gold
- SOCKS4: 226 alive / 150 gold
- SOCKS5: 242 alive / 152 gold

## Historical pool

- Discovered: 155739
- Ever alive: 29283
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
