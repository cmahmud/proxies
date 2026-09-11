# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 424
- HTTP: 106 alive / 71 gold
- HTTPS: 46 alive / 21 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48988
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
