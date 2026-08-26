# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 402
- HTTP: 104 alive / 60 gold
- HTTPS: 76 alive / 15 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39207
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
