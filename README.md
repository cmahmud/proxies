# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 403
- HTTP: 93 alive / 61 gold
- HTTPS: 72 alive / 18 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38580
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
