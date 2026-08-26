# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 400
- HTTP: 104 alive / 59 gold
- HTTPS: 67 alive / 13 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 202 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38294
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
