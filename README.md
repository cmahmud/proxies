# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 401
- HTTP: 97 alive / 59 gold
- HTTPS: 75 alive / 16 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38447
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
