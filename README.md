# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 402
- HTTP: 94 alive / 61 gold
- HTTPS: 85 alive / 14 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39159
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
