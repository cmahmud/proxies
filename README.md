# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 412
- HTTP: 102 alive / 66 gold
- HTTPS: 87 alive / 13 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 204 alive / 171 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38163
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
