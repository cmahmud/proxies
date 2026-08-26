# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 403
- HTTP: 107 alive / 61 gold
- HTTPS: 94 alive / 12 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 201 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38243
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
