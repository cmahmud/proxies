# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 406
- HTTP: 100 alive / 61 gold
- HTTPS: 91 alive / 13 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 197 alive / 171 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38248
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
