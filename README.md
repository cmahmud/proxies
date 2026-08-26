# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 404
- HTTP: 113 alive / 66 gold
- HTTPS: 77 alive / 16 gold
- SOCKS4: 182 alive / 158 gold
- SOCKS5: 192 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38743
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
