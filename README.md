# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 407
- HTTP: 111 alive / 61 gold
- HTTPS: 83 alive / 13 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 203 alive / 172 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38216
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
