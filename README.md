# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 401
- HTTP: 94 alive / 60 gold
- HTTPS: 73 alive / 17 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38563
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
