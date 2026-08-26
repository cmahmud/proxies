# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 406
- HTTP: 106 alive / 63 gold
- HTTPS: 84 alive / 16 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38326
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
