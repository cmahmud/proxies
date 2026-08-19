# SyndProxy private pool

## Current pool

- Alive now: 839
- Gold now: 321
- HTTP: 272 alive / 52 gold
- HTTPS: 168 alive / 11 gold
- SOCKS4: 210 alive / 132 gold
- SOCKS5: 189 alive / 126 gold

## Historical pool

- Discovered: 127417
- Ever alive: 20007
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
