# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 406
- HTTP: 98 alive / 66 gold
- HTTPS: 78 alive / 20 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 175 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37678
- Ever gold: 1286

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
