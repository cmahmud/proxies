# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 401
- HTTP: 87 alive / 65 gold
- HTTPS: 74 alive / 20 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 171 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37653
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
