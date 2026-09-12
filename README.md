# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 466
- HTTP: 136 alive / 96 gold
- HTTPS: 59 alive / 33 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 196 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49349
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
