# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 424
- HTTP: 93 alive / 66 gold
- HTTPS: 46 alive / 28 gold
- SOCKS4: 189 alive / 167 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49045
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
