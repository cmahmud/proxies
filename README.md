# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 402
- HTTP: 98 alive / 62 gold
- HTTPS: 54 alive / 18 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38960
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
