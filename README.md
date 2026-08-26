# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 406
- HTTP: 94 alive / 63 gold
- HTTPS: 69 alive / 19 gold
- SOCKS4: 175 alive / 157 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38521
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
