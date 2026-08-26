# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 404
- HTTP: 83 alive / 61 gold
- HTTPS: 59 alive / 18 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38543
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
