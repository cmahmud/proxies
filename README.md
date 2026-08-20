# SyndProxy private pool

## Current pool

- Alive now: 674
- Gold now: 380
- HTTP: 174 alive / 65 gold
- HTTPS: 105 alive / 18 gold
- SOCKS4: 200 alive / 150 gold
- SOCKS5: 195 alive / 147 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25704
- Ever gold: 1072

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
