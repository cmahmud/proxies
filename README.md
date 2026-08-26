# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 403
- HTTP: 93 alive / 61 gold
- HTTPS: 74 alive / 18 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38561
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
