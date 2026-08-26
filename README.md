# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 403
- HTTP: 98 alive / 64 gold
- HTTPS: 87 alive / 13 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39226
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
