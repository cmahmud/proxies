# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 408
- HTTP: 108 alive / 67 gold
- HTTPS: 83 alive / 19 gold
- SOCKS4: 181 alive / 158 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38747
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
