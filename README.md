# SyndProxy private pool

## Current pool

- Alive now: 1096
- Gold now: 519
- HTTP: 394 alive / 147 gold
- HTTPS: 272 alive / 89 gold
- SOCKS4: 224 alive / 148 gold
- SOCKS5: 206 alive / 135 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17718
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
