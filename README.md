# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 400
- HTTP: 97 alive / 57 gold
- HTTPS: 88 alive / 15 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39150
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
