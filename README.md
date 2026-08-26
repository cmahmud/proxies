# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 401
- HTTP: 88 alive / 59 gold
- HTTPS: 80 alive / 20 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38514
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
