# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 406
- HTTP: 278 alive / 83 gold
- HTTPS: 162 alive / 23 gold
- SOCKS4: 204 alive / 154 gold
- SOCKS5: 240 alive / 146 gold

## Historical pool

- Discovered: 165846
- Ever alive: 32376
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
