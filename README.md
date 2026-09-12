# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 447
- HTTP: 117 alive / 90 gold
- HTTPS: 52 alive / 28 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 176 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49301
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
