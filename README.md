# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 406
- HTTP: 86 alive / 62 gold
- HTTPS: 61 alive / 19 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38542
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
