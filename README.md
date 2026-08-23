# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 380
- HTTP: 95 alive / 64 gold
- HTTPS: 51 alive / 12 gold
- SOCKS4: 158 alive / 150 gold
- SOCKS5: 175 alive / 154 gold

## Historical pool

- Discovered: 174159
- Ever alive: 33076
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
