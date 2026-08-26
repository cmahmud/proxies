# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 406
- HTTP: 104 alive / 63 gold
- HTTPS: 55 alive / 20 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38760
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
