# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 424
- HTTP: 90 alive / 68 gold
- HTTPS: 59 alive / 26 gold
- SOCKS4: 190 alive / 167 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49072
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
