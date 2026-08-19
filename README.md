# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 316
- HTTP: 306 alive / 55 gold
- HTTPS: 192 alive / 10 gold
- SOCKS4: 212 alive / 123 gold
- SOCKS5: 216 alive / 128 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20133
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
