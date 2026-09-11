# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 427
- HTTP: 99 alive / 71 gold
- HTTPS: 64 alive / 26 gold
- SOCKS4: 180 alive / 167 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49055
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
