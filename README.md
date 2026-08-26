# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 404
- HTTP: 108 alive / 62 gold
- HTTPS: 72 alive / 10 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 203 alive / 171 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38216
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
