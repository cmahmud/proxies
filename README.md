# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 434
- HTTP: 92 alive / 74 gold
- HTTPS: 43 alive / 26 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 180 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49156
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
