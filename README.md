# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 403
- HTTP: 111 alive / 59 gold
- HTTPS: 68 alive / 18 gold
- SOCKS4: 163 alive / 160 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39001
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
