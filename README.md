# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 406
- HTTP: 106 alive / 63 gold
- HTTPS: 71 alive / 15 gold
- SOCKS4: 184 alive / 159 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38400
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
