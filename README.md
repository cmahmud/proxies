# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 401
- HTTP: 111 alive / 59 gold
- HTTPS: 84 alive / 13 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38262
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
