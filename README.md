# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 405
- HTTP: 111 alive / 65 gold
- HTTPS: 60 alive / 19 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38954
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
